---
nav_title: 통합
article_title: 푸시 통합 for FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "이 참조 문서는 FireOS 애플리케이션에 Braze 푸시 알림을 통합하는 방법을 안내합니다."
channel: push
search_rank: 0.9
---

# FireOS 푸시 통합

> 이 참조 문서는 FireOS 애플리케이션에 Braze 푸시 알림을 통합하는 방법을 안내합니다.

푸시 알림은 중요한 업데이트가 발생할 때 사용자의 화면에 나타나는 앱 외부 알림입니다. 푸시 알림은 사용자에게 시의적절하고 관련성 높은 콘텐츠를 제공하여 앱에 다시 참여하도록 유도할 수 있는 유용한 방법입니다.

ADM (Amazon 기기 메시징)는 비-Amazon 기기에서 지원되지 않습니다. Kindle 푸시를 테스트하려면 [FireOS 기기](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm)가 있어야 합니다. 추가 모범 사례에 대한 [도움말 기사]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/)를 확인하세요.

Braze는 [Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging)을 사용하여 Amazon 기기에 푸시 알림을 보냅니다.

## 1단계: ADM 활성화

1. 계정을 생성하십시오 [Amazon Apps & Games 개발자 포털](https://developer.amazon.com/public) 이미 그렇게 하지 않은 경우.
2. [OAuth 자격 증명(클라이언트 ID 및 클라이언트 비밀)과 ADM API 키](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)를 구합니다.
3. Unity Braze 구성 창에서 **자동 ADM 등록 활성화됨**을 활성화합니다. 
  - 또는 다음 줄을 `res/values/braze.xml` 파일에 추가하여 ADM 등록을 활성화할 수 있습니다:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## 2단계: 업데이트 AndroidManifest.xml

앱의 AndroidManifest.xml에서 Amazon의 네임스페이스를 `<>manifest</>` 태그에 추가하세요:

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

다음으로, `<>manifest</> element` 뒤에 `<>permission</>` 및 `<>uses-permission</>` 요소를 추가하여 ADM을 지원하는 데 필요한 권한을 선언합니다.

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

다음으로, 매니페스트의 application 요소에 `amazon:enable-feature` 요소를 추가하여 앱이 기기의 ADM 기능을 사용하며, 앱이 기기에서 ADM 없이도 기능하도록 설계되었음(`android:required="false"`)을 선언합니다. `android:required`를 `"false"`로 설정해도 안전합니다. ADM이 기기에 없을 때 Braze ADM 코드 성능이 점진적으로 저하되기 때문입니다.

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

마지막으로, Braze `AndroidManifest.xml` 파일 내에서 ADM의 `REGISTRATION` 및 `RECEIVE` 의도를 처리하기 위해 의도 필터를 추가합니다. `amazon:enable-feature` 바로 뒤에 다음 요소를 추가합니다.

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## 3단계: ADM API 키를 저장하세요

먼저, ADM API 키를 `api_key.txt` 파일에 저장하고 프로젝트의 [`Assets/Plugins/Android/assets`][54] 폴더에 저장합니다. 다음으로, [앱의 ADM API 키를 구합니다](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

Amazon은 `api_key.txt`에 후행 줄 바꿈과 같은 공백 문자가 포함된 경우 키를 인식하지 않습니다.

## 4단계: 딥링크 추가

#### 자동 딥링크 열기 활성화

푸시 알림을 클릭할 때 Braze가 앱과 딥링크를 자동으로 열도록 설정하려면 `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`를 `true`로 설정합니다.

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

딥링크의 커스텀 처리를 설정하려면 Braze에서 푸시를 수신하고 여는 의도를 수신 대기하는 푸시 콜백을 만들어야 합니다. 자세한 내용은 Android 푸시 문서에서 푸시 [수신 및 열기 사용자 지정 처리를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) 참조하세요.

## 5단계: Braze 대시보드에 클라이언트 시크릿 및 클라이언트 ID를 추가하십시오

마지막으로 [1단계](#step-1-enable-adm)에서 얻은 클라이언트 비밀과 클라이언트 ID를 Braze 대시보드의 **설정 관리** 페이지에 추가해야 합니다.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## 수동 푸시 등록

Braze는 수동 등록을 권장하지 않지만, ADM 등록을 직접 처리해야 하는 경우 [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm)에 다음을 추가하십시오:

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
다음으로, [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html)을(를) 사용하여 사용자의 ADM `registration_id`을(를) Braze로 전달하십시오:

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## ADM 엑스트라

사용자는 [딥링킹]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/), 추적 URL 등에 대해 Kindle 푸시 메시지와 함께 커스텀 키-값 페어를 `extras`로 보낼 수 있습니다. Android 푸시와 달리, Kindle 푸시 사용자는 `extra` 키-값 페어를 정의할 때 Braze 예약 키를 키로 사용할 수 없습니다.

예약 키로 다음이 포함됩니다.

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Kindle 예약 키가 감지되면 Braze가 `Status Code 400: Kindle Push Reserved Key Used`을 반환합니다.

