---
nav_title: 푸시 알림
article_title: 푸시 알림 Xamarin용
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "이 문서에서는 Xamarin 플랫폼용 Android, FireOS 및 iOS 푸시 알림 통합을 다룹니다."
channel: push
toc_headers: h2
---

# 푸시 알림 통합

> Xamarin용 Android, FireOS 및 iOS 푸시 알림을 설정하는 방법을 알아보세요.

## 필수 조건

이 기능을 사용하려면 [Xamarin 플랫폼용 Braze SDK를 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)해야 합니다.

## 푸시 알림 통합

{% tabs %}
{% tab android %}
{% alert tip %}
Java와 C# 사이에서 네임스페이스의 변경 방식을 확인하려면 GitHub에서 [Xample 샘플 앱](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp)을 참조하세요.
{% endalert %}

Xamarin용 푸시 알림을 통합하려면 기본 Android 푸시 알림 단계를 완료해야 합니다. 다음 단계는 요약에 불과합니다. 전체 설명을 보려면 [네이티브 푸시 알림 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/)를 참조하세요.

### 1단계: 프로젝트를 업데이트하세요

1. Android 프로젝트에 Firebase를 추가하세요.
2. Android 프로젝트의 `build.gradle`에 Cloud 메시징 라이브러리를 추가합니다.
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### 2단계: JSON 자격 증명 생성

1. Google Cloud에서 [Firebase 클라우드 메시징 API](https://console.cloud.google.com/apis/library/fcm.googleapis.com)를 활성화하세요.
2. **서비스 계정** > 프로젝트 > **서비스 계정 생성**을 선택한 다음, 서비스 계정 이름, ID 및 설명을 입력합니다. 완료되면 **생성하고 계속**을 선택하십시오.
3. **역할** 필드에서 역할 목록에서 **Firebase Cloud Messaging API 관리자**를 찾아 선택합니다.
4. **서비스 계정**에서 프로젝트를 선택한 다음, <i class="fa-solid fa-ellipsis-vertical"></i> **작업** > **키 관리** > **키 추가** > **새 키 생성**을 선택합니다. **JSON**을 선택한 다음, **생성**을 선택합니다.

### 3단계: JSON 자격 증명을 업로드하세요

1. Braze에서 <i class="fa-solid fa-gear"></i> **설정** > **앱 설정**을 선택합니다. Android 앱의 **푸시 알림 설정**에서 **Firebase**를 선택한 다음 **JSON 파일 업로드**를 선택하고 이전에 생성한 자격 증명을 업로드합니다. 완료되면 **저장**을 선택하십시오.
2. Firebase Console로 이동하여 자동 FCM 토큰 등록을 활성화합니다. 프로젝트를 열고 <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정**을 선택합니다. **클라우드 메시징**을 선택하고 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID** 필드의 숫자를 복사합니다.
3. Android Studio 프로젝트에서 다음을 `braze.xml`에 추가합니다.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
무음 푸시 알림을 보낼 때마다 Braze가 불필요한 네트워크 요청을 트리거하지 않도록 하려면 `Application` 클래스의 `onCreate()` 메서드에 구성된 모든 자동 네트워크 요청을 제거합니다. 자세한 내용은 [Android 개발자 참조를 참조하십시오: 애플리케이션](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### 1단계: 초기 설정을 완료하십시오

푸시를 사용해 애플리케이션을 설정하고 서버에 자격 증명을 저장하는 방법은 [Swift 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)을 참조하세요. 자세한 내용은 [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) 샘플 애플리케이션을 참조하세요.

### 2단계: 푸시 알림 권한 요청

이제 Xamarin SDK는 자동 푸시 설정을 지원합니다. 다음 코드를 Braze 인스턴스 구성에 추가하여 푸시 자동화 및 권한을 설정합니다.

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

자세한 내용은 [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) 샘플 애플리케이션을 참조하세요. 자세한 내용은 Xamarin 설명서의 [Xamarin.iOS의 향상된 사용자 알림](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos)을 참조하세요.
{% endtab %}
{% endtabs %}
