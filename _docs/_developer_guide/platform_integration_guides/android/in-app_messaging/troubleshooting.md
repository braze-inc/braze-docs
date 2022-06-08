---
nav_title: Troubleshooting
article_title: In-App Message Troubleshooting for Android and FireOS
page_order: 40
platform: 
  - Android
  - FireOS
description: "This reference article covers potential Android or FireOS in-app message troubleshooting topics."
channel:
  - in-app messages

---

# Troubleshooting

## Impressions

#### Impression or click analytics aren't being logged

If you have set an in-app message delegate to manually handle message display or click actions, you'll need to manually log clicks and impressions on the in-app message.

#### Impressions are lower than expected

Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

## Expected in-app message did not display

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, you should first ensure that the [in-app message was delivered to the device][troubleshooting_iams_11], then [troubleshoot message display][troubleshooting_iams_12].

## In-app message delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze's servers on session start. To check if in-app messages are being delivered to your device, you'll need to ensure that in-app messages are being both requested by the SDK and returned by Braze's servers.

### Check if messages are requested and returned

1. Add yourself as a [test user][troubleshooting_iams_1] on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs][troubleshooting_iams_3] to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs][troubleshooting_iams_3] to check if the correct in-app messages are being returned in the response data.<br>![][troubleshooting_iams_5]

#### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.][troubleshooting_iams_10]

### Troubleshoot messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue:

- Your segment does not contain your user.
  - Check your user's [**Engagement**][troubleshooting_iams_6] tab to see if the correct segment appears under **Segments**.
- Your user has previously received the in-app message and was not re-eligible to receive it again.
  - Check the [campaign re-eligibility settings][troubleshooting_iams_7] under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.
- Your user hit the frequency cap for the campaign.
  - Check the campaign [frequency cap settings][troubleshooting_iams_8] and ensure they align with your testing setup.
- If there was a control group on the campaign, your user may have fallen into the control group.
  - You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment.
  - When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.

## In-app message display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages, but they are not being shown, some device-side logic may be preventing display:

- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers][troubleshooting_iams_9], which defaults to 30 seconds.
- If you have set a delegate to customize in-app message handling, check your delegate to ensure it is not affecting the in-app message display.
- Failed image downloads will prevent in-app messages with images from displaying. Image downloads will always fail if the `BrazeInAppMessageManager` is not registered properly. Check your device logs to ensure that image downloads are not failing.
- If the device orientation does not match the orientation specified by the in-app message, the in-app message will not display. Make sure that your device is in the correct orientation.

[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_4]: #session-tracking
[troubleshooting_iams_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
[troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
[troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
[troubleshooting_iams_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
[troubleshooting_iams_11]: #troubleshooting-in-app-message-delivery
[troubleshooting_iams_12]: #troubleshooting-in-app-message-display
