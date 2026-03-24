## React Native Braze SDK에 대한 설명

React Native Braze SDK를 통합하면 기본 분석 기능을 제공하고 iOS 및 Android 모두에 대해 하나의 코드베이스로 인앱 메시지 및 콘텐츠 카드를 통합할 수 있습니다.

## 새 아키텍처 호환성

다음 최소 SDK 버전은 [React Native의 새 아키텍처](https://reactnative.dev/docs/the-new-architecture/landing-page)를 사용하는 모든 앱과 호환됩니다:

{% sdk_min_versions reactnative:2.0.1 %}

SDK 버전 6.0.0부터 Braze는 React Native Turbo 모듈을 사용하며, 이는 새 아키텍처와 레거시 브리지 아키텍처 모두와 호환됩니다. 즉, 추가 설정이 필요하지 않습니다.

{% alert warning %}
iOS 앱이 `RCTAppDelegate`를 준수하고 이전 `AppDelegate` 설정을 따르는 경우, Turbo 모듈에서 이벤트를 구독할 때 발생할 수 있는 충돌을 방지하기 위해 [완전한 네이티브 설정](#reactnative_step-2-complete-native-setup)의 샘플을 검토하십시오.
{% endalert %}

## React Native SDK 통합하기

### 필수 조건

SDK를 통합하려면 React Native 버전 0.71 이상이 필요합니다. 지원되는 버전의 전체 목록은 [React Native SDK GitHub 리포지토리](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)를 참조하세요.

### 1단계: Braze 라이브러리를 통합하십시오

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

### 2단계: 설정 옵션 선택하기

Braze SDK는 Braze Expo 플러그인 또는 네이티브 레이어 중 하나를 통해 관리할 수 있습니다. Expo 플러그인을 사용하면 네이티브 레이어에서 코드를 작성하지 않고도 특정 SDK 기능을 구성할 수 있습니다. 앱의 요구 사항에 가장 적합한 옵션을 선택하십시오.

{% tabs %}
{% tab Expo %}
#### 2.1 단계: Braze Expo 플러그인을 설치하십시오

Braze React Native SDK 버전이 1.37.0 이상인지 확인합니다. 지원되는 버전의 전체 목록은 [Braze React Native 저장소](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support)를 확인하십시오.

Braze Expo 플러그인을 설치하려면 다음 명령을 실행하십시오:

```bash
npx expo install @braze/expo-plugin
```

#### 2.2 단계: 플러그인을 app.json에 추가하세요

귀하의 `app.json`에 Braze Expo 플러그인을 추가하십시오. 다음 구성 옵션을 제공할 수 있습니다:

| 방법                                        | 유형    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | 문자열  | 필수. 귀하의 Android 애플리케이션에 대한 [API 키]({{site.baseurl}}/api/identifier_types/)는 Braze 대시보드의 **설정 관리** 아래에 있습니다. |
| `iosApiKey`                                   | 문자열  | 필수. iOS 애플리케이션의 [API 키]({{site.baseurl}}/api/identifier_types/)는 Braze 대시보드의 **설정 관리** 아래에 있습니다.     |
| `baseUrl`                                     | 문자열  | 필수. 귀하의 애플리케이션에 대한 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 **설정 관리** 아래 Braze 대시보드에 위치해 있습니다.    |
| `enableBrazeIosPush`                          | 불리언 | iOS만 해당. iOS에서 푸시 알림을 처리하기 위해 Braze를 사용할지 여부. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.                       |
| `enableFirebaseCloudMessaging`                | 불리언 | Android만 해당. 푸시 알림에 Firebase 클라우드 메시징을 사용할지 여부. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.             |
| `firebaseCloudMessagingSenderId`              | 문자열  | Android만 해당. Firebase 클라우드 메시징 발신자 ID. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.                                    |
| `sessionTimeout`                              | 정수 | 애플리케이션의 Braze 세션 제한 시간(초).                                                                                               |
| `enableSdkAuthentication`                     | 불리언 | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부.      |
| `logLevel`                                    | 정수 | 애플리케이션의 로그 레벨. 기본 로그 수준은 8이며 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 활성화하려면 로그 수준 0을 사용합니다.    |
| `minimumTriggerIntervalInSeconds`             | 정수 | 트리거 사이의 최소 시간 간격(초) 기본값은 30초입니다.                                                                           |
| `enableAutomaticLocationCollection`           | 불리언 | 자동 위치 수집이 활성화되어 있는지 여부(사용자가 허용하는 경우).                                                                                  |
| `enableGeofence`                              | 불리언 | 지오펜스가 활성화되어 있는지 여부.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | 불리언 | 지오펜스 요청이 자동으로 이루어져야 하는지 여부.                                                                                                  |
| `dismissModalOnOutsideTap`                    | 불리언 | iOS만 해당. 사용자가 인앱 메시지 외부를 클릭할 때 모달 인앱 메시지가 해제되는지 여부.                                           |
| `androidHandlePushDeepLinksAutomatically`     | 불리언 | Android만 해당. Braze SDK가 푸시 딥링크를 자동으로 처리해야 하는지 여부.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | 불리언 | Android만 해당. 푸시 알림에서 텍스트 콘텐츠를 `android.text.Html.fromHtml`을 사용하여 HTML로 해석하고 렌더링할지 여부를 설정합니다.        |
| `androidNotificationAccentColor`              | 문자열  | Android만 해당. Android 알림 강조 색상을 설정합니다.                                                                                                |
| `androidNotificationLargeIcon`                | 문자열  | Android만 해당. Android 알림 큰 아이콘을 설정합니다.                                                                                                  |
| `androidNotificationSmallIcon`                | 문자열  | Android만 해당. Android 알림 작은 아이콘을 설정합니다.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | 불리언 | iOS만 해당. 앱 실행 시 푸시 권한에 대한 프롬프트를 사용자에게 표시해야 하는지 여부.                                                          |
| `enableBrazeIosRichPush`                      | 불리언 | iOS만 해당. iOS에 리치 푸시 기능을 활성화할지 여부.                                                                                                  |
| `enableBrazeIosPushStories`                   | 불리언 | iOS만 해당. iOS용 Braze 푸시 스토리를 활성화할지 여부.                                                                                                  |
| `iosPushStoryAppGroup`                        | 문자열  | iOS만 해당. iOS 푸시 스토리에 사용되는 앱 그룹.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | 불리언 | iOS만 해당. 장치 ID가 무작위로 생성된 UUID를 사용할지 여부.                                                                                       |
| `iosForwardUniversalLinks`                    | 불리언 | iOS만 해당. SDK가 자동으로 유니버설 링크를 인식하고 시스템 메서드로 전달해야 하는지 여부를 지정합니다(기본값: `false`). 활성화되면 SDK는 [앱에서 유니버설 링크 지원](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/)에 정의된 시스템 메서드로 유니버설 링크를 자동으로 전달합니다. React Native SDK v11.1.0 및 Expo Plugin v3.2.0에서 도입되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

예시 구성:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

##### 안드로이드 푸시 알림 아이콘 구성 {#android-push-icons}

`androidNotificationLargeIcon` 및 `androidNotificationSmallIcon`를 사용할 때, 아이콘 표시를 위한 최선의 관행을 따르십시오:

###### 아이콘 배치 및 형식

Braze Expo 플러그인으로 커스텀 푸시 알림 아이콘을 사용하려면:

1. [아이콘 요구 사항](#icon-requirements)에 자세히 설명된 Android의 요구 사항에 따라 아이콘 파일을 만드십시오.
2. 프로젝트의 Android 네이티브 디렉토리에 `android/app/src/main/res/drawable-<density>/`에 배치하십시오 (예: `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` 또는 유사한 위치).
3. 또는 React Native 디렉토리에서 자산을 관리하는 경우, Expo의 [app.json 아이콘 구성](https://docs.expo.dev/versions/latest/config/app/#icon)을 사용하거나 [Expo 구성 플러그인](https://docs.expo.dev/config-plugins/introduction/)을 만들어 아이콘을 Android 드로어블 폴더로 복사할 수 있습니다.

Braze Expo 플러그인은 Android의 드로어블 리소스 시스템을 사용하여 이러한 아이콘을 참조합니다.

###### 아이콘 요구 사항

- **작은 아이콘:** 투명한 배경에 흰색 실루엣이어야 합니다 (이것은 Android 플랫폼 요구 사항입니다)
- **큰 아이콘:** 풀 컬러 이미지일 수 있습니다
- **형식:** PNG 형식이 권장됩니다
- **이름 지정:** 소문자, 숫자 및 밑줄만 사용하십시오 (예: `my_large_icon.png`)

###### 구성 app.json에서

파일 이름 _확장자 없이_에 `@drawable/` 접두사를 사용하십시오. 예를 들어, 아이콘 파일 이름이 `large_icon.png`인 경우, `@drawable/large_icon`로 참조하십시오:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
상대 파일 경로(예: `src/assets/images/icon.png`)를 사용하지 않거나 아이콘을 참조할 때 파일 확장자를 포함하지 마십시오. Expo 플러그인은 사전 빌드 프로세스 후 Android 네이티브 폴더에서 아이콘을 올바르게 찾기 위해 `@drawable/` 접두사가 필요합니다.
{% endalert %}

###### 작동 방식

Braze Expo 플러그인은 Android `drawable` 디렉토리에서 아이콘 파일을 참조합니다. `npx expo prebuild`를 실행하면 Expo가 네이티브 Android 프로젝트 구조를 생성합니다. 아이콘은 빌드 프로세스 전에 Android `drawable` 폴더에 존재해야 합니다(수동으로 배치하거나 구성 플러그인을 통해 복사). 그런 다음 플러그인은 경로 또는 확장자 없이 이름으로 이러한 드로어블 리소스를 사용하도록 Braze SDK를 구성합니다. 그래서 `@drawable/` 접두사가 구성에서 필요합니다.

Android 알림 아이콘에 대한 자세한 내용은 [Android의 알림 아이콘 가이드라인](https://developer.android.com/develop/ui/views/notifications#icon)을 참조하십시오.

#### 2.3 단계: 애플리케이션 빌드 및 실행

응용 프로그램을 사전 빌드하면 Braze Expo 플러그인이 작동하는 데 필요한 네이티브 파일이 생성됩니다.

```bash
npx expo prebuild
```

[Expo 문서](https://docs.expo.dev/workflow/customizing/)에 지정된 대로, 애플리케이션을 실행합니다. 구성 옵션에 변경 사항을 적용하면 응용 프로그램을 다시 사전 빌드하고 실행해야 합니다.
{% endtab %}

{% tab Android %}

#### 2.1 단계: 리포지토리 추가

상위 수준 프로젝트 `build.gradle`에서 `buildscript` > `dependencies` 아래에 다음을 추가합니다.

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

이것은 프로젝트에 Kotlin을 추가합니다.

#### 2.2 단계: Braze SDK 구성

Braze 서버에 연결하려면 프로젝트의 `res/values` 폴더에서 `braze.xml` 파일을 생성합니다. 다음 코드를 붙여넣고 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 값으로 바꾸세요:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

`AndroidManifest.xml` 파일에 필요한 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze SDK 버전 12.2.0 이상에서는 `gradle.properties` 파일에 `importBrazeLocationLibrary=true` 을 설정하여 android-sdk-location 라이브러리를 자동으로 가져올 수 있습니다.
{% endalert %}

#### 2.3단계: 사용자 세션 추적 구현

`openSession()` 및 `closeSession()`에 대한 호출은 자동으로 처리됩니다.
`onCreate()` 메서드에 다음 코드를 추가하십시오: `MainApplication` 클래스:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### 2.4 단계: 의도 업데이트 처리

MainActivity에서 `android:launchMode`가 `singleTask`로 설정된 경우, `MainActivity` 클래스에 다음 코드를 추가합니다.

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### 2.1 단계: (선택 사항) 동적 XCFrameworks용 Podfile 구성

BrazeUI와 같은 특정 Braze 라이브러리를 Objective-C++ 파일에 가져오려면 `#import` 구문을 사용해야 합니다. Braze Swift SDK의 버전 7.4.0부터 바이너리는 이 구문과 호환되는 [동적 XCFrameworks로 선택적 배포 채널](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)을 사용합니다.

이 배포 채널을 사용하려면 Podfile에서 CocoaPods 소스 위치를 수동으로 재정의합니다. 샘플을 참조하고 `{your-version}`을 가져오려는 관련 버전으로 바꿉니다.

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### 2.2 단계: 포드 설치

React Native는 라이브러리를 기본 플랫폼에 자동으로 연결하므로 CocoaPods를 사용하여 SDK를 설치할 수 있습니다.

프로젝트의 루트 폴더에서:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

#### 2.3 단계: Braze SDK 구성

{% subtabs local %}
{% subtab SWIFT %}

`AppDelegate.swift` 파일 맨 위에서 Braze SDK를 가져옵니다.
```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)` 메서드에서 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 앱의 값으로 바꾸십시오. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate` 에 정적 속성을 생성하여 쉽게 액세스할 수 있도록 합니다:

{% alert note %}
우리의 예제는 React Native 설정에서 여러 추상화를 제공하는 [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)의 구현을 가정합니다. 앱에 다른 설정을 사용하는 경우 필요에 따라 구현을 조정하십시오.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

`AppDelegate.m` 파일 맨 위에서 Braze SDK를 가져옵니다.
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

`application:didFinishLaunchingWithOptions:` 메서드에서 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 앱의 값으로 바꾸십시오. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate` 에 정적 속성을 생성하여 쉽게 액세스할 수 있도록 합니다:

{% alert note %}
우리의 예제는 React Native 설정에서 여러 추상화를 제공하는 [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)의 구현을 가정합니다. 앱에 다른 설정을 사용하는 경우 필요에 따라 구현을 조정하십시오.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### 3단계: 라이브러리 가져오기

다음으로, React Native 코드에서 `import` 라이브러리를 가져옵니다. 자세한 내용은 [샘플 프로젝트](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)를 확인하십시오. 

```javascript
import Braze from "@braze/react-native-sdk";
```

### 4단계: 통합 테스트(선택 사항)

SDK 통합을 테스트하려면 앱에서 다음 코드를 호출하여 사용자에 대한 새 세션을 시작하십시오.

```javascript
Braze.changeUser("userId");
```

예를 들어, 앱 시작 시 사용자 ID를 할당할 수 있습니다.

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Braze 대시보드에서 [사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search)으로 이동하여 ID가 `some-user-id`와 일치하는 사용자를 찾습니다. 여기에서 세션 및 기기 데이터가 기록되었는지 확인할 수 있습니다.

## 다음 단계

Braze SDK를 통합한 후 일반 메시징 기능을 구현할 수 있습니다:

- [푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/): 사용자에게 푸시 알림을 설정하고 전송하세요
- [인앱 메시지]({{site.baseurl}}/developer_guide/in_app_messages/): 앱 내에서 상황별 메시지를 표시하세요
- [배너]({{site.baseurl}}/developer_guide/banners/): 앱 인터페이스에 지속적인 배너를 표시하세요
