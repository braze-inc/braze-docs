---
nav_title: Tracking Custom Events
article_title: Tracking Custom Events for Web
platform: Web
page_order: 2
page_type: reference
description: "This article covers how to track custom events for Web."

---

# Tracking custom events for web

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices][0]. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

See the [`logCustomEvent`][1] documentation for more information.

## Adding properties {#properties-events}

You can optionally add metadata about custom events by passing a properties object with your custom event.

Properties are defined as key-value pairs. Keys are strings and values can be `string`, `numeric`, `boolean`, or [`Date`][2] objects.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

See the [`logCustomEvent()` documentation][1] for more information.

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent
[2]: http://www.w3schools.com/jsref/jsref_obj_date.asp
