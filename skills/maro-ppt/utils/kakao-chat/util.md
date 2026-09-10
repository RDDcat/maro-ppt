---
util: kakao-chat
label: 카카오톡 채팅 화면
shows: 주고받은 대화 — 누가 말했는지, 어떤 순서였는지, 그때의 온도
when: 상황을 재현해야 할 때 · 실패나 오해가 대화 속에서 드러날 때 · 청중이 겪어 본 장면을 되살릴 때
slot: .two 오른쪽 열 · .one 전폭(이때는 max-width 560px 로 가운데)
needs: 메시지 3~6개 (누가 / 무슨 말)
---

# 카카오톡 채팅 화면

말로 설명하면 한 문단이 필요한 상황을, **그 상황이 실제로 벌어진 대화**로 보여 준다.

> "링크를 보냈는데 상대가 못 연다" → 설명하지 말고, 그 카톡을 그대로 보여 준다.

라이트 모드(푸른빛 회색 바탕 · 노란 말풍선)로 그린다. 사람들이 아는 그 화면이다.

---

## 1. 언제 쓰나

**쓴다**

- 실패·오해가 **대화 속에서** 드러날 때 (링크가 안 열린다, 요구사항이 어긋난다)
- 청중이 겪어 봤을 장면을 되살릴 때 — 도입 장에서 특히 강하다
- "이런 요청이 들어온다"를 인용할 때. 카드에 따옴표로 적는 것보다 훨씬 빠르게 읽힌다

**쓰지 않는다**

- 개념을 **정의**하는 장. 정의는 대화로 안 된다
- 수치를 비교하는 장. `.stat` 이 할 일이다
- 한 덱에 **두 번을 넘기지 않는다.** 세 번째부터는 밈이 아니라 습관으로 보인다

---

## 2. 붙이는 법

### CSS — `<style>` 맨 아래에 붙인다

스타일 고유 CSS 뒤에 와야 `.card p` 같은 규칙을 덮는다.

```css
/* ── 유틸: 카카오톡 채팅 화면 ─────────────────────── */
.kakao{background:#b2c7d9;border:1px solid var(--line);overflow:hidden}
.kakao .k-head{display:flex;align-items:center;gap:7px;padding:9px 12px;
  background:#a3b9cc;border-bottom:1px solid rgba(0,0,0,.09)}
.kakao .k-head p{margin:0;font-size:12px;font-weight:850;color:#1f2d3a;letter-spacing:-.02em}
.kakao .k-log{padding:14px 12px 16px;display:flex;flex-direction:column;gap:9px}
.kakao .k-day{align-self:center;background:rgba(255,255,255,.55);color:#33475a;
  font-size:10px;font-weight:800;padding:3px 11px;border-radius:999px;margin-bottom:2px}
.kakao .row{display:flex;align-items:flex-end;gap:6px}
.kakao .row.me{justify-content:flex-end}
.kakao .k-av{width:26px;height:26px;border-radius:9px;background:#8fa6b8;flex:none}
.kakao .b{position:relative;max-width:74%;margin:0;background:#fff;color:#101820;
  font-size:13.5px;line-height:1.42;font-weight:700;padding:8px 11px;border-radius:4px;
  letter-spacing:-.02em;word-break:break-all}
.kakao .row.me .b{background:#FEE500;color:#181600}
.kakao .b::after{content:'';position:absolute;top:8px;left:-5px;
  border:5px solid transparent;border-left:0;border-right-color:#fff}
.kakao .row.me .b::after{left:auto;right:-5px;border-right:0;
  border-left:5px solid #FEE500;border-right-color:transparent}
.kakao .t{display:block;font-size:9.5px;font-weight:800;color:#4d6272;
  line-height:1.3;white-space:nowrap;padding-bottom:2px}
.kakao .row.me .t{order:-1}
.kakao.wide{max-width:560px;margin:0 auto}
@media(max-width:600px){.kakao .b{max-width:82%}}
```

### 마크업 — `.two` 오른쪽 열

```html
<div>
  <div class="kakao">
    <div class="k-head"><p>{상대 이름}</p></div>
    <div class="k-log">
      <span class="k-day">{날짜}</span>

      <div class="row me">
        <small class="t">{시간}</small>
        <p class="b">{내가 한 말}</p>
      </div>

      <div class="row">
        <div class="k-av"></div>
        <p class="b">{상대가 한 말}</p>
        <small class="t">{시간}</small>
      </div>
    </div>
  </div>
  <div class="band">{이 대화가 말하는 것 한 줄}</div>
</div>
```

`.one` 전폭에 놓을 때는 `<div class="kakao wide">` 로 폭을 잡는다.

---

## 3. 대사 쓰는 법

**대사는 담백하게 쓰지 않는다.** 덱 본문의 문장 규칙(과장 금지·이모지 금지)은 여기 적용되지 않는다.
인용된 대화는 **실제로 사람이 그렇게 말하는 대로** 적어야 재현이 된다.
`ㅋㅋㅋ`, 오타, 줄임말, 물음표를 그대로 쓴다. 다듬으면 밈이 죽는다.

- 메시지는 **3~5개**. 6개를 넘으면 읽다가 슬라이드가 끝난다
- **마지막 말풍선이 펀치라인**이다. 문제가 터지는 지점에서 끊는다
- 시간은 실제처럼 1~3분 간격으로. 다 같은 시간이면 가짜로 보인다
- 이름은 실명을 쓰지 않는다. 관계로 부른다 (`팀장님`, `친구`, `클라이언트`)

---

## 4. 지켜야 할 것

| | |
|---|---|
| 글자는 `<p class="b">` 와 `<small class="t">` 안에 | 인라인 편집 대상 선택자가 `p` 와 `small` 이라 그대로 고칠 수 있다 |
| 이미지·이모지 파일 금지 | 프로필은 CSS 색 사각형(`.k-av`)이다. 외부 요청 0건 원칙 |
| SVG `<text>` 금지 | 이 유틸은 SVG를 쓰지 않는다 |
| **결론 밴드로 닫는다** | 채팅만 놓고 넘어가지 않는다. 그 대화가 무엇을 말하는지 한 줄 |

**둥근 모서리와 노란색은 여기서만 허용된다.** 카톡 화면은 *덱의 스타일이 아니라 인용된 제품의 스타일*이다.
덱 자신의 카드·밴드는 여전히 각지고, 강조색은 여전히 라임 하나다.

---

## 5. 완성 예 — "링크를 보냈는데 안 열린다"

배포를 설명하는 덱의 도입 장이다. localhost 주소를 그대로 보내는 장면.

```html
<div>
  <div class="kakao">
    <div class="k-head"><p>친구</p></div>
    <div class="k-log">
      <span class="k-day">오늘</span>
      <div class="row me">
        <small class="t">8:43</small>
        <p class="b">야 나 웹만들어봄ㅋㅋㅋ쉽던데?</p>
      </div>
      <div class="row">
        <div class="k-av"></div>
        <p class="b">오 ㅋㅋㅋ 함보자 링크 보내봐바</p>
        <small class="t">8:44</small>
      </div>
      <div class="row me">
        <small class="t">8:45</small>
        <p class="b">http://127.0.0.1:5500/index.html</p>
      </div>
      <div class="row">
        <div class="k-av"></div>
        <p class="b">어 안 열리는데?</p>
        <small class="t">8:47</small>
      </div>
    </div>
  </div>
  <div class="band">127.0.0.1 은 '내 컴퓨터'라는 뜻이다</div>
</div>
```

마지막 말풍선이 펀치라인이다. 여기서 끊고, 밴드가 이유를 말한다.
