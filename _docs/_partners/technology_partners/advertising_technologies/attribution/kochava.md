---
nav_title: Kochava
alias: /partners/kochava/
---

# Kochava

Kochava offers mobile attribution and analytics to help you harness your data for growth. The Kochava Audience Platform enables you to plan, target, activate, measure, and optimize your app campaigns.

Kochava and Braze power a more holistic understanding of campaigns. Kochava sends attribution data to Braze to better understand what campaigns are driving installs, in-app activity, and more.

## Integration

__Step 1: Integration Requirements__

* This integration supports iOS, Android, and Windows apps.
* If you expect more than 100 attributed installs per hour, you will need a Braze Enterprise account. See [API Restrictions][5] for more information.
* Your app will need Braze's SDK and Kochava's SDK installed.
* You will need to [enable IDFA collection][13] in Braze's SDK.

__Step 2: Getting the Attribution ID__

Go to your Braze account, navigate to ["Technology Partners", then "Attribution"][14] and find the API key and REST Endpoint in the Kochava section. The API key and the REST Endpoint are used in the next step when setting up a postback in Kochava's dashboard.

__Step 3: Setting Up A Postback from Kochava__

Follow [these instructions][18] to add a postback in Kochava's dashboard. You will be prompted for the key and REST Endpoint that you found in Braze's Dashboard in Step 2. Select the __"POST"__ request when creating the PostBack Call on Kochava's dashboard.

__Step 4: Confirming the Integration__

Once Braze receives attribution data from Kochava, the status connection indicator on ["Technology Partners" , then "Attribution"][14] will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs are ignored by our API and are not counted when determining if a successful connection was established.

Note for Android and Windows Support: If you are planning to leverage the server side integration between Braze and Kochava, you'll need to ensure that you utilize the 'Identity Link' method of the Kochava SDK to capture the 'Braze ID' for [Android][29] and [Windows][30]. Please ensure that you instrument this method to capture/pass the 'Braze ID' on SDK initialization to ensure it is available when Kochava is posting your data back to Braze via the server side integration.

### Tune (MobileAppTracking)
__Step 1: Integration Requirements__

* This integration supports iOS, Android, and Windows Universal apps.
* If you expect more than 100 attributed installs per hour, you will need a Braze Enterprise account. See [API Restrictions][5] for more information.
* Your app will need Braze's SDK and Tune's SDK installed.
* If you have an iOS app, you will need to [enable IDFA collection][13] in Braze's SDK.
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to Tune. For most setups, this code should be included alongside all calls to `mobileAppTracker.setAndroidId` or `mobileAppTracker.setGoogleAdvertisingId`, typically in an activity's `onCreate` callback.

```java
mobileAppTracker.setUserId(Appboy.getInstance(MyActivity.this).getInstallTrackingId());
```

__Step 2: Getting the Postback URL__

In your Braze account, navigate to "Technology Partners" , then "Attribution" and find the Postback URL in the MobileAppTracking section. This url represents the api endpoint that an attribution partner will send data to. You will need this url in the next step when setting up a callback in Tune's dashboard.

__Step 3: Setting Up A Postback from Tune__

Follow [these instructions][19] to set up a postback in Tune's dashboard so that it sends attribution data to Braze. This should be configured to send to the Postback URL you copied from Braze's Dashboard in Step 2. Also configure the Postback to only send data for non-organic installs.

Braze maps Tune's Postback Macros to segment filters in the following way

| Tune Postback Macro | Braze Segment Filter |
| -------------------- | --------------------- |
| {advertiser_sub_publisher} | Attributed Source |
| {advertiser_sub_campaign} | Attributed Campaign |
| {advertiser_sub_adgroup} | Attributed Adgroup |
| {advertiser_sub_ad} | Attributed Ad |

__Step 4: Confirming the Integration__

Once Braze receives attribution data from Tune, the status connection indicator on ["Technology Partners" , then "Attribution"][14] will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded from the Tune postback, are ignored by our API and are not counted when determining if a successful connection was established.

[5]: #api-restrictions
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#optional-idfa-collection
[15]: https://docs.adjust.com/en/callbacks/ "Adjust Callbacks"
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[17]: http://support.apsalar.com/customer/portal/articles/1503188-creating-and-managing-postbacks "Singular Postbacks"
[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[19]: http://support.mobileapptracking.com/entries/22560357-Setting-Up-Postback-URLs "Tune Postbacks"
[20]: https://github.com/adjust/ios_sdk#9-implement-the-attribution-callback "Adjust SDK-to-SDK Integrations on iOS"
[21]: https://github.com/adjust/android_sdk#16-set-listener-for-attribution-changes "Adjust SDK-to-SDK Integrations on Android"
[22]: https://dev.branch.io/recipes/analytics_appboy/ "Branch Webhooks"
[23]:{% image_buster /assets/img_archive/adjust.png %}
[24]:{% image_buster /assets/img_archive/appsflyer.png %}
[25]:{% image_buster /assets/img_archive/singular.png %}
[26]:{% image_buster /assets/img_archive/branch.png %}
[27]:{% image_buster /assets/img_archive/kochava.png %}
[28]:{% image_buster /assets/img_archive/tune.png %}
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
