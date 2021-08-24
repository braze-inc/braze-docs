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

# Xamarin Analytics

## Setting User IDs

{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).ChangeUser("YOUR_USER_ID");
```

See [the Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.

{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

See [the iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) for an in-depth discussion of when and how to set and change a user ID.
{% endtab %}
{% endtabs %}

## Tracking Custom Events
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogCustomEvent("YOUR_EVENT_NAME");
```

See [the Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) for an in-depth discussion of event tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogCustomEvent ("YOUR_EVENT_NAME");
```

**Implementation Example** - `logCustomEvent` is utilized within the `AppboySampleViewController.cs` within the [TestApp.XamariniOS](https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS) sample application.

See [the iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) for an in-depth discussion of event tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

## Logging Purchases
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogPurchase("YOUR_PURCHASE_NAME", 100);
```

See [the Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases=) for an in-depth discussion of revenue tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogPurchase ("myProduct", "USD", new NSDecimalNumber("10"));
```

**Implementation Example** - You can see user properties being set in the sample application's `EventsAndPurchasesButtonHandler` method inside `AppboySampleViewController.cs`.

See [the iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) for an in-depth discussion of revenue tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

## Setting Custom Attributes
{% tabs %}
{% tab %}
```csharp
Braze.getInstance(context).CurrentUser.SetFirstName("FirstName");
```

See [the Android integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.
{% endtab %}
{% tab iOS %}

```csharp
// C#
Appboy.SharedInstance ().User.FirstName = "YOUR_NAME";
```

**Implementation Example** - You can see user properties being set in the sample application's `UserPropertyButtonHandler` method inside `AppboySampleViewController.cs`.

See [the iOS integration instructions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) for an in-depth discussion of attribute tracking best practices and interfaces.
{% endtab %}
{% endtabs %}

## Location Tracking

- Android: See [the Android integration instructions][2] for information on how to support location tracking.
- iOS: See [Xamarin Walkthrough - Using Background Location][11] and [the iOS integration instructions][12] for information on how to support location tracking.

## Social Data Tracking (Android Only)

You can see the Xamarin binding accessing these interfaces in the `HomeFragment.cs` of our sample app.  The sample code logs a social share and populates the Braze user with data from the social networks.

```csharp
// Record Facebook Data
FacebookUser facebookUser = new FacebookUser("708379", "Test", "User", "test@braze.com", "Test", "Testtown", Gender.Male, new Java.Lang.Integer(100), new String[]{"Cats", "Dogs"}, "06/17/1987");
Braze.getInstance(context).CurrentUser.SetFacebookData(facebookUser);

// Record Twitter Data
TwitterUser twitterUser = new TwitterUser(6253282, "Test", "User", "Tester",  new Java.Lang.Integer(100), new Java.Lang.Integer(100), new Java.Lang.Integer(100), "https://si0.twimg.com/profile_images/2685532587/fa47382ad67a0135acc62d4c6b49dbdc_bigger.jpeg");
Braze.getInstance(context).CurrentUser.SetTwitterData(twitterUser);
```
See [the Android integration instructions][6] for an in-depth discussion of social data best practices and interfaces.

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/social_data_tracking/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/#location-tracking
[11]: http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/