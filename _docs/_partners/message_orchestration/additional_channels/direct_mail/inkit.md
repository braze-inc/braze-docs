---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "This article outlines the partnership between Braze and Inkit, which enables you to save time and effort by automating your direct mail campaigns and bring offline customers back online."
page_type: partner
search_tag: Partner

---

# Inkit Direct Mail Integration

> [Inkit][1] enables you to reach and communicate with your customers by delivering automated and personalized direct mail campaigns, rendering paperless documents at scale, and validating customer mailing addresses. 

You can access Inkit's services through Braze's webhook feature and send mail to your users.

## Requirements

|Requirement| Origin| Access| Description|
| ---| ---| ---|
| Inkit API Key | Inkit | [Inkit Dashboard](https://app.inkit.io/#/account/integrations) | This key will enable you to connect your Braze and Inkit accounts.|
| Inkit Template ID | Inkit | Found within the URL for each template. | This key will enable you to send your template to Braze. <br> Within the URL `https://app.inkit.io/#/templates/design/bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`, the Template ID is `bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`. |
| HTTP Header | Inkit | Inkit Account | You will combine this with your Inkit API Key to authorize the connection as a key-value pair within your Braze template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Integration

You will need to use both your Inkit and Braze accounts to use the Inkit integration.

### Step 1: Create a Webhook Template in Braze

You can create this from the **Templates & Media** section, or create a new webhook campaign in Braze.

![Inkit_Webhook_Template][7]

Once you have selected the Inkit webhook template, you should see the following:

- `Webhook URL`: https://internal.inkit.io/integrations/webhook
- `Request Body`: Raw Text
- `HTTP Method`: POST

### Step 2: Fill Out Your Template

Please ensure that your Liquid matches the proper custom attributes associated with the required and optional fields listed below. You can also add custom data fields to any request.

```json
{% raw %}
{
  "api_token": "INKIT_API_TOKEN",
  "template_id": "INKIT_TEMPLATE_ID",
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
}
{% endraw %}
```
Replace the necessary fields with the correct information - specifically `INKIT_API_TOKEN` and `INKIT_TEMPLATE_ID`.

![Inkit Integration][5]{: height="70%" width="70%"}

Inkit also requires a `HTTP Header` for authorization that includes your Inkit API key. The following will already be included within the template as a key-value pair, but you will need to replace `INKIT_API_TOKEN` with your Inkit API key.

{% raw %}

- `Header Name`: Authorization
- `Header Value`: ``` { Basic {{ 'INKIT_API_TOKEN' | base64_encode }} } ```

{% endraw %}

### Step 3: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag. You must have `street`, `unit`, `state`, and `zip` set up as [custom attributes][3] to send this Webhook.

You should be able to preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}

See Inkit's integration docs [here][2].

## Usage

If you hadn't created this in `Templates & Media`, you can go to `Campaigns`, then click `+ Create Campaign`. Select "Webhook" and choose your template from the "Saved Webhook Template" list. Create your [Webhook][6]!

![Inkit Usage][4]{: height="70%" width="70%"}


[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[4]: {% image_buster /assets/img/inkit-use.png %}
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}
