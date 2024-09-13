---
nav_title: 브라우저 확장 프로그램
article_title: 웹용 브라우저 확장 프로그램 통합
platform: Web
page_order: 20
page_type: reference
description: "이 문서에서는 브라우저 확장 프로그램(구글 크롬, 파이어폭스)에서 Braze 웹 SDK를 사용하는 방법을 설명합니다."

---

# 브라우저 확장

> 이 문서에서는 브라우저 확장 프로그램(구글 크롬, 파이어폭스)에서 Braze 웹 SDK를 사용하는 방법을 설명합니다.

브라우저 확장 프로그램 내에 Braze Web SDK를 통합하여 분석을 수집하고 사용자에게 리치 메시지를 표시하세요. 여기에는 **구글 크롬 확장** 프로그램과 **파이어폭스 애드온이** 모두 포함됩니다.

## 지원되는 항목

일반적으로 확장 프로그램은 HTML과 JavaScript이므로 다음과 같은 용도로 Braze를 사용할 수 있습니다:

* **애널리틱스**: 사용자 지정 이벤트와 속성을 캡처하고 확장 프로그램 내에서 반복 사용자를 식별할 수도 있습니다. 이러한 프로필 특성을 사용하여 크로스 채널 메시징을 강화하세요.
* **인앱 메시지**: 기본 또는 사용자 지정 HTML 메시지를 사용하여 사용자가 확장 프로그램 내에서 작업을 수행할 때 인앱 메시지를 트리거합니다.
* **콘텐츠 카드**: 온보딩 또는 프로모션 콘텐츠를 위해 확장 프로그램에 기본 카드 피드를 추가하세요.
* **웹 푸시**: 웹 페이지가 현재 열려 있지 않을 때에도 적시에 알림을 보내세요.

## 지원되지 않는 항목

* 매니페스트 v3 서비스 워커는 웹 환경용 모듈 가져오기를 지원하지 않습니다.

## 확장 유형

Braze는 확장 프로그램의 다음 영역에 포함될 수 있습니다:

| 영역 | 세부 정보 | 지원되는 항목 |
|--------|-------|------|
| 팝업 페이지 | [팝업][1] 페이지는 브라우저 툴바에서 확장 프로그램의 아이콘을 클릭하면 사용자에게 표시되는 대화상자입니다.| 애널리틱스, 인앱 메시지 및 콘텐츠 카드 |
| 백그라운드 스크립트 | [백그라운드 스크립트][2] (매니페스트 v2 전용)를 사용하면 확장 프로그램에서 사용자 탐색을 검사하고 상호작용하거나 웹페이지를 수정할 수 있습니다(예: 광고 차단기가 페이지의 콘텐츠를 감지하고 변경하는 방법). | 애널리틱스, 인앱 메시지 및 콘텐츠 카드.<br><br>백그라운드 스크립트는 사용자에게 표시되지 않으므로 메시지를 표시할 때 브라우저 탭이나 팝업 페이지와 통신해야 합니다. |
| 옵션 페이지 | [옵션 페이지에서는][3] 사용자가 확장 프로그램 내에서 설정을 전환할 수 있습니다. 새 탭이 열리는 독립형 HTML 페이지입니다. | 애널리틱스, 인앱 메시지 및 콘텐츠 카드 |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## 권한

Braze SDK(`braze.min.js`)를 확장에 번들로 제공되는 로컬 파일로 통합할 때 `manifest.json` 에 추가 권한이 필요하지 않습니다. 

그러나 \[Google 태그 관리자][8]]를 사용하거나 외부 URL에서 Braze SDK를 참조하거나 확장 프로그램에 대해 엄격한 콘텐츠 보안 정책을 설정한 경우 확장 프로그램의 [`content_security_policy`][6]`manifest.json` 설정을 조정하여 원격 스크립트 소스를 허용해야 합니다.

## 시작하기

{% alert tip %}
시작하기 전에 웹 SDK의 [초기 SDK 설정 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) 읽고 JavaScript 통합에 대해 전반적으로 자세히 알아보세요.  <br><br>다양한 SDK 메서드 및 구성 옵션에 대한 자세한 내용은 [JavaScript SDK 참조를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) 북마크에 추가할 수도 있습니다.
{% endalert %}

Braze의 웹 SDK를 통합하려면 먼저 최신 자바스크립트 라이브러리 사본을 다운로드해야 합니다. 이 작업은 NPM을 사용하거나 [Braze의 CDN에서][7] 직접 다운로드할 수 있습니다.

또는 \[Google 태그 관리자][8] ]를 사용하거나 외부에서 호스팅된 Braze SDK 사본을 사용하는 경우, 외부 리소스를 로드하려면 다음과 같이 [`content_security_policy`][6] 설정을 조정해야 합니다( `manifest.json`).

다운로드가 완료되면 `braze.min.js` 파일을 확장 프로그램의 디렉토리에 복사하세요.

### 확장 프로그램 팝업 {#popup}

확장 팝업에 Braze를 추가하려면 일반 웹사이트에서와 마찬가지로 `popup.html` 에서 로컬 JavaScript 파일을 참조하세요. Google 태그 매니저를 사용하는 경우, 대신 \[Google 태그 매니저 템플릿][8] ]을 사용하여 Braze를 추가할 수 있습니다.

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### 백그라운드 스크립트(매니페스트 v2만 해당) {#background-script}

확장 프로그램의 백그라운드 스크립트 내에서 Braze를 사용하려면 `background.scripts` 배열의 `manifest.json` 에 Braze 라이브러리를 추가하세요. 이렇게 하면 백그라운드 스크립트 컨텍스트에서 글로벌 `braze` 변수를 사용할 수 있게 됩니다.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### 옵션 페이지 {#options-page}

옵션 페이지( `options` 또는 `options_ui` 매니페스트 속성을 통해)를 사용하는 경우, [`popup.html` 지침에서와](#popup) 마찬가지로 Braze를 포함할 수 있습니다.

## 초기화

SDK가 포함되면 평소처럼 라이브러리를 초기화할 수 있습니다. 

브라우저 확장 프로그램에서는 쿠키가 지원되지 않으므로 `noCookies: true` 으로 초기화하여 쿠키를 비활성화할 수 있습니다.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

지원되는 초기화 옵션에 대한 자세한 내용은 \[웹 SDK 참조][10]]를 참조하세요.

## 푸시

확장 프로그램 팝업 대화상자에는 푸시 프롬프트가 허용되지 않습니다(탐색에 URL 표시줄이 없음). 따라서 확장 프로그램의 팝업 대화 상자에서 푸시 권한을 등록하고 요청하려면 \[대체 푸시 도메인][11] 에 설명된 대로 대체 도메인 해결 방법을 사용해야 합니다.

[1]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups
[2]: https://developer.chrome.com/extensions/background_pages
[3]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages
[6]: https://developer.chrome.com/extensions/contentSecurityPolicy
[7]: https://js.appboycdn.com/web-sdk/latest/braze.min.js
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/
[10]:https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
