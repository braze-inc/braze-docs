{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 푸시 알림 설정하기 {#setting-up-push-notifications}

### 1단계: 초기 설정을 완료하십시오

{% tabs local %}
{% tab Expo %}
#### 필수 조건

푸시 알림에 Expo를 사용하려면 먼저 [Braze Expo 플러그인을 설정해야]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo) 합니다.

#### 1.1단계: `app.json` 파일 업데이트

다음으로 Android 및 iOS용 `app.json` 파일을 업데이트합니다:

- **Android:** `enableFirebaseCloudMessaging` 옵션을 추가합니다.
- **iOS:** `enableBrazeIosPush` 옵션을 추가합니다.

#### 1.2단계: Google 발신자 ID 추가

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음, <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정**을 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징**을 선택하고 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID**를 클립보드에 복사합니다.

!['발신자 ID'가 강조 표시된 Firebase 프로젝트의 '클라우드 메시징' 페이지.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

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

{% tab Android 네이티브 %}
Braze Expo 플러그인을 사용하지 않거나 대신 이러한 설정을 [네이티브로]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/) 구성하려는 경우 [네이티브 Android 푸시 통합 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/) 참조하여 푸시 등록을 하세요.
{% endtab %}

{% tab iOS 네이티브 %}
Braze Expo 플러그인을 사용하지 않거나 대신 이러한 설정을 [네이티브로]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 구성하려는 경우 [네이티브 iOS 푸시 통합 가이드의]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 다음 단계를 참조하여 푸시 등록을 하세요:

#### 1.1단계: 푸시 권한 요청하기

앱이 실행될 때 푸시 권한을 요청하지 않을 계획이라면 앱디렉티브에서 `requestAuthorizationWithOptions:completionHandler:` 호출을 생략하세요. 그런 다음 [2단계로](#reactnative_step-2-request-push-notifications-permission) 건너뜁니다. 그렇지 않은 경우 [기본 iOS 통합 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration) 따르세요.

#### 1.2단계(선택 사항): 푸시 키 마이그레이션

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

푸시 알림을 클릭했을 때 Braze가 React 컴포넌트 내부의 [딥링킹을](https://reactnative.dev/docs/linking) 처리하도록 인에이블먼트하려면 먼저 [React Native 링크](https://reactnative.dev/docs/linking) 라이브러리 또는 선택한 솔루션에 설명된 단계를 구현하세요. 그런 다음 아래의 추가 단계를 따르세요.

딥링크 개념에 대한 자세한 내용은 [FAQ 문서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)를 참조하세요.

{% tabs local %}
{% tab Android 네이티브 %}
[Braze Expo 플러그인을]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option) 사용하는 경우 `app.json` 에서 `androidHandlePushDeepLinksAutomatically` 을 `true` 으로 설정하여 푸시 알림 딥링크를 자동으로 처리할 수 있습니다.

대신 딥링크를 수동으로 처리하려면 기본 Android 설명서를 참조하세요: [딥링크 추가하기]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

{% endtab %}
{% tab iOS 네이티브 %}
#### 3.1 단계: 앱 실행 시 푸시 알림 페이로드 저장하기
{% alert note %}
이 단계는 자동으로 처리되는 기능이므로 Braze Expo 플러그인을 사용하는 경우 3.1단계를 건너뛰세요.
{% endalert %}

iOS의 경우 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 `populateInitialPayloadFromLaunchOptions`를 추가합니다. 예를 들어, 다음과 같습니다.

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

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

#### 3.2 단계: 닫힌 상태에서 딥링크 처리하기

[React Native Linking에서](https://reactnative.dev/docs/linking) 처리하는 기본 시나리오 외에도 `Braze.getInitialPushPayload` 메서드를 구현하고 `url` 값을 검색하여 앱이 실행 중이 아닐 때 앱을 여는 푸시 알림의 딥링킹을 고려하세요. For example:

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
React Native의 링킹 API는 앱 시작 시 경합 조건으로 인해 이 시나리오를 지원하지 않으므로 Braze는 이 해결 방법을 제공합니다.
{% endalert %}

#### 3.3 단계: 유니버설 링크 인에이블먼트(선택 사항)

[유니버설 링크]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links) 지원을 인에이블하려면 `iOS` 디렉터리에 `BrazeReactDelegate.h` 파일을 만든 다음 다음 코드 스니펫을 추가하세요.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

그런 다음 `BrazeReactDelegate.m` 파일을 만든 다음 다음 코드 스니펫을 추가합니다. `YOUR_DOMAIN_HOST` 을 실제 도메인으로 바꿉니다.

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

그런 다음 프로젝트의 `AppDelegate.m` 파일에 `BrazeReactDelegate` 을 생성하고 `didFinishLaunchingWithOptions` 에 등록합니다.

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

통합 예시는 [여기에서](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm) 샘플 앱을 참조하세요.
{% endtab %}
{% endtabs %}

### 4단계: 테스트 푸시 알림 보내기

이 시점에서 기기에 알림을 보낼 수 있어야 합니다. 다음 단계에 따라 푸시 연동을 테스트하세요.

{% alert note %}
macOS 13부터 특정 기기에서는 Xcode 14 이상에서 실행되는 iOS 16 이상 시뮬레이터에서 푸시 알림을 테스트할 수 있습니다. 자세한 내용은 [Xcode 14 릴리스 노트](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)를 참조하세요.
{% endalert %}

1. `Braze.changeUserId('your-user-id')` 메서드를 호출하여 React Native 애플리케이션에서 활성 사용자를 설정합니다.
2. **캠페인으로** 이동하여 새 푸시 알림 캠페인을 만듭니다. 테스트할 플랫폼을 선택합니다.
3. 테스트 알림을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id`를 추가하고 **테스트 보내기**를 클릭합니다. 곧 기기에서 알림을 받습니다.

![자신의 사용자 아이디를 테스트 수신자로 추가하여 푸시 알림을 테스트할 수 있는 Braze 푸시 캠페인을 보여줍니다.]({% image_buster /assets/img/react-native/push-notification-test.png %} "푸시 캠페인 테스트").

## 엑스포 플러그인 사용

[엑스포에 대한 푸시 알림을 설정한](#reactnative_setting-up-push-notifications) 후에는 기본 Android 또는 iOS 레이어에서 코드를 작성할 필요 없이 다음 푸시 알림 동작을 처리하는 데 사용할 수 있습니다.

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

다음은 Braze React Native SDK 및 Expo 플러그인과의 푸시 알림 통합에 대한 일반적인 문제 해결 단계입니다.

#### 푸시 알림이 작동을 멈췄습니다. {#troubleshooting-stopped-working}

엑스포 플러그인을 통한 푸시 알림이 작동을 멈춘 경우:

1. Braze 소프트웨어 개발 키트에서 세션을 추적하고 있는지 확인합니다.
2. `wipeData` 에 대한 명시적 또는 암시적 호출로 소프트웨어 개발 키트가 비활성화되지 않았는지 확인합니다.
3. 최근 업그레이드된 Expo 또는 관련 라이브러리가 Braze 구성과 충돌할 수 있으므로 이를 검토하세요.
4. 최근에 추가된 프로젝트 종속성을 검토하고 기존 푸시 알림 델리게이트 메서드를 수동으로 재정의하고 있는지 확인하세요.

{% alert tip %}
iOS 통합의 경우 [푸시 알림 설정 튜토리얼을](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) 참조하여 프로젝트 종속성과의 잠재적 충돌을 식별할 수도 있습니다.
{% endalert %}

#### 기기 토큰이 Braze에 등록되지 않습니다. {#troubleshooting-token-registration}

기기 토큰이 Braze에 등록되지 않는 경우 먼저 [푸시 알림 작동 중지를](#troubleshooting-stopped-working) 검토하세요.

문제가 지속되면 별도의 종속성이 Braze 푸시 알림 구성을 방해하고 있을 수 있습니다. 대신 제거하거나 `Braze.registerPushToken` 으로 직접 문의할 수 있습니다.
