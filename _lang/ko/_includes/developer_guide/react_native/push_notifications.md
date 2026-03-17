{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 푸시 알림 설정 {#setting-up-push-notifications}

### 1단계: 초기 설정을 완료하십시오

{% tabs local %}
{% tab Expo %}
#### 필수 조건

Expo를 푸시 알림에 사용하기 전에 [Braze Expo 플러그인 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo)을 해야 합니다.

#### 1.1단계: `app.json` 파일을 업데이트하세요.

다음으로 Android 및 iOS용 `app.json` 파일을 업데이트하세요:

- **Android:** `enableFirebaseCloudMessaging` 옵션을 추가하세요.
- **iOS:** `enableBrazeIosPush` 옵션을 추가하세요.

#### 1.2단계: Google 발신자 ID 추가

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음, <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정**을 선택합니다.

![ "설정" 메뉴가 열려 있는 Firebase 프로젝트입니다.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징**을 선택하고 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID**를 클립보드에 복사합니다.

![ "발신자 ID"가 강조 표시된 Firebase 프로젝트의 "클라우드 메시징" 페이지입니다.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

그런 다음, 프로젝트의 `app.json` 파일을 열고 `firebaseCloudMessagingSenderId` 속성정보를 클립보드의 발신자 ID로 설정합니다. 예를 들어, 다음과 같습니다.

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### 1.3단계: Google 서비스 JSON에 경로 추가

프로젝트의 `app.json` 파일에 `google-services.json` 파일의 경로를 추가합니다. 이 파일은 구성에서 `enableFirebaseCloudMessaging: true`를 설정할 때 필요합니다.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

[Expo 알림](https://docs.expo.dev/versions/latest/sdk/notifications/)과 같은 추가 푸시 알림 라이브러리를 사용하는 경우 기본 설정 지침 대신 이 설정을 사용해야 합니다.
{% endtab %}

{% tab Android Native %}
Braze Expo 플러그인을 사용하지 않거나 이러한 설정을 네이티브로 구성하려는 경우, [네이티브 Android 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)를 참조하여 푸시를 등록하세요.
{% endtab %}

{% tab iOS Native %}
Braze Expo 플러그인을 사용하지 않거나 이러한 설정을 네이티브로 구성하려는 경우, [네이티브 iOS 푸시 통합 가이드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)의 다음 단계를 참조하여 푸시를 등록하세요:

#### 1.1단계: 푸시 권한 요청

앱이 시작될 때 푸시 권한을 요청할 계획이 없다면, AppDelegate에서 `requestAuthorizationWithOptions:completionHandler:` 호출을 생략하세요. 그런 다음 [2단계](#reactnative_step-2-request-push-notifications-permission)로 건너뛰세요. 그렇지 않은 경우 [기본 iOS 통합 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration) 따르세요.

#### 1.2단계 (선택 사항): 푸시 키 마이그레이션

이전에 `expo-notifications`를 사용하여 푸시 키를 관리했다면 애플리케이션의 루트 폴더에서 `expo fetch:ios:certs`를 실행합니다. 이렇게 하면 푸시 키(.p8 파일)가 다운로드되며, 이를 Braze 대시보드에 업로드할 수 있습니다.
{% endtab %}
{% endtabs %}

### 2단계: 푸시 알림 권한 요청하기

`Braze.requestPushPermission()` 메서드(v1.38.0 이상에서 사용 가능)를 사용하여 iOS 및 Android 13 이상에서 사용자에게 푸시 알림에 대한 권한을 요청합니다. Android 12 이하에서는 이 방법을 사용할 수 없습니다.

이 메서드는 SDK가 iOS에서 사용자에게 요청할 권한을 지정하는 필수 매개변수를 사용합니다. 이러한 옵션은 Android에는 적용되지 않습니다.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### 2.1단계: 푸시 알림 듣기(선택 사항)

Braze가 수신 푸시 알림을 감지하고 처리한 이벤트를 추가로 구독할 수 있습니다. 리스너 키 `Braze.Events.PUSH_NOTIFICATION_EVENT`를 사용합니다.

{% alert important %}
iOS 푸시 수신 이벤트는 포그라운드 알림과 `content-available` 백그라운드 알림에 대해서만 트리거됩니다. 종료된 상태에서 받은 알림이나 `content-available` 필드가 없는 백그라운드 알림에 대해서는 트리거되지 않습니다.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### 푸시 알림 이벤트 필드

푸시 알림 필드의 전체 목록은 아래 표를 참조하세요:

| 필드 이름         | 유형      | Description |
| ------------------ | --------- | ----------- |
| `payload_type`     | 문자열    | 알림 페이로드 유형을 지정합니다. Braze React Native SDK에서 전송되는 두 개의 값은 `push_opened` 및 `push_received`입니다. |
| `url`              | 문자열    | 알림에 의해 열린 URL을 지정합니다. |
| `use_webview`      | 부울   | `true`인 경우 URL은 Modal 웹 보기에서 인앱으로 열립니다. `false`인 경우 기기 브라우저에서 URL이 열립니다. |
| `title`            | 문자열    | 알림의 제목을 나타냅니다. |
| `body`             | 문자열    | 알림의 본문 또는 콘텐츠 텍스트를 나타냅니다. |
| `summary_text`     | 문자열    | 알림의 요약 텍스트를 표시합니다. 이는 iOS의 `subtitle` 에서 매핑됩니다. |
| `badge_count`      | 숫자   | 알림의 배지 개수를 나타냅니다. |
| `timestamp`        | 숫자 | 애플리케이션이 페이로드를 수신한 시간을 나타냅니다. |
| `is_silent`        | 부울   | `true`인 경우 페이로드가 자동으로 수신됩니다. Android 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [Android에서 무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)을 참조하세요. iOS 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [iOS에서 무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)을 참조하세요. |
| `is_braze_internal`| 부울   | 지오펜스 동기화, 기능 플래그 동기화 또는 제거 추적과 같은 내부 SDK 기능에 대한 알림 페이로드가 전송된 경우 `true`입니다. 페이로드는 사용자 측에서 자동으로 수신됩니다. |
| `image_url`        | 문자열    | 알림 이미지와 연결된 URL을 지정합니다. |
| `braze_properties` | 객체    | 캠페인과 관련된 Braze 속성(키-값 쌍)을 나타냅니다. |
| `ios`              | 객체    | iOS 관련 필드를 나타냅니다. |
| `android`          | 객체    | Android 전용 필드를 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 3단계: 딥링킹 활성화(선택 사항)

푸시 알림이 클릭될 때 React 구성 요소 내에서 Braze가 딥 링크를 처리할 수 있도록 하려면, 먼저 [React Native Linking](https://reactnative.dev/docs/linking) 라이브러리에서 설명된 단계를 구현하거나 원하는 솔루션으로 진행하세요. 그런 다음 아래의 추가 단계를 따르세요.

딥링크 개념에 대한 자세한 내용은 [FAQ 문서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)를 참조하세요.

{% tabs local %}
{% tab Android Native %}
[Braze Expo 플러그인]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option)을 사용하는 경우, `androidHandlePushDeepLinksAutomatically`를 `true`로 설정하여 푸시 알림 딥 링크를 자동으로 처리할 수 있습니다.

대신 딥 링크를 수동으로 처리하려면, 네이티브 Android 설명서를 참조하세요: [딥 링크 추가]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

#### 3.1 단계: 앱 시작 시 푸시 알림 페이로드 저장

{% alert note %}
이는 React Native SDK 19.1.0부터 지원됩니다.
{% endalert %}

주 활동의 `onCreate()` 메서드에 `populateInitialPushPayloadFromIntent`을 추가하세요. 이것은 React Native가 초기 Intent 데이터를 캡처하기 위해 초기화되기 전에 호출되어야 합니다. For example:

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
  super.onCreate(savedInstanceState)
}
```

#### 3.2 단계: 닫힌 상태에서 딥 링크 처리하기

[React Native Linking](https://reactnative.dev/docs/linking)이 처리하는 기본 시나리오 외에도, `Braze.getInitialPushPayload` 메서드를 구현하고 푸시 알림에서 앱이 실행되지 않을 때 열리는 딥 링크를 고려하기 위해 `url` 값을 검색하세요. For example:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
이 메서드는 귀하의 플랫폼에 대한 3.1 단계에서의 네이티브 설정이 필요합니다. Braze Expo 플러그인을 사용하는 경우, 이는 자동으로 처리될 수 있습니다.
{% endalert %}

{% endtab %}
{% tab iOS Native %}
#### 3.1 단계: 앱 시작 시 푸시 알림 페이로드 저장
{% alert note %}
Braze Expo 플러그인을 사용하는 경우 3.1 단계를 건너뛰세요. 이 기능은 자동으로 처리됩니다.
{% endalert %}

iOS의 경우 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 `populateInitialPayloadFromLaunchOptions`를 추가합니다. For example:

{% subtabs local %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // ... Perform regular React Native setup

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```
{% endsubtab %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
) -> Bool {
  // ... Perform regular React Native setup

  let configuration = Braze.Configuration(apiKey: apiKey, endpoint: endpoint)
  configuration.triggerMinimumTimeInterval = 1
  configuration.logger.level = .info
  let braze = BrazeReactBridge.initBraze(configuration)
  AppDelegate.braze = braze
  registerForPushNotifications()
  BrazeReactUtils.shared().populateInitialPayload(fromLaunchOptions: launchOptions)

  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```
{% endsubtab %}
{% endsubtabs %}

#### 3.2 단계: 닫힌 상태에서 딥 링크 처리하기

[React Native Linking](https://reactnative.dev/docs/linking)이 처리하는 기본 시나리오 외에도, `Braze.getInitialPushPayload` 메서드를 구현하고 푸시 알림에서 앱이 실행되지 않을 때 열리는 딥 링크를 고려하기 위해 `url` 값을 검색하세요. For example:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
이 메서드는 귀하의 플랫폼에 대한 3.1 단계에서의 네이티브 설정이 필요합니다. Braze Expo 플러그인을 사용하는 경우, 이는 자동으로 처리될 수 있습니다.
{% endalert %}

#### Step 3.3: 유니버설 링크 활성화 (선택 사항)

[유니버설 링크]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links) 지원을 활성화하려면, 주어진 URL을 열지 여부를 결정하는 Braze 대리자를 구현한 다음, 이를 귀하의 Braze 인스턴스에 등록하세요.

{% subtabs local %}
{% subtab Swift %}
귀하의 `iOS` 디렉토리에 `BrazeReactDelegate.swift` 파일을 생성하고 다음을 추가하세요. `YOUR_DOMAIN_HOST`를 실제 도메인으로 교체하세요.

```swift
import Foundation
import BrazeKit
import UIKit

class BrazeReactDelegate: NSObject, BrazeDelegate {

  /// This delegate method determines whether to open a given URL.
  /// Reference the context to get additional details about the URL payload.
  func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
    if let host = context.url.host,
       host.caseInsensitiveCompare("YOUR_DOMAIN_HOST") == .orderedSame {
      // Sample custom handling of universal links
      let application = UIApplication.shared
      let userActivity = NSUserActivity(activityType: NSUserActivityTypeBrowsingWeb)
      userActivity.webpageURL = context.url
      // Routes to the `continueUserActivity` method, which should be handled in your AppDelegate.
      application.delegate?.application?(
        application,
        continue: userActivity,
        restorationHandler: { _ in }
      )
      return false
    }
    // Let Braze handle links otherwise
    return true
  }
}
```

그런 다음, 프로젝트의 `AppDelegate.swift` 파일의 `didFinishLaunchingWithOptions`에서 `BrazeReactDelegate`을 생성하고 등록하세요.

```swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  
  static var braze: Braze?
  
  // Keep a strong reference to the BrazeDelegate so it is not deallocated.
  private var brazeDelegate: BrazeReactDelegate?
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Other setup code (e.g., Braze initialization)
    
    brazeDelegate = BrazeReactDelegate()
    AppDelegate.braze?.delegate = brazeDelegate
    return true
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
귀하의 `iOS` 디렉토리에 `BrazeReactDelegate.h` 파일을 생성한 다음, 다음 코드 스니펫을 추가하세요.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

다음으로, `BrazeReactDelegate.m` 파일을 생성한 다음, 다음 코드 스니펫을 추가하세요. `YOUR_DOMAIN_HOST`를 실제 도메인으로 교체하세요.

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

그런 다음, 프로젝트의 `AppDelegate.m` 파일의 `didFinishLaunchingWithOptions`에서 `BrazeReactDelegate`을 생성하고 등록하세요.

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```
{% endsubtab %}
{% endsubtabs %}

예제 통합을 위해, 샘플 앱 [여기](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm)를 참조하세요.
{% endtab %}
{% endtabs %}

### 4단계: 전경 알림 처리하기

전경 알림 처리는 귀하의 플랫폼과 설정에 따라 다르게 작동합니다. 귀하의 통합에 맞는 접근 방식을 선택하세요:

{% tabs local %}
{% tab iOS %}
iOS의 경우, 전경 알림 처리는 네이티브 Swift 통합과 동일합니다. `handleForegroundNotification(notification:)`을(를) `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)` 구현 내에서 호출하십시오.

완전한 세부정보 및 코드 예제는 Swift 푸시 알림 설명서의 [전경 알림 처리]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#handling-foreground-notifications)을(를) 참조하십시오.
{% endtab %}

{% tab Android %}
Android의 경우, 전경 알림 처리는 기본 Android 통합과 동일합니다. `FirebaseMessagingService.onMessageReceived` 메서드 내에서 `BrazeFirebaseMessagingService.handleBrazeRemoteMessage`을(를) 호출하십시오.

완전한 세부정보 및 코드 예제는 Android 푸시 알림 설명서의 [전경 알림 처리]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications)을(를) 참조하십시오.
{% endtab %}

{% tab Expo %}
Expo 관리 워크플로에서는 기본 알림 핸들러를 직접 호출하지 않습니다. 대신, Expo Notifications API를 사용하여 전경 프레젠테이션을 제어하고, Braze Expo 플러그인이 기본 처리를 자동으로 처리합니다.

```javascript
import * as Notifications from 'expo-notifications';
import Braze from '@braze/react-native-sdk';

// Control foreground presentation in Expo
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,    // Show alert while in foreground
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// React to Braze push events
const subscription = Braze.addListener('pushNotificationEvent', (event) => {
  console.log('Braze push event', {
    type: event.payload_type,   // "push_received" | "push_opened"
    title: event.title,
    url: event.url,
    is_silent: event.is_silent,
  });
  // Handle deep links, custom behavior, etc.
});

// Handle initial payload when app launches via push
Braze.getInitialPushPayload((payload) => {
  if (payload) {
    console.log('Initial push payload', payload);
  }
});
```

{% alert note %}
Expo 관리 워크플로에서는 Braze Expo 플러그인이 기본 푸시 처리를 자동으로 처리합니다. 위에 표시된 Expo Notifications 프레젠테이션 옵션을 통해 전경 UI를 제어합니다.
{% endalert %}

베어 워크플로 통합의 경우, 대신 기본 iOS 및 Android 접근 방식을 따르십시오.
{% endtab %}
{% endtabs %}

### 5단계: 테스트 푸시 알림을 전송하십시오.

이 시점에서 기기에 알림을 보낼 수 있어야 합니다. 다음 단계에 따라 푸시 연동을 테스트하세요.

{% alert note %}
macOS 13부터 특정 기기에서는 Xcode 14 이상에서 실행되는 iOS 16 이상 시뮬레이터에서 푸시 알림을 테스트할 수 있습니다. 자세한 내용은 [Xcode 14 릴리스 노트](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)를 참조하세요.
{% endalert %}

1. `Braze.changeUserId('your-user-id')` 메서드를 호출하여 React Native 애플리케이션에서 활성 사용자를 설정하십시오.
2. **캠페인으로** 이동하여 새 푸시 알림 캠페인을 만듭니다. 테스트할 플랫폼을 선택합니다.
3. 테스트 알림을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id`를 추가하고 **테스트 보내기**를 클릭합니다. 곧 기기에서 알림을 받습니다.

![자신의 사용자 아이디를 테스트 수신자로 추가하여 푸시 알림을 테스트할 수 있는 Braze 푸시 캠페인을 보여줍니다.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Expo 플러그인 사용

Expo에 대한 푸시 알림을 [설정한 후](#reactnative_setting-up-push-notifications), 기본 Android 또는 iOS 레이어에서 코드를 작성할 필요 없이 다음 푸시 알림 동작을 처리하는 데 사용할 수 있습니다.

### Android 푸시를 추가 FMS로 전달하기

추가 Firebase 메시징 서비스(FMS)를 사용하려는 경우 애플리케이션에서 Braze에서 보낸 푸시가 아닌 푸시를 수신할 경우 호출할 대체 FMS를 지정할 수 있습니다. For example:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

### Expo 애플리케이션 서비스로 앱 확장 사용 {#app-extensions}

Expo 애플리케이션 서비스(EAS)를 사용하고 `enableBrazeIosRichPush` 또는 `enableBrazeIosPushStories`를 활성화한 경우 프로젝트의 각 앱 확장에 해당하는 번들 식별자를 선언해야 합니다. 이 단계에는 EAS로 코드 서명을 관리하도록 프로젝트를 구성한 방식에 따라 여러 가지 방법으로 접근할 수 있습니다.

한 가지 방법은 Expo의 [앱 확장 설명서](https://docs.expo.dev/build-reference/app-extensions/)에 따라 `app.json` 파일에서 `appExtensions` 구성을 사용하는 것입니다. 또는 Expo의 [로컬 자격 증명 설명서](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)에 따라 `credentials.json` 파일에서 `multitarget` 설정을 구성할 수도 있습니다.

### 문제 해결

이것은 Braze React Native SDK 및 Expo 플러그인과의 푸시 알림 통합을 위한 일반적인 문제 해결 단계입니다.

#### 푸시 알림이 작동을 멈췄습니다 {#troubleshooting-stopped-working}

Expo 플러그인을 통한 푸시 알림이 작동을 멈췄다면:

1. Braze SDK가 여전히 세션을 추적하고 있는지 확인하십시오.
2. SDK가 `wipeData`에 대한 명시적 또는 암시적 호출로 비활성화되지 않았는지 확인하십시오.
3. Expo 또는 관련 라이브러리에 대한 최근 업그레이드를 검토하십시오. Braze 구성과 충돌이 있을 수 있습니다.
4. 최근에 추가된 프로젝트 종속성을 검토하고 기존 푸시 알림 대리자 메서드를 수동으로 재정의하고 있는지 확인하십시오.

{% alert tip %}
iOS 통합의 경우, 프로젝트 종속성과의 잠재적 충돌을 식별하는 데 도움이 되는 [푸시 알림 설정 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications)를 참조할 수 있습니다.
{% endalert %}

#### 기기 토큰이 Braze {#troubleshooting-token-registration}에 등록되지 않습니다.

기기 토큰이 Braze에 등록되지 않으면 먼저 [푸시 알림이 작동을 멈췄습니다](#troubleshooting-stopped-working)를 검토하십시오.

문제가 지속되면 Braze 푸시 알림 구성에 간섭하는 별도의 종속성이 있을 수 있습니다. 제거하거나 대신 `Braze.registerPushToken`을 수동으로 호출해 볼 수 있습니다.
