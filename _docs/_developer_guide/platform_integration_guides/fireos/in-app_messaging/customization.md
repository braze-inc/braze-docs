---
nav_title: Customization
platform: FireOS
page_order: 2
---

# Customization {#in-app-message-customization}
All of Braze’s in-app message types are highly customizable across messages, images, [Font Awesome][15]  icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

## Key-Value Pair Extras

In-app message objects may carry key-value pairs as `extras`. They are specified on the dashboard under "Advanced Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by the application.

Call the following when you get an in-app message object to retrieve its extras:

```java
Map<String, String> getExtras()
```

See the [Javadoc][44] for more information.

## Custom Styling

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

### Using Custom Styling to Set a Custom Font

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

## Setting Custom Listeners

Before customizing in-app messages with custom listeners, it's important to understand the [`AppboyInAppMessageManager`][34], which handles the majority of in-app message handling. As described in [Step 1][5], it must be registered for in-app messages to function appropriately.

`AppboyInAppMessageManager` manages in-app message display on Android.  It contains helper class instances that help it manage the lifecycle and display of in-app messages. All of these classes have standard implementations and defining custom classes is completely optional. However, doing so can add another level of control over the display and behavior of in-app messages.  These customizable classes include:

- [`IInAppMessageManagerListener`][21] - Implement to [custom manage in-app message display and behavior][19].
- [`IInAppMessageViewFactory`][42] - Implement to [build custom in-app message views][12].
- [`IInAppMessageAnimationFactory`][20] - Implement to [define custom in-app message animations][22].

### Setting a Custom Manager Listener

The `AppboyInAppMessageManager` automatically handles the display and lifecycle of in-app messages.  If you require more control over the lifecycle of a message, setting a custom manager listener will enable you to receive the in-app message object at various points in the in-app message lifecycle, allowing you to handle its display yourself, perform further processing, react to user behavior, process the object's [Extras][14], and much more.

#### Step 1: Implement an In-App Message Manager Listener

Create a class that implements [`IInAppMessageManagerListener`][21]

The callbacks in your `IInAppMessageManagerListener` will be called at various points in the in-app message lifecycle.

For example, if you set a custom manager listener, when an in-app message is received from Braze, the `beforeInAppMessageDisplayed()` method will be called. If your implementation of this method returns [`InAppMessageOperation.DISCARD`][83], that signals to Braze that the in-app message will be handled by the host app and should not be displayed by Braze. If `InAppMessageOperation.DISPLAY_NOW` is returned, Braze will attempt to display the in-app message. This method should be used if you choose to display the in-app message in a customized manner.

`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons.  A common use case would be intercepting a message when a button or message is clicked for further processing.

- See [`CustomInAppMessageManagerListener.java`][36] in our Droidboy sample app for an implementation example.

#### Step 2: Instruct Braze to use your In-App Message Manager Listener

Once your `IInAppMessageManagerListener` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageManagerListener` instead of the default listener.

>  We recommend setting your `IInAppMessageManagerListener` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom listener is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

#### In-Depth: Altering In-App Messages Before Display

When a new in-app message is received, and there is already an in-app message being displayed, the new message will be put onto the top of the stack and can be displayed at a later time.

However, if there is no in-app message being displayed, the following delegate method in `IInAppMessageManagerListener` will be called:

```java
  @Override
  public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
    return InAppMessageOperation.DISPLAY_NOW;
  }
```

The `InAppMessageOperation()` return value can be used to control when the message should be displayed. The suggested usage of this method would be to delay messages in certain parts of the app by returning `DISPLAY_LATER` when in-app messages would be distracting to the user's app experience.

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

### Setting a Custom View Factory {#custom-view}

Braze's suite of in-app messages types are versatile enough to cover the vast majority of custom use cases.  However, if you would like to fully define the visual appearance of your in-app messages instead of using a default type, Braze makes this possible via setting a custom view factory.

#### Step 1: Implement an In-App Message View Factory

Create a class that implements [`IInAppMessageViewFactory`][42]

- See [`CustomInAppMessageViewFactory.java`][43] in our Droidboy sample app for an implementation example.

#### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageViewFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageViewFactory` instead of the default view factory.

>  We recommend setting your `IInAppMessageViewFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom view factory is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

#### In-Depth: Implementing a Braze View Interface

Braze's `slideup` in-app message view implements [`IInAppMessageView`][25].  Braze's `full` and `modal` type message views implement [`IInAppMessageImmersiveView`][24].  Implementing one of these classes will allow Braze to add click listeners to your custom view where appropriate.  All Braze view classes extend Android's [View][18] class.

Implementing `IInAppMessageView` allows you to define a certain portion of your custom view as clickable.  Implementing `IInAppMessageImmersiveView` allows you to define message button views and a close button view.

- See [`CustomInAppMessageView.java`][26] in our Droidboy sample app for an implementation example.

### Setting a Custom Animation Factory

In-app messages have preset animation behavior. `Slideup` type messages slide into the screen; `full` and `modal` messages fade in and out.  If you would like to define custom animation behaviors for your in-app messages, Braze makes this possible via setting a custom animation factory.

#### Step 1: Implement an In-App Message Animation Factory

Create a class that implements [`IInAppMessageAnimationFactory`][20]

- See [`CustomInAppMessageAnimationFactory.java`][9] in our Droidboy sample app for an implementation example.

#### Step 2: Instruct Braze to use your In-App Message View Factory

Once your `IInAppMessageAnimationFactory` is created, call `AppboyInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` to instruct `AppboyInAppMessageManager`
to use your custom `IInAppMessageAnimationFactory` instead of the default animation factory.

>  We recommend setting your `IInAppMessageAnimationFactory` in your [`Application.onCreate()`][82] before any other calls to Braze. This will ensure that the custom animation factory is set before any in-app message is displayed.

See [`InAppMessageTesterFragment.java`][2] in the DroidBoy sample app for an example implementation.

## Setting Fixed Orientation

To set a fixed orientation for an in-app message, first [set a custom in-app message manager listener][19]. Then, call `setOrientation()` on the `IInAppMessage` object in the `beforeInAppMessageDisplayed()` delegate method.

```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
 inAppMessage.setOrientation(Orientation.PORTRAIT);
 return InAppMessageOperation.DISPLAY_NOW;
}
```

## GIFs {#gifs-IAMs}

{% include archive/android/gifs.md channel="in-app messages" %}

## Advanced Notes
### Android Dialogs

Braze doesn't support displaying in-app messages in [Android Dialogs][39] at this time.

### Button Text Capitalization

Android Material Design specifies that Button text should be upper case by default. Braze's in-app message buttons follow this convention as well.

### Youtube in HTML in-app messages

Starting in Braze Android SDK version 2.0.1, Youtube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see the [Android developer guide][71] for more details. Also, that hardware acceleration is only available on API versions 11 and above.

[1]: https://github.com/Appboy/appboy-android-sdk/tree/master/samples/manual-session-integration
[2]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/InAppMessageTesterFragment.java
[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html
[4]: {{site.baseurl}}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/values/styles.xml
[7]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageImmersive.html
[9]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageAnimationFactory.java
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-view-factory
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#key-value-pairs
[15]: http://fortawesome.github.io/Font-Awesome/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#modal-in-app-messages
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-manager-listener
[20]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageAnimationFactory.java
[21]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/listeners/IInAppMessageManagerListener.java
[22]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#setting-a-custom-animation-factory
[23]: http://developer.android.com/reference/android/R.integer.html#config_shortAnimTime
[24]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageImmersiveView.java
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageView.java
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageView.java
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageImmersiveBase.html
[29]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessage.java
[30]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[34]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/AppboyInAppMessageManager.java
[36]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageManagerListener.java
[39]: https://developer.android.com/guide/topics/ui/dialogs.html
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#html-full-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#full-in-app-messages
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/IInAppMessageViewFactory.java
[43]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomInAppMessageViewFactory.java
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessage.html#getExtras()
[45]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/IInAppMessageHtml.html
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[54]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#in-app-message-customization
[55]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/#gifs-iams
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/#activity-lifecycle-callback-integration-api-14
[60]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/res/values-xlarge/styles.xml
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[66]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestInAppMessageRefresh--
[67]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#requestDisplayInAppMessage--
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/
[69]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[70]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[71]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/push_notifications/silent_push_notifications/#silent-push-notifications
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/IAMeventTrigger.png %}
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-1-register-your-broadcastreceiver
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[80]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#registerInAppMessageManager-android.app.Activity-
[81]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/inappmessage/AppboyInAppMessageManager.html#unregisterInAppMessageManager-android.app.Activity-
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/inappmessage/InAppMessageOperation.java
