---
nav_title: 통합 완료
article_title: Swift SDK 통합 완료
platform: Swift
description: "이 참조 문서에서는 통합 옵션 중 하나를 통해 Braze Swift SDK를 설치한 후 해당 통합을 완료하는 방법을 보여줍니다."
page_order: 2

---

# 통합 완료

> 이 단계를 따르기 전에 [스위프트 패키지 매니저]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) 또는 [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/)를 사용하여 iOS용 Swift SDK를 통합했는지 확인합니다.

## 앱 대리자를 업데이트하세요

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab 목표-C %}

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

{% endtab %}
{% endtabs %}


## SDK 통합 완료

이 시점에서, 기본 통합이 완료되어야 합니다. 이제 Braze가 애플리케이션에서 데이터를 수집하고 있을 것입니다. 이 통합 가이드의 다른 문서에 따라 Braze 기능 및 메시징 채널의 전체 범위를 구현하고 사용자 지정합니다.

## 추가 리소스

[SDK 참조 문서전체](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "iOS 클래스 문서는") 각 SDK 심볼에 대한 추가 정보와 지침을 제공합니다.

