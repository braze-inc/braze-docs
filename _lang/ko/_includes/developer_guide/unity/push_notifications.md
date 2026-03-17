{% multi_lang_include developer_guide/prerequisites/unity.md %}

## 푸시 알림 설정하기

### 1단계: 플랫폼 설정

{% tabs %}
{% tab Android %}
#### 1.1단계: Firebase 활성화

시작하려면 [Firebase Unity 설정 설명서](https://firebase.google.com/docs/unity/setup)를 따르세요.

{% alert note %}
Firebase Unity SDK를 통합하면 `AndroidManifest.xml`이 재정의될 수 있습니다. 이 경우 원래대로 되돌려야 합니다.
{% endalert %}

#### 1.2단계: Firebase 자격 증명 설정

Braze 대시보드에 Firebase 서버 키와 발신자 ID를 입력해야 합니다. 이렇게 하려면 [Firebase 개발자 콘솔에](https://console.firebase.google.com/) 로그인하고 Firebase 프로젝트를 선택합니다. 다음으로, **설정**에서 **클라우드 메시징**을 선택하고 서버 키와 발신자 ID를 복사합니다:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Braze에서 **설정 관리** 아래의 **앱 설정** 페이지에서 Android 앱을 선택합니다. 다음으로, **Firebase 클라우드 메시징 서버 키** 필드에 Firebase 서버 키를 입력하고 **Firebase 클라우드 메시징 발신자** ID 필드에 Firebase 발신자 ID를 입력합니다.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### 1.1단계: 통합 방법 확인

Braze는 iOS 푸시 통합 자동화를 위한 네이티브 Unity 솔루션을 제공합니다. 대신 통합을 수동으로 설정하고 관리하려면 [Swift를 참조하세요: 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

그렇지 않으면 다음 단계로 계속 진행합니다.

{% alert note %}
자동 푸시 알림 솔루션은 iOS 12의 임시 인증 기능을 활용하며 기본 푸시 프롬프트 팝업에서는 사용할 수 없습니다.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### 1.1단계: ADM 활성화

1. 아직 계정을 만들지 않았다면 [Amazon 앱 & 게임 개발자 포털에](https://developer.amazon.com/public) 계정을 만드세요.
2. [OAuth 자격 증명(클라이언트 ID 및 클라이언트 비밀)과 ADM API 키](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)를 구합니다.
3. Unity Braze 구성 창에서 **자동 ADM 등록 활성화됨**을 활성화합니다. 
  - 또는 다음 줄을 `res/values/braze.xml` 파일에 추가하여 ADM 등록을 활성화할 수 있습니다:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### 2단계: 푸시 알림 구성

{% tabs %}
{% tab Android %}
#### 2.1 단계: 푸시 설정 구성하기

Braze SDK는 푸시 알림을 받기 위해 Firebase 클라우드 메시징 서버에 푸시 등록을 자동으로 처리할 수 있습니다. Unity에서 **자동화 Unity Android 통합을** 인에이블한 다음 다음 **푸시 알림** 설정을 구성합니다.

| Setting                                | 설명                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 자동 Firebase 클라우드 메시징 등록 활성화됨 | Braze SDK가 기기에 대한 FCM 푸시 토큰을 자동으로 검색하고 전송하도록 지시합니다.                                                                |
| Firebase Cloud Messaging 발송자 ID     | Firebase 콘솔의 발신자 ID.                                                                                                                |
| 푸시 딥링크를 자동으로 처리    | SDK가 푸시 알림을 클릭할 때 딥링크 열기 또는 앱 열기 중 어떤 처리 방식을 수행해야 하는지 여부.                                                  |
| 작은 알림 아이콘 드로어블       | 푸시 알림을 받을 때마다 드로어블이 작은 아이콘으로 표시되어야 합니다. 알림은 아이콘이 제공되지 않은 경우 애플리케이션 아이콘을 작은 아이콘으로 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### 2.1 단계: APN 토큰 업로드

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### 2.2 단계: 자동 푸시 인에이블먼트 사용

Unity 편집기에서 **Braze > Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.

푸시 알림에 사용자를 자동으로 등록하고, 푸시 토큰을 Braze에 전달하며, 푸시 열람 분석을 추적하고, 기본 푸시 알림 처리 기능을 활용하려면 **Braze와 푸시 통합**을 선택합니다.

#### 2.3 단계: 백그라운드 푸시 사용(선택 사항)

푸시 알림에 대해 `background mode`를 활성화하려면 **백그라운드 푸시 활성화**를 선택합니다. 그러면 푸시 알림이 도착할 때 시스템이 애플리케이션을 `suspended` 상태에서 해제하여 애플리케이션이 푸시 알림에 대한 응답으로 콘텐츠를 다운로드할 수 있습니다. 제거 추적 기능을 사용하려면 이 옵션을 선택해야 합니다.

![Unity 에디터에 Braze 구성 옵션이 표시됩니다. 이 편집기에서는 'Unity iOS 통합 자동화', 'Braze와 푸시 통합', '백그라운드 푸시 활성화'가 활성화되어 있습니다.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### 2.4 단계: 자동 등록 비활성화(선택 사항)

푸시 알림을 아직 옵트인하지 않은 사용자는 애플리케이션을 열 때 자동으로 푸시 권한이 부여됩니다. 이 기능을 비활성화하고 푸시에 대해 사용자를 수동으로 등록하려면 **자동 푸시 등록 비활성화**를 선택합니다.

- iOS 12 이상에서 **임시 권한 부여 비활성화**를 선택하지 않으면 사용자에게 무음 푸시 수신 권한이 임시로(자동으로) 부여됩니다. 이 옵션을 선택하면 사용자에게 기본 푸시 프롬프트가 표시됩니다.
- 런타임에 프롬프트가 표시되는 시점을 정확하게 구성해야 하는 경우, Braze 구성 편집기에서 자동 등록을 비활성화하고 대신 `AppboyBinding.PromptUserForPushPermissions()`를 사용합니다.

![Unity 에디터에 Braze 구성 옵션이 표시됩니다. 이 편집기에서는 'Unity iOS 통합 자동화', 'Braze와 푸시 통합', '자동 푸시 등록 비활성화'가 활성화되어 있습니다.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### 2.1 단계: 업데이트 `AndroidManifest.xml`

앱에 `AndroidManifest.xml`이 없는 경우 다음을 템플릿으로 사용할 수 있습니다. 그렇지 않으면 이미 `AndroidManifest.xml`이 있는 경우 기존 `AndroidManifest.xml`에 다음 중 누락된 섹션이 추가되었는지 확인합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### 2.2 단계: ADM API 키를 저장하세요

먼저 [앱의 ADM API 키를 생성한](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials) 다음 `api_key.txt` 이라는 파일에 키를 저장하고 프로젝트의 [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) 디렉토리에 추가합니다.

{% alert important %}
Amazon은 `api_key.txt`에 후행 줄 바꿈과 같은 공백 문자가 포함된 경우 키를 인식하지 않습니다.
{% endalert %}

다음으로 `mainTemplate.gradle` 파일에 다음을 추가합니다:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### 2.3 단계: ADM Jar 추가

필수 ADM Jar 파일은 [Unity JAR 문서에](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) 따라 프로젝트의 어느 곳에나 배치할 수 있습니다.

#### 2.4 단계: Braze 대시보드에 클라이언트 비밀 및 클라이언트 ID 추가하기

마지막으로 [1단계](#unity_step-1-enable-adm)에서 얻은 클라이언트 비밀과 클라이언트 ID를 Braze 대시보드의 **설정 관리** 페이지에 추가해야 합니다.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### 3단계: 푸시 리스너 설정

{% tabs %}
{% tab Android %}
#### 3.1 단계: 푸시 수신 리스너 인에이블먼트

사용자가 푸시 알림을 받을 때 푸시 수신 리스너가 실행됩니다. 푸시 페이로드를 Unity로 보내려면 게임 오브젝트의 이름을 설정하고 **푸시 수신 리스너 설정** 아래에 수신된 리스너 콜백 메서드를 푸시합니다.

#### 3.2 단계: 푸시 열린 리스너 인에이블먼트 사용

사용자가 푸시 알림을 클릭하여 앱을 실행하면 푸시 열람 리스너가 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 열람 리스너 설정** 아래 게임 오브젝트의 이름과 푸시 열람 리스너 콜백 메서드를 설정합니다.

#### Step 3.3: 푸시 삭제된 리스너 인에이블먼트하기

푸시 삭제 리스너는 사용자가 푸시 알림을 밀거나 해제할 때 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 삭제 리스너 설정** 아래 게임 오브젝트의 이름과 푸시 삭제 리스너 콜백 메서드를 설정합니다.

#### 푸시 리스너 예제

다음 예제는 각각 `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, `PushNotificationDeletedCallback`이라는 콜백 메서드 이름을 사용하여 `BrazeCallback` 게임 오브젝트를 구현합니다.

![이 구현 예제 그래픽에서는 이전 섹션에서 언급한 Braze 구성 옵션과 C# 코드 스니펫을 보여줍니다.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### 3.1 단계: 푸시 수신 리스너 인에이블먼트

푸시 수신 리스너는 사용자가 애플리케이션을 적극적으로 사용하는 동안(예: 앱이 포그라운드 상태일 때) 푸시 알림을 수신할 때 실행됩니다. Braze 설정 에디터에서 푸시 수신 리스너를 설정합니다. 런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.PUSH_RECEIVED`를 지정합니다.

![Unity 에디터에 Braze 구성 옵션이 표시됩니다. 이 편집기에서는 '푸시 수신 리스너 설정' 옵션이 확장되어 있고 '게임 오브젝트 이름'(AppBoyCallback)과 '콜백 메서드 이름'(PushNotificationReceivedCallback)이 제공됩니다.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### 3.2 단계: 푸시 열린 리스너 인에이블먼트 사용

사용자가 푸시 알림을 클릭하여 앱을 실행하면 푸시 열람 리스너가 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 열람 리스너 설정** 옵션에서 게임 오브젝트의 이름과 푸시 열람 리스너 콜백 메서드를 설정합니다.

![Unity 에디터에 Braze 구성 옵션이 표시됩니다. 이 편집기에서는 '푸시 수신 리스너 설정' 옵션이 확장되어 있고 '게임 오브젝트 이름'(AppBoyCallback)과 '콜백 메서드 이름'(PushNotificationOpenedCallback)이 제공됩니다.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.PUSH_OPENED`를 지정합니다.

#### 푸시 리스너 예제

다음 예제는 각각 `PushNotificationReceivedCallback` 및 `PushNotificationOpenedCallback`이라는 콜백 메서드 이름을 사용하여 `AppboyCallback` 게임 오브젝트를 구현합니다.

![이 구현 예제 그래픽에서는 이전 섹션에서 언급한 Braze 구성 옵션과 C# 코드 스니펫을 보여줍니다.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
[이전 단계에서](#unity_step-21-update-androidmanifestxml) `AndroidManifest.xml` 을 업데이트하면 다음 줄을 추가하면 푸시 리스너가 자동으로 설정됩니다. 따라서 추가 설정이 필요하지 않습니다.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
ADM 푸시 리스너에 대해 자세히 알아보려면 [Amazon을 참조하세요: Amazon 기기 메시징 통합](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## 선택적 구성

{% tabs %}
{% tab Android %}
#### 인앱 리소스에 대한 딥링킹

Braze는 기본적으로 표준 딥링크(웹사이트 URL, Android URI 등)를 처리할 수 있지만, 커스텀 딥링크를 생성하려면 추가적인 매니페스트 설정이 필요합니다.

설정 지침은 [인앱 리소스에 대한 딥링킹을](https://developer.android.com/training/app-links/deep-linking) 참조하세요.

#### Braze 푸시 알림 아이콘 추가하기

프로젝트에 푸시 아이콘을 추가하려면 아이콘 이미지 파일이 포함된 안드로이드 아카이브(AAR) 플러그인 또는 안드로이드 라이브러리를 생성하세요. 단계와 자세한 내용은 유니티 설명서를 참조하세요: [안드로이드 라이브러리 프로젝트 및 안드로이드 아카이브 플러그인](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### 푸시 토큰 콜백

OS에서 Braze 기기 토큰의 사본을 수신하려면 `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`를 사용하여 위임을 설정합니다.
{% endtab %}

{% tab Amazon Device Messaging %}
현재 ADM에 대한 선택적 구성은 없습니다.
{% endtab %}
{% endtabs %}
