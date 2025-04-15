{% multi_lang_include developer_guide/prerequisites/android.md %}

## Setting up push notifications

Newer phones manufactured by [Huawei](https://huaweimobileservices.com/) come equipped with Huawei Mobile Services (HMS) - a service used to deliver push instead of Google's Firebase Cloud Messaging (FCM).

### Step 1: Register for a Huawei developer account

Before getting started, you'll need to register and set up a [Huawei Developer account](https://developer.huawei.com/consumer/en/console). In your Huawei account, go to **My Projects > Project Settings > App Information**, and take note of the `App ID` and `App secret`.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Step 2: Create a new Huawei app in the Braze dashboard

In the Braze dashboard, go to **App Settings**, listed under the **Settings** navigation.

Click **+ Add App**, provide a name (such as My Huawei App), select `Android` as the platform.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Once your new Braze app has been created, locate the push notification settings and select `Huawei` as the push provider. Next, provide your `Huawei Client Secret` and `Huawei App ID`.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Step 3: Integrate the Huawei messaging SDK into your app

Huawei has provided an [Android integration codelab](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) detailing integrating the Huawei Messaging Service into your application. Follow those steps to get started.

After completing the codelab, you will need to create a custom [Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) to obtain push tokens and forward messages to the Braze SDK.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

After adding your custom push service, add the following to your `AndroidManifest.xml`:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Step 4: Test your push notifications (optional)

At this point, you've created a new Huawei Android app in the Braze dashboard, configured it with your Huawei developer credentials, and have integrated the Braze and Huawei SDKs into your app.

Next, we can test out the integration by testing a new push campaign in Braze.

#### Step 4.1: Create a new push notification campaign

In the **Campaigns** page, create a new campaign, and choose **Push Notification** as your message type.

After you name your campaign, choose **Android Push** as the push platform.

![The campaign creation composer displaying the available push platforms.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Next, compose your push campaign with a title and message.

#### Step 4.2: Send a test push

In the **Test** tab, enter your user ID, which you've set in your app using the [`changeUser(USER_ID_STRING)` method]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id), and click **Send Test** to send a test push.

![The test tab in the campaign creation composer shows you can send a test message to yourself by providing your user ID and entering it into the "Add Individual Users" field.]({% image_buster /assets/img/huawei/huawei-test-send.png %})

At this point, you should receive a test push notification on your Huawei (HMS) device from Braze.

#### Step 4.3: Set up Huawei segmentation (optional)

Since your Huawei app in the Braze dashboard is built upon the Android push platform, you have the flexibility to send push to all Android users (Firebase Cloud Messaging and Huawei Mobile Services), or you can choose to segment your campaign audience to specific apps.

To send push to only Huawei apps, [create a new Segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) and select your Huawei App within the **Apps** section.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Of course, if you want to send the same push to all Android push providers, you can choose not to specify the app which will send to all Android apps configured within the current workspace.
