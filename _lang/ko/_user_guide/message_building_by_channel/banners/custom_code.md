---
nav_title: 커스텀 코드 및 자바스크립트 브리지
article_title: 배너를 위한 커스텀 코드 및 자바스크립트 브리지
page_order: 2
page_type: reference
description: "배너에서 커스텀 HTML을 사용하는 방법과 클릭을 기록하고 Braze 작업을 트리거하는 자바스크립트 브리지에 대해 알아보세요."
channel:
  - banners
---

# 배너를 위한 커스텀 코드 및 자바스크립트 브리지

> 배너 작곡기에서 **커스텀 코드** 편집기 블록을 사용할 때, 클릭을 기록하기 위해 커스텀 HTML 내에서 `brazeBridge.logClick()`를 호출해야 합니다. 배너는 HTML 인앱 메시지와 동일한 자바스크립트 브리지를 사용하므로 동일한 메서드와 패턴이 적용됩니다.

배너 디자인에 커스텀 HTML을 사용하는 경우, Braze SDK는 커스텀 코드 내의 요소에 클릭 리스너를 자동으로 첨부할 수 없습니다. 캠페인 분석에서 추적하려는 클릭 가능한 요소(링크, 버튼 등)에 대해 `brazeBridge.logClick()`을 명시적으로 호출해야 합니다.

예를 들어, 사용자가 커스텀 HTML의 버튼을 탭할 때 클릭을 기록하려면:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

모든 사용 가능한 메서드 및 클릭 추적 옵션을 포함한 전체 자바스크립트 브리지 참조는 아래 섹션을 참조하세요.

## JavaScript 브리지 {#javascript-bridge}

{% include javascript_bridge/reference.md %}
