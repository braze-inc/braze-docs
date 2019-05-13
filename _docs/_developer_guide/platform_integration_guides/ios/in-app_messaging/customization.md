---
nav_title: Customization
platform: iOS
page_order: 1
search_rank: 5
---

# Customization {#in-app-message-customization}

All of Braze's in-app message types are highly customizable across messages, images, [Font Awesome][26] icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard][13]. Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

## Key-Value Pair Extras

`ABKInAppMessage` objects may carry key-value pairs as `extras`. These are specified on the dashboard when creating an in-app message campaign. Key-value pairs can be used to send data down along with an in-app message for further handling by your app, allowing you to add custom behaviors on top of what Braze provides.

## Setting Delegates

In-app message display and delivery customizations can be accomplished in code by setting delegates. All of these customizations are entirely optional.

### In-App Message Controller Delegate

This delegate contains one method [`beforeInAppMessageDisplayed:`][32] and is part of our [`Core` subspec][33].

Set the `delegate` on `ABKInAppMessageController` by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

In some cases (e.g., on session start), the in-app message may be triggered and displayed before the in-app message delegate is set. To guard against this, you can also set the in-app message delegate in the `appboyOptions` with key `ABKInAppMessageControllerDelegateKey` in [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][31].
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.startWithApiKey("YOUR-API-KEY",
                       inApplication:application,
                       withLaunchOptions:launchOptions,
                       withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ]])
```
{% endtab %}
{% endtabs %}

### In-App Message UI Delegate

This [delegate][34] can be used with our `UI` and `InAppMessage` subspecs.

Set this delegate by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController.setInAppMessageUIDelegate(self);
```

{% endtab %}
{% endtabs %}

See our [in-app message sample app][35] for an example.

### Migrate from Version 3.2.3 and Earlier

To migrate from version 3.2.3 or earlier, change the code with your delegate methods to conform to the ABKInAppMessageUIDelegate protocol instead of the ABKInAppMessageControllerDelegate and set the delegate by calling:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController.setInAppMessageUIDelegate(self);
```

{% endtab %}
{% endtabs %}

## Customizing Fixed Orientation

### Setting Orientation For All In-App Messages

To set a fixed orientation for all in-app messages, you can set the `supportedOrientationMasks` property on `ABKInAppMessageController`. Add the following code after your app's call to `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
[Appboy sharedInstance].inAppMessageController.supportedOrientationMasks = UIInterfaceOrientationMaskPortrait;
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
Appboy.sharedInstance()?.inAppMessageController.supportedOrientationMasks = portrait;
// Use landscape to display in-app messages in landscape
```

{% endtab %}
{% endtabs %}

Following this, all in-app messages will be displayed in the supported orientation, regardless of device orientation. Please note that the device orientation must also be supported by the in-app message's `orientation` property in order for the message to display. For more information, see the section below.

### Setting Orientation Per In-App Message

You may alternatively set orientation on a per-message basis. To do this, [set an in-app message delegate][23]. Then, in the `beforeInAppMessageDisplayed:` delegate method or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` UI delegate method, set the `orientation` property on the `ABKInAppMessage`. For example:

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

In-app messages will not display if the device orientation does not match the `orientation` property on the in-app message.

## Customizing In-App Message Display Behavior

The following delegate method is called each time right before an in-app message is displayed:

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

If you have only implemented the UI delegate, the following UI delegate method will be called instead:

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
| `ABKDisplayInAppMessageNow` | The message will be displayed immediately |
| `ABKDisplayInAppMessageLater` | The message will be not be displayed and will be placed back on the top of the stack |
| `ABKDiscardInAppMessage` | The message will be discarded and will not be displayed |

You can use the `beforeInAppMessageDisplayed:` delegate method to add in-app message display logic, customize in-app messages before Braze displays them, or opt-out of Braze's in-app message display logic and UI entirely.

For an implementation example, see our [In-App Message Sample Application][36].

>  If you are using the `Core` subspec, this is the method where you should customize and display your in-app message, and then return `ABKDiscardInAppMessage`.

### Overriding In-App Messages Before Display

If you would like to alter the display behavior of in-app messages, you should add any necessary display logic to the `beforeInAppMessageDisplayed:` delegate method or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` UI delegate method. For example, you might want to display the in-app message from the top of the screen if the keyboard is currently being displayed, or take the in-app message data model and display the in-app message yourself.

### Logging Impressions and Clicks

Logging in-app message impressions and clicks is not automatic when you implement completely custom handling (*i.e.* if you circumvent Braze's in-app message display by returning `ABKDiscardInAppMessage` in the `beforeInAppMessageDisplayed:` delegate method or the deprecated `beforeInAppMessageDisplayed:withKeyboardIsUp:` UI delegate method). If you choose to implement your own UI using our in-app message models, you must log analytics with the following methods on the `ABKInAppMessage` class:

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
// Registers that a user has viewed a in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on a in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

Furthermore, you should be logging button clicks on subclasses of `ABKInAppMessageImmersive` (*i.e*., `Modal` and `Full` in-app messages):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
/// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
/// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Customizing In-App Message Behavior on Click
The `inAppMessageClickActionType` property on the `ABKInAppMessage` defines the action behavior after the in-app message is clicked. This property is read only. If you want to change the in-app message's click behavior, you can call the following method on `ABKInAppMessage`:

```objc
- (void)setInAppMessageClickAction:(ABKInAppMessageClickActionType)clickActionType
                           withURI:(NSURL *)uri;
```

The `inAppMessageClickActionType` can be set to one of the following values:

| `ABKInAppMessageClickActionType` | On-Click Behavior |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | The News Feed will be displayed when the message is clicked, and the message will be dismissed. **Note**: The `uri` parameter will be ignored, and the `uri` property on the `ABKInAppMessage` will be set to nil. |
| `ABKInAppMessageRedirectToURI` | The given URI will be displayed when the message is clicked, and the message will be dismissed. **Note**: The `uri` parameter cannot be nil. |
| `ABKInAppMessageNoneClickAction` | The message will be dismissed when clicked. **Note**: The `uri` parameter will be ignored, and the `uri` property on the `ABKInAppMessage` will be set to nil. |

### Customizing In-App Message Body Clicks

>  This method cannot be used when using the `Core` subspec.

The following UI delegate method is called when the in-app message is clicked, and can be used to customize in-app message on-click behavior:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

### Customizing In-App Message Button Clicks

>  These methods cannot be used when using the `Core` subspec.

For clicks on in-app message buttons and HTML in-app message buttons (*i.e.*, links), you can also use the following delegate methods for customization:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Each method returns a `BOOL` value to indicate if Braze should continue to execute the click action.

To access the click action type of a button in a delegate method, you can use the following code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

>  When an in-app message has buttons, the only click actions that will be executed are the ones on the ABKInAppMessageButton model. The in-app message body will not be clickable even though the ABKInAppMessage model will have the default click action ("News Feed") assigned.

## Display In-App Messages In a Custom View Controller

In-app messages can also be displayed within a custom view controller which you pass to Braze. Braze will animate the customized in-app message in and out, as well as handle analytics of the in-app message. The view controller must meet the following requirements:

- It must be a subclass or an instance of `ABKInAppMessageViewController`.
- The view of the returned view controller should be an instance of `ABKInAppMessageView` or its subclass.

The following UI delegate method is called every time an in-app message is offered to `ABKInAppMessageViewController` to allow the app would like to pass a custom view controller to Braze for in-app message display:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

All of our in-app message view controllers are open-sourced. You can use subclasses or categories to customize display or behavior of in-app messages.

See the [in-app message view controllers][37] for more details.

## Custom In-App Message Triggering

By default in-app messages are triggered by event types which are logged by the SDK. If you would like to trigger in-app messages by server-sent events you are also able to achieve this.

To enable this feature you would send a silent push to the device which allows the device to log a SDK based event. This SDK event would subsequently trigger the user-facing in-app message.

### Step 1: Handle Silent Push and Key Value Pairs
When building against iOS 10+ we recommend you integrate the UserNotifications framework. If you use the UserNotifications framework, add the following code within the `userNotificationCenter(_:willPresent:withCompletionHandler:)` method:

```objc
- (void)handleExtrasFromPush:(UNNotification *)notification {
 NSLog(@"A push was received");
NSDictionary *userInfo = notification.request.content.userInfo;
 if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil ) {
   // Here based on the extras key-value pair, you can run some custom code.
   [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
 };
```

This will be called when a notification is received whilst the application is in the foreground. When the silent push is received an SDK recorded event 'IAM Trigger' will be logged against the user profile.

### Step 2: Create a Push Campaign

Create a silent push campaign which is triggered via the server sent event. For details on how to create a silent push campaign please review this section of our [Docs][39].

![serverEventTrigger][40]

The push campaign must include key value pair extras which indicate that this push campaign is sent with the intention to log an SDK custom event. This event will be used to trigger the in-app message:

![IAMSilentPush][41]

The code within the `userNotificationCenter(_:willPresent:withCompletionHandler:)` method checks for key `IS_SERVER_EVENT` and will log an SDK custom event if this is present.

You are able to alter either the event name or event properties by sending the desired value within the key-value pair extras of the push payload. These extras can be used as the parameter of either the event name, or as an event property, when logging the custom event.

### Step 3: Create an In-App Message Campaign

Create your user visible in-app message campaign from within Braze’s dashboard. This campaign should have an Action Based delivery, and be triggered from the custom event logged from within the `userNotificationCenter(_:willPresent:withCompletionHandler:)` method.

In the example below the specific in-app message to be trigger has been configured by sending the event property as part of the initial silent push.

![IAMPushTrigger][42]

>  Due to a push message being used to to record an SDK logged custom event, Braze will need to store a push token for each user in order to enable this solution. For iOS users, Braze will only store a token from the point that a user has been served the OS's push prompt. Prior to this the user will not be reachable using push and the above solution will not be possible.

## Method Declarations

For additional information see the following header files:

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageController.h`][15]
- [`ABKInAppMessageControllerDelegate.h`][16]
- [`ABKInAppMessageView.h`][17]
- [`ABKInAppMessageViewController.h`][18]

## Implementation Samples

See [`AppDelegate.m`][36], [`ViewController.m`][35] and [`CustomInAppMessageViewController.m`][19] in the in-app message sample app.

[1]: #customize-inAppMessage-dashboard
[2]: #customize-inAppMessage-code
[3]: #set-delegate
[4]: #customize-inAppMessage-display
[5]: #before-display
[6]: #manual-cue
[7]: #situational-display
[8]: #inAppMessage-click
[9]: #custom-view
[10]: #custom-inAppMessage
[11]: #custom-complete
[12]: #method-declarations
[13]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#creating-an-in-app-message
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessage.h
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageController.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[17]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageView.h
[18]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageViewController.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/CustomInAppMessageViewController.m
[21]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[23]: #setting-delegates
[25]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#2121
[26]: http://fortawesome.github.io/Font-Awesome/
[27]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messages-triggered
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: {{ site.baseurl  }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#setting-delegates
[31]: #customizing-appboy-on-startup
[32]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKInAppMessageControllerDelegate.h
[33]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/InAppMessage/ABKInAppMessageUIDelegate.h
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/InAppMessage/ViewControllers
[38]: #in-app-mssage-ui-delegate
[39]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}
