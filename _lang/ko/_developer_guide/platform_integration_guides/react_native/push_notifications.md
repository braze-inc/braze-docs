---
nav_title: 푸시 알림
article_title: React Native용 푸시 알림
platform: React Native
page_order: 2
toc_headers: h2
description: "이 문서에서는 React Native에서 푸시 알림을 구현하는 방법을 다룹니다."
channel: push

---

# 푸시 알림 통합

> 이 참조 문서에서는 React Native의 푸시 알림을 설정하는 방법을 다룹니다. 푸시 알림을 통합하려면 각 기본 플랫폼을 개별적으로 설정해야 합니다. 나열된 각 가이드에 따라 설치를 완료합니다.

## 1단계: 초기 설정 완료

{% tabs %}
{% tab Expo %}
`app.json` 파일에서 `enableBrazeIosPush` 및 `enableFirebaseCloudMessaging` 옵션을 설정하여 각각 iOS 및 Android용 푸시를 활성화합니다. 자세한 내용은 [여기]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup)에서 구성 지침을 참조하세요.

[Expo 알림](https://docs.expo.dev/versions/latest/sdk/notifications/)과 같은 추가 푸시 알림 라이브러리를 사용하는 경우 기본 설정 지침 대신 이 설정을 사용해야 합니다.
{% endtab %}

{% tab Android %}
### 1.1단계: 푸시 등록하기

Google의 Firebase 클라우드 메시징(FCM) API를 사용하여 푸시에 등록합니다. 전체 안내 과정은 [기본 Android 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)의 다음 단계를 참조하세요:

1. [프로젝트에 Firebase를 추가합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [종속성에 클라우드 메시징을 추가합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [서비스 계정을 만듭니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [JSON 자격 증명을 생성합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Braze에 JSON 자격 증명을 업로드합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### 1.2단계: Google 발신자 ID 추가

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음, <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정**을 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징**을 선택하고 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID**를 클립보드에 복사합니다.

!['발신자 ID'가 강조 표시된 Firebase 프로젝트의 '클라우드 메시징' 페이지.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

그런 다음, 프로젝트의 `app.json` 파일을 열고 `firebaseCloudMessagingSenderId` 속성정보를 클립보드의 발신자 ID로 설정합니다. 예를 들어, 다음과 같습니다.

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### 1.3단계: Google 서비스 JSON에 경로 추가

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
{% endtab %}

{% tab iOS %}
### 1.1단계: APN 인증서 업로드

Apple 푸시 알림 서비스(APN) 인증서를 생성하고 이를 Braze 대시보드에 업로드합니다. 전체 안내 과정은 [APN 인증서 업로드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate)를 참조하세요.

### 1.2단계: 통합 방법 선택

앱이 실행될 때 푸시 권한을 요청하지 않으려면 AppDelegate에서 `requestAuthorizationWithOptions:completionHandler:` 호출을 생략하고 [2단계](#step-2-request-push-notifications-permission)로 건너뜁니다. 그렇지 않은 경우 [기본 iOS 통합 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration) 따르세요.

완료했으면 [1.3단계로](#step-13-migrate-your-push-key) 계속 진행합니다.

### 1.3단계: 푸시 키 마이그레이션

이전에 `expo-notifications`를 사용하여 푸시 키를 관리했다면 애플리케이션의 루트 폴더에서 `expo fetch:ios:certs`를 실행합니다. 이렇게 하면 푸시 키(.p8 파일)가 다운로드되며, 이를 Braze 대시보드에 업로드할 수 있습니다.
{% endtab %}
{% endtabs %}

## 2단계: 푸시 알림 권한 요청하기

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

### 2.1단계: 푸시 알림 듣기(선택 사항)

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

#### 푸시 알림 이벤트 필드

푸시 알림 필드의 전체 목록은 아래 표를 참조하세요:

| 필드 이름         | 유형      | 설명 |
| ------------------ | --------- | ----------- |
| `payload_type`     | 문자열    | 알림 페이로드 유형을 지정합니다. Braze React Native SDK에서 전송되는 두 개의 값은 `push_opened` 및 `push_received`입니다. |
| `url`              | 문자열    | 알림에 의해 열린 URL을 지정합니다. |
| `use_webview`      | 부울   | `true`인 경우 URL은 Modal 웹 보기에서 인앱으로 열립니다. `false`인 경우 기기 브라우저에서 URL이 열립니다. |
| `title`            | 문자열    | 알림의 제목을 나타냅니다. |
| `body`             | 문자열    | 알림의 본문 또는 콘텐츠 텍스트를 나타냅니다. |
| `summary_text`     | 문자열    | 알림의 요약 텍스트를 표시합니다. 이는 iOS의 `subtitle` 에서 매핑됩니다. |
| `badge_count`      | 숫자   | 알림의 배지 개수를 나타냅니다. |
| `timestamp`        | 숫자 | 애플리케이션이 페이로드를 수신한 시간을 나타냅니다. |
| `is_silent`        | 부울   | `true`인 경우 페이로드가 자동으로 수신됩니다. Android 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [Android에서 무음 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications)을 참조하세요. iOS 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [iOS에서 무음 푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)을 참조하세요. |
| `is_braze_internal`| 부울   | 지오펜스 동기화, 기능 플래그 동기화 또는 제거 추적과 같은 내부 SDK 기능에 대한 알림 페이로드가 전송된 경우 `true`입니다. 페이로드는 사용자 측에서 자동으로 수신됩니다. |
| `image_url`        | 문자열    | 알림 이미지와 연결된 URL을 지정합니다. |
| `braze_properties` | 객체    | 캠페인과 관련된 Braze 속성(키-값 쌍)을 나타냅니다. |
| `ios`              | 객체    | iOS 관련 필드를 나타냅니다. |
| `android`          | 객체    | Android 전용 필드를 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 3단계: 딥링킹 활성화(선택 사항)

푸시 알림을 클릭할 때 Braze가 React 구성요소 내부의 딥링크를 처리하게 하려면 추가 단계를 수행합니다.

{% tabs %}
{% tab Expo %}
[BrazeProject 샘플 앱](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)에는 딥링크 구현의 전체 예제가 포함되어 있습니다. 딥링크 개념에 대한 자세한 내용은 [FAQ 문서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)를 참조하세요.

{% endtab %}
{% tab Android %}
Android의 경우 딥링크를 설정하는 방법은 [기본 Android 앱에서 딥링크 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links) 방법과 동일합니다. Braze SDK가 푸시 딥링크를 자동으로 처리하게 하려면 `app.json`에서 `androidHandlePushDeepLinksAutomatically: true`를 설정합니다.

{% endtab %}
{% tab iOS %}
### 3.1단계: 딥링킹 기능 추가

iOS의 경우 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 `populateInitialUrlFromLaunchOptions`를 추가합니다. 예를 들어, 다음과 같습니다.

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
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### 3.2단계: 딥링크 처리 구성

앱을 여는 딥링크의 경우 `Linking.getInitialURL()` 메서드를 사용하고, 앱이 실행 중이 아닐 때 앱을 여는 푸시 알림 내부 딥링크의 경우 `Braze.getInitialURL` 메서드를 사용합니다. 예를 들어, 다음과 같습니다.

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
React Native의 링킹 API는 앱 시작 시 경합 조건으로 인해 이 시나리오를 지원하지 않으므로 Braze는 이 해결 방법을 제공합니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 4단계: 푸시 알림 표시 테스트

이 시점에서 기기에 알림을 보낼 수 있어야 합니다. 다음 단계에 따라 푸시 연동을 테스트하세요.

{% alert note %}
macOS 13부터 특정 기기에서는 Xcode 14 이상에서 실행되는 iOS 16 이상 시뮬레이터에서 푸시 알림을 테스트할 수 있습니다. 자세한 내용은 [Xcode 14 릴리스 노트](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)를 참조하세요.
{% endalert %}

1. `Braze.changeUserId('your-user-id')` 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. **캠페인으로** 이동하여 새 푸시 알림 캠페인을 만듭니다. 테스트할 플랫폼을 선택합니다.
3. 테스트 알림을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id`를 추가하고 **테스트 보내기**를 클릭합니다. 곧 기기에서 알림을 받습니다.

![자신의 사용자 아이디를 테스트 수신자로 추가하여 푸시 알림을 테스트할 수 있는 Braze 푸시 캠페인을 보여줍니다.]({% image_buster /assets/img/react-native/push-notification-test.png %} "푸시 캠페인 테스트").

## Android 푸시를 추가 FMS로 전달하기

추가 Firebase 메시징 서비스(FMS)를 사용하려는 경우 애플리케이션에서 Braze에서 보낸 푸시가 아닌 푸시를 수신할 경우 호출할 대체 FMS를 지정할 수 있습니다. 예를 들어, 다음과 같습니다.

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

## Expo로 앱 확장 구성

### iOS용 리치 푸시 알림 사용 설정하기

{% alert tip %}
Android에서는 기본적으로 리치 푸시 알림을 사용할 수 있습니다.
{% endalert %}

Expo를 사용하여 iOS에서 리치 푸시 알림을 활성화하려면 `app.json`의 `expo.plugins` 오브젝트에서 `enableBrazeIosRichPush` 속성정보를 `true`로 구성합니다.

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

마지막으로, 프로젝트의 자격 증명 구성에 이 앱 확장에 대한 번들 식별자를 추가합니다. `<your-app-bundle-id>.BrazeExpoRichPush`. 이 프로세스에 대한 자세한 내용은 [Expo 애플리케이션 서비스에서 앱 확장 사용](#app-extensions)을 참조하세요.

### iOS용 푸시 스토리 활성화하기

{% alert tip %}
푸시 스토리는 기본적으로 Android에서 사용할 수 있습니다.
{% endalert %}

Expo를 사용하여 iOS에서 푸시 스토리를 활성화하려면 애플리케이션에 대한 앱 그룹이 정의되어 있는지 확인합니다. 자세한 내용은 [앱 그룹 추가하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group) 참조하세요.

그런 다음, `enableBrazeIosPushStories` 속성정보를 `true`로 구성하고 `app.json`에 있는 `expo.plugins` 오브젝트의 `iosPushStoryAppGroup`에 앱 그룹 ID를 할당합니다.

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

마지막으로, 프로젝트의 자격 증명 구성에 이 앱 확장에 대한 번들 식별자를 추가합니다. `<your-app-bundle-id>.BrazeExpoPushStories`. 이 프로세스에 대한 자세한 내용은 [Expo 애플리케이션 서비스에서 앱 확장 사용](#app-extensions)을 참조하세요.

{% alert warning %}
Expo 애플리케이션 서비스와 함께 푸시 스토리를 사용하는 경우 `eas build`를 실행할 때 `EXPO_NO_CAPABILITY_SYNC=1` 플래그를 사용해야 합니다. 확장의 프로비저닝 프로필에서 앱 그룹 기능이 제거되는 것은 명령줄의 알려진 문제입니다.
{% endalert %}

### Expo 애플리케이션 서비스로 앱 확장 사용 {#app-extensions}

Expo 애플리케이션 서비스(EAS)를 사용하고 `enableBrazeIosRichPush` 또는 `enableBrazeIosPushStories`를 활성화한 경우 프로젝트의 각 앱 확장에 해당하는 번들 식별자를 선언해야 합니다. 이 단계에는 EAS로 코드 서명을 관리하도록 프로젝트를 구성한 방식에 따라 여러 가지 방법으로 접근할 수 있습니다.

한 가지 방법은 Expo의 [앱 확장 설명서](https://docs.expo.dev/build-reference/app-extensions/)에 따라 `app.json` 파일에서 `appExtensions` 구성을 사용하는 것입니다. 또는 Expo의 [로컬 자격 증명 설명서](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)에 따라 `credentials.json` 파일에서 `multitarget` 설정을 구성할 수도 있습니다.

