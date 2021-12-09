---
nav_title: Tracking Custom Events
article_title: Tracking Custom Events for Windows Universal
platform: Windows Universal
page_order: 2
description: "This reference article covers how to track custom events on the Windows Universal platform."
---

# Tracking custom events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

All events are logged by using the `EventLogger`, which is a property exposed in IAppboy. To obtain a reference to the `EventLogger`, call `Appboy.SharedInstance.EventLogger`. You can use the following methods to track important user actions and custom events:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```

You should also check out our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

