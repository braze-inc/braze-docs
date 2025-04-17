{% multi_lang_include developer_guide/prerequisites/android.md %}

## Built-in features

The following features are built into the Braze Android SDK. To use any other push notification features, you will need to [set up push notifications](#android_setting-up-push-notifications) for your app.

|Feature|Description|
|-------|-----------|
|Push Stories|Android Push Stories are built into the Braze Android SDK by default. To learn more, see [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/).|
|Push Primers|Push primer campaigns encourage your users to enable push notifications on their device for your app. This can be done without SDK customization using our [no code push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Setting up push notifications

{% alert tip %}
To check out a sample app using FCM with the Braze Android SDK, see [Braze: Firebase Push Sample App](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).
{% endalert %}

### Rate limits

Firebase Cloud Messaging (FCM) API has a default rate limit of 600,000 requests per minute. If you reach this limit, Braze will automatically try again in a few minutes. To request an increase, contact [Firebase Support](https://firebase.google.com/support).

### Step 1: Add Firebase to your project

First, add Firebase to your Android project. For step-by-step instructions, see Google's [Firebase setup guide](https://firebase.google.com/docs/android/setup).

### Step 2: Add Cloud Messaging to your dependencies

Next, add the Cloud Messaging library to your project dependencies. In your Android project, open `build.gradle`, then add the following line to your `dependencies` block.

```gradle
implementation "google.firebase:firebase-messaging:+"
```

Your dependencies should look similar to the following:

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### Step 3: Enable the Firebase Cloud Messaging API

In Google Cloud, select the project your Android app is using, then enable the [Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![Enabled Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Step 4: Create a service account {#service-account}

Next, create a new service account, so Braze can make authorized API calls when registering FCM tokens. In Google Cloud, go to **Service Accounts**, then choose your project. On the **Service Accounts** page, select **Create Service Account**.

![A project's service account home page with "Create Service Account" highlighted.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Enter a service account name, ID, and description, then select **Create and continue**.

![The form for "Service account details."]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

In the **Role** field, find and select **Firebase Cloud Messaging API Admin** from the list of roles. For more restrictive access, create a [custom role](https://cloud.google.com/iam/docs/creating-custom-roles) with the `cloudmessaging.messages.create` permission, then choose it from the list instead. When you're finished, select **Done**.

{% alert warning %}
Be sure to select **Firebase Cloud Messaging _API_ Admin**, not **Firebase Cloud Messaging Admin**.
{% endalert %}

![The form for "Grant this service account access to project" with "Firebase Cloud Messaging API Admin" selected as the role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Step 5: Generate JSON credentials {#json}

Next, generate JSON credentials for your FCM service account. On Google Cloud IAM & Admin, go to **Service Accounts**, then choose your project. Locate the FCM service account [you created earlier](#android_service-account), then select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Manage Keys**.

![The project's service account homepage with the "Actions" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Select **Add Key** > **Create new key**.

![The selected service account with the "Add Key" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Choose **JSON**, then select **Create**. If you created your service account using a different Google Cloud project ID than your FCM project ID, you'll need to manually update the value assigned to the `project_id` in your JSON file.

Be sure to remember where you downloaded the key&#8212;you'll need it in the next step.

![The form for creating a private key with "JSON" selected.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Private keys could pose a security risk if compromised. Store your JSON credentials in a secure location for now&#8212;you'll delete your key after you upload it to Braze.
{% endalert %}

### Step 6: Upload your JSON credentials to Braze

Next, upload your JSON credentials to your Braze dashboard. In Braze, select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**.

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Under your Android app's **Push Notification Settings**, choose **Firebase**, then select **Upload JSON File** and upload the credentials [you generated earlier](#android_json). When you're finished, select **Save**.

![The form for "Push Notification Settings" with "Firebase" selected as the push provider.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Private keys could pose a security risk if compromised. Now that your key is uploaded to Braze, delete the file [you generated previously](#android_json).
{% endalert %}

### Step 7: Set up automatic token registration

When one of your users opt-in for push notifications, your app needs to generate an FCM token on their device before you can send them push notifications. With the Braze SDK, you can enable automatic FCM token registration for each user's device in your project's Braze configuration files.

First, go to Firebase Console, open your project, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Select **Cloud Messaging**, then under **Firebase Cloud Messaging API (V1)**, copy the number in the **Sender ID** field.

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Next, open your Android Studio project and use your Firebase Sender ID to enable automatic FCM token registration within your `braze.xml` or `BrazeConfig`.

{% tabs local %}
{% tab Braze.XML %}
To configure automatic FCM token registration, add the following lines to your `braze.xml` file:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

Replace `FIREBASE_SENDER_ID` with the value you copied from your Firebase project settings. Your `braze.xml` should look similar to the following:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string>
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}

{% tab BrazeConfig %}
To configure automatic FCM token registration, add the following lines to  your `BrazeConfig`:

{% subtabs local %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

Replace `FIREBASE_SENDER_ID` with the value you copied from your Firebase project settings. Your `BrazeConfig` should look similar to the following:

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
If you'd like manually register FCM tokens instead, you can call [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) inside your app's [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) method.
{% endalert %}
{% endtab %}
{% endtabs %}

### Step 8: Remove automatic requests in your application class

To prevent Braze from triggering unnecessary network requests every time you send silent push notifications, remove any automatic network requests configured in your `Application` class's `onCreate()` method. For more information see, [Android Developer Reference: Application](https://developer.android.com/reference/android/app/Application).

## Displaying notifications

### Step 1: Register Braze Firebase Messaging Service

You can either create a new, existing, or non-Braze Firebase Messaging Service. Choose whichever best meets your specific needs.

{% tabs local %}
{% tab New %}
Braze includes a service to handle push receipt and open intents. Our `BrazeFirebaseMessagingService` class will need to be registered in your `AndroidManifest.xml`:

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

Our notification code also uses `BrazeFirebaseMessagingService` to handle open and click action tracking. This service must be registered in the `AndroidManifest.xml` to function correctly. Also, remember that Braze prefixes notifications from our system with a unique key so that we only render notifications sent from our systems. You may register additional services separately to render notifications sent from other FCM services. See [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml) in the Firebase push sample app.

{% alert important %}
Before Braze SDK 3.1.1, `AppboyFcmReceiver` was used to handle FCM push. The `AppboyFcmReceiver` class should be removed from your manifest and replaced with the preceding integration.
{% endalert %}
{% endtab %}

{% tab Existing %}
If you already have a Firebase Messaging Service registered, you can pass [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) objects to Braze via [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html). This method will only display a notification if the [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) object originated from Braze and will safely ignore if not.

{% subtabs %}
{% subtab JAVA %}

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

{% endsubtab %}
{% subtab KOTLIN %}

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

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Non-Braze %}
If you have another Firebase Messaging Service you would also like to use, you can also specify a fallback Firebase Messaging Service to call if your application receives a push that isn't from Braze.

In your `braze.xml`, specify:

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

or set via [runtime configuration:]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 2: Conform small icons to design guidelines

For general information about Android notification icons, visit the [Notifications overview](https://developer.android.com/guide/topics/ui/notifiers/notifications).

Starting in Android N, you should update or remove small notification icon assets that involve color. The Android system (not the Braze SDK) ignores all non-alpha and transparency channels in action icons and the notification small icon. In other words, Android will convert all parts of your notification small icon to monochrome except for transparent regions.

To create a notification small icon asset that displays properly:
- Remove all colors from the image except for white.
- All other non-white regions of the asset should be transparent.

{% alert note %}
A common symptom of an improper asset is the small notification icon rendering as a solid monochrome square. This is due to the Android system not being able to find any transparent regions in the notification small icon asset.
{% endalert %}

The following large and small icons pictured are examples of properly designed icons:

![A small icon appearing in the bottom corner of a large icons beside a message that says "Hey I'm on my way to the bar but.."]({% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon")

### Step 3: Configure notification icons {#configure-icons}

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

This flag can also be set via [runtime configuration]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android):

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

If you want to custom handle deep links, you will need to create a push callback that listens for push received and opened intents from Braze. For more information, see [Using a callback for push events]({{site.baseurl}}/developer_guide/push_notifications/customization#android_using-a-callback-for-push-events).

#### Creating custom deep links

Follow the instructions found within the [Android developer documentation](http://developer.android.com/training/app-indexing/deep-linking.html) on deep linking if you have not already added deep links to your app. To learn more about what deep links are, see our [FAQ article]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

#### Adding deep links

The Braze dashboard supports setting deep links or web URLs in push notifications campaigns and Canvases that will be opened when the notification is clicked.

![The 'On Click Behavior' setting in the Braze dashboard with 'Deep Link Into Application' selected from the dropdown.]({% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action")

#### Customizing back stack behavior

The Android SDK, by default, will place your host app's main launcher activity in the back stack when following push deep links. Braze allows you to set a custom activity to open in the back stack in place of your main launcher activity or to disable the back stack altogether.

For example, to set an activity called `YourMainActivity` as the back stack activity using [runtime configuration]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android):

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

The Braze Android SDK supports [Android notification channels](https://developer.android.com/preview/features/notification-channels.html). If a Braze notification does not contain the ID for a notification channel or that a Braze notification contains an invalid channel ID, Braze will display the notification with the default notification channel defined in the SDK. Braze users use [Android Notification Channels]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) within the platform to group notifications.

To set the user facing name of the default Braze notification channel, use [`BrazeConfig.setDefaultNotificationChannelName()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html).

To set the user facing description of the default Braze notification channel, use [`BrazeConfig.setDefaultNotificationChannelDescription()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html).

Update any API campaigns with the [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) parameter to include the `notification_channel` field. If this field is not specified, Braze will send the notification payload with the [dashboard fallback]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel) channel ID.

Other than the default notification channel, Braze will not create any channels. All other channels must be programmatically defined by the host app and then entered into the Braze dashboard.

The default channel name and description can also be configured in `braze.xml`.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### Step 6: Test notification display and analytics

#### Testing display

At this point, you should be able to see notifications sent from Braze. To test this, go to the **Campaigns** page on your Braze dashboard and create a **Push Notification** campaign. Choose **Android Push** and design your message. Then click the eye icon in the composer to get the test sender. Enter the user ID or email address of your current user and click **Send Test**. You should see the push show up on your device.

![The 'Test' tab of a push notification campaign in the Braze dashboard.]({% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test")

For issues related to push display, see our [troubleshooting guide]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).

#### Testing analytics

At this point, you should also have analytics logging for push notification opens. Clicking on the notification when it arrives should result in the **Direct Opens** on your campaign results page to increase by 1. Check out our [push reporting]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) article for a break down on push analytics.

For issues related to push analytics, see our [troubleshooting guide]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).

#### Testing from command line

If you'd like to test in-app and push notifications via the command-line interface, you can send a single notification through the terminal via cURL and the [messaging API]({{site.baseurl}}/api/endpoints/messaging/). You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` (Go to **Settings** > **API Keys**.)
- `YOUR_EXTERNAL_USER_ID` (Search for a profile on the **Search Users** page.)
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

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

This example uses the `US-01` instance. If you are not on this instance, replace the `US-01` endpoint with [your endpoint]({{site.baseurl}}/api/basics/#endpoints).

## Conversation push notifications

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

The [people and conversations initiative](https://developer.android.com/guide/topics/ui/conversations) is a multi-year Android initiative that aims to elevate people and conversations in the system surfaces of the phone. This priority is based on the fact that communication and interaction with other people is still the most valued and important functional area for the majority of Android users across all demographics.

### Usage requirements

- This notification type requires the Braze Android SDK v15.0.0+ and Android 11+ devices. 
- Unsupported devices or SDKs will fallback to a standard push notification.

This feature is only available over the Braze REST API. See the [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object) for more information.

## FCM quota exceeded errors

When your limit for Firebase Cloud Messaging (FCM) is exceeded, Google returns "quota exceeded" errors. The default limit for FCM is 600,000 requests per minute. Braze retries sending according to Google's recommended best practices. However, a large volume of these errors can prolong sending time by several minutes. To mitigate potential impact, Braze will send you an alert that the rate limit is being exceeded and steps you can take to prevent the errors.

To check your current limit, go to your **Google Cloud Console** > **APIs & Services** > **Firebase Cloud Messaging API** > **Quotas & System Limits**, or visit the [FCM API Quotas page](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas).

### Best practices

We recommend these best practices to keep these error volumes low.

#### Request a rate limit increase from FCM

To request a rate limit increase from FCM, you can contact [Firebase Support](https://firebase.google.com/support) directly or do the following:

1. Go to the [FCM API Quotas page](https://console.cloud.google.com/apis/api/fcm.googleapis.com/quotas).
2. Locate the **Send requests per minute** quota.
3. Select **Edit Quota**. 
4. Enter a new value and submit your request.

#### Request global rate limiting via Braze

To apply a workspace-wide limit for Android push notifications, contact [Braze Support]({{site.baseurl}}/help/support#access-the-support-portal).