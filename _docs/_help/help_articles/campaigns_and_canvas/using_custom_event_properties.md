---
nav_title: Logging Custom Event Properties
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

[Custom event properties][22] are metadata that describe custom events. Multiple properties may be logged each time a custom event is logged.

### Verify events

Check with your developers which event properties are being tracked. Keep in mind that all event properties are case-sensitive. For additional information on tracking custom events, check out these articles based on your platform:

* [Android][51]
* [iOS][23]
* [Web][52]

### Verify log

To confirm that the event properties are successfully tracked, you can view all event properties by navigating to the **Manage Settings > Custom Events** tab **> **Manage Properties**. This will show you the names of the properties associated with an event.

### Verify values

After adding your user as a test user, follow these steps to verify your values: 

1. Perform the custom event within the app.
2. Wait for roughly 10 seconds for the data to flush.
3. Refresh the [Event User Log][24] to view the custom event and the event property value that was passed with it.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on April 10, 2023_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
