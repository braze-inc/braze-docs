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

> [Branch](https://docs.branch.io/pages/integrations/braze/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints. This article will walk you through how to use Branch with Braze to support your attribution needs.

Branch and Braze help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust attribution and [deep linking]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/).

## Integration

### Step 1: Integration requirements

* This integration supports iOS and Android.
* Your app will need Braze's SDK and Branch's SDK installed.

{% tabs %}
{% tab Android %}
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to Branch. You must set the correct key before calling `initSession`. You must also initialize the Braze SDK before setting the request metadata in the Branch SDK.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).getInstallTrackingId());

...

Branch.initSession(...);
```
{% endtab %}
{% tab iOS %}

If you have an iOS app, your IDFV will be collected by Branch and sent to Braze. This ID will then be mapped to a unique device ID in Braze.

Braze will still store IDFA values for users that have opted-in if you are collecting the IDFA with Braze, as described in our [iOS 14 Upgrade Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Otherwise, the IDFV will be used as a fallback identifier to map users.

{% endtab %}
{% endtabs %}

### Step 2: Getting the Braze data import key

In your Braze account, navigate to "Attribution" under "Technology Partners" and select "Branch". Here, you will find the REST Endpoint and generate your Braze Data Import Key. Once generated, you will be able to create a new key, or invalidate an existing one as needed. The Data Import Key and the REST Endpoint are used in the next step when setting up a postback in Branch's dashboard.<br><br>![Branch Image][4]{: style="max-width:70%;"}

### Step 3: Setting up a webhook from Branch

Follow [these instructions][22] to add a webhook in Branch's dashboard. You will be prompted for the key and REST Endpoint that you found in Braze's dashboard in Step 2.

### Step 4: Confirming the integration

Once Braze receives attribution data from Branch, the status connection indicator on "Technology Partners", then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter attribution data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners __cannot send that data to Braze__.

## Branch click tracking URls in Braze (optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Branch click tracking links, visit their [documentation](https://help.branch.io/using-branch/docs/ad-links). You can insert the Branch click tracking links into your Braze campaigns directly. Branch will then use their [probabilistic attribution methodologies](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) to attribute the user that has clicked on the link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your Branch tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Branch SDK integration. You can include the GAID in your Branch click tracking links by utilizing the Liquid logic below:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Branch automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Branch click tracking links by utilizing the Liquid logic below:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Branch will still be able to attribute these clicks through their probabilistic modeling.

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"
[4]: {% image_buster /assets/img/attribution/branch.png %}

