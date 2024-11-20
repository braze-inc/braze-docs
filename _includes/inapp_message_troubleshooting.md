## Basic Checks

#### My in-app message wasn't shown for one user

1. Was the user in the segment at session start, when the SDK requests new in-app messages?
2. Was the user eligible or re-eligible to receive the in-app message per campaign targeting rules?
3. Was the user affected by a frequency cap?
4. Was the user in a control group? Check whether your campaign is configured is configured for AB Testing.
5. Was a different, higher priority in-app message displayed in place of the expected message?
6. Was my device in the correct orientation specified by the campaign?
7. Was my message suppressed by the default 30-second minimum time interval between triggers, enforced by the SDK?

#### My in-app message wasn't shown to all users on this platform

1. Is your campaign configured to target either Mobile Apps or Web Browsers as appropriate? As an example, if your campaign only targets Web Browsers, it will not send to Android devices.
2. Did you implement a custom UI, and is it working as intended? Is there other app-side custom handling or suppression that could be interfering with display? 
3. Has this particular platform and app version ever shown in-app messages successfully?
4. Did the trigger take place locally on the device? Note that a REST call can't be used to trigger an in-app message in the SDK.

#### My in-app message wasn't shown for all users

1. Was the Trigger Action set up properly in the dashboard, as well as in the app integration?
2. Was a different, higher priority in-app message displayed in place of the expected message?
3. Are you on a recent version of the SDK? Some in-app message types have SDK version requirements.
4. Have sessions been integrated properly in your integration? Are session analytics working for this app?

For more in-depth discussion of these scenarios, visit [the advanced troubleshooting section](#troubleshooting-in-app-advanced).

## Issues with Impressions and Click Analytics

{% if include.sdk == "iOS" %}
#### Impressions and Clicks aren't being logged

If you have set an in-app message delegate to manually handle message display or click actions, you must manually [log clicks](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) and [impressions](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) on the in-app message.
{% elsif include.sdk == "Android" %}
#### Impressions and Clicks aren't being logged
If you have set an in-app message delegate to manually handle message display or click actions, you must manually log clicks and impressions on the in-app message.
{% endif %}

#### Impressions are lower than expected

Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

## Advanced Troubleshooting {#troubleshooting-in-app-advanced}

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, confirm that the [in-app message was delivered to the device](#troubleshooting-in-app-message-delivery), then [troubleshoot message display](#troubleshooting-in-app-message-display).

### Troubleshooting in-app message delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to make sure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Troubleshoot messages not being returned

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


### Troubleshooting in-app message display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages, but they are not being shown, device-side logic may be preventing display:

{% if include.sdk == "iOS" %}
- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), which defaults to 30 seconds.
{% elsif include.sdk == "Android" %}
- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), which defaults to 30 seconds.
{% elsif include.sdk == "Web" %}
- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), which defaults to 30 seconds.
{% endif %}
- Failed image downloads will prevent in-app messages with images from displaying. Check your device logs to ensure that image downloads are not failing.
{% case include.sdk %}
  {% when "iOS", "Android" %}
- If you have set a delegate to customize in-app message handling, check your delegate to ensure it is not affecting the in-app message display.
  {% when "Web" %}
- If you have custom in-app message handling through `braze.subscribeToInAppMessage` or `appboy.subscribeToNewInAppMessages`, check that subscription to ensure it is not affecting in-app message display.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
- If the device orientation does not match the orientation specified by the in-app message, the in-app message will not display. Make sure that your device is in the correct orientation.
{% endcase %}