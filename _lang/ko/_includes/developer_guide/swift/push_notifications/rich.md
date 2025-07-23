{% multi_lang_include developer_guide/prerequisites/swift.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

## 리치 푸시 알림 설정하기

### 1단계: 서비스 확장 만들기

[알림 서비스 확장](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension)을 생성하려면 Xcode에서 **파일 > 새로 만들기 > 대상**으로 이동하고 **알림 서비스 확장**을 선택합니다.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

**애플리케이션에 임베드**가 애플리케이션에 확장을 임베드하도록 설정되었는지 확인합니다.

### 2단계: 알림 서비스 확장 설정하기

알림 서비스 확장은 앱에 번들로 제공되는 자체 바이너리입니다. [Apple 개발자 포털에서](https://developer.apple.com) 자체 앱 ID 및 프로비저닝 프로필을 사용하여 설정해야 합니다.

알림 서비스 확장 프로그램의 번들 ID는 기본 앱 대상의 번들 ID와 구별되어야 합니다. 예를 들어 앱의 번들 ID가 `com.company.appname`인 경우 서비스 확장에 `com.company.appname.AppNameServiceExtension`을 사용할 수 있습니다.

### 3단계: 리치 푸시 알림 통합

리치 푸시 알림을 `BrazeNotificationService`와 통합하는 방법에 대한 단계별 가이드는 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)을 참조하세요.

샘플을 보려면 예제 앱의 [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) 의 사용법을 참조하세요.

#### 앱에 리치 푸시 프레임워크 추가하기

{% tabs local %}
{% tab 스위프트 패키지 매니저 %}

[스위프트 패키지 매니저 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)를 수행한 후 다음을 수행하여 `Notification Service Extension`에 `BrazeNotificationService`를 추가합니다.

1. Xcode의 프레임워크 및 라이브러리에서 <i class="fas fa-plus"></i> 추가 아이콘을 선택하여 프레임워크를 추가합니다. <br><br>![더하기 아이콘은 Xcode의 프레임워크 및 라이브러리 아래에 있습니다.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. "BrazeNotificationService" 프레임워크를 선택합니다. <br><br>!["BrazeNotificationService 프레임워크는 열리는 모달에서 선택할 수 있습니다.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

포드파일에 다음을 추가합니다:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
푸시 스토리를 구현하는 방법은 [설명서를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager) 참조하세요.
{% endalert %}

Podfile을 업데이트한 후 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하고 `pod install`을 실행합니다.

{% endtab %}

{% tab 매뉴얼 %}

`Notification Service Extension` 에 `BrazeNotificationService.xcframework` 를 추가하려면 [수동 통합을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/) 참조하세요.

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### 자체 UNNotificationServiceExtension 사용

자체 UNNotificationServiceExtension을 사용해야 하는 경우 대신 `didReceive` 메서드에서 [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:))을 호출하면 됩니다.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### 4단계: 대시보드에서 리치 알림 만들기

마케팅팀은 대시보드에서 다양한 알림을 만들 수도 있습니다. 푸시 작성기를 통해 푸시 알림을 생성하고 이미지나 GIF를 첨부하거나 이미지, GIF 또는 비디오를 호스팅하는 URL을 제공하기만 하면 됩니다. 푸시 알림을 받으면 자산이 다운로드되므로 콘텐츠를 호스팅하는 경우 요청이 동시에 급증하는 상황에 대비해야 합니다.
