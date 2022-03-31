---
nav_title: Integration
article_title: In-App Message Integration for Android and FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "This reference article covers how to integrate in-app messaging in your Android or FireOS application."
channel:
  - in-app messages

---

# In-app message integration

[In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) help you get content to your users without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value from your app. With various layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [case studies][83].

## In-app message types

Braze offers several default in-app message types, each customizable with messages, images, [Font Awesome][15] icons, click actions, analytics, editable styling, and color schemes. The currently available types are:

- [`Slideup`][91]
- [`Modal`][90]
- [`Full`][93]
- [`HTML Full`][92]

It is also possible to define your own [custom in-app message view][12].

All in-app messages implement the [`IInAppMessage`][3] interface, which defines all in-app messages' basic behavior and traits. [`InAppMessageBase`][27] is an abstract class that implements `IInAppMessage` and provides the foundational in-app message implementation. All in-app message classes are subclasses of `InAppMessageBase`.

In addition, there is a subinterface of `IInAppMessage` called [`IInAppMessageImmersive`][8], which adds click-action and analytics enabled [buttons][50], as well as header text and a close button. [`InAppMessageImmersiveBase`][28] is an abstract class that implements `IInAppMessageImmersive` and provides the foundational `immersive` in-app message implementation. `Modal` and `Full` in-app messages are subclasses of `InAppMessageImmersiveBase`.

HTML full in-app messages are [`InAppMessageHtmlFull`][51] instances, which implement [`IInAppMessageHtml`][52], another subclass of `IInAppMessage`.

### Expected behaviors by message type

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
{% tab Slideup %}
[`Slideup`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom right corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with two click-action and analytics-enabled buttons.

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}
[`Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) in-app messages are useful for maximizing the content and impact of your user communication. The upper half of a `full` in-app message contains an image, and the lower half displays text and up to two click action and analytics-enabled buttons.

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Custom HTML %}
[`HTML Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html) in-app messages are useful for creating fully customized user content. User-defined HTML full in-app message content is displayed in a `WebView` and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. <br><br>Android in-app messages support a JavaScript `brazeBridge` interface to call methods on the Braze Web SDK from within your HTML, see our <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/best_practices/">best practices</a> for more details.

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
We currently do not support the display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Defining custom in-app message types

The `slideup` in-app message object extends [`InAppMessageBase`][27]. 
The `full` and `modal` type messages extends [`InAppMessageImmersiveBase`][28]. Extending one of these classes gives you the option of adding custom functionality to your locally generated in-app messages.

## Integration {#in-app-messaging-integration}

### Step 1: Braze in-app message manager registration

In-app message display is managed by the [`BrazeInAppMessageManager`][34] class. Every activity in your app must be registered with the `BrazeInAppMessageManager` to allow it to add in-app message views to the view hierarchy. There are two ways to accomplish this:

#### Activity lifecycle callback integration (recommended)

The [activity lifecycle callback integration][59] handles in-app message registration automatically; no extra integration is required. This is the recommended integration for handling in-app message registration.

#### Manual in-app message registration

{% alert warning %}
If you did the activity lifecycle integration, you should *not* do a manual in-app message integration.
{% endalert %}

First, in your [`Application.onCreate()`][82], call [`ensureSubscribedToInAppMessageEvents()`][69]:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

Next, in every activity where in-app messages can be shown, [`registerInAppMessageManager()`][80] should be called in that activity's `onResume()`:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

Lastly, in every activity where [`registerInAppMessageManager()`][80] was called, [`unregisterInAppMessageManager()`][81] should be called in that activity's `onPause()`:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### Step 2: In-app message manager blacklist (optional)

In your integration, you may require that certain activities in your app should not show in-app messages. The [activity lifecycle callback integration][59] provides an easy way to accomplish this.

The following sample code adds two activities to the in-app message registration blacklist, `SplashActivity` and `SettingsActivity`:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlacklist = new HashSet<>();
    inAppMessageBlacklist.add(SplashActivity.class);
    inAppMessageBlacklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlacklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlacklist = HashSet<Class<*>>()
    inAppMessageBlacklist.add(SplashActivity::class.java)
    inAppMessageBlacklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlacklist))
  }
}
```

{% endtab %}
{% endtabs %}

See the [`BrazeActivityLifecycleCallbackListener`][83] constructor KDocs for more information.

[34]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[69]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html
[80]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html
[81]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory
[15]: http://fortawesome.github.io/Font-Awesome/
[27]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html
[28]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html
[50]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html
[51]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[52]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html
[83]: https://www.braze.com/customers
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[90]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[91]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[92]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[93]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
