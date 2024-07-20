---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "This reference article outlines the partnership between Braze and Gimbal, which enables you to perfect your marketing relevance using location data."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) enables you to perfect your marketing relevance using location data. Their location SDK paired with geofencing software and beacons power relevant, personalized, proximity-aware mobile experiences.

Combine your beacon or geofence support with Braze's targeting and messaging features to learn more about your user's physical actions and message them accordingly. This partnership integration opens up an array of use cases for:
- **Marketing:** Send contextually relevant messaging and build experiential consumer journeys.
- **Competitive Analysis:** Set up triggers around competitive locations to understand consumer trends and patterns.
- **Audience Insights:** Understand your users' visitation behaviors and further segment based on those learnings.

## Prerequisites

| Requirement| Description|
| ---| ---|
| [Gimbal manager account](https://manager.gimbal.com/login/users/sign_in) | A Gimbal manager account is required to take advantage of this partnership. |
|[Gimbal Location SDK](https://docs.gimbal.com/index.html) | The Gimbal Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. You must have the SDK implemented, and geofences (or beacons) set up. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2}

## SDK integration

To integrate Braze and Gimbal, you must implement the Gimbal Location SDK and create a Gimbal manager account. The following integrations for Android, FireOS, and iOS will create a unique custom event for each new place a user enters, these events can then be used for triggering and retargeting in your campaigns and Canvases.

If you anticipate creating more than 50 places, we recommend creating a generic `Places Entered` custom event and adding the place name as an event property. 

1. Integrate the [Gimbal SDK](https://manager.gimbal.com/sdk_downloads) for Android and iOS into your app by following the instructions in the [Gimbal documentation](https://docs.gimbal.com/).
2. Use Gimbal's [place REST API](https://docs.gimbal.com/rest.html) to get user `places`.
3. Link your Gimbal account to Braze by entering the Braze [REST API key](https://manager.gimbal.com/apps).
4. Set up [custom events]({{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/) in the Braze SDK. You can integrate Gimbal with Braze for [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons).
5. Log properties for these events (Place Name, Dwell Time).
6. Use these properties and events for triggering campaigns and Canvases in Braze. 

