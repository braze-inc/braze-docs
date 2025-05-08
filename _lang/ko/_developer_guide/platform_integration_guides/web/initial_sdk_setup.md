---
nav_title: 초기 SDK 설정
article_title: Braze 웹 SDK의 초기 설정
platform: Web
page_order: 0
page_type: reference
---

# 웹용 초기 SDK 설정

> 이 참조 문서에서는 Braze 웹 SDK를 설치하는 방법을 다룹니다. Braze 웹 SDK를 사용하면 분석을 수집하고 리치 형식의 인앱 메시지, 푸시 및 콘텐츠 카드 메시지를 웹 사용자에게 표시할 수 있습니다. 전체 기술 참조는 [자바스크립트 ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "문서JSDocs를") 참조하세요.

{% multi_lang_include archive/web-v4-rename.md %}

## 1단계: Braze 라이브러리 설치

다음 방법 중 하나를 사용하여 Braze 라이브러리를 설치할 수 있습니다. 웹사이트에서 `Content-Security-Policy`를 사용하는 경우 라이브러리를 설치하기 전에 [콘텐츠 보안 정책 헤더 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/)를 참조하세요.

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

자세한 내용은 [Google Tag Manager 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/)를 참조하세요.
{% endtab %}

{% tab braze cdn %}
라이브러리를 비동기적으로 로드하는 CDN 호스팅 스크립트를 참조하여 Braze 웹 SDK를 HTML에 직접 추가합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## 2단계: SDK 초기화

Braze 웹 SDK가 웹사이트에 추가되면 Braze 대시보드 내 **설정** > **앱 설정에** 있는 API 키와 [SDK 엔드포인트 URL로]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) 라이브러리를 초기화합니다.

{% alert note %}
Tag Manager에서 Braze 초기화 옵션을 구성한 경우 이 단계를 건너뛸 수 있습니다.
{% endalert %}

`braze.initialize()`에 대한 전체 옵션 목록과 다른 JavaScript 메서드에 대한 자세한 내용은 [JavaScript 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)를 참조하세요.

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

## 3단계: 푸시 알림 설정(선택 사항)

Braze 웹 SDK에 대한 푸시 알림을 설정하려면 추가 설정이 필요합니다. 전체 안내는 [웹용 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)을 참조하세요.

## 로깅

로깅을 빠르게 활성화하려면 웹사이트 URL에 `?brazeLogging=true`를 매개변수로 추가하면 됩니다. 또는 [기본](#basic-logging) 또는 [사용자 지정](#custom-logging) 로깅을 사용 설정할 수 있습니다.

### 기본 로깅

{% tabs local %}
{% tab 초기화 전 %}
SDK가 초기화되기 전에 `enableLogging`을 사용하여 기본 디버깅 메시지를 JavaScript 콘솔에 기록합니다.

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
SDK가 초기화된 후에 `braze.toggleLogging()`을 사용하여 기본 디버깅 메시지를 JavaScript 콘솔에 기록합니다. 방법은 다음과 유사해야 합니다:

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
기본 로그는 모든 사용자에게 표시되므로 코드를 프로덕션에 출시하기 전에 비활성화하거나 [`setLogger`](#custom-logging)로 전환합니다.
{% endalert %}

### 사용자 지정 로깅

`setLogger` 을 사용하여 사용자 지정 디버깅 메시지를 자바스크립트 콘솔에 기록합니다. 기본 로그와 달리 이러한 로그는 사용자에게 표시되지 않습니다.

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

## 대체 통합 방법

### 서버 측 렌더링 프레임워크 {#ssr}

Next.js와 같은 서버 측 렌더링 프레임워크를 사용하는 경우 SDK가 브라우저 환경에서 실행되기 때문에 오류가 발생할 수 있습니다. SDK를 동적으로 가져오면 이러한 문제를 해결할 수 있습니다.

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

### Vite 지원 {#vite}

Vite를 사용할 때 순환 종속성 또는 `Uncaught TypeError: Class extends value undefined is not a constructor or null`에 대한 경고가 표시되는 경우 Braze SDK를 [종속성 검색](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)에서 제외해야 할 수 있습니다.

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Electron 지원 {#electron}

Electron은 웹 푸시 알림을 공식적으로 지원하지 않습니다(이 [GitHub 이슈](https://github.com/electron/electron/issues/6697) 참조). Braze에서 테스트하지 않은 다른 [오픈 소스 해결 방법을](https://github.com/MatthieuLemoine/electron-push-receiver) 시도해 볼 수 있습니다.

### AMD 모듈 로더

RequireJS 또는 기타 AMD module-loaders를 사용하는 경우 라이브러리 사본을 자체 호스팅하고 다른 리소스와 마찬가지로 참조하는 것이 좋습니다.

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### 대안 AMD 설치 없음

사이트에서 RequireJS 또는 다른 AMD module-loader를 사용하지만 위의 다른 옵션 중 하나를 통해 Braze 웹 SDK 로드를 선호하는 경우 AMD 지원이 포함되지 않은 라이브러리 버전을 로드할 수 있습니다. 이 라이브러리 버전은 다음 CDN 위치에서 로드할 수 있습니다:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ는 기본적인 턴키 방식의 Braze 통합을 제공합니다. 통합을 구성하려면 Tealium 태그 관리 인터페이스에서 Braze를 검색하고 대시보드에서 웹 SDK API 키를 제공합니다.

자세한 내용이나 심층적인 Tealium 구성 지원은 [통합 설명서를]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) 확인하거나 Tealium 계정 관리자에게 문의하세요.

### 기타 태그 관리자
Braze는 사용자 지정 HTML 태그 내의 통합 지침에 따라 다른 태그 관리 솔루션과도 호환될 수 있습니다. 이러한 솔루션을 평가하는 데 도움이 필요하면 Braze 담당자에게 문의하세요.

### Jest 프레임워크 문제 해결 {#jest}

Jest를 사용할 때 `SyntaxError: Unexpected token 'export'` 와 유사한 오류가 표시될 수 있습니다. 이 문제를 해결하려면 Braze SDK를 무시하도록 `package.json`에서 구성을 조정합니다.

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```
