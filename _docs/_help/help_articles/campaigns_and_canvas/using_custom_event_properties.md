---
nav_title: Using Custom Event Properties
page_order: 5
---

# Are My Custom Event Properties Being Logged?

There are three important checks to carry out to ensure your Custom events are being logged as you expect:

* [Establish which events are logged](#which-events)
* [Verify log](#verify-log)
* [Verify values](#verify-values)

## Custom Event Properties

[Custom event properties][22] are metadata that describe custom events. Multiple properties may be logged each time a custom event is logged.

## Verify Custom Event properties

### Which Events?

Check with your developers which event properties are being tracked. Keep in mind that all event properties are case sensitive.

For further information see:

* [Android][51]
* [iOS][23]
* [Web][52]


### Verify Log

To confirm that the event properties are successfully tracked, you can view all event properties by going to the Manage App Groups page, clicking on the Custom Events tab, then clicking on Manage Properties. This will show you the names of all of the properties associated with an event.

### Verify Values

To check the specific property values that are being passed for each event, check the [Event User Logs][24] on your dashboard. After adding your user as a test user, you should perform the Custom event within the App, wait around 10 seconds for the data to flush, and then refresh the event user log to view the custom event and the event property value that was passed with it.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
