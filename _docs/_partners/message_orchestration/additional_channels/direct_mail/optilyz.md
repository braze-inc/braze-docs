---
nav_title: optilyz
article_title: optilyz
page_order: 1
description: "This article outlines the partnership between Braze and optilyz, which enables you to run more customer-centric, sustainable, and profitable direct mail campaigns."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz][1] is a direct mail automation platform that enables you to run more customer-centric, sustainable, and profitable direct mail campaigns. 

Use the optilyz and Braze webhook integration to send your customers direct mail such as letters, postcards, and self-mailers.

## Prerequisites

| Requirement | Description |
|---|---|
|optilyz account | An optilyz account is required to take advantage of this partnership. |
| optilyz API key<br><br>`<OPTILYZ_API_KEY>`| Your optilyz customer success manager will provide you with your optilyz API key.<br><br>This API key will enable you to connect your Braze and optilyz accounts. |
| optilyz automation ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | The automation ID can be found in a box on the page header.<br><br>When logged into optilyz, you can navigate to the automation you want to send data into.<br>The automation must be activated first. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Use cases

Running direct mail like a digital channel means moving away from mass mailings and leveraging the channel as part of your (digital) customer journeys. The benefits of a modern approach to direct mail are:
- Increased conversion rates via increased relevance, additional use cases, easier A/B testing, and cross-channel effects
- Reduced effort via automation and an end-to-end solution
- Reduced cost via frame contracts & cost transparency

## Integration

To integrate with optilyz, use the [optilyz API][2] to send recipient data to the Braze webhook.

### Step 1: Create your Braze webhook template

In the Braze platform, to create an optilyz webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section. If you would like to create a one-off optilyz webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:
- **Webhook URL**: `https://www.optilyz.com/api/v2/automations/<OPTILYZ_AUTOMATION_ID>/recipient`
- **Request Body**: Raw Text

#### Request headers and method

optilyz also requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab, you must replace the `<OPTILYZ_API_KEY>` with your optilyz API key. This key must include a ":" directly after the key and be encoded in base 64. 

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![optilyz_settings][6]{: style="max-width:50%"}

#### Request body

In the following request body, you can use any Liquid personalization tags and build a custom request template according to optilyz' [API documentation][2].

The `variation` field is optional and can define which design inside the automation should be used. If a variation is omitted, optilyz will assign one of the defined variations randomly.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![optilyz_compose][5]

### Step 2: Preview your request

Next, preview your request in the left-hand panel or navigate to the __Test__ tab, where you can select a random user, an existing user, or customize your own to test your webhook. Remember to save your template before leaving the page!

![optilyz_testing][7]

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/