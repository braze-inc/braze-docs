---
nav_title: 통합 완료
article_title: iOS SDK 통합 완료
platform: iOS
description: "이 참조 문서에서는 통합 옵션 중 하나를 통해 Braze SDK를 설치한 후 해당 통합을 완료하는 방법을 보여줍니다."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 통합 완료

이 단계를 수행하기 전에 [Carthage]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/), [스위프트 패키지 매니저]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) 또는 [수동]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) 통합을 사용하여 SDK를 통합했는지 확인합니다.

## 1단계: 앱 위임 업데이트

{% tabs %}
{% tab OBJECTIVE-C %}

Braze SDK를 CocoaPods, Carthage와 통합하거나 [동적 수동 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/)을 사용하는 경우 `AppDelegate.m` 파일에 다음 코드 줄을 추가합니다

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

스위프트 패키지 매니저와 통합하거나 [정적 수동 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/)을 사용하는 경우 대신 이 줄을 사용합니다.

```objc
#import "AppboyKit.h"
```

그런 다음, `AppDelegate.m` 파일 내 `application:didFinishLaunchingWithOptions:` 메서드에 다음 스니펫을 추가합니다.

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

**설정 관리** 페이지에서 `YOUR-APP-IDENTIFIER-API-KEY` 을 올바른 값으로 업데이트합니다. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)를 참조하세요.

{% endtab %}
{% tab swift %}

Braze SDK를 CocoaPods, Carthage와 통합하거나 [동적 수동 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/)을 사용하는 경우 `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다

```swift
import Appboy_iOS_SDK
```

스위프트 패키지 매니저와 통합하거나 [정적 수동 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/)을 사용하는 경우 대신 이 줄을 사용합니다.

```swift
import AppboyKit
```
Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 설명서](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)를 참조하세요.

다음으로, `AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`에 다음 스니펫을 추가합니다.

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**설정 관리** 페이지에서 `YOUR-APP-IDENTIFIER-API-KEY` 을 올바른 값으로 업데이트합니다. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)를 참조하세요.

{% endtab %}
{% endtabs %}

{% alert note %}
`sharedInstance` 싱글톤은 `startWithApiKey:` 호출 전에 nil 상태입니다. 모든 Braze 기능을 사용하기 위한 전제 조건이기 때문입니다.
{% endalert %}

{% alert warning %}
애플리케이션의 메인 스레드에서 Braze를 초기화해야 합니다. 비동기적으로 초기화하면 기능이 손상될 수 있습니다.
{% endalert %}


## 2단계: 데이터 클러스터 지정

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않습니다. 기존 사용자 지정 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록을</a> 참조하세요.
{% endalert %}

### 컴파일 타임 엔드포인트 구성(권장)

기존 사용자 지정 엔드포인트가 있는 경우:
- Braze iOS SDK v3.0.2부터 `Info.plist` 파일을 사용하여 커스텀 지정 엔드포인트를 설정할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전 내에서 `Endpoint` 문자열 하위 항목을 추가하고 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`). Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy`의 사전 키를 사용해야 합니다.

Braze 담당자가 이미 [올바른 엔드포인트]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)를 알려드렸을 것입니다.

### 런타임 엔드포인트 구성

기존 사용자 지정 엔드포인트가 있는 경우:
- Braze iOS SDK v3.17.0 이상부터 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달된 `appboyOptions`매개변수 내 `ABKEndpointKey`를 통해 엔드포인트 설정을 재정의할 수 있습니다. 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`).

## SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하며 기본 통합이 완료됩니다. [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), [푸시 메시징]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) 및 전체 Braze 기능 스위트를 사용하려면 다음 문서를 참조하세요.

## 시작 시 Braze 사용자 지정

시작 시 Braze를 사용자 지정하려면 대신 Braze 초기화 메서드 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`를 사용하고 선택 사항인 Braze 시작 키, `NSDictionary`를 전달할 수 있습니다.
{% tabs %}
{% tab 목표-C %}

`AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions:` 메서드에서 다음 Braze 메서드를 추가합니다.

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

이 방법은 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 방법을 대체한다는 점에 유의하세요.

{% endtab %}
{% tab swift %}

`AppDelegate.swift`의 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` 메서드에 다음 Braze 메서드를 추가합니다. 여기서 `appboyOptions`는 시작 구성 값의 `Dictionary`입니다.

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

이 방법은 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 방법을 대체한다는 점에 유의하세요.

{% endtab %}
{% endtabs %}

이 메서드는 다음 매개변수와 함께 호출됩니다:

- `YOUR-APP-IDENTIFIER-API-KEY` - Braze 대시보드에서 [앱 식별자]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) API 키를 입력합니다.
- `application` - 현재 앱입니다.
- `launchOptions` - `application:didFinishLaunchingWithOptions:`에서 가져올 수 있는 옵션 `NSDictionary`.
- `appboyOptions` - Braze의 시작 구성 값이 포함된 선택적 `NSDictionary`.

Braze 시작 키 목록은 [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h)를 참조하세요.

## Appboy.sharedInstance() 및 Swift 널 지정 가능
일반적인 관행과는 다소 다르게 `Appboy.sharedInstance()` 싱글톤은 선택 사항입니다. `startWithApiKey:` 호출 전에 `sharedInstance`가 `nil`이고, 표준은 아니지만, 지연된 초기화를 사용할 수 있는 유효한 구현이 일부 있기 때문입니다.

Appboy의 `sharedInstance`(표준 구현)에 액세스하기 전에 `didFinishLaunchingWithOptions:` 위임에서 `startWithApiKey:`를 호출하면 `Appboy.sharedInstance()?.changeUser("testUser")`와 같은 선택적 체인을 사용하여 번거로운 확인 작업을 피할 수 있습니다. null이 아닌 `sharedInstance`를 가정하는 Objective-C 구현과 동등합니다.

## 추가 리소스

[전체 iOS 클래스 문서 모든 SDK 메서드에 대한 추가 지침은 전체](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html "iOS 클래스 문서에서") 확인할 수 있습니다.

