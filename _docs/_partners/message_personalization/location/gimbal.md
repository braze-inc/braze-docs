---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "This article outlines the partnership between Braze and Gimbal, which enables you to perfect your marketing relevance using location data."
page_type: partner
search_tag: Partner

---

# Gimbal

> Originally started out of Qualcomm, Gimbal enables you to perfect your marketing relevance using location data. Their location SDK paired with geofencing software and beacons power relevant, personalized, proximity-aware mobile experiences.

Combine your beacon or geofence support with Braze’s targeting and messaging features to learn more about your user’s physical actions and message them accordingly. This partnership integration opens up an array of use cases for:
- __Marketing:__ Send contextually relevant messaging and build experiential consumer journeys.
- __Competitive Analysis:__ Set up triggers around competitive locations to understand consumer trends and patterns.
- __Audience Insights:__ Understand your users' visitation behaviors and further segment based on those learnings.

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
|Gimbal SDK | Gimbal | https://docs.gimbal.com/index.html | The Gimbal Location SDK powers macro and micro location-based mobile experiences using proximity beacons and geofences that allow you to communicate more effectively with your app users. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## SDK Integration

You must have the Location SDK implemented & geofences (or beacons) set up, as well as a Gimbal Manager account to proceed with the integration.
1.	Create a [Gimbal Manager][1] account.
2.	Integrate the [Gimbal SDK][2] for Android and iOS into your app by following the instructions in the [Gimbal Docs][3].
3.	Use [Gimbal’s Place REST API][4] to get user ‘places’.
4.	Create new apps and generate an app-specific API Key in your Braze account.
5.	Link your Gimbal account to Braze by entering the server [API key][5].
6.	Set up [Custom events][6] in the Braze SDK. You can integrate Gimbal with Braze for [Android][7], [iOS][8], and [FireOS][9].
7.	Log properties for these events (Place Name, Dwell Time).

The integrations for Android, FireOS, and iOS above will create a unique custom event for each new place that the user enters. So, if you anticipate creating more than fifty (50) places, we recommend you create one generic “Place Entered” custom event and include the place name as an event property.

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/beacon_integration/#gimbal-beacons
