---
nav_title: Huawei Integration
platform: Android
page_order: 1

---
# Huawei Integration

Newer phones manufactured by [Huawei][1] come equipped with Huawei Mobile Services (HMS) - a service used to deliver push _instead of_ Google's Firebase Cloud Messaging (FCM).

This guide will show you how to set up your Huawei Android integration in order to send push through Braze, and take advantage of all existing Braze features, including segmentation, analytics, canvas, and more!

## 1. Register for a Huawei Developer Account

Before getting started, you'll need to register and set up a [Huawei Developer account][2].

In your Huawei account, go to `My Projects` > `Project Settings` > `App Information`, and take note of the `App ID` and `App secret`.

![Huawei App Credentials][3]

In the next step, you will enter these credentials in the Braze Dashboard which will let Braze send push on behalf of your Huawei app.

## 2. Create a new Huawei App in the Braze Dashboard

In the Braze Dashboard, go to `Manage App Group` listed under the `App Settings` navigation.

Add a new App, provide a name (i.e. My Huawei App), select `Android` as the Platform, and choose `Huawei (HMS)` as the Push Provider.

Once your new Braze App has been created, you will be shown an `API Key`, and a section for Push Notification Settings where you will enter your Huawei credentials from the previous step.

![Create Huawei App in Braze Dashboard][4]

## 3. Enter Huawei Credentials in the Braze Dashboard

Using the credentials from your Huawei Developer account, enter the `Huawei App ID` and `Huawei App Secret` within your newly created Huawei Braze App. When you're done, save your changes.

![Huawei Dashboard Credentials][12]

## 4. Integrate the Braze Android SDK into your App

_hocus pocus julian's focus_

## 5. Sending Huawei Push

At this point, you've created a new Huawei Android app in the Braze Dashboard, configured it with your Huawei Developer credentials, and have integrated the Braze SDK into your app.

Next, we can test out the integration by testing out a new Push campaign in Braze.

### Create a new Push Notification Campaign

In the Campaigns menu, create a new campaign, and choose Push Notification.

After you name your campaign, choose `Android Push` as the Push Platform.

![Choose Android Push Channel][5]

Next, compose your push campaign with a Title and Message.

![Compose Android Huawei Push Message][6]

### Send a Test Push

In the Test tab, enter your user ID which you've set in your app using the [`changeUser(USER_ID_STRING)` method][9], and click to send the test push.

![Huawei Test Send][7]

At this point, you should receive a test push notification on your Huawei (HMS) device from Braze!

### Setting up Huawei Segmentation

Since your Huawei App in the Braze dashboard is built upon the Android Push platform, you have the flexibility to send push to all android users (Firebase Cloud Messaging and Huawei Mobile Services), or you can choose to segment your campaign audience to specific apps.

To segment your campaign, you can use the `Has App` filter to specify which of your Android apps should receive the message.

![Huawei Segmentation][8]

Of course, if you want to send the same push to all Android devices, you can choose to not specify the app which will send to all Android apps configured within the current App Group.

### Analytics

Once you campaign has been launched, you will see analytics for your campaign or canvas aggregated for Android Push. For more information on Android Push analytics and settings, see our our [User Guide for Push][10].


[1]: https://huaweimobileservices.com/
[2]: https://developer.huawei.com/consumer/en/console
[3]: {% image_buster /assets/img/huawei/huawei-credentials.png %}
[4]: {% image_buster /assets/img/huawei/huawei-create-app.png %}
[5]: {% image_buster /assets/img/huawei/huawei-test-push-platforms.png %}
[6]: {% image_buster /assets/img/huawei/huawei-test-push-composer.png %}
[7]: {% image_buster /assets/img/huawei/huawei-test-send.png %}
[8]: {% image_buster /assets/img/huawei/huawei-segmentation.png %}
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#results-data-push
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/
[12]: {% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %}