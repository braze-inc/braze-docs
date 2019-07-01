---
nav_title: Branch
alias: /partners/branch_for_attribution/
---

# Branch
[Branch](https://docs.branch.io/pages/integrations/braze/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touch points.

Branch and Braze help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust attribution and deep linking.

## Integration

### Step 1: Integration Requirements

* This integration supports iOS and Android.
* If you expect more than 100 attributed installs per hour, you will need a Braze Enterprise account. See [API Restrictions][5] for more information.
* Your app will need Braze's SDK and Branch's SDK installed.
* You will need to [enable IDFA collection][13] in Braze's SDK.
* If you have an Android app, you will need to include the code snippet below, which passes a unique Braze device id to Branch. You must set the correct key before calling `initSession`. You must also initialize the Braze SDK before setting the request metadata in the Branch SDK.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Appboy.getInstance(this).getInstallTrackingId());

...

Branch.initSession(...);
```

### Step 2: Getting the Attribution ID

In your Braze account, navigate to "Technology Partners" , then "Attribution" and find the API key and REST Endpoint in the Branch section. The API key and the REST Endpoint are used in the next step when setting up a webhook in Branch's dashboard.

### Step 3: Setting Up A Webhook from Branch

Follow [these instructions][22] to add a webhook in Branch's dashboard. You will be prompted for the key and REST Endpoint that you found in Braze's Dashboard in Step 2.

### Step 4: Confirming the Integration

Once Braze receives attribution data from Branch, the status connection indicator on "Technology Partners" , then "Attribution" will change to green and a timestamp of the last successful request will be included. Note that this will not happen until we receive data about an __attributed__ install. Organic installs are ignored by our API and are not counted when determining if a successful connection was established.

## Facebook and Twitter Attribution Data

Attribution data for Facebook and Twitter campaigns is __not available through our partners__. These media sources do not permit their partners to share attribution data with third-parties and, therefore, our partners __cannot send that data to Braze__.

[5]: {{ site.baseurl }}/developer_guide/rest_api/basics/#api-limits
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection "IDFA Collection"
[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"
