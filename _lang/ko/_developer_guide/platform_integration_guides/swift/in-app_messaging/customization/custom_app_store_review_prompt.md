---
nav_title: 예시 - 앱 스토어 리뷰 프롬프트
article_title: 예시 - 앱 스토어 리뷰 프롬프트
platform: Swift
page_order: 8
description: "이 참조 문서에서는 사용자에게 앱에 대한 리뷰를 제공하도록 요청하는 커스텀 인앱 메시지의 iOS 예제를 제공합니다."
channel:
  - in-app messages

---

# 예제 - App Store 리뷰 프롬프트

{% alert note %}
이 예제 프롬프트는 Braze의 기본 동작을 재정의하기 때문에 구현된 경우 노출 횟수를 자동으로 추적할 수 없습니다. 자신의 [분석]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks)을 기록해야 합니다.
{% endalert %}

> App Store 리뷰를 요청하기 위한 캠페인 생성은 널리 사용되는 인앱 메시지 사용법입니다. 이 예제는 사용자가 앱을 검토하도록 요청하는 커스텀 인앱 메시지를 만드는 과정을 안내합니다.

## 1단계: 인앱 메시지 위임자를 설정합니다
먼저, 앱에서 [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/)을 설정하세요. 

## 2단계: 기본 App Store 리뷰 메시지 비활성화
다음으로, 기본 App Store 리뷰 메시지를 비활성화하기 위해 `inAppMessage(_:displayChoiceForMessage:)` [위임 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 구현합니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

## 3단계: 딥링크를 생성합니다
딥링크 처리 코드에서 `{YOUR-APP-SCHEME}:app-store-review` 딥링크를 처리하기 위해 다음 코드를 추가합니다. `StoreKit`를 가져와서 `SKStoreReviewController`를 사용해야 합니다.

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

## 4단계: 커스텀 클릭 시 동작 설정

다음으로, 다음을 사용하여 인-앱 메시징 캠페인을 만드십시오:

- 키-값 쌍 `"AppStore Review" : "true"`
- 클릭 시 동작이 '앱으로 딥링크'로 설정되며 딥링크 `{YOUR-APP-SCHEME}:app-store-review`를 사용합니다.

{% endraw %}

{% alert tip %}
Apple은 사용자당 연간 최대 세 번으로 App Store 리뷰 요청을 제한하므로 캠페인에서도 사용자당 연간 세 번으로 [한도를 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)해야 합니다.<br><br>사용자는 App Store 리뷰 프롬프트를 끌 수도 있습니다. 결과적으로, 커스텀 리뷰 프롬프트는 기본 App Store 리뷰 프롬프트의 표시를 보장하지 않으며 직접적으로 리뷰를 요청해서는 안 됩니다.
{% endalert %}

