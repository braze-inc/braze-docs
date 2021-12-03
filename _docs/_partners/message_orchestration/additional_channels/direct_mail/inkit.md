---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "This article outlines the partnership between Braze and Inkit, which enables you to save time and effort by automating your direct mail campaigns and bring offline customers back online."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit][1] enables you to reach and communicate with your customers by delivering automated and personalized direct mail campaigns, rendering paperless documents at scale, and validating customer mailing addresses. 

The Braze and Inkit integration allows you to send Inkit mail to Braze users through Braze webhooks. 

## Prerequisites

|Requirement| Description|
| ---| ---|
|Inkit account | An [Inkit account](https://console.liftigniter.com/login) is required to take advantage of this partnership. |
| Inkit API key<br><br>`<INKIT_API_TOKEN>` | This key is found on your [Inkit Dashboard](https://app.inkit.io/#/account/integrations) will enable you to connect your Braze and Inkit accounts.|
| Inkit template ID<br><br>`<INKIT_TEMPLATE_ID>` | This key is found within the URL for each template, enabling you to send your template to Braze. <br><br>For example, within the URL `https://app.inkit.io/#/templates/design/bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`, the Template ID is `bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`. |
| HTTP header  | Found on your Inkit account, you will combine this with your Inkit API Key to authorize the connection as a key-value pair within your Braze template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

### Step 1: Create an Inkit template

On the Inkit platform, create a template to be used in your Braze campaign. 
Check out [Inkit documentation](https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration) on this partnership to learn more.

### Step 2: Create your Braze webhook template

In the Braze platform, to create an Inkit webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section. If you would like to create a one-off Inkit webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

![Inkit webhook template][7]

Once you have selected the Inkit webhook template, you should see the following:
- **Webhook URL**: `https://internal.inkit.io/integrations/webhook`
- **Request Body**: Raw Text

![Inkit integration][5]

#### Request headers and method

Inkit requires an `HTTP Header` for authorization that includes your Inkit API key encoded in base 64. The following will already be included within the template as a key-value pair, but in the **Settings** tab, you must replace the `<INKIT_API_TOKEN>` with your Inkit API key.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Request Body**: application/json
{% endraw %}

#### Request body

Ensure that your Liquid matches the proper custom attributes associated with the required and optional fields listed below. You can also add custom data fields to any request.

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

Your raw text will automatically highlight if it is an applicable Braze tag. `street`, `unit`, `state`, and `zip` must be set up as [custom attributes][3] to send this Webhook.

Preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new webhook campaign. 
{% endalert %}

[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}