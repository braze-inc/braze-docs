---
nav_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/

description: "This page outlines the partnership between Braze and AppsFlyer Audiences, a feature of the AppsFlyer platform that allows you to efficiently build and connect audience segments to partner networks."
page_type: partner

---

# AppsFlyer Audiences

> [AppsFlyer][1] is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking. [AppsFlyer Audiences][2] allows you to to build and connect audience segments to your partner networks.

Drive user engagement and increase the efficiency of your remarketing programs by leveraging the power of the user segments built in AppsFlyer Audiences. Pass your AppsFlyer audiences (cohorts) directly to Braze to create powerful customer engagement campaigns targeted toward just the right users at just the right time.

## AppsFlyer Cohort Import

This page describes the Braze and AppsFlyer Audiences integration for **importing cohorts into Braze**. If you are looking for information about passing AppsFlyer **attribution data** to Braze, you can find it [here in the Braze documentation][3].

{% alert note %}The Braze/AppsFlyer Audiences integration supports iOS and Android apps.

The Braze SDK and the AppsFlyer SDK must be integrated into your app.{% endalert %}

### Step 1: Configure the AppsFlyer SDK

To use this integration, you must pass the user’s **Braze External ID** to AppsFlyer using the `setPartnerData` function of the AppsFlyer SDK. Usage examples follow:

{% tabs local %}
{% tab Android %}

```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```
{% endtab %}
{% tab iOS %}

```objective-c
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

{% endtab %}
{% endtabs %}

### Step 2: Get the Braze Data Import Key and REST Endpoint

In your Braze account, navigate to **Integrations > Technology Partners**, and select **AppsFlyer**. In the **Data Import Using Cohort Import** section, click **Generate New Key** to generate your Data Import Key. Copy this key and the REST Endpoint to use when configuring a Braze connection in AppsFlyer Audiences.

![data_import_key][5]{: style="max-width:70%;"}

{% alert important %}Be sure that you copy the key from the **Data Import Using Cohort Import** section of the page (not the install attribution section).{% endalert %}

### Step 3: Configure a Braze Connection in AppsFlyer Audiences

In AppsFlyer Audiences: 

1. Go to the **Connections** tab and click **Add partner connection**.
2. Select Braze as the partner and give the connection a name.
3. Enter the Data Import Key and the REST Endpoint you copied from your Braze account in step 2.
4. Save the connection and it will be available to link to any new or existing audience.

![partner_connection][6]{: style="max-width:70%;"}

Learn more about working with partner connections in the [AppsFlyer documentation][4].

### Step 4: Using AppsFlyer Audiences Cohorts in Braze

Once an AppsFlyer audience has been uploaded to Braze, you can use it as a filter when defining segments in Braze.

![cohort_filter][7]{: style="max-width:70%;"}



[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: https://www.braze.com/docs/partners/message_orchestration/attribution/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections

[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}

[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}

[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}

