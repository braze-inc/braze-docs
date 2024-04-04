---
nav_title: MetaRouter
article_title: MetaRouter
description: "Elevate your customer data management in Braze, with MetaRouter.  This high-performance, server-side tag management solution offers maximum compliance and control with seamless deployment options, whether on a MetaRouter hosted private cloud or your own infrastructure."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
layout: dev_guide
--- cd

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# MetaRouter

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a consice overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> 
MetaRouter elevates your Braze experience by seamlessly integrating as a powerful server-side tag management platform. It empowers you to orchestrate a complete customer data journey within Braze, from reliable fully first-party data collection enriched by up to 30%, to real-time event stream activation for personalized journeys. This translates to deeper customer insights, more sophisticated journeys, and ultimately, a maximized return on investment in Braze. Additionally, MetaRouter streamlines implementation by eliminating the need for Braze tags or other third-party tags, granting you granular, parameter-by-parameter control over the data flowing into Braze.

<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

- A MetaRouter account: A MetaRouter Enterprise account https://enterprise.metarouter.io/.
- MetaRouter cluster: An active cluster
- A Braze REST API key: A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**.
- A Braze REST endpoint: [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}


<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. -->
## Integrating Braze and MetaRouter

1. Establish your MetaRouter Cluster.
2. Determine the events you would like to track.
3. Install an SDK & code events into your website.
4. Connect your cluster to the UI.
5. Set up your first pipeline.
6. Verify that events are being sent to MetaRouter and your integration.


### Step 1: Add Braze as an Integration

In Enterprise MetaRouter, Navigate to the Integrations section. Select the New Integration. Select Braze and give the integration a name. 

MetaRouter’s required parameters are the instance URL and the API key.  Add the information into the provided text box and Apply Changes.

![alt text](img1.png)

<!-- Use the "Make a post request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->
### Step 2: Add Event Mapping

Add event mapping for each of the identity outputs. Configure the events that you want to send to Braze.

In the top header, select “Save as New Revision” to implement changes.

![alt text](img2.png)

<!-- A section outlinning how to use your integration with Braze. For example: how to access the data sent to Braze, or how to leverage your integration with Braze messaging. -->
## Using MetaRouter with Braze

 - Retries can be built in.
 - Requests are batched. 
 - Rate limiting issues are handled with a retry.
 - External ID and PII are supported. MetaRouter passes their anonymous ID and any PII (email, phone number, name) that clients want.
 - You can send Braze Purchases and Custom Events data.
     - Event properties are supported.
     - Nested event properties are not supported.
