---
nav_title: Huawei Integration
article_title: Huawei Push Integration for Android
platform: Android
page_order: 9
description: "This article covers how to set up a Huawei Android integration."
channel:
  - push

---

# Huawei integration

Newer phones manufactured by [Huawei][1] come equipped with Huawei Mobile Services (HMS) - a service used to deliver push instead of Google's Firebase Cloud Messaging (FCM).

This guide will show you how to set up your Huawei Android integration to send push through Braze and take advantage of all existing Braze features, including segmentation, analytics, Canvas, and more!

## Step 1: Register for a Huawei developer account

Before getting started, you'll need to register and set up a [Huawei Developer account][2]. In your Huawei account, go to **My Projects > Project Settings > App Information**, and take note of the `App ID` and `App secret`.

![][3]

## Step 2: Create a new Huawei app in the Braze dashboard

In the Braze dashboard, go to **Manage Settings**, listed under the **Settings** navigation.

Click **+ Add App**, provide a name (i.e., My Huawei App), select `Android` as the platform, and choose `Huawei (HMS)` as the push provider.

![][4]

Once your new Braze app has been created, you will find your app identifier API key and a section for **Push Notification Settings** where you can enter your `Huawei App ID` and `Huawei App Secret`.

![][12]

## Step 3: Integrate the Huawei messaging SDK into your app

Huawei has provided an [Android integration codelab][13] detailing integrating the Huawei Messaging Service into your application. Follow those steps to get started.

After completing the codelab, you will need to create a custom [Huawei Message Service][14] to obtain push tokens and forward messages to the Braze SDK.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).registerAppboyPushMessages(token);
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
    Braze.getInstance(applicationContext).registerAppboyPushMessages(token!!)
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

## Step 4: Send a Huawei push

At this point, you've created a new Huawei Android app in the Braze dashboard, configured it with your Huawei developer credentials, and have integrated the Braze and Huawei SDKs into your app.

Next, we can test out the integration by testing a new push campaign in Braze.

### Create a new push notification campaign

In the **Campaigns** page, create a new campaign, and choose **Push Notification** as your message type.

After you name your campaign, choose **Android Push** as the push platform.

![The campaign creation wizard displaying the available push platforms.][5]

Next, compose your push campaign with a title and message.

### Send a test push

In the **Test** tab, enter your user ID, which you've set in your app using the [`changeUser(USER_ID_STRING)` method][9], and click **Send Test** to send a test push.

![The test tab in the campaign creation wizard shows you can send a test message to yourself by providing your user ID and entering it into the "Add Individual Users" field.][7]

At this point, you should receive a test push notification on your Huawei (HMS) device from Braze.

### Setting up Huawei segmentation (optional)

Since your Huawei app in the Braze dashboard is built upon the Android push platform, you have the flexibility to send push to all Android users (Firebase Cloud Messaging and Huawei Mobile Services), or you can choose to segment your campaign audience to specific apps.

To send push to only Huawei apps, [create a new Segment][15] and select your Huawei App within the **Apps** section.

![][8]

Of course, if you want to send the same push to all Android push providers, you can choose not to specify the app which will send to all Android apps configured within the current App Group.

## Analytics

Once your campaign has been launched, you will see analytics for your campaign or Canvas aggregated for Android push. See our [push user guide][10] for more information on Android push analytics and settings.

[1]: https://huaweimobileservices.com/
[2]: https://developer.huawei.com/consumer/en/console
[3]: {% image_buster /assets/img/huawei/huawei-credentials.png %}
[4]: {% image_buster /assets/img/huawei/huawei-create-app.png %}
[5]: {% image_buster /assets/img/huawei/huawei-test-push-platforms.png %}
[6]: {% image_buster /assets/img/huawei/huawei-test-push-composer.png %}
[7]: {% image_buster /assets/img/huawei/huawei-test-send.png %}
[8]: {% image_buster /assets/img/huawei/huawei-segmentation.png %}
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/
[12]: {% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %}
[13]: https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html
[14]: https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls
[15]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform
