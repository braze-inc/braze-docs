---
nav_title: In-App Messaging
platform: FireOS
page_order: 2
search_rank: 4
---

# In-App Messaging

In-App Messages are great for creating unobtrusive calls to action, notifying people of new content in the News Feed and driving them toward it or communicating with users who have push turned off. They are also effective for other content that isn't time-sensitive enough to warrant a push notification, or permanent enough to warrant a News Feed item. You can find a detailed explanation of in-app message behavior in [Braze Docs][4].

## Integration {#in-app-messaging-integration}

### Step 1: Braze In-App Message Manager Registration

In-App Message display is managed by the [`AppboyInAppMessageManager`][34] class. Every activity in your app must be registered with the `AppboyInAppMessageManager` to allow it to add in-app message views to the view hierarchy. There are two ways to accomplish this:

#### Activity Lifecycle Callback Integration (Recommended)

The [Activity Lifecycle Callback Integration][59] handles in-app message registration automatically, no extra integration is required. This is the recommended integration for handling in-app message registration.

#### Manual In-App Message Registration

A manual in-app message registration requires 3 steps.

>  If you did the activity lifecycle integration, then you should *not* do a manual in-app message integration.

* In your [`Application.onCreate()`][82], [`ensureSubscribedToInAppMessageEvents()`][69] should be called.

```java
AppboyInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

* In every activity where in-app messages can be shown, [`registerInAppMessageManager()`][80] should be called in that activity's `onResume()`.

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the AppboyInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  AppboyInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

* In every activity where [`registerInAppMessageManager()`][80] was called, [`unregisterInAppMessageManager()`][81] should be called in that activity's `onPause()`.

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the AppboyInAppMessageManager for the current Activity.
  AppboyInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

## In-App Message Types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome][15] icons, click actions, analytics, editable styling and color schemes.  The currently available types are [`Slideup`][13], [`Modal`][17], [`Full`][41], and [`HTML Full`][40].  It is also possible to [define your own custom in-app message view][12].

All in-app messages implement the [`IInAppMessage`][3] interface, which defines basic behavior and traits for all in-app messages.  [`InAppMessageBase`][27] is an abstract class that implements `IInAppMessage` and provides the foundational in-app message implementation.  All in-app message classes are subclasses of `InAppMessageBase`.

In addition, there is a subinterface of `IInAppMessage` called [`IInAppMessageImmersive`][8], which adds click action and analytics enabled [buttons][50], as well as header text and a close button.  [`InAppMessageImmersiveBase`][28] is an abstract class that implements `IInAppMessageImmersive` and provides the foundational `immersive` in-app message implementation.  `Modal` and `Full` in-app messages are subclasses of `InAppMessageImmersiveBase`.

HTML Full in-app messages are [`InAppMessageHtmlFull`][51] instances, which implement [`IInAppMessageHtml`][52], another subclass of `IInAppMessage`.

{% include archive/in_app_message.md platform="Android" %}

### Local In-App Messages

In-app messages can be created within the app and displayed locally in real-time.  All customization options available on the dashboard are also available locally.  This is particularly useful for displaying messages that you wish to trigger within the app in real-time.

```java
  // Initializes a new slideup type in-app message and specifies its message.
  InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
  inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

>  Do not display in-app messages when the soft keyboard is displayed on screen as rendering is undefined in this circumstance.

#### Manually Triggering In-App Message Display

The following method will manually display your in-app message.

```java
  AppboyInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```
See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for example usage.

#### In-Depth: Defining Custom In-App Message Types

Braze's `slideup` in-app message object extends [`InAppMessageBase`][27].  Braze's `full` and `modal` type messages extend [`InAppMessageImmersiveBase`][28].  Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

See [`CustomInAppMessage.java`][29] in the DroidBoy sample app for an example implementation.

## Customization {#in-app-message-customization}

### Key-Value Pair Extras

In-app message objects may carry key-value pairs as `extras`. They are specified on the dashboard under "Advanced Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by the application.

Call the following when you get an in-app message object to retrieve its extras:

```java
Map<String, String> getExtras()
```

See the [Javadoc][44] for more information.

### Custom Styling

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the Braze SDK's [`styles.xml`][6] file.

```xml
  <style name="Appboy"/>
    <!-- In-app Message -->
  <style name="Appboy.InAppMessage">
  </style>
  <style name="Appboy.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">wrap_content</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_appboy_inappmessage_header_text_light</item>
    <item name="android:textSize">19.0sp</item>
    <item name="android:layout_gravity">center</item>
    <item name="android:singleLine">true</item>
    <item name="android:textStyle">bold</item>
  </style>
```

If you would prefer, you can override these styles to create a look and feel that better suits your app.

To override a style, copy it in its entirety to the `styles.xml` file in your own project and make modifications. The whole style must be copied over to your local `styles.xml` file in order for all attributes to be correctly set. Please note that these custom styles are for changes to individual UI elements, not wholesale changes to layouts. Layout-level changes need to be handled with custom views.

#### Using Custom Styling to Set a Custom Font

Braze allows for setting a custom font using the [font family guide][79]. To use it, override the style for message text, headers, and/or button text and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on your in-app message button text, override the `Appboy.InAppMessage.Button` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```
  <style name="Appboy.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aside from the `Appboy.InAppMessage.Button` style for button text, the style for message text is `Appboy.InAppMessage.Message` and the style for message headers is `Appboy.InAppMessage.Header`. If you want to use your custom font family across all possible in-app message text, you can set your font family on the `Appboy.InAppMessage` style, which is the parent style for all in-app messages.

>  As with other custom styles, the entire style must be copied over to your local `styles.xml` file for all attributes to be correctly set.

### Setting Custom Listeners

Before customizing in-app messages with custom listeners, it's important to understand the [`AppboyInAppMessageManager`][34], which handles the majority of in-app message handling. As described in [Step 1][5], it must be registered for in-app messages to function appropriately.

`AppboyInAppMessageManager` manages in-app message display on Android.  It contains helper class instances that help it manage the lifecycle and display of in-app messages. All of these classes have standard implementations and defining custom classes is completely optional. However, doing so can add another level of control over the display and behavior of in-app messages.  These customizable classes include:

- [`IInAppMessageManagerListener`][21] - Implement to [custom manage in-app message display and behavior][19].
- [`IInAppMessageViewFactory`][42] - Implement to [build custom in-app message views][12].
- [`IInAppMessageAnimationFactory`][20] - Implement to [define custom in-app message animations][22].

#### Setting a Custom Manager Listener

The `AppboyInAppMessageManager` automatically handles the display and lifecycle of in-app messages.  If you require more control over the lifecycle of a message, setting a custom manager listener will enable you to recieve the in-app message object at various points in the in-app message lifecycle, allowing you to handle its display yourself, perform further processing, react to user behavior, process the object's [Extras][14], and much more.

##### Step 1: Implement an In-App Message Manager Listener

Create a class that implements [`IInAppMessageManagerListener`][21]

The callbacks in your `IInAppMessageManagerListener` will be called at various points in the in-app message lifecycle.

For example, if you set a custom manager listener, when an in-app message is received from Braze, the `beforeInAppMessageDisplayed()` method will be called. If your implementation of this method returns [`InAppMessageOperation.DISCARD`][83], that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If `InAppMessageOperation.DISPLAY_NOW` is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons.  A common use case would be intercepting a message when a button or message is clicked for further processing.

- See [`CustomInAppMessageManagerListener.java`][36] in our Droidboy sample app for an implementation example.

##### Step 2: Instruct Braze to use your In-App Message Manager Listener

Once your `IInAppMessageManagerListener` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageManagerListener` instead of the default listener.

>  We recommend setting your `IInAppMessageManagerListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom listener is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

##### In-Depth: Altering In-App Messages Before Display

When a new in-app message is received, and there is already an in-app message being displayed, the new message will be put onto the top of the stack and can be displayed at a later time.

However, if there is no in-app message being displayed, the following delegate method in `IInAppMessageManagerListener` will be called:

```java
  @Override
  public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
    return InAppMessageOperation.DISPLAY_NOW;
  }
```

The `InAppMessageOperation()` return value can be used to control when the message should be displayed. A suggested usage of this method would be to delay messages in certain parts of the app by returning `DISPLAY_LATER` when in-app messages would be distracting to the user's app experience.

| `InAppMessageOperation` return value | Behavior |
| -------------------------- | -------- |
| `DISPLAY_NOW` | The message will be displayed |
| `DISPLAY_LATER` | The message will be returned to the stack and displayed at the next available opportunity |
| `DISCARD` | The message will be discarded |
| `null` | The message will be ignored. This method should __NOT__ return `null` |

See [`InAppMessageOperation.java`][45] for more details.

>  If you choose to `DISCARD` the in-app message and replace it with your own in-app message view, you will need to manually log in-app message clicks and impressions.

On Android, this is done by calling `logClick` and `logImpression` on in-app messages, and `logButtonClick` on immersive in-app messages.

>  Once an in-app message has been placed on the stack, you can request for it to be retrieved and displayed at any time by calling [`AppboyInAppMessageManager.getInstance().requestDisplayInAppMessage()`][67]. Calling this method requests Braze to display the next available in-app message from the stack.

#### Setting a Custom View Factory

Braze's suite of in-app messages types are versatile enough to cover the vast majority of custom use cases.  However, if you would like to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible via setting a custom view factory.

##### Step 1: Implement an In-App Message View Factory

Create a class that implements [`IInAppMessageViewFactory`][42]

- See [`CustomInAppMessageViewFactory.java`][43] in our Droidboy sample app for an implementation example.

##### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageViewFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageViewFactory` instead of the default view factory.

>  We recommend setting your `IInAppMessageViewFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom view factory is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

##### In-Depth: Implementing a Braze View Interface

Braze's `slideup` in-app message view implements [`IInAppMessageView`][25].  Braze's `full` and `modal` type message views implement [`IInAppMessageImmersiveView`][24].  Implementing one of these classes will allow Braze to add click listeners to your custom view where appropriate.  All Braze view classes extend Android's [View][18] class.

Implementing `IInAppMessageView` allows you to define a certain portion of your custom view as clickable.  Implementing `IInAppMessageImmersiveView` allows you to define message button views and a close button view.

- See [`CustomInAppMessageView.java`][26] in our Droidboy sample app for an implementation example.

##### Client Example

The following image is an example custom In-App Message view from a Braze client:

![Foodo In-App Message Customization Example][33]

#### Setting a Custom Animation Factory

In-app messages have preset animation behavior. `Slideup` type messages slide into the screen; `full` and `modal` messages fade in and out.  If you would like to define custom animation behaviors for your in-app messages, Braze makes this possible via setting a custom animation factory.

##### Step 1: Implement an In-App Message Animation Factory

Create a class that implements [`IInAppMessageAnimationFactory`][20]

- See [`CustomInAppMessageAnimationFactory.java`][9] in our Droidboy sample app for an implementation example.

##### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageAnimationFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageAnimationFactory` instead of the default animation factory.

>  We recommend setting your `IInAppMessageAnimationFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom animation factory is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

### Setting Fixed Orientation

To set a fixed orientation for an in-app message, first [set a custom in-app message manager listener][19]. Then, call `setOrientation()` on the `IInAppMessage` object in the `beforeInAppMessageDisplayed()` delegate method.

```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
 inAppMessage.setOrientation(Orientation.PORTRAIT);
 return InAppMessageOperation.DISPLAY_NOW;
}
```

## Server-side Event Triggering

By default in-app messages are triggered by custom events logged by the SDK. If you would like to trigger in-app messages by server sent events you are also able to achieve this.

To enable this feature, a silent push is sent to the device which allows a custom push receiver to log an SDK based event. This SDK event will subsequently trigger the user-facing in-app message.

### Step 1: Register a Custom Broadcast Receiver to Log Custom Event

Register your custom `BroadcastReceiver` to listen for a specific silent push within your AndroidManifest.xml. For more information on how to register a custom `BroadcastReceiver` please review [Braze's push documentation][78].

### Step 2: Create your BroadcastReceiver

Your receiver will handle the intent broadcast by the silent push and log an SDK event. Starting in SDK 2.0.0, events can be logged in the background without issue. All clients implementing this solution must be on SDK v2.0.0+.

It will subclass `BroadcastReceiver` and override `onReceive()`. For a detailed example, please see our [EventBroadcastReceiver.java][72] in the linked gist.

>  Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom `BroadcastReceiver`. To ensure the same event is not duplicated, the event logged from within your `BroadcastReceiver` should be given a generic naming convention, for example "in-app message trigger event," and not the same name as the server sent event. If this is not done segmentation and user data may be affected by duplicate events being logged for a single user action.

For further details on custom handling push receipts, opens, and key-value pairs please visit this section of our [Documentation][78].

### Step 3: Create a Push Campaign

Create a silent push campaign which is triggered via the server sent event. You can learn how to to this with our page on [how to create a silent push campaign][73].

![serverEventTrigger][75]

The push campaign must include key value pair extras which indicate that this push campaign is sent with the intention to log an SDK custom event. This event will be used to trigger the in-app message

![kvpConfiguration][76]

The [EventBroadcastReceiver.java][72] recognizes the key value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your 'In-App Message Trigger' event, you can achieve this by passing these in the key value pairs of the push payload. In the example above the campaign name of the subsequent in-app message has been included. Your custom `BroadcastReceiver` can then pass the value as the parameter of the event property when logging the custom event.

###  Step 4: Create an In-App Message Campaign

Create your user visible in-app message campaign from within Braze’s dashboard. This campaign should have an Action Based delivery, and be triggered from the custom event logged from within the custom [EventBroadcastReceiver.java][72].

In the example below the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![serverEventTrigger][77]

>  If a server sent event is logged whilst the app is not in the foreground, the event will log but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.

## GIFs {#gifs-IAMs}

{% include archive/android/gifs.md channel="in-app messages" %}

## Advanced Notes

#### Android Dialogs

Braze doesn't support displaying in-app messages in [Android Dialogs][39] at this time.

#### Button Text Capitalization

Android Material Design specifies that Button text should be upper case by default. Braze's in-app message buttons follow this convention as well.

#### Youtube in HTML in-app messages

Starting in Braze Android SDK version 2.0.1, Youtube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see the [Android developer guide][71] for more details. Also that hardware acceleration is only available on API versions 11 and above.

{% include archive/troubleshooting_iams.md platform="FireOS" %}

[1]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/InAppMessageTesterFragment.java
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[4]: {{ site.baseurl }}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/values/styles.xml
[7]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageImmersive.html
[9]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageAnimationFactory.java
[12]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-view-factory
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[14]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/news_feed/#key-value-pairs
[15]: http://fortawesome.github.io/Font-Awesome/
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#modal-in-app-messages
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-manager-listener
[20]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageAnimationFactory.java
[21]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.java
[22]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-animation-factory
[23]: http://developer.android.com/reference/android/R.integer.html#config_shortAnimTime
[24]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageImmersiveView.java
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageView.java
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageView.java
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageImmersiveBase.html
[29]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessage.java
[30]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#creating-an-in-app-message
[33]: {% image_buster /assets/img_archive/foodo-slideup.gif %}
[34]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/AppboyInAppMessageManager.java
[36]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[39]: https://developer.android.com/guide/topics/ui/dialogs.html
[40]: {{ site.baseurl }}/docs/developer_guide/platform_integration_guides/android/in-app_messaging/#html-full-in-app-messages
[41]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#full-in-app-messages
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageViewFactory.java
[43]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageViewFactory.java
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html#getExtras()
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html
[53]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[54]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#in-app-message-customization
[55]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/#gifs-iams
[59]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[60]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values-xlarge/styles.xml
[65]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[66]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestInAppMessageRefresh--
[67]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#requestDisplayInAppMessage--
[68]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/
[69]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[70]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[71]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{ site.baseurl }}/developer_guide/platform_integration_guides/fireos/push_notifications/silent_push_notifications/#silent-push-notifications
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/IAMeventTrigger.png %}
[78]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-1-register-your-broadcastreceiver
[79]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[80]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#registerInAppMessageManager-android.app.Activity-
[81]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#unregisterInAppMessageManager-android.app.Activity-
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
