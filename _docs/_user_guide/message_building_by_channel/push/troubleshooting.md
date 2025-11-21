---
nav_title: Troubleshooting
article_title: Troubleshooting Push
page_order: 23
page_type: reference
description: "This page contains troubleshooting steps for various issues relating to the Push messaging channel."
channel: push
---

# Troubleshooting Push

> Use this page to troubleshoot issues with the Push messaging channel.

## Missing push notifications

Experiencing delivery challenges with push notifications? There are a number of steps you can take to troubleshoot this issue by checking the:

- [Push subscription status](#push-subscription-status)
- [Segment](#segment)
- [Push notification caps](#push-notification-caps)
- [Rate limits](#rate-limits)
- [Control group status](#control-group-status)
- [Valid push token](#valid-push-token)
- [Push notification type](#push-notification-type)
- [Current app](#current-app)

#### Push subscription status

Pushes can only be sent to subscribed or opted-in users. Check your user profile in the [Engagement]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab in the **User Profile** section to confirm if you are actively registered for push for the workspace that you are testing. If you are registered for multiple apps, you will find them listed in the **Push Registered For** field:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

You can also export the user profiles using Braze export endpoints:
- [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Either endpoint will return a push token object that includes push enablement information per device.

#### Segment

Make sure you fall into the segment that you are targeting (if this is a live campaign and not a test). In the **User Profile**, you will see a list of segments that the user currently falls into. Remember this is an ever-changing variable as segmentation is updated in real time.

![List of Segments]({% image_buster /assets/img_archive/trouble2.png %})

You can also confirm that the user is part of the segment by using **User Lookup** when creating a segment.

![User Lookup section with a search field.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Push notification caps

Check the global frequency caps. It's possible you did not receive the push notification because your workspace has global frequency capping in place and you've already hit your push notification cap for the specified time frame.

You can do this by checking [global frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) in the dashboard. If the campaign is set to abide by frequency capping rules, there will be a number of users impacted by these settings

![Campaign Details]({% image_buster /assets/img_archive/trouble3.png %})

#### Rate limits

If you have a rate limit set for your campaign or Canvas, you might be falling out of receiving messaging due to exceeding this limit. For more information, refer to [Rate Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Control group status

If this is a single channel campaign or a Canvas with a control group, it's possible you are falling into the control group.

  1. Check the [variant distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) to see if there is a control group.
  2. If so, create a segment filtering for [in campaign control group]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) then [export the segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) and check if your user ID is on this list.

#### Valid push token
A push token is an identifier that senders use to target specific devices with a push notification. So, if the device does not have a valid push token, then there is no way to send a push notification to it. 

#### Push notification type

Check that you're using the correct type of push notification. For example, if you want to target a FireTV, then you would use a Kindle push notification, not an Android push campaign. Likewise, if you want to target an Android, use an Android push notification and not an iOS push campaign. Check out the following articles for more information on understanding the Braze workflow for:
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Current app

When testing push sends with internal users, make sure that the user who you want to receive the push notification is currently logged into the relevant app. This can lead to the user either not receiving a push or receiving a push you believe they aren't segmented for.

## Push clicks unexpectedly open in app

If you're experiencing issues with links in push notifications unexpectedly opening in your app instead of your web browser, there may be an issue with your campaign configuration or SDK implementation. Refer to these steps for help.

### Verify on-click behavior

In your campaign or Canvas step, double-check that **Open web URL inside mobile app** is not selected. If it is, clear the selection and relaunch. 

!["On-click behavior" field of configuring a push set to "Open web URL" with "Open web URL inside mobile app" unchecked.]({% image_buster /assets/img/push_on_click.png %})

The default interaction for the on-click behavior "Open web URL" differs by SDK version. For SDK versions iOS 2.29.0 and Android 2.0.0 and higher, this option is selected by default and web URLs will open in a web view within the app. Prior to these versions, this option is cleared by default and web URLs open in the device's default web browser.

If this is not the issue, there may be a problem with your push implementation. 

### Double-check push integration

If links in your push notifications are opening in the app unexpectedly, it might be due to issues with your push notification integration or customization settings. Follow these steps to troubleshoot:

1. **Review the push delegate implementation:** Ensure that the Braze push delegate is implemented correctly. For detailed instructions, refer to the integration guide for push notifications for your [platform]({{site.baseurl}}/developer_guide/home/).
2. **Inspect custom link handling:** Check if the app includes custom handling for all `https://` links. Custom configurations might override default behaviors. Collaborate with your development team to review and adjust these settings if necessary.
3. **Verify iOS push registration:** For iOS, revisit step 1 of the push integration guide on [registering push notifications with APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Ensure your delegate object is assigned synchronously before the app finishes launching. This step should be completed in the `application:didFinishLaunchingWithOptions:` method.
4. **Test your integration:** After making adjustments, test the push notification behavior on both iOS and Android devices to confirm the issue is resolved.

## Web push notifications aren't behaving as expected

If you're experiencing issues with push notifications in your browser, you may need to reset your site's notification permissions and clear your site's storage. Refer to these steps for help.

{% tabs %}
{% tab Chrome %}

### Reset Chrome on desktop

1. Next to your URL in the Chrome browser, select the **View Site Information** slider icon.
2. Under **Notifications**, select **Reset permission**.
3. Open Chrome DevTools. The following are the relevant shortcuts per operating system.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Keyboard shortcuts                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. In DevTools, navigate to the **Application** tab.
5. In the sidebar, select **Storage**.
6. Select **Clear site data**.
7. Chrome will prompt you to reload the page to apply your updated settings. Select **Reload**.

Your push permissions are now reset. Open a new tab to your site and try it out.

### Reset Chrome on Android

If you have a notification from your site visible in your Android notification drawer:

1. From the push notification, tap <i class="fas fa-cog" title="Settings"></i> and select **Site settings**.
2. From **Site settings**, tap **Clear & Reset**.

If you don't have a notification from your site open:

1. Open Chrome on Android.
2. Tap the <i class="fas fa-ellipsis-vertical"></i> menu.
3. Go to **Settings** > **Site Settings** > **Notifications**.
4. Verify notifications are set to **Ask before sending (recommended)**.
5. Find your site on the list.
6. Select the entry and tap **Clear and Reset**.

Your push permissions are now reset. Open a new tab to your site and try it out.

{% endtab %}
{% tab Firefox %}

### Reset Firefox on desktop

1. Next to your site URL, select <i class="fa-solid fa-circle-info" alt="info icon"></i> or <i class="fas fa-lock" alt="lock icon"></i>.
2. Under **Permissions**, next to **Receive Notifications**, select <i class="fa-solid fa-circle-xmark" title="Clear this permission and ask again"></i> to clear notification permissions.
3. On the same menu, select **Clear Cookies and Site Data**.
4. In the dialog to confirm your choice, select **OK**.

Your push permissions are now reset. Open a new tab to your site and try it out.

### Reset Firefox on Android

To reset push permissions on Android, refer to this [Mozilla support article](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Reset Safari on macOS

{% alert note %}
These steps are for macOS only, as Apple doesn't support Web Push for Safari on Windows.
{% endalert %}

1. Open Safari.
2. From the [menu bar on Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), go to **Safari** > **Settings** > **Websites** > **Notifications**.
3. Select your site from the list.
4. Select **Remove** to delete notification permissions for the site.
5. Then, go to **Privacy** > **Manage Website Data**.
6. Select your site from the list.
7. Select **Remove**, or to remove all site data, select **Remove All**.
8. Select **Done**.

Your push permissions are now reset. Open a new tab to your site and try it out.

{% endtab %}
{% endtabs %}

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

