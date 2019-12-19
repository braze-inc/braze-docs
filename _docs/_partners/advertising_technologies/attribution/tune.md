---
nav_title: Tune
alias: /partners/tune/

description: "This article outlines the partnership between Braze and Tune, a mobile analytics and performance marketing platform that makes it easy to manage campaigns."
page_type: partner

---

# Tune (MobileAppTracking)

> Tune is a mobile analytics and performance marketing platform that makes it easy to manage campaigns, engage the right audiences, and optimize app performance.

Braze and Tune enable you to import paid install attribution data from Tune to Segment more intelligently within your lifecycle campaigns.

## Integration

### Step 1: Integration Requirements

* This integration supports iOS, Android, and Windows Universal apps.
* If you expect more than 100 attributed installs per hour, you will need a Braze Enterprise account. See [API Restrictions][5] for more information.
* Your app will need Braze's SDK and Tune's SDK installed.
* If you have an iOS app, you will need to [enable IDFA collection][13] in Braze's SDK.
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to Tune. For most setups, this code should be included alongside all calls to `mobileAppTracker.setAndroidId` or `mobileAppTracker.setGoogleAdvertisingId`, typically in an activity's `onCreate` callback.

```java
mobileAppTracker.setUserId(Appboy.getInstance(context).getInstallTrackingId());
```

### Step 2: Getting the Postback URL

In your Braze account, navigate to "Technology Partners" , then "Attribution"and find the Postback URL in the MobileAppTracking section. This url represents the api endpoint that an attribution partner will send data to. You will need this url in the next step when setting up a callback in Tune's dashboard.

### Step 3: Setting Up A Postback from Tune

Follow [these instructions][19] to set up a postback in Tune's dashboard so that it sends attribution data to Braze. This should be configured to send to the Postback URL you copied from Braze's Dashboard in Step 2. Also configure the Postback to only send data for non-organic installs.

Braze maps Tune's Postback Macros to segment filters in the following way

| Tune Postback Macro | Braze Segment Filter |
| -------------------- | --------------------- |
| {advertiser_sub_publisher} | Attributed Source |
| {advertiser_sub_campaign} | Attributed Campaign |
| {advertiser_sub_adgroup} | Attributed Adgroup |
| {advertiser_sub_ad} | Attributed Ad |

### Step 4: Confirming the Integration

Once Braze receives attribution data from Tune, the status connection indicator on ["Technology Partners" , then "Attribution"][14] will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded from the Tune postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third-parties and, therefore, our partners __cannot send that data to Braze__.


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
