---
nav_title: Custom Display Handling
article_title: Customizing In-App Message Display Handling for iOS
platform: Swift
page_order: 4
description: "This reference article covers in-app messaging custom display handling for your iOS application."
channel:
  - in-app messages

---

# Custom handling in-app message display

When the [`BrazeInAppMessageUIDelegate`][16] is set, the following delegate method will determine when the in-app message will be displayed.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

You can customize in-app message handling by implementing this delegate method and returning one of the following values for `BrazeInAppMessageUI.DisplayChoice`:

| Display Choice                      | Behavior                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.now`                              | The message will be displayed immediately.                                            |
| `.later`                            | The message will be not be displayed and will be placed back on the top of the stack. |
| `.discard`                          | The message will be discarded and will not be displayed.                              |
{: .reset-td-br-1 .reset-td-br-2}

You can use the `inAppMessage(_:prepareWith:)` delegate method to add in-app message display logic, customize in-app messages before Braze displays them, or opt-out of Braze's in-app message display logic and UI entirely.

## Overriding in-app messages before display

If you would like to alter the display behavior of in-app messages, you should add any necessary display logic to your `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog). For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

If the in-app message campaign is not displaying when the session has been started, make sure you have the necessary display logic added to your `inAppMessage(_:prepareWith:)` delegate method. This allows the in-app message campaign to display from the top of the screen even if the keyboard is being displayed.

## Hiding the status bar during display

For `Full` and `HTML` in-app messages, the SDK will attempt to place the message over the status bar by default. However, in some cases, the status bar may still appear on top of the in-app message. Using the `PresentationContext` object in your `inAppMessage(_:prepareWith:)` delegate method, you can configure the behavior of the status bar by setting the `statusBarHideBehavior` property. This field takes one of the following values:

| Status Bar Hide Behavior            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | The message view decides the status bar hidden state.                                 |
| `.hidden`                           | Always hide the status bar.                                                           |
| `.visible`                          | Always display the status bar.                                                        |

## Logging impressions and clicks

Logging in-app message impressions and clicks is not automatic when you implement completely custom handling (i.e., you circumvent Braze's in-app message display by returning `.discard` in your `inAppMessage(_:displayChoiceForMessage:)`). If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `ABKInAppMessage` class:

{% tabs %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
message.context?.logImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
message.context?.logClick(buttonId: "button-id")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
[message.context logImpression];
// Registers that a user has clicked on an in-app message with the Braze server.
[message.context logClickWithButtonId:@"button-id"];
```

{% endtab %}
{% endtabs %}

## Implementation samples

See [`InAppMessages-CustomUI`][36] in-app message sample app.

[16]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate
[36]: https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessages-Custom-UI
