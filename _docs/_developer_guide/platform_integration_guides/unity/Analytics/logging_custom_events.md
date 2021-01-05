---
nav_title: Logging Custom Events
platform: Unity
page_order: 1
---
## Logging Custom Events

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by Custom events vs. Custom attributes vs Purchase events in our [Best Practices section][4]. You should also check out our notes on [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze also supports adding metadata about custom events by passing a `Dictionary` of event properties:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

### REST API

You can also use our REST API to record events. Refer to the [user API documentation][5] for details.

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/InitialViewController.m
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/AppboyKit.framework/Headers/Appboy.h
[3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "logcustomevent documentation"
[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
