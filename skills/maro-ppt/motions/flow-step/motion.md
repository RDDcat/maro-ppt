---
motion: flow-step
label: 흐름 켜기
shows: 이 순서로 넘어간다 — 흐릿하게 깔린 경로가 왼쪽부터 한 칸씩 켜지고 마지막 결과 칸이 자리를 잡는다
when: 순서·인과를 말하는 .flow 장에서, 결과 칸까지 가는 과정이 핵심일 때
target: .flow (또는 .flow 를 감싼 요소)
dur: 칸 수에 따라 (약 1.6초)
---

# 흐름 켜기

처음에 경로 전체가 20% 농도로 보인다 — 청중은 어디로 갈지 먼저 안다.
그다음 칸과 화살표가 왼쪽부터 켜지고, 마지막 `strong`(잉크 칸)은 살짝 작았다가 제 크기로 놓인다.

## 언제 쓰나

**쓴다** — "요청 → 처리 → 결과", "작게 시작 → 커진다" 같은 3칸 흐름.
**쓰지 않는다** — 갈라지거나 되돌아오는 구조(`.dg` 도식이 할 일).

## 붙이는 법

```html
<div class="flow mo" data-motion="flow-step">
  <span>{1단계}</span><i>→</i><span>{2단계}</span><i>→</i><strong>{결과}</strong>
</div>
```

## JS 덩이

```js
(function(){
  const cells=el=>{const f=el.classList.contains('flow')?el:el.querySelector('.flow')||el;
    return [...f.children].filter(n=>!n.hasAttribute('data-mo-gen'))};
  MOTIONS['flow-step']={
    dur:el=>.4+.24*cells(el).length,
    draw(el,t,M){
      const cs=cells(el);
      cs.forEach((n,k)=>{
        const a=.15+k*.24,p=M.seg(t,a,a+.35),last=k===cs.length-1&&n.tagName==='STRONG';
        M.css(n,{opacity:String(M.lerp(.2,1,p)),
          transform:p<1?(last?`scale(${M.lerp(.94,1,p)})`:`translateX(${(1-p)*-8}px)`):'none'});
      });
    }
  };
})();
```

## 지켜야 할 것

- 칸은 3개(화살표 포함 5자식)가 기본이다. 5칸을 넘기면 `.dg` 로 간다.
