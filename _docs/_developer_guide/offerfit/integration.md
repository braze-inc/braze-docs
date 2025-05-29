---
nav_title: Integrating OfferFit
article_title: Integrating OfferFit
page_order: 1
description: "Learn how to..."
---

# Integrating OfferFit by Braze

> Learn how to integrate OfferFit into Braze, so you can work with the OfferFit team to [build uses cases]({{site.baseurl}}/developer_guide/offerfit/building_use_cases), so you can leverage AI to make 1:1 decisions that maximize any business metric.

## Prerequisites

Before you can integrate OfferFit by Braze, you'll need an active OfferFit license. Interested in learning more? [Book a call](https://offerfit.ai/book-now)!

## Integrating OfferFit

### Step 1: Get your endpoint URL

You'll need to get the endpoint URL associated with your specific Braze instance. For more information, see [Braze API endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).

### Step 2: Create an API key

In Braze, go to **Settings** > **API Keys**, then create a new key with the following permissions:

| Permission | Purpose | Required? |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | Updates custom attributes on user profiles, in addition to creating temporary user profiles when using [test sends]({{site.baseurl}}/developer_guide/offerfit/test_sends). | &#10003; |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | Deletes temporary user profiles that were created while using [test sends]({{site.baseurl}}/developer_guide/offerfit/test_sends). | Only for [test sends]({{site.baseurl}}/developer_guide/offerfit/test_sends) |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Updates the available audience communications every morning by exporting the list of users from each selected segment. | &#10003; |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Retrieves a list of identifiers when targeting users using an `external_id` instead of a segment. Since OfferFit doesn’t accept Personally Identifiable Information (PII), you'll need to ensure your `fields_to_export` parameter to return only non-PII fields.
 | Only if using `external_ids` |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Sends recommended variants at the recommended time using API Campaigns that are configured for OfferFit's experimenter. | &#10003; |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | Retrieves the list of active campaigns and extracts available email content for experimentation. | &#10003; |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Exports aggregated campaign data to enable reporting, validation, and troubleshooting in OfferFit, so you can compare reporting values and analyze baseline performance.<br><br>While not required, this permission is recommended. |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Retrieves HTML content, subject line, and image resources from existing Campaigns for experimentation. | &#10003; |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Retrieves the list of active Canvases to extract available email content for experimentation. | &#10003; |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Exports aggregated canvas data for reporting and validation, especially when BAU is orchestrated via Canvas.<br><br>While not required, this permission is recommended. |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | Retrieves HTML content, subject line, and image resources from existing Canvases for experimentation. | &#10003; |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Retrieves all existing segments as potential target audiences for the OfferFit experimenter. | &#10003; |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Exports segment size information, which is shown in OfferFit when selecting an audience. | &#10003; |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | Retrieves segment details such as entry and exit criteria to help understand changes in audience size or performance. |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Creates copies of selected base HTML templates with [dynamic placeholders]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) (Braze liquid tags) for experimentation, avoiding changes to the originals. | &#10003; |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Pushes updates to OfferFit-created template copies when experimentation criteria change, such as call-to-actions. | &#10003; |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | Retrieves information about OfferFit-created templates in your Braze instance. | &#10003; |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Validates that templates were successfully copied over to your the Braze instance. | &#10003; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Contact OfferFit

Reach out to your OfferFit customer success manager and ask them to enable OfferFit by Braze. They'll use your Braze API key and endpoint URL to finish setting up your integration.

When it's complete, you'll work alongside the OfferFit team to [start building uses cases for your product]({{site.baseurl}}/developer_guide/offerfit/building_use_cases). Each use case is tailor-made to a specific business goal, so you'll work together to design an implementation that's right for you.
