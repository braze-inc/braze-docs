---
nav_title: Custom On Click Behavior
article_title: Customizing In-App Message On Click Behavior for iOS
platform: Swift
page_order: 5
description: "This reference article covers custom in-app messaging on-click behavior for your iOS application."
channel:
  - in-app messages
---

{% alert note %}
This article includes information on News Feed, which is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel, as it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more details.
{% endalert %}

# Customizing in-app message click behaviors

Each `Braze.InAppMessage` object can contain an instance of [`Context`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessageraw/context-swift.class), which defines various action behaviors, like click actions for example. If you wish to customize the logging behavior of your in-app messages, you can initialize your `Context` with the following sample:

{% tabs %}
{% tab swift %}

```swift
inAppMessage.context = .init(logImpression: {
  // Log impression
}, logClick: { buttonId in
  // Log click
}, processClickAction: { clickAction, url in
  // Process click action
}, logError: { error in
  // Log error
}, braze: {
  // Return Braze instance
}, discard: {
  // Discard the message
}, multipleLogClickEnabled: true)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
inAppMessage.context = [[BRZInAppMessageContext alloc] initWithLogImpression:^{
  // Log impression
} logClick:^(NSString * buttonId) {
  // Log click
} processClickAction:^(enum BRZInAppMessageRawClickAction clickAction, NSURL * url) {
  // Process click action
} logError:^(NSError * error) {
  // Log error
} braze:^id {
  // Return Braze instance
} discard:^{
  // Discard the message
} multipleLogClickEnabled:YES];
```

{% endtab %}
{% endtabs %}

## Click action types

The `clickAction` property on your `Braze.InAppMessage` defaults to `.none` but can be set to one of the following values:

| `ClickAction` | On-Click Behavior |
| -------------------------- | -------- |
| `.newsFeed` | The News Feed will be displayed when the message is clicked, and the message will be dismissed. |
| `.url(URL, useWebView: Bool)` | Opens the given URL. If `useWebView` is set to `true`, it will open in a web view. |
| `.none` | The message will be dismissed when clicked. |
{: .reset-td-br-1 .reset-td-br-2}

## Customizing in-app message and button clicks

The following [`BrazeInAppMessageUIDelegate`][34] delegate method is called when an in-app message is clicked. For clicks on in-app message buttons and HTML in-app message buttons (i.e., links), a button ID is provided as an optional parameter.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

This method returns a boolean value to indicate if Braze should continue to execute the click action.

To access the click action type of a button in a delegate method, you can use the following code:

{% tabs %}
{% tab swift %}

```swift
var buttons: [Braze.InAppMessage.Button] = []
switch message {
case .modal(let modal):
  buttons = modal.buttons
case .modalImage(let modalImage):
  buttons = modalImage.buttons
case .full(let full):
  buttons = full.buttons
case .fullImage(let fullImage):
  buttons = fullImage.buttons
case .slideup(_), .html(_), .control(_):
  break
@unknown default:
  break
}

for button in buttons {
  // Process `button.clickAction`
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if (message.buttons) {
  for (BRZInAppMessageRawButton *button in message.buttons) {
    // Process `button.clickAction`
  }
}
```

{% endtab %}
{% endtabs %}

[34]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate
