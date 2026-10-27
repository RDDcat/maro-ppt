---
motion: packet-flow
label: 흘러가는 패킷
shows: 이 길로 계속 흘러간다 — 단계 상자들이 놓이고, 그 사이 레일을 작은 패킷이 끊임없이 지나간다
when: 요청·데이터·작업이 파이프라인을 계속 통과하는 구조(배포 파이프라인, 렌더 파이프라인, 요청 → 서버 → 응답)
target: .pipe
dur: 상자 수에 따라 (약 1초) + 반복
loop: 있음 — 패킷 3개가 레일을 따라 계속 지나간다
---

# 흘러가는 패킷

상자(단계)가 왼쪽부터 놓이고, 끝 장면 뒤로 **라임 패킷 3개가 상자 아래 레일을 따라 계속 흐른다.**
패킷이 지나가는 상자는 밑변에 라임 줄이 잠깐 켜진다 — 상자가 패킷을 받아 넘기는 것처럼 읽힌다.

`.flow`(3칸, 한 번에 이해)와 달리 **"이건 한 번이 아니라 계속 돌아가는 길이다"** 가 말일 때 쓴다.

## 언제 쓰나

**쓴다** — 매번 같은 길을 지나는 것: 커밋이 배포까지 가는 길, 프롬프트가 영상이 되는 길.
**쓰지 않는다** — 한 번 일어나고 끝나는 순서(`flow-step`), 갈라지는 구조(`.dg`).

## CSS — `<style>` 맨 아래

```css
/* ── 모션: 파이프라인 ──────────────────────────── */
.pipe{position:relative;display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:28px;align-items:stretch;padding-bottom:26px}
.pipe::before{content:'';position:absolute;left:8%;right:8%;bottom:8px;height:2px;background:var(--line)}
.pipe-node{position:relative;z-index:1;background:#fff;border:1px solid var(--line);padding:16px 14px}
.pipe-node p{margin:0;font-size:16px;font-weight:850;color:var(--ink);letter-spacing:-.03em}
.pipe-node small{display:block;margin-top:5px;font-size:12.5px;line-height:1.45;color:var(--muted)}
.pipe-node.ink{background:var(--ink);border-color:var(--ink)}
.pipe-node.ink p{color:#fff}.pipe-node.ink small{color:#b9c4bd}
.pipe .pk{position:absolute;width:9px;height:9px;margin:-4.5px 0 0 -4.5px;background:var(--lime);
  outline:1px solid var(--ink);z-index:0}
@media(max-width:900px){.pipe{grid-auto-flow:row;gap:14px;padding:0 0 0 26px}
  .pipe::before{left:8px;right:auto;top:6%;bottom:6%;width:2px;height:auto}}
```

## 마크업 — 상자 3~5개, 마지막이 결과(`.ink`)

```html
<div class="pipe mo" data-motion="packet-flow">
  <div class="pipe-node"><p>{단계}</p><small>{한 줄}</small></div>
  <div class="pipe-node"><p>{단계}</p><small>{한 줄}</small></div>
  <div class="pipe-node ink"><p>{결과}</p><small>{한 줄}</small></div>
</div>
```

## JS 덩이

```js
(function(){
  const nodes=el=>[...el.querySelectorAll(':scope>.pipe-node')];
  MOTIONS['packet-flow']={
    dur:el=>.5+.18*nodes(el).length,
    init(el,M){el._pk=[0,1,2].map(()=>{const d=M.gen(document.createElement('i'));d.className='pk';d.style.opacity='0';el.append(d);return d})},
    draw(el,t,M){
      nodes(el).forEach((n,k)=>{const p=M.seg(t,k*.18,k*.18+.45);
        M.css(n,{opacity:String(p),transform:p<1?`translateY(${(1-p)*12}px)`:'none','box-shadow':''})});
      el._pk.forEach(d=>d.style.opacity='0');               /* 끝 장면에는 패킷이 없다 */
    },
    /* 반복 — 패킷 3개가 상자 아래 레일을 첫 상자 가운데에서 마지막 상자 가운데로. 한 칸에 0.9초 */
    loop(el,u,M){
      const ns=nodes(el),a=ns[0],b=ns[ns.length-1];if(!a||!b)return;
      const col=b.offsetTop>a.offsetTop+10,                  /* 좁은 화면 — 세로 레일 */
            c=n=>col?n.offsetTop+n.offsetHeight/2:n.offsetLeft+n.offsetWidth/2,
            rail=col?8:el.offsetHeight-8,P=.9*(ns.length-1),amp=M.seg(u,0,.8),hit=ns.map(()=>0);
      el._pk.forEach((d,k)=>{
        const f=((u/P)+k/3)%1,edge=Math.min(f/.06,(1-f)/.06,1),x=M.lerp(c(a),c(b),f);
        d.style.left=(col?rail:x)+'px';d.style.top=(col?x:rail)+'px';
        d.style.opacity=String(amp*edge);
        ns.forEach((n,j)=>{hit[j]=Math.max(hit[j],amp*edge*M.clamp(1-Math.abs(x-c(n))/(col?n.offsetHeight:n.offsetWidth)*2))});
      });
      ns.forEach((n,j)=>M.css(n,{'box-shadow':hit[j]>.02?`inset 0 -${(3*hit[j]).toFixed(2)}px 0 var(--lime)`:''}));
    }
  };
})();
```

## 지켜야 할 것

- 패킷은 3개, 라임 사각형 하나뿐. 상자 밑변 라임 줄은 패킷이 그 상자 아래를 지날 때만. 꼬리·빛 번짐·속도 변화 없음 — 일정한 속도가 "계속"을 말한다.
- 상자 글자는 움직이지 않는다. 반복하는 것은 패킷뿐이다.
