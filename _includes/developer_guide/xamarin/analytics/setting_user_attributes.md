{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Setting user attributes

Braze provides methods for assigning attributes to users. You’ll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK. For example, you can set the user's first name:

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Email

### Custom user attributes

In addition to our predefined user attribute methods, Braze also provides custom attributes using `SetCustomUserAttribute` to track data from your applications.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) for an in-depth discussion of attribute tracking best practices and interfaces.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) for an in-depth discussion of attribute tracking best practices and interfaces.

{% endtab %}
{% endtabs %}
