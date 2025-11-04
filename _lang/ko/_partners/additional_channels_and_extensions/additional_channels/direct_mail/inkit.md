---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "This reference article outlines the partnership between Braze and Inkit, which enables you to save time and effort by automating your direct mail campaigns and bring offline customers back online."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) and Braze empower organizations to securely generate and distribute documents - both digitally as well as via direct mail.

_This integration is maintained by Inkit._

## About the integration

The Braze and Inkit integration allows you to generate documents and mail them directly to Braze users with Braze webhooks.

## Prerequisites

|Requirement| Description|
| ---| ---|
|Inkit account | An [Inkit account](https://www.inkit.com/) is required to take advantage of this partnership. |
| Inkit API key<br><br>`<INKIT_API_TOKEN>` | This key is found on your [Inkit Dashboard](https://app.inkit.io/#/account/integrations) under the **Development** tab and will enable you to connect your Braze and Inkit accounts.|
| Inkit template ID<br><br>`<INKIT_TEMPLATE_ID>` | After creating a template, you can copy the template ID from the **Templates** tab to use in your template in Braze.<br><br>For example, you might create a template called `invoice_template` in the Inkit environment with the Template ID: `tmpl_3bDScFl9cwr3OAVR1RSdEC`.
| HTTP header | The HTTP header is part of the API request that you send from Braze to Inkit. In it, you will include your Inkit API key to authenticate and authorize calls to the Inkit API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Create an Inkit template

On the Inkit platform, create a template to be used in your Braze campaign in HTML, Word, PowerPoint, Excel or PDF. Check out [Inkit documentation](https://docs.inkit.com/docs/create-a-template) to learn more.

### Step 2: Create your Braze webhook template

To create an Inkit webhook template to use in future campaigns or Canvases, navigate to **Templates** > **Webhook Templates** in the Braze platform. 

If you would like to create a one-off Inkit webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

![A selection of available predesigned webhook templates in the Webhook Templates tab of the Templates & Media section.]({% image_buster /assets/img/inkit-webhook-template.png %})

Once you have selected the Inkit webhook template, you should see the following:
- **Webhook URL**: Blank
- **Request Body**: Raw Text

In the Webhook URL field, you will need to [create](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) and input a Inkit webhook URL.

![Request body code and webhook URL shown in the Braze webhook builder compose tab.]({% image_buster /assets/img/inkit-integration.png %})

#### Request headers and method

Inkit requires an `HTTP Header` for authorization, including your Inkit API key encoded in base 64. The following will already be included within the template as a key-value pair, but in the **Settings** tab, you must replace the `<INKIT_API_TOKEN>` with your Inkit API key.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

Ensure that your Liquid matches the proper custom attributes associated with the following required and optional fields. You can also add custom data fields to any request.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Step 3: Preview your request

Your raw text will automatically highlight if it is an applicable Braze tag. `street`, `unit`, `state`, and `zip` must be set up as [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) to send this Webhook.

Preview your request in the **Preview** panel or navigate to the **Test** tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


