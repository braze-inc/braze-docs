---
nav_title: In-App Messages Not Displaying
article_title: In-App Messages Not Displaying
page_order: 1

page_type: solution
description: "This help article walks you through troubleshooting issues with in-app messages not displaying or rendering properly."
channel: in-app messages
---

# In-app messages not displaying

If you find that your in-app messages are not displaying or rendering properly, there are a number of approaches to check:

* [Event triggers](#event-triggers)
* [Message impressions](#message-impressions)
* [Tests](#run-tests)
* [Session timeout](#session-timeout)
* [Messaging interval](#minimum-interval)

## Event triggers

If the campaign is triggered by a session start or a custom event, you want to ensure that this event or session is happening frequently enough to trigger the message. Check this data on the [Overview][1] (for session data) or [Custom Events][2] pages:

![Custom Events page showing a graph for the number of times the custom event Added to Favorites occurred over a one month period][14]

## Message impressions

Customization of the in-app message UI or delivery mechanisms within the SDK may require your developers to utilize our methods to manually log in-app message impressions. Check with your developers to see if you use in-app message customization.

## Run tests

It is important to determine whether the trigger event is failing to occur, or the message itself is unable to display. To test, trigger the message using a different action (like a session start or different custom event) and verify whether it displays. This will help isolate if this is potentially a data issue.

Alternatively try using a different type of in-app message template or size of image. There are [specifications for in-app messages][15] that must be followed. Sometimes, if an image is too large, it will prevent the in-app message from displaying.

## Session timeout

Find out if you have customized your session timeout. By default, Braze retrieves in-app messages at the start of a session from the server.

If you have an extended the session timeout it will extended the period of time from which we can refresh the potential in-app messages you are eligible for. Additionally, if your campaign is set to trigger off of a session start, you’ll need to make sure the appropriate amount of time has passed for a new session to be registered. For example, the session timeout may have been customized to be 30 seconds. If you open and close the app in less than 30 seconds you will not be eligible to receive another in-app message triggered on session start. 

Learn more about customizing session timeouts for the following platforms:
* [iOS][16]
* [Android][17]
* [Web][18]

## Minimum interval

There is a minimum interval at which we’ll allow in-app messages to be consecutively triggered, so you might be trying to trigger them too quickly. Learn more about the minimum interval for the following platforms: 
* [iOS][19]
* [Android][20]
* [Web][21]

While intervals are customizable, we still have them in place to avoid over-messaging your users.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on July 15, 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#customizing-session-timeout
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
