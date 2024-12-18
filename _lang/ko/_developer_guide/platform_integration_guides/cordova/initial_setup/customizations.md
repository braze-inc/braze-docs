---
nav_title: 사용자 지정
article_title: Cordova Braze SDK 사용자 지정
page_order: 1
---

# Cordova Braze SDK 사용자 지정

> 다음은 Cordova Braze SDK에서 사용 가능한 사용자 지정입니다.

{% multi_lang_include cordova/prerequisites.md %}

## 사용자 지정 옵션

프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 기본 설정 중 하나를 추가할 수 있습니다:

{% tabs %}
{% tab ios %}
| 방법 | 설명 | 설명
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key` | 애플리케이션의 API 키를 설정합니다. |
| `ios_api_endpoint`                             | 애플리케이션에 대한 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 설정합니다. |
| `ios_disable_automatic_push_registration` | 자동 푸시 등록을 비활성화할지 여부를 설정합니다. |
| `ios_disable_automatic_push_handling` | 자동 푸시 처리를 비활성화할지 여부를 설정합니다. |
| `ios_enable_idfa_automatic_collection`         | Braze SDK에서 IDFA 정보를 자동으로 수집해야 합니다. 자세한 내용은 [Braze의 IDFA 메서드 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)를 참조하세요. |
| `enable_location_collection` | 자동 위치 수집 활성화 여부를 설정합니다(사용자가 허용한 경우). `geofence-branch` |
| `geofences_enabled`                            | 지오펜스 활성화 여부를 설정합니다. |
| `ios_session_timeout`                          | 애플리케이션의 Braze 세션 제한 시간(초)을 설정합니다. 기본값은 10초입니다. |
| `sdk_authentication_enabled` | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부를 설정합니다. |
| `display_foreground_push_notifications`        | 애플리케이션이 포그라운드에 있을 때 푸시 알림 표시 여부를 설정합니다. |
| `ios_disable_un_authorization_option_provisional` | `UNAuthorizationOptionProvisional`의 비활성화 여부를 설정합니다. |
| `trigger_action_minimum_time_interval_seconds` | 트리거 사이의 최소 시간 간격을 초 단위로 설정합니다. 기본값은 30초입니다. |
| `ios_push_app_group` | iOS 푸시 확장 프로그램의 앱 그룹 ID를 설정합니다. |
| `ios_forward_universal_links` | SDK가 유니버설 링크를 자동으로 인식하여 시스템 메서드에 전달할지 여부를 설정합니다. |
| `ios_log_level` | `Braze.Configuration.Logger` 에 대한 최소 로깅 수준을 설정합니다. |
| `ios_use_uuid_as_device_id` | 무작위로 생성된 UUID를 디바이스 ID로 사용할지 여부를 설정합니다. |
| `ios_flush_interval_seconds` | 자동 데이터 플러시 간격을 초 단위로 설정합니다. 기본값은 10초입니다. |
| `ios_use_automatic_request_policy` | `Braze.Configuration.Api` 에 대한 요청 정책을 자동 또는 수동으로 설정합니다. |
| `should_opt_in_when_push_authorized` | 푸시 권한이 승인되면 사용자의 알림 구독 상태를 자동으로 `optedIn` 로 설정할지 여부를 설정합니다. |

{% alert tip %}
자세한 내용은 [GitHub를 참조하세요: Braze iOS 코르도바 플러그인](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| 방법 | 설명 | 설명
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key` | 애플리케이션의 API 키를 설정합니다. |
| `android_api_endpoint`                         | 애플리케이션에 대한 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 설정합니다. |
| `android_small_notification_icon` | 알림 작은 아이콘을 설정합니다. |
| `android_large_notification_icon` | 알림 큰 아이콘을 설정합니다. |
| `android_notification_accent_color`            | 16진수 표현을 사용하여 알림 강조 색상을 설정합니다. |
| `android_default_session_timeout`              | 애플리케이션의 Braze 세션 제한 시간(초)을 설정합니다. 기본값은 10초입니다. |
| `android_handle_push_deep_links_automatically` | Braze SDK가 푸시 딥링크를 자동으로 처리할지 여부를 설정합니다. |
| `android_log_level` | 애플리케이션의 로그 수준을 설정합니다. 기본 로그 수준은 4이며, 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 활성화하려면 로그 수준 2를 사용합니다.
| `firebase_cloud_messaging_registration_enabled`| 푸시 알림에 Firebase 클라우드 메시징을 사용할지 여부를 설정합니다. |
| `android_fcm_sender_id`                        | Firebase 클라우드 메시징 발신자 ID를 설정합니다. |
| `enable_location_collection`                   | 사용자가 허용하는 경우 자동 위치 수집의 활성화 여부를 설정합니다. |
| `geofences_enabled`                            | 지오펜스 활성화 여부를 설정합니다. |
| `android_disable_auto_session_tracking`        | 자동 세션 추적에서 Android Cordova 플러그인의 비활성화 여부를 설정합니다. |
| `sdk_authentication_enabled` | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부를 설정합니다. |
| `trigger_action_minimum_time_interval_seconds` | 트리거 사이의 최소 시간 간격을 초 단위로 설정합니다. 기본값은 30초입니다. |
| `is_session_start_based_timeout_enabled` | 세션 시간 초과 동작을 세션 시작 이벤트 또는 세션 종료 이벤트 중 어느 쪽을 기준으로 할지를 설정합니다. |
| `default_notification_channel_name` | `NotificationChannel.getName` 을 통해 표시되는 사용자 대면 이름을 Braze 기본값 `NotificationChannel` 으로 설정합니다. |
| `default_notification_channel_description` | `NotificationChannel.getDescription` 을 통해 표시되는 사용자 대면 설명을 Braze 기본값 `NotificationChannel` 으로 설정합니다. |
| `does_push_story_dismiss_on_click` | 푸시 스토리를 클릭했을 때 자동으로 해제할지 여부를 설정합니다. |
| `is_fallback_firebase_messaging_service_enabled`| 대체 Firebase 클라우드 메시징 서비스 사용의 활성화 여부를 설정합니다. |
| `fallback_firebase_messaging_service_classpath`| 대체 Firebase 클라우드 메시징 서비스에 대한 클래스 경로를 설정합니다. |
| `is_content_cards_unread_visual_indicator_enabled`| 콘텐츠 카드 읽지 않음 시각적 표시줄의 활성화 여부를 설정합니다. |
| `is_firebase_messaging_service_on_new_token_registration_enabled`| Braze SDK가 `com.google.firebase.messaging.FirebaseMessagingService.onNewToken` 에 토큰을 자동으로 등록할지 여부를 설정합니다. |
| `is_push_deep_link_back_stack_activity_enabled` | 푸시를 위해 딥링크를 자동으로 팔로우할 때 Braze가 백 스택에 활동을 추가할지 여부를 설정합니다. |
| `push_deep_link_back_stack_activity_class_name` | 푸시를 위해 딥링크를 자동으로 팔로우할 때 Braze가 백 스택에 추가할 활동을 설정합니다. |
| `should_opt_in_when_push_authorized` | 푸시 권한이 부여될 때 Braze가 자동으로 사용자를 옵트인할지 여부를 설정합니다. |

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

## 플랫폼별 구문

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
