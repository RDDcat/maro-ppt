---
motion: kinetic-title
label: 제목 각인
shows: 이 한 문장을 기억하라 — 제목이 아래에서 솟고, 핵심 명사에 형광펜이 그어지고, 리드가 따라온다
when: 덱에서 가장 무거운 문장 하나를 꽂을 때(핵심 주장·결론). 표지와 평범한 본문 제목에는 쓰지 않는다
target: 제목(h1·h2)과 리드를 함께 감싼 요소 — 보통 .copy
dur: 1.5
---

# 제목 각인

제목은 아래에서 마스크를 뚫고 솟고, 그 다음 `.accent` 형광펜이 왼쪽에서 오른쪽으로 그어진다.
나머지 요소(리드·링크)는 0.12초 간격으로 따라온다. **형광펜이 그어지는 순간**이 이 모션의 사건이다.

## 언제 쓰나

**쓴다** — 덱 전체에서 가장 기억시키고 싶은 문장. 한 덱에 **2번까지**.
**쓰지 않는다** — 표지(발표 전에 띄워 두는 화면이라 움직임을 아무도 못 본다). 매 장의 제목 — 모든 제목이 솟으면 아무 제목도 무겁지 않다.

## 붙이는 법

```html
<div class="copy mo" data-motion="kinetic-title">
  <h1>{제목} <span class="accent">{핵심 명사}</span></h1>
  <p class="body">{리드 한 문장}</p>
</div>
```

## JS 덩이

```js
MOTIONS['kinetic-title']={
  dur:el=>1.3+.12*Math.max(1,el.children.length-1),
  draw(el,t,M){
    const h=el.querySelector('h1,h2'),a=h&&h.querySelector('.accent'),
          rest=[...el.children].filter(n=>n!==h&&!n.hasAttribute('data-mo-gen'));
    if(h){const p=M.seg(t,0,.7),q=(1-p)*100;
      M.css(h,p<1?{transform:`translateY(${q}%)`,'clip-path':`inset(0 0 ${q}% 0)`}:{transform:'none','clip-path':'none'})}
    if(a)M.css(a,{'background-repeat':'no-repeat','background-size':`${M.seg(t,.7,1.15,M.ease.inOut)*100}% 100%`});
    rest.forEach((n,k)=>{const p=M.seg(t,.9+k*.12,1.3+k*.12);
      M.css(n,{opacity:String(p),transform:p<1?`translateY(${(1-p)*10}px)`:'none'})});
  }
};
```

## 지켜야 할 것

- `.accent` 는 원래대로 한 장에 한 번. 형광펜이 없으면 솟기만 한다.
- 끝 장면은 원래 마크업과 같다(형광펜 100%, 변형 없음).
