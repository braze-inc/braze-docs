---
nav_title: AppsFlyer
alias: /partners/appsflyer/

description: "This article outlines the partnership between Braze and AppsFlyer, a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps."
page_type: partner

---

# AppsFlyer

{% include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking.

Build more holistic marketing campaigns by leveraging mobile install attribution data from AppsFlyer. With AppsFlyer and Braze, you can pass install attribution data to Braze to better understand how to optimize your campaigns.

## Integration

### Step 1: Integration Requirements

{% alert important %}
As of March 4th, 2019, AppsFlyer requires that the Activate Partner toggle be switched to "on" for every integrated partner, including Braze. Please be sure that your toggle is flipped on from your AppsFlyer dashboard.
{% endalert %}

* This integration supports iOS and Android apps.
* If you expect more than 100 attributed installs per hour, you will need a Braze Enterprise account. See [API Restrictions][5] for more information.
* Your app will need Braze's SDK and AppsFlyer's SDK installed.
* If you have an iOS app, you will need to [enable IDFA collection][13] in Braze's SDK.
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to AppsFlyer. For most setups, this code should be included alongside all calls to `AppsFlyerLib.setAppsFlyerKey`, typically in an activity's `onCreate` callback.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId = Appboy.getInstance(context).getInstallTrackingId();
customData.put("customData", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

### Step 2: Getting the Braze API Key

In your Braze account, navigate to "Technology Partners" , then "Attribution" and find the API key and REST Endpoint in the AppsFlyer section. The API key and the REST Endpoint are used in the next step when setting up a postback in Appsflyer's dashboard.

### Step 3: Configure Braze in Appsflyer's Dashboard

- In Appsflyer's dashboard, navigate to the "Integrated Partners" page.
- On that page, search for Braze and click on Braze's logo to open up a configuration window.
- Under "Integration Parameters" select "enable".
- Copy the Braze API key (obtained in the prior step) into the "API_key" field.
- Copy the Braze Rest Endpoint url (obtained in the prior step) into the "REST_endpoint" field.
- Click "Save & Close".

Additional information on these instructions is available in [Appsflyer's documentation][16].

Braze maps AppsFlyer's data fields to segment filters in the following way

| AppsFlyer Data Field | Braze Segment Filter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |

### Step 4: Confirming the Integration

Once Braze receives attribution data from AppsFlyer, the status connection indicator on ["Technology Partners" , then "Attribution"][14] will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded by the AppsFlyer integration, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook, Snapchat, and Twitter Attribution Data

Attribution data for Facebook, Snapchat, and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third-parties and, therefore, our partners __cannot send that data to Braze__.

For more information, please see Appsflyer's [documentation][31].

[5]: #api-restrictions
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
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
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
