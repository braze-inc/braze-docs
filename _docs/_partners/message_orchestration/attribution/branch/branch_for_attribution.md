---
nav_title: Branch for Attribution
article_title: Branch for Attribution
alias: /partners/branch_for_attribution/
description: "This article outlines the partnership between Braze and Branch, a mobile linking platform that helps you acquire, engage, and measure across all devices, channels, and platforms."
page_type: partner
search_tag: Partner

---

# Branch for attribution {#branch}

{% include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints.

The Braze and Branch integration will help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust attribution and [deep linking]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/).

## Prerequisites

| Requirement | Description |
|---|---|
| Branch account | A Branch account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Branch SDK | In addition to the required Braze SDK, you must install the [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Map device IDs

#### Android 

If you have an Android app, you will need to pass a unique Braze device ID to Branch. This ID can be set in the Branch SDK's `setRequestMetadataKey()` method. The following code snippet must be included before calling `initSession`. You must also initialize the Braze SDK before setting the request metadata in the Branch SDK.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).getInstallTrackingId());

...

Branch.initSession(...);
```
#### iOS

If you have an iOS app, your IDFV will be collected by Branch and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

### Step 2: Get the Braze data import key

In Braze, navigate to **Attribution** under **Technology Partners** and select **Branch**. Here, you will find the REST Endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Branch's dashboard.<br><br>![Branch Image][4]{: style="max-width:90%;"}

### Step 3: Set up data feeds

1. In Branch, under the **Exports** section, click **Data Feeds**.
2. On the **Data Feeds Manager** page, click the **Data Integrations** tab at the top of the page. 
3. Select Braze from the list of available data partners. 
4. On the Braze export page, provide the data import key and REST endpoint that you found in Braze's dashboard and click **Enable**.

### Step 4: Confirm the integration

Once Braze receives attribution data from Branch, the status connection indicator on the Branch technology partners page in Braze will change to green. A timestamp of the last successful request will also be included. 

Note that this will not happen until we receive data about an attributed install. Organic installs, which should be excluded from the Branch postback, are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter attribution data

Attribution data for Facebook and Twitter campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Branch click tracking URLs in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Branch click tracking links, visit their [documentation](https://help.branch.io/using-branch/docs/ad-links). You can insert the Branch click tracking links into your Braze campaigns directly. Branch will then use their [probabilistic attribution methodologies](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) to attribute the user that has clicked on the link. We recommend appending your Branch tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Branch SDK integration. You can include the GAID in your Branch click tracking links by utilizing the Liquid logic below:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Branch automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Branch click tracking links by utilizing the Liquid logic below:

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
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Branch will still be able to attribute these clicks through their probabilistic modeling.
{% endalert %}

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"
[4]: {% image_buster /assets/img/attribution/branch.png %}