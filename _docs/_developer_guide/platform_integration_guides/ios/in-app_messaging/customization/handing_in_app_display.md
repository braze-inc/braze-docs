---
nav_title: Custom Display Handling
article_title: Customizing In-App Message Display Handling for iOS
platform: iOS
page_order: 4
description: "This reference article covers in-app messaging custom display handling for your iOS application."
channel:
  - in-app messages

---

# Custom handling in-app message display

When the [`ABKInAppMessageControllerDelegate`][16] is set, the following delegate method will be called before in-app messages are displayed:

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

If you have only implemented [`ABKInAppMessageUIDelegate`][34], the following UI delegate method will be called instead:

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
| `ABKDisplayInAppMessageNow` | The message will be displayed immediately. |
| `ABKDisplayInAppMessageLater` | The message will be not be displayed and will be placed back on the top of the stack. |
| `ABKDiscardInAppMessage` | The message will be discarded and will not be displayed. |
{: .reset-td-br-1 .reset-td-br-2}

You can use the `beforeInAppMessageDisplayed:` delegate method to add in-app message display logic, customize in-app messages before Braze displays them, or opt-out of Braze's in-app message display logic and UI entirely.

Check out our [sample application][36] for an implementation example.

## Overriding in-app messages before display

If you would like to alter the display behavior of in-app messages, you should add any necessary display logic to your `beforeInAppMessageDisplayed:` delegate method. For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

If the in-app message campaign is not displaying when the session has been started, make sure you have the necessary display logic added to your `beforeInAppMessageDisplayed:` delegate method. This allows the in-app message campaign to display from the top of the screen even if the keyboard is being displayed.

## Hiding the status bar during display

For `Full` and `HTML` in-app messages, the SDK will attempt to place the message over the status bar by default. However, in some cases, the status bar may still appear on top of the in-app message. As of version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) of the iOS SDK, you can force the status bar to hide when displaying `Full` and `HTML` in-app messages by setting `ABKInAppMessageHideStatusBarKey` to `YES` within the `appboyOptions` passed to `startWithApiKey:`.

## Logging impressions and clicks

Logging in-app message impressions and clicks is not automatic when you implement completely custom handling (i.e., you circumvent Braze's in-app message display by returning `ABKDiscardInAppMessage` in your `beforeInAppMessageDisplayed:`). If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `ABKInAppMessage` class:

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

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageControllerDelegate.h`][16]

## Implementation samples

See [`AppDelegate.m`][36] in-app message sample app.


[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h

