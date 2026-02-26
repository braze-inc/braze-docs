---
nav_title: Create geofences
article_title: Create Geofences
page_order: 1
page_type: reference
toc_headers: h2
description: "Learn how to set up location permissions, create a location permission primer, and build geofences for location-based campaigns."
tool: 
  - Location
search_rank: 9
---

# Geofences

> A geofence is a virtual geographic area, represented as latitude and longitude combined with a radius, forming a circle around a specific global position. Geofences can vary from the size of a building to the size of an entire city. You can use geofences to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later.

{% alert tip %}
For a guided walkthrough, refer to the Braze Learning course [Create a Geofence](https://learning.braze.com/create-a-geofence).
{% endalert %}

## How it works

Geofences are organized into geofence sets—a group of geofences that you can use to segment or engage users throughout the platform. Each geofence set can hold a maximum of 10,000 geofences. You can create or upload an unlimited number of geofences.

Users who enter or exit your geofences add a new layer of user data that you can use for segmentation and re-targeting.

Keep the following device limits in mind:

- Android apps may store up to 100 geofences locally at a time. Braze is configured to store only up to 20 geofences locally per app.
- iOS devices may monitor up to 20 geofences at a time per app. Braze monitors up to 20 locations if space is available.
- If the user is eligible to receive more than 20 geofences, Braze downloads the maximum number of locations based on proximity to the user at session start.
- For geofences to work correctly, ensure that your app is not using all available geofence spots.

The following table describes common geofence terms:

| Term | Description |
|---|---|
| Latitude and longitude | The geographic center of the geofence. |
| Radius | The radius of the geofence in meters, measured from the geographic center. Set a minimum radius of 100 meters to 150 meters for all geofences. |
| Cooldown | Users receive geofence-triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined period during which that user can't perform the same transition on that individual geofence again. This "cooldown" is pre-defined by Braze and its main purpose is to prevent unnecessary network requests. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prerequisites

### SDK and platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following must be in place:

* Your integration must support background push notifications.
* Braze geofences or location collection must be enabled.
* On iOS 11 and later, the user must grant "Always Allow" location access for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0, Braze location collection is disabled by default. To verify that it's enabled on Android, confirm that `com_braze_enable_location_collection` is set to `true` in your `braze.xml`.
{% endalert %}

For platform-specific setup instructions, refer to [Geofences]({{site.baseurl}}/developer_guide/geofences/) in the developer guide.

### Location permissions

Before your geofences can function, users must grant your app permission to access their location. Understanding the different permission levels and their impact on geofencing is critical to building an effective location-based strategy.

## Understanding location permissions

Both iOS and Android offer multiple levels of location access. The permission level a user grants directly affects whether geofencing works and how accurate the location data is.

### Permission levels

{% tabs local %}
{% tab iOS %}

| Permission | Description | Geofencing support |
|---|---|---|
| **Allow Once** | Grants location access for a single session. The prompt reappears the next time the user opens the app. | No. Background tracking is disabled, so the device only receives location updates when the app is open. |
| **Allow While Using the App** | Grants location access whenever the app is in the foreground. After this is granted, iOS may present a follow-up prompt asking the user to upgrade to "Always Allow". | Yes. iOS enables background location monitoring, including geofence transitions, for apps with this permission. |
| **Always Allow** | Grants continuous location access, including in the background and when the app is closed. | Yes. This provides the most reliable geofence monitoring. |
| **Don't Allow** | Denies all location access. | No. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Android %}

| Permission | Description | Geofencing support |
|---|---|---|
| **While Using the App** | Grants location access while the app is in the foreground. | No. On Android, background location access is required for geofence monitoring. |
| **Always Allow** | Grants continuous location access, including in the background. On Android 10 and later, this requires a separate prompt after the initial "While Using the App" permission is granted. | Yes. This is required for geofencing on Android. |
| **Don't Allow** | Denies all location access. On Android 13 and later, if a user denies the location prompt twice, the OS blocks further in-app prompts. | No. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Precise versus approximate location

On iOS 14 and later, and Android 12 and later, users can choose between **precise** and **approximate** location.

| Setting | Accuracy | Impact on geofencing |
|---|---|---|
| **Precise location (on)** | Accuracy in the 5 meter to 50 meter range, using GPS, Wi-Fi, and cellular triangulation. | Geofences function as expected. Recommended for all geofence-based use cases. |
| **Approximate location (off)** | Accuracy around 3 square kilometers (approximately 1 square mile). The device returns a general area rather than exact coordinates. | Geofences don't trigger reliably. The device can't accurately determine whether a user is inside or outside a geofence boundary. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
For geofencing to work reliably, users must enable precise location. Include this guidance in your location permission primer messaging so users understand why precise location matters.
{% endalert %}

## Setting up a location permission primer

A location permission primer is an in-app message that explains the value of sharing location data before the user sees the native OS permission prompt. Because the native location prompt can only be shown once (on iOS) or a limited number of times (on Android), priming users in advance increases opt-in rates.

{% alert note %}
Braze in-app messages don't include a built-in button action to trigger the native location permission prompt. To create a location permission primer, your development team must set up a [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) that invokes the native location permission dialog on iOS and Android.
{% endalert %}

### Step 1: Work with your development team

Before building the in-app message in Braze, coordinate with your development team to set up the following deep links:

1. **A deep link that triggers the native location prompt** (for example, `yourapp://request-location-permission`). This invokes the native location permission dialog on iOS and Android from within your app. For more information, refer to [Deep linking to in-app content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).
2. **A deep link that opens the app's location settings page in the OS** (for example, `yourapp://open-location-settings`). This is useful for re-prompting users who previously denied or limited their permissions.
    - On iOS, this links to the app-specific settings screen using `UIApplication.openSettingsURLString`.
    - On Android, this links to the app's settings detail page using `android.provider.Settings.ACTION_APPLICATION_DETAILS_SETTINGS`.

### Step 2: Build the location primer in-app message

Create a custom in-app message campaign that explains the value of location access.

1. Go to **Messaging** > **Campaigns**, then select **Create Campaign** > **In-App Message**.
2. Choose a message layout. A **Modal** or **Full** layout gives you space to articulate the benefits.
3. Write messaging that clearly explains why location access benefits the user. For example:
    - "Enable location to get notified about deals near you."
    - "Turn on location so we can let you know when your order is ready for pickup at your nearest store."
4. Add a primary call-to-action button (such as **Turn On Location**) and set its on-click behavior to **Deep Link into App**, using the custom deep link your development team created (for example, `yourapp://request-location-permission`).
5. Add a secondary button (such as **Not Now**) that closes the message.

### Step 3: Target the right audience

For best results, show the location primer when users are engaged and likely to see value in sharing their location.

- **Target users who haven't granted location access yet.** Use custom attributes set by your app to track which users haven't been prompted or haven't granted permissions.
- **Time the primer after a high-value action,** such as completing a purchase, saving a store as a favorite, or browsing nearby events. Users are more likely to opt in when they understand the benefit.
- **Avoid showing the primer on first launch.** Wait until users have experienced enough value from the app to want a more personalized experience.

### Step 4: Encourage the recommended permission level

Your primer messaging should encourage users to grant the permission level that enables geofencing:

- **On iOS,** encourage users to select **Allow While Using the App** at minimum. iOS may later prompt the user to upgrade to **Always Allow** on its own. You can also follow up with a separate campaign to explain why "Always Allow" provides the best experience.
- **On Android,** encourage users to grant **Always Allow**. On Android 10 and later, the user must first grant "While Using the App", then grant "Always Allow" in a separate follow-up prompt. Guide them through both steps.

In both cases, remind users to keep **Precise Location** turned on for the best experience.

## Redirecting users to OS settings

If a user previously denied location access or selected a limited permission, you can't trigger the native prompt again from within the app on most OS versions. Instead, direct them to update their permissions in device settings.

Use a deep link inside a custom [in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) to navigate the user to the app's settings page in the OS:

- **Deep link target:** Use the deep link your development team created that opens the app's location settings page (for example, `yourapp://open-location-settings`).
- **When to show:** Target users who have "While Using the App" permission when you need "Always Allow", or users who previously denied location access.
- **Messaging example:** "To get the most out of location-based features, update your location settings to 'Always Allow'. Tap below to go to Settings."

{% alert tip %}
You can trigger this in-app message at any point in the user journey—after a purchase, when browsing nearby content, or as part of a Canvas flow. Be selective when re-prompting: limit these campaigns to loyal or highly engaged users to avoid opt-in fatigue.
{% endalert %}

## Example location priming strategies

### "While Using the App" primer

A retail app displays a modal in-app message after a user saves a store as a favorite:

- **Heading:** "Get notified about in-store deals"
- **Body:** "Turn on location so we can send you exclusive offers when you're near your favorite stores. Your location is only accessed when using the app."
- **CTA:** **Turn On Location** → deep links to native location permission prompt
- **Secondary:** **Maybe Later** → closes the message

This approach is effective because the user has already expressed interest in a specific store, creating a natural context for the location permission request.

### "Always Allow" follow-up

After a user grants "While Using the App" permission, show a follow-up in-app message during the next session:

- **Heading:** "Never miss a nearby deal"
- **Body:** "Update your location settings to 'Always' so we can notify you about offers even when you're not browsing the app. We'll only send relevant alerts when you're near participating locations."
- **CTA:** **Update Settings** → deep links to the app's location settings page in the OS
- **Secondary:** **Keep Current Settings** → closes the message

This follow-up gives the user context for why upgrading to "Always Allow" provides additional value beyond the initial permission level.

## Manually create geofences

### Step 1: Create a geofence set

To create a geofence, create a geofence set first.

1. Go to **Audience** > **Locations** in the Braze dashboard.
2. Select **Create Geofence Set**.
3. For **Set name**, enter a name for your geofence set.
4. (Optional) Add tags to filter your set.

### Step 2: Add the geofences

Next, add geofences to your geofence set.

1. Select **Draw Geofence** to click and drag the circle on the map. Repeat to add more geofences to your set as needed.
2. (Optional) Select **Edit** and replace the geofence description with a name.
3. Select **Save Geofence Set** to save.

{% alert tip %}
Create geofences with a radius of at least 200 meters for optimal functionality. For more information, refer to [Geofence best practices](#geofence-best-practices).
{% endalert %}

![A geofence set with two geofences "EastCoastGreaterNY" and "WesternRegion" with two circles on the map.]({% image_buster /assets/img/geofence_example.png %})

## Bulk upload geofences {#creating-geofence-sets-via-bulk-upload}

You can upload geofences in bulk as a GeoJSON object of type `FeatureCollection`. Each geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `radius` key and an optional `name` key for each geofence. 

To upload your JSON file, select **More** > **Upload JSON**.

When creating your geofences, consider the following details:

- The `coordinates` value in the GeoJSON is formatted as `[Longitude, Latitude]`.
- The maximum geofence radius that may be uploaded is 10,000 meters (about 10 kilometers or 6.2 miles).

### Example

The following example shows the correct GeoJSON format for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Using geofence events

After you configure your geofences, you can use them to enhance and enrich how you communicate with your users.

### Triggering campaigns and Canvases

To use geofence data as part of campaign and Canvas triggers, choose **Action-Based Delivery** for the delivery method. Next, add a trigger action of `Trigger a Geofence`. Finally, choose the geofence set and geofence transition event types for your message. You can also advance users through a Canvas using geofence events.

![An action-based campaign with a geofence that will trigger when a user enters German airports.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizing messages

To use geofence data to personalize a message, you can use the following Liquid personalization syntax:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Updating geofence sets

The Braze SDK requests geofences only once per day on session start. If you make changes to the geofence sets after session start, you need to wait 24 hours from the time the sets are first pulled down to receive the updated set.

If the user has background push enabled, Braze sends a silent push once every 24 hours when geofence sets are updated to pull down the latest locations to the device.

{% alert note %}
If the geofences aren't loaded onto the device locally, the user can't trigger the geofence even if they enter the area.
{% endalert %}

## Geofence best practices

### Geofence configuration

- Use a radius of 200 meters or more for reliable triggering.
- Avoid setting up geofences that overlap or are nested inside each other, as this can cause problems with triggering.
- A geofence can trigger an enter event only once every six hours. This cooldown period is enforced locally. If a user uninstalls the app or clears app data, all cooldowns reset.
- No more than 20 geofences in total can be stored on a device. If the user is eligible for more than 20, Braze downloads the closest locations based on proximity at session start or silent push refresh.
- Braze sends only geofences within a 2,000 km radius of the user to the device.

### Device requirements

- Push permissions and location permissions must both be enabled for the app.
- A valid foreground push token is required.

{% alert note %}
Basic SDK integration enables location tracking only. Geofencing requires additional setup steps for both iOS and Android. For details, refer to [Geofences]({{site.baseurl}}/developer_guide/geofences/) in the developer guide.
{% endalert %}

You can also use geofences with Braze Technology Partners, such as [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) and [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/).

## Frequently asked questions

### What's the difference between geofences and location tracking?

In Braze, a geofence is a different concept from location tracking. Geofences are used as triggers for certain actions—when a user enters or exits a virtual boundary set up around a geographical location, it can trigger a specific action, such as sending a message.

Location tracking collects and stores a user's most recent location data. This data can be used to segment users based on the `Most Recent Location` filter. For example, you could use the `Most Recent Location` filter to target users located in New York.

For more information, refer to [Location tracking]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location, including Wi-Fi, GPS, and cellular towers.

Typical accuracy is in the 20 meter to 50 meter range, and best-case accuracy is in the 5 meter to 10 meter range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Create geofences with larger radii in rural locations.

Accuracy also depends on whether the user has precise location enabled. With approximate location only, accuracy drops to around 3 square kilometers, making geofences unreliable. For more information, refer to [Precise versus approximate location](#precise-versus-approximate-location).

### How do geofences affect battery life?

Braze geofencing uses the native geofence system service on iOS and Android. It's tuned to intelligently trade off accuracy and power, saving battery life and improving performance as the underlying service improves.

### When are geofences active?

Braze geofences work at all hours of the day, even when your app is closed. They become active as soon as they are defined and uploaded to the Braze dashboard. However, geofences can't function if a user has disabled location tracking.

For geofences to work, users must have location services enabled on their device and must have granted your app the required location permission level. For more information, refer to [Understanding location permissions](#understanding-location-permissions).

### Is geofence data stored in user profiles?

No, Braze doesn't store geofence data on user profiles. Geofences are monitored by Apple and Google location services, and Braze only gets notified when a user triggers a geofence. At that point, Braze processes any associated trigger campaigns.

### Can I set up a geofence within a geofence?

As a best practice, avoid setting up geofences that overlap with each other, as this may cause issues with triggering notifications.

### What if a user denies location access?

You can use a deep link inside a custom in-app message at any time to direct users to the app's location settings page in the OS, where they can update their permissions. Be selective about when you show this message—target users who are engaged or who have performed a high-value action to increase the chance of an opt-in. For more information, refer to [Redirecting users to OS settings](#redirecting-users-to-os-settings).

