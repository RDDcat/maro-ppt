---
motion: typing
label: 프롬프트 치기
shows: 이걸 그대로 친다 — 프롬프트 블록이 한 글자씩 쳐지고 커서가 따라간다
when: 수강생이 그대로 따라 칠 프롬프트를 보여 주는 장. 덱 전체에서 한 번
target: .prompt 를 감싼 요소
dur: 글자 수에 따라 (최대 6초)
---

# 프롬프트 치기

원래 `.prompt` 를 감춘 채 그 위에 겹친 사본에서 한 글자씩 친다. 라임 커서가 끝을 따라간다.
다 치면 사본이 사라지고 원래 블록이 남는다.

## 언제 쓰나

**쓴다** — "이 문장을 그대로 붙여 넣으세요"가 그 장의 결론일 때. 실제로 치는 감각이 전달된다.
**쓰지 않는다** — 프롬프트가 5줄을 넘을 때(6초 상한에 걸려 너무 빨리 쳐진다), 덱에서 두 번째 프롬프트.

## 붙이는 법

```html
<div class="mo" data-motion="typing">
  <div class="prompt">…</div>
</div>

<!-- .prompt 에 바로 걸어도 된다 -->
<div class="prompt mo" data-motion="typing">…</div>
```

## JS 덩이

```js
MOTIONS['typing']={
  dur:el=>{const s=el.matches('.prompt')?el:el.querySelector('.prompt')||el.firstElementChild;
    return Math.min(6,.8+s.textContent.replace(/\s+/g,' ').trim().length/45)},
  init(el,M){
    const src=el.matches('.prompt')?el:el.querySelector('.prompt')||el.firstElementChild,box=src.parentElement;
    if(getComputedStyle(box).position==='static')M.css(box,{position:'relative'});
    const g=M.gen(src.cloneNode(true));
    g.style.position='absolute';g.style.margin='0';
    src.after(g);
    const ts=[],w=document.createTreeWalker(g,NodeFilter.SHOW_TEXT);let x;
    while(x=w.nextNode())if(x.nodeValue.trim())ts.push({n:x,s:x.nodeValue});
    const c=M.gen(document.createElement('span'));
    c.style.cssText+=';display:inline-block;width:.5em;height:1.05em;vertical-align:-.15em;margin-left:1px;background:var(--lime,#c9f450)';
    el._ty={src,g,ts,c,total:ts.reduce((a,v)=>a+v.s.length,0)};
  },
  draw(el,t,M,dur){
    const {src,g,ts,c,total}=el._ty,done=t>=dur;
    M.css(src,{visibility:done?'visible':'hidden'});
    g.style.display=done?'none':'';
    g.style.left=src.offsetLeft+'px';g.style.top=src.offsetTop+'px';g.style.width=src.offsetWidth+'px';
    let k=Math.round(total*M.seg(t,.2,dur-.2,M.ease.lin)),at=ts[0];
    ts.forEach(v=>{const take=Math.max(0,Math.min(v.s.length,k));v.n.nodeValue=v.s.slice(0,take);
      if(take>0)at=v;k-=v.s.length});
    if(at)at.n.after(c);
  }
};
```

## 지켜야 할 것

- 원래 블록을 바꾸지 않는다. 사본만 친다.
- 커서는 라임 하나. 깜빡임은 넣지 않는다(박자를 흐린다).
