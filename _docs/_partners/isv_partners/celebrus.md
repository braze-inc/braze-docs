---
nav_title: Celebrus
article_title: Celebrus Integration
description: "Integrating Braze and Celebrus."
---

<!-- The title of your page, used to render the in-page title. -->
# Celebrus

<!-- The description starts with a '>' character and contains an overview of what will be covered. Optionally, in a following paragraph, you can contextualize the topic at a high-level. -->
> Celebrus seamlessly integrates with Braze SDK across web and mobile app channels, facilitating the population of Braze with channel activity data. This includes comprehensive insights into visitor traffic across digital assets over specified periods. In addition, Celebrus captures rich profile data for each individual customer, which can be seamlessly synced with Braze. This enables the delivery of precise Braze analytics, empowering you to devise highly effective communication strategies based on comprehensive, accurate, and detailed first-party data. This capability is further bolstered by Celebrus' Machine Learning-driven Signals, ensuring hassle-free data capture without the need for extensive tagging. With a robust first-party identity graph in place, all data becomes instantly accessible for immediate use.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Celebrus Implementation
When your Celebrus implementation is installed and running, use the Celebrus connectors for Braze to integrate Celebrus data into Braze. If you do not already have the Braze SDK implemented in your web channel, you can use Celebrus to deploy the Braze SDK. Customer attributes can by sync'ed with Braze via a cloud database. 

## Celebrus Integration
There are two elements to the Celebrus integration for Braze, "Braze SDK" and "Braze Custom Attributes". You can deploy either or both depending on how you use Braze today, and the use cases you need.  

### Celebrus connector for Braze SDK

The Celebrus connector for Braze SDK provides high-level web and mobile app channel data for Braze. The connector deploys and configures the Braze SDK in your channel - you will need to configure some settings in the Braze SDK data stream. You will need to provide values for these three settings:

    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");


### Celebrus connector for Braze Custom Attributes

The Celebrus connector for Braze Custom Attributes sends custom attributes to an intermediate database. In Celebrus you configure the connection details for the database - these will depend on what type of database you are using (e.g. Snowflake or Redshift). The attributes will be taken from the Celebrus profile builder definition, so the attributes in Braze will mirror those in the Celebrus profile. In Braze you will need to configure the Cloud Data Ingestion settings in the Data Settings area.
