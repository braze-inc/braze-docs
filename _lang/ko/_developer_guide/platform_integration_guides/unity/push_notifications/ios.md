---
nav_title: iOS
article_title: Unity용 푸시 알림
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "이 참조 문서에서는 Unity 플랫폼용 iOS 푸시 알림 통합을 다룹니다."

---

# iOS 푸시 알림 통합

> 이 참조 문서에서는 Unity 플랫폼용 iOS 푸시 알림 통합을 다룹니다.

## 1단계: 자동 또는 수동 푸시 통합 선택

Braze는 iOS 푸시 통합 자동화를 위한 네이티브 Unity 솔루션을 제공합니다.

- 빌드한 Xcode 프로젝트를 수정하여 수동으로 통합을 완료하려면 [기본 iOS 푸시 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)을 따릅니다
- 수동 통합에서 자동 통합으로 전환하는 경우 [자동 통합으로 전환]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios)의 지침을 따릅니다.
- 자동 푸시 알림 솔루션은 iOS 12의 임시 인증 기능을 활용하며 기본 푸시 프롬프트 팝업에서는 사용할 수 없습니다.

## 2단계: 자동 푸시 통합 구현

### 푸시 알림 구성

[iOS 푸시 알림 구성 문서에]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) 따라 `.p8` 파일을 사용하여 Braze를 구성할 수 있습니다.

### 자동 푸시 통합 사용

Unity 편집기에서 **Braze > Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.

푸시 알림에 사용자를 자동으로 등록하고, 푸시 토큰을 Braze에 전달하며, 푸시 열람 분석을 추적하고, 기본 푸시 알림 처리 기능을 활용하려면 **Braze와 푸시 통합**을 선택합니다.

### 백그라운드 푸시 사용(선택 사항)

푸시 알림에 대해 `background mode`를 활성화하려면 **백그라운드 푸시 활성화**를 선택합니다. 그러면 푸시 알림이 도착할 때 시스템이 애플리케이션을 `suspended` 상태에서 해제하여 애플리케이션이 푸시 알림에 대한 응답으로 콘텐츠를 다운로드할 수 있습니다. 제거 추적 기능을 사용하려면 이 옵션을 선택해야 합니다.

![Unity 에디터는 Braze 구성 옵션을 표시합니다. 이 에디터에서는 'Unity iOS 통합 자동화', '브레이즈와 푸시 통합', '백그라운드 푸시 활성화'가 활성화되어 있습니다.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### 자동 등록 비활성화(선택 사항)

푸시 알림을 아직 옵트인하지 않은 사용자는 애플리케이션을 열 때 자동으로 푸시 권한이 부여됩니다. 이 기능을 비활성화하고 푸시에 대해 사용자를 수동으로 등록하려면 **자동 푸시 등록 비활성화**를 선택합니다.

- iOS 12 이상에서 **임시 권한 부여 비활성화**를 선택하지 않으면 사용자에게 무음 푸시 수신 권한이 임시로(자동으로) 부여됩니다. 이 옵션을 선택하면 사용자에게 기본 푸시 프롬프트가 표시됩니다.
- 런타임에 프롬프트가 표시되는 시점을 정확하게 구성해야 하는 경우, Braze 구성 편집기에서 자동 등록을 비활성화하고 대신 `AppboyBinding.PromptUserForPushPermissions()`를 사용합니다.

![Unity 에디터는 Braze 구성 옵션을 표시합니다. 이 에디터에서는 "Unity iOS 통합 자동화", "푸시를 브라즈와 통합" 및 "자동 푸시 등록 비활성화"가 활성화되어 있습니다.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## 3단계: 푸시 리스너 설정

사용자가 푸시 알림을 수신할 때 추가 단계를 수행하거나 Unity에 푸시 알림 페이로드를 전달하려는 경우 Braze는 푸시 알림 리스너를 설정하는 옵션을 제공합니다.

### 푸시 수신 리스너

푸시 수신 리스너는 사용자가 애플리케이션을 적극적으로 사용하는 동안(예: 앱이 포그라운드 상태일 때) 푸시 알림을 수신할 때 실행됩니다. Braze 설정 에디터에서 푸시 수신 리스너를 설정합니다. 런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.PUSH_RECEIVED`를 지정합니다.

![Unity 에디터는 Braze 구성 옵션을 표시합니다. 이 에디터에서는 '푸시 수신 리스너 설정' 옵션이 확장되고 '게임 오브젝트 이름'(AppBoyCallback)과 '콜백 메서드 이름'(PushNotificationReceivedCallback)이 제공됩니다.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### 푸시 열람 리스너

사용자가 푸시 알림을 클릭하여 앱을 실행하면 푸시 열람 리스너가 실행됩니다. 푸시 페이로드를 Unity로 전송하려면 **푸시 열람 리스너 설정** 옵션에서 게임 오브젝트의 이름과 푸시 열람 리스너 콜백 메서드를 설정합니다.

![Unity 에디터는 Braze 구성 옵션을 표시합니다. 이 에디터에서는 '푸시 수신 리스너 설정' 옵션이 확장되고 '게임 오브젝트 이름'(AppBoyCallback)과 '콜백 메서드 이름'(PushNotificationOpenedCallback)이 제공됩니다.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.PUSH_OPENED`를 지정합니다.

### 푸시 리스너 구현 예제

다음 예제는 각각 `PushNotificationReceivedCallback` 및 `PushNotificationOpenedCallback`이라는 콜백 메서드 이름을 사용하여 `AppboyCallback` 게임 오브젝트를 구현합니다.

![이 구현 예제 그래픽은 이전 섹션에서 언급한 Braze 구성 옵션과 C# 코드 스니펫을 보여줍니다.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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

## 고급 기능

### 푸시 토큰 콜백

OS에서 Braze 기기 토큰의 사본을 수신하려면 `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`를 사용하여 위임을 설정합니다.

### 기타 기능

딥링크, 배지 수, 커스텀 사운드와 같은 고급 기능을 구현하려면 [기본 iOS 푸시 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)을 참조하세요.

