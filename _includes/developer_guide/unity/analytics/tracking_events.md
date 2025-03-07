## Tracking custom events

To record custom events in Braze, so you can learn more about your Unity app's usage patterns and to segment your users by their actions on the dashboard, use the following method:

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze also supports adding metadata about custom events by passing a `Dictionary` of event properties:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

You can also use our REST API to record events. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

