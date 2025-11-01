## Android SDK 통합하기

### 1단계: `build.gradle` 업데이트

`build.gradle` 에서 [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) 를 리포지토리 목록에 추가합니다.

```kotlin
repositories {
  mavenCentral()
}
```

다음으로 종속성에 Braze를 추가합니다.

{% tabs local %}
{% tab 베이스 전용 %}
Braze UI 컴포넌트를 사용하지 않을 계획이라면 `build.gradle` 에 다음 코드를 추가하세요. `SDK_VERSION` 을 현재 버전의 Android Braze 소프트웨어 개발 키트로 바꿉니다. 전체 버전 목록은 [체인지로그를]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android) 참조하세요.

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab UI 구성 요소 사용 %}
나중에 Braze UI 컴포넌트를 사용할 계획이라면 `build.gradle` 에 다음 코드를 추가하세요.  `SDK_VERSION` 을 현재 버전의 Android Braze 소프트웨어 개발 키트로 바꿉니다. 전체 버전 목록은 [체인지로그를]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android) 참조하세요.

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### 2단계: 구성 `braze.xml`

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않으며, 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a>을 참조하십시오.
{% endalert %}

프로젝트의 `res/values` 폴더에 `braze.xml` 파일을 만듭니다. 특정 데이터 클러스터에 있거나 기존 커스텀 엔드포인트가 있는 경우 `braze.xml` 파일에서도 엔드포인트를 지정해야 합니다. 

해당 파일의 내용은 다음 코드 스니펫과 유사해야 합니다. Braze 대시보드의 **설정 관리** 페이지에서 식별자로 `YOUR_APP_IDENTIFIER_API_KEY`을(를) 대체하십시오. [dashboard.braze.com](https://dashboard.braze.com)에 로그인하여 [클러스터 주소]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)를 찾으십시오. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### 3단계: 다음에 대한 권한을 추가합니다. `AndroidManifest.xml`

다음으로 `AndroidManifest.xml` 에 다음 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M의 출시와 함께 Android는 설치 시점에서 런타임 권한 모델로 전환되었습니다. 그러나 이 두 권한 모두 일반 권한이며 앱 매니페스트에 나열된 경우 자동으로 부여됩니다. 자세한 내용은 Android의 [권한 설명서](https://developer.android.com/training/permissions/index.html)를 참조하십시오.
{% endalert %}

### 4단계: 지연된 초기화 인에이블먼트(선택 사항)

지연 초기화를 사용하려면 최소 Braze 소프트웨어 개발 키트 버전이 필요합니다:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
지연 초기화가 인에이블먼트되어 있는 동안에는 모든 네트워크 연결이 취소되어 소프트웨어 개발 키트에서 Braze 서버로 데이터를 전송하지 못합니다.
{% endalert %}

#### Step 4.1: `braze.xml` 업데이트

지연 초기화는 기본값으로 비활성화되어 있습니다. 인에이블하려면 다음 옵션 중 하나를 사용합니다:

{% tabs %}
{% tab Braze XML 파일 %}
프로젝트의 `braze.xml` 파일에서 `com_braze_enable_delayed_initialization` 을 `true` 으로 설정합니다.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab 런타임 시 %}
런타임에 지연 초기화를 인에이블먼트하려면 다음 방법을 사용하세요.

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

#### Step 4.2: 푸시 분석 구성(선택 사항)

지연 초기화를 인에이블먼트하면 푸시 분석이 기본값으로 대기줄에 대기합니다. 그러나 대신 푸시 분석을 [명시적으로 대기줄에](#explicitly-queue-push-analytics) 넣거나 [삭제하도록](#drop-push-analytics) 선택할 수 있습니다.

##### 명시적으로 대기줄 지정 {#explicitly-queue-push-analytics}

푸시 분석을 명시적으로 대기줄에 추가하려면 다음 옵션 중 하나를 선택합니다:

{% tabs %}
{% tab Braze XML 파일 %}
`braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior` 을 `QUEUE` 으로 설정합니다:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab 런타임 시 %}
`QUEUE` 추가 [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메소드에 추가합니다:

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

##### 드롭 {#drop-push-analytics}

푸시 분석을 삭제하려면 다음 옵션 중 하나를 선택합니다:

{% tabs %}
{% tab Braze XML 파일 %}
`braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior` 을 `DROP` 으로 설정합니다: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab 런타임 시 %}
`DROP` 추가 [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메서드에 추가합니다:

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

#### Step 4.3: 소프트웨어 개발 키트 수동 초기화하기

선택한 지연 기간이 지나면 [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) 메서드를 사용하여 소프트웨어 개발 키트를 수동으로 초기화합니다.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### 5단계: 사용자 세션 추적 인에이블먼트

사용자 세션 추적을 인에이블먼트하면 `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)및 `InAppMessageManager` 등록이 자동으로 처리될 수 있습니다.

활동 수명 주기 콜백을 등록하려면 `Application` 클래스의 `onCreate()` 메서드에 다음 코드를 추가하세요. 

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
{% tab 코틀린 %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

사용 가능한 매개변수 목록은 [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## 테스트 세션 추적

{% alert tip %}
[소프트웨어 개발 키트 디버거를]({{site.baseurl}}/developer_guide/debugging) 사용하여 소프트웨어 [개발]({{site.baseurl}}/developer_guide/debugging) 키트 문제를 진단할 수도 있습니다.
{% endalert %}

테스트하는 동안 문제가 발생하면 [상세 로깅을](#android_enabling-logs) 인에이블먼트한 다음 로그캣을 사용하여 활동에서 누락된 `openSession` 및 `closeSession` 호출을 감지하세요.

1. Braze에서 **개요로** 이동하여 앱을 선택한 다음 **표시 데이터 대상** 드롭다운에서 **오늘을** 선택합니다.
    ![Braze의 "개요" 페이지, "표시 데이터 날짜" 필드가 "오늘"로 설정되어 있습니다.]({% image_buster /assets/img_archive/android_sessions.png %})
2. 앱을 연 다음 Braze 대시보드를 새로고침합니다. 측정기준이 1 증가했는지 확인합니다.
3. 앱을 탐색하여 Braze에 하나의 세션만 로그인되어 있는지 확인합니다.
4. 앱을 10초 이상 백그라운드로 보낸 다음 포그라운드로 가져옵니다. 새 세션이 기록되었는지 확인합니다.

## 선택적 구성

### 런타임 구성

`braze.xml` 파일이 아닌 코드에서 Braze 옵션을 설정하려면 [런타임 구성을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) 사용하세요. 두 위치에 모두 값이 있는 경우 런타임 값이 대신 사용됩니다. 런타임에 모든 필수 설정이 제공되면 `braze.xml` 파일을 삭제할 수 있습니다.

다음 예제에서는 [빌더 객체가](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) 생성된 다음 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). 사용 가능한 런타임 옵션 중 일부만 표시되어 있으며, 전체 목록은 [KDoc을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) 참조하세요.

{% tabs %}
{% tab 자바 %}

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
{% tab 코틀린 %}

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
다른 예를 찾고 계신가요? [Hello Braze 샘플 앱을](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java) 확인해 보세요.
{% endalert %}

### 구글 광고 ID

[Google 광고 ID(GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) 는 Google Play 서비스에서 제공하는 광고용 선택적 사용자별 익명 고유 ID로, 재설정이 가능합니다. GAID를 통해 사용자는 자신의 식별자를 재설정하고 Google Play 앱 내에서 관심 기반 광고를 옵트아웃할 수 있으며, 개발자는 간단한 표준 시스템으로 앱에서 지속적으로 수익을 창출할 수 있습니다.

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
{% tab 코틀린 %}

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

Braze 위치 수집을 인에이블먼트하려면 `braze.xml` 파일에서 `com_braze_enable_location_collection` 을 `true` 으로 설정하세요:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화됩니다.
{% endalert %}

### 로깅

기본적으로 Braze Android SDK 로그 수준은 `INFO`로 설정되어 있습니다. [이러한 로그를 억제](#android_suppressing-logs)하거나 `VERBOSE`, `DEBUG` 또는 `WARN`과 같은 [여러 로그 수준을 설정](#android_enabling-logs)할 수 있습니다 .

#### 로그 인에이블먼트

앱의 문제를 해결하거나 Braze 지원팀과의 문제 처리 시간을 단축하기 위해 SDK에 대한 상세 로그를 활성화할 수 있습니다. 상세 로그를 Braze 지원팀에 보낼 때 애플리케이션을 실행하자마자 로깅을 시작하여 문제가 발생하고 한참 후에 종료해야 합니다.

상세 로그는 개발 환경 전용이므로 앱을 출시하기 전에 비활성화하는 것이 좋습니다.

{% alert important %}
`Application.onCreate()`에서 다른 호출 전에 상세 로그를 활성화하여 최대한 완전한 로그를 작성합니다.
{% endalert %}

{% tabs local %}
{% tab 애플리케이션 %}
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

Braze 소프트웨어 개발 키트에 대한 모든 로그를 억제하려면 다른 방법보다 _먼저_ 애플리케이션의 `onCreate()` 메서드에서 로그 수준을 `BrazeLogger.SUPPRESS` 로 설정하세요.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab 코틀린 %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### 여러 API 키

여러 API 키의 가장 일반적인 사용 사례는 디버그 및 릴리스 빌드 배리언트에 대한 API 키를 분리하는 것입니다.

빌드에서 여러 API 키 사이를 쉽게 전환하려면 각 관련 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 만드는 것이 좋습니다. 빌드 배리언트는 빌드 유형과 제품 버전의 조합입니다. 기본적으로 새 Android 프로젝트는 [`debug` 및 `release` 빌드 유형으로](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) 구성되며 제품 플레이버는 없습니다.

각 관련 구축 배리언트에 대해 `src/<build variant name>/res/values/` 디렉터리에 `braze.xml` 을 새로 만듭니다. 빌드 변형이 컴파일되면 새 API 키를 사용합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
코드에서 API 키를 설정하는 방법을 알아보려면 [런타임 구성을]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android) 참조하세요.
{% endalert %}

### 독점 인앱 메시지 TalkBack

[Android 접근성 가이드라인을](https://developer.android.com/guide/topics/ui/accessibility) 준수하기 위해 Braze 소프트웨어 개발 키트에서는 기본값으로 Android 토크백을 제공합니다. 앱 제목 표시줄이나 내비게이션과 같은 다른 화면 요소를 포함하지 않고 인앱 메시지 내용만 소리로 읽도록 하려면 TalkBack 전용 모드를 인에이블먼트하면 됩니다.

인앱 메시지 전용 모드를 인에이블먼트합니다:

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
