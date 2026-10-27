---
motion: bar-grow
label: 막대 자라기
shows: 무엇이 얼마나 큰가 — 가로 막대가 차례로 자라고 값이 따라붙는다. 맨 위 막대가 결론이다
when: 항목 3~7개의 크기를 견줄 때(분포·순위·구성). 두 숫자만 비교하면 .stat 이 낫다
target: .bars
dur: 막대 수에 따라 (약 1.4초)
loop: 없음 — 크기는 한 번 보이면 끝이다
---

# 막대 자라기

정적인 HTML 막대그래프(`.bars`)를 이 모션이 왼쪽에서 자라게 한다. 막대는 위에서부터 0.12초 간격으로 자라고,
막대가 다 자란 뒤 값이 나타난다. **반복하지 않는다** — 크기는 계속 움직일 이유가 없다.

## 언제 쓰나

**쓴다** — "11편 중 제품 UI가 가장 많다"처럼 분포의 모양 자체가 말일 때.
**쓰지 않는다** — 항목 2개(`.stat`), 8개 이상(표가 낫다), 시간에 따른 추이(선이 필요하다).

## CSS — `<style>` 맨 아래

```css
/* ── 모션: 막대 그래프 ─────────────────────────── */
.bars{display:grid;gap:10px}
.bars .bar{display:grid;grid-template-columns:120px 1fr;align-items:center;gap:14px}
.bars .bar p{margin:0;font-size:14px;font-weight:800;color:var(--ink);text-align:right}
.bars .track{display:flex;align-items:center;gap:9px}
.bars .track i{display:block;flex:none;height:24px;background:#c9cec8;transform-origin:left center;
  width:calc(var(--v) / var(--max,100) * (100% - 48px))}
.bars .bar.top .track i{background:var(--ink)}
.bars .track b{font-size:15px;font-weight:850;color:var(--ink)}
@media(max-width:600px){.bars .bar{grid-template-columns:84px 1fr}}
```

## 마크업

`--max` 는 가장 큰 값. `--v` 와 `<b>` 의 숫자는 같아야 한다(막대 길이는 `--v` 가 정한다).

```html
<div class="bars mo" data-motion="bar-grow" style="--max:11">
  <div class="bar top" style="--v:11"><p>{항목}</p><span class="track"><i></i><b>11</b></span></div>
  <div class="bar" style="--v:9"><p>{항목}</p><span class="track"><i></i><b>9</b></span></div>
  …
</div>
<div class="band">{이 분포가 말하는 것 한 줄}</div>
```

## JS 덩이

```js
MOTIONS['bar-grow']={
  dur:el=>.8+.12*Math.max(0,el.querySelectorAll('.bar').length-1),
  draw(el,t,M){
    el.querySelectorAll('.bar').forEach((b,k)=>{
      const a=k*.12,p=M.seg(t,a,a+.6,M.ease.inOut),q=M.seg(t,a+.45,a+.75);
      const i=b.querySelector('.track i'),v=b.querySelector('.track b');
      if(i)M.css(i,{transform:p<1?`scaleX(${p})`:'none'});
      if(v)M.css(v,{opacity:String(q)});
      M.css(b.querySelector('p')||b,{opacity:String(M.lerp(.35,1,M.seg(t,a,a+.3)))});
    });
  }
};
```

## 지켜야 할 것

- 값 글자 `<b>` 는 편집 대상이 아니다. 값을 바꾸면 `--v` 도 같이 바꾼다.
- 막대 색은 회색과 잉크(결론 막대 하나)뿐. 라임은 제목 형광펜 몫이다.
