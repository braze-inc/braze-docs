---
page_order: 1.4
nav_title: 상세 로깅
article_title: 상세 로깅
description: "Braze SDK에 대한 상세 로깅을 활성화하는 방법을 배우고, 문제 해결을 위한 로그를 수집하고, Braze 지원팀과 공유하세요."
---

# 상세 로깅

> 상세 로깅은 Braze SDK에서 낮은 수준의 자세한 정보를 출력하여 SDK가 초기화되고, 서버와 통신하며, 푸시, 인앱 메시지 및 콘텐츠 카드와 같은 메시징 채널을 처리하는 방식을 볼 수 있게 해줍니다.

푸시 알림이 도착하지 않거나, 인앱 메시지가 표시되지 않거나, 사용자 데이터가 동기화되지 않는 등 예상대로 작동하지 않을 때, 상세 로그는 문제의 근본 원인을 파악하는 데 도움이 됩니다. 추측하는 대신, 각 단계에서 SDK가 무엇을 하고 있는지 정확히 볼 수 있습니다.

{% alert tip %}
상세 로깅을 수동으로 활성화하지 않고 디버깅하려면 [SDK 디버거]({{site.baseurl}}/developer_guide/sdk_integration/debugging)를 사용하여 Braze 대시보드에서 직접 디버깅 세션을 생성할 수 있습니다.
{% endalert %}

## 상세 로깅을 사용할 때

다음이 필요할 때 상세 로깅을 켜세요:

- **SDK 초기화 확인**: SDK가 올바른 API 키와 엔드포인트로 올바르게 시작되는지 확인하세요.
- **메시지 전달 문제 해결**: 푸시 토큰이 등록되었는지, 인앱 메시지가 트리거되었는지, 콘텐츠 카드가 동기화되었는지 확인하세요.
- **딥 링크 디버깅**: SDK가 푸시, 인앱 메시지 또는 콘텐츠 카드에서 딥 링크를 수신하고 여는지 확인하세요.
- **세션 추적 검증**: 세션이 예상대로 시작되고 종료되는지 확인하세요.
- **연결 문제 진단**: SDK와 Braze 서버 간의 네트워크 요청 및 응답을 검사하세요.

## 상세 로깅 활성화

{% alert important %}
상세 로그는 개발 및 테스트 환경에서만 사용하도록 설계되었습니다. 앱을 프로덕션에 배포하기 전에 자세한 로깅을 비활성화하여 민감한 정보가 노출되는 것을 방지하십시오.
{% endalert %}

{% tabs %}
{% tab Android %}

가장 완전한 출력을 캡처하기 위해 `Application.onCreate()` 메서드에서 다른 SDK 호출 전에 자세한 로깅을 활성화하십시오.

**코드:**

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}

**`braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

자세한 로깅이 활성화되었는지 확인하려면 Logcat 출력에서 `V/Braze`을 검색하십시오. For example:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

자세한 내용은 [Android SDK 로깅]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs)을 참조하십시오.

{% endtab %}
{% tab Swift %}

초기화 중에 `Braze.Configuration` 객체에서 로그 수준을 `.debug`으로 설정하십시오.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

`.debug` 수준은 가장 자세하며 문제 해결을 위해 권장됩니다. 자세한 내용은 [Swift SDK 로깅]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels)을 참조하십시오.

{% endtab %}
{% tab Web %}

URL 매개변수로 `?brazeLogging=true`을 추가하거나 SDK 초기화 중에 로깅을 활성화하십시오:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

초기화 후에도 로깅을 토글할 수 있습니다:

```javascript
braze.toggleLogging();
```

로그는 브라우저의 개발자 도구의 **콘솔** 탭에 나타납니다. 자세한 내용은 [Web SDK 로깅]({{site.baseurl}}/developer_guide/sdk_integration#web_logging)을 참조하십시오.

{% endtab %}
{% tab Unity %}

1. **Braze** > **Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Braze Android 설정 표시** 드롭다운을 선택하십시오.
3. **SDK 로그 수준** 필드에 `0`를 입력하십시오.

{% endtab %}
{% tab React Native %}

SDK 구성 중에 로그 수준을 설정하십시오:

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## 로그 수집

자세한 로깅을 활성화한 후, 문제를 재현하고 플랫폼의 콘솔 또는 디버깅 툴에서 로그를 수집하십시오.

{% tabs %}
{% tab Android %}

Android Studio에서 **Logcat**을 사용하여 로그를 캡처하십시오:

1. 기기를 연결하거나 에뮬레이터를 시작하십시오.
2. Android 스튜디오에서 하단 패널의 **Logcat**을 엽니다.
3. Braze SDK 출력을 분리하기 위해 `V/Braze` 또는 `D/Braze`로 필터링합니다.
4. 문제를 재현합니다.
5. 관련 로그를 복사하여 텍스트 파일에 저장합니다.

{% endtab %}
{% tab iOS %}

macOS에서 **Console** 앱을 사용하여 로그를 캡처합니다:

1. 상세 로깅이 활성화된 상태로 기기에 앱을 설치합니다.
2. 기기를 Mac에 연결합니다.
3. **Console** 앱을 열고 **Devices** 사이드바에서 기기를 선택합니다.
4. 검색창에서 `Braze` 또는 `BrazeKit`로 로그를 필터링합니다.
5. 문제를 재현합니다.
6. 관련 로그를 복사하여 텍스트 파일에 저장합니다.

{% endtab %}
{% tab Web %}

브라우저의 개발자 도구를 사용합니다:

1. 브라우저의 개발자 도구를 엽니다(보통 **F12** 또는 **Cmd+Option+I**입니다).
2. **Console** 탭으로 이동합니다.
3. 문제를 재현합니다.
4. 콘솔 출력을 복사하여 텍스트 파일에 저장합니다.

{% endtab %}
{% endtabs %}

{% alert tip %}
Braze 지원을 위한 로그를 수집할 때, 앱을 실행하기 전에 로깅을 시작하고 문제가 발생한 후에도 계속합니다. 이것은 사건의 전체 순서를 캡처하는 데 도움이 됩니다.
{% endalert %}

## 상세 로그 읽기

상세 로그는 SDK가 수행하는 작업을 추적하는 데 도움이 되는 일관된 구조를 따릅니다. 특정 채널에 대한 로그 출력을 해석하는 방법, 어떤 주요 항목을 찾아야 하는지 및 일반적인 문제 해결 패턴에 대해 알아보려면 [상세 로그 읽기]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)를 참조하세요.

## Braze 지원과 로그 공유하기

SDK 문제로 Braze 지원에 연락할 때 다음을 포함하세요:

1. **자세한 로그 파일**: 앱 실행 전부터 문제 발생까지의 전체 로그 캡처입니다.
2. **재현 단계**: 문제를 유발하는 행동에 대한 명확한 설명입니다.
3. **예상 vs. 실제 동작**: 당신이 기대했던 일과 실제로 일어난 일입니다.
4. **SDK 버전**: 당신이 사용하고 있는 Braze SDK의 버전입니다.
5. **플랫폼 및 OS 버전**: 예: iOS 18.0, Android 14, 또는 Chrome 120.