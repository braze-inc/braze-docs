{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Setting up push notifications

{% tabs %}
{% tab android %}
{% alert tip %}
To see how namespaces change between Java and C#, check out our [Xample sample app on GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp).
{% endalert %}

To integrate push notifications for .NET MAUI (formerly Xamarin), you'll need to complete the steps for native Android push notifications. The following steps are only a summary. For a full walkthrough, see the [native push notification guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).

### Step 1: Update your project

1. Add Firebase to your Android project.
2. Add the Cloud Messaging library to your Android project's `build.gradle`:
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### Step 2: Create your JSON credentials

1. In Google Cloud, enable the [Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com).
2. Select **Service Accounts** > your project > **Create Service Account**, then enter a service account name, ID, and description. When you're finished, select **Create and continue**.
3. In the **Role** field, find and select **Firebase Cloud Messaging API Admin** from the list of roles.
4. In **Service Accounts**, choose your project, then select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Manage Keys** > **Add Key** > **Create new key**. Choose **JSON**, then select **Create**.

### Step 3: Upload your JSON credentials

1. In Braze, select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**. Under your Android app's **Push Notification Settings**, choose **Firebase**, then select **Upload JSON File** and upload the credentials you generated earlier. When you're finished, select **Save**.
2. Enable automatic FCM token registration, by going to Firebase Console. Open your project, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**. Select **Cloud Messaging**, then under **Firebase Cloud Messaging API (V1)**, copy the number in the **Sender ID** field.
3. In your Android Studio project and the following to your `braze.xml`.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
To prevent Braze from triggering unnecessary network requests every time you send silent push notifications, remove any automatic network requests configured in your `Application` class's `onCreate()` method. For more information see, [Android Developer Reference: Application](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### Step 1: Complete the initial setup

See the [Swift integration instructions]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) for information about setting up your application with push and storing your credentials on our server. Refer to the [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) sample application for more details.

### Step 2: Request push notifications permission

Our .NET MAUI SDK now supports automatic push set up. Set up push automation and permissions by adding the following code to your Braze instance configuration:

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

Refer to the [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) sample application for more details. For more details, see the Xamarin documentation for [Enhanced User Notifications in Xamarin.iOS](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos).
{% endtab %}
{% endtabs %}
