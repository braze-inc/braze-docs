---
nav_title: Celebrus
article_title: Celebrus Integration
description: "Integrating Braze and Celebrus."
---

<!-- The title of your page, used to render the in-page title. -->
# Celebrus

<!-- The description starts with a '>' character and contains an overview of what will be covered. Optionally, in a following paragraph, you can contextualize the topic at a high-level. -->
> Integrating Braze and Celebrus.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Celebrus Implementation
You will need to get your Celebrus implementation installed and running, then it can be configured to integrate with Braze. 

## Celebrus Integration
There are two elements to the Celebrus integration for Braze, "Braze SDK" and "Braze Custom Attributes".  

### Celebrus connector for Braze SDK

The Celebrus connector for Braze SDK provides high-level web and mobile app channel data for Braze. The connector deploys and configures the Braze SDK in your channel - you will need to configure some settings in the Braze SDK data stream. You will need to provide values for these three settings:

    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");


### Celebrus connector for Braze Custom Attributes

The Celebrus connector for Braze Custom Attributes sends custom attributes to an intermediate database. In Celebrus you configure the connection details for the database - these will depend on what type of database you are using (e.g. Snowflake or Redshift). The attributes will be taken from the Celebrus profile builder definition, so the attributes in Braze will mirror those in the Celebrus profile. In Braze you will need to configure the Cloud Data Ingestion settings in the Data Settings area.
