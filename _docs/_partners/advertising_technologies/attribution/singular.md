---
nav_title: Singular
alias: /partners/singular/

description: "This article outlines the partnership between Braze and Singular, a unified marketing analytics platform."
page_type: partner

---

# Singular

> Singular is a unified marketing analytics platform that delivers attribution, cost aggregation, creative reporting, and workflow automation.

Singular allows you to import paid install attribution data to segment more intelligently within your lifecycle campaigns.

## Integration

### Step 1: Integration Requirements

* This integration supports iOS and Android apps.
* Your app will need Braze's SDK and Singular's SDK installed.
* If you have an iOS app, you will need to [enable IDFA collection][13] in Braze's SDK.
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze user id to Singular. For most setups, 2 lines of code must be added in an app's `onCreate()` method immediately after Singular's `init` method  or session start. Braze's `device_id` must be available when the first “App Open” event is sent to Singular.

```java
@Override
protected void onCreate(Bundle savedInstanceState)
{
    // Other code
    // Init Singular SDK
   Singular.init(context, config); // context is Application Context
   // Code For Braze
   String appboyDeviceId = Appboy.getInstance(context).getInstallTrackingId();
   Singular.event("App Open", "appboyUserID", appboyDeviceId);
}
```

### Step 2: Getting the Braze API Key

In your Braze account, navigate to "Technology Partners" , then "Attribution" and find the API key and REST Endpoint in the Singular section. You will need to provide the API key and the REST Endpoint to your Singular Account Manager for the integration to be completed.

### Step 3: Confirming the Integration

Once Braze receives attribution data from Singular, the status connection indicator on "Technology Partners" , then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded from the Singular postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third-parties and, therefore, our partners __cannot send that data to Braze__.


[5]: #api-restrictions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#optional-idfa-collection
[15]: https://docs.adjust.com/en/callbacks/ "Adjust Callbacks"
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[17]: http://support.apsalar.com/customer/portal/articles/1503188-creating-and-managing-postbacks "Singular Postbacks"
[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[19]: http://support.mobileapptracking.com/entries/22560357-Setting-Up-Postback-URLs "Tune Postbacks"
[20]: https://github.com/adjust/ios_sdk#9-implement-the-attribution-callback "Adjust SDK-to-SDK Integrations on iOS"
[21]: https://github.com/adjust/android_sdk#16-set-listener-for-attribution-changes "Adjust SDK-to-SDK Integrations on Android"
[22]: https://dev.branch.io/recipes/analytics_appboy/ "Branch Webhooks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
