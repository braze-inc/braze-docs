Braze SDK를 설치하면 기본 분석 기능({% if include.platform == 'iOS' %})과 함께 사용자를 참여시킬 수 있는 인앱 메시지({% endif %})가 제공됩니다.

Objective-C 및 Swift 프로젝트의 종속성 관리자인 [CocoaPods](http://cocoapods.org/)를 사용하여 {{include.platform}} Braze SDK를 설치하거나 업데이트해야 합니다. CocoaPods를 사용하면 통합과 업데이트가 더욱 간편해집니다.

## {{include.platform}} SDK CocoaPods 통합

### 1단계: CocoaPods 설치

{{include.platform}} [CocoaPods](http://cocoapods.org/)을 통해 SDK를 설치하면 대부분의 설치 과정이 자동화됩니다. 이 프로세스를 시작하기 전에 [Ruby 버전 2.0.0](https://www.ruby-lang.org/en/installation/) 이상을 사용하고 있는지 확인하세요. 루비 구문에 대한 지식이 없어도 이 SDK를 설치할 수 있습니다.

시작하려면 다음 명령을 실행하기만 하면 됩니다.

```bash
$ sudo gem install cocoapods
```

**참고**: `rake` 실행 파일을 덮어쓰라는 메시지가 표시되면 자세한 내용은 [시작하기 지침CocoaPods.org](http://guides.cocoapods.org/using/getting-started.html)을 참조하세요.

**참고**: 코코아팟과 관련된 문제가 있는 경우 [코코아팟 문제 해결 가이드를](http://guides.cocoapods.org/using/troubleshooting.html) 참조하세요.

### 2단계: 포드파일 구성하기

CocoaPods Ruby Gem을 설치했으므로 Xcode 프로젝트 디렉토리에 `Podfile` 파일을 만들어야 합니다.

포드파일에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**참고**: 포드 업데이트에서 부 버전 업데이트보다 작은 내용을 자동으로 가져올 수 있도록 Braze 버전을 설정하는 것이 좋습니다. 'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'처럼 보입니다. 주요 변경 사항이 있는 경우에도 최신 버전의 Braze SDK를 자동으로 통합하려면 Podfile에 `pod 'Appboy-{{include.platform}}-SDK'`를 사용하면 됩니다.
{% if include.platform == 'iOS' %}
**참고**: Braze 기본 UI를 사용하지 않고 SDWebImage 종속성을 도입하고 싶지 않다면, Podfile에서 Braze 종속성을 Core subspec으로 가리키세요(예: Podfile의 `pod 'Appboy-iOS-SDK/Core'`). {% endif %}.

### 3단계: Braze SDK 설치하기

Braze SDK CocoaPods를 설치하려면 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하여 다음 명령을 실행합니다.
```
pod install
```

이 시점에서 CocoaPods에서 생성한 새 Xcode 프로젝트 작업 공간을 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용해야 합니다. 

![새 워크스페이스]({% image_buster /assets/img_archive/podsworkspace.png %})

### 4단계: 앱 위임 업데이트

{% tabs %}
{% tab 목표-C %}

`AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

`AppDelegate.m` 파일 내에 `application:didFinishLaunchingWithOptions` 메서드에 다음 스니펫을 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Braze SDK를 CocoaPods 또는 Carthage와 통합하는 경우 `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 설명서](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)를 참조하세요.

`AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`에 다음 스니펫을 추가합니다.

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**참고**: 브레이즈 기능을 사용하기 위한 전제 조건인 `sharedInstance` 싱글톤은 `startWithApiKey:` 호출 전에는 존재하지 않습니다.

{% endtab %}
{% endtabs %}

{% alert important %}
설정 관리 페이지에서 `YOUR-API-KEY`를 올바른 값으로 업데이트하세요.
{% endalert %}

{% alert warning %}
애플리케이션의 메인 스레드에서 Braze를 초기화해야 합니다. 비동기적으로 초기화하면 기능이 손상될 수 있습니다.
{% endalert %}


### 5단계: 사용자 지정 엔드포인트 또는 데이터 클러스터 지정

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않으며, 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a>을 참조하십시오.
{% endalert %}

Braze 담당자가 이미 [올바른 엔드포인트]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).를 알려드렸을 것입니다.

#### 컴파일 타임 엔드포인트 구성(권장)
기존 사용자 지정 엔드포인트가 있는 경우...
- Braze iOS SDK v3.0.2부터 `Info.plist` 파일을 사용하여 커스텀 지정 엔드포인트를 설정할 수 있습니다. Info.plist 파일에 `Appboy` 사전을 추가합니다. `Appboy` 사전 내에서 `Endpoint` 문자열 하위 항목을 추가하고 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `sdk.iad-01.braze.com`(`https://sdk.iad-01.braze.com` 아님).

#### 런타임 엔드포인트 구성

기존 사용자 지정 엔드포인트가 있는 경우...
- Braze iOS SDK v3.17.0+부터 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달된 `appboyOptions`매개변수 내 `ABKEndpointKey`를 통해 엔드포인트 설정을 재정의할 수 있습니다. 값을 커스텀 엔드포인트 URL의 권한으로 설정합니다(예: `sdk.iad-01.braze.com`(`https://sdk.iad-01.braze.com` 아님).

{% alert note %}
`ABKAppboyEndpointDelegate`를 사용하여 런타임에 엔드포인트를 설정하는 지원은 Braze iOS SDK v3.17.0에서 제거되었습니다. 이미 `ABKAppboyEndpointDelegate`를 사용하고 있는 경우, Braze iOS SDK 버전 v3.14.1~v3.16.0에서는 `getApiEndpoint()` 메서드에서 `dev.appboy.com`에 대한 참조를 `sdk.iad-01.braze.com`에 대한 참조로 바꾸어야 합니다.
{% endalert %}

{% alert important %}
특정 클러스터를 찾으려면 고객 성공 매니저에게 문의하거나 지원팀에 문의하세요.
{% endalert %}

### SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하며 기본 통합이 완료됩니다. {% if include.platform == 'iOS' %}커스텀 이벤트 추적, 푸시 메시지, 뉴스피드 및 전체 Braze 기능을 사용하려면 다음 섹션을 참조하세요.{% else %}tvOS 앱 및 기타 타사 라이브러리를 컴파일할 때 Bitcode를 사용하도록 설정해야 한다는 점에 유의하세요.{% endif %}

### CocoaPod를 통해 Braze SDK 업데이트하기

CocoaPod을 업데이트하려면 프로젝트 디렉토리에서 다음 명령을 실행하면 됩니다.

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

**참고**: 이 메서드는 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 메서드를 대체합니다.

이 메서드는 다음 매개변수와 함께 호출됩니다:

- `YOUR-API-KEY` - Braze 대시보드의 애플리케이션 API 키
- `application` - 현재 앱
- `launchOptions` - 다음에서 제공되는 옵션 `NSDictionary`  `application:didFinishLaunchingWithOptions:`
- `appboyOptions` - Braze에 대한 시작 구성 값이 포함된 선택 사항`NSDictionary`

Braze 시작 키 목록은 [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)를 참조하세요.

## Appboy.sharedInstance() 및 Swift 널 지정 가능
일반적인 관행과는 다소 다르게 `Appboy.sharedInstance()` 싱글톤은 선택 사항입니다. `startWithApiKey:` 호출 전에 `sharedInstance`가 `nil`이고, 표준은 아니지만, 지연된 초기화를 사용할 수 있는 유효한 구현이 일부 있기 때문입니다.

Appboy의 `sharedInstance`(표준 구현)에 액세스하기 전에 `didFinishLaunchingWithOptions:` 위임에서 `startWithApiKey:`를 호출하면 `Appboy.sharedInstance()?.changeUser("testUser")`와 같은 선택적 체인을 사용하여 번거로운 확인 작업을 피할 수 있습니다. null이 아닌 `sharedInstance`를 가정하는 Objective-C 구현과 동등합니다.

