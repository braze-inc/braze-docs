---
nav_title: MetaRouter Partner Page
article_title: MetaRouter Partner Page

description: Elevate your customer data management in Braze, with MetaRouter.  This high-performance, server-side tag management solution offers maximum compliance and control with seamless deployment options, whether on a MetaRouter hosted private cloud or your own infrastructure.
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
layout: dev_guide
---


# MetaRouter
MetaRouter elevates your Braze experience by seamlessly integrating as a powerful server-side tag management platform. It empowers you to orchestrate a complete customer data journey within Braze, from reliable fully first-party data collection enriched by up to 30%, to real-time event stream activation for personalized journeys. This translates to deeper customer insights, more sophisticated journeys, and ultimately, a maximized return on investment in Braze. Additionally, MetaRouter streamlines implementation by eliminating the need for Braze tags or other third-party tags, granting you granular, parameter-by-parameter control over the data flowing into Braze.

## Prerequisites
This section should list what you need to complete this partnership integration. The best way to deliver this information is with a quick instructional paragraph that describes any non-technically important details or "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, use a chart to describe the technical requirements of the integration.
<div class='alert alert-important' role='alert'><div class='alert-msg'> <b>important: </b><br />
<p>The following requirements are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the following chart. Be sure to adjust the descriptions and tailor them to your partnership integration.</p>
</div></div>
| Requirement | Description |
| ----------- | ----------- |
| Partner account | A partner account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration
In Enterprise MetaRouter, Navigate to the Integrations section, and select the New Integration. Select Braze and give the integration a name. MetaRouter’s required parameters are the instance url and API key. Add the information into the provided text box and Apply Changes. In the top header, select save as new revision to implement changes.

##Commonly Asked Questions
- Are there retries? Yes, retries can be built in. 
- Are the requests batched? Yes
- How will rate limiting issues be handled? Rate limiting issues are handled with a retry.
- What identifiers are supported? External ID and PII. MetaRouter passes our anonymous ID and any PII (email, phone number, name) that clients want.
- What types of data can be sent to Braze: attributes, events, purchases? Events, Purchases and Custom Events
- If purchase/custom events are supported, are event properties supported. Yes
- Are nested event properties supported? No

