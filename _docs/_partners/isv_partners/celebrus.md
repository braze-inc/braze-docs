---
nav_title: Celebrus
article_title: Celebrus Integration
description: "Integrating Braze and Celebrus."
---

<!-- The title of your page, used to render the in-page title. -->
# Celebrus

<!-- The description starts with a '>' character and contains an overview of what will be covered. Optionally, in a following paragraph, you can contextualize the topic at a high-level. -->
> Celebrus seamlessly integrates with Braze SDK across web and mobile app channels, facilitating the population of Braze with channel activity data. This includes comprehensive insights into visitor traffic across digital assets over specified periods. In addition, Celebrus captures rich profile data for each individual customer, which can be seamlessly synced with Braze. This empowers you to devise highly effective Braze analytics and communication strategies based on comprehensive, accurate, and detailed first-party data. This capability is further bolstered by Celebrus' Machine Learning-driven Signals, ensuring hassle-free data capture without the need for extensive tagging. With a robust first-party identity graph in place, all data becomes instantly accessible for immediate use.
>
>
## Prerequisites

| Requirement | Description |
|---|---|
| Celebrus account | A Celebrus account is required to take advantage of this partnership. |
| Data Warehouse (Optional) | When using the Celebrus connector for Braze Custom Attributes, you must have a data warehouse that is supported by Braze's Cloud Data Ingestion (CDI) integration, and configure CDI in the Braze dashboard. |
| Braze SDK Configuration Settings (Optional) | When using the Celebrus connector for Braze SDK, you must pass the SDK endpoint and SDK API Key. |
{: .reset-td-br-1 .reset-td-br-2}


<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Celebrus Implementation
When your Celebrus implementation is installed and running, use the Celebrus connectors for Braze to integrate Celebrus data into Braze. There are two elements to the Celebrus integration for Braze, "Braze SDK" and "Braze Custom Attributes". You can deploy either or both depending on how you use Braze today and the use cases you need.


If you do not already have the Braze SDK implemented in your web channel, you can use Celebrus to deploy the Braze SDK. Celebrus will add the Braze SDK to web pages, and set up the Braze identity for the web visitor using the Celebrus identity graph. Customer attributes can be synced with Braze via a Cloud Data Ingestion (CDI). This requires a data warehouse supported by Braze CDI, and the configuration of the CDI in Braze.

### Celebrus connector for Braze SDK

The Celebrus connector for Braze SDK provides high-level web and mobile app channel data for Braze. In the Braze SDK, the Celebrus `System Identity` from the Celebrus identity graph will be used as the identifier for Braze integration. Other identifiers are supported for syncing custom attributes via the "Braze Custom Attributes" Celebrus connector.

The connector deploys and configures the Braze SDK in your channel - you will need to configure some settings in the Braze SDK data stream. You will need to provide values for these three settings:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
The Celebrus connector for Braze SDK will insert and initialize the Braze SDK to identify the user and add the identifier to Celebrus' Identity Graph. This connector will not log data to the user profile or trigger other Braze SDK methods. You can call any desired methods directly within your code base to log data via the [Braze SDK] (https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/) or take advantage of other Braze SDK-supported features. 
{% endalert%}

### Celebrus connector for Braze Custom Attributes

#### Step 1: Configure Connected details in Celebrus 
The Celebrus connector for Braze Custom Attributes sends custom attributes to an intermediate database, pre-formatted in the way Braze expects to receive it. In Celebrus you configure the connection details for the database - these will depend on what type of database you are using (e.g. Snowflake or Redshift). 

#### Step 2: Configure Cloud Data Ingestion in your Braze dashboard
This integration uses Braze's Cloud Data Ingestion product. Follow Braze's documentation to set up the Cloud Data Ingestion settings according to the type of warehouse you are using. In Braze, you will need to [configure the Cloud Data Ingestion settings](https://www.braze.com/docs/user_guide/data_and_analytics/cloud_ingestion/overview/) to accept data from the warehouse Celebrus is connected to.

#### Step 3: Sync data from Celebrus to Braze
Celebrus captures and assigns unique identifier(s) to an individual such as email, phone, external_id or user alias and sends to Braze via CDI. This allows data to be synced to Braze for the same individual.

Celebrus will use the defined identifiers to send the customer attributes that are defined in the Celebrus Profile Builder, but only when attribute values change. The integration currently supports attributes; events and purchases are planned for a future release. Note that the attribute names will be as defined in the Celebrus profile builder, so the attributes in Braze will mirror those in the Celebrus profile. These may need to be adjusted to conform to Braze naming conventions. For example, conforming to Braze's [standard attribute naming conventions] (https://www.braze.com/docs/api/objects_filters/user_attributes_object#:~:text=custom%20attributes.-,Braze%20user%20profile%20fields,-Important%3A%0AThe).  

{% alert important %}
In this release, attributes are sent as string values. Some attributes are lists (such as signals), which may be converted to arrays in a future release. There are no nested attributes.
{% endalert%}

