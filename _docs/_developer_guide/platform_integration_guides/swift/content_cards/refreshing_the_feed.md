---
nav_title: Refreshing the Feed
article_title: Refreshing the Content Card Feed for iOS
platform: Swift
page_order: 4
description: "This reference article covers implementing Content Card refreshing in your iOS application."
channel:
  - content cards

---

# Refreshing the feed

## Refreshing Content Cards

You can manually request Braze to refresh the user's Content Cards using the `requestRefresh` method on the `Braze` instance:
{% tabs %}
{% tab Swift %}

In Swift, Content Cards can be refreshed either with an optional completion handler or with an asynchronous return using the native Swift concurrency APIs.

{% subtabs %}
{% subtab Completion Handler %}
```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
// Implement completion handler
}
```
{% endsubtab %}
{% subtab Async/Await %}
```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endtab %}
{% endtabs %}

For more information, refer to the `Braze.ContentCards` [class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class).
