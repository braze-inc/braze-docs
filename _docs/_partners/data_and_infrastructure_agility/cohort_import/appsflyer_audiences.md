---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "This reference article outlines the partnership between Braze and AppsFlyer Audiences, a feature of the AppsFlyer platform that allows you to efficiently build and connect audience segments to partner networks."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> This article describes how to import user cohorts from AppsFlyer to Braze by using the [AppsFlyer Audiences][2] integration. For more information on integrating AppsFlyer and its other functionalities, such as mobile attribution see the main [AppsFlyer article][3].

## Prerequisites

| Requirement | Description |
|---|---|
| AppsFlyer account | An AppsFlyer account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| AppsFlyer SDK | In addition to the required Braze SDK, you must install the [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

### Step 1: Configure the AppsFlyer SDK

To use this integration, you must pass the user's Braze external ID to AppsFlyer using the `setPartnerData()` function of the AppsFlyer SDK:

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **AppsFlyer**. 

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Technology Partners** under **Integrations**.
{% endalert %}

Here, you will find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![The "Data Import Using Cohort Import" box on the AppsFlyer technology page. In this box, you are shown the data import key and the REST endpoint.][5]{: style="max-width:90%;"}

### Step 3: Configure a Braze connection in AppsFlyer Audiences

1. In [AppsFlyer Audiences][4], go to the **Connections** tab and click **Add partner connection**.
2. Select Braze as the partner and give the connection a name.
3. Provide the data import key and Braze REST endpoint.
4. Save the connection, and it will be available to link to any new or existing audience.

![The AppsFlyer audiences platform partner connection configuration page. The lower part of the images shows that the Braze external ID box is checked.][6]{: style="max-width:80%;"}

### Step 4: Using AppsFlyer Audiences cohorts in Braze

Once an AppsFlyer audience has been uploaded to Braze, you can use it as a filter when defining segments in Braze by selecting the **AppsFlyer Cohorts** filter.

![User attributes filter "AppsFlyer Cohorts" selected.][7]

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}