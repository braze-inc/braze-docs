---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "This article outlines the partnership between Braze and Adjust, a mobile attribution and analytics company that lets you import non-organic install attribution data to segment more intelligently within your lifecycle campaigns."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) is a mobile attribution and analytics company that combines attribution for advertising sources with advanced analytics for a comprehensive picture of business intelligence.

The Braze and Adjust integration lets you import non-organic install attribution data to segment more intelligently within your lifecycle campaigns.

## Prerequisites

| Requirement | Description |
|---|---|
| Adjust account | An Adjust account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Adjust SDK | In addition to the required Braze SDK, you must install the [Adjust SDK](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Map device IDs

#### Android

If you have an Android app, you will need to pass a unique Braze device ID to Adjust. This ID can be set in the Adjust SDK's `addSessionPartnerParameter()` method. The following code snippet must be included before initializing the SDK on `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getInstallTrackingId()););
```

#### iOS 

If you have an iOS app, your IDFV will be collected by Adjust and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% alert note %}
If you are planning to send post-install events from Adjust into Braze, you will need to: <br><br>1) Ensure that you append `external_id` as a session and event parameter within the Adjust SDK. For revenue event forwarding, you will also need to set up `product_id` as a parameter for events. Visit [Adjust’s documentation](https://github.com/adjust/sdks) for more information on defining partner parameters for event forwarding.<br><br>2) Generate a new API key to input into Adjust. This can be done by selecting the **Generate API Key** button found within the Adjust partner page in the Braze dashboard.
{% endalert %}

### Step 2: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Adjust**. Here, you will find the REST Endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Adjust's dashboard.<br><br>![This image shows the "Data Import for Install Attribution" box found in the Adjust technology page. In this box, you are shown the data import key and the REST endpoint.][1]{: style="max-width:90%;"}

### Step 3: Configure Braze in Adjust

1. In Adjust’s dashboard, navigate to **App Settings** and navigate to **Partner Setup**, then **Add Partners**.
2. Select **Braze (formerly Appboy)** and provide the data import key and Braze REST endpoint.
3. Click **Save & Close**.

### Step 4: Confirm the integration

Once Braze receives attribution data from Adjust, the status connection indicator on the Adjust technology partners page in Braze will change from "Not Connected" to "Connected". A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Adjust postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Available data fields

Assuming you configure your integration as suggested, Braze will map Adjust's data to segment filters as described in the following table.

| Adjust data field | Braze segment filter |
| --- | --- |
| `{network_name}` | Attributed Source |
| `{campaign_name}` | Attributed Campaign |
| `{adgroup_name}` | Attributed Adgroup |
| `{creative_name}` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2}

## Facebook and Twitter attribution data

Attribution data for Facebook and Twitter campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Adjust click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Adjust click tracking links, visit their [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). You can insert the Adjust click tracking links into your Braze campaigns directly. Adjust will then use their [probabilistic attribution methodologies](https://www.adjust.com/blog/attribution-compatible-with-ios14/) to attribute the user that has clicked on the link. We recommend appending your Adjust tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Adjust SDK integration. You can include the GAID in your Adjust click tracking links by utilizing the following Liquid logic:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Adjust automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Adjust click tracking links by utilizing the following Liquid logic:

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
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Adjust will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}