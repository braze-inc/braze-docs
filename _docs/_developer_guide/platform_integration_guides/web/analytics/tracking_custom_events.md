---
nav_title: Tracking Custom Events
article_title: Tracking Custom Events for Web
platform: Web
page_order: 2
page_type: reference
description: "This article covers how to track custom events via the Braze SDK."

---

# Tracking custom events for web

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [Best practices][0]. We also recommend familiarizing yourself with our [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
import braze from "@braze/web-sdk"
braze.logCustomEvent("YOUR-EVENT-NAME");
```

See the [`logCustomEvent` documentation][1] for more information.


## Adding properties {#properties-events}

You can also add event properties to supply added metadata about the custom event.

Properties are an object where its keys are strings, and their values can a valid data type (see below), or any array or object containing valid data.

Valid data types include: `string`, `number`, `boolean`, or [`Date`][2].

```javascript
import braze from "@braze/web-sdk";

// flat event properties
braze.logCustomEvent(YOUR_EVENT_NAME, {
  you: 'can', 
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
[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcustomevent
[2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
