## 필수 조건

이 튜토리얼을 시작하기 전에 Braze 소프트웨어 개발 키트가 최소 버전 요구 사항을 충족하는지 확인하세요:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## 웹 소프트웨어 개발 키트용 배너 표시하기

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md 튜토리얼="배너 웹 표시하기" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!단계
lines-index.js=5

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
라인-index.js=8-23

#### 2\. 배너 업데이트 가입하기

`subscribeToBannersUpdates()` 을 사용하여 배너가 업데이트될 때마다 실행되는 핸들러를 등록하세요. 핸들러 내에서 `braze.getBanner("global_banner")` 으로 전화하여 최신 배치를 받으세요.

!!단계
라인-index.js=15-22

#### 3\. 배너를 삽입하고 대조군을 처리합니다.

반환 시 배너를 삽입하려면 `braze.insertBanner(banner, container)` 을 사용하세요. 레이아웃을 깔끔하게 유지하려면 대조군에서 벗어난 배너를 숨기거나 축소하세요(예: `isControl` 이 `true` 인 경우).

!!단계
줄-index.js=25

#### 4\. 배너 새로고침하기

소프트웨어 개발 키트를 초기화한 후 `requestBannersRefresh(["global_banner", ...])` 으로 전화하여 각 세션이 시작될 때마다 배너가 새로고침되도록 합니다.

나중에 언제든지 이 함수를 호출하여 배너 배치를 새로고침할 수도 있습니다.

!!단계
lines-main.html=3

#### 5\. 배너를 위한 컨테이너 추가

HTML에 새 `<div>` 요소를 추가하고 `global-banner-container` 와 같이 배너와 관련된 짧은 `id` 을 지정합니다. Braze는 이 `<div>` 을 사용하여 페이지에 배너를 삽입합니다.

{% endscrolly %}
