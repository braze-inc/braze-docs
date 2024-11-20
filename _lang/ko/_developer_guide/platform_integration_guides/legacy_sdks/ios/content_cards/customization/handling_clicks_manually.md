---
nav_title: 수동으로 클릭 처리하기
article_title: iOS용 콘텐츠 카드 클릭 수동 처리하기
platform: iOS
page_order: 3
description: "이 문서에서는 iOS 애플리케이션에서 콘텐츠 카드 클릭을 수동으로 처리하는 방법에 대해 설명합니다."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 수동으로 클릭 처리

[`ABKContentCardsTableViewControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) 프로토콜을 구현하고 위임 오브젝트를 `ABKContentCardsTableViewController`의 `delegate` 속성정보로 설정하여 콘텐츠 카드 클릭을 수동으로 처리할 수 있습니다. 예제는 [콘텐츠 카드 샘플 앱을](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) 참조하세요. 

{% tabs %}
{% tab Objective-C %}
```objc
contentCardsTableViewController.delegate = delegate;

// Methods to implement in delegate
- (BOOL)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                 shouldHandleCardClick:(NSURL *)url {
  if ([[url.host lowercaseString] isEqualToString:@"my-domain.com"]) {
    // Custom handle link here
    NSLog(@"Manually handling Content Card click with URL %@", url.absoluteString);
    return NO;
  }
  // Let the Braze SDK handle the click action
  return YES;
}

- (void)contentCardTableViewController:(ABKContentCardsTableViewController *)viewController
                    didHandleCardClick:(NSURL *)url {
  NSLog(@"Braze SDK handled Content Card click with URL %@", url.absoluteString);
}
```
{% endtab %}
{% tab Swift %}
```swift
contentCardsTableViewController.delegate = delegate

// Methods to implement in delegate
func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    shouldHandleCardClick url: URL!) -> Bool {
  if (url.host?.lowercased() == "my-domain.com") {
    // Custom handle link here
    NSLog("Manually handling Content Card click with URL %@", url.absoluteString)
    return false
  }
  // Let the Braze SDK handle the click action
  return true
}

func contentCardTableViewController(_ viewController: ABKContentCardsTableViewController!,
                                    didHandleCardClick url: URL!) {
  NSLog("Braze SDK handled Content Card click with URL %@", url.absoluteString)
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
`ABKContentCardsTableViewController`에서 `handleCardClick:` 메서드를 재정의하면 이러한 위임 메서드가 호출되지 않을 수 있습니다.
{% endalert %}
