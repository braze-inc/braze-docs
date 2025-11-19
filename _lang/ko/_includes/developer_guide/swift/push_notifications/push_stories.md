{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 `UNNotification` 프레임워크 구현을 포함하여 [푸시 알림을 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

푸시 스토리를 받으려면 다음 최소 소프트웨어 개발 키트 버전이 필요합니다:

{% sdk_min_versions swift:5.0.0 %}

## 푸시 스토리 설정하기

### 1단계: 알림 콘텐츠 확장 대상 추가 {#notification-content-extension}

앱 프로젝트에서 메뉴 **파일 > 새로 만들기 > 타겟**로 이동하여 새 `Notification Content Extension` 타겟을 추가하고 활성화하세요.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode가 새 대상을 자동으로 생성하고 다음을 포함하여 파일을 자동으로 생성합니다.

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### 2단계: 기능 활성화 {#enable-capabilities}

Xcode에서 **서명 및 기능** 창을 사용하여 백그라운드 모드 기능을 기본 앱 대상에 추가합니다. **백그라운드 가져오기** 및 **원격 알림** 체크박스를 모두 선택합니다.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### 앱 그룹 추가

또한 Xcode의 **서명 및 기능** 창에서 기본 앱 대상과 알림 콘텐츠 확장 대상에 앱 그룹 기능을 추가합니다. 그런 다음 **+** 버튼을 클릭합니다. 앱의 번들 ID를 사용하여 앱 그룹을 만드십시오. 예를 들어 앱의 번들 ID가 `com.company.appname`인 경우 앱 그룹 이름을 `group.com.company.appname.xyz`로 지정할 수 있습니다.

{% alert important %}
이 컨텍스트에서 앱 그룹은 Braze 워크스페이스(이전 앱 그룹) ID가 아닌 Apple의 [앱 그룹 권한](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)을 의미합니다.
{% endalert %}

앱을 앱 그룹에 추가하지 않으면 푸시 페이로드에서 특정 필드를 채우지 못하고 예상대로 완전히 작동하지 않을 수 있습니다.

### 3단계: 앱 {#enable-capabilities}에 푸시 스토리 프레임워크 추가

{% tabs local %}
{% tab 스위프트 패키지 매니저 %}

[스위프트 패키지 매니저 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)를 수행한 후 `Notification Content Extension`에 `BrazePushStory`를 추가합니다.

![Xcode의 프레임워크 및 라이브러리에서 '+' 아이콘을 선택하여 프레임워크를 추가합니다.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

포드파일에 다음 줄을 추가합니다:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
리치 푸시를 구현하는 방법에 대한 지침은 [리치 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager)을 참조하세요.
{% endalert %}

Podfile을 업데이트한 후 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하고 `pod install`을 실행합니다.

{% endtab %}
{% tab 매뉴얼 %}

[GitHub 릴리스 페이지](https://github.com/braze-inc/braze-swift-sdk/releases)에서 최신 `BrazePushStory.zip`을 다운로드하여 압축을 푼 후 프로젝트의 `Notification Content Extension`에 `BrazePushStory.xcframework`를 추가합니다.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
**Do Not Embed**이(가) **Embed** 열의 **BrazePushStory.xcframework** 아래에 선택되어 있는지 확인하십시오.
{% endalert %}

{% endtab %}
{% endtabs %}

### 4단계: 알림 보기 컨트롤러 업데이트 {#enable-capabilities}

`NotificationViewController.swift`에서 헤더 파일을 가져오도록 다음 줄을 추가합니다.

```swift
import BrazePushStory
```

다음으로, [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/)를 상속하여 기본 구현을 대체합니다.

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### 커스텀 처리 푸시 스토리 이벤트

푸시 스토리 알림 이벤트를 처리하기 위해 자체 커스텀 로직을 구현하려면 위와 같이 `BrazePushStory.NotificationViewController`을(를) 상속하고 아래와 같이 [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) 메서드를 재정의하십시오.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

### 5단계: 알림 콘텐츠 확장 plist 설정 {#notification-content-extension}

`Notification Content Extension`의 `Info.plist` 파일을 열고 `NSExtension \ NSExtensionAttributes` 아래에서 다음 키를 추가 및 변경합니다.

| 키                                              | 유형    | 값                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | 문자열  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | 부울 | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | 숫자  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | 부울 | `YES`                  |

귀하의 `Info.plist` 파일은 다음 이미지와 일치해야 합니다:

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### 6단계: 주요 앱 {#update-braze}에서 Braze 통합 업데이트

Braze를 초기화하기 전에 앱 그룹의 이름을 Braze 구성의 [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) 속성에 할당하십시오.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
