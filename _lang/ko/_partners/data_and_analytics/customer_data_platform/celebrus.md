---
nav_title: Celebrus
article_title: Celebrus Integration
description: "Integrating Braze and Celebrus."
---

# Celebrus

> Celebrus seamlessly integrates with the Braze SDK across web and mobile app channels, facilitating the population of Braze with channel activity data. This includes comprehensive insights into visitor traffic across digital assets over specified periods. <br><br>In addition, Celebrus captures rich profile data for each individual customer, which can be synced with Braze. This empowers you to create effective Braze analytics and communication strategies based on comprehensive, accurate, and detailed first-party data. This capability is further bolstered by Celebrus' Machine Learning-driven Signals, allowing for hassle-free data capture without the need for extensive tagging. With a robust first-party identity graph in place, all data becomes instantly accessible for immediate use. 

_This integration is maintained by Celebrus._

## Prerequisites

| Requirement | Description |
|---|---|
| Celebrus account | A Celebrus account is required to take advantage of this partnership. |
| Data warehouse (optional) | When using the Celebrus connector for Braze custom attributes, you must have a data warehouse that is supported by the Braze Cloud Data Ingestion (CDI) integration, and configure CDI in the Braze dashboard. |
| Braze SDK configuration settings (optional) | When using the Celebrus connector for Braze SDK, you must pass the SDK endpoint and SDK API Key. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Implementation
After installing your Celebrus implementation, use the Celebrus connectors for Braze to integrate Celebrus data into Braze. There are two elements to the Celebrus integration for Braze: the Braze SDK and Braze custom attributes. You can deploy either or both depending on how you use Braze and the use cases you need.

If you don't already have the Braze SDK implemented in your web channel, you can use Celebrus to deploy the Braze SDK. Celebrus will add the Braze SDK to web pages, and set up the Braze identity for the web visitor using the Celebrus identity graph. Customer attributes can be synced with Braze via a Cloud Data Ingestion (CDI). This requires a data warehouse supported by Braze CDI, and the configuration of the CDI in Braze.

### Celebrus connector for Braze SDK

The Celebrus connector for Braze SDK provides high-level web and mobile app channel data for Braze. In the Braze SDK, the Celebrus `System Identity` from the Celebrus identity graph will be used as the identifier for Braze integration. Other identifiers are supported for syncing custom attributes via the Braze Custom Attributes Celebrus connector.

The connector deploys and configures the Braze SDK in your channel, so you will need to configure some settings in the Braze SDK data stream and provide the values for these three settings:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
The Celebrus connector for Braze SDK will insert and initialize the Braze SDK to identify the user and add the identifier to Celebrus' Identity Graph. This connector will not log data to the user profile or trigger other Braze SDK methods. <br><br>You can call any desired methods directly within your code base to log data via the [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) or take advantage of other Braze SDK-supported features.
{% endalert%}

### Celebrus connector for Braze custom attributes

#### Step 1: Configure Connected details in Celebrus 

The Celebrus connector for Braze custom attributes sends custom attributes to an intermediate database, pre-formatted in the way Braze expects to receive it. In Celebrus you configure the connection details for the database, which will depend on what type of database you are using (such as Snowflake or Redshift). 

#### Step 2: Configure Cloud Data Ingestion in your Braze dashboard

This integration uses Braze Cloud Data Ingestion. Follow the instructions in [Data warehouse integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) to set up and configure the [Cloud Data Ingestion settings]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) according to the type of warehouse you are using. 

#### Step 3: Sync data from Celebrus to Braze

Celebrus captures and assigns unique identifiers to an individual such as email, phone, `external_id`or user alias and sends to Braze via CDI. This allows data to be synced to Braze for the same individual.

Celebrus will use the defined identifiers to send the customer attributes that are defined in the Celebrus profile builder, but only when attribute values change. Note that the attribute names defined in the Celebrus profile builder will be used in Braze by default. So be sure you update these names to adhere to [Braze naming conventions]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

{% alert important %}
For now, this release doesn't support events and purchases.<br><br> This integration sends attributes as string values, so some attributes are lists (such as signals). For now, lists can't be converted to arrays. There are no nested attributes.
{% endalert%}

