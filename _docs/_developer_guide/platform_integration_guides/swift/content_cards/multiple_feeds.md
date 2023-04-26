---
nav_title: Multiple Feeds
article_title: Using Multiple Content Card Feeds for iOS
platform: Swift
page_order: 6
description: "This reference article covers implementing multiple iOS Content Card feeds in the Swift SDK."
channel:
  - content cards

---

# Multiple feeds

> Content Cards can be filtered on your app so that only specific cards are displayed, enabling you to have multiple Content Card feeds for different use cases. For example, you can maintain both a transactional feed and a marketing feed.<br><br>This article shows an example implementation that you can change to fit your specific integration.

## Step 1: Setting key-value pairs on cards

When creating a Content Card campaign, set key-value pair data on each card. Braze filtering logic will use this key-value pair data to categorize cards.

For this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed. The value will be whatever your custom feeds will be, such as `Transactional`, `Marketing`, etc.

## Step 2: Filter your content cards

Refer the following code snippet to filter your Content Cards. In this example, we will only display cards with a matching key-value pair of `feed_type: "Transactional"` in the `extras` dictionary.

{% tabs %}
{% tab SWIFT %}
```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

To take it a step further with Content Cards UI, you can access the `transform` property on your `Attributes` struct to display only the cards filtered by your criteria.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```
{% endtab %}
{% endtabs %}

For further details about customizing Content Cards, refer to the [Content Cards UI customization tutorial](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/)