## 안드로이드 SDK 통합

### 1단계: Gradle 빌드 구성 업데이트

프로젝트의 리포지토리 구성(예: `settings.gradle`, `settings.gradle.kts` 또는 최상위 `build.gradle`)에서 [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html)를 리포지토리 목록에 추가하세요. 이 구문은 Groovy와 Kotlin DSL 모두에 동일합니다.

```groovy
repositories {
  mavenCentral()
}
```

다음으로, Braze를 종속성에 추가하세요. 다음 예제에서 `SDK_VERSION`을 현재 버전의 Android Braze SDK로 교체하세요. 전체 버전 목록은 [변경 로그]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)를 참조하세요.

{% alert note %}
- Kotlin DSL(`build.gradle.kts`)의 경우, `implementation("...")` 구문을 사용하세요.
- Groovy(`build.gradle`)의 경우, `implementation '...'` 구문을 사용하세요.
- [버전 카탈로그](https://developer.android.com/build/migrate-to-catalogs)의 경우, `gradle/libs.versions.toml` 파일에 항목을 추가하고 생성된 접근자를 사용하여 참조하세요.
{% endalert %}

{% tabs local %}
{% tab base only %}
Braze UI 구성 요소를 사용할 계획이 없다면, 종속성에 다음을 추가하세요.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
당신의 `gradle/libs.versions.toml` 파일에서:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

그런 다음, `build.gradle` 또는 `build.gradle.kts` 파일에 다음 종속성을 추가하세요. 이 구문은 Groovy와 Kotlin DSL 모두에 동일합니다.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Braze UI 구성 요소를 사용할 계획이라면, 종속성에 다음을 추가하세요.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
당신의 `gradle/libs.versions.toml` 파일에서:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

그런 다음, `build.gradle` 또는 `build.gradle.kts` 파일에 다음 종속성을 추가하세요. 이 구문은 Groovy와 Kotlin DSL 모두에 동일합니다.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: 당신의 `braze.xml`을 구성하세요.

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않으며, 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a>을 참조하십시오.
{% endalert %}

프로젝트의 `res/values` 폴더에 `braze.xml` 파일을 생성하세요. 특정 데이터 클러스터에 있거나 기존 커스텀 엔드포인트가 있는 경우 `braze.xml` 파일에서도 엔드포인트를 지정해야 합니다. 

해당 파일의 내용은 다음 코드 스니펫과 유사해야 합니다. Braze 대시보드의 **설정 관리** 페이지에서 식별자로 `YOUR_APP_IDENTIFIER_API_KEY`을(를) 대체하십시오. [dashboard.braze.com](https://dashboard.braze.com)에 로그인하여 [클러스터 주소]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)를 찾으십시오. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### 3단계: `AndroidManifest.xml`에 권한 추가

다음으로, `AndroidManifest.xml`에 다음 권한을 추가하세요:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M의 출시와 함께 Android는 설치 시점에서 런타임 권한 모델로 전환되었습니다. 그러나 이 두 권한 모두 일반 권한이며 앱 매니페스트에 나열된 경우 자동으로 부여됩니다. 자세한 내용은 Android의 [권한 설명서](https://developer.android.com/training/permissions/index.html)를 참조하십시오.
{% endalert %}

### 4단계: 지연 초기화 활성화(선택 사항)

지연 초기화를 사용하려면 최소 Braze SDK 버전이 필요합니다:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
지연 초기화가 활성화되면 모든 네트워크 연결이 취소되어 SDK가 Braze 서버에 데이터를 전송할 수 없습니다.
{% endalert %}

#### Step 4.1: `braze.xml` 업데이트

지연 초기화는 기본적으로 비활성화되어 있습니다. 활성화하려면 다음 옵션 중 하나를 사용하십시오:

{% tabs %}
{% tab Braze XML file %}
프로젝트의 `braze.xml` 파일에서 `com_braze_enable_delayed_initialization`를 `true`로 설정하십시오.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
런타임에서 지연 초기화를 활성화하려면 다음 메서드를 사용하십시오.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
지연 초기화가 활성화되고 푸시 알림에 딥 링크 작업이 포함된 경우, 딥 링크가 해결되지 않습니다.
{% endalert %}

#### Step 4.2: 푸시 분석 구성(선택 사항)

지연 초기화가 활성화되면 푸시 분석이 기본적으로 대기열에 추가됩니다. 그러나 푸시 분석을 [명시적으로 대기열에 추가](#explicitly-queue-push-analytics)하거나 [버리기](#drop-push-analytics)를 선택할 수 있습니다.

##### 명시적으로 대기열에 추가 {#explicitly-queue-push-analytics}

푸시 분석을 명시적으로 대기열에 추가하려면 다음 옵션 중 하나를 선택하십시오:

{% tabs %}
{% tab Braze XML file %}
당신의 `braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior`를 `QUEUE`로 설정하십시오:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
당신의 [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메서드에 `QUEUE`를 추가하십시오:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### 버리기 {#drop-push-analytics}

푸시 분석을 버리려면 다음 옵션 중 하나를 선택하십시오:

{% tabs %}
{% tab Braze XML file %}
당신의 `braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior`를 `DROP`로 설정하십시오: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메서드에 `DROP`를 추가하십시오:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Step 4.3: SDK를 수동으로 초기화하십시오

선택한 지연 기간 후, [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) 메서드를 사용하여 SDK를 수동으로 초기화하십시오.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### 5단계: 사용자 세션 추적 활성화

사용자 세션 추적을 활성화하면 `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html), 및 `InAppMessageManager` 등록에 대한 호출이 자동으로 처리될 수 있습니다.

활동 생명주기 콜백을 등록하려면 `onCreate()` 클래스의 `Application` 메서드에 다음 코드를 추가하세요. 

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

사용 가능한 매개변수 목록은 [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)을 참조하세요.

{% endtab %}
{% endtabs %}

## 테스트 세션 추적

{% alert tip %}
SDK 문제를 진단하기 위해 [SDK 디버거]({{site.baseurl}}/developer_guide/debugging)를 사용할 수도 있습니다.
{% endalert %}

테스트 중 문제가 발생하면 [상세 로깅](#android_enabling-logs)을 활성화한 다음 logcat을 사용하여 활동에서 누락된 `openSession` 및 `closeSession` 호출을 감지하세요.

1. Braze에서 **개요**로 이동하여 앱을 선택한 다음 **데이터 표시** 드롭다운에서 **오늘**을 선택하세요.
    ![Braze의 "개요" 페이지로, "데이터 표시" 필드가 "오늘"으로 설정되어 있습니다.]({% image_buster /assets/img_archive/android_sessions.png %})
2. 앱을 열고 Braze 대시보드를 새로고침하세요. 측정기준이 1만큼 증가했는지 확인하세요.
3. 앱을 탐색하고 Braze에 단 하나의 세션만 기록되었는지 확인하세요.
4. 앱을 최소 10초 동안 백그라운드로 보내고, 다시 포그라운드로 가져오세요. 새 세션이 기록되었는지 확인하세요.

## 선택적 구성

### 런타임 구성

코드에서 Braze 옵션을 설정하려면 `braze.xml` 파일 대신 [런타임 구성](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)을 사용하세요. 두 곳에 값이 존재하는 경우 런타임 값이 대신 사용됩니다. 런타임에 모든 필수 설정이 제공된 후에는 `braze.xml` 파일을 삭제할 수 있습니다.

다음 예제에서는 [빌더 객체](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)가 생성된 후 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)에 전달됩니다. 사용 가능한 런타임 옵션 중 일부만 표시됩니다—전체 목록은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)를 참조하세요.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
다른 예제를 찾고 있나요? 우리의 [안녕하세요 Braze 샘플 앱](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)를 확인하세요.
{% endalert %}

### 구글 광고 ID

[구글 광고 ID (GAID)<1>는 구글 플레이 서비스에서 제공하는 광고를 위한 선택적 사용자 특정, 익명, 고유 및 재설정 가능한 ID입니다. GAID를 통해 사용자는 자신의 식별자를 재설정하고 Google Play 앱 내에서 관심 기반 광고를 옵트아웃할 수 있으며, 개발자는 간단한 표준 시스템으로 앱에서 지속적으로 수익을 창출할 수 있습니다.

Google 광고 ID는 Braze SDK에서 자동으로 수집되지 않으며, [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) 메서드를 통해 수동으로 설정해야 합니다.

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google은 비 UI 스레드에서 광고 ID를 수집하도록 요구합니다.
{% endalert %}


### 위치 추적

Braze 위치 수집을 활성화하려면 `com_braze_enable_location_collection`을 `true`로 설정하십시오 `braze.xml` 파일에서:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화됩니다.
{% endalert %}

### 로깅

기본적으로 Braze Android SDK 로그 수준은 `INFO`로 설정되어 있습니다. [이러한 로그를 억제](#android_suppressing-logs)하거나 `VERBOSE`, `DEBUG` 또는 `WARN`과 같은 [여러 로그 수준을 설정](#android_enabling-logs)할 수 있습니다 .

#### 로그 활성화

앱의 문제를 해결하거나 Braze 지원과의 처리 시간을 단축하려면 SDK에 대한 자세한 로그를 활성화할 수 있습니다. 상세 로그를 Braze 지원팀에 보낼 때 애플리케이션을 실행하자마자 로깅을 시작하여 문제가 발생하고 한참 후에 종료해야 합니다. 중앙 집중식 개요를 보려면 [자세한 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 참조하십시오. 로그 출력을 해석하는 방법을 배우려면 [자세한 로그 읽기]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)를 참조하십시오.

상세 로그는 개발 환경 전용이므로 앱을 출시하기 전에 비활성화하는 것이 좋습니다.

{% alert important %}
`Application.onCreate()`에서 다른 호출 전에 상세 로그를 활성화하여 최대한 완전한 로그를 작성합니다.
{% endalert %}

{% tabs local %}
{% tab Application %}
앱에서 직접 로그를 활성화하려면 다른 메서드보다 먼저 애플리케이션의 `onCreate()` 메서드에 다음을 추가합니다.

{% subtabs local %}
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

{% subtabs local %}
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

{% tab xml %}
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

#### 상세 로그 확인

로그가 `VERBOSE`로 설정되어 있는지 확인하려면 로그의 어딘가에 `V/Braze`가 있는지 확인합니다. 그러면 상세 로그가 활성화된 것입니다. 예를 들어, 다음과 같습니다.

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### 로그 억제

Braze Android SDK에 대한 모든 로그를 억제하려면 애플리케이션의 `onCreate()` 메서드에서 로그 수준을 `BrazeLogger.SUPPRESS`로 설정하십시오 _다른 메서드_보다 먼저.

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

### 여러 API 키

여러 API 키의 가장 일반적인 사용 사례는 디버그 및 릴리스 빌드 배리언트에 대한 API 키를 분리하는 것입니다.

빌드에서 여러 API 키 사이를 쉽게 전환하려면 각 관련 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 만드는 것이 좋습니다. 빌드 배리언트는 빌드 유형과 제품 버전의 조합입니다. 기본적으로 새로운 Android 프로젝트는 [`debug` 및 `release` 빌드 유형](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType)으로 구성되며 제품 맛이 없습니다.

각 관련 빌드 변형에 대해 `braze.xml`을 `src/<build variant name>/res/values/` 디렉토리에 새로 만드십시오. 빌드 변형이 컴파일되면 새 API 키를 사용합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
코드에서 API 키를 설정하는 방법을 배우려면 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)를 참조하십시오.
{% endalert %}

### 독점 인앱 메시지 TalkBack

[Android 접근성 가이드라인](https://developer.android.com/guide/topics/ui/accessibility)을 준수하여 Braze Android SDK는 기본적으로 Android Talkback을 제공합니다. 인앱 메시지의 내용만 소리 내어 읽도록 하려면—앱 제목 표시줄이나 탐색과 같은 다른 화면 요소를 포함하지 않고—TalkBack에 대한 독점 모드를 활성화할 수 있습니다.

인앱 메시지에 대한 독점 모드를 활성화하려면:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 및 ProGuard

[코드 축소](https://developer.android.com/build/shrink-code) 구성은 Braze 통합에 자동으로 포함됩니다.

Braze 코드를 난독화하는 클라이언트 앱은 Braze가 스택 추적을 해석할 수 있도록 릴리스 매핑 파일을 저장해야 합니다. 모든 Braze 코드를 계속 유지하려면 ProGuard 파일에 다음을 추가합니다.

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
