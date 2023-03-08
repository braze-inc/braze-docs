---
nav_title: In-App Message UI Delegate
article_title: In-App Message UI Delegate for iOS
platform: Swift
page_order: 2
description: "This reference article covers setting an in-app messaging delegate for your iOS application."
channel:
  - in-app messages

---

# In-App Message UI Delegate for iOS

If you are using the default [`BrazeInAppMessageUI`][1] implementation as your `inAppMessagePresenter`, set the optional [`BrazeInAppMessageUIDelegate`][34] to customize the presentation of in-app messages and react to various lifecycle events.

`BrazeInAppMessageUIDelegate` can be used to receive triggered in-app message payloads for further processing, receive display lifecycle events, and control display timing. 

Note that if you do not include the `BrazeUI` library in your project, this delegate protocol is unavailable.

## Setting the in-app message delegate

Set your [`BrazeInAppMessageUIDelegate`][34] delegate object on the Braze instance by following this sample code:

{% tabs %}
{% tab swift %}

First, implement the `BrazeInAppMessageUIDelegate` protocol and any corresponding methods you wish. In our example below, we are implementing this protocol in our application's `AppDelegate` class.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

Then assign the `delegate` object on the `BrazeInAppMessageUI` instance before assigning this in-app message UI as your `inAppMessagePresenter`.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIVE-C %}

First, implement the `BrazeInAppMessageUIDelegate` protocol and any corresponding methods you wish. In our example below, we are implementing this protocol in our application's `AppDelegate` class.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

Then assign the `delegate` object on the `BrazeInAppMessageUI` instance before assigning this in-app message UI as your `inAppMessagePresenter`.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

Not all delegate methods are available in Objective-C due to the incompatibility of their parameters with the language runtime.

{% endtab %}
{% endtabs %}

### Step-by-step guide

For a step-by-step implementation of the in-app message UI delegate, refer to this [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Customizing in-app message orientation for iOS

### Setting a preferred orientation

You can configure all in-app messages to display in a specific orientation&mdash;either `.portrait` or `.landscape`&mdash;regardless of device orientation. To set a preferred orientation, use the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) to set the `preferredOrientation` property on the `PresentationContext`. 

{% tabs %}
{% tab swift %}

For example, to create a preferred orientation of portrait:

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

The `inAppMessage(_:prepareWith:)` method is not available in Objective-C.

{% endtab %}
{% endtabs %}

Note that the device orientation must also be supported by the in-app message's `orientation` property for the message to display.

### Modifying message orientations

You may alternatively set the orientation on a per-message basis. To do this, set the `orientation` property on a given `Braze.InAppMessage`:

{% tabs %}
{% tab swift %}

```swift    
// Set inAppMessage orientation to portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

In-app messages will not display if the device orientation does not match the `orientation` property on the in-app message.

{% alert note %}
For iPads, in-app messages will appear in the user's preferred orientation style regardless of actual screen orientation.
{% endalert %}

## Hiding the status bar during display

For `Full`, `FullImage` and `HTML` in-app messages, the SDK will hide the status bar by default. For other types of in-app messages, the status bar is left untouched. To configure this behavior, use the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) to set the `statusBarHideBehavior` property on the `PresentationContext`. This field takes one of the following values:

| Status Bar Hide Behavior            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | The message view decides the status bar hidden state.                                 |
| `.hidden`                           | Always hide the status bar.                                                           |
| `.visible`                          | Always display the status bar.                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Customizing display timing 

You can control if an available in-app message will display during certain points of your user experience. If there are situations where you would not want the in-app message to appear, such as during a full-screen game or on a loading screen, you can delay or discard pending in-app message messages. To control the timing of in-app message, use the `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to set the `BrazeInAppMessageUI.DisplayChoice` property. 

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

Configure `BrazeInAppMessageUI.DisplayChoice` to return one of the following values:

| Display Choice                      | Behavior                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.now`                              | The message will be displayed immediately. This is the default value.                 |
| `.later`                            | The message will be not be displayed and will be placed back on the top of the stack. |
| `.discard`                          | The message will be discarded and will not be displayed.                              |
{: .reset-td-br-1 .reset-td-br-2}

## Implementation samples

See `InAppMessageUI` in our Examples folder for a sample in [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) and [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui
[34]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate
