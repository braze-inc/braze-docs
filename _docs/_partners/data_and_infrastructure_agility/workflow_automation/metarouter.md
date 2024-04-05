---
nav_title: MetaRouter
article_title: MetaRouter
description: "Elevate your customer data management in Braze, with MetaRouter.  This high-performance, server-side tag management solution offers maximum compliance and control with seamless deployment options, whether on a MetaRouter hosted private cloud or your own infrastructure."
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> MetaRouter elevates your Braze experience by seamlessly integrating as a powerful server-side tag management platform. It empowers you to orchestrate a complete customer data journey within Braze, from reliable fully first-party data collection enriched by up to 30%, to real-time event stream activation for personalized journeys. Additionally, MetaRouter streamlines implementation by eliminating the need for Braze tags or other third-party tags, granting you granular, parameter-by-parameter control over the data flowing into Braze.

## Prerequisites

Before you start, you'll need the following:

| Requirement | Description |
|---|---|
| A MetaRouter account | A [MetaRouter Enterprise account](https://enterprise.metarouter.io/).|
| A MetaRouter cluster | An active cluster |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Integrating Braze and MetaRouter

1. Establish your MetaRouter Cluster.
2. Determine the events you would like to track.
3. Install an SDK & code events into your website.
4. Connect your cluster to the UI.
5. Set up your first pipeline.
6. Verify that events are being sent to MetaRouter and your integration.

### Step 1: Add Braze as an Integration

In Enterprise MetaRouter, select **Integrations** > **New Integration** > **Braze**, then name your integration. Next enter your instance URL and API key, then select **Apply Changes**.

![Adding Braze as an integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %})

### Step 2: Add Event Mapping

Add event mapping for each of the identity outputs, then configure the events you want to send to Braze. When you're finished, select **Save as New Revision**.

![Add event mapping for each of the identity outputs.]({% image_buster /assets/img/metarouter/img2.png %})

## Using MetaRouter with Braze

 - Retries can be built in.
 - Requests are batched. 
 - Rate limiting issues are handled with a retry.
 - External ID and PII are supported. MetaRouter passes their anonymous ID and any PII (email, phone number, name) that clients want.
 - You can send Braze Purchases and Custom Events data.
     - Event properties are supported.
     - Nested event properties are not supported.
