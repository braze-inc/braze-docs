---
nav_title: Standard Integration
article_title: Standard Push Notification Integration for Android
platform: Android
page_order: 0
description: "This article covers how to integrate push notifications in your Android application."
channel:
  - push
search_rank: 3
---

# Standard Android push integration

> This article covers how to integrate push notifications in your Android application.

![Android inline image push example]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

Braze sends push notifications to Android devices using [Firebase Cloud Messaging (FCM)][45].

Check out our [help documentation][8] for push best practices.

## Registering for push 

Use [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) to register for push. For a full sample of using Firebase with the Braze Android SDK, see our [Firebase push sample app](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

### Step 1: Enable Firebase

To get started, follow the [Firebase instructions][49] on adding Firebase to your Android project.

Next, add the Firebase messaging dependency to your module's `build.gradle`:

```gradle
implementation "com.google.firebase:firebase-messaging:${FIREBASE_PUSH_MESSAGING_VERSION}"
```

### Step 2: Configure token registration

Braze push notifications won't work until a Firebase Cloud Messaging token (FCM registration token) is registered. FCM registration tokens can either be registered by the Braze SDK **automatically** (recommended) or **manually** registered. Tokens can be manually registered using the [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) method.

Make sure to use your Firebase Sender ID. This is a unique numerical value created when you create your Firebase project, available in the **Cloud Messaging** tab of the Firebase console **Settings** pane. The sender ID is used to identify each sender that can send messages to the client app.

{% tabs local %}
{% tab Automatic registration (recommended) %}

To automatically register FCM registration tokens, enable automatic Firebase registration and set a Firebase Cloud Messaging sender ID.

In your `braze.xml`:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">your_fcm_sender_id_here</string>
```

Or in your [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("YOUR FIREBASE SENDER ID HERE")
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsFirebaseCloudMessagingRegistrationEnabled(true)
    .setFirebaseCloudMessagingSenderIdKey("YOUR FIREBASE SENDER ID HERE")
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Manual registration %}

To manually register your tokens, we recommended you call [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) from within your application [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) method to ensure that push tokens are reliably delivered to Braze.

{% subtabs local %}
{% subtab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    final Context applicationContext = this;
    FirebaseMessaging.getInstance().getToken().addOnCompleteListener(task -> {
      if (!task.isSuccessful()) {
        Log.w(TAG, "Exception while registering FCM token with Braze.", task.getException());
        return;
      }

      final String token = task.getResult();
      Braze.getInstance(applicationContext).setRegisteredPushToken(token);
    });
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
class MyApplication: Application() {
  override fun onCreate() {
    super.onCreate()
    FirebaseMessaging.getInstance().token.addOnCompleteListener { task: Task<String?> ->
      if (!task.isSuccessful) {
        Log.w(TAG, "Exception while registering FCM token with Braze.", task.exception)
        return@addOnCompleteListener
      }
      val token = task.result
      Braze.getInstance(applicationContext).setRegisteredPushToken(token)
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}

While we strongly recommend registering your FCM registration token in your application `onCreate()`, the token can be registered anywhere in your code.

{% endtab %}
{% endtabs %}

### Step 3: Migrate from GCM (Optional)

If you are migrating from using GCM to using Firebase with Braze, visit the [GCM migration guide][48] for instructions on switching to using Firebase in your app.

### Step 4: Set Your Firebase credentials

{% alert warning %}
The **Legacy** Cloud Messaging API server key is required to configure Android Push in Braze. Using the Firebase Cloud Messaging API (V1) credentials will not allow you to send push notifications.
{% endalert %}

First, you must locate your Cloud Messaging API server key and sender ID in the [Firebase developers console][58]. Select your Firebase project, go to **Settings > Cloud Messaging**, and copy the **Cloud Messaging API (Legacy) Server Key** and **Sender ID**:

![The Firebase platform under "Settings" and then "Cloud Messaging" will display your server ID and server key.][80]

{% alert note %}
If Cloud Messaging API is disabled, click on the three dots to enable the API in Google Cloud Console, then refresh the **Project settings** page.
{% endalert %}
![The Cloud Messaging API can be enabled by clicking on the three dots on the right.][79]

Input your Cloud Messaging API (Legacy) server key and sender ID into the Braze dashboard:

1. Go to **Settings** > **App Settings** and select your Android app.
2. Enter your Cloud Messaging API (Legacy) server key in the **Firebase Cloud Messaging Server Key** field, under the push notification settings section.
3. Enter your Cloud Messaging API (Legacy) sender ID in the **Firebase Cloud Messaging Sender ID** field, under the push notification settings section.

![][16]

### Step 5: Remove old permissions

Braze no longer requires the following permissions if using Firebase:

  ```xml
  <uses-permission android:name="android.permission.GET_ACCOUNTS" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
  <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
  <permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" android:protectionLevel="signature"/>
  <uses-permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" />
  ```

### Step 6: Remove automatic actions from your application class

If you have a custom [application][76] subclass, ensure you do not have automatic logic that pings your servers in your class's `Application.onCreate()` lifecycle method. This will ensure that silent push notifications from Braze don't cause unnecessary requests to your servers.

## Receiving and displaying push {#displaying-push}

After completing this section, you should be able to receive and display push notifications sent by Braze.

### Step 1: Register Braze Firebase Messaging Service

{% alert warning %}
If you already have a Firebase Messaging Service registered, do not complete this step. Instead, proceed to [Using your own Firebase Messaging Service](#using-your-own-firebase-messaging-service) and complete the steps listed there.
{% endalert %}

Braze includes a service to handle push receipt and open intents. Our `BrazeFirebaseMessagingService` class will need to be registered in your `AndroidManifest.xml`:

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

Braze's notification code also uses `BrazeFirebaseMessagingService` to handle open and click action tracking. This service must be registered in the `AndroidManifest.xml` to function correctly. Also, remember that Braze prefixes notifications from our system with a unique key to ensure we only render notifications sent from Braze's systems. You may register additional services separately to render notifications sent from other FCM services. See [`AndroidManifest.xml`][70] in the Firebase push sample app.

{% alert important %}
Before Braze SDK 3.1.1, `AppboyFcmReceiver` was used to handle FCM push. The `AppboyFcmReceiver` class should be removed from your manifest and replaced with the preceding integration.
{% endalert %}

##### Using your own Firebase Messaging Service

If you already have a Firebase Messaging Service registered, you can pass [`RemoteMessage`][75] objects to Braze via [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`][74]. This method will only display a notification if the [`RemoteMessage`][75] object originated from Braze and will safely ignore if not.

{% tabs %}
{% tab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Step 2: Ensure small icons conform to design guidelines

For general information about Android notification icons, visit the [Notifications overview][37].

Starting in Android N, you should update or remove small notification icon assets that involve color. The Android system (not the Braze SDK) ignores all non-alpha and transparency channels in action icons and the notification small icon. In other words, Android will convert all parts of your notification small icon to monochrome except for transparent regions.

To properly create a notification small icon asset:
- Remove all colors from the image except for white.
- All other non-white regions of the asset should be transparent.

{% alert note %}
A common symptom of an improper asset is the small notification icon rendering as a solid monochrome square. This is due to the Android system not being able to find any transparent regions in the notification small icon asset.
{% endalert %}

The following large and small icons pictured are examples of properly designed icons:

![A small icon appearing in the bottom corner of a large icons beside a message that says "Hey I'm on my way to the bar but.."][38]

### Step 3: Configure notification icons

#### Specifying icons in braze.xml

Braze allows you to configure your notification icons by specifying drawable resources in your `braze.xml`:

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

Setting a small notification icon is required. **If you do not set one, Braze will default to using the application icon as the small notification icon, which may look suboptimal.**

Setting a large notification icon is optional but recommended.

#### Specifying icon accent color

The notification icon accent color can be overridden in your `braze.xml`. If the color is not specified, the default color is the same gray Lollipop uses for system notifications.

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

You may also optionally use a color reference:

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### Step 4: Add deep links

#### Enabling automatic deep link opening

To enable Braze to automatically open your app and any deep links when a push notification is clicked, set `com_braze_handle_push_deep_links_automatically` to `true`, in your `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

This flag can also be set via [runtime configuration][65]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

If you would like to custom handle deep links, you will need to create a push callback that listens for push received and opened intents from Braze. See our [Custom handling push receipts and opens][52] article for more information.

#### Creating custom deep links

Follow the instructions found within the [Android developer documentation][40] on deep linking if you have not already added deep links to your app. To learn more about what deep links are, see our [FAQ article][42].

#### Adding deep links

The Braze dashboard supports setting deep links or web URLs in push notifications campaigns and Canvases that will be opened when the notification is clicked.

![][41]

#### Customizing back stack behavior

The Android SDK, by default, will place your host app's main launcher activity in the back stack when following push deep links. Braze allows you to set a custom activity to open in the back stack in place of your main launcher activity or to disable the back stack altogether.

For example, to set an activity called `YourMainActivity` as the back stack activity using [runtime configuration][65]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

See the equivalent configuration for your `braze.xml`. Note that the class name must be the same as returned by `Class.forName()`.

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### Step 5: Define notification channels

The Braze Android SDK supports [Android notification channels][62]. If a Braze notification does not contain the ID for a notification channel or that a Braze notification contains an invalid channel ID, Braze will display the notification with the default notification channel defined in the SDK. Braze users use [Android Notification Channels][61] within the platform to group notifications.

To set the user facing name of the default Braze notification channel, use [`BrazeConfig.setDefaultNotificationChannelName()`][72].

To set the user facing description of the default Braze notification channel, use [`BrazeConfig.setDefaultNotificationChannelDescription()`][73].

You should ensure that any API campaigns with the [Android push object][63] parameter are updated to include the `notification_channel` field. If this field is not specified, Braze will send the notification payload with the [dashboard fallback][64] channel ID.

Other than the default notification channel, Braze will not create any channels. All other channels must be programmatically defined by the host app and then entered into the Braze dashboard.

The default channel name and description can also be configured in `braze.xml`.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### Step 6: Test notification display and analytics

#### Testing display

At this point, you should be able to see notifications sent from Braze. To test this, go to the **Campaigns** page on your Braze dashboard and create a **Push Notification** campaign. Choose **Android Push** and design your message. Then click the eye icon in the composer to get the test sender. Enter the user ID or email address of your current user and click **Send Test**. You should see the push show up on your device.

![][55]

For issues related to push display, see our [troubleshooting guide][57].

#### Testing analytics

At this point, you should also have analytics logging for push notification opens. Clicking on the notification when it arrives should result in the **Direct Opens** on your campaign results page to increase by 1. Check out our [push reporting]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) article for a break down on push analytics.

For issues related to push analytics, see our [troubleshooting guide][57].

#### Testing from command line

If you'd like to test in-app and push notifications via the command-line, you can send a single notification through the terminal via cURL and the [messaging API][22]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available at **Settings** > **API Keys**
- `YOUR_EXTERNAL_USER_ID` - available by searching for a profile on the **Search Users** page
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), these pages are in a different location: <br>- **API Keys** is located at **Developer Console** > **API Settings** <br>- **Search Users** is located at **Users** > **User Search**
{% endalert %}

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

This example uses the `US-01` instance. If you are not on this instance, replace the `US-01` endpoint with [your endpoint][66].

## Customizing your integration

### Custom displaying notifications

#### Step 1: Create your custom notification factory

In some scenarios, you may wish to customize push notifications in ways that would be cumbersome or unavailable server side. To give you complete control of notification display, we've added the ability to define your own [`IBrazeNotificationFactory`][6] to create notification objects for display by Braze.

If a custom `IBrazeNotificationFactory` is set, Braze will call your factory's `createNotification()` method upon push receipt before the notification is displayed to the user. Braze will pass in a `Bundle` containing Braze push data and another `Bundle` containing custom key-value pairs sent either via the dashboard or the messaging APIs:

Braze will pass in a [`BrazeNotificationPayload`][77] containing data from the Braze push notification.

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

You can return `null` from your custom `createNotification()` method to not show the notification at all, use `BrazeNotificationFactory.getInstance().createNotification()` to obtain Braze's default `notification` object for that data and modify it before display, or generate a completely separate `notification` object for display.

{% alert note %}
For documentation on Braze push data keys, refer to the [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

#### Step 2: Set your custom notification factory

To instruct Braze to use your custom notification factory, use the `setCustomBrazeNotificationFactory` method to set your [`IBrazeNotificationFactory`][6]:

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
Creating your own notification from scratch is an advanced use case and should be done only with thorough testing and a deep understanding of Braze's push functionality. For example, you must ensure your notification logs push opens correctly.
{% endalert %}

To unset your custom [`IBrazeNotificationFactory`][6] and return to default Braze handling for push, pass in `null` to our custom notification factory setter:

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

## Push primers

Push primer campaigns encourage your users to enable push notifications on their device for your app. This can be done without SDK customization using our [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[16]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[22]: {{site.baseurl}}/api/endpoints/messaging/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/
[37]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[38]: {% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon"
[40]: http://developer.android.com/training/app-indexing/deep-linking.html "Google Deep Linking Documentation"
[41]: {% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action"
[42]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[45]: https://firebase.google.com/docs/cloud-messaging/
[48]: https://developers.google.com/cloud-messaging/android/android-migrate-fcm
[49]: https://firebase.google.com/docs/android/setup
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[55]: {% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test"
[56]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[57]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
[61]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/
[62]: https://developer.android.com/preview/features/notification-channels.html
[63]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[64]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[67]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
[70]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "AndroidManifest.xml"
[72]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html
[73]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html
[74]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html
[75]: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[76]: https://developer.android.com/reference/android/app/Application
[77]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html
[78]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html
[79]: {% image_buster /assets/img_archive/cloud_messaging_legacy_disabled.png %} "Firebase Legacy Disabled"
[80]: {% image_buster /assets/img_archive/cloud_messaging_legacy_enabled.png %} "Firebase Server Key"
