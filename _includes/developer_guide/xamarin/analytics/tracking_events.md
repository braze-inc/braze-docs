{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Logging custom events

You can record custom events in Braze using `LogCustomEvent` to learn more about your app’s usage patterns and to segment your users by their actions in the dashboard.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/tracking_custom_events/) for an in-depth discussion of event tracking best practices and interfaces.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/analytics/tracking_custom_events/) for an in-depth discussion of event tracking best practices and interfaces.

{% endtab %}
{% endtabs %}
