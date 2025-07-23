{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Setting up the UI delegate (required)

To customize the presentation of in-app messages and react to various lifecycle events, you'll need to set up [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). This is a delegate protocol used for receiving and processing triggered in-app message payloads, receiving display lifecycle events, and controlling display timing. To use `BrazeInAppMessageUIDelegate`, you must:
- Use the default [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) implementation as your `inAppMessagePresenter`. 
- Include the `BrazeUI` library in your project.

### Step 1: Implement the `BrazeInAppMessageUIDelegate` protocol 

First, implement the `BrazeInAppMessageUIDelegate` protocol and any corresponding methods you wish. In our example below, we are implementing this protocol in our application's `AppDelegate` class.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Step 2: Assign the `delegate` object 

Assign the `delegate` object on the `BrazeInAppMessageUI` instance before assigning this in-app message UI as your `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
Not all delegate methods are available in Objective-C due to the incompatibility of their parameters with the language runtime.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
For a step-by-step implementation of the in-app message UI delegate, refer to this [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## On-click behavior

Each `Braze.InAppMessage` object contains a corresponding [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), which defines the behavior upon clicking. 

### Click action types

The `clickAction` property on your `Braze.InAppMessage` defaults to `.none` but can be set to one of the following values:

| `ClickAction` | On-Click Behavior |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Opens the given URL in an external browser. If `useWebView` is set to `true`, it will open in a web view. |
| `.none` | The message will be dismissed when clicked. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
For in-app messages containing buttons, the message `clickAction` will also be included in the final payload if the click action is added prior to adding the button text.
{% endalert %}

### Customizing on-click behavior

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

### Handling the custom behavior

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

## Customizing modal dismissals

To enable outside tap dismissals, you can modify the `dismissOnBackgroundTap` property on the `Attributes` struct of the in-app message type you wish to customize. 

For example, if you wish to enable this feature for modal image in-app messages, you can configure the following:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

Customization via `Attributes` is not available in Objective-C.

{% endtab %}
{% endtabs %}

The default value is `false`. This determines if the modal in-app message will be dismissed when the user taps outside of the in-app message.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `true`         | Modal in-app messages will be dismissed on outside tap.     |
| `false`        | Default, modal in-app messages will not be dismissed on outside tap. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details on in-app message customization, refer to this [article](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Customizing message orientation

You can customize the orientation of your in-app messages. You can set a new default orientation for all messages or set a custom orientation for a single message.

{% tabs local %}
{% tab all messages %}
To choose a default orientation for all in-app messages, use the [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) method to set the `preferredOrientation` property on the `PresentationContext`. 

For example, to set portrait as the default orientation:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab single message %}
To set the orientation for a single message, modify the `orientation` property of `Braze.InAppMessage`:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

After the in-app message is displayed, any device orientation changes while the message is still being displayed will cause the message to rotate with the device (provided it's supported by the message's `orientation` configuration).

The device orientation must also be supported by the in-app message's `orientation` property for the message to display. Additionally, the `preferredOrientation` setting will only be respected if it is included in your application's supported interface orientations under the **Deployment Info** section of your target's settings in Xcode.

![Supported orientations in Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
The orientation is applied only for the presentation of the message. After the device changes orientation, the message view adopts one of the orientations it supports. On smaller devices (iPhones, iPod Touch), setting a landscape orientation for a modal or full in-app message may lead to truncated content.
{% endalert %}

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

{% alert tip %}
For a sample of `InAppMessageUI`, check out our [Swift Braze SDK repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) and [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Hiding the status bar

For `Full`, `FullImage` and `HTML` in-app messages, the SDK will hide the status bar by default. For other types of in-app messages, the status bar is left untouched. To configure this behavior, use the `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) to set the `statusBarHideBehavior` property on the `PresentationContext`. This field takes one of the following values:

| Status Bar Hide Behavior            | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | The message view decides the status bar hidden state.                                 |
| `.hidden`                           | Always hide the status bar.                                                           |
| `.visible`                          | Always display the status bar.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

## Customizing the app store review prompt

You can use in-app messages in a campaign to ask users for an App Store review.

{% alert note %}
Because this example prompt overrides default behavior of Braze, we cannot automatically track impressions if it is implemented. You must [log your own analytics]({{site.baseurl}}/developer_guide/analytics/).
{% endalert %}

### Step 1: Set the in-app message delegate

First, set the [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required) in your app. 

### Step 2: Disable the default App Store review message

Next, implement the `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) to disable the default App Store review message.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Step 3: Create a deep link

In your deep link handling code, add the following code to process the `{YOUR-APP-SCHEME}:app-store-review` deep link. Note that you will need to import `StoreKit` to use `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Step 4: Set custom on-click behavior

Next, create an in-app messaging campaign with the following:

- The key-value pair `"AppStore Review" : "true"`
- The on-click behavior set to "Deep Link Into App", using the deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limits App Store review prompts to a maximum of three times per year for each user, so your campaign should be [rate-limited]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) to three times per year per user.<br><br>Users may turn off App Store review prompts. As a result, your custom review prompt should not promise that a native App Store review prompt will appear or directly ask for a review.
{% endalert %}
