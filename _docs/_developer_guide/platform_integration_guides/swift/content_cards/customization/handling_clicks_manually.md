---
nav_title: Handling Clicks Manually
article_title: Handling Content Card Clicks Manually for iOS
platform: Swift
page_order: 3
description: "This article covers how to handle Content Cards clicks manually in your iOS application."
channel:
  - content cards
---

# Handling clicks manually

You can manually handle Content Card clicks by implementing the [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) protocol and setting your delegate object as the `delegate` property of your `BrazeContentCardUI.ViewController`. Refer to the [Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) for an example. 

{% tabs %}
{% tab Swift %}
```swift
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```
{% endtab %}
{% tab Objective-C %}
```objc
[contentCardsController setDelegate:delegate];

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endtab %}
{% endtabs %}
