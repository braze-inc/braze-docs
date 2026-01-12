---
nav_title: Troubleshooting
article_title: In-App Messaging Troubleshooting for iOS
platform: iOS
page_order: 7
description: "This reference article covers potential iOS in-app message troubleshooting topics."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Troubleshoot in-app messages

## Impressions

#### Impression or click analytics aren't being logged

If you have set an in-app message delegate to manually handle message display or click actions, you'll need to manually log clicks and impressions on the in-app message.

#### Impressions are lower than expected

Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

## Expected in-app message did not display

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, you should first ensure that the [in-app message was delivered to the device](#troubleshooting-in-app-message-delivery), then [troubleshoot message display](#troubleshooting-in-app-message-display).

### In-app message delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to ensure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Troubleshoot messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue:

- Your segment does not contain your user.
  - Check your user's [**Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab to see if the correct segment appears under **Segments**.
- Your user has previously received the in-app message and was not re-eligible to receive it again.
  - Check the [campaign re-eligibility settings]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.
- Your user hit the frequency cap for the campaign.
  - Check the campaign [frequency cap settings]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and ensure they align with your testing setup.
- If there was a control group on the campaign, your user may have fallen into the control group.
  - You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment.
  - When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.

### In-app message display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages but they are not being shown, some device-side logic may be preventing display:

- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), which defaults to 30 seconds.
- If you have set a delegate to customize in-app message handling, check your delegate to ensure it is not affecting in-app message display.
- Failed image downloads will prevent in-app messages with images from displaying. Image downloads will always fail if the `SDWebImage` framework is not integrated properly. Check your device logs to ensure that image downloads are not failing.
- If the device orientation did not match the orientation specified by the in-app message, the in-app message will not display. Make sure that your device is in the correct orientation.


