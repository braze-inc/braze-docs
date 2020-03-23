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
| Braze SDK | Be sure to enable the proper SDK for your needs - either [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) or [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).|
| Braze API Key & REST Endpoint | In your Braze account, navigate to Technology Partners and search for Adjust. There, you'll find the Install API Key and the REST Endpoint. The Install API Key and REST Endpoint will used to set up a postback in Adjust’s dashboard. |
| Adjust SDK | Please see the [Adjust docs](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk) for more information on this requirement. |
| Enable IDFA Collection in Braze SDK | [IDFA Collection]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection) is optional within the Braze SDK and disabled by default. This is required to be enabled for all of our Attribution partner integrations. |
{: .reset-td-br-1 .reset-td-br-2}

If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device ID to Adjust. You should call the following before initializing the SDK on `Adjust.onCreate.`:

```
Adjust.addSessionPartnerParameter("braze_device_id", Appboy.getInstance(getApplicationContext()).getDeviceId()););
```

{% alert note %}
If you are planning to send post-install events from Adjust into Braze, you will need to ensure that you append `external_id` as a session and event parameter within the Adjust SDK. For revenue event forwarding, you will need to set up `product_id` as parameter for events. For more information on defining partner parameters for event forwarding see [Adjust’s documentation](https://github.com/adjust/sdks).
{% endalert %}

## Integration

To integrate Braze with Adjust, you must configure Braze in Adjust's dashboard.

1. In Adjust’s dashboard, navigate to __App Settings__ and navigate to __Partner Setup__, then __Add Partners__.
2. Select __Braze (formerly Appboy)__.
3. Copy the Braze API Key into the `Install API Key` field.
- There is a separate `Event API Key` field available in the Adjust dashboard. Please contact your success manager for more information.
4. Copy the Braze REST Endpoint into the `REST_endpoint` field.
5. Click __Save & Close__.



### Attribution Parameters

Assuming you configure your integration as suggested above, Braze will map Adjust's data to segment filters as described below.

| Adjust Attribution Parameter | Braze Segment Filter |
| --- | --- |
| {network_name} | Attributed Source |
| {campaign_name} | Attributed Campaign |
| {adgroup_name} | Attributed Adgroup |
| {creative_name} | Attributed Ad |


{% alert important %}
  At this time, Braze only receives non-organic install attribution data from these attribution partners. This means that organic data will **not** appear as an attributed source within Braze.
{% endalert %}

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. Facebook and Twitter do not permit their partners to share attribution data with third-parties and, therefore, our partners __cannot send that data to Braze__.
