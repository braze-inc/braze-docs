---
nav_title: 딥링킹
article_title: iOS용 딥링킹
platform: Swift
page_order: 1
description: "이 문서에서는 iOS 앱용 유니버설 딥링킹 위임을 구현하는 방법과 Swift SDK의 앱 설정에 딥링킹하는 방법에 대한 예제를 다룹니다."

---

# 딥링킹

> 딥링킹은 기본 앱을 실행하거나 특정 콘텐츠를 표시하거나 특정 동작을 수행하는 링크를 제공하는 방법입니다. iOS 앱에서 딥링크를 처음 구현하려는 경우 다음 단계를 따르세요.

딥링크에 대한 일반적인 정보는 [FAQ 문서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)를 참조하세요. 

## 1단계: 스키마 등록

딥링킹을 처리하려면 `Info.plist` 파일에 사용자 정의 스키마를 명시해야 합니다. 탐색 구조는 사전의 배열로 정의됩니다. 이러한 각 사전에는 문자열 배열이 포함되어 있습니다.

Xcode를 사용하여 `Info.plist` 파일을 편집합니다:

1. 새 키( `URL types`)를 추가합니다. Xcode는 자동으로 `Item 0` 사전을 포함하는 배열로 만듭니다.
2. `Item 0`에서 `URL identifier` 키를 추가합니다. 값을 커스텀 스키마로 설정합니다.
3. `Item 0`에서 `URL Schemes` 키를 추가합니다. 그러면 자동으로 `Item 0` 문자열을 포함하는 배열이 됩니다.
4. `URL Schemes` >> `Item 0` 을 사용자 지정 구성표로 설정합니다.

또는 `Info.plist` 파일을 직접 편집하려면 다음 사양을 따를 수 있습니다.

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## 2단계: 스키마 허용 목록 추가

앱의 Info.plist 파일에 `LSApplicationQueriesSchemes` 키를 추가하여 `canOpenURL(_:)`에 전달할 URL 스키마를 선언해야 합니다. 이 허용 목록에 없는 스키마를 호출하려고 시도하면 시스템에서 기기 로그에 오류를 기록하고 딥링크가 열리지 않습니다. 이 오류의 예는 다음과 같습니다:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

예를 들어, 인앱 메시지에서 Facebook 앱을 탭하여 열려면 앱의 허용 목록에 Facebook 커스텀 스키마(`fb`)가 있어야 합니다. 그렇지 않으면 시스템이 딥 링크를 거부합니다. 앱 내부의 페이지나 보기로 연결되는 딥링크는 여전히 앱의 `Info.plist`에 앱의 커스텀 스키마가 나열되어야 합니다.

허용 목록의 예는 다음과 같습니다:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

자세한 내용은 [Apple 설명서](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)에서 `LSApplicationQueriesSchemes` 키를 참조하세요.

## 3단계: 핸들러 구현

앱을 활성화한 후 iOS는 [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) 메서드를 호출합니다. 중요한 인수는 [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) 객체입니다.

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## 앱 전송 보안(ATS)

### ATS 요구 사항
[Apple의 문서에서](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) 발췌한 내용입니다: "앱 전송 보안은 앱과 웹 서비스 간의 연결 보안을 강화하는 기능입니다. 이 기능은 보안 연결을 위한 모범 사례를 준수하는 기본 연결 요구 사항으로 구성되어 있습니다. 앱은 이 기본 동작을 재정의하고 전송 보안을 해제할 수 있습니다."

ATS는 기본적으로 적용됩니다. 모든 연결은 HTTPS를 사용해야 하며, 순방향 비밀성을 지원하는 TLS 1.2를 사용하여 암호화해야 합니다. 자세한 내용은 [ATS를 사용하여 연결하기 위한 요구 사항](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)을 참조하세요. Braze가 최종 기기에 제공하는 모든 이미지는 TLS 1.2를 지원하고 ATS와 호환되는 콘텐츠 전송 네트워크("CDN")에서 처리됩니다.

애플리케이션의 `Info.plist`에서 예외로 지정하지 않는 한, 이러한 요구 사항을 따르지 않는 연결은 다음과 같은 오류와 함께 실패합니다.

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

ATS 규정 준수는 모바일 앱 내에서 열린 링크(클릭된 링크에 대한 기본 처리)에 대해 적용되며 웹 브라우저를 통해 외부에서 열린 사이트에는 적용되지 않습니다.

### ATS 요구 사항 처리

다음 세 가지 방법 중 하나로 ATS를 처리할 수 있습니다:

#### 모든 링크가 ATS를 준수하는지 확인(권장)
예를 들어 인앱 메시지 및 푸시 캠페인을 통해 사용자를 유도하는 기존 링크가 ATS 요건을 충족하는지 확인하여 Braze 통합을 통해 ATS 요건을 충족할 수 있습니다. ATS 제한을 우회하는 방법이 있지만, 링크된 모든 URL이 ATS 규정을 준수하는 것이 좋습니다. Apple은 애플리케이션 보안을 점점 더 강조하고 있기 때문에 다음과 같은 ATS 예외 허용에 관한 접근 방식은 Apple에서 지원되지 않습니다.

#### ATS 부분 비활성화
특정 도메인 또는 스키마가 있는 링크의 하위 집합을 ATS 규칙의 예외로 취급하도록 허용할 수 있습니다. Braze 메시징 채널에서 사용하는 모든 링크가 ATS를 준수하거나 예외를 통해 처리되는 경우, Braze 통합은 ATS 요구 사항을 충족합니다.

ATS의 예외로 도메인을 추가하려면 앱의 `Info.plist` 파일에 다음을 추가합니다.

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

자세한 내용은 Apple의 [앱 전송 보안 키](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) 관련 문서를 참조하세요.

#### ATS를 완전히 비활성화

ATS를 완전히 끌 수 있습니다. 보안 보호 기능이 손실되고 향후 iOS 호환성이 저하될 수 있으므로 권장되지 않는 방법입니다. ATS를 비활성화하려면 앱의 `Info.plist` 파일에 다음을 삽입하세요:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

## URL 인코딩

SDK는 링크를 퍼센트 인코딩하여 유효한 `URL`을 생성합니다. 유니코드 문자와 같이 올바르게 형성된 URL에서 허용되지 않는 모든 링크 문자는 퍼센트 기호로 이스케이프 처리됩니다.

인코딩된 링크를 디코딩하려면 `String` 속성 [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding)을 사용합니다. 또한 `BrazeDelegate.braze(_:shouldOpenURL:)`에서 `true`를 반환해야 합니다. 앱에서 URL 처리를 트리거하려면 콜투액션이 필요합니다. 

예를 들어, 다음과 같습니다.

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}


## 앱 설정에 대한 딥링킹

`UIApplicationOpenSettingsURLString`을 활용하여 Braze 푸시 알림, 인앱 메시지, 뉴스피드에서 앱 설정으로 사용자를 딥링킹할 수 있습니다.

앱에서 iOS 설정으로 사용자를 이동합니다:
1. 먼저, 애플리케이션이 [스키마 기반 딥링크](##step-1-registering-a-scheme) 또는 [유니버설 링크](#universal-links)를 사용하도록 설정되어 있는지 확인합니다.
2. **설정** 페이지로 딥링킹할 URI를 결정합니다(예: `myapp://settings` 또는 `https://www.braze.com/settings`).
3. 사용자 정의 구성표 기반 딥링크를 사용하는 경우 `application:openURL:options:` 메서드에 다음 코드를 추가하세요:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## 사용자 지정 {#linking-customization}

### 기본 WebView 사용자 지정

`Braze.WebViewController` 클래스는 일반적으로 웹 딥링크에 대해 '앱 내에서 웹 URL 열기'를 선택한 경우 SDK에 의해 열린 웹 URL을 표시합니다.

[`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) 위임 메서드를 통해 `Braze.WebViewController`를 사용자 지정할 수 있습니다.

### 링크 처리 사용자 지정

`BrazeDelegate` 프로토콜을 사용하여 딥링크, 웹 URL, 유니버설 링크 등의 URL 처리를 사용자 지정할 수 있습니다. Braze 초기화 중에 위임을 설정하려면 `Braze` 인스턴스에서 위임 오브젝트를 설정합니다. 그러면 Braze는 URI를 처리하기 전에 `shouldOpenURL`의 위임 구현을 호출합니다.

#### 유니버설 링크

Braze는 푸시 알림, 인앱 메시지, 콘텐츠 카드에서 유니버설 링크를 지원합니다. 유니버설 링크 지원을 사용하려면 [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks)를 `true`로 설정해야 합니다.

활성화하면 Braze는 [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) 메서드를 통해 앱의 `AppDelegate`로 유니버설 링크를 전달합니다. 

또한 유니버설 링크를 처리하도록 애플리케이션을 설정해야 합니다. 애플리케이션이 유니버설 링크에 맞게 올바르게 구성되었는지 확인하려면 [Apple의 설명서](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)를 참조하세요.

{% alert warning %}
유니버설 링크를 전달하려면 애플리케이션 권한에 대한 액세스 권한이 필요합니다. 시뮬레이터에서 애플리케이션을 실행할 때는 이러한 권한을 직접 사용할 수 없으며 유니버설 링크가 시스템 핸들러에 전달되지 않습니다.
시뮬레이터 빌드에 지원을 추가하려면 _번들 리소스 복사_ 빌드 단계에 애플리케이션 `.entitlements` 파일을 추가하면 됩니다. 자세한 내용은 [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) 설명서를 참조하세요.
{% endalert %}

{% alert note %}
SDK는 도메인의 `apple-app-site-association` 파일을 쿼리하지 않습니다. 도메인 이름만 보고 유니버설 링크와 일반 URL을 구분합니다. 따라서 SDK는 [지원되는 관련 도메인](https://developer.apple.com/documentation/xcode/supporting-associated-domains)당 `apple-app-site-association`에 정의된 제외 규칙을 따르지 않습니다.
{% endalert %}

### 통합 예제: BrazeDelegate

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}

자세한 내용은 [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)를 참조하세요.


