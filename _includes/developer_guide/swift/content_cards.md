## Prerequisites

Before you can use Content Cards, you'll need to integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) into your app. However, no additional setup is required.

## View controller contexts

The default Content Cards UI can be integrated from the `BrazeUI` library of the Braze SDK. Create the Content Cards view controller using the `braze` instance. If you wish to intercept and react to the Content Card UI lifecycle, implement [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) as the delegate for your `BrazeContentCardUI.ViewController`.

{% alert note %}
For more information about iOS view controller options, refer to the [Apple developer documentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

The `BrazeUI` library of the Swift SDK provides two default view controller contexts: [navigation](#swift_navigation) or [modal](#swift_modal). This means you can integrate Content Cards in these contexts by adding a few lines of code to your app or site. Both views offer customization and styling options as described in the [customization guide]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). You can also create a custom Content Card view controller instead of using the standard Braze one for even more customization options&#8212;refer to the [Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) for an example.

{% alert important %}
To handle control variant Content Cards in your custom UI, pass in your [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) object, then call the `logImpression` method as you would with any other Content Card type. The object will implicitly log a control impression to inform our analytics of when a user would have seen the control card.
{% endalert %}

### Navigation

A navigation controller is a view controller that manages one or more child view controllers in a navigation interface. Here is an example of pushing a `BrazeContentCardUI.ViewController` instance into a navigation controller:

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

### Modal

Use modal presentations to create temporary interruptions in your app’s workflow, such as prompting the user for important information. This model view has a navigation bar on top and a **Done** button on the side of the bar. Here is an example of pushing a `BrazeContentCard.ViewController` instance into a modal controller:

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

For example usage of `BrazeUI` view controllers, check out the corresponding Content Cards UI samples in our [Examples app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Base card model

The Content Cards data model is available in the `BrazeKit` module of the Braze Swift SDK. This module contains the following Content Card types, which are an implementation of the `Braze.ContentCard` type. For a full list of Content Card properties and their usage, see  [`ContentCard` class](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard). 

- Image only
- Captioned image
- Classic
- Classic image
- Control

To access the Content Cards data model, call `contentCards.cards` on your `braze` instance. See [Logging analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for more information on subscribing to card data.

{% alert note %}
Keep in mind, `BrazeKit` offers an alternative [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) class for Objective-C compatibility.
{% endalert %}

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details, refer to the [`Context` class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)
