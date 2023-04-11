---
nav_title: Handling Clicks Manually
article_title: Handling Content Card Clicks Manually 
page_order: 1
description: "This article covers how to manually handle Content Cards clicks and analytics."

---

# Handling Content Card clicks manually 

In cases where you are building your own Content Cards UI, you can manually handle Content Card clicks. To do this, implement the [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) protocol and set your delegate object as the `delegate` property of your `BrazeContentCardUI.ViewController`. Refer to the [Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) for an example. 

{% tabs %}
{% tab Swift %}
```swift
// Set the delegate when creating the Content Cards controller
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
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

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
