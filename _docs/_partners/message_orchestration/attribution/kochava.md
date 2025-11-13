---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "This reference article outlines the partnership between Braze and Kochava, a mobile attribution platform that offers attribution and analytics insights to help you harness your data for growth."
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochava](https://www.kochava.com/) offers mobile attribution and analytics to help you harness your data for growth. The Kochava Audience Platform enables you to plan, target, activate, measure, and optimize your app campaigns.

_This integration is maintained by Kochava._

## About the integration

The Braze and Kochava integration helps power a more holistic understanding of your campaigns by sending attribution data to Braze to better understand what campaigns are driving installs, in-app activity, and more.

## Prerequisites

| Requirement | Description |
|---|---|
| Kochava account | A Kochava account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Kochava SDK | In addition to the required Braze SDK, you must install the [Kochava SDK](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map user IDs

#### Android

The [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generates a Globally Unique Identifier (GUID) as the Braze ID on session start. This identifier should be passed into the Kochava `IdentityLink` method so Braze can reconcile the data back to the correct user profile. Retrieve the Braze ID with the following method:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Prior to February 2023, our Kochava attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and send it to Kochava upon install because there is no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Kochava upon app install in order for Braze to appropriately match iOS attributions.

Braze has two APIs that will produce the same value, one with a completion handler and another using the new Swift concurrency support. Note that you will need to modify the following code snippets to conform with Kochava's [iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/) instructions. For additional help, contact Kochava support.

##### Completion handler
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Swift concurrency
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Kochava**. 

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kochava's dashboard.<br><br>![This image shows the "Data Import for Install Attribution" box found in the Kochava technology page. In this box, you are shown the data import key and the REST endpoint.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Step 3: Set up a postback from Kochava

[Add a postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) in your Kochava dashboard. You will be prompted for the data import key and REST endpoint that you found in the Braze dashboard.

### Step 4: Confirm the integration

Once Braze receives attribution data from Kochava, the status connection indicator on the Kochava technology partners page in Braze will change from "Not Connected" to "Connected". A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Kochava postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Kochava click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Kochava click tracking links, visit their [documentation](https://support.kochava.com/reference-information/attribution-overview/). You can insert the Kochava click tracking links into your Braze campaigns directly. Kochava will then use their [probabilistic attribution methodologies](https://www.kochava.com/getting-prepared-for-ios-14/) to attribute the user that has clicked on the link. We recommend appending your Kochava tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs local %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Kochava SDK integration. You can include the GAID in your Kochava click tracking links by utilizing the following Liquid logic:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Kochava automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Kochava click tracking links by utilizing the following Liquid logic:

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
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Kochava will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}


