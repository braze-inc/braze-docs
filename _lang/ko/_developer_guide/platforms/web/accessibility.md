---
nav_title: 접근성
article_title: 접근성
platform: Web
page_order: 22
page_type: reference
description: "이 문서에서는 Braze가 접근성을 지원하는 방법을 설명합니다."

---

# 접근성

> 이 문서에서는 통합 내에서 Braze가 접근성을 지원하는 방법에 대한 개요를 제공합니다.

Braze 웹 소프트웨어 개발 키트는 [웹 콘텐츠 접근성 지침(WCAG 2.1)](https://www.w3.org/TR/WCAG21/)에서 제공하는 표준을 지원합니다. 모든 신규 구축에서 콘텐츠 카드와 인앱 메시지에 대해 [100/100의 등대 점수를](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) 유지하여 접근성 표준을 준수하고 있습니다.

## 필수 조건

WCAG 2.1을 충족하는 최소 소프트웨어 개발 키트 버전은 v3.4.0에 가깝습니다. 그러나 주요 이미지 태그 수정을 위해 최소 v6.0.0으로 업그레이드하는 것이 좋습니다.

### 주목할 만한 접근성 수정 사항

| 버전 | 유형 | 주요 변경 사항 |
|---------|------|-------------|
| **6.0.0** | **전공** | 이미지 `<img>` 태그, `imageAltText` 또는 `language` 필드, 일반 UI 접근성 개선 |
| **3.5.0** | Minor | 스크롤 가능한 텍스트 접근성 개선 |
| **3.4.0** | 고치다 | 콘텐츠 카드 `article` 역할 수정 |
| **3.2.0** | Minor | 버튼의 최소 터치 타겟팅 45x45px |
| **3.1.2** | Minor | 이미지의 기본값 대체 텍스트 |
| **2.4.1** | **전공** | 시맨틱 HTML (`h1` 또는 `button`), ARIA 속성, 키보드 탐색, 포커스 관리 |
| **2.0.5** | Minor | 초점 관리, 키보드 탐색, 레이블 |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## 지원되는 접근성 기능

콘텐츠 카드와 인앱 메시징에 이러한 기능을 지원합니다:

- ARIA 역할 및 레이블
- 키보드 탐색 지원
- 집중 관리
- 화면 리더 공지 사항
- 이미지에 대한 대체 텍스트 지원

## SDK 통합을 위한 접근성 가이드라인

일반적인 접근성 가이드라인은 [Braze에서 접근성 있는 메시지 구축하기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) 참조하세요. 이 가이드는 Braze 웹 SDK를 웹 애플리케이션에 통합할 때 접근성을 극대화하기 위한 팁과 모범 사례를 제공합니다.

### 콘텐츠 카드

#### 최대 높이 설정

콘텐츠 카드가 너무 많은 세로 공간을 차지하는 것을 방지하고 접근성을 개선하려면 이 예시와 같이 피드 컨테이너에 최대 높이를 설정할 수 있습니다:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### 뷰포트 고려 사항

인라인으로 표시되는 콘텐츠 카드의 경우 이 예시와 같이 뷰포트 제약 조건을 고려합니다.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### 인앱 메시지

{% alert warning %}
슬라이드 업 인앱 메시지에는 화면 리더가 액세스할 수 없으므로 중요한 정보를 넣지 마세요.
{% endalert %}

### 모바일 고려 사항

#### 반응형 디자인

소프트웨어 개발 키트에는 반응형 중단점이 포함되어 있습니다. 이 예시와 같이 커스텀한 내용이 화면 크기와 상관없이 작동하는지 확인합니다:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### 접근성 테스트

#### 수동 테스트 체크리스트

다음 작업을 완료하여 접근성을 수동으로 테스트하세요:

- 키보드(탭, 엔터, 스페이스)로만 콘텐츠 카드 및 인앱 메시지 탐색하기
- 스크린 리더로 테스트(NVDA, JAWS, VoiceOver)
- 모든 이미지에 대체 텍스트가 있는지 확인
- 색상 대비 비율 확인(WebAIM 대비 검사기 같은 도구 사용)
- 터치 기능이 있는 모바일 기기에서 테스트하기
- 초점 표시기가 표시되는지 확인
- 모달 메시지 포커스 트래핑 테스트하기
- 모든 대화형 요소에 키보드로 접근할 수 있는지 확인합니다.

### 일반적인 접근성 문제

일반적인 접근성 문제를 방지하려면 다음을 수행하세요:

1. **포커스 스타일을 유지하세요:** 소프트웨어 개발 키트의 초점 표시기는 키보드 사용자에게 필수적인 기능입니다.
2. **비대화형 요소에는 `display: none` 만 사용하세요:** `visibility: hidden` 또는 `opacity: 0` 을 사용하여 대화형 요소를 숨깁니다.
3. **ARIA 속성을 재정의하지 마세요:** 소프트웨어 개발 키트는 적절한 ARIA 역할과 레이블을 설정합니다.
4. **`tabindex` 속성을 사용합니다:** 키보드 탐색 순서를 제어합니다.
5. **`overflow: hidden` 을 설정한 경우 스크롤을 제공하세요:** 스크롤 가능한 콘텐츠에 계속 액세스할 수 있는지 확인합니다.
6. **구축된 키보드 핸들러를 방해하지 마세요:** 기존 키보드 탐색이 작동하는지 확인합니다.