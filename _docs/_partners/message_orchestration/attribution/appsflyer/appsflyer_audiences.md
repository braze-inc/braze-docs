---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "This page outlines the partnership between Braze and AppsFlyer Audiences, a feature of the AppsFlyer platform that allows you to efficiently build and connect audience segments to partner networks."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> [AppsFlyer][1] is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking. [AppsFlyer Audiences][2] allows you to build and connect audience segments to your partner networks.

Drive user engagement and increase the efficiency of your remarketing programs by leveraging the power of the user segments built in AppsFlyer Audiences. Pass your AppsFlyer audiences (cohorts) directly to Braze to create powerful customer engagement campaigns targeted toward just the right users at just the right time.

## Requirements
- __AppsFlyer Account__ - This Braze integration is only available to AppsFlyer customers.
- __Braze Data Import Key and REST Endpoint__ - This integration invokes the braze [/users/track/ endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to function.
- __SDKs Integrated__ - The Braze SDK and AppsFlyer SDK must be integrated into your app 

## AppsFlyer and Braze Cohort Import

The following describes the Braze and AppsFlyer Audiences integration for importing cohorts into Braze. This integration supports iOS and Android apps. If you are looking for information about passing AppsFlyer attribution data to Braze, you can find it [here][3].

### Step 1: Configure the AppsFlyer SDK

To use this integration, you must pass the user's Braze External ID to AppsFlyer using the `setPartnerData` function of the AppsFlyer SDK:

{% tabs local %}
{% tab Android %}
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```
{% endtab %}
{% tab iOS %}
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```
{% endtab %}
{% endtabs %}

### Step 2: Get the Braze Data Import Key and REST Endpoint

In the Braze platform:

1. Navigate to __Integrations__ > __Technology Partners__, and select __AppsFlyer__. 
2. In the __Data Import Using Cohort Import__ section at the bottom of the page, click __Generate New Key__ to generate your Data Import Key. 
3. Copy this key and the REST endpoint to use when configuring a Braze connection in AppsFlyer Audiences.<br><br>![data_import_key][5]{: style="max-width:70%;"}

### Step 3: Configure a Braze Connection in AppsFlyer Audiences

In the AppsFlyer platform, within AppsFlyer Audiences: 

1. Go to the **Connections** tab and click **Add partner connection**.
2. Select Braze as the partner and give the connection a name.
3. Enter the data import key and the REST endpoint you copied from your Braze account in step two.
4. Save the connection, and it will be available to link to any new or existing audience.<br><br>![partner_connection][6]{: style="max-width:70%;"}

Learn more about working with partner connections in the [AppsFlyer documentation][4].

### Step 4: Using AppsFlyer Audiences Cohorts in Braze

Once an AppsFlyer audience has been uploaded to Braze, you can use it as a filter when defining segments in Braze by selecting the __AppsFlyer Cohorts__ filter.

![cohort_filter][7]{: style="max-width:70%;"}

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: https://www.braze.com/docs/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}

