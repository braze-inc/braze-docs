---
nav_title: Logging custom event properties
article_title: Logging Custom Event Properties
page_order: 3
page_type: solution
description: "This help article walks you through three important checks to ensure your custom events are logged as you expect."
tool: 
- Campaigns
- Canvas
---

# Logging custom event properties

There are three important checks to carry out to ensure your custom events are being logged as you expect:

* [Establish which events are logged](#verify-events)
* [Verify log](#verify-log)
* [Verify values](#verify-values)

## Verify custom event properties

[Custom event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) are metadata that describe custom events. Multiple properties may be logged each time a custom event is logged.

### Verify events

Check with your developers which event properties are being tracked. Keep in mind that all event properties are case-sensitive. For additional information on tracking custom events, check out these articles based on your platform:

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Verify log

To confirm that the event properties are successfully tracked, you can view all event properties from the **Custom Events** page.

1. Navigating to **Data Settings** > **Custom Events**.
2. Locate your custom event from the list.
3. For your event, click **Manage Properties**. This will show you the names of the properties associated with an event.

### Verify values

After adding your user as a test user, follow these steps to verify your values: 

1. Perform the custom event within the app.
2. Wait for roughly 10 seconds for the data to flush.
3. Refresh the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to view the custom event and the event property value that was passed with it.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on April 10, 2023_

