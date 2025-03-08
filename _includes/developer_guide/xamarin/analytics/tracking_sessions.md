{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Tracking sessions

The Braze SDK reports session data used by the Braze dashboard to calculate user engagement and other analytics integral to understanding your users. Based on the following session semantics, our SDK generates “start session” and “close session” data points that account for session length and session counts viewable within the Braze dashboard.

To set a user ID or start a session, use the `ChangeUser` method, which takes a user ID parameter.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.

{% endtab %}
{% endtabs %}
