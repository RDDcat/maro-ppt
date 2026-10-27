---
motion: cycle
label: 도는 고리
shows: 이건 한 바퀴로 끝나지 않는다 — 3~4단계가 고리로 놓이고, 표시점이 고리를 계속 돌며 지금 단계를 짚는다
when: 반복 루프 자체가 말일 때(만들기 → 확인 → 고치기, 에이전트 루프, 학습 사이클)
target: .cycle
dur: 약 1.2초 + 반복
loop: 있음 — 표시점이 4.8초에 한 바퀴, 지나가는 단계 상자에 라임 테두리
---

# 도는 고리

단계 상자 3~4개가 타원 고리 위에 차례로 놓이고, 끝 장면 뒤로 **표시점이 고리를 따라 천천히 돈다.**
표시점이 지나는 상자에는 라임 테두리가 잠깐 켜진다 — "지금 이 단계"를 짚는 손가락이다.

## 언제 쓰나

**쓴다** — 끝이 처음으로 돌아가는 구조. "한 번에 안 되고 돈다"가 메시지일 때.
**쓰지 않는다** — 처음과 끝이 다른 순서(`flow-step` · `packet-flow`). 단계 5개 이상(고리가 읽히지 않는다).

## CSS — `<style>` 맨 아래

```css
/* ── 모션: 고리 ───────────────────────────────── */
.cycle{position:relative;height:400px;width:100%;max-width:640px;margin:0 auto}
.cy-ring{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.cy-ring ellipse{fill:none;stroke:var(--line);stroke-width:2;vector-effect:non-scaling-stroke}
.cy-node{position:absolute;z-index:1;transform:translate(-50%,-50%);width:180px;padding:12px 14px;
  background:#fff;border:1px solid var(--line);text-align:center}
.cy-node p{margin:0;font-size:16px;font-weight:850;color:var(--ink);letter-spacing:-.03em}
.cy-node small{display:block;margin-top:4px;font-size:12px;line-height:1.4;color:var(--muted)}
.cycle[data-n="4"] .cy-node:nth-of-type(1){left:50%;top:12%}
.cycle[data-n="4"] .cy-node:nth-of-type(2){left:88%;top:50%}
.cycle[data-n="4"] .cy-node:nth-of-type(3){left:50%;top:88%}
.cycle[data-n="4"] .cy-node:nth-of-type(4){left:12%;top:50%}
.cycle[data-n="3"] .cy-node:nth-of-type(1){left:50%;top:12%}
.cycle[data-n="3"] .cy-node:nth-of-type(2){left:82.9%;top:69%}
.cycle[data-n="3"] .cy-node:nth-of-type(3){left:17.1%;top:69%}
.cy-core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);margin:0;max-width:170px;
  text-align:center;font-size:14px;font-weight:800;color:var(--muted)}
.cycle .cy-dot{position:absolute;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;
  background:var(--lime);outline:1px solid var(--ink)}
@media(max-width:600px){.cycle{height:360px}.cy-node{width:128px;padding:9px}}
```

## 마크업 — `data-n` 은 상자 수(3 또는 4), 상자는 시계 방향으로 12시부터

```html
<div class="cycle mo" data-motion="cycle" data-n="4">
  <svg class="cy-ring" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><ellipse cx="50" cy="50" rx="38" ry="38"/></svg>
  <div class="cy-node"><p>{단계}</p><small>{한 줄}</small></div>
  <div class="cy-node"><p>{단계}</p><small>{한 줄}</small></div>
  <div class="cy-node"><p>{단계}</p><small>{한 줄}</small></div>
  <div class="cy-node"><p>{단계}</p><small>{한 줄}</small></div>
  <p class="cy-core">{고리 이름 한 줄}</p>
</div>
```

## JS 덩이

```js
(function(){
  const nodes=el=>[...el.querySelectorAll(':scope>.cy-node')];
  const ang=(k,n)=>-Math.PI/2+2*Math.PI*k/n;               /* 12시부터 시계 방향 */
  MOTIONS['cycle']={
    dur:1.2,
    init(el,M){const d=M.gen(document.createElement('i'));d.className='cy-dot';d.style.opacity='0';el.append(d);el._cy=d},
    draw(el,t,M){
      const ring=el.querySelector('.cy-ring'),ns=nodes(el);
      if(ring)M.css(ring,{opacity:String(M.seg(t,0,.5))});
      ns.forEach((n,k)=>{const a=.15+k*.2,p=M.seg(t,a,a+.4);
        M.css(n,{opacity:String(p),transform:`translate(-50%,-50%)`+(p<1?` scale(${M.lerp(.92,1,p)})`:''),'box-shadow':'','border-color':''})});
      const c=el.querySelector('.cy-core');if(c)M.css(c,{opacity:String(M.seg(t,.8,1.2))});
      el._cy.style.opacity='0';
    },
    /* 반복 — 한 칸에 1.2초. 표시점이 가까운 상자에 라임 테두리 */
    loop(el,u,M){
      const ns=nodes(el),n=ns.length;if(!n)return;
      const w=el.offsetWidth,h=el.offsetHeight,P=1.2*n,a=ang(0,1)+2*Math.PI*(u%P)/P,amp=M.seg(u,0,.8);
      el._cy.style.left=w*(.5+.38*Math.cos(a))+'px';el._cy.style.top=h*(.5+.38*Math.sin(a))+'px';
      el._cy.style.opacity=String(amp);
      ns.forEach((nd,k)=>{let d=Math.abs(((a-ang(k,n))%(2*Math.PI)+3*Math.PI)%(2*Math.PI)-Math.PI);
        const on=amp*M.ease.out(M.clamp(1-d/.7));             /* 표시점이 상자 뒤를 지나는 동안 라임 테두리 */
        M.css(nd,{'border-color':on>.5?'var(--ink)':'','box-shadow':on>.02?`0 0 0 ${(4*on).toFixed(2)}px var(--lime)`:''})});
    }
  };
})();
```

## 지켜야 할 것

- 한 바퀴 4.8초(상자 4개). 빠르면 시계가 아니라 경고등이 된다.
- 표시점과 테두리 말고는 반복하지 않는다. 글자·상자 위치는 고정.
- `data-n` 과 실제 상자 수가 같아야 자리가 맞는다.
