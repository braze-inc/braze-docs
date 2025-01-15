---
nav_title: UI Delegates
article_title: Custom UI delegates for the Braze Swift SDK
platform: Swift
description: "This reference article covers setting an iOS in-app messaging delegate for the Swift SDK."
channel:
  - in-app messages

---

# Custom UI delegates

> Use the optional [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) to customize the presentation of in-app messages and react to various lifecycle events. This delegate protocol can be used to receive triggered in-app message payloads for further processing, receive display lifecycle events, and control display timing. 

## Prerequisites

To use `BrazeInAppMessageUIDelegate`:
* You must be using the default [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) implementation as your `inAppMessagePresenter`. 
* You must include the `BrazeUI` library in your project.

## Customizing the UI delegate

Set your [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) delegate object on the Braze instance by following this sample code:

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

{% alert tip %}
For a step-by-step implementation of the in-app message UI delegate, refer to this [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Customizing in-app message orientation for iOS

### Setting a preferred orientation

You can configure all in-app messages to be presented in a specific orientation regardless of device orientation. To set a preferred orientation, use the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) to set the `preferredOrientation` property on the `PresentationContext`. 

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

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

Once the in-app message has been presented, any device orientation changes while the message is still displayed will cause the message to rotate with the device, provided it is supported under the message's `orientation` configuration.

Note that the device orientation must also be supported by the in-app message's `orientation` property for the message to display. Additionally, the `preferredOrientation` setting will only be respected if it is included in your application's supported interface orientations under the **Deployment Info** section of your target's settings in Xcode.

![Supported orientations in Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
The orientation is applied only for the presentation of the message. After the device changes orientation, the message view adopts one of the orientations it supports. On smaller devices (iPhones, iPod Touch), setting a landscape orientation for a modal or full in-app message may lead to truncated content.
{% endalert %}

### Modifying message orientations

You may alternatively set the orientation on a per-message basis. This property defines all the available orientation types for that message. To do this, set the `orientation` property on a given `Braze.InAppMessage`:

{% tabs %}
{% tab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

## Disabling dark mode

To prevent in-app messages from adopting dark mode styling when the user device has dark mode enabled, implement the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) method. The `PresentationContext` passed to the method contains a reference to the `InAppMessage` object to be presented. Each `InAppMessage` has a `themes` property containing a `dark` and `light` mode theme. If you set the `themes.dark` property to `nil`, Braze will automatically present the in-app message using its light theme.

In-app message types with buttons have an additional `themes` object on their `buttons` property. To prevent buttons from adopting dark mode styling, you can use [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) to create a new array of buttons with a `light` theme and no `dark` theme.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Customizing button clicks

To access in-app message button information or override the click behavior, implement [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi). Return `true` to allow Braze to process the click action, or return `false` to override the behavior.
{% tabs %}
{% tab swift %}

```swift
  func inAppMessage(
    _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
    buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
  ) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Hiding the status bar during display

For `Full`, `FullImage` and `HTML` in-app messages, the SDK will hide the status bar by default. For other types of in-app messages, the status bar is left untouched. To configure this behavior, use the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) to set the `statusBarHideBehavior` property on the `PresentationContext`. This field takes one of the following values:

| Status Bar Hide Behavior            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | The message view decides the status bar hidden state.                                 |
| `.hidden`                           | Always hide the status bar.                                                           |
| `.visible`                          | Always display the status bar.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Customizing display timing 

You can control if an available in-app message will display during certain points of your user experience. If there are situations where you would not want the in-app message to appear, such as during a fullscreen game or on a loading screen, you can delay or discard pending in-app message messages. To control the timing of in-app message, use the `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to set the `BrazeInAppMessageUI.DisplayChoice` property. 

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

| Display Choice                      | Behavior                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | The message will be displayed immediately. This is the default value.                                                       |
| `.reenqueue`                        | The message will be not be displayed and will be placed back on the top of the stack.                                       |
| `.later`                            | The message will be not be displayed and will be placed back on the top of the stack. (Deprecated, please use `.reenqueue`) |
| `.discard`                          | The message will be discarded and will not be displayed.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Implementation samples

See `InAppMessageUI` in our Examples folder for a sample in [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) and [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

