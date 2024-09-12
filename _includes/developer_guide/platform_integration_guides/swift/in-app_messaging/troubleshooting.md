---
nav_title: Troubleshooting
article_title: Troubleshooting In-App Messaging for iOS
platform: Swift
page_order: 6
description: "This reference article covers potential iOS in-app message troubleshooting topics for the Swift SDK."
channel:
  - in-app messages

---

# Troubleshooting

> This reference article covers potential iOS in-app message troubleshooting topics.

## Impressions

### Impression or click analytics aren't being logged

If you have set an in-app message delegate to manually handle message display or click actions, you'll need to manually [log clicks](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) and [impressions](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) on the in-app message.

### Impressions are lower than expected

Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

## Expected in-app message did not display

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, you should first ensure that the [in-app message was delivered to the device](#troubleshooting-in-app-message-delivery), then [troubleshoot message display](#troubleshooting-in-app-message-display).

### Troubleshooting in-app message delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to ensure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

#### Messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue.

##### Your segment does not contain your user
Check your user's [**Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/user_profiles/#engagement-tab) tab to see if the correct segment appears under **Segments**.

##### Your user has previously received the in-app message and was not re-eligible to receive it again
Check the [campaign re-eligibility settings]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.

##### Your user hit the frequency cap for the campaign
Check the campaign [frequency cap settings]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and ensure they align with your testing setup.

##### User fallen out of the control group
If there was a control group on the campaign, your user may have fallen into the control group. You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment. 

When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.

### Troubleshooting in-app message display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages but they are not being shown, some device-side logic may be preventing display:

- Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), which defaults to 30 seconds.
- If you have set a delegate to customize in-app message handling, check your delegate to ensure it is not affecting in-app message display.
- Failed image downloads will prevent in-app messages with images from displaying. Check your device logs to ensure that image downloads are not failing.
- If the device orientation did not match the orientation specified by the in-app message, the in-app message will not display. Make sure that your device is in the correct orientation.

### Troubleshooting asset loading (`NSURLError` code `-1008`)

When integrating Braze alongside third-party network logging libraries, developers can commonly run into an `NSURLError` with the domain code `-1008`. This error indicates that assets like images and fonts could not be retrieved or failed to cache. To work around such cases, you will need to register Braze's CDN URLs to the list of domains that should be ignored by these libraries.

#### Domains

The full list of CDN domains is as listed below:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Examples

Below are libraries that are known to conflict with Braze's asset caching, along with example code to work around the issue. If your project uses a library that causes an unavailable resource error and is not listed below, consult the documentation of that library for similar usage APIs.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### NetGuard

{% tabs %}
{% tab Swift %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNLogger

{% tabs %}
{% tab Swift %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


