## 필수 조건

이 튜토리얼을 시작하기 전에, Braze SDK가 최소 버전 요구 사항을 충족하는지 확인하십시오:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## 웹 SDK용 배너 표시

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

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
lines-index.js=8-23

#### 2\. 배너 업데이트 구독

배너가 업데이트될 때마다 실행되는 핸들러를 등록하려면 `subscribeToBannersUpdates()`을 사용하십시오. 핸들러 내부에서 `braze.getBanner("global_banner")`를 호출하여 최신 배치 정보를 가져옵니다.

!!단계
lines-index.js=15-22

#### 3\. 배너를 삽입하고 대조군을 처리하십시오

반환될 때 배너를 삽입하려면 `braze.insertBanner(banner, container)`을 사용하십시오. 레이아웃을 깔끔하게 유지하려면 대조군의 일부인 배너(예: `isControl`가 `true`일 때)를 숨기거나 축소하십시오.

!!단계
줄-index.js=25

#### 4\. 배너 새로 고침

SDK를 초기화한 후, 각 세션 시작 시 배너가 새로 고쳐지도록 `requestBannersRefresh(["global_banner", ...])`을 호출하십시오.

이 함수를 언제든지 호출하여 나중에 배너 배치를 새로 고칠 수도 있습니다.

!!단계
lines-main.html=3

#### 5\. 배너를 위한 컨테이너 추가

HTML에서 새로운 `<div>` 요소를 추가하고 `global-banner-container`과 같은 짧은 배너 관련 `id`를 부여하십시오. Braze는 이 `<div>`를 사용하여 페이지에 배너를 삽입합니다.

{% endscrolly %}
