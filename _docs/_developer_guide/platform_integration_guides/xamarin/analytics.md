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
 
# Xamarin analytics

## Setting user IDs

{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).ChangeUser("YOUR_USER_ID");
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.

{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.
{% endtab %}
{% endtabs %}

## Tracking custom events
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogCustomEvent("YOUR_EVENT_NAME");
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) for an in-depth discussion of event tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogCustomEvent ("YOUR_EVENT_NAME");
```

**Implementation Example** - `logCustomEvent` is utilized within the `AppboySampleViewController.cs` within the [TestApp.XamariniOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS) sample application.

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) for an in-depth discussion of event tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

## Logging purchases
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogPurchase("product_id", 100);
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases=) for an in-depth discussion of revenue tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogPurchase ("product_id", "USD", new NSDecimalNumber("10"));
```

**Implementation Example** - You can see user properties being set in the sample application's `EventsAndPurchasesButtonHandler` method inside `AppboySampleViewController.cs`.

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

### Log purchases at the order level
If you would like to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

## Setting custom attributes
{% tabs %}
{% tab %}
```csharp
Braze.getInstance(context).CurrentUser.SetFirstName("FirstName");
```

See the [Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}

```csharp
// C#
Appboy.SharedInstance ().User.FirstName = "YOUR_NAME";
```

**Implementation Example** - You can see user properties being set in the sample application's `UserPropertyButtonHandler` method inside `AppboySampleViewController.cs`.

See the [iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

## Location tracking

- Android: See the [Android integration instructions][2] for information on how to support location tracking.
- iOS: See the Xamarin [using background location walkthrough][11] and the [iOS integration instructions][12] for information on how to support location tracking.

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/#location-tracking
[11]: http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/
