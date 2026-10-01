#!/usr/bin/env python3
"""maro-ppt 저장 서버 — 덱을 고치는 즉시 원본 파일에 저장되게 한다.

브라우저는 file:// 로 연 파일에 스스로 쓸 수 없다. 이 서버로 덱을 열면
편집할 때마다 덱이 PUT 으로 원본을 덮어쓴다. 파일 고르기 창이 없다.

  python3 serve.py --open "덱.html"   # 서버가 없으면 띄우고, 덱을 브라우저로 연다
  python3 serve.py --stop             # 서버 끄기

- 127.0.0.1 에서만 듣는다. 홈 폴더 아래 .html 만 읽고 쓴다.
- 쓰기는 X-Maro 헤더가 있어야 받는다 → 다른 사이트가 몰래 쓸 수 없다(CORS 사전 요청을 허락하지 않는다).
- X-Base-Mtime 이 지금 파일과 다르면(에이전트가 그 사이 고쳤으면) 409 로 거절한다.
  덱은 409 를 받으면 새로고침하고, 저장 안 한 편집을 원래 글자 기준으로 다시 붙여 저장한다.
"""
import http.server, json, os, sys, subprocess, time, urllib.parse, urllib.request, tempfile, signal

PORT = int(os.environ.get("MARO_PPT_PORT", "8765"))
ROOT = os.path.realpath(os.path.expanduser("~"))
PIDFILE = os.path.join(tempfile.gettempdir(), f"maro-ppt-serve-{PORT}.pid")


def resolve(url_path):
    p = os.path.realpath(os.path.join(ROOT, urllib.parse.unquote(url_path.split("?")[0]).lstrip("/")))
    if not (p == ROOT or p.startswith(ROOT + os.sep)) or not p.lower().endswith((".html", ".htm")):
        return None
    return p


def mtime(p):
    return int(os.stat(p).st_mtime_ns // 1_000_000)


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body=b"", ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == "/__maro/ping":
            return self.send(200, {"ok": True, "root": ROOT})
        if u.path == "/__maro/stat":
            p = resolve(urllib.parse.parse_qs(u.query).get("p", [""])[0])
            if not p or not os.path.isfile(p):
                return self.send(404, {"error": "not found"})
            return self.send(200, {"mtime": mtime(p)})
        p = resolve(u.path)
        if not p or not os.path.isfile(p):
            return self.send(404, b"not found", "text/plain")
        with open(p, "rb") as f:
            self.send(200, f.read(), "text/html; charset=utf-8")

    def do_PUT(self):
        if self.headers.get("X-Maro") != "1":
            return self.send(403, {"error": "X-Maro header required"})
        p = resolve(urllib.parse.urlparse(self.path).path)
        if not p or not os.path.isfile(p):
            return self.send(404, {"error": "not found"})
        base = self.headers.get("X-Base-Mtime")
        if base and base != "0" and int(base) != mtime(p):
            return self.send(409, {"error": "changed on disk", "mtime": mtime(p)})
        n = int(self.headers.get("Content-Length", "0"))
        data = self.rfile.read(n)
        if not data.strip():
            return self.send(400, {"error": "empty"})
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), prefix=".maro-", suffix=".tmp")
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, p)
        self.send(200, {"mtime": mtime(p)})


def running():
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/__maro/ping", timeout=1) as r:
            return json.load(r).get("ok")
    except Exception:
        return False


def url_for(path):
    p = os.path.realpath(path)
    if not p.startswith(ROOT + os.sep):
        sys.exit(f"홈 폴더 밖의 파일은 열 수 없습니다: {p}")
    rel = os.path.relpath(p, ROOT)
    return f"http://127.0.0.1:{PORT}/" + "/".join(urllib.parse.quote(s) for s in rel.split(os.sep))


def main():
    a = sys.argv[1:]
    if a[:1] == ["--serve"]:
        with open(PIDFILE, "w") as f:
            f.write(str(os.getpid()))
        http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    elif a[:1] == ["--stop"]:
        try:
            os.kill(int(open(PIDFILE).read()), signal.SIGTERM)
            print("stopped")
        except Exception:
            print("not running")
    elif a[:1] == ["--open"] and len(a) == 2:
        if not running():
            subprocess.Popen([sys.executable, os.path.abspath(__file__), "--serve"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            for _ in range(50):
                if running():
                    break
                time.sleep(0.1)
        u = url_for(a[1])
        print(u)
        if sys.platform == "darwin":
            subprocess.run(["open", u])
        else:
            import webbrowser
            webbrowser.open(u)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
