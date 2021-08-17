---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "This article outlines the partnership between Braze and Singular, a unified marketing analytics platform."
page_type: partner
search_tag: Partner

---

# Singular

> Singular is a unified marketing analytics platform that delivers attribution, cost aggregation, creative reporting, and workflow automation.

Singular allows you to import paid install attribution data to segment more intelligently within your lifecycle campaigns.

## Integration

### Step 1: Integration Requirements

* This integration supports iOS and Android apps.
* Your app will need Braze's SDK and Singular's SDK installed.

{% tabs %}
{% tab Android %}
If you have an Android app, you will need to include the code snippet below, which passes a unique Braze user id to Singular. For most setups, 2 lines of code must be added in an app's `onCreate()` method immediately after Singular's `init` method or session start. Braze's `device_id` must be available when the first “App Open” event is sent to Singular.

```java
@Override
protected void onCreate(Bundle savedInstanceState)
{
    // Other code
    // Init Singular SDK
   Singular.init(context, config); // context is Application Context
   // Code For Braze
   String appboyDeviceId = Braze.getInstance(context).getInstallTrackingId();
   Singular.event("App Open", "appboyUserID", appboyDeviceId);
}
```
{% endtab %}
{% tab iOS %}

If you have an iOS app, your IDFV will be collected by Singular and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% endtab %}
{% endtabs %}

### Step 2: Getting the Braze Data Import Key

In your Braze account, navigate to "Attribution" under "Technology Partners" and select "Singular". Here, you will find the REST Endpoint and generate your Braze Data Import Key. Once generated, you will be able to create a new key, or invalidate an existing one as needed. You will need to provide the Data Import Key and your REST Endpoint to your Singular Account Manager for the integration to be completed.<br><br>![Singular Image][4]{: style="max-width:70%;"}

### Step 3: Confirming the Integration

Once Braze receives attribution data from Singular, the status connection indicator on "Technology Partners", then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs, which should be excluded from the Singular postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners __cannot send that data to Braze__.

## Singular Click Tracking URLs in Braze (Optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Singular click tracking links, visit their [documentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). You can insert the Singular click tracking links into your Braze campaigns directly. Singular will then use their [probabilistic attribution methodologies](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) to attribute the user that has clicked on the link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your Singular tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Singular SDK integration. You can include the GAID in your Adjust click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Singular automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Singular click tracking links by utilizing the Liquid logic below:

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
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Singular will still be able to attribute these clicks through their probabilistic modeling.

[4]: {% image_buster /assets/img/attribution/singular.png %}


