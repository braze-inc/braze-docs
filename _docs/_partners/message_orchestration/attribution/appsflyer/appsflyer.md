---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "This reference article outlines the partnership between Braze and AppsFlyer, a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking.

The Braze and AppsFlyer integration allows you to better understand how to optimize and build more holistic campaigns by leveraging mobile install attribution data from AppsFlyer.

## Prerequisites

| Requirement | Description |
|---|---|
| AppsFlyer account | An AppsFlyer account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| AppsFlyer SDK | In addition to the required Braze SDK, you must install the [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Map device ID

#### Android

If you have an Android app, you will need to pass a unique Braze device ID to AppsFlyer. 

Make sure the following lines of code are inserted at the correct place—after the Braze SDK is launched and before the initialization code for the AppsFlyer SDK. See the AppsFlyer [Android SDK integration guide](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) for more information.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId =(Braze.getInstance(MyActivity.this).getDeviceId());
customData.put("brazeCustomerId", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

#### iOS

{% alert important %}
Prior to February 2023, our AppsFlyer attribution integration used the IDFV as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and sent to AppsFlyer upon install as there will be no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to AppsFlyer upon app install in order for Braze to appropriately match iOS attributions.

{% tabs local %}
{% tab Objective-C %}

```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[braze deviceIdWithCompletion:^(NSString * _Nonnull brazeDeviceId) {
    NSLog(@">>[BRZ]: %@", brazeDeviceId);
    [[AppsFlyerLib shared] setAdditionalData:@{
        @"brazeDeviceId": brazeDeviceId
    }];
}];
```

{% endtab %}
{% tab Swift %}

##### Swift completion handler
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
braze.deviceId {
    brazeDeviceId in
    AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
}
```
##### Swift await
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
let brazeDeviceId = await braze.deviceId()
AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
```

{% endtab %}
{% endtabs %}

#### Unity

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **AppsFlyer**. 

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Technology Partners** under **Integrations**.
{% endalert %}

Here, you will find the REST endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![The "Data Import for Install Attribution" box available on the AppsFlyer Technology page. Included in this box is the data import key and the REST endpoint.][4]{: style="max-width:70%;"}

### Step 3: Configure Braze in AppsFlyer's dashboard

1. In AppsFlyer, navigate to the **Integrated Partners** page on the left bar. Next, search for **Braze** and click on Braze's logo to open up a configuration window.
2. Within the **Integration** tab, switch on **Activate Partner**.
3. Provide the data import key and REST endpoint that you found in Braze's dashboard. 
4. Toggle **Advanced Privacy** off and save your configuration.

Additional information on these instructions is available in [AppsFlyer's documentation][16].

### Step 4: Confirm the integration

Once Braze receives attribution data from AppsFlyer, the status connection indicator on the AppsFlyer technology partners page in Braze will change from "Not Connected" to "Connected". A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the AppsFlyer postback, are ignored by our API and are not counted when determining if a successful connection was established.

### Step 5: Viewing user attribution data

#### Available data fields

Assuming you configure your integration as suggested, Braze will map all organic and non-organic install data to segment filters.

| AppsFlyer data field | Braze segment filter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2}

Your user base can be segmented by attribution data in the Braze dashboard using the Install Attribution filters.

![Four available filters. The first is "Install Attribution Source is network_val_0". The second is "Install Attribution Source is campaign_val_0". The third is "Install Attribution Source is adgroup_val_0". The fourth is "Install Attribution Source is creative_val_0". Beside the listed filters, you can see how these attribution sources will be added to the user profile. In the "Install Attribution" box on a user's information page, Install Source is listed as network_val_0, campaign is listed as campaign_val_0, etc.][2]

Additionally, attribution data for a particular user is available on each user's profile in the Braze dashboard.

## Facebook, Snapchat, and Twitter attribution data

Attribution data for Facebook and Twitter campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Email deep linking and click tracking

Deep links, links that direct users toward a specific page or place within an app or website, are crucial in creating a tailored user experience. While widely used, issues often come up when using them with click tracking, another vital feature used in collecting user data. These issues are due to ESPs (Email Service Providers) wrapping deep links in their own click recording domain, breaking the original link. 

There are, however, ESPs like SendGrid that support both universal linking and click tracking. Braze recommends integrating [OneLink-based attribution links][3] into your SendGrid or [SparkPost](https://support.appsflyer.com/hc/en-us/articles/360014381317-SparkPost-integration-with-AppsFlyer) email system to seamlessly deep link from emails.

### AppsFlyer click tracking URLs in Braze (optional)

You can use AppsFlyer's [OneLink attribution links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) in Braze campaigns across push, email, and more. This allows you to send back install or re-engagement attribution data from their Braze campaigns into AppsFlyer. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

You can simply create your OneLink tracking URL in AppsFlyer and directly insert it into your Braze campaigns. AppsFlyer will then use their [probabilistic attribution methodologies](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) to attribute the user that has clicked on the link. We recommend appending your AppsFlyer tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs local %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the AppsFlyer SDK integration. You can include the GAID in your AppsFlyer click tracking links by utilizing the following Liquid logic:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and AppsFlyer automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your AppsFlyer click tracking links by utilizing the following Liquid logic:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**This recommendation is purely optional**<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, AppsFlyer will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}

[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
