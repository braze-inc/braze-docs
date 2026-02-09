---
nav_title: Push notifications
article_title: Push Notifications for Windows Universal
platform: Windows Universal
page_order: 1
description: "This article covers push notification integration instructions for the windows universal platform."
channel: push 
hidden: true
---

# Push notification integration
{% multi_lang_include archive/windows_deprecation.md %}

![An example windows universal push.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

A push notification is an out-of-app alert that appears on the user's screen when an important update occurs. Push notifications are a valuable way to provide your users with time-sensitive and relevant content or to re-engage them with your app.

Visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) for additional best practices.

## Step 1: Configure your application for push

Ensure that in your `Package.appxmanifest` file, the following settings are configured:

Within the **Application** tab, ensure that `Toast Capable` is set to `YES`.

## Step 2: Configure the Braze dashboard

1. [Find your SID and Client Secret](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Within the **Settings** page of the Braze dashboard, add the SID and Client Secret in your settings.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## Step 3: Update for background open logging

In your `OnLaunched` method, after you have called `OpenSession` add the following code snippet.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## Step 4: Creating event handlers

To listen to events that are fired when the push is received and activated (clicked by user), create event handlers and add them to the `PushManager` events:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Your event handlers should have the signatures:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Step 5: Deep linking from push into your app

### Part 1: Creating deep links for your app

Deep links are used to navigate users from outside your application directly to a certain screen or page in your application. Typically this is done by registering a URL scheme (for example, myapp://mypage) with an operating system and registering your application to handle that scheme; when the OS is asked to open a URL of that format it transfers control to your application.

WNS deep link support differs from this as it launches your application with data about where to send the user. When WNS push is created it can include a launch string that is passed through to your application's `OnLaunched` when the push is clicked and your application is opened. We already use this launch string to do campaign tracking, and we give users the ability to append their own data that can be parsed and used to navigate the user when the app is launched.

If you specify an extra launch string in the dashboard or the REST API, it will be added to the end of the launch string that we create, after the key "abextras=". So, an example launch string might look like `ab_cn_id=_trackingid_abextras=page=settings`, in which you specified `page=settings` in the extra launch string parameter so you can parse it and navigate the user to the settings page.

### Part 2: Deep linking through the dashboard

Specify the string to be appended to the launch string in the "Additional Launch String Configuration" field in push notification settings.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### Part 3: Deep linking through the REST API

Braze also allows sending deep links through the REST API. [Windows Universal push objects]({{site.baseurl}}/api/objects_filters/) accept an optional `extra_launch_string` parameter.

