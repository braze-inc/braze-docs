---
nav_title: Analytics
article_title: Analytics for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "This article covers iOS, Android, and FireOS analytics for the Xamarin platform."

---
 
# Analytics

> Learn how to generate and review analytics for the Xamarin platform.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Session tracking

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

## Logging purchases

Record in-app purchases using `LogPurchase` to track your revenue over time and across revenue sources, as well as segment your users by their lifetime value.

Braze supports purchases in multiple currencies. Purchases that you report in a currency other than USD will be shown in the dashboard in USD based on the exchange rate at the date they were reported.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.

{% endtab %}
{% endtabs %}

### Log purchases at the order level

If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### Reserved keys

The following keys are reserved and **cannot** be used as purchase properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Logging custom attributes

Braze provides methods for assigning attributes to users. You’ll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To assign user attributes automatically collected by Braze, you can use setter methods that come with the SDK. For example, you can set the user's first name:

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

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.

{% endtab %}
{% endtabs %}

## Location tracking

For an example of logging and tracking analytics, refer to our [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) and [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs) sample applications.

{% tabs %}
{% tab android %}
For more information, see the [Android integration instructions]({{site.baseurl}}/developer_guide/platforms/android/analytics/location_tracking/).
{% endtab %}

{% tab ios %}
To support local tracking, see [iOS: Using background location](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) and the [iOS integration instructions]({{site.baseurl}}/developer_guide/platforms/swift/geofences/).
{% endtab %}
{% endtabs %}

