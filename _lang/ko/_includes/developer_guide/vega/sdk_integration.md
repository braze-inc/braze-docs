## Braze Vega SDK에 대한 설명

Braze Vega SDK를 사용하면 분석을 수집하고 사용자에게 풍부한 인앱 메시지를 표시할 수 있습니다. Braze Vega SDK의 대부분의 메서드는 비동기이며, 대기하거나 해결해야 하는 약속을 반환합니다.

## Braze Vega SDK 통합하기

### 1단계: Braze 라이브러리 설치

선호하는 패키지 관리자를 사용하여 Braze Vega SDK를 설치하세요.

{% tabs local %}
{% tab npm %}
프로젝트에서 NPM을 사용하는 경우, Braze Vega SDK를 종속성으로 추가할 수 있습니다.

```bash
npm install @braze/vega-sdk --save
```

설치 후, 필요한 메서드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
프로젝트에서 Yarn을 사용하는 경우, Braze Vega SDK를 종속성으로 추가할 수 있습니다.

```bash
yarn add @braze/vega-sdk
```

설치 후, 필요한 메서드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### 2단계: SDK 초기화

Braze Vega SDK가 프로젝트에 추가된 후, Braze 대시보드의 **설정** > **앱 설정**에서 찾은 API 키와 [SDK 엔드포인트 URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)으로 라이브러리를 초기화하세요.

{% alert important %}
다른 Braze 메서드를 호출하기 전에 `changeUser` 약속을 대기하거나 해결해야 하며, 그렇지 않으면 이벤트와 속성이 잘못된 사용자에게 설정될 수 있습니다.
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
익명 사용자는 [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)에 포함될 수 있습니다. 따라서 조건부로 SDK를 로드하거나 초기화하여 이러한 사용자를 MAU 수에서 제외할 수 있습니다.
{% endalert %}

## 선택적 구성

### 로깅

디버깅 및 문제 해결을 돕기 위해 SDK 로깅을 활성화할 수 있습니다. 로깅을 활성화하는 방법은 여러 가지가 있습니다.

#### 초기화 중 로깅 활성화

디버깅 메시지를 콘솔에 기록하기 위해 `initialize()`에 `enableLogging: true`을 전달하세요:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
기본 로그는 모든 사용자에게 표시되므로, 코드를 프로덕션에 배포하기 전에 로깅을 비활성화하는 것을 고려하세요.
{% endalert %}

#### 초기화 후 로깅 활성화

초기화 후 SDK 로깅을 활성화하거나 비활성화하려면 `toggleLogging()`을 사용하세요:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### 사용자 지정 로깅

SDK 로그 처리 방법에 대한 더 많은 제어를 위해 사용자 정의 로거 함수를 제공하려면 `setLogger()`을 사용하세요:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 구성 옵션

SDK 동작을 사용자 정의하기 위해 `initialize()`에 추가 구성 옵션을 전달할 수 있습니다:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDK 업그레이드하기

NPM 또는 Yarn에서 Braze Vega SDK를 참조할 때 패키지 종속성을 업데이트하여 최신 버전으로 업그레이드할 수 있습니다:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 통합 테스트

SDK 통합이 올바르게 작동하는지 확인하려면:

1. 콘솔에서 디버그 메시지를 보려면 `enableLogging: true`로 SDK를 초기화하십시오
2. 다른 SDK 메서드를 호출하기 전에 `await changeUser()`을(를) 확인하십시오
3. 세션을 시작하려면 `await openSession()`을(를) 호출하십시오
4. 세션 데이터가 기록되고 있는지 확인하려면 **개요**에서 Braze 대시보드를 확인하십시오
5. 커스텀 이벤트를 로깅하고 대시보드에 나타나는지 확인하십시오


