---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "This article outlines the partnership between Braze and Kochava, which offers mobile attribution and analytics to help you harness your data for growth."
page_type: partner
search_tag: Partner

---

# Kochava

> kochava offers mobile attribution and analytics to help you harness your data for growth. the kochava audience platform enables you to plan, target, activate, measure, and optimize your app campaigns.

Kochava and Braze power a more holistic understanding of campaigns. Kochava sends attribution data to Braze to better understand what campaigns are driving installs, in-app activity, and more.

## Integration

### step 1: integration requirements

* This integration supports iOS and Android apps.
* Your app will need Braze's SDK and Kochava's SDK installed.

### Step 2: getting the braze data import key

In your Braze account, navigate to "Attribution" under "Technology Partners" and select "Kochava". Here, you will find the REST Endpoint and generate your Braze Data Import Key. Once generated, you will be able to create a new key, or invalidate an existing one as needed. The Data Import Key and the REST Endpoint are used in the next step when setting up a postback in Kochava's dashboard.<br><br>![Kochava Image][4]{: style="max-width:70%;"}

### Step 3: setting up a postback from kochava

Follow [these instructions][18] to add a postback in Kochava's dashboard. You will be prompted for the key and REST Endpoint that you found in Braze's dashboard in Step 2. 

### Step 4: confirming the integration

Once Braze receives attribution data from Kochava, the status connection indicator on "Technology Partners", then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs are ignored by our API and are not counted when determining if a successful connection was established.
<br><br>
__Note for [Android][29] and [Windows][30] Support__:<br>
If you are planning to leverage the server-side integration between Braze and Kochava, you will need to ensure that you utilize the `IdentityLink` method of the Kochava SDK to capture the Braze ID. The 'Braze ID' can be retrieved using the following method:

{% tabs local %}
{% tab JAVA %}
The [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generates a GUID as the Braze ID on session start. This is the identifier we recommend using to pass into the Kochava `IdentityLink` method as it allows Braze to reconcile the data back to the correct user profile. Please ensure that you instrument this method to pass the 'Braze ID' on SDK initialization to ensure it is available when Kochava is posting your data back to Braze via the server-side integration.

```java
Apppboy.getInstance(context).getDeviceId();
```
{% endtab %}
{% tab iOS %}

If you have an iOS app, your IDFV will be collected by Kochava and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% endtab %}
{% endtabs %}

## Facebook, Twitter and Snapchat Attribution Data

Attribution data for Facebook, Twitter, and Snapchat campaigns are __not available through our partners__. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners __cannot send that data to Braze__.

## Kochava click tracking urls in braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Kochava click tracking links, visit their [documentation](https://support.kochava.com/reference-information/attribution-overview/). You can insert the Kochava click tracking links into your Braze campaigns directly. Kochava will then use their [probabilistic attribution methodologies](https://www.kochava.com/getting-prepared-for-ios-14/) to attribute the user that has clicked on the link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your Kochava tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs local %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Kochava SDK integration. You can include the GAID in your Adjust click tracking links by utilizing the Liquid logic below:
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

__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Kochava will still be able to attribute these clicks through their probabilistic modeling.

[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
