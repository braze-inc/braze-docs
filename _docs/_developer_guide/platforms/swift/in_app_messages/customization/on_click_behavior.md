---
nav_title: On-Click Behavior
article_title: Custom on-click behavior for the Braze Swift SDK
platform: Swift
description: "This reference article covers custom iOS in-app messaging on-click behavior for the Swift SDK."
channel:
  - in-app messages
---

# Custom on-click behavior

> Each `Braze.InAppMessage` object contains a corresponding [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), which defines the behavior upon clicking. 

## Click action types

The `clickAction` property on your `Braze.InAppMessage` defaults to `.none` but can be set to one of the following values:

| `ClickAction` | On-Click Behavior |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Opens the given URL in an external browser. If `useWebView` is set to `true`, it will open in a web view. |
| `.newsFeed` | News Feed will be displayed when the message is clicked, and the message will be dismissed.<br><br>**Note:** The News Feed is being deprecated. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more details. |
| `.none` | The message will be dismissed when clicked. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
For in-app messages containing buttons, the message `clickAction` will also be included in the final payload if the click action is added prior to adding the button text.
{% endalert %}

## Customizing on-click behavior

To customize this behavior, you may modify the `clickAction` property by referring to the following sample:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

The `inAppMessage(_:prepareWith:)` method is not available in Objective-C.

{% endtab %}
{% endtabs %}

## Customizing in-app message and button clicks

The following [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) delegate method is called when an in-app message is clicked. For clicks on in-app message buttons and HTML in-app message buttons (links), a button ID is provided as an optional parameter.

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
