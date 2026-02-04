## Cordova SDK 통합하기

### 필수 조건

시작하기 전에 사용 중인 환경이 [최신 Braze Cordova 소프트웨어 개발 키트 버전으로](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements) 지원되는지 확인하세요.

### 1단계: 프로젝트에 SDK 추가

{% alert warning %}
아래 방법을 사용하여 Braze Cordova 소프트웨어 개발 키트만 추가하세요. 보안 침해로 이어질 수 있으므로 다른 방법으로 설치를 시도하지 마세요.
{% endalert %}

Cordova 6 이상을 사용하는 경우 GitHub에서 직접 SDK를 추가할 수 있습니다. 또는 [GitHub 리포지토리](https://github.com/braze-inc/braze-cordova-sdk)의 ZIP 파일을 다운로드하여 SDK를 수동으로 추가할 수도 있습니다.

{% tabs local %}
{% tab geofence disabled %}
위치 수집 및 지오펜스를 사용하지 않는다면 GitHub의 `master` 브랜치를 사용합니다.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
위치 수집 및 지오펜스를 사용하려면 GitHub의 `geofence-branch`를 사용합니다.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
이 단계를 반복하여 언제든지 `master` 와 `geofence-branch` 사이를 전환할 수 있습니다.
{% endalert %}

### 2단계: 프로젝트 구성

다음으로 프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 환경설정을 추가합니다.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

다음을 교체합니다:

| 값                 | 설명                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | [Braze REST API 키입니다]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | 사용자 지정 API 엔드포인트. 이 엔드포인트는 Braze 대시보드의 올바른 앱 그룹으로 Braze 인스턴스 데이터를 라우팅하는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`config.xml` 파일의 `platform` 요소는 다음과 유사해야 합니다:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## 플랫폼별 구문

다음 섹션에서는 iOS 또는 Android에서 Cordova를 사용할 때 플랫폼별 구문에 대해 설명합니다.

### 정수

{% tabs %}
{% tab ios %}
정수 환경설정은 다음 예제에서와 같이 문자열 표현으로 읽습니다.

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Cordova 8.0.0 이상 프레임워크가 환경설정을 처리하는 방식으로 인해 다음 예제와 같이 정수 전용 환경설정(예: 발신자 ID)은 `str_`이 앞에 오는 문자열로 설정해야 합니다.

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### 부울

{% tabs %}
{% tab ios %}
부울 환경설정은 다음 예제와 같이 `YES` 및 `NO` 키워드를 문자열 표현으로 사용하여 SDK에서 읽습니다.

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
부울 환경설정은 다음 예제와 같이 `true` 및 `false` 키워드를 문자열 표현으로 사용하여 SDK에서 읽습니다.

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## 선택적 구성 {#optional}

프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 기본 설정 중 하나를 추가할 수 있습니다:

{% tabs %}
{% tab ios %}
| 방법 | 설명 | 설명
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | 애플리케이션의 API 키를 설정합니다.                                                                                                                                                                                                                |
| `ios_api_endpoint` | 애플리케이션의 [SDK 엔드포인트를]({{site.baseurl}}/api/basics/#endpoints) 설정합니다.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration` | 자동 푸시 등록을 비활성화할지 여부를 설정합니다.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling` | 자동 푸시 처리를 비활성화할지 여부를 설정합니다.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection` | Braze 소프트웨어 개발 키트에서 IDFA 정보를 자동으로 수집할지 여부를 설정합니다. 자세한 내용은 [Braze IDFA 메서드 설명서를](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/) 참조하세요. |
| `enable_location_collection` | 자동 위치 수집을 인에이블먼트할지 여부를 설정합니다(사용자가 허용한 경우). `geofence-branch` |
| `geofences_enabled` | 지오펜싱 인에이블먼트 여부를 설정합니다.                                                                                                                                                                                                                   |
| `ios_session_timeout` | 애플리케이션의 Braze 세션 시간 제한을 초 단위로 설정합니다. 기본값은 10초입니다.                                                                                                                                                               |
| `sdk_authentication_enabled` | [소프트웨어 개발 키트 인증]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 인에이블먼트할지 여부를 설정합니다.                                                                                              |
| `display_foreground_push_notifications` | 애플리케이션이 포그라운드에 있는 동안 푸시 알림을 표시할지 여부를 설정합니다.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | `UNAuthorizationOptionProvisional` 비활성화 여부를 설정합니다.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds` | 트리거 사이의 최소 시간 간격을 초 단위로 설정합니다. 기본값은 30초입니다.                                                                                                                                                                   |
| `ios_push_app_group` | iOS 푸시 확장 프로그램의 앱 그룹 ID를 설정합니다.                                                                                                                                                                                                        |
| `ios_forward_universal_links` | 소프트웨어 개발 키트에서 유니버설 링크를 자동으로 인식하여 시스템 메서드에 전달할지 여부를 설정합니다.                                                                                                                                                     |
| `ios_log_level` | `Braze.Configuration.Logger` 에 대한 최소 로깅 수준을 설정합니다.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id` | 무작위로 생성된 UUID를 기기 ID로 사용할지 여부를 설정합니다.                                                                                                                                                                                    |
| `ios_flush_interval_seconds` | 자동 데이터 플러시 간격을 초 단위로 설정합니다. 기본값은 10초입니다.                                                                                                                                                                  |
| `ios_use_automatic_request_policy` | `Braze.Configuration.Api` 에 대한 요청 정책을 자동 또는 수동으로 설정합니다.                                                                                                                                                          |
| `should_opt_in_when_push_authorized` | 푸시 권한이 승인되면 사용자의 알림 구독 상태를 자동으로 `optedIn` 로 설정할지 여부를 설정합니다.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
자세한 내용은 [GitHub를 참조하세요: Braze iOS 코르도바 플러그인](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| 방법 | 설명 | 설명
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | 애플리케이션의 API 키를 설정합니다.                                                                                                                                                        |
| `android_api_endpoint` | 애플리케이션의 [SDK 엔드포인트를]({{site.baseurl}}/api/basics/#endpoints) 설정합니다.                                                                                                         |
| `android_small_notification_icon` | 알림 작은 아이콘을 설정합니다.                                                                                                                                                             |
| `android_large_notification_icon` | 알림 큰 아이콘을 설정합니다.                                                                                                                                                             |
| `android_notification_accent_color` | 16진수 표현을 사용하여 알림 강조 색상을 설정합니다.                                                                                                                        |
| `android_default_session_timeout` | 애플리케이션의 Braze 세션 시간 제한을 초 단위로 설정합니다. 기본값은 10초입니다.                                                                                                       |
| `android_handle_push_deep_links_automatically` | Braze 소프트웨어 개발 키트에서 푸시 딥링킹을 자동으로 처리할지 여부를 설정합니다.                                                                                                                       |
| `android_log_level` | 애플리케이션의 로그 수준을 설정합니다. 기본 로그 수준은 4이며, 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 인에이블먼트하려면 로그 수준 2를 사용하세요.                                    |
| `firebase_cloud_messaging_registration_enabled` | 푸시 알림에 Firebase 클라우드 메시징을 사용할지 여부를 설정합니다.                                                                                                                          |
| `android_fcm_sender_id` | Firebase Cloud 메시징 발신자 ID를 설정합니다.                                                                                                                                                  |
| `enable_location_collection` | 자동 위치 수집을 인에이블먼트할지 여부를 설정합니다(사용자가 허용한 경우).                                                                                                              |
| `geofences_enabled` | 지오펜싱 인에이블먼트 여부를 설정합니다.                                                                                                                                                           |
| `android_disable_auto_session_tracking` | 자동으로 세션을 추적하지 않도록 Android Cordova 플러그인을 비활성화합니다. 자세한 내용은 [자동 세션 추적 비활성화하기](#cordova_disable-automatic-session-tracking) | 도움말을 참조하세요.
| `sdk_authentication_enabled` | [소프트웨어 개발 키트 인증]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 인에이블먼트할지 여부를 설정합니다.                                      |
| `trigger_action_minimum_time_interval_seconds` | 트리거 사이의 최소 시간 간격을 초 단위로 설정합니다. 기본값은 30초입니다.                                                                                                           |
| `is_session_start_based_timeout_enabled` | 세션 시간 초과 동작을 세션 시작 이벤트 또는 세션 종료 이벤트 중 어느 쪽을 기준으로 할지를 설정합니다.                                                                                          |
| `default_notification_channel_name` | `NotificationChannel.getName` 을 통해 표시되는 사용자 이름을 Braze 기본값 `NotificationChannel` 으로 설정합니다.                                                                              |
| `default_notification_channel_description` | Braze 기본값 `NotificationChannel` 에 대해 `NotificationChannel.getDescription` 을 통해 표시되는 사용자 대면 설명을 설정합니다.                                                                |
| `does_push_story_dismiss_on_click` | 푸시 스토리를 클릭했을 때 자동으로 해제할지 여부를 설정합니다.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled` | 대체 Firebase 클라우드 메시징 서비스 사용 인에이블먼트 여부를 설정합니다.                                                                                                               |
| `fallback_firebase_messaging_service_classpath` | 대체 Firebase 클라우드 메시징 서비스에 대한 클래스 경로를 설정합니다.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled` | 콘텐츠 카드 미열람 시각적 표시기 표시줄의 인에이블먼트 여부를 설정합니다.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Braze 소프트웨어 개발 키트에서 토큰을 `com.google.firebase.messaging.FirebaseMessagingService.onNewToken` 에 자동으로 등록할지 여부를 설정합니다.                                                         |
| `is_push_deep_link_back_stack_activity_enabled` | 푸시를 위해 딥링크를 자동으로 팔로우할 때 Braze가 백 스택에 활동을 추가할지 여부를 설정합니다.                                                                                   |
| `push_deep_link_back_stack_activity_class_name` | 푸시를 위해 딥링크를 자동으로 팔로우할 때 Braze가 백 스택에 추가할 활동을 설정합니다.                                                                                     |
| `should_opt_in_when_push_authorized` | 푸시가 승인될 때 Braze가 자동으로 사용자를 옵트인할지 여부를 설정합니다.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
자세한 내용은 [GitHub를 참조하세요: Braze Android Cordova 플러그인](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

다음은 추가 구성이 포함된 `config.xml` 파일 예시입니다:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## 자동 세션 추적 비활성화하기(Android만 해당) {#disable-automatic-session-tracking}

기본적으로 Android Cordova 플러그인은 세션을 자동으로 추적합니다. 자동 세션 추적을 사용하지 않으려면 프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 환경 설정을 추가하세요:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

세션 추적을 다시 시작하려면 `BrazePlugin.startSessionTracking()` 으로 전화하세요. 다음 `Activity.onStart()` 이후에 시작된 세션만 추적됩니다.
