---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "This article outlines the partnership between Braze and Gimbal, which enables you to perfect your marketing relevance using location data."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) enables you to perfect your marketing relevance using location data. Their location SDK paired with geofencing software and beacons power relevant, personalized, proximity-aware mobile experiences.

Combine your beacon or geofence support with Braze’s targeting and messaging features to learn more about your user’s physical actions and message them accordingly. This partnership integration opens up an array of use cases for:
- **Marketing:** Send contextually relevant messaging and build experiential consumer journeys.
- **Competitive Analysis:** Set up triggers around competitive locations to understand consumer trends and patterns.
- **Audience Insights:** Understand your users' visitation behaviors and further segment based on those learnings.

## Prerequisites

| Requirement| Description|
| ---| ---|
| [Gimbal manager account][1] | A Gimbal manager account is required to take advantage of this partnership. |
|[Gimbal Location SDK](https://docs.gimbal.com/index.html) | The Gimbal Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. You must have the SDK implemented, and geofences (or beacons) set up. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## SDK integration

To integrate Braze and Gimbal, you must implement the Gimbal Location SDK and create a Gimbal manager account. The following integrations for [Android][7], [FireOS][7], and [iOS][8] will create a unique custom event for each new place a user enters, these events can then be used for triggering and retargeting in your campaigns and Canvases.

If you anticipate creating more than 50 places, we recommend creating a generic `Places Entered` custom event and adding the place name as an event property. 

1. Integrate the [Gimbal SDK][2] for Android and iOS into your app by following the instructions in the [Gimbal documentation][3].
2. Use Gimbal’s [place REST API][4] to get user `places`.
3. Link your Gimbal account to Braze by entering the Braze [REST API key][5].
4. Set up [custom events][6] in the Braze SDK. See [tracking custom events](#tracking-custom-events) for more details.
5. Log properties for these events (Place Name, Dwell Time).
6. Use these properties and events for triggering campaigns and Canvases in Braze. 

## Tracking custom events
Once you have your Gimbal beacons set up and integrated into your app, you can use the Braze SDK to log custom events for things like a visit starting or ending, or a beacon being sighted. You can also log properties for these events, like the place name or the dwell time.

{% tabs %}
{% tab Android and FireOS %}

To log a custom event when a user enters a place, include this code in the `onVisitStart` method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endtab %}

The `requestImmediateDataFlush` ensures that your event will log even if the app is in the background, and the same process can be implemented for leaving a location. Note that the activity and context that you are working in may change exactly how you integrate the `logCustomEvent` and `requestImmediateDataFlush` lines. Also, note that this code will create and increment a unique custom event for each new place that the user enters. As such, if you anticipate creating more than 50 places we recommend you create one generic "Place Entered" custom event and include the place name as an event property.
{% endtab %}
{% tab Swift %}
To log a custom event when a user enters a place, input this code into the `didBeginVisit` method:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logCustomEvent:@"Entered %@", visit.place.name];
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent("Entered %@", visit.place.name)
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
The `requestImmediateDataFlush` ensures that your event will log even if the app is in the background, and the same process can be implemented for leaving a location. Note that this will create and increment a unique custom event for each new place that the user enters. If you anticipate creating more than 50 places, we recommend you create one generic "Place Entered" custom event and include the place name as an event property.
{% endtab %}
{% endtabs %}


[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/