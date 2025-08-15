{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Using a callback for push events {#push-callback}

Braze provides a [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) callback for when push notifications are received, opened, or dismissed. It is recommended to place this callback in your `Application.onCreate()` in order to not miss any events occurring while your application is not running.

{% alert note %}
If previously using a Custom Broadcast Receiver for this functionality in your application, you can safely remove it in favor of this integration option.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
With notification action buttons, `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents fire when buttons with `opens app` or `deep link` actions are clicked. Deep link and extras handling remains the same. Buttons with `close` actions don't fire `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents and dismiss the notification automatically.
{% endalert %}

{% alert important %}
Create your push notification listener in `Application.onCreate` to ensure your listener is triggered after an end-user taps a notification while your app is in a terminated state.
{% endalert %}

## Customizing notification display {#customization-display}

### Step 1: Create your custom notification factory

In some scenarios, you may wish to customize push notifications in ways that would be cumbersome or unavailable server side. To give you complete control of notification display, we've added the ability to define your own [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) to create notification objects for display by Braze.

If a custom `IBrazeNotificationFactory` is set, Braze will call your factory's `createNotification()` method upon push receipt before the notification is displayed to the user. Braze will pass in a `Bundle` containing Braze push data and another `Bundle` containing custom key-value pairs sent either via the dashboard or the messaging APIs:

Braze will pass in a [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) containing data from the Braze push notification.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

You can return `null` from your custom `createNotification()` method to not show the notification at all, use `BrazeNotificationFactory.getInstance().createNotification()` to obtain our default `notification` object for that data and modify it before display, or generate a completely separate `notification` object for display.

{% alert note %}
For documentation on Braze push data keys, refer to the [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Step 2: Set your custom notification factory

To instruct Braze to use your custom notification factory, use the `setCustomBrazeNotificationFactory` method to set your [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

The recommended place to set your custom `IBrazeNotificationFactory` is in the `Application.onCreate()` application lifecycle method (not activity). This will allow the notification factory to be set correctly whenever your app process is active.

{% alert important %}
Creating your own notification from scratch is an advanced use case and should be done only with thorough testing and a deep understanding of the Braze push functionality. For example, you must make sure your notification logs push opens correctly.
{% endalert %}

To unset your custom [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) and return to default Braze handling for push, pass in `null` to our custom notification factory setter:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Rendering multicolor text

In Braze SDK version 3.1.1, HTML can be sent to a device to render multicolor text in push notifications.

![An Android push message "Multicolor Push test message" where the letters are different colors, italicized and given a background color.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

This example is rendered with the following HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Keep in mind that, Android limits which HTML elements and tags are valid in your push notifications. For example, `marquee` is not allowed.

{% alert important %}
Multicolor text rendering is device-specific and may not display based on Android device or version.
{% endalert %}

To render multicolor text in a push notification, you can update your `braze.xml` or `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Add the following in your `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Add the following in your [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Supported HTML tags

Currently, Google doesn't list their supported HTML tags for Android directly in their documentation&#8212;this information can only be found in their [Git repository's `Html.java` file](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Keep this in mind when referencing the following table, as this information was pulled from this file, and their supported HTML tags could be subject to change.

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>HTML Tag</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Basic Text Styling</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Bold text</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Italic text</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Underline text</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Strikethrough text</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Superscript text</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Subscript text</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Monospace text</td>
    </tr>
    <tr>
      <td rowspan="3">Size/Font</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Relative text size changes</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Sets foreground color</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (with inline CSS)</td>
      <td>Inline styles (e.g., color, background)</td>
    </tr>
    <tr>
      <td rowspan="4">Paragraph &amp; Block</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Block-level sections</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Line break</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Quoted block</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Unordered list with bullets</td>
    </tr>
    <tr>
      <td>Headings</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Headings (various sizes)</td>
    </tr>
    <tr>
      <td rowspan="2">Links &amp; Images</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Clickable link</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Inline image</td>
    </tr>
    <tr>
      <td>Other Inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonyms for italic or bold</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rendering inline images

### How it works

You can showcase a larger image within your Android push notification using inline image push. With this design, users won't have to manually expand the push to enlarge the image. Unlike regular Android push notifications, inline image push images are in a 3:2 aspect ratio.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibility

While you can send inline images to any device, devices and SDKs that don't meet the minimum versions will display a standard image instead. For inline images to display properly, both the Android Braze SDK v10.0.0+ and a device running Android M+ are required. The SDK must also be enabled for the image to render.

{% alert note %}
Devices running Android 12 will render differently due to changes in custom push notification styles.
{% endalert %}

### Sending an inline image push

When creating an Android push message, this feature is available in the **Notification Type** dropdown.

![The push campaign editor showing the location of the "Notification Type" dropdown (above the standard push preview).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Settings

There are many advanced settings available for Android push notifications sent through the Braze dashboard. This article will describe these features and how to use them successfully.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Notification ID {#notification-id}

A **Notification ID** is a unique identifier for a message category of your choosing that informs the messaging service to only respect the most recent message from that ID. Setting a notification ID allows you to send just the most recent and relevant message, rather than a stack of outdated, irrelevant ones.

### Firebase Messaging Delivery priority {#fcm-priority}

The [Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) field lets you control whether a push is sent with "normal" or "high" priority to Firebase Cloud Messaging.

### Time to live (TTL) {#ttl}

The **Time to Live** (TTL) field allows you to set a custom length of time to store messages with the push messaging service. The default values for time to live are four weeks for FCM and 31 days for ADM.

### Summary text {#summary-text}

The summary text allows you to set additional text in the expanded notification view. It also serves as a caption for notifications with images.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

The summary text will display under the body of the message in the expanded view. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. 

### Custom URIs {#custom-uri}

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep link inside your app and direct users to resources that exist outside of your app. This can be specified via the [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or our dashboard under **Advanced Settings** in the push composer as pictured:

![The deep linking advanced setting in the Braze push composer.]({% image_buster /assets/img_archive/deep_link.png %})

### Notification display priority {#notification-priority}

{% alert important %}
The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life, whereas high priority messages are always sent immediately.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for Android notifications is possible via the Braze dashboard and messaging API. 

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) *and* send the individual priority from the dashboard (to target &#60;O devices).

The priority levels that you can set on Android or Fire OS push notifications are:

| Priority | Description/Intended Use | `priority` value (for API messages) |
|----------|--------------------------|-------------------------------------|
| Max      | Urgent or time-critical messages | `2` |
| High     | Important communication, such as a new message from a friend | `1` |
| Default  | Most notifications - use if your message doesn't explicitly fall under any of the other priority types | `0` |
| Low      | Information that you want users to know about but does not require immediate action | `-1` |
| Min      | Contextual or background information. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's [Android notification](http://developer.android.com/design/patterns/notifications.html) documentation.

### Sounds {#sounds}

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (for example, `android.resource://com.mycompany.myapp/raw/mysound`). Specifying "default" in this field will play the default notification sound on the device. This can be specified via the [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or the dashboard under **Advanced Settings** in the push composer.

![The sound advanced setting in the Braze push composer.]({% image_buster /assets/img_archive/sound_android.png %})

Enter the full sound resource URI (for example, `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) *and* send the individual sound from the dashboard (to target &#60;O devices).
