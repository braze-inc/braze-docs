---
nav_title: Tracking Custom Events
article_title: Tracking Custom Events for Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "This reference article covers how to log custom events on Unity platform."

---

# Logging custom events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices][4]. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze also supports adding metadata about custom events by passing a `Dictionary` of event properties:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

You can also use our REST API to record events. Refer to the [users API][5] documentation for details.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
