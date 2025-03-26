---
nav_title: Manuelles Verarbeiten von Klicks
article_title: Manuelle Handhabung von Inhaltskartenklicks für iOS
platform: iOS
page_order: 3
description: "In diesem Artikel erfahren Sie, wie Sie Klicks auf Inhaltskarten in Ihrer iOS-Anwendung manuell behandeln können."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Manuelles Verarbeiten von Klicks

Sie können Content-Card-Klicks manuell verarbeiten, indem Sie das Protokoll [`ABKContentCardsTableViewControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_content_cards_table_view_controller_delegate-p.html) implementieren und Ihr Delegate-Objekt als Eigenschaft des Typs `delegate` für `ABKContentCardsTableViewController` festlegen. Ein Beispiel dafür finden Sie in der [Beispielanwendung Content Cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp). 

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
Wenn Sie die Methode `handleCardClick:` in `ABKContentCardsTableViewController` außer Kraft setzen, werden diese Delegate-Methoden möglicherweise nicht aufgerufen.
{% endalert %}
