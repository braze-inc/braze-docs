---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "This reference article outlines the partnership between Braze and Infillion, which enables you to perfect your marketing relevance using location data."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) enables you to perfect your marketing relevance using location data. Their location SDK paired with geofencing software and beacons power relevant, personalized, proximity-aware mobile experiences.

Combine your beacon or geofence support with Braze targeting and messaging features to learn more about your user's physical actions and message them accordingly. This partnership integration opens up an array of use cases for:

- **Marketing:** Send contextually relevant messaging and build experiential consumer journeys.
- **Competitive Analysis:** Set up triggers around competitive locations to understand consumer trends and patterns.
- **Audience Insights:** Understand your users' visitation behaviors and further segment based on those learnings.

{% alert note %}
This integration works the same for Infillion beacons and Infillion geofence solutions.
{% endalert %}

## Prerequisites

| Requirement| Description|
| ---| ---|
| [Infillion manager account][1] | A Infillion manager account is required to take advantage of this partnership. |
|[Infillion Location SDK](https://docs.gimbal.com/index.html) | The Infillion Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. You must have the SDK implemented, and geofences (or beacons) set up. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK integration

To integrate Braze and Infillion, you must implement the Infillion Location SDK and create a Infillion manager account. The following integrations for Android, FireOS, and iOS will create a unique custom event for each new place a user enters, these events can then be used for triggering and retargeting in your campaigns and Canvases.

If you anticipate creating more than 50 places, we recommend creating a generic `Places Entered` custom event and adding the place name as an event property. 

1. Integrate the [Infillion SDK][2] for Android and iOS into your app by following the instructions in the [Infillion documentation][3].
2. Use Infillion's [place REST API][4] to get user `places`.
3. Link your Infillion account to Braze by entering the Braze [REST API key][5].
4. Set up [custom events][6] in the Braze SDK. You can integrate Infillion with Braze for [Android and FireOS][7] and [iOS][8].
5. Log properties for these events (Place Name, Dwell Time).
6. Use these properties and events for triggering campaigns and Canvases in Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data/custom_data/custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons