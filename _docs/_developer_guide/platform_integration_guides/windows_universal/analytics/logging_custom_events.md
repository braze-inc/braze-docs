---
nav_title: Logging Custom Events
platform: Windows_Universal
page_order: 2
---
## Logging Custom Events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

All events are logged by using the `EventLogger`, which is a property exposed in IAppboy. To obtain a reference to the `EventLogger`, call `Appboy.SharedInstance.EventLogger`. You can use the following methods to track important user actions and custom events:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```

You should also check out our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

