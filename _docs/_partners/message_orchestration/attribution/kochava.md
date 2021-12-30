---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "This article outlines the partnership between Braze and Kochava, a mobile attribution platform that offers attribution and analytics insights to help you harness your data for growth."
page_type: partner
search_tag: Partner

---

# Kochava

> Kochava offers mobile attribution and analytics to help you harness your data for growth. The Kochava Audience Platform enables you to plan, target, activate, measure, and optimize your app campaigns.

The Braze and Kochava integration helps power a more holistic understanding of your campaigns by sending attribution data to Braze to better understand what campaigns are driving installs, in-app activity, and more.

## Prerequisites

| Requirement | Description |
|---|---|
| Kochava account | A Kochava account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Kochava SDK | In addition to the required Braze SDK, you must install the [Kochava SDK](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Map user IDs

#### Android

The [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generates a GUID as the Braze ID on session start. This is the identifier we recommend passing into the Kochava `IdentityLink` method as it allows Braze to reconcile the data back to the correct user profile. The Braze ID can be retrieved using the following method:

```java
Apppboy.getInstance(context).getDeviceId();
```
#### iOS

If you have an iOS app, your IDFV will be collected by Kochava and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

### Step 2: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Kochava**. Here, you will find the REST Endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kochava's dashboard.<br><br>![Kochava Image][4]{: style="max-width:90%;"}

### Step 3: Set up a postback from Kochava

[Add a postback][18] in your Kochava dashboard. You will be prompted for the data import key and REST endpoint that you found in Braze's dashboard.

### Step 4: Confirm the integration

Once Braze receives attribution data from Kochava, the status connection indicator on the Kochava technology partners page in Braze will change to green. A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Kochava postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter attribution data

Attribution data for Facebook and Twitter campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Kochava click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Kochava click tracking links, visit their [documentation](https://support.kochava.com/reference-information/attribution-overview/). You can insert the Kochava click tracking links into your Braze campaigns directly. Kochava will then use their [probabilistic attribution methodologies](https://www.kochava.com/getting-prepared-for-ios-14/) to attribute the user that has clicked on the link. We recommend appending your Kochava tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Kochava SDK integration. You can include the GAID in your Kochava click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Kochava automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Kochava click tracking links by utilizing the Liquid logic below:

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
__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Kochava will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}