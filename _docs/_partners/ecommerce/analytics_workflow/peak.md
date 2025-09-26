---
nav_title: Peak
article_title: Peak
description: "This reference article outlines the partnership between Braze and Peak, a decision intelligence platform, allows you to take predicted churn probability and attributes based on customer behaviors and interactions, and import them into Braze to use in customer segmentation and targeting."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://peak.ai/), a decision intelligence platform, is an end-to-outcome system where decision intelligence is the commercial application of AI to enhance business decision-making, growing revenue and profits.

_This integration is maintained by Peak._

## About the integration

The partnership between Braze and Peak allows you to take predicted churn probability and attributes based on customer behaviors and interactions, and import them into Braze to use in customer segmentation and targeting. 

## Prerequisites

As a starting point, a Peak tenant must host the integration between Peak and Braze. This is traditionally created during the onboarding of Peak customers. Additionally, a decisions intelligence solution is initially required as this generates the AI-driven outputs that will subsequently be integrated into Braze.

| Requirement | Description |
| ----------- | ----------- |
| Peak tenant | An instance of the Peak platform, known as a tenant, is required to host and orchestrate the integration. |
| Decision intelligence solution | Integration between Peak and Braze is based on AI-driven outputs and thus requires a Peak or Customer deployed solution within your tenant. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |

## Integration

The Peak solution customer intelligence utilizes a model to predict a range of forward-looking attributes based on customer behaviors and interactions. These attributes are stored within Peak and can be used to generate predictive segmentation, including a customer's probability of churning. The updating of these predictive attributes will be based on a configurable cadence (daily or weekly).

### Step 1: Run model and extract customers

The integration is triggered off the back of the AI model run and recalculation of the predictive customer attributes. These AI outputs are stored within Peak, including when an attribute is updated with a new status or value.

Based on when attributes have been updated, a selection is carried out to collect all customers with updated predictive attributes since the last sync between Peak and Braze.

### Step 2: Update Braze

With the updated customers and associated attributes, Peak will POST these to Braze using the [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), utilizing the [bulk]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates) header.

On receipt of successful status codes from the API, Peak will record the successful sync between Peak and Braze.

### Step 3: Using this integration

Once the sync between Peak and Braze is successful, the updated users now include the new attributes. Use these attributes in campaigns and Canvases to target users and personalize messages.


