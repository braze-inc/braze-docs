---
nav_title: クリックの手動処理
article_title: iOS でコンテンツカードのクリックを手動で処理する
platform: iOS
page_order: 3
description: "この記事では、iOS アプリケーションでコンテンツカードのクリックを手動で処理する方法について説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# クリックの手動処理

コンテンツカードのクリックを手動で処理するには、[`ABKContentCardsTableViewControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) プロトコルを実装し、`ABKContentCardsTableViewController` の `delegate` プロパティとしてデリゲートオブジェクトを設定します。例については、[コンテンツカードのサンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)を参照してください。 

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
`ABKContentCardsTableViewController` で `handleCardClick:` メソッドをオーバーライドすると、これらのデリゲートメソッドが呼び出されない場合があります。
{% endalert %}
