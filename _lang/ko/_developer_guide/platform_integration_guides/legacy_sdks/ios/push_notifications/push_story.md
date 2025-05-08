---
nav_title: 푸시 스토리
article_title: iOS용 푸시 스토리
platform: iOS
page_order: 27
description: "이 참조 문서에서는 iOS 애플리케이션에 푸시 스토리를 설정하는 방법을 설명합니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 푸시 스토리 설정

푸시 스토리 기능을 사용하려면 `UNNotification` 프레임워크와 iOS 10이 필요합니다. 이 기능은 iOS SDK 버전 3.2.1부터 사용할 수 있습니다.

## 1단계: 앱에서 푸시 활성화

[푸시 알림 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)에 따라 앱에서 푸시를 활성화합니다.

## 2단계: 알림 콘텐츠 확장 대상 추가하기

앱 프로젝트에서 **파일 > 새로 만들기 > 대상...** 메뉴로 이동하여 새 `Notification Content Extension` 대상을 추가하고 활성화합니다.

![]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode가 새 대상을 자동으로 생성하고 다음을 포함하여 파일을 자동으로 생성합니다.

{% tabs %}
{% tab 목표-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## 3단계: 기능 활성화

푸시 스토리 기능을 사용하려면 기본 앱 대상의 **기능** 섹션에서 백그라운드 모드가 필요합니다. 백그라운드 모드를 켠 후 **백그라운드 가져오기** 및 **원격 알림**을 선택합니다.

![]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### 앱 그룹 추가

또한 `Capability App Groups` 을 추가해야 합니다. 앱에 앱 그룹이 없으면 기본 앱 대상의 **기능**으로 이동하여 `App Groups`을 켜고 **+** 버튼을 클릭합니다. 앱의 번들 ID를 사용하여 앱 그룹을 생성합니다. 예를 들어 앱의 번들 ID가 `com.company.appname`인 경우 앱 그룹 이름을 `group.com.company.appname.xyz`로 지정할 수 있습니다. 기본 앱과 콘텐츠 확장 대상 모두에 대해 `App Groups`을 켜야 합니다.

{% alert important %}
이 컨텍스트에서 `App Groups`은 Braze 워크스페이스(이전 앱 그룹) ID가 아닌 Apple의 [앱 그룹 권한](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)을 의미합니다.
{% endalert %}

앱을 앱 그룹에 추가하지 않으면 앱이 푸시 페이로드의 특정 필드를 채우지 못하고 예상대로 완전히 작동하지 않을 수 있습니다.

## 4단계: 앱에 푸시 스토리 프레임워크 추가하기

{% tabs local %}
{% tab 스위프트 패키지 매니저 %}

[스위프트 패키지 매니저 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/)를 수행한 후 `Notification Content Extension`에 `AppboyPushStory`를 추가합니다.

![Xcode의 프레임워크 및 라이브러리에서 '+' 아이콘을 선택하여 프레임워크를 추가합니다.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

포드파일에 다음 줄을 추가합니다:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Podfile을 업데이트한 후 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하고 `pod install`을 실행합니다.

{% endtab %}
{% tab 매뉴얼 %}

[GitHub 릴리스 페이지](https://github.com/Appboy/appboy-ios-sdk/releases)에서 최신 `AppboyPushStory.zip`을 다운로드하여 압축을 푼 후 프로젝트의 `Notification Content Extension`에 다음 파일을 추가합니다.
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
**Do Not Embed**이(가) **Embed** 열의 **AppboyPushStory.xcframework** 아래에 선택되어 있는지 확인하십시오.
{% endalert %}

**빌드 설정 > 기타 링커 플래그**에서 프로젝트의 `Notification Content Extension`에 `-ObjC` 플래그를 추가합니다.

{% endtab %}
{% endtabs %}

## 5단계: 알림 보기 컨트롤러 업데이트하기

{% tabs %}
{% tab OBJECTIVE-C %}

`NotificationViewController.h` 에 다음 줄을 추가하여 새 속성을 추가하고 헤더 파일을 가져옵니다:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

`NotificationViewController.m` 에서 기본 구현을 제거하고 다음 코드를 추가합니다:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

`NotificationViewController.swift` 에 다음 줄을 추가하여 헤더 파일을 가져옵니다:

```swift
import AppboyPushStory
```

그런 다음 기본 구현을 제거하고 다음 코드를 추가합니다:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }
    
  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }
    
  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## 6단계: 알림 콘텐츠 확장 스토리보드 설정

`Notification Content Extension` 스토리보드를 열고 알림 보기 컨트롤러에 새 `UIView` 을 배치합니다. 클래스 이름을 `ABKStoriesView` 로 변경합니다. 알림 보기 컨트롤러의 기본 보기 프레임에 맞게 보기 너비와 높이를 자동 크기 조정할 수 있도록 설정합니다.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

그런 다음, 알림 보기 컨트롤러의 `storiesView` IBOutlet을 추가된 `ABKStoriesView`에 연결합니다.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## 7단계: 알림 콘텐츠 확장 목록 설정

`Notification Content Extension`의 `Info.plist` 파일을 열고 `NSExtension \ NSExtensionAttributes` 아래에서 다음 키를 추가 및 변경합니다.

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` 유형)
`UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` 유형)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (`Number` 유형)

![]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## 8단계: 기본 앱에서 Braze 연동 업데이트하기

##### 옵션 1: 런타임

Braze 인스턴스를 구성하는 데 사용되는 `appboyOptions` 사전에서 `ABKPushStoryAppGroupKey` 항목을 추가하고 값을 워크스페이스 API 식별자로 설정합니다.

{% tabs %}
{% tab 목표-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### 옵션 2: Info.plist

또는 `Info.plist` 파일에서 푸시 스토리 작업 영역을 구성하려면 `Info.plist` 파일에 `Braze` 이라는 사전을 추가합니다. `Braze` 사전 내에서 문자열 형식의 `PushStoryAppGroup` 하위 항목을 추가하고 값을 워크스페이스 식별자로 설정합니다. Braze iOS SDK v4.0.2 이전 버전에서는 `Appboy` 대신 `Braze`의 사전 키를 사용해야 합니다.

## 다음 단계

다음으로 푸시 스토리 메시지에 버튼이 표시되는 데 필요한 [작업 버튼]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/) 통합 단계를 참조하세요.


