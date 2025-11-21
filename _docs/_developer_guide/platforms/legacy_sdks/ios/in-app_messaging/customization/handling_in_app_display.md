---
nav_title: Custom display handling
article_title: Customizing In-App Message Display Handling for iOS
platform: iOS
page_order: 4
description: "This reference article covers in-app messaging custom display handling for your iOS application."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Custom handling in-app message display

When the [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) is set, the following delegate method will be called before in-app messages are displayed:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

If you have only implemented [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h), the following UI delegate method will be called instead:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

You can customize in-app message handling by implementing this delegate method and returning one of the following values for `ABKInAppMessageDisplayChoice`:

| `ABKInAppMessageDisplayChoice` | Behavior |
| -------------------------- | -------- |
| Objective-C: `ABKDisplayInAppMessageNow`<br>Swift: `displayInAppMessageNow` | The message will be displayed immediately. |
| Objective-C: `ABKDisplayInAppMessageLater`<br>Swift: `displayInAppMessageLater` | The message will be not be displayed and will be placed back on the top of the stack. |
| Objective-C: `ABKDiscardInAppMessage`<br>Swift: `discardInAppMessage`| The message will be discarded and will not be displayed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can use the `beforeInAppMessageDisplayed:` delegate method to add in-app message display logic, customize in-app messages before Braze displays them, or opt out of the Braze in-app message display logic and UI entirely.

Check out our [sample application](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) for an implementation example.

## Overriding in-app messages before display

If you want to alter the display behavior of in-app messages, you should add any necessary display logic to your `beforeInAppMessageDisplayed:` delegate method. For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

If the in-app message campaign is not displaying when the session has been started, make sure you have the necessary display logic added to your `beforeInAppMessageDisplayed:` delegate method. This allows the in-app message campaign to display from the top of the screen even if the keyboard is being displayed.

## Disabling Dark Mode

To prevent in-app messages from adopting dark mode styling when the user device has dark mode enabled, use the [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d) property. From within either the `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` or `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:` method, set the `enableDarkTheme` property of the method's `inAppMessage` parameter to `NO`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## Hiding the status bar during display

For `Full` and `HTML` in-app messages, the SDK will attempt to place the message over the status bar by default. However, in some cases, the status bar may still appear on top of the in-app message. As of version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) of the iOS SDK, you can force the status bar to hide when displaying `Full` and `HTML` in-app messages by setting `ABKInAppMessageHideStatusBarKey` to `YES` within the `appboyOptions` passed to `startWithApiKey:`.

## Logging impressions and clicks

Logging in-app message impressions and clicks is not automatic when you implement completely custom handling (for example, you circumvent Braze in-app message display by returning `ABKDiscardInAppMessage` in your `beforeInAppMessageDisplayed:`). If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `ABKInAppMessage` class:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

Furthermore, you should be logging button clicks on subclasses of `ABKInAppMessageImmersive` (*i.e*., `Modal` and `Full` in-app messages):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Method declarations

For additional information, see the following header files:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Implementation samples

See [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) in-app message sample app.



