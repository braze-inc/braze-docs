---
nav_title: Android
article_title: Android 푸시 알림 for Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "이 참조 문서에서는 Unity 플랫폼용 Android 푸시 알림 통합을 다룹니다."

---

# Android 푸시 알림 통합

> 이 참조 문서에서는 Unity 플랫폼용 Android 푸시 알림 통합을 다룹니다.

이 지침은 [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/)과 푸시를 통합하기 위한 것입니다.

ADM 통합 지침은 [Unity ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/) 설명서를 참조하세요.

## 1단계: Firebase 활성화

시작하려면 [Firebase Unity 설정 설명서](https://firebase.google.com/docs/unity/setup)를 따르세요.

{% alert note %}
Firebase Unity SDK를 통합하면 `AndroidManifest.xml`이 재정의될 수 있습니다. 이 경우 원래대로 되돌려야 합니다.
{% endalert %}

## 2단계: Firebase 자격 증명 설정

Braze 대시보드에 Firebase 서버 키와 발신자 ID를 입력해야 합니다. 이렇게 하려면 [Firebase 개발자 콘솔에](https://console.firebase.google.com/) 로그인하고 Firebase 프로젝트를 선택합니다. 다음으로, **설정**에서 **클라우드 메시징**을 선택하고 서버 키와 발신자 ID를 복사합니다:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "파이어베이스서버키")

Braze에서 **설정 관리** 아래의 **앱 설정** 페이지에서 Android 앱을 선택합니다. 다음으로, **Firebase 클라우드 메시징 서버 키** 필드에 Firebase 서버 키를 입력하고 **Firebase 클라우드 메시징 발신자** ID 필드에 Firebase 발신자 ID를 입력합니다.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## 3단계: 자동 푸시 통합 구현

Braze SDK는 푸시 알림을 받기 위해 Firebase 클라우드 메시징 서버에 푸시 등록을 자동으로 처리할 수 있습니다.

![Unity 에디터는 Braze 구성 옵션을 표시합니다. 이 편집기에서 'Unity Android 통합 자동화', '푸시 알림 Firebase 푸시', '푸시 구성 푸시 딥링크 자동 처리', '푸시 구성 푸시 알림 HTML 렌더링 활성화됨', 및 '푸시 Deleted/Opened/Received 리스너 설정'이 설정됩니다. '파이어베이스 발신자 ID', '작은/큰 아이콘 그리기 가능', '기본 알림 강조 색상' 필드도 제공됩니다.]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "안드로이드 푸시 설정").

- **자동 Firebase 클라우드 메시징 등록 활성화됨**<br> Braze SDK가 기기에 대한 FCM 푸시 토큰을 자동으로 검색하고 전송하도록 지시합니다. 
- **Firebase Cloud Messaging 발송자 ID**<br> Firebase 콘솔의 발신자 ID.
- **푸시 딥링크를 자동으로 처리**<br> SDK가 푸시 알림을 클릭할 때 딥링크 열기 또는 앱 열기 중 어떤 처리 방식을 수행해야 하는지 여부.
- **작은 알림 아이콘 드로어블**<br>푸시 알림을 받을 때마다 드로어블이 작은 아이콘으로 표시되어야 합니다. 알림은 아이콘이 제공되지 않은 경우 애플리케이션 아이콘을 작은 아이콘으로 사용합니다.

## 4단계: 푸시 리스너 설정

사용자가 푸시 알림을 수신할 때 추가 단계를 수행하거나 Unity에 푸시 알림 페이로드를 전달하려는 경우 Braze는 푸시 알림 리스너를 설정하는 옵션을 제공합니다.

Braze에서 **설정 관리** 아래의 **앱 설정** 페이지에서 Android 앱을 선택합니다. 다음으로, **푸시 알림 설정** 필드에 Firebase 서버 키를 입력하고 **푸시 알림 설정** ID 필드에 Firebase 발신자 ID를 입력합니다.

#### 푸시 수신 리스너

사용자가 푸시 알림을 받을 때 푸시 수신 리스너가 실행됩니다. 푸시 페이로드를 Unity로 보내려면 게임 오브젝트의 이름을 설정하고 **푸시 수신 리스너 설정** 아래에 수신된 리스너 콜백 메서드를 푸시합니다.

#### 푸시 열람 리스너

사용자가 푸시 알림을 클릭하여 앱을 실행하면 푸시 열람 리스너가 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 열람 리스너 설정** 아래 게임 오브젝트의 이름과 푸시 열람 리스너 콜백 메서드를 설정합니다.

#### 푸시 삭제 리스너(Android 전용)

푸시 삭제 리스너는 사용자가 푸시 알림을 밀거나 해제할 때 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 삭제 리스너 설정** 아래 게임 오브젝트의 이름과 푸시 삭제 리스너 콜백 메서드를 설정합니다.

#### 푸시 리스너 구현 예제

다음 예제는 각각 `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, `PushNotificationDeletedCallback`이라는 콜백 메서드 이름을 사용하여 `BrazeCallback` 게임 오브젝트를 구현합니다.

![이 구현 예제 그래픽은 이전 섹션에서 언급한 Braze 구성 옵션과 C# 코드 스니펫을 보여줍니다.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android 전체 리스너 예제").

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

### 구현 예

[Braze Unity SDK 리포지토리](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples)의 샘플 프로젝트에는 FCM이 포함된 완전한 작동 샘플 앱이 포함되어 있습니다.

## 인앱 리소스에 대한 딥링킹

Braze는 기본적으로 표준 딥링크(웹사이트 URL, Android URI 등)를 처리할 수 있지만, 커스텀 딥링크를 생성하려면 추가적인 매니페스트 설정이 필요합니다.

설정 지침은 [인앱 리소스에 대한 딥링킹을](https://developer.android.com/training/app-links/deep-linking) 참조하세요.

## Braze 푸시 알림 아이콘 추가하기

프로젝트에 푸시 아이콘을 추가하려면 아이콘 이미지 파일이 포함된 안드로이드 아카이브(AAR) 플러그인 또는 안드로이드 라이브러리를 생성하세요. 단계와 자세한 내용은 유니티 설명서를 참조하세요: [안드로이드 라이브러리 프로젝트 및 안드로이드 아카이브 플러그인](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).