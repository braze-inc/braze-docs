---
nav_title: VideoSmart
article_title: VideoSmart
description: 'This reference article outlines the partnership between Braze and VideoSmart. A personalized, interactive video technology that enables brands to deliver data-driven, non-linear content at scale.'
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) provides personalized, interactive video technology that enables brands to deliver data-driven, non-linear content at scale. Each video is dynamically generated using customer-level data, allowing for tailored messaging and user journeys within a single video experience.
>
> The VideoSmart integration with Braze allows marketers to embed personalized video content directly into email campaigns. This is achieved using Braze’s Connected Content and Liquid templating to request video assets from VideoSmart at send time.
>
> The integration is typically implemented via a reusable Content Block template within Braze, enabling consistent deployment across campaigns while allowing flexibility in campaign selection and personalization logic.

_This integration is developed and maintained by VideoSmart._

## About this integration

VideoSmart integrates with Braze to dynamically generate personalized video assets at send time, which are then embedded directly into your Braze campaign and Canvas email content.

Within Braze, marketers select the relevant VideoSmart campaign and pass customer attributes (via Liquid templating) to VideoSmart at the point of send. These attributes are used to render a unique, personalized video experience for each recipient.

The integration leverages Braze’s Connected Content functionality to request video URLs or assets from VideoSmart’s API in real time, enabling scalable personalization.

This integration is designed for Braze email messages that support Liquid templating and Connected Content, and can be configured to work with standard Braze user profile attributes or custom data fields.

## Use cases

### Use case examples

Common use cases include the following:

- Customer onboarding and welcome journeys
- Financial education (e.g. pensions, insurance policies)
- Annual statements and regulatory communications
- Product awareness and cross-sell campaigns
- Customer retention and re-engagement campaigns
- Abandoned cart: When a customer adds products to their cart but doesn’t purchase, send an email with a personalized video that highlights the items they left behind.
- Post-purchase follow-up: After a purchase, send a personalized thank you video and recommend related products.

## Prerequisites

Before you start, confirm you have the following:

| Prerequisite                        | Description                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Braze Connected Content credentials | A Connected Content Basic Authentication credential named **basic_credentials**, configured with VideoSmart-provided values |
| VideoSmart Content Block template   | The VideoSmart Content Block template added in your Braze dashboard (provided by VideoSmart)                                |
| A Braze email message               | A Braze Campaign email or Canvas email step where you will insert the VideoSmart Content Block                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating VideoSmart

Follow these steps to enable the VideoSmart Content Block and use it in an email.

### Step 1: Set up VideoSmart Content Block template in your Braze account

Request the VideoSmart Content Block template from your VideoSmart representative and add it to your Braze dashboard.

VideoSmart will also provide credentials for the Connected Content authentication used by the Content Block.

### Step 2: Set up Connected Content authentication

Create a Connected Content Basic Authentication credential in Braze named **basic_credentials**.

- Follow Braze’s instructions for Basic Authentication: [Using basic authentication](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#using-basic-authentication)
- Use the username/password provided by VideoSmart.

### Step 3: Add the Content Block to your email

Insert the **VideoSmart Content Block** in your email where you want the video content to appear.

In most Braze setups, Content Blocks are referenced using the following pattern (replace **VideoSmart_Campaign** with the name of the Content Block in your account):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

The Content Block name is case-sensitive and must match exactly what you have configured in Braze.

### Step 4 (optional): Override campaign and record data

If your Content Block supports defaults, you can use it without setting any variables.

If you need to choose a specific VideoSmart campaign and/or pass custom personalization fields, set the following Liquid variables before rendering the Content Block:

- `vs_campaign_id`: VideoSmart campaign identifier
- `vs_record_data`: a JSON string containing the values you want to pass into the VideoSmart template

Example (using Braze user attributes for first name and last name):

{% raw %}
```
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'John' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

Notes:

- Always provide defaults for values used in `vs_record_data` to keep Braze email preview working.
- `vs_record_data` must be valid JSON, encoded as a single string (the example uses `strip_newlines`).

### Step 5: Use the available variables generated by VideoSmart's content block template

After the Content Block runs, it can expose variables you can reference elsewhere in your email.

Common variables include:

{% raw %}
| Variable                          | Description                                           |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}`                 | URL of the personalized video                         |
| `{{ poster_url }}`                | URL of the poster image for the video                 |
| `{{ output_data.VARIABLE_NAME }}` | Additional output fields exposed by the Content Block |
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Rate limit

VideoSmart's API has a rate limit of 10,000 requests per minute. If you exceed this limit, you may receive errors or experience delays in video generation.

To reduce this risk, configure Braze campaign rate limiting so the message send rate stays below VideoSmart API capacity.

Braze guidance for delivery speed and rate limiting:
[Delivery speed and rate limiting](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)

## Considerations

- Connected Content is executed when the message is rendered, so values can differ between preview and send if your defaults or attributes differ.
- Ensure your email includes the Content Block before referencing variables like `video_url`.
- If you use custom fields in `vs_record_data`, confirm the expected field names with VideoSmart.

## Troubleshooting

### Preview not working

If Braze Preview fails (for example, repeated retries or authentication errors), check that:

- The Connected Content credential named **basic_credentials** exists and is configured correctly.
- The **VideoSmart Content Block** template is present in your Braze account.
- Any required variables (for example, `vs_campaign_id` or required fields in `vs_record_data`) have defaults set for preview.

### VideoSmart's content block template variables not generating expected output

If the variables generated by VideoSmart's content block template are not generating the expected output, make sure to check the following:

- The **VideoSmart Content Block** template is set up correctly in your Braze account.
- The Connected Content authentication is set up correctly with the appropriate credentials.
- Print variables in your email to confirm they are being set. For example: `{% raw %}{{ video_url }}{% endraw %}`

If you are using a custom campaign, also verify:

- `vs_campaign_id` is set to a valid campaign identifier.
- `vs_record_data` is valid JSON and contains the expected fields.
