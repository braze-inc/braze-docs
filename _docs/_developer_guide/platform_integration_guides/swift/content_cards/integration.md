---
nav_title: Integration
article_title: Content Card Integration for iOS
platform: Swift
page_order: 1
description: "This article covers the integration steps, data models, and card-specific properties available in the Swift SDK."
channel:
  - content cards

---

# Content Card integration

## Content Cards data model

The Content Cards data model is available in the `BrazeKit` module of the iOS Swift SDK.

### Getting the data

To access the Content Cards data model, call `contentCards.cards` on your `braze` instance.

{% tabs local %}
{% tab swift %}
```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Additionally, you can also maintain a subscription to observe for changes in your Content Cards. You can do so in one of two ways: 
1. Maintaining a cancellable; or 
2. Maintaining an `AsyncStream`.

{% subtabs local %}
{% subtab CANCELLABLE %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```
{% endsubtab %}
{% subtab ASYNC STREAM %}
```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Additionally, if you wish to maintain a subscription to your content cards, you can call `subscribeToUpdates`:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```
{% endtab %}
{% endtabs %}

## Content Card model

Braze offers five Content Card types: banner, captioned image, classic, classic image, and control. Each type is an implementation of the `Braze.ContentCard` type. Note that BrazeKit offers an alternative [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) class for Objective-C compatibility.

For a full list of Content Card properties, as well as details about using Content Cards, refer to the [`ContentCard` class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

## Card methods

Each card is initialized with a `Context` object, which contains various methods for managing your card's state. Call these methods when you want to modify the corresponding state property on a particular card object.

| Method                               | Description                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Log the content card impression event.                                                                                                   |
| `card.context?.logClick()`           | Log the content card click event.                                                                                                        |
| `card.context?.processClickAction()` | Process a given [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) input. |
| `card.context?.logDismissed()`       | Log the content card dismissed event.                                                                                                    |
| `card.context?.logError()`           | Log an error related to the content card.                                                                                                |
| `card.context?.loadImage()`          | Load a given content card image from a URL. This method can be nil when the content card does not have an image.                         |
{: .reset-td-br-1 .reset-td-br-2}

For more details, refer to the [`Context` class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)

## Refreshing Content Cards

{% alert tip %}
To dynamically show up-to-date Content Cards without manually refreshing, select **At first impression** during card creation. These cards will be refreshed once they are available.
{% endalert %}

You can manually request Braze to refresh the user's Content Cards using the `requestRefresh` method on the `Braze` instance:
{% tabs local %}
{% tab Swift %}

In Swift, Content Cards can be refreshed either with an optional completion handler or with an asynchronous return using the native Swift concurrency APIs.

{% subtabs local %}
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

{% alert important %}
The default rate limit for calling `requestRefresh` is 3 calls per 10 minutes per device to prevent performance degradation and errors.
{% endalert %}

## Content Cards UI integration

Content Cards UI can be integrated from the `BrazeUI` library of the Swift SDK. This library provides two view controller contexts: navigation or modal. For more information about iOS navigation options, refer to the [Apple developer documentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).

If you wish to intercept and react to the Content Card UI lifecycle, implement [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) as the delegate for your `BrazeContentCardUI.ViewController`.

### Navigation context

Example of pushing a `BrazeContentCardUI.ViewController` instance into a navigation controller:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modal context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a **Done** button on the side of the bar.

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

For example usage of BrazeUI view controllers, check out the corresponding Content Cards UI samples in our [Examples app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).
