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
As of March 4, 2019, AppsFlyer requires that the Activate Partner toggle be switched to "on" for every integrated partner, including Braze. Please be sure that your toggle is flipped on from your AppsFlyer dashboard.
{% endalert %}

* This integration supports iOS and Android apps.
* Your app will need Braze's SDK and AppsFlyer's SDK installed.

{% tabs local %}
{% tab Android %}

If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to AppsFlyer. For most setups, this code should be included alongside all calls to `AppsFlyerLib.Instance.StartTracking`, typically in an activity's `onCreate` callback.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId = Appboy.getInstance(context).getInstallTrackingId();
customData.put("customData", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```
{% endtab %}
{% tab iOS %}

If you have an iOS app, your IDFV will be collected by AppsFlyer and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% endtab %}
{% tab Unity %}

```
CopiedAppboy.AppboyBinding.GetInstallTrackingId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.GetInstallTrackingId());
AppsFlyer.setAdditionalData(customData);
```

{% endtab %}
{% endtabs %}

### Step 2: Getting the Braze Data Import Key

In your Braze account, navigate to __Attribution__ under __Technology Partners__ and select __AppsFlyer__. Here, you will find the REST Endpoint and generate your Braze Data Import Key. Once generated, you will be able to create a new key, or invalidate an existing one. The Data Import Key and the REST Endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![AppsFlyer Image][4]{: style="max-width:70%;"}

### Step 3: Configure Braze in AppsFlyer's Dashboard

In AppsFlyer's dashboard, navigate to the __Integrated Partners__ page on the left bar. From here, search for __Braze__ and click on Braze's logo to open up a configuration window.
![AppsFlyer][1]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;margin-top:15px"}

Within the __Integration__ tab, switch on __Activate Partner__, copy the Data Import Key into the `API_key` field, add your Braze REST Endpoint URL into the `REST Endpoint` field. Finally, save your configuration.

Additional information on these instructions is available in [AppsFlyer's documentation][16].

Once you have saved the configuration, AppsFlyer sends the following data to Braze for every organic and non-organic install. Below, you can view how Braze maps AppsFlyer's data fields to specific segment filters.

| AppsFlyer Data Field | Braze Segment Filter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2}

### Step 4: Confirming the Integration

Once Braze receives attribution data from AppsFlyer, the status connection indicator on __Technology Partners__, then __Attribution__ will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded by the AppsFlyer integration, are ignored by our API and are not counted when determining if a successful connection was established.

### Step 5: Viewing User Attribution Data

Your user-base can be segmented by attribution data in the Braze dashboard using the Install Attribution filters.

![User Attributes 1][2]{: style="max-width:80%;margin-right:15px;"} 

Additionally, attribution data for a particular user is available on each user’s profile in the Braze Dashboard.

## Facebook, Snapchat, and Twitter Attribution Data

Attribution data for Facebook, Snapchat, and Twitter campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

For more information, please see AppsFlyer's [documentation][31].

## Email Deep Linking and Click Tracking

Deep links, links that direct users toward a specific page or place within an app or website, are crucial in creating a tailored user experience. While widely used, often issues come up when using them in tandem with click tracking, another vital feature used in collecting user data. These issues are due to ESPs (Email Service Providers) wrapping deep links in their own click recording domain, breaking the original link. 

There are, however, ESPs like Sendgrid that support both universal linking and click tracking. Braze recommends integrating OneLink-based attribution links into your SendGrid email system in order to seamlessly deep link from emails. To get started, check out AppsFlyer's [documentation][3].

### Click Tracking URLs in Braze (Optional)

You can use AppsFlyer's [OneLink attribution links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) in Braze campaigns across push, email, and more. This allows you to be able to send back install or re-engagement attribution data from their Braze campaigns into AppsFlyer. As a result, you will be able to holistically see the impact of your paid and owned channels in a single platform.

You can simply create your OneLink tracking URL in AppsFlyer and insert it into your Braze campaigns directly. AppsFlyer will then use their [probabilistic attribution methodologies](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) to attribute the user that has clicked on the link or deep link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your AppsFlyer tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the AppsFlyer SDK integration. You can include the GAID in your AppsFlyer click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
advertising_id={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and AppsFlyer automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your AppsFlyer click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
device_id={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, AppsFlyer will still be able to attribute these clicks through their probabilistic modeling.

[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}

