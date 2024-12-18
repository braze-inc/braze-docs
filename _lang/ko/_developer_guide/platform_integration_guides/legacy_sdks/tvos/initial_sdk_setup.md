---
nav_title: 초기 SDK 설정
article_title: tvOS용 초기 SDK 설정
platform: tvOS
page_order: 0
page_type: reference
description: "이 페이지에서는 tvOS Braze SDK의 초기 설정 단계를 다룹니다."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 초기 SDK 설정

> 이 참조 문서에서는 tvOS용 Braze SDK를 설치하는 방법을 설명합니다. Braze SDK를 설치하면 기본적인 분석 기능을 사용할 수 있습니다.

{% alert note %}
현재 tvOS SDK는 분석 기능을 지원합니다. 대시보드에 tvOS 앱을 추가하려면 [지원 티켓]({{site.baseurl}}/braze_support/)을 엽니다.
{% endalert %}

tvOS Braze SDK는 Objective-C 및 Swift 프로젝트의 종속성 매니저인 [CocoaPods](http://cocoapods.org/)를 사용하여 설치하거나 업데이트해야 합니다. CocoaPods를 사용하면 통합과 업데이트가 더욱 간편해집니다.

## tvOS SDK CocoaPods 통합

### 1단계: CocoaPods 설치

tvOS [CocoaPods](http://cocoapods.org/)를 통해 SDK를 설치하면 대부분의 설치 과정이 자동으로 수행됩니다. 이 프로세스를 시작하기 전에 [Ruby 버전 2.0.0](https://www.ruby-lang.org/en/installation/) 이상을 사용 중인지 확인합니다.

시작하려면 다음 명령을 실행하세요:

```bash
$ sudo gem install cocoapods
```

- `rake` 실행 파일을 덮어쓰라는 메시지가 표시되면 자세한 내용은 CocoaPods.org에서 [시작하기의 코코아팟](http://guides.cocoapods.org/using/getting-started.html "설치 안내를")(  ) 참조하세요.
- CocoaPods와 관련된 문제가 있는 경우 CocoaPods 문제 [해결 가이드CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "문제 해결 가이드를") 참조하세요.

### 2단계: Podfile 구성

CocoaPods Ruby Gem을 설치했으므로 Xcode 프로젝트 디렉토리에 `Podfile` 파일을 만들어야 합니다.

포드파일에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

포드 업데이트에서 부 버전 업데이트보다 작은 내용을 자동으로 가져올 수 있도록 Braze 버전을 설정하는 것이 좋습니다. `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`와 유사합니다. 최신 Braze SDK 버전을 자동으로 통합하려면 주요 변경 사항이 있어도 Podfile에서 `pod 'Appboy-tvOS-SDK'`를 사용하면 됩니다.

### 3단계: Braze SDK 설치하기

Braze SDK CocoaPods를 설치하려면 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하여 다음 명령을 실행합니다.
```
pod install
```

이때 CocoaPods에서 생성한 새 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용해야 합니다. 

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### 4단계: 앱 위임 업데이트

{% tabs %}
{% tab 목표-C %}

`AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

`AppDelegate.m` 파일 내에 `application:didFinishLaunchingWithOptions` 메서드에 다음 스니펫을 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

마지막으로 **설정 관리** 페이지에서 `YOUR-API-KEY` 을 올바른 값으로 업데이트합니다.

{% endtab %}
{% tab swift %}

Braze SDK를 CocoaPods 또는 Carthage와 통합하는 경우 `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다

```swift
import AppboyTVOSKit
```

Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 설명서](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)를 참조하세요.

`AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`에 다음 스니펫을 추가합니다.

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

그런 다음 **설정 관리** 페이지에서 `YOUR-API-KEY` 을 올바른 값으로 업데이트합니다.

`sharedInstance` 싱글톤은 `startWithApiKey:` 호출 전에 nil 상태입니다. 모든 Braze 기능을 사용하기 위한 전제 조건이기 때문입니다.

{% endtab %}
{% endtabs %}

{% alert warning %}
애플리케이션의 메인 스레드에서 Braze를 초기화해야 합니다. 비동기적으로 초기화하면 기능이 손상될 수 있습니다.
{% endalert %}

### 5단계: 사용자 지정 엔드포인트 또는 데이터 클러스터 지정

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않으며, 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a>을 참조하십시오.
{% endalert %}

Braze 담당자가 이미 [올바른 엔드포인트]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).를 알려드렸을 것입니다.

#### 컴파일 타임 엔드포인트 구성(권장)
기존 사용자 지정 엔드포인트가 있는 경우:
- Braze iOS SDK v3.0.2부터 `Info.plist` 파일을 사용하여 커스텀 지정 엔드포인트를 설정할 수 있습니다. Info.plist 파일에 `Appboy` 사전을 추가합니다. `Appboy` 사전 내에서 `Endpoint` 문자열 하위 항목을 추가하고 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`).

#### 런타임 엔드포인트 구성
기존 사용자 지정 엔드포인트가 있는 경우:
- Braze iOS SDK v3.17.0+부터 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달된 `appboyOptions`매개변수 내 `ABKEndpointKey`를 통해 엔드포인트 설정을 재정의할 수 있습니다. 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`).

{% alert note %}
`ABKAppboyEndpointDelegate`를 사용하여 런타임에 엔드포인트를 설정하는 지원은 Braze iOS SDK v3.17.0에서 제거되었습니다. 이미 `ABKAppboyEndpointDelegate`를 사용하고 있는 경우, Braze iOS SDK 버전 v3.14.1~v3.16.0에서는 `getApiEndpoint()` 메서드에서 `dev.appboy.com`에 대한 참조를 `sdk.iad-01.braze.com`에 대한 참조로 바꾸어야 합니다.
{% endalert %}

### SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하며 기본 통합이 완료됩니다. tvOS 앱 및 기타 서드파티 라이브러리를 컴파일할 때는 Bitcode를 활성화해야 합니다.

### CocoaPod를 통해 Braze SDK 업데이트하기

CocoaPod를 업데이트하려면 프로젝트 디렉토리에서 다음 명령을 실행하면 됩니다:

```
pod update
```

## 시작 시 Braze 사용자 지정

시작 시 Braze를 사용자 지정하려면 대신 Braze 초기화 메서드 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`를 사용하고 선택 사항인 Braze 시작 키, `NSDictionary`를 전달할 수 있습니다.
{% tabs %}
{% tab 목표-C %}

`AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions` 메서드에서 다음 Braze 메서드를 추가합니다.

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

`AppDelegate.swift` 에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` 메소드 내에 다음 Braze 메소드를 추가합니다:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

여기서 `appboyOptions`는 시작 구성 값의 `Dictionary`입니다.

{% endtab %}
{% endtabs %}

이 메서드는 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 메서드를 대체하며 다음 매개변수와 함께 호출됩니다.

- `YOUR-API-KEY`: 애플리케이션의 API 키는 Braze 대시보드의 **설정 관리**에서 찾을 수 있습니다.
- `application`: 현재 앱입니다.
- `launchOptions`: `application:didFinishLaunchingWithOptions:`에서 가져올 수 있는 옵션 `NSDictionary`.
- `appboyOptions`: Braze의 시작 구성 값이 포함된 선택적 `NSDictionary`.

Braze 시작 키 목록은 [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)를 참조하세요.

## Appboy.sharedInstance() 및 Swift 널 지정 가능
일반적인 관행과는 다소 다르게 `Appboy.sharedInstance()` 싱글톤은 선택 사항입니다. `startWithApiKey:` 호출 전에 `sharedInstance`가 `nil`이고, 표준은 아니지만, 지연된 초기화를 사용할 수 있는 유효한 구현이 일부 있기 때문입니다.

Appboy의 `sharedInstance`(표준 구현)에 액세스하기 전에 `didFinishLaunchingWithOptions:` 위임에서 `startWithApiKey:`를 호출하면 `Appboy.sharedInstance()?.changeUser("testUser")`와 같은 선택적 체인을 사용하여 번거로운 확인 작업을 피할 수 있습니다. null이 아닌 `sharedInstance`를 가정하는 Objective-C 구현과 동등합니다.

## 수동 통합 옵션

[퍼블릭 리포지토리](https://github.com/appboy/appboy-ios-sdk)에서 프레임워크를 가져와 이전 섹션에서 설명한 대로 Braze를 초기화하기만 하면 tvOS SDK를 수동으로 통합할 수도 있습니다.

## 사용자 식별 및 분석 보고
사용자 ID 설정, 커스텀 이벤트 기록, 사용자 속성 설정에 대한 자세한 내용은 [iOS 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/)를 참조하세요. 또한 [이벤트 이름 지정 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) 숙지하는 것이 좋습니다.

