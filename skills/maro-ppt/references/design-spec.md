# 최소 덱(Minimal Deck) 디자인 정의서

> 출처: 실제 세미나 덱 한 편(15장)에서 규칙을 뽑아낸 것입니다.
> 이 문서는 그 덱에서 **재사용 가능한 규칙만** 뽑아 정리한 것입니다.
> 그 발표의 내용·문구·스크린샷은 이 시스템에 속하지 않습니다.

---

## 0. 한 줄 정의

**화면이 아니라 종이처럼 보이는 덱.**
아이보리 종이 위에 흰 카드를 얹고, 선과 여백으로 나누고,
형광펜 한 획(라임)과 잉크 밴드 한 줄로만 강조합니다.

이 인상을 만드는 것은 세 가지입니다.

| | |
|---|---|
| **따뜻한 종이 바탕** | `#f4f1e9` — 흰 배경이 아닙니다. 이게 절반입니다. |
| **각진 면** | 구조 요소의 `border-radius`는 **0**. 그림자도 없습니다. |
| **형광펜 한 획** | 제목의 핵심 명사에만 라임 하이라이트. 한 장에 한 번. |

---

## 1. 색

### 1-1. 토큰

```css
:root{
  --ink:   #17231d;  /* 본문 글자 · 다크 밴드 바탕 — 검정이 아닌 짙은 초록빛 */
  --muted: #65716a;  /* 보조 글자 · 설명문 · 화살표 */
  --paper: #f4f1e9;  /* 덱 바탕 — 아이보리 */
  --white: #fff;     /* 카드 면 */
  --lime:  #c9f450;  /* 강조 1개 — 하이라이트 · 결론 밴드 · 프롬프트 레일 */
  --blue:  #337fe5;  /* 예시 UI의 액션색 (덱의 색이 아니라 "보여주는 제품"의 색) */
  --red:   #c74740;  /* before 수치 */
  --green: #167746;  /* 체크 · after 수치 */
  --line:  #d4d8d0;  /* 1px 경계선 */
}
```

### 1-2. 토큰이 아닌 보조 회색

원본에서 반복해 쓰인 값입니다. 새로 만들 때는 아래 5개만 씁니다.

| 값 | 용도 |
|---|---|
| `#eef1ec` | 사각 라벨·흐름 칸의 옅은 바탕 |
| `#f8f7f2` | 카드 안 한 단 낮은 면 |
| `#e9ece8` | 빈 진행 막대·목업 선 |
| `#c5cec8` | **잉크 바탕 위의** 보조 글자 |
| `#132019` | 프롬프트 블록 바탕 (잉크보다 한 단 더 어두움) |

### 1-3. 사용 규칙

- **강조색은 라임 하나.** 파랑·빨강·초록은 *덱의 색이 아니라* 슬라이드 안에 그려 넣은 **예시 UI의 색**입니다. 제목·본문·장식에 쓰지 않습니다.
- **라임 위의 글자는 항상 `--ink`.** 라임 위에 흰 글자를 얹지 않습니다.
- **잉크 위의 글자는 `#fff` 또는 `#c5cec8`.** 그 위의 강조 숫자만 라임.
- before/after 수치에만 빨강·초록을 씁니다. 그 외 의미색 금지.

---

## 2. 타이포그래피

```css
font-family: Arial, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
word-break: keep-all;      /* 한국어 어절 단위 줄바꿈 */
overflow-wrap: normal;
line-break: strict;
```

웹폰트를 쓰지 않습니다. 라틴은 Arial, 한글은 시스템 고딕이 받습니다.

### 2-1. 크기 스케일

| 역할 | 값 | 비고 |
|---|---|---|
| 표지 h1 | `clamp(50px, 5.7vw, 78px)` / 1.04 | |
| 슬라이드 h1 | `clamp(45px, 5vw, 70px)` / 1.07 | 줄 수는 자유 |
| 밀도 높은 슬라이드 h1 | `clamp(33px, 3vw, 43px)` | 오른쪽 도해가 클 때 |
| h2 | `clamp(35px, 4vw, 55px)` / 1.12 | 1단 슬라이드 |
| h3 (카드 제목) | `24~26px` | |
| 리드 본문 `.body` | `18px` / 1.65, `--muted`, `max-width:740px` | 표지만 21px |
| 카드 본문 | `15px` / 1.55~1.65, `--muted` | |
| ~~사각 라벨·칩~~ | ~~`11~13px`~~ | 폐기 — 6-4 참고 |
| 브랜드·키커 | `11px`, `letter-spacing:.14em` | |

- 제목 자간은 **`-.048em`**. 이 음수 자간이 제목의 밀도를 만듭니다. 빼면 인상이 무너집니다.
- 페이지 카운터·토큰 값·프롬프트는 `ui-monospace`.

### 2-2. 굵기

**700 / 800 / 850** 세 단계만 씁니다. 900은 쓰지 않습니다.

| 굵기 | 용도 |
|---|---|
| 700 | 카운터·모노 값 |
| 800 | 소제목·라벨·버튼 |
| **850** | 결론 문장·키커·강조 숫자 — 이 덱의 "굵게"는 850입니다 |

### 2-3. 한국어 줄바꿈 — `.nowrap`

제목을 여러 줄로 쓸 때는 자동 줄바꿈에 맡기지 않고 **의미 단위로 직접 끊습니다.**
한 줄 제목이면 `.nowrap` 없이 그냥 씁니다.

```html
<h1><span class="nowrap">둘은 똑같아 보이는데</span><br>
    <span class="accent nowrap">왜 하나는 수정이 더 쉬울까?</span></h1>
```

`.nowrap{white-space:nowrap}` 이고, 600px 이하에서 `white-space:normal`로 풀립니다.
어절이 어색하게 끊기는 것을 막는 장치입니다. **직접 끊은 줄에만 적용합니다.**

---

## 3. 레이아웃 골격

```
┌──────────────────────────────────────────┐
│ BRAND                            01 / 15 │  header
├──────────────────────────────────────────┤
│                                          │
│   [ copy .9fr ]   gap 5vw  [ visual 1.1fr ]│  1fr, 세로 중앙
│                                          │
├──────────────────────────────────────────┤
│ ▬▬▬▬▬▭▭▭▭  ← → · SPACE        (←) (→)   │  footer
└──────────────────────────────────────────┘
```

```css
.deck{height:100%;min-height:640px;padding:26px 4.5vw 20px;
      display:grid;grid-template-rows:auto 1fr auto;background:var(--paper)}
.slide{display:none;width:min(1280px,100%);margin:auto;align-items:center;gap:5vw}
.slide.active{display:grid;animation:enter .3s ease-out}
.one{grid-template-columns:1fr}          /* 도해가 가로로 넓을 때 */
.two{grid-template-columns:.9fr 1.1fr}   /* 기본: 왼쪽 말, 오른쪽 그림 */
```

- 캔버스를 1280×720으로 고정하지 않습니다. **뷰포트를 꽉 채우고** 안쪽 폭만 1280으로 제한합니다.
- `.two`가 기본. 왼쪽은 항상 `제목 + 리드 한 문장`, 오른쪽은 그 문장의 **증거 도해**.
- `.one`은 3~5칸짜리 가로 흐름을 놓을 때만.
- 전환 애니메이션은 하나뿐: `opacity 0→1, translateY(8px)→0`, `.3s ease-out`.

### 헤더·푸터

| 요소 | 규격 |
|---|---|
| 브랜드 | 11px / 850 / `.14em` 자간 / 대문자 영문 |
| 카운터 | `700 12px ui-monospace`, `--muted`, `01 / 15` (2자리 패딩) |
| 진행 막대 | 높이 **2px**, 바탕 `#d8dcd4`, 채움 `--ink` |
| 힌트 | 11px `#8a928e`, `← → · SPACE` (600px 이하 숨김) |
| 이동 버튼 | 38px 원형, 배경 없음, 비활성 `opacity:.25` |

---

## 4. 시그니처 장치 7개

이 7개가 "이 덱처럼 보이는가"를 결정합니다.

### ① 형광펜 하이라이트 `.accent`

```css
.accent{background:linear-gradient(transparent 64%, var(--lime) 64%)}
```

글자 아래 36%만 라임이 지나갑니다. **제목에서 핵심 명사에 해당하는 부분**에 겁니다.
한 슬라이드에 **한 번만**. 두 번 쓰면 강조가 사라집니다.

마무리 문장에는 변형을 씁니다: `border-bottom:7px solid var(--lime)`.

### ② 잉크 결론 밴드

도해 **맨 아래**에 붙여 그 도해가 말하려는 결론을 한 줄로 못 박습니다.

```css
.band{padding:16px 20px;background:var(--ink);color:#fff;
      display:flex;justify-content:space-between;align-items:center;
      font-weight:850}
.band b{color:var(--lime);font-size:25px}   /* 숫자 하나만 라임 */
```

### ③ 라임 결론 밴드

같은 자리, 다른 온도. 경고·비용·전제를 말할 때.

```css
.band.lime{background:var(--lime);color:var(--ink);
           text-align:center;font-size:15~17px;font-weight:850}
```

한 덱에서 **잉크 밴드와 라임 밴드를 합쳐 5~6개**를 넘기지 않습니다.

### ④ 프롬프트 블록

수강생이 그대로 칠 프롬프트는 항상 이 모양입니다.

```css
.prompt{padding:25px;background:#132019;color:#e8eee9;
        border-left:7px solid var(--lime);
        font:500 16px/1.75 ui-monospace,monospace}
.prompt .skill{display:block;margin-bottom:13px;color:var(--lime);font-weight:850}
.prompt strong{color:#fff}      /* 실제 칠 문장 */
.prompt small{display:block;margin-top:13px;color:#aeb9b2;
              font:600 13px/1.6 Arial}   /* 제약조건 — 가운뎃점으로 나열 */
```

### ⑤ 화살표 흐름 행

단계·인과를 보여주는 기본 도구. **박스보다 흐름을 먼저 씁니다.**

```css
.flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;
      gap:8px;align-items:center}
.flow span{padding:13px 8px;background:#eef1ec;text-align:center;font-size:12px}
.flow strong{background:var(--ink);color:#fff}   /* 마지막 칸 = 결과 */
.flow i{font-style:normal;color:var(--muted)}    /* → */
```

- 칸은 **3개**가 기본, 최대 5개.
- 마지막 칸만 잉크로 채웁니다. 그게 결론입니다.
- 600px 이하에서 `grid-template-columns:1fr`, 화살표 `display:none`.

### ⑥ 숫자 히어로

수치 대비는 그래프가 아니라 **큰 숫자 두 개**로 보여줍니다.

```css
.stat{display:flex;align-items:center;gap:22px;line-height:1}
.stat span  {font-size:70px;color:#939c96;font-weight:850}  /* before — 흐리게 */
.stat i     {font-size:39px;color:#8c958f;font-style:normal} /* → */
.stat strong{font-size:104px;color:var(--ink);
             background:linear-gradient(transparent 68%,var(--lime) 68%)} /* after */
```

아래에 4칸짜리 세부 내역(`색 8→2` 형식)을 `#eef1ec` 칸으로 깔고, 그 아래 잉크 밴드로 닫습니다.

### ⑦ 스크린샷 프레임

```css
.shot{height:min(55vh,540px);overflow:hidden;background:#111;
      border:1px solid #303431;box-shadow:17px 17px 0 #dce4c5}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top left}
```

- 그림자는 **블러 0의 오프셋 그림자** 하나뿐입니다. 덱 전체에서 그림자는 여기에만 씁니다.
- `object-position:top left` — 스크린샷은 왼쪽 위를 기준으로 자릅니다.
- **"before" 이미지는 죽입니다**: `opacity:.52; filter:grayscale(.45) saturate(.55)`.
  두 이미지를 나란히 놓고 한쪽을 흐리게 하는 것으로 "이쪽을 보라"를 말합니다.

---

## 5. 컴포넌트 규칙

### 카드

```css
.card{padding:25~28px;background:#fff;border:1px solid var(--line)}
.card.top{border:0;border-top:5px solid var(--ink)}   /* 병렬 항목 3개일 때 */
```

- **radius 0. 그림자 없음.** 카드는 선으로만 존재합니다.
- 한 줄에 놓이는 카드는 `min-height`로 높이를 맞춥니다 (190 / 230 / 285 / 320px).
- 카드 안 제목은 `① ② ③` 또는 `01 02 03`으로 번호를 답니다.

### 사각 라벨 (칩) — 폐기

`.chip` / `.chips` 는 **쓰지 않습니다.**

주제를 태그로 나열하면 읽는 사람이 관계를 못 읽고 단어만 훑게 됩니다.
정보를 태그로 늘어놓는 대신, **관계를 보이는 도해**(흐름·비교·단계·표)로 놓습니다.

| 태그로 쓰던 것 | 대신 |
|---|---|
| 표지의 주제 나열 | 목차 장에서 번호 단계 목록으로 |
| 카드의 결론 배지 | 카드 본문의 마지막 문장으로 |
| 항목 나열 | `.pairs` 또는 `.trio` 카드로 |

CSS는 기존 덱 호환을 위해 남겨 두되, 새 덱에서는 쓰지 않습니다.

### 번호 단계 목록

```css
.steps > div{display:grid;grid-template-columns:42px 1fr;gap:13px;
             align-items:center;padding:16px 0;border-top:1px solid var(--line)}
.steps > div:first-child{border-top:0}
.steps b{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;
         background:var(--ink);color:#fff;font-size:12px}
.steps strong{display:block;font-size:17px}
.steps span{display:block;margin-top:5px;color:var(--muted);font-size:13px}
```

원형 번호는 **여기(단계 목록)에서만** 허용합니다.

### 예시 UI (슬라이드 안에 그리는 제품 화면)

슬라이드 안에서 "제품 UI"를 흉내 낼 때만 둥근 모서리와 파란색이 등장합니다.

```css
button{padding:10~13px 20px;border:0;border-radius:6~12px;
       background:var(--blue);color:#fff;font-weight:800~850}
.bar{height:9~10px;background:#e8ece8;border-radius:999px;overflow:hidden}
.bar i{display:block;width:72%;height:100%;background:var(--blue)}
```

> **경계가 중요합니다.** 라운드·파랑·알약은 *덱의 스타일이 아니라 인용된 제품의 스타일*입니다.
> 덱 자신의 구조(카드·밴드·헤더)에는 절대 쓰지 않습니다.

### 모서리 정리표

| 대상 | radius |
|---|---|
| 카드·밴드·프레임·프롬프트 | **0** |
| 예시 버튼 | 6~12px |
| 예시 진행 막대·배지 | 999px |
| 이동 버튼·단계 번호 | 50% (원) |

---

## 5-9. 벤다이어그램 `.venn`

두 집합의 **포함·교집합 관계**를 보일 때만 씁니다. 순서나 인과에는 쓰지 않습니다(그건 `.flow`).

- 원은 `viewBox="0 0 620 360"` 의 SVG, 반지름 150, 중심 x=245 / x=375.
- 흰 원 두 개를 그린 뒤 `clipPath` 로 **교집합만 라임(`#c9f450`)** 으로 칠합니다. 테두리는 잉크 2px.
- **글자는 SVG 안에 넣지 않습니다.** `position:absolute` 한 HTML `<p>` 세 개를
  좌(25.8%) · 중앙(50%) · 우(74.2%)에 얹습니다 — 그래야 인라인 편집이 걸립니다.
- 각 라벨은 `<b>이름</b><span>설명 2~3줄</span>` 형태, 설명은 12px muted.
- 600px 이하에서는 라벨이 다이어그램 아래로 흘러내립니다(`position:static`).

## 5-10. 인라인 편집

발표 직전에 문장을 고칠 수 있도록, 모든 덱은 **클릭 편집**을 탑재합니다.

| 동작 | 방법 |
|---|---|
| 편집 켜기/끄기 | 푸터 `[편집]` 버튼 또는 `E` |
| 고치기 | 글자를 클릭하고 그대로 타이핑 (서식은 못 바꿉니다) |
| 저장 | `[저장]` 또는 `⌘S` — **원본 파일을 덮어씁니다.** 파일은 처음 한 번만 고르면 되고, 핸들이 IndexedDB 에 남아 다음부터는 묻지 않습니다 |
| 되돌리기 | `[원래대로]` |

- 편집 중에는 방향키로 장이 넘어가지 않습니다.
- 고친 내용은 `localStorage` 에 자동으로 남으므로, 저장 전에 창을 닫아도 유지됩니다.
- 덮어쓰기는 File System Access API 를 씁니다. 지원하지 않는 브라우저에서는 내려받기로 떨어지고, 그 이유가 푸터에 표시됩니다.
- 편집 버튼은 `.edit-btn` — **각지고 흰 면**입니다. `.nav` 안에 넣으면 원형으로 잘리니 `.tools` 에 둡니다.

## 6. 슬라이드 문법

### 6-1. 한 장의 형태

```
h1        — 핵심 명사에 .accent (한 장에 한 번) · 후킹 금지
p.body  1문장 (18px, muted)          ← 제목을 풀어 주는 한 줄. 두 문장 넘기지 않음
────────── 오른쪽 ──────────
도해 (카드/흐름/비교/단계 중 하나)
결론 밴드 1줄
```

**한 장 = 메시지 하나 + 그것을 보이는 그림 하나 + 못 박는 한 줄.**

### 6-2. 제목 작법

**제목은 그 장에서 다루는 것을 그대로 부릅니다. 후킹하지 않습니다.**

| 방식 | 예 |
|---|---|
| 명사구 (기본) | `MCP 서버의 세 가지 구성요소` |
| 주어+서술 (정의할 때) | `API는 서비스가 정한 창구` |
| 대비 표기 (수치·비교) | `연결 비용 N×M vs N+M` |

- **한 줄이 기본입니다.** 두 줄은 정의문이 길어질 때만 씁니다.
- **쓰지 않습니다**: 반문(`왜 자꾸 헷갈릴까?`), 반전(`질문이 틀렸다`),
  조건+주장 2단 구성(`겉보기엔 똑같은데 / 누가 붙느냐가 다르다`).
  장마다 후킹을 걸면 장끼리 경쟁해서 덱 전체가 난잡해집니다.
- 주장은 제목이 아니라 **리드 한 문장(`p.body`)과 결론 밴드**가 맡습니다.
- 표지 제목은 **강의 이름**입니다. 주장이 아니라 다룰 범위를 적습니다.
- 형광펜은 제목의 **핵심 명사**에 겁니다. 한 장에 한 번.
- 마침표를 찍지 않습니다. 물음표도 쓰지 않습니다.
- 마케팅 문구·감탄사·이모지를 쓰지 않습니다.

### 6-3. 15장 서사 골격

원본 덱의 순서입니다. 주제가 달라도 이 뼈대는 재사용됩니다.

| # | 유형 | 하는 일 |
|---|---|---|
| 1 | 표지 | 제목 + 한 줄 부제 |
| 2 | 상황 | 듣는 사람이 아는 불편을 재현 (요청 → 내가 할 일 3가지) |
| 3 | 대조 | 겉보기 같은 A/B, 무엇이 다른지 (2열 비교 + 잉크 펀치라인) |
| 4 | 확대 | 문제가 규모에 따라 어떻게 커지는지 (3단계 흐름 + 라임 밴드) |
| 5 | 정의 | 용어를 한 문장으로 |
| 6 | 해부 | 구성요소 3개 (`.card.top` 3열) |
| 7 | 이유 | 없을 때 / 있을 때 두 경로 비교 |
| 8 | 절차 | 3단계 번호 목록 + 결과 밴드 |
| 9 | 도구 | 쓸 도구가 무엇인지 + 출처 링크 |
| 10 | 실행 | 흐름 3칸 + **프롬프트 블록** |
| 11 | before | 스크린샷 1장 |
| 12 | after | 숫자 히어로 + before/after 썸네일 |
| 13 | 원리 | 한곳의 규칙 → 여러 UI (좌우 매핑) |
| 14 | 시작점 | 따라 할 경로 2개 + 예시 프롬프트 |
| 15 | 마무리 | 할 수 있는 것 / 별도로 고민할 것 2카드 |

- 프롬프트 블록은 **10번과 14번**에만. 남발하면 무게가 사라집니다.
- 외부 출처는 `↗`를 붙인 텍스트 링크로 표기합니다: `공식 GitHub ↗`.

---

## 7. 반응형

두 개의 분기점만 씁니다.

```css
@media(max-width:900px){
  .deck{padding:20px}
  .slide.active{grid-template-columns:1fr;gap:24px}  /* 2단 → 1단 */
  .slide h1{font-size:42px}
  .shot{height:380px}
}
@media(max-width:600px){
  .slide h1{font-size:33px} .slide h2{font-size:30px}
  /* 모든 다열 그리드 → 1열 */
  .flow{grid-template-columns:1fr}
  .flow i,.hint{display:none}    /* 화살표·힌트 숨김 */
  .nowrap{white-space:normal}
}
```

---

## 8. 조작 규격

```
→ / PageDown / Space   다음
← / PageUp             이전
]                      확대 (5%씩, 최대 200%)
[                      축소 (5%씩, 최소 50%)
\                      배율 100% 로 되돌리기
```

- 카운터는 `String(i+1).padStart(2,'0')`.
- 진행 막대 폭 `= (i+1)/n × 100%`.
- 첫/마지막 장에서 이동 버튼 `disabled`.
- 슬라이드 전환은 `.active` 클래스 토글만. 스크롤·페이지 이동이 아닙니다.

### 화면 배율 (강의 중 확대·축소)

강의실 뒷자리를 위한 조작입니다. **화면에는 버튼도 표시도 두지 않습니다.**

```css
:root{ --zoom:1 }
.slide{ width:min(1280px, calc(100% / var(--zoom,1))) }
.slide.active{ transform:scale(var(--zoom,1)); transform-origin:center center }
@keyframes enter{ from{...scale(var(--zoom,1))} to{...scale(var(--zoom,1))} }
```

- 배율이 걸리는 것은 `.slide` 뿐입니다. 헤더·푸터·진행 막대는 제자리에 남습니다.
- 폭을 배율만큼 좁게 잡고 키우므로 **확대해도 좌우가 잘리지 않고** 글이 다시 흐릅니다.
- 값은 `localStorage['deck-zoom:'+경로]` 에 남아 새로 고쳐도 유지됩니다.
- 실제 사용 범위는 100~140%. 그 이상은 도해가 많은 장의 위아래가 잘립니다.
- 편집 중(`isContentEditable`)에는 동작하지 않습니다.

---

## 9. 금지 목록

| ❌ | 이유 |
|---|---|
| 알약 배지·칩 (`radius:999px`) — 예시 UI 제외 | AI 생성물의 대표적 인상 |
| 그라데이션 배경 | 형광펜 하이라이트만 예외 |
| 카드 그림자 | 그림자는 스크린샷 프레임 1곳뿐 |
| 장식용 이모지 (✨🚀💡🎯) | `→ ↗ ✓ ①` 같은 기능 기호만 허용 |
| 강조색 2개 이상 | 라임 하나 |
| 라임 위 흰 글자 / 색 위 색 글자 | 대비 |
| 흰색(`#fff`) 덱 배경 | 종이 느낌이 사라짐 |
| 웹폰트·CDN·외부 이미지 | 네트워크 없이 떠야 함 |
| 한 장에 항목 6개 이상 | 두 장으로 나눔 |
| 여러 줄 제목을 자동 줄바꿈에 맡김 | `.nowrap`으로 직접 끊음 |

---

## 10. 체크리스트

```
□ 배경이 #f4f1e9 인가 (흰색이 아닌가)
□ 제목마다 .accent 가 한 번씩만 걸렸는가
□ 직접 끊은 제목 줄이 .nowrap 으로 감싸였는가
□ 제목 자간이 -.048em 인가
□ 카드·밴드의 radius 가 0 인가
□ 태그(.chip/.chips)를 쓰지 않았는가
□ 라운드·파랑·알약이 "예시 UI" 안에만 있는가
□ 그림자가 스크린샷 프레임 외에 없는가
□ 각 도해가 결론 밴드 한 줄로 닫히는가
□ 결론 밴드(잉크+라임) 합이 6개 이하인가
□ 프롬프트 블록이 2개 이하인가
□ 외부 요청 0건인가 (웹폰트·CDN·http 이미지 없음)
□ 900px·600px 에서 1단으로 접히는가
□ 헤더 카운터의 분모가 실제 장수와 같은가
□ --zoom 과 [ ] 배율 스크립트가 살아 있는가
```

### 검증 명령

```bash
f=대상.html
grep -c 'class="slide' "$f"                       # 장수 = 헤더 분모
grep -o 'class="accent[^"]*"' "$f" | wc -l        # 장수와 비슷해야 정상
grep -nE 'https?://(fonts|cdn|unpkg|jsdelivr)' "$f"   # 비어야 정상
grep -oE '[✨🚀🎯💡🔥]' "$f"                        # 비어야 정상
grep -o 'border-radius:999px' "$f" | wc -l        # 예시 UI 개수와 일치해야 함
```

---

## 11. 원본에서 고쳐 쓸 것

원본 HTML은 여러 번 고쳐 쓰이며 **CSS 패치 레이어가 아래로 쌓여** 있습니다.
같은 선택자를 뒤에서 다시 덮는 구간이 여럿입니다.

```css
/* 앞쪽 */ .anatomy .middle{background:var(--ink);color:#fff}
/* 뒤쪽 */ .anatomy .middle{background:#fff;color:var(--ink)}   /* 무효화 */
```

- `.anatomy .middle`(잉크 카드 → 흰 카드), `.final-card.yes`(라임 → 회색), `.slide:nth-of-type(8)` 계열, `.howto .input/.output` 높이 — **뒤에 오는 선언이 정답**입니다.
- 새로 만들 때는 패치를 쌓지 말고 `template.html`의 정리된 CSS에서 시작합니다.
- `.slide:nth-of-type(n)`으로 특정 장을 겨냥한 규칙은 **장 순서가 바뀌면 깨집니다.** 클래스 이름을 붙여 쓰세요.

---

## 12. 이 시스템을 쓰지 말아야 할 때

- **1280×720 고정 캔버스 · 인쇄용 PDF**가 필요한 경우 → 고정 캔버스를 쓰는 별도 구조가 필요합니다. 이 정의서의 덱은 뷰포트 반응형이라 인쇄 규격이 다릅니다.
- **발표 대본(`note:`)이 필요한 강의용** → 위와 같습니다. 이 덱에는 대본 슬롯이 없습니다.

> 이 정의서는 **강의·세미나용 단발 발표 덱**을 위한 것입니다.
