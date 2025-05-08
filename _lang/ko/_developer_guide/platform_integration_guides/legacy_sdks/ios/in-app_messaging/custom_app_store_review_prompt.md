---
nav_title: 사용자 지정 App Store 검토 프롬프트
article_title: 사용자 지정 App Store 검토 프롬프트
platform: iOS
page_order: 4
description: "이 참조 문서에서는 커스텀 iOS App Store 리뷰 프롬프트를 설정하는 방법을 보여줍니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용자 지정 App Store 검토 프롬프트

{% alert note %}
이 프롬프트를 구현하면 Braze는 자동으로 노출 횟수 추적을 중지하며, 사용자가 [분석]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks)을 기록해야 합니다.
{% endalert %}

사용자에게 앱 스토어 리뷰를 요청하는 캠페인을 생성하는 것은 인앱 메시지의 인기 있는 사용 방법입니다.

앱에서 [인앱 메시지 델리게이트를](#in-app-message-controller-delegate) 설정하는 것부터 시작하세요. 다음으로, 기본 App Store 리뷰 메시지를 비활성화하기 위해 다음 위임 메서드를 구현합니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage.uri options:@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage.uri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice.discardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

딥링크 처리 코드에서 `{YOUR-APP-SCHEME}:appstore-review` 딥링크를 처리하기 위해 다음 코드를 추가합니다. `StoreKit`를 가져와서 `SKStoreReviewController`를 사용해야 합니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

다음으로 다음을 사용하여 인앱 메시징 캠페인을 만듭니다:

- 키-값 쌍 `"Appstore Review" : "true"`
- 클릭 시 동작이 '앱으로 딥링크'로 설정되며 딥링크 `{YOUR-APP-SCHEME}:appstore-review`를 사용합니다.

{% endraw %}

{% alert tip %}
Apple은 사용자당 연간 최대 3번으로 App Store 리뷰 요청을 제한하므로 캠페인에서도 사용자당 연간 세 번으로 [한도를 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)해야 합니다.<br><br>사용자는 App Store 리뷰 프롬프트를 끌 수 있습니다. 결과적으로, 커스텀 리뷰 프롬프트는 기본 App Store 리뷰 프롬프트의 표시를 보장하지 않으며 직접적으로 리뷰를 요청해서는 안 됩니다.
{% endalert %}

