---
nav_title: Branch for attribution
article_title: Branch for Attribution
alias: /partners/branch_for_attribution/
description: "This reference article outlines the partnership between Braze and Branch, a mobile linking platform that helps you acquire, engage, and measure across all devices, channels, and platforms."
page_type: partner
search_tag: Partner
---

# Branch for attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints.

_This integration is maintained by Branch._

## About the integration

The Braze and Branch integration will help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust attribution and [deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).

## Prerequisites

| Requirement | Description |
|---|---|
| Branch account | A Branch account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Branch SDK | In addition to the required Braze SDK, you must install the [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map device IDs

#### Android 

If you have an Android app, you will need to pass a unique Braze device ID to Branch. This ID can be set in the Branch SDK's `setRequestMetadataKey()` method. The following code snippet must be included before calling `initSession`. You must also initialize the Braze SDK before setting the request metadata in the Branch SDK.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Prior to February 2023, our Branch attribution integration used the IDFV as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and sent to Branch upon install as there will be no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Branch upon app install in order for Braze to appropriately match iOS attributions.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Branch**. 

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Branch's dashboard.<br><br>![This image shows the "Data Import for Install Attribution" box found in the Branch technology page. In this box, you are shown the data import key and the REST endpoint.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### Step 3: Set up data feeds

1. In Branch, under the **Exports** section, select **Data Feeds**.
2. On the **Data Feeds Manager** page, select the **Data Integrations** tab at the top of the page. 
3. Select Braze from the list of available data partners. 
4. On the Braze export page, provide the data import key and REST endpoint that you found in the Braze dashboard and select **Enable**.

### Step 4: Confirm the integration

Once Braze receives attribution data from Branch, the status connection indicator on the Branch technology partners page in Braze will change from "Not Connected" to "Connected". A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Branch postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Branch click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Branch click tracking links, visit their [documentation](https://help.branch.io/using-branch/docs/ad-links). You can insert the Branch click tracking links into your Braze campaigns directly. Branch will then use their [probabilistic attribution methodologies](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) to attribute the user that has clicked on the link. We recommend appending your Branch tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs local %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Branch SDK integration. You can include the GAID in your Branch click tracking links by utilizing the following Liquid logic:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Branch automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Branch click tracking links by utilizing the following Liquid logic:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**This recommendation is purely optional**<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Branch will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}


