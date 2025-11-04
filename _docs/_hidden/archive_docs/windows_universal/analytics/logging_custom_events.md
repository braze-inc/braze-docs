---
nav_title: Tracking custom events
article_title: Tracking Custom Events for Windows Universal
platform: Windows Universal
page_order: 2
description: "This reference article covers how to track custom events on the Windows Universal platform."
hidden: true
---

# Tracking custom events
{% multi_lang_include archive/windows_deprecation.md %}

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

All events are logged by using the `EventLogger`, which is a property exposed in IAppboy. To obtain a reference to the `EventLogger`, call `Appboy.SharedInstance.EventLogger`. You can use the following methods to track important user actions and custom events:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
