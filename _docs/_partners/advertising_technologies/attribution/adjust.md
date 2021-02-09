---
nav_title: Adjust
alias: /partners/adjust/

description: "This article outlines the partnership between Braze and Adjust, a mobile attribution and analytics company that combines attribution for advertising sources."
page_type: partner
---

# Adjust

> [Adjust](https://www.adjust.com/) is a mobile attribution and analytics company that combines attribution for advertising sources with advanced analytics for a comprehensive picture of business intelligence.

Adjust allows you to import non-organic install attribution data to segment more intelligently within your lifecycle campaigns.

## Requirements

This integration supports iOS and Android apps.

| Requirement | Description |
|---|---|
| Braze SDK | Be sure to enable the proper SDK for your needs - either [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) or [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).|
| Braze API Key & REST Endpoint | In your Braze account, navigate to Technology Partners and search for Adjust. There, you'll be able to find your rest endpoint and generate a Data Import Key. The Data Import Key and REST Endpoint will be used to set up a postback in Adjust’s dashboard. |
| Adjust SDK | Please see the [Adjust docs](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk) for more information on this requirement. |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Android %}

If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device ID to Adjust. You should call the following before initializing the SDK on `Adjust.onCreate.`:

```
Adjust.addSessionPartnerParameter("braze_device_id", Appboy.getInstance(getApplicationContext()).getInstallTrackingId()););
```
{% endtab %}
{% tab iOS %}

If you have an iOS app, your IDFV will be collected by Adjust and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% endtab %}
{% endtabs %}

{% alert note %}
If you are planning to send post-install events from Adjust into Braze, you will need to: <br><br>1) Ensure that you append `external_id` as a session and event parameter within the Adjust SDK. For revenue event forwarding, you will need to set up `product_id` as a parameter for events. For more information on defining partner parameters for event forwarding see [Adjust’s documentation](https://github.com/adjust/sdks).<br><br>2) Generate a new API key to input into Adjust. This can be done by selecting the __Generate API Key__ button found within the Adjust partner section of the Braze dashboard.<br><br>![Adjust Image]({% image_buster /assets/img/attribution/adjust2.png %}){: style="max-width:70%;"}
{% endalert %}

## Integration

To integrate Braze with Adjust, you must configure Braze in Adjust's dashboard.

1. In Adjust’s dashboard, navigate to __App Settings__ and navigate to __Partner Setup__, then __Add Partners__.<br><br>
2. Select __Braze (formerly Appboy)__.<br><br>
3. Copy the Braze Data Import Key into the `Install API Key` field.<br><br>This Data Import Key is available in the Braze Dashboard. This can be found by navigating to __Technology Partners__ under __Integrations__ and selecting __Adjust__. Here, you can generate a new key or invalidate an existing key. From here, the API you need is housed under the __Data Import for Install Attribution__ section.<br><br>![Adjust Image][1]{: style="max-width:70%;"}<br><br>
4. Copy your specific Braze REST Endpoint into the `REST_endpoint` field.<br><br>
5. Click __Save & Close__.

### Attribution Parameters

Assuming you configure your integration as suggested above, Braze will map Adjust's data to segment filters as described below.

| Adjust Attribution Parameter | Braze Segment Filter |
| --- | --- |
| {network_name} | Attributed Source |
| {campaign_name} | Attributed Campaign |
| {adgroup_name} | Attributed Adgroup |
| {creative_name} | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2}


{% alert important %}
  At this time, Braze only receives non-organic install attribution data from these attribution partners. This means that organic data will **not** appear as an attributed source within Braze.
{% endalert %}

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. Facebook and Twitter do not permit their partners to share attribution data with third parties and, therefore, our partners __cannot send that data to Braze__.

## Adjust Click Tracking URLs in Braze (Optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Adjust click tracking links, visit their [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). You can insert the Adjust click tracking links into your Braze campaigns directly. Adjust will then use their [probabilistic attribution methodologies](https://www.adjust.com/blog/attribution-compatible-with-ios14/) to attribute the user that has clicked on the link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your Adjust tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Adjust SDK integration. You can include the GAID in your Adjust click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
gps_adid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Adjust automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Adjust click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Adjust will still be able to attribute these clicks through their probabilistic modeling.

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}

