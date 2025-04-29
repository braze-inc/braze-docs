## 웹브레이즈 SDK 정보

웹브레이즈 SDK를 사용하면 분석을 수집하고 풍부한 인앱 메시지, 푸시 및 콘텐츠 카드 메시지를 웹 사용자에게 표시할 수 있습니다. 자세한 내용은 [Braze 자바스크립트 참조  참조하세요](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "문서JSDocs를").

{% multi_lang_include archive/web-v4-rename.md %}

## 웹 SDK 통합

{% alert tip %}
표준 통합 방법이 적합한지 잘 모르시겠어요? 계속하기 전에 [다른 연동 방법을](#web_other-integration-methods) 확인하세요.
{% endalert %}

### 1단계: Braze 라이브러리 설치

다음 방법 중 하나를 사용하여 Braze 라이브러리를 설치할 수 있습니다. 웹사이트에서 `Content-Security-Policy`를 사용하는 경우 라이브러리를 설치하기 전에 [콘텐츠 보안 정책 헤더 가이드]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/)를 참조하세요.

{% alert important %}
대부분의 광고 차단기는 Braze 웹 SDK를 차단하지 않지만, 일부 제한적인 광고 차단기는 문제를 일으키는 것으로 알려져 있습니다.
{% endalert %}

{% tabs local %}
{% tab 패키지 관리자 %}
사이트에서 NPM 또는 Yarn 패키지 관리자를 사용하는 경우 [Braze NPM 패키지를](https://www.npmjs.com/package/@braze/web-sdk) 종속성으로 추가할 수 있습니다.

이제 v3.0.0부터 Typescript 정의가 포함됩니다. 2.x에서 3.x로 업그레이드할 때 참고할 사항은 [체인지로그](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)를 참조하세요.

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

설치가 완료되면 일반적인 방법으로 라이브러리의 `import` 또는 `require` 작업을 수행할 수 있습니다.

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab Google 태그 관리자 %}
Braze 웹 SDK는 Google Tag Manager 템플릿 라이브러리에서 설치할 수 있습니다. 두 가지 태그가 지원됩니다:

1. 초기화 태그: 웹사이트에 웹 SDK를 로드하고 선택적으로 외부 사용자 ID를 설정합니다.
2. 작업 태그: 커스텀 이벤트, 구매, 사용자 ID 변경 또는 SDK 추적 토글을 트리거하는 데 사용됩니다.

자세한 내용은 [Google Tag Manager 통합 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_google-tag-manager)를 참조하세요.
{% endtab %}

{% tab braze cdn %}
라이브러리를 비동기적으로 로드하는 CDN 호스팅 스크립트를 참조하여 Braze 웹 SDK를 HTML에 직접 추가합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

### 2단계: SDK 초기화(선택 사항)

Tag Manager에서 Braze 초기화 옵션을 구성한 경우 이 단계를 건너뛸 수 있습니다.

그렇지 않은 경우, Braze 웹 SDK가 웹사이트에 추가된 후 Braze 대시보드 내 **설정** > **앱 설정에** 있는 API 키와 [SDK 엔드포인트 URL로]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) 라이브러리를 초기화합니다. `braze.initialize()` 에 대한 전체 옵션 목록과 다른 [자바스크립트](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 메서드에 대한 자세한 내용은 [Braze 자바스크립트 문서를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 참조하세요.

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
});

// optionally show all in-app messages without custom handling
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
모바일 또는 웹 디바이스의 익명 사용자도 [MAU에]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) 포함될 수 있습니다. 따라서 조건부로 SDK를 로드하거나 초기화하여 이러한 사용자를 MAU 수에서 제외할 수 있습니다.
{% endalert %}

## 선택적 구성

### 로깅

로깅을 빠르게 활성화하려면 웹사이트 URL에 `?brazeLogging=true`를 매개변수로 추가하면 됩니다. 또는 [기본](#web_basic-logging) 또는 [사용자 지정](#web_custom-logging) 로깅을 사용 설정할 수 있습니다.

#### 기본 로깅

{% tabs local %}
{% tab 초기화 전 %}
SDK가 초기화되기 전에 `enableLogging` 을 사용하여 기본 디버깅 메시지를 JavaScript 콘솔에 기록하세요.

```javascript
enableLogging: true
```

방법은 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 초기화 후 %}
SDK가 초기화된 후 기본 디버깅 메시지를 JavaScript 콘솔에 기록하려면 `braze.toggleLogging()` 을 사용하세요. 방법은 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
기본 로그는 모든 사용자에게 표시되므로 코드를 프로덕션에 출시하기 전에 비활성화하거나 [`setLogger`](#web_custom-logging)로 전환합니다.
{% endalert %}

#### 사용자 지정 로깅

`setLogger` 을 사용하여 사용자 지정 디버깅 메시지를 JavaScript 콘솔에 기록합니다. 기본 로그와 달리 이러한 로그는 사용자에게 표시되지 않습니다.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING` 를 단일 문자열 매개변수로 메시지로 바꿉니다. 방법은 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDK 업그레이드하기

{% multi_lang_include archive/web-v4-rename.md %}

기본 통합 지침에서 권장하는 대로 콘텐츠 전송 네트워크(예: `https://js.appboycdn.com/web-sdk/a.a/braze.min.js`)에서 Braze 웹 SDK를 참조하면 사용자가 사이트를 새로 고칠 때 자동으로 사소한 업데이트(위 예제에서 버그 수정 및 역호환 가능한 기능, `a.a.a`~`a.a.z` 버전)를 수신합니다.

그러나 주요 변경 사항을 출시할 때는 주요 변경 사항이 통합 기능에 영향을 주지 않도록 하기 위해 Braze 웹 SDK를 수동으로 업그레이드해야 합니다. 또한 SDK를 다운로드하여 직접 호스팅하는 경우 버전 업데이트를 자동으로 수신하지 않으므로 최신 기능 및 버그 수정을 수신하려면 수동으로 업그레이드해야 합니다.

RSS 리더 또는 원하는 서비스를 사용하여 [릴리스 피드를 따라](https://github.com/braze-inc/braze-web-sdk/tags.atom) 최신 릴리스를 최신 상태로 유지할 수 있습니다. 웹 SDK 릴리스 내역에 대한 전체 설명은 [체인지로그](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)를 참조하세요. Braze 웹 SDK를 업그레이드하려면:

- `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`의 버전 번호를 변경하거나 패키지 매니저의 종속성에서 Braze 라이브러리 버전을 업데이트합니다.
- 웹 푸시가 통합된 경우 사이트의 서비스 종사자 파일을 업데이트합니다. 기본적으로 사이트의 루트 디렉토리 내 `/service-worker.js`에 있지만 일부 통합에서는 위치를 사용자 지정할 수 있습니다. 서비스 워커 파일을 호스팅하려면 루트 디렉터리에 액세스해야 합니다.

이 두 파일은 적절한 기능을 위해 서로 조정하여 업데이트해야 합니다.

## Google 태그 관리자 {#google-tag-manager}

[Google 태그 관리자(GTM)를](https://support.google.com/tagmanager/answer/6103696) 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다. Braze는 다음과 같은 GTM 템플릿을 제공합니다:

|태그 유형|사용 사례|
|--------|--------|
| **초기화 태그:** | 초기화 태그는 [웹브레이즈 SDK를 초기화하는]({{site.baseurl}}/developer_guide/sdk_integration/initialization/?sdktabs=web) 데 사용할 수 있습니다.|
| **작업 태그:** | 액션 태그는 [콘텐츠 카드 관리]({{site.baseurl}}/docs/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager) 및 [분석 로깅에]({{site.baseurl}}/docs/developer_guide/analytics/) 사용할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

두 태그 모두 [Google의 커뮤니티 갤러리에서](https://tagmanager.google.com/gallery/#/?filter=braze) 또는 커뮤니티 템플릿에서 새 태그를 추가할 때 Braze를 검색하여 작업 공간에 추가할 수 있습니다.

![갤러리 검색 이미지]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

### Google의 업데이트된 EU 사용자 동의 정책

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) 개정 사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 자세한 내용은 다음 문서를 참조하세요.
{% endalert %}

Google의 EU 사용자 동의 정책의 일환으로 다음 부울 커스텀 속성을 고객 프로필에 기록해야 합니다.

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 통합을 통해 설정하는 경우 커스텀 속성을 사용하려면 커스텀 HTML 태그를 생성해야 합니다. 다음은 이러한 값을 문자열이 아닌 부울 데이터 유형으로 기록하는 방법의 예시입니다:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

자세한 내용은 [Google에 오디언스 동기화]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)를 참조하세요.

## 기타 통합 방법

### AMP(가속 모바일 페이지)
{% details 자세히 보기 %}
#### 1단계: AMP 웹 푸시 스크립트 포함

다음 비동기 스크립트 태그를 기억합니다.

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### 2단계: 구독 위젯 추가

사용자가 푸시를 구독 및 수신 취소할 수 있는 위젯을 HTML 본문에 추가하세요.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### 3단계: `helper-iframe` 및 `permission-dialog`

AMP 웹 푸시 컴포넌트는 푸시 구독을 처리하는 팝업을 생성하므로 이 기능을 사용하려면 프로젝트에 다음 헬퍼 파일을 추가해야 합니다:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### 4단계: 서비스 워커 파일 만들기

웹사이트의 루트 디렉터리에 `service-worker.js` 파일을 만들고 다음 코드 조각을 추가합니다:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### 5단계: AMP 웹 푸시 HTML 요소 구성

HTML 본문에 다음 `amp-web-push` HTML 요소를 추가합니다. [`apiKey` 및 `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) 을 `service-worker-URL` 에 쿼리 매개 변수로 추가해야 한다는 점을 기억하세요.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### AMD: 지원 비활성화하기

사이트에서 RequireJS 또는 다른 AMD 모듈 로더를 사용하지만 이 목록의 다른 옵션 중 하나를 통해 Braze Web SDK를 로드하는 것을 선호하는 경우 AMD 지원이 포함되지 않은 라이브러리 버전을 로드할 수 있습니다. 이 라이브러리 버전은 다음 CDN 위치에서 로드할 수 있습니다:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### AMD: 모듈 로더

RequireJS 또는 기타 AMD module-loaders를 사용하는 경우 라이브러리 사본을 자체 호스팅하고 다른 리소스와 마찬가지로 참조하는 것이 좋습니다.

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### 전자 {#electron}

Electron은 웹 푸시 알림을 공식적으로 지원하지 않습니다(이 [GitHub 이슈](https://github.com/electron/electron/issues/6697) 참조). Braze에서 테스트하지 않은 다른 [오픈 소스 해결 방법을](https://github.com/MatthieuLemoine/electron-push-receiver) 시도해 볼 수 있습니다.

### 재스트 프레임워크 {#jest}

Jest를 사용할 때 `SyntaxError: Unexpected token 'export'` 와 유사한 오류가 표시될 수 있습니다. 이 문제를 해결하려면 Braze SDK를 무시하도록 `package.json`에서 구성을 조정합니다.

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSR 프레임워크 {#ssr}

Next.js 와 같은 서버 측 렌더링(SSR) 프레임워크를 사용하는 경우 SDK가 브라우저 환경에서 실행되도록 되어 있기 때문에 오류가 발생할 수 있습니다. SDK를 동적으로 가져오면 이러한 문제를 해결할 수 있습니다.

SDK에서 필요한 부분을 별도의 파일로 내보낸 다음, 해당 파일을 구성요소에 동적으로 가져오는 방식으로 트리 셰이킹의 이점을 유지할 수 있습니다.

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

또는 웹팩을 사용하여 앱을 번들링하는 경우 매직 코멘트를 활용하여 SDK의 필요한 부분만 동적으로 가져올 수 있습니다.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Tealium iQ

Tealium iQ는 기본적인 턴키 방식의 Braze 통합을 제공합니다. 통합을 구성하려면 Tealium 태그 관리 인터페이스에서 Braze를 검색하고 대시보드에서 웹 SDK API 키를 제공합니다.

자세한 내용이나 심층적인 Tealium 구성 지원은 [통합 설명서를]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) 확인하거나 Tealium 계정 관리자에게 문의하세요.

### Vite {#vite}

Vite를 사용할 때 순환 종속성 또는 `Uncaught TypeError: Class extends value undefined is not a constructor or null`에 대한 경고가 표시되는 경우 Braze SDK를 [종속성 검색](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)에서 제외해야 할 수 있습니다.

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### 기타 태그 관리자

Braze는 사용자 지정 HTML 태그 내의 통합 지침에 따라 다른 태그 관리 솔루션과도 호환될 수 있습니다. 이러한 솔루션을 평가하는 데 도움이 필요하면 Braze 담당자에게 문의하세요.
