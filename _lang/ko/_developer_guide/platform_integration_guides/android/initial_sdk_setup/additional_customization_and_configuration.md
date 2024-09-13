---
nav_title: 기타 SDK 사용자 지정
article_title: Android 및 FireOS용 기타 SDK 커스터마이징
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 자세한 로깅, 로깅 억제, 여러 API 키를 구현하는 방법 등의 추가 사용자 지정 및 구성 옵션에 대해 설명합니다."

---

# Android 및 FireOS용 기타 SDK 커스터마이징

> 이 참조 문서에서는 자세한 로깅, 로깅 억제, 여러 API 키를 구현하는 방법 등의 추가 사용자 지정 및 구성 옵션에 대해 설명합니다.

## Braze와 함께 R8/ProGuard 사용

[코드 축소](https://developer.android.com/studio/build/shrink-code) 구성은 Braze 통합에 자동으로 포함됩니다.

Braze 코드를 난독화하는 클라이언트 앱은 Braze가 스택 추적을 해석할 수 있도록 릴리스 매핑 파일을 저장해야 합니다. 모든 Braze 코드를 계속 유지하려면 ProGuard 파일에 다음을 추가하세요:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## 로깅

기본적으로 Braze Android SDK 로그 레벨은 `INFO` 로 설정되어 있습니다. [이러한 로그를 표시하지 않](#suppressing-logs) 거나 `VERBOSE`, `DEBUG` 또는 `WARN` 과 같은 [다른 로그 수준을 설정할](#enabling-logs) 수 있습니다 .

### 로그 활성화 {#enabling-logs}

앱의 문제를 해결하거나 Braze 지원으로 처리 시간을 단축하려면 SDK에 대한 자세한 로그를 사용하도록 설정하는 것이 좋습니다. 자세한 로그를 Braze 지원팀에 보낼 때는 애플리케이션을 실행하자마자 시작하여 문제가 발생한 한참 후에 끝내도록 하세요.

자세한 로그는 개발 환경 전용이므로 앱을 출시하기 전에 비활성화하는 것이 좋습니다.

{% alert important %}
`Application.onCreate()` 에서 다른 호출 전에 상세 로그를 사용 설정하여 최대한 완전한 로그를 작성하세요.
{% endalert %}

{% tabs %}
{% tab 애플리케이션 %}
앱에서 직접 로그를 활성화하려면 다른 메서드보다 먼저 애플리케이션의 `onCreate()` 메서드에 다음을 추가하세요.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

`MIN_LOG_LEVEL` 을 최소 로그 수준으로 설정하려는 로그 수준의 **상수로** 바꿉니다. `>=` 수준의 모든 로그는 `MIN_LOG_LEVEL` 설정으로 Android의 기본값인 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정한 `<` 로그( `MIN_LOG_LEVEL` )는 모두 삭제됩니다.

| 상수    | 값          | 설명                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | 디버깅 및 개발을 위한 가장 자세한 메시지를 기록합니다.            |
| `DEBUG`     | 3              | 디버깅 및 개발을 위한 설명 메시지를 기록합니다.                  |
| `INFO`      | 4              | 일반적인 하이라이트에 대한 정보 메시지를 기록합니다.                       |
| `WARN`      | 5              | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다.     |
| `ERROR`     | 6              | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT`    | 7              | 개발 중 조건이 거짓일 때 어설션 메시지를 기록합니다.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

예를 들어 다음 코드는 로그 레벨을 `2`, `3`, `4`, `5`, `6`, `7` 를 `Log` 메서드로 전달합니다.

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
{% endtab %}

{% tab braze.xml %}
`braze.xml` 파일에 로그를 활성화하려면 파일에 다음을 추가합니다:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL` 를 최소 로그 수준으로 설정하려는 로그 수준의 **값으로** 바꿉니다. `>=` 수준의 모든 로그는 `MIN_LOG_LEVEL` 설정으로 Android의 기본값인 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정한 `<` 로그( `MIN_LOG_LEVEL` )는 모두 삭제됩니다.

| 상수    | 값          | 설명                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | 디버깅 및 개발을 위한 가장 자세한 메시지를 기록합니다.            |
| `DEBUG`     | 3              | 디버깅 및 개발을 위한 설명 메시지를 기록합니다.                  |
| `INFO`      | 4              | 일반적인 하이라이트에 대한 정보 메시지를 기록합니다.                       |
| `WARN`      | 5              | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다.     |
| `ERROR`     | 6              | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT`    | 7              | 개발 중 조건이 거짓일 때 어설션 메시지를 기록합니다.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

예를 들어 다음 코드는 로그 레벨을 `2`, `3`, `4`, `5`, `6`, `7` 를 `Log` 메서드로 전달합니다.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### 상세 로그 확인

로그가 `VERBOSE` 로 설정되어 있는지 확인하려면 로그의 어딘가에 `V/Braze` 이 있는지 확인하세요. 그러면 상세 로그가 성공적으로 활성화된 것입니다. 예를 들어, 다음과 같습니다.

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### 로그 억제

Braze Android SDK의 기본 로그 수준은 `INFO` 입니다. Braze Android SDK에 대한 모든 로그를 숨기려면 다른 방법보다 _먼저_ 애플리케이션의 `onCreate()` 메서드에서 `BrazeLogger.SUPPRESS` 을 호출하세요.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

## 여러 API 키

다중 API 키의 가장 일반적인 사용 사례는 디버그 및 릴리스 빌드 변형을 위한 API 키를 분리하는 것입니다.

빌드에서 여러 API 키를 쉽게 전환하려면 각 관련 [빌드 변형에](https://developer.android.com/studio/build/build-variants.html) 대해 별도의 `braze.xml` 파일을 만드는 것이 좋습니다. 빌드 변형은 빌드 유형과 제품 플레이버의 조합입니다. 기본적으로 [새 Android 프로젝트는 `debug` 및 `release` 빌드 유형으로 구성되며](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) 제품 플레이버는 없습니다.

각 관련 빌드 변형에 대해 `src/<build variant name>/res/values/` 에서 `braze.xml` 을 새로 만듭니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

빌드 변형이 컴파일되면 새 API 키를 사용합니다.

코드에서 API 키를 설정하려면 [런타임 구성]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) 설명서를 참조하세요.
