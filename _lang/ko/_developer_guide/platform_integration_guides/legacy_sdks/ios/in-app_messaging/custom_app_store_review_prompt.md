---
nav_title: 사용자 지정 App Store 검토 프롬프트
article_title: 사용자 지정 App Store 검토 프롬프트
platform: iOS
page_order: 4
description: "이 참조 문서에서는 사용자 지정 iOS 앱 스토어 리뷰 프롬프트를 설정하는 방법을 설명합니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include 사용 중단/목적-c.md %}

# 사용자 지정 App Store 검토 프롬프트

{% alert note %}
이 프롬프트를 구현하면 Braze는 자동으로 노출 추적을 중지하며, 직접 [분석을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks) 기록해야 합니다.
{% endalert %}

사용자에게 앱 스토어 리뷰를 요청하는 캠페인을 생성하는 것은 인앱 메시지의 인기 있는 사용 방법입니다.

앱에서 [인앱 메시지 델리게이트를][30] 설정하는 것부터 시작하세요. 다음으로 다음 델리게이트 메서드를 구현하여 기본 App Store 리뷰 메시지를 비활성화합니다:

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

딥링크 처리 코드에 다음 코드를 추가하여 `{YOUR-APP-SCHEME}:appstore-review` 딥링크를 처리합니다. `SKStoreReviewController` 을 사용하려면 `StoreKit` 을 가져와야 합니다:

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
- 딥 링크 `{YOUR-APP-SCHEME}:appstore-review` 를 사용하여 클릭 시 동작을 "앱으로 딥 링크"로 설정합니다.

{% endraw %}

{% alert tip %}
Apple은 사용자당 연간 최대 3회까지만 앱스토어 리뷰 메시지를 표시하도록 제한하므로 캠페인은 사용자당 연간 3회까지로 [제한해야]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) 합니다.<br><br>사용자는 App Store 리뷰 프롬프트를 끌 수 있습니다. 따라서 사용자 지정 검토 프롬프트는 기본 App Store 검토 프롬프트가 표시되거나 직접 검토를 요청해서는 안 됩니다.
{% endalert %}

[30]: #in-app-message-controller-delegate
