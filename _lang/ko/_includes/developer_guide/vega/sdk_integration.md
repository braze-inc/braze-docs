## Braze Vega 소프트웨어 개발 키트 정보

Braze Vega 소프트웨어 개발 키트를 사용하면 분석을 수집하고 사용자에게 풍부한 인앱 메시지를 표시할 수 있습니다. Braze Vega 소프트웨어 개발 키트의 대부분의 메서드는 비동기식이며 기다리거나 해결해야 하는 약속을 반환합니다.

## Braze Vega SDK 통합하기

### 1단계: Braze 라이브러리 설치

선호하는 패키지 매니저를 사용하여 Braze Vega 소프트웨어 개발 키트를 설치합니다.

{% tabs local %}
{% tab npm %}
프로젝트에서 NPM을 사용하는 경우 Braze Vega 소프트웨어 개발 키트를 종속 요소로 추가할 수 있습니다.

```bash
npm install @braze/vega-sdk --save
```

설치 후 필요한 메소드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
프로젝트에서 Yarn을 사용하는 경우 Braze Vega 소프트웨어 개발 키트를 종속 요소로 추가할 수 있습니다.

```bash
yarn add @braze/vega-sdk
```

설치 후 필요한 메소드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### 2단계: SDK 초기화

프로젝트에 Braze Vega SDK를 추가한 후, **설정** > **앱 설정의** **설정** > **앱 설정에** 있는 API 키와 [SDK 엔드포인트 URL로]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) 라이브러리를 초기화하세요.

{% alert important %}
다른 Braze 메서드를 호출하기 전에 `changeUser` 약속을 기다리거나 해결해야 하며, 그렇지 않으면 이벤트와 속성이 잘못된 사용자에게 설정될 수 있습니다.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
익명 사용자는 [MAU에]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) 포함될 수 있습니다. 따라서 조건부로 SDK를 로드하거나 초기화하여 이러한 사용자를 MAU 수에서 제외할 수 있습니다.
{% endalert %}

## 선택적 구성

### 로깅

소프트웨어 개발 키트 로깅을 인에이블먼트하여 디버깅 및 문제 해결에 도움을 받을 수 있습니다. 로깅을 인에이블먼트하는 방법에는 여러 가지가 있습니다.

#### 초기화 중 로깅 인에이블먼트

`enableLogging: true` 을 `initialize()` 으로 전달하여 디버깅 메시지를 콘솔에 기록합니다:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
기본 로그는 모든 사용자에게 표시되므로 코드를 프로덕션에 릴리스하기 전에 로깅을 비활성화하는 것이 좋습니다.
{% endalert %}

#### 초기화 후 로깅 인에이블먼트

초기화 후 소프트웨어 개발 키트 로깅을 인에이블먼트하거나 비활성화하려면 `toggleLogging()` 을 사용하세요:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### 사용자 지정 로깅

`setLogger()` 에서 커스텀 로거 기능을 제공하여 소프트웨어 개발 키트 로그 처리 방식을 보다 세밀하게 제어할 수 있습니다:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 구성 옵션

`initialize()` 에 추가 구성 옵션을 전달하여 소프트웨어 개발 키트 동작을 커스텀할 수 있습니다:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDK 업그레이드하기

NPM 또는 Yarn에서 Braze Vega 소프트웨어 개발 키트를 참조하는 경우 패키지 종속성을 업데이트하여 최신 버전으로 업그레이드할 수 있습니다:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 통합 테스트하기

SDK 통합이 올바르게 작동하는지 확인하려면 다음과 같이 하세요:

1. 콘솔에서 디버그 메시지를 보려면 `enableLogging: true` 으로 소프트웨어 개발 키트를 초기화합니다.
2. 다른 소프트웨어 개발 키트 메서드를 호출하기 전에 `await changeUser()` 을 확인하십시오.
3. 세션을 시작하려면 `await openSession()` 으로 전화하세요.
4. 세션 데이터가 기록되고 있는지 확인하려면 **개요에서** Braze 대시보드를 확인하세요.
5. 커스텀 이벤트 로깅을 테스트하고 대시보드에 표시되는지 확인합니다.


