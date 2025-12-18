---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "This reference article outlines the partnership between Braze and Singular, a unified marketing analytics platform that allows you to import paid install attribution data."
page_type: partner
search_tag: Partner

---

# Singular

> [Singular](https://www.singular.net/) is a unified marketing analytics platform that delivers attribution, cost aggregation, marketing analytics, creative reporting, and workflow automation.

_This integration is maintained by Singular._

## About the integration

The Braze and Singular integration allows you to import paid install attribution data to segment intelligently within your lifecycle campaigns.

## Prerequisites

| Requirement | Description |
|---|---|
| Singular account | A Singular account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Singular SDK | In addition to the required Braze SDK, you must install the [Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map user IDs

#### Android

If you have an Android app, you will need to include the following code snippet, which passes a unique Braze user ID to Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Prior to February 2023, our Singular attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and send it to Singular upon install because there is no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Singular upon app install in order for Braze to appropriately match iOS attributions.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Singular**. 

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. 

You will need to provide the data import key and REST endpoint to your Singular account manager to complete the integration.<br><br>![This image shows the "Data Import for Install Attribution" box found in the Singular technology page. In this box, you are shown the data import key and the REST endpoint.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### Step 3: Confirm the integration

Once Braze receives attribution data from Singular, the status connection indicator on the Singular technology partners page in Braze will change from "Not Connected" to "Connected". A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Singular postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Singular click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Singular click tracking links, visit their [documentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). You can insert the Singular click tracking links into your Braze campaigns directly. Singular will then use their [probabilistic attribution methodologies](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) to attribute the user that has clicked on the link. We recommend appending your Singular tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs local %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Singular SDK integration. You can include the GAID in your Singular click tracking links by utilizing the following Liquid logic:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Singular automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Singular click tracking links by utilizing the following Liquid logic:

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
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Singular will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}


