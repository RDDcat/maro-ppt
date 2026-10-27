---
motion: stagger
label: 차례로 등장
shows: 하나씩 쌓인다 — 단계가 순서대로 붙고, 카드가 하나씩 놓이고, 대화가 한 마디씩 오간다
when: 나열의 순서 자체가 의미일 때(절차·대화·누적). 순서가 상관없는 나열에는 쓰지 않는다
target: 나열을 감싼 요소 — .steps · .trio · .duo · .kakao 등
dur: 항목 수에 따라 (0.5 + 간격 × (n-1))
---

# 차례로 등장

감싼 요소의 자식(또는 `data-items` 로 지정한 것)이 `data-gap` 초 간격으로 아래에서 떠오른다.
**대화 화면(`.kakao`)에 걸면 말풍선이 한 마디씩 오간다** — 마지막 말풍선이 펀치라인이 되는 순간을 연출할 수 있다.

## 언제 쓰나

**쓴다** — 절차(1→2→3), 대화 재현, "하나 더, 하나 더" 쌓이는 누적.
**쓰지 않는다** — 비교(A/B 는 동시에 봐야 한다), 항목 2개 이하.

## 붙이는 법

```html
<div class="steps mo" data-motion="stagger">…</div>

<!-- 카톡 대화: 말풍선 줄만, 대화처럼 느리게 -->
<div class="kakao mo" data-motion="stagger" data-items=".row" data-gap=".8">…</div>
```

| 속성 | 기본값 | |
|---|---|---|
| `data-items` | 자식 전부 | 차례로 나올 요소의 선택자 |
| `data-gap` | `.35` | 항목 사이 간격(초). 대화는 `.7~.9` |

## JS 덩이

```js
(function(){
  const items=el=>el.dataset.items?[...el.querySelectorAll(el.dataset.items)]
                  :[...el.children].filter(n=>!n.hasAttribute('data-mo-gen'));
  const gap=el=>+el.dataset.gap||.35;
  MOTIONS['stagger']={
    dur:el=>.5+gap(el)*Math.max(0,items(el).length-1),
    draw(el,t,M){
      const g=gap(el);
      items(el).forEach((n,k)=>{const p=M.seg(t,k*g,k*g+.5);
        M.css(n,{opacity:String(p),transform:p<1?`translateY(${(1-p)*14}px)`:'none'})});
    }
  };
})();
```

## 지켜야 할 것

- 항목은 **6개 이하**. 그 이상이면 마지막이 나올 때쯤 청중이 지친다.
- 결론 밴드는 나열 바깥에 둔다 — 밴드까지 차례로 나오면 결론이 늦다.
