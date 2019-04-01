---
nav_title: Inkit
alias: /partners/inkit/
---

# Inkit Direct Mail Integration

[Inkit][1] enables you to save time and effort by automating your direct mail campaigns and bring offline customers back online. You can access Inkit's services through Braze's webhook feature and send mail to your users.


## Requirements

|Requirement| Origin| Access| Description|
| ---| ---| ---|
| Inkit API Key | Inkit | [Inkit Dashboard](https://app.inkit.io/#/account/api) | This key will enable you to connect your Braze and Inkit accounts.|
| Inkit Template ID | Inkit | Found within the URL for each template. | This key will enable you to send your template to Braze. <br> Within the URL `https://app.inkit.io/#/templates/design/bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`, the Template ID is `bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`. |
| HTTP Header | Inkit | Inkit Account | You will combine this with your Inkit API Key to authorize the connection as a key value pair within your Braze template. |


## Integration

You will need to use both your Inkit and Braze accounts to use the Inkit integration.

### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign in Braze.

![Inkit_Webhook_Template][7]

Click on `New Template`. Then, add your `HTTP Header` into the `Webhook URL` field.

Choose "Raw Text" from the `Request Body` drop down. A new field should appear.

### Step 2: Fill Out Your Template

Insert the following text into the new field. Each of these fields are required.

```json
{% raw %}
{
  "api_token": "INKIT_API_TOKEN",
  "template_id": "INKIT_TEMPLATE_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "address": "{{custom_attribute.${address}}}",
  "address2": "{{custom_attribute.${address2}}}",
  "city": "{{${city}}}",
  "country": "{{${country}}}",
  "state": "{{custom_attribute.${state}}}",
  "zip": "{{custom_attribute.${zip}}}"
}
{% endraw %}
```
Replace the necessary fields with the correct information - specifically `INKIT_API_TOKEN` and `INKIT_TEMPLATE_ID`.

![Inkit Integration][5]{: height="70%" width="70%"}


### Step 3: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag. You must have `address`, `address2`, `state`, and `zip` set up as [custom attributes][3] to send this Webhook.

You should be able to preview your request in the left-hand panel, or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}

See Inkit's integration docs [here][2].

## Usage

If you hadn't created this in `Templates & Media`, you can go to `Campaigns`, then click `+ Create Campaign`. Select "Webhook" and choose your template from the "Saved Webhook Template" list. Create your [Webhook][6]!

![Inkit Usage][4]{: height="70%" width="70%"}


[1]: https://inkit.io/
[2]: http://support.inkit.io/integrations/braze-inkit-integration
[3]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[4]: {% image_buster /assets/img/inkit-use.png %}
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{ site.baseurl }}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}
