---
motion: count-up
label: 숫자 올리기
shows: 이만큼 바뀌었다 — 큰 숫자가 0에서 실제 값까지 올라간다
when: 수치 대비·결과 장에서 그 숫자 하나가 장의 주인공일 때
target: .stat 을 감싼 요소 (기본으로 .stat strong 을 센다)
dur: 1.4
---

# 숫자 올리기

`.stat strong`(후 값)이 0에서 실제 값까지 올라간다. 접두·접미(`$`, `배`, `%`, `만 원`)와
소수 자릿수, 천 단위 쉼표는 원래 글자 그대로 지킨다. **원래 글자는 건드리지 않고**
그 위에 겹친 사본에서 센다. 다 세면 사본이 사라지고 원래 글자가 남는다.

## 언제 쓰나

**쓴다** — "10배", "3시간 → 12분", "$4,200" 처럼 숫자 하나가 결론일 때.
**쓰지 않는다** — 숫자가 여러 개 늘어선 표, 숫자가 없는 값("절반", "거의 0").

## 붙이는 법

```html
<div class="hero mo" data-motion="count-up">
  <div class="stat"><span>{전}</span><i>→</i><strong>{후}</strong></div>
  …
</div>
```

다른 숫자를 세고 싶으면 `data-items="{선택자}"` 를 준다. 예: 결과 칩들 — `data-items=".breakdown span"`.
숫자가 없는 칩은 그대로 둔다. **시각(`9:36`)·날짜는 세지 않는다** — 첫 숫자만 세서 이상한 값이 지나간다.

## JS 덩이

```js
(function(){
  const parse=s=>{const m=s.match(/-?\d[\d,]*(\.\d+)?/);if(!m)return null;
    return{pre:s.slice(0,m.index),post:s.slice(m.index+m[0].length),
      n:parseFloat(m[0].replace(/,/g,'')),dec:m[1]?m[1].length-1:0,comma:m[0].includes(',')}};
  const fmt=(v,f)=>{let s=v.toFixed(f.dec);if(f.comma)s=s.replace(/\B(?=(\d{3})+(?!\d))/g,',');return f.pre+s+f.post};
  MOTIONS['count-up']={
    dur:1.4,
    init(el,M){
      el._cu=[...el.querySelectorAll(el.dataset.items||'.stat strong')].map(n=>{
        const f=parse(n.textContent.trim());if(!f)return null;
        const box=n.parentElement;
        if(getComputedStyle(box).position==='static')M.css(box,{position:'relative'});
        const g=M.gen(n.cloneNode(true));
        g.style.position='absolute';g.style.margin='0';g.style.whiteSpace='nowrap';
        n.after(g);return{n,g,f};
      }).filter(Boolean);
    },
    draw(el,t,M,dur){
      el._cu.forEach(({n,g,f},k)=>{
        const p=M.seg(t,k*.15,dur-.2+k*.15),done=t>=dur;
        M.css(n,{visibility:done?'visible':'hidden'});
        g.style.display=done?'none':'';
        g.style.left=n.offsetLeft+'px';g.style.top=n.offsetTop+'px';
        g.style.width=n.offsetWidth+'px';g.style.height=n.offsetHeight+'px';g.style.boxSizing='border-box';
        g.textContent=fmt(f.n*p,f);
      });
    }
  };
})();
```

## 지켜야 할 것

- 원래 글자를 바꾸지 않는다 — 편집기가 고치는 건 원래 글자다.
- 사본이 원래 자리에 정확히 겹치는지 `MO.seek(.7)` 로 본다.
