---
nav_title: Branch
alias: /partners/branch_for_attribution/

description: "This article outlines the partnership between Braze and Branch, a mobile linking platform that helps you acquire, engage, and measure across all devices, channels, and platforms."
page_type: partner

---

# Branch for Attribution {#branch}

{% include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints. This article will walk you through how to use Branch with Braze to support your attribution needs.

Branch and Braze help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust attribution and [deep linking]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/).

## Integration

### Step 1: Integration Requirements

* This integration supports iOS and Android.
* Your app will need Braze's SDK and Branch's SDK installed.

{% tabs %}
{% tab Android %}
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to Branch. You must set the correct key before calling `initSession`. You must also initialize the Braze SDK before setting the request metadata in the Branch SDK.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Appboy.getInstance(context).getInstallTrackingId());

...

Branch.initSession(...);
```
{% endtab %}
{% tab iOS %}
If you have an iOS app, you will need to include the code snippet below, which passes the customer's IDFV to Branch. This ID will then be mapped to a unique device ID in Braze.

```
Code Snippet TBA
```

{% alert important %}
As of MM/DD/YYYY, we're recommending that all customers use the Braze `device_id` instead of the IDFA. This is in response to Apple's changes to the [IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa) as part of the iOS 14 update.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 2: Getting the Attribution ID

In your Braze account, navigate to "Technology Partners", then "Attribution" and find the API key and REST Endpoint in the Branch section. The API key and the REST Endpoint are used in the next step when setting up a webhook in Branch's dashboard.

### Step 3: Setting Up A Webhook from Branch

Follow [these instructions][22] to add a webhook in Branch's dashboard. You will be prompted for the key and REST Endpoint that you found in Braze's Dashboard in Step 2.

### Step 4: Confirming the Integration

Once Braze receives attribution data from Branch, the status connection indicator on "Technology Partners", then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners __cannot send that data to Braze__.

[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-limits
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection "IDFA Collection"
[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"
