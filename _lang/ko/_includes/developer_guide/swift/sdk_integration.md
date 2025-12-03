## Swift SDK 통합하기

스위프트 패키지 매니저(SPM), 코코아팟 또는 수동 통합 방법을 사용하여 Braze Swift SDK를 통합하고 커스텀할 수 있습니다. 다양한 소프트웨어 개발 키트 심볼에 대한 자세한 내용은 [Braze Swift 참조 설명서를 참조하세요](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### 필수 조건

시작하기 전에 사용 중인 환경이 [최신 Braze Swift 소프트웨어 개발 키트 버전으로](https://github.com/braze-inc/braze-swift-sdk#version-information) 지원되는지 확인하세요.

### 1단계: Braze Swift 소프트웨어 개발 키트 설치하기

[스위프트 패키지 매니저(SwiftPM)](https://swift.org/package-manager/) 또는 [코코아팟을](http://cocoapods.org/) 사용하여 Braze Swift 소프트웨어 개발 키트를 설치하는 것이 좋습니다. 또는 소프트웨어 개발 키트를 수동으로 설치할 수도 있습니다.

{% tabs local %}
{% tab 스위프트 패키지 매니저 %}
#### 1.1단계: SDK 버전 가져오기

프로젝트를 열고 프로젝트 설정으로 이동합니다. **Swift 패키지** 탭을 선택하고 패키지 목록 아래에 있는 <i class="fas fa-plus"></i> 추가 버튼을 클릭합니다.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이 형식 중 하나를 대신 사용하려면 해당 리포지토리의 설치 지침을 따릅니다.
{% endalert %}

텍스트 필드에 iOS Swift SDK 리포지토리 URL(`https://github.com/braze-inc/braze-swift-sdk`)을 입력합니다. **종속성 규칙** 섹션에서 SDK 버전을 선택합니다. 마지막으로 **패키지 추가를** 클릭합니다.

![]({% image_buster /assets/img/importsdk_example.png %})

#### 1.2단계: 패키지 선택

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 잘 제어할 수 있도록 합니다.

| 패키지         | 세부 정보                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다.                                                                                        |
| `BrazeLocation` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리를 제공합니다.                                                                              |
| `BrazeUI`       | 인앱 메시지, 콘텐츠 카드, 배너를 위한 Braze가 제공하는 사용자 인터페이스 라이브러리입니다. 기본값 UI 컴포넌트를 사용하려는 경우 이 라이브러리를 가져옵니다. |

{: .ws-td-nw-1}

##### 확장 라이브러리 정보

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이므로 기본 애플리케이션 대상에 직접 추가해서는 안 됩니다. 대신 링크된 가이드에 따라 각각의 대상 확장에 개별적으로 통합합니다.
{% endalert %}

| 패키지                    | 세부 정보                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | 풍부한 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `BrazePushStory`           | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다.            |

{: .ws-td-nw-1}

필요에 가장 적합한 패키지를 선택하고 **패키지 추가를** 클릭합니다. 최소한 `BrazeKit`를 선택해야 합니다.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### 1.1단계: CocoaPods 설치

전체 안내는 CocoaPods [시작하기 가이드를](https://guides.cocoapods.org/using/getting-started.html) 참조하세요. 그렇지 않은 경우 다음 명령을 실행하여 빠르게 시작할 수 있습니다:

```bash
$ sudo gem install cocoapods
```

문제가 발생하면 CocoaPods의 [문제 해결 가이드를](http://guides.cocoapods.org/using/troubleshooting.html) 확인하세요.

#### 1.2단계: Podfile 구성

그런 다음 Xcode 프로젝트 디렉토리에 `Podfile` 라는 파일을 만듭니다.

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이 형식 중 하나를 대신 사용하려면 해당 리포지토리의 설치 지침을 따릅니다.
{% endalert %}

포드파일에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit`에는 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리가 포함되어 있습니다.

포드 업데이트에서 부 버전 업데이트보다 작은 내용을 자동으로 가져올 수 있도록 Braze 버전을 설정하는 것이 좋습니다. `pod 'BrazeKit' ~> Major.Minor.Build`와 유사합니다. 최신 Braze SDK 버전을 자동으로 통합하려면 주요 변경 사항이 있어도 Podfile에서 `pod 'BrazeKit'`를 사용하면 됩니다.

##### 추가 라이브러리 정보

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 잘 제어할 수 있도록 합니다. `BrazeKit` 외에도 다음 라이브러리를 Podfile에 추가할 수 있습니다.

| 라이브러리               | 세부 정보                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리를 제공합니다.                                                                              |
| `pod 'BrazeUI'`       | 인앱 메시지, 콘텐츠 카드, 배너를 위한 Braze가 제공하는 사용자 인터페이스 라이브러리입니다. 기본값 UI 컴포넌트를 사용하려는 경우 이 라이브러리를 가져옵니다. |

{: .ws-td-nw-1}

###### 확장 라이브러리

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이며, 메인 애플리케이션 대상에 직접 추가해서는 안 됩니다. 대신, 이러한 모듈 각각에 대해 별도의 확장 대상을 생성하고 해당 대상으로 Braze 모듈을 가져와야 합니다.

| 라이브러리                          | 세부 정보                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | 풍부한 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `pod 'BrazePushStory'`           | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다.            |

{: .ws-td-nw-1}

#### 1.3단계: 소프트웨어 개발 키트 설치하기

Braze SDK CocoaPod을 설치하려면 터미널에서 Xcode 앱 프로젝트 디렉토리로 이동한 후 다음 명령어를 실행합니다.
```
pod install
```

이때 CocoaPods에서 생성한 새 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용해야 합니다.

![Braze 예제 폴더가 확장되어 새로운 `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### CocoaPods를 사용하여 소프트웨어 개발 키트 업데이트하기

CocoaPod를 업데이트하려면 프로젝트 디렉토리에서 다음 명령을 실행하면 됩니다:

```
pod update
```
{% endtab %}

{% tab 매뉴얼 %}
#### 1.1단계: Braze SDK 다운로드

[GitHub의 Braze SDK 릴리스 페이지](https://github.com/braze-inc/braze-swift-sdk/releases)로 이동한 다음, `braze-swift-sdk-prebuilt.zip`을 다운로드합니다.

!['GitHub의 Braze SDK 릴리스 페이지.']({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### 1.2단계: 프레임워크 선택

Braze Swift SDK에는 다양한 독립형 XCFrameworks가 포함되어 있어 모든 기능을 통합할 필요 없이 원하는 기능을 자유롭게 통합할 수 있습니다. 다음 표를 참조하여 XCFrameworks를 선택합니다.

| 패키지                    | 필수 항목인가요? | 설명                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | 예       | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다.                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | 아니요        | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리입니다.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | 아니요        | 인앱 메시지, 콘텐츠 카드, 배너를 위한 Braze가 제공하는 사용자 인터페이스 라이브러리입니다. 기본값 UI 컴포넌트를 사용하려는 경우 이 라이브러리를 가져옵니다.                                                                                                                                                                      |
| `BrazeNotificationService` | 아니요        | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 대상에 직접 추가하지 말고 [`BrazeNotificationService` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)합니다.                 |
| `BrazePushStory`           | 아니요        | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 대상에 직접 추가하지 말고 [`BrazePushStory` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)합니다.                                                 |
| `BrazeKitCompat`           | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X에서 사용 가능했던 모든 `Appboy` 및 `ABK*` 클래스 및 메서드가 포함된 호환성 라이브러리. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요.            |
| `BrazeUICompat`            | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X부터 `AppboyUI` 라이브러리에서 사용 가능했던 모든 `ABK*` 클래스 및 메서드가 포함된 호환성 라이브러리. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요. |
| `SDWebImage`               | 아니요        | 최소 마이그레이션 시나리오에서 `BrazeUICompat` 에서만 사용하는 종속성입니다.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 1.3단계: 파일 준비

**정적** XCFrameworks를 사용할지 **동적** XCFrameworks를 사용할지 결정한 다음, 파일을 준비합니다.

1. XCFrameworks의 임시 디렉토리를 생성합니다.
2. `braze-swift-sdk-prebuilt`에서 `dynamic` 디렉토리를 열고 `BrazeKit.xcframework`를 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. 각 [선택한 XCFrameworks](#swift_step-2-choose-your-frameworks)를 임시 디렉토리로 이동합니다. 디렉터리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### 1.4단계: 프레임워크 통합

다음으로, [이전에 준비](#swift_step-3-prepare-your-files)한 **동적** 또는 **정적** XCFrameworks를 통합합니다.

Xcode 프로젝트에서 빌드 대상을 선택한 다음, **일반**을 선택합니다. **프레임워크, 라이브러리 및 임베디드 콘텐츠**에서 [이전에 준비한 파일](#swift_step-3-prepare-your-files)을 끌어다 놓습니다.

!['각 Braze 라이브러리가 '임베드 및 서명'으로 설정된 예제 Xcode 프로젝트.']({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Swift 소프트웨어 개발 키트 12.0.0부터는 정적 및 동적 배리언트 모두에 대해 항상 Braze XC프레임워크에 대해 **임베드 및 서명을** 선택해야 합니다. 이렇게 하면 프레임워크 리소스가 앱 번들에 올바르게 포함될 수 있습니다.
{% endalert %}

{% alert tip %}
GIF 지원을 인에이블하려면 `braze-swift-sdk-prebuilt/static` 또는 `braze-swift-sdk-prebuilt/dynamic` 에 `SDWebImage.xcframework` 를 추가하세요.
{% endalert %}

#### Objective-C 프로젝트의 일반적인 오류

Xcode 프로젝트에 Objective-C 파일만 포함된 경우 프로젝트를 빌드하려고 할 때 '누락된 기호' 오류가 발생할 수 있습니다. 이러한 오류를 해결하려면 프로젝트를 열고 파일 트리에 빈 Swift 파일을 추가합니다. 그러면 빌드 툴체인에 [Swift 런타임](https://support.apple.com/kb/dl1998)이 강제로 임베드되고 빌드 시간 동안 적절한 프레임워크에 링크됩니다.

```bash
FILE_NAME.swift
```

`FILE_NAME` 을 띄어쓰기가 없는 문자열로 바꿉니다. 파일은 다음과 비슷하게 보일 것입니다:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### 2단계: 지연 초기화 설정(선택 사항)

Braze Swift 소프트웨어 개발 키트가 초기화되는 시기를 지연하도록 선택할 수 있으며, 이는 앱에서 구성을 로드하거나 SDK를 시작하기 전에 사용자 동의를 기다려야 하는 경우에 유용합니다. 초기화가 지연되면 소프트웨어 개발 키트가 준비될 때까지 Braze 푸시 알림이 대기줄에 대기합니다.

이 기능을 인에이블하려면 가능한 한 빨리 `Braze.prepareForDelayedInitialization()` 으로 전화하여 `application(_:didFinishLaunchingWithOptions:)`.

{% alert note %}
이는 Braze의 푸시 알림에만 적용됩니다. 다른 푸시 알림은 시스템 위임자가 정상적으로 처리합니다.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) 는 선택적 `pushAutomation` 매개 변수를 허용합니다. `nil` 으로 설정하면 실행 시 푸시 승인 요청을 제외한 모든 푸시 자동화 기능이 인에이블먼트됩니다.
{% endalert %}

### 3단계: 앱 대리자를 업데이트하세요

{% alert important %}
다음은 프로젝트에 `AppDelegate` 을 이미 추가했다고 가정합니다(기본값으로 생성되지 않음). 사용할 계획이 없다면 앱 출시 시와 같이 가능한 한 빨리 Braze 소프트웨어 개발 키트를 초기화하세요.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Braze Swift SDK에 포함된 기능을 가져오기 위해 다음 코드를 `AppDelegate.swift` 파일에 추가합니다.

```swift
import BrazeKit
```

다음으로, `AppDelegate` 클래스에 정적 속성정보를 추가하여 애플리케이션의 수명 동안 Braze 인스턴스에 대한 강력한 참조를 유지합니다.

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

마지막으로, `AppDelegate.swift`에서 다음 스니펫을 `application:didFinishLaunchingWithOptions:` 메서드에 추가하십시오:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

`YOUR-APP-IDENTIFIER-API-KEY` 및 `YOUR-BRAZE-ENDPOINT`을(를) **앱 설정** 페이지에서 올바른 값으로 업데이트하십시오. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)을 참조하세요.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

다음 코드 줄을 `AppDelegate.m` 파일에 추가하십시오:

```objc
@import BrazeKit;
```

다음으로, `AppDelegate.m` 파일에 정적 변수를 추가하여 애플리케이션의 수명 동안 Braze 인스턴스에 대한 참조를 유지합니다.

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

마지막으로, `AppDelegate.m` 파일 내에서 `application:didFinishLaunchingWithOptions:` 메서드 내에 다음 스니펫을 추가합니다.

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

`YOUR-APP-IDENTIFIER-API-KEY` 및 `YOUR-BRAZE-ENDPOINT`을(를) **설정 관리** 페이지에서 올바른 값으로 업데이트하십시오. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)를 참조하세요.

{% endsubtab %}
{% endsubtabs local %}

## 선택적 구성

### 로깅

#### 로그 레벨

Braze Swift 소프트웨어 개발 키트의 기본값 로그 수준은 `.error`이며, 로그가 인에이블먼트된 경우 지원되는 최소 수준이기도 합니다. 다음은 로그 레벨의 전체 목록입니다:

| Swift       | Objective-C              | 설명                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | 로그 디버깅 정보 + `.info` + `.error`.                      |
| `.info`     | `BRZLoggerLevelInfo`     | 일반 SDK 정보(사용자 변경 사항 등) + `.error`를 기록합니다. |
| `.error`    | `BRZLoggerLevelError`    | 로그 오류.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | 로깅이 발생하지 않습니다.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 로그 수준 설정

`Braze.Configuration` 객체에서 런타임에 로그 수준을 지정할 수 있습니다. 전체 사용법에 대한 자세한 내용은 [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
