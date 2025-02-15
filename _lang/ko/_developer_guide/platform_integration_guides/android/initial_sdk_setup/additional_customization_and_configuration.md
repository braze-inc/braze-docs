---
nav_title: 기타 SDK 사용자 지정
article_title: Android 및 FireOS용 기타 SDK 커스터마이징
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 상세 로깅, 로깅 억제, 여러 API 키를 구현하는 방법 등 추가적인 사용자 지정 및 구성 옵션을 다룹니다."

---

# Android 및 FireOS용 기타 SDK 커스터마이징

> 이 참조 문서에서는 상세 로깅, 로깅 억제, 여러 API 키를 구현하는 방법 등 추가적인 사용자 지정 및 구성 옵션을 다룹니다.

## Braze와 함께 R8/ProGuard 사용

[코드 축소](https://developer.android.com/studio/build/shrink-code) 구성은 Braze 통합에 자동으로 포함됩니다.

Braze 코드를 난독화하는 클라이언트 앱은 Braze가 스택 추적을 해석할 수 있도록 릴리스 매핑 파일을 저장해야 합니다. 모든 Braze 코드를 계속 유지하려면 ProGuard 파일에 다음을 추가합니다.

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## 로깅

기본적으로 Braze Android SDK 로그 수준은 `INFO`로 설정되어 있습니다. [이러한 로그를 억제](#suppressing-logs)하거나 `VERBOSE`, `DEBUG` 또는 `WARN`과 같은 [여러 로그 수준을 설정](#enabling-logs)할 수 있습니다 .

### 로그 활성화 {#enabling-logs}

앱의 문제를 해결하거나 Braze 지원팀과의 문제 처리 시간을 단축하기 위해 SDK에 대한 상세 로그를 활성화할 수 있습니다. 상세 로그를 Braze 지원팀에 보낼 때 애플리케이션을 실행하자마자 로깅을 시작하여 문제가 발생하고 한참 후에 종료해야 합니다.

상세 로그는 개발 환경 전용이므로 앱을 출시하기 전에 비활성화하는 것이 좋습니다.

{% alert important %}
`Application.onCreate()`에서 다른 호출 전에 상세 로그를 활성화하여 최대한 완전한 로그를 작성합니다.
{% endalert %}

{% tabs %}
{% tab 애플리케이션 %}
앱에서 직접 로그를 활성화하려면 다른 메서드보다 먼저 애플리케이션의 `onCreate()` 메서드에 다음을 추가합니다.

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

`MIN_LOG_LEVEL`을 최소 로그 수준으로 설정하려는 로그 수준의 **상수**로 바꿉니다. 설정된 `MIN_LOG_LEVEL` 이상(`>=`) 수준의 모든 로그는 Android의 기본 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정된 `MIN_LOG_LEVEL` 수준 아래(`<`)의 모든 로그는 삭제됩니다.

| 상수    | 값          | 설명                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | 디버깅 및 개발을 위한 가장 자세한 메시지를 기록합니다.            |
| `DEBUG`     | 3              | 디버깅 및 개발을 위한 설명 메시지를 기록합니다.                  |
| `INFO`      | 4              | 일반적인 하이라이트에 대한 정보 메시지를 기록합니다.                       |
| `WARN`      | 5              | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다.     |
| `ERROR`     | 6              | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT`    | 7              | 개발 중 조건이 거짓일 때 어설션 메시지를 기록합니다.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

예를 들어 다음 코드는 `2`, `3`, `4`, `5`, `6`, `7`의 로그 수준을 `Log` 메서드에 전달합니다.

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
`braze.xml`에서 로그를 활성화하려면 파일에 다음을 추가합니다.

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL`을 최소 로그 수준으로 설정하려는 로그 수준의 **값**으로 바꿉니다. 설정된 `MIN_LOG_LEVEL` 이상(`>=`) 수준의 모든 로그는 Android의 기본 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정된 `MIN_LOG_LEVEL` 수준 아래(`<`)의 모든 로그는 삭제됩니다.

| 상수    | 값          | 설명                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | 디버깅 및 개발을 위한 가장 자세한 메시지를 기록합니다.            |
| `DEBUG`     | 3              | 디버깅 및 개발을 위한 설명 메시지를 기록합니다.                  |
| `INFO`      | 4              | 일반적인 하이라이트에 대한 정보 메시지를 기록합니다.                       |
| `WARN`      | 5              | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다.     |
| `ERROR`     | 6              | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT`    | 7              | 개발 중 조건이 거짓일 때 어설션 메시지를 기록합니다.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

예를 들어 다음 코드는 `2`, `3`, `4`, `5`, `6`, `7`의 로그 수준을 `Log` 메서드에 전달합니다.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### 상세 로그 확인

로그가 `VERBOSE`로 설정되어 있는지 확인하려면 로그의 어딘가에 `V/Braze`가 있는지 확인합니다. 그러면 상세 로그가 활성화된 것입니다. 예를 들어, 다음과 같습니다.

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### 로그 억제

Braze Android SDK의 기본 로그 수준은 `INFO` 입니다. Braze Android SDK에 대한 모든 로그를 억제하려면 다른 메서드보다 _이전_에 애플리케이션의 `onCreate()` 메서드에서 `BrazeLogger.SUPPRESS`를 호출합니다.

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

여러 API 키의 가장 일반적인 사용 사례는 디버그 및 릴리스 빌드 배리언트에 대한 API 키를 분리하는 것입니다.

빌드에서 여러 API 키 사이를 쉽게 전환하려면 각 관련 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 만드는 것이 좋습니다. 빌드 배리언트는 빌드 유형과 제품 버전의 조합입니다. 기본적으로 [새 Android 프로젝트는 `debug` 및 `release` 빌드 유형으로 구성되며](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) 제품 버전은 구성되지 않습니다.

각 관련 빌드 배리언트에 대해 `src/<build variant name>/res/values/`에서 새 `braze.xml`을 생성하세요.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

빌드 변형이 컴파일되면 새 API 키를 사용합니다.

코드에서 API 키를 설정하려면 [런타임 구성]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) 설명서를 참조하세요.
