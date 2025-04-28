---
nav_title: 초기 SDK 설정
article_title: 초기 소프트웨어 개발 키트 설정 for React Native
platform: React Native
page_order: 1
description: "이 참조에서는 React Native SDK를 소개하고 Android 및 iOS에서 기본적으로 통합하는 방법을 설명합니다."
search_rank: 1
---

# 초기 SDK 설정

> 이 참조 문서에서는 React Native용 Braze SDK를 설치하는 방법을 설명합니다. Braze React Native SDK를 설치하면 기본적인 분석 기능을 제공하며, 이를 통해 하나의 코드베이스에서 iOS 및 Android용 인앱 메시지와 콘텐츠 카드를 통합할 수 있습니다.

## 전제 조건 및 호환성

이 SDK를 설정하려면 React Native v0.71 이상이 필요합니다. 지원되는 버전의 전체 목록은 [React Native SDK GitHub 리포지토리](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)를 참조하세요.

### React Native 새로운 아키텍처 지원

{% sdk_min_versions reactnative:2.0.1 %}

## 새로운 아키텍처에서 Braze 사용

Braze React Native SDK는 SDK 버전 2.0.1 이상부터 [React Native New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page)을 사용하는 모든 앱과 호환됩니다.

SDK 버전 6.0.0부터 Braze는 내부적으로 React Native Turbo Module로 업그레이드되었으며, 여전히 새로운 아키텍처나 기존 브리지 아키텍처와 함께 사용할 수 있습니다. Turbo Module은 역호환성도 지원하므로 [체인지로그](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)에 언급된 주요 변경 사항과 React Native v0.70 이상의 요구 사항 외에는 마이그레이션 단계가 필요하지 않습니다.

{% alert warning %}
iOS 앱이 `RCTAppDelegate`를 준수하고 이 설명서 또는 Braze 샘플 프로젝트의 이전 `AppDelegate` 설정을 따른 경우 Turbo Module에서 이벤트에 가입할 때 충돌이 발생하지 않도록 [전체 기본 설정](#step-2-complete-native-setup)의 샘플을 참조해야 합니다.
{% endalert %}

## 1단계: Braze 라이브러리 통합

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

## 2단계: 기본 설정 완료

{% tabs %}
{% tab Expo %}

#### 2.1 단계: Braze Expo 플러그인을 설치하십시오

Braze React Native SDK 버전이 1.37.0 이상인지 확인합니다. 그런 다음, Braze Expo 플러그인을 설치합니다.

```bash
expo install @braze/expo-plugin
```

#### 2.2 단계: 플러그인을 app.json에 추가하세요

귀하의 `app.json`에 Braze Expo 플러그인을 추가하십시오. 다음 구성 옵션을 제공할 수 있습니다:

| 방법                                        | 유형    | 설명                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | 문자열  | 필수. 귀하의 Android 애플리케이션에 대한 [API 키]({{site.baseurl}}/api/identifier_types/)는 Braze 대시보드의 **설정 관리** 아래에 있습니다. |
| `iosApiKey`                                   | 문자열  | 필수. iOS 애플리케이션의 [API 키]({{site.baseurl}}/api/identifier_types/)는 Braze 대시보드의 **설정 관리** 아래에 있습니다.     |
| `baseUrl`                                     | 문자열  | 필수. 귀하의 애플리케이션에 대한 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 **설정 관리** 아래 Braze 대시보드에 위치해 있습니다.    |
| `enableBrazeIosPush`                          | 불리언 | iOS만 해당. iOS에서 푸시 알림을 처리하기 위해 Braze를 사용할지 여부. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.                       |
| `enableFirebaseCloudMessaging`                | 불리언 | Android만 해당. 푸시 알림에 Firebase 클라우드 메시징을 사용할지 여부. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.             |
| `firebaseCloudMessagingSenderId`              | 문자열  | Android만 해당. Firebase 클라우드 메시징 발신자 ID. React Native SDK v1.38.0 및 Expo 플러그인 v0.4.0에 도입되었습니다.                                    |
| `sessionTimeout`                              | 정수 | 애플리케이션의 Braze 세션 제한 시간(초).                                                                                               |
| `enableSdkAuthentication`                     | 불리언 | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부.      |
| `logLevel`                                    | 정수 | 애플리케이션의 로그 레벨. 기본 로그 수준은 8이며, 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 활성화하려면 로그 수준 0을 사용합니다.    |
| `minimumTriggerIntervalInSeconds`             | 정수 | 트리거 사이의 최소 시간 간격(초) 기본값은 30초입니다.                                                                           |
| `enableAutomaticLocationCollection`           | 불리언 | 자동 위치 수집이 활성화되어 있는지 여부(사용자가 허용하는 경우).                                                                                  |
| `enableGeofence`                              | 불리언 | 지오펜스가 활성화되어 있는지 여부.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | 불리언 | 지오펜스 요청이 자동으로 이루어져야 하는지 여부.                                                                                                  |
| `dismissModalOnOutsideTap`                    | 불리언 | iOS만 해당. 사용자가 인앱 메시지 외부를 클릭할 때 Modal 인앱 메시지의 해제 여부.                                           |
| `androidHandlePushDeepLinksAutomatically`     | 불리언 | Android만 해당. Braze SDK가 푸시 딥링크를 자동으로 처리해야 하는지 여부.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | 불리언 | Android만 해당. 푸시 알림에서 텍스트 콘텐츠를 `android.text.Html.fromHtml`을 사용하여 HTML로 해석하고 렌더링할지 여부를 설정합니다.        |
| `androidNotificationAccentColor`              | 문자열  | Android만 해당. Android 알림 강조 색상을 설정합니다.                                                                                                |
| `androidNotificationLargeIcon`                | 문자열  | Android만 해당. Android 알림 큰 아이콘을 설정합니다.                                                                                                  |
| `androidNotificationSmallIcon`                | 문자열  | Android만 해당. Android 알림 작은 아이콘을 설정합니다.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | 불리언 | iOS만 해당. 앱 실행 시 푸시 권한에 대한 프롬프트를 사용자에게 표시해야 하는지 여부.                                                          |
| `enableBrazeIosRichPush`                      | 불리언 | iOS만 해당. iOS에 리치 푸시 기능을 활성화할지 여부.                                                                                                  |
| `enableBrazeIosPushStories`                   | 불리언 | iOS만 해당. iOS용 Braze 푸시 스토리를 활성화할지 여부.                                                                                                  |
| `iosPushStoryAppGroup`                        | 문자열  | iOS만 해당. iOS 푸시 스토리에 사용되는 앱 그룹.                                                                                                       |
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
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
        }
      ],
    ]
  }
}
```

#### 2.3 단계: 애플리케이션 빌드 및 실행

애플리케이션을 미리 빌드하면 Braze SDK가 작동하는 데 필요한기본 파일이 생성됩니다.

```bash
expo prebuild
```

[Expo 문서](https://docs.expo.dev/workflow/customizing/)에 지정된 대로, 애플리케이션을 실행합니다. 구성 옵션을 변경하면 애플리케이션을 다시 빌드하고 실행해야 합니다.

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

그러면 프로젝트에 Kotlin이 추가됩니다.

#### 2.2 단계: Braze SDK 구성

Braze 서버에 연결하려면 프로젝트의 `res/values` 폴더에서 `braze.xml` 파일을 생성합니다. 다음 코드를 붙여넣고 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 값으로 바꾸세요:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
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

특정 Braze 라이브러리(예: BrazeUI)를 Objective-C++ 파일에 가져오려면 `#import` 구문을 사용해야 합니다. Braze Swift SDK의 버전 7.4.0부터 바이너리는 이 구문과 호환되는 [동적 XCFrameworks로 선택적 배포 채널](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)을 사용합니다.

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
cd ios && RCT_NEW_ARCH_ENABLED=1 pod install

# To install using the React Native legacy architecture
cd ios && pod install
```

#### 2.3 단계: Braze SDK 구성

{% subtabs local %}
{% subtab SWIFT %}

`AppDelegate.swift` 파일 맨 위에서 Braze SDK를 가져옵니다.
```swift
import BrazeKit
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

## 3단계: 사용량

설치가 완료되면 React Native 코드에서 라이브러리 `import` 작업을 수행할 수 있습니다.

```javascript
import Braze from "@braze/react-native-sdk";
```

자세한 내용은 [샘플 프로젝트](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)를 참조하십시오.

## 기본 통합을 테스트하십시오

이 시점에서는 대시보드에서 세션 통계를 확인하여 SDK가 통합되었는지 확인할 수 있습니다. 어느 플랫폼에서든 애플리케이션을 실행하면 대시보드( **개요** 섹션)에 새 세션이 표시됩니다.

특정 사용자를 위한 세션을 시작하려면 앱에서 다음 코드를 호출하십시오.

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

그런 다음, 대시보드의 [사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search)에서 `some-user-id`로 사용자를 검색할 수 있습니다. 여기에서 세션 및 디바이스 데이터가 기록되었는지 확인할 수 있습니다.


