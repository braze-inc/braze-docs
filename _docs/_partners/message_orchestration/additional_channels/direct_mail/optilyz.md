---
nav_title: optilyz
article_title: optilyz
page_order: 1
description: "This article outlines the partnership between Braze and optilyz, which enables you to run more customer-centric, sustainable, and profitable direct mail campaigns."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz Direct Mail Automation

> [optilyz][1] is a direct mail automation platform that enables you to run more customer-centric, sustainable, and profitable direct mail campaigns. optilyz is used by hundreds of companies across Europe and empowers you to integrate letters, postcards, and self-mailers into your cross-channel marketing as well as automate and better personalize campaigns.

Use the optilyz and Braze webhook integration to send direct mail to your customers.

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| optilyz API Key<br><br>`OPTILYZ_API_KEY`| optilyz | Your optilyz customer success manager will provide you with your optilyz API key. | This API key will enable you to connect your Braze and optilyz accounts. |
| optilyz Automation ID<br><br>`OPTILYZ_AUTOMATION_ID` | optilyz | The automation ID can be found in a box on the page header. | When logged into optilyz, you can navigate to the automation you want to send data into.<br><br>The automation must be activated first. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

To integrate with optilyz, use the [optilyz API][2] to send recipient data to the Braze webhook.

### Step 1: Create a Webhook Template in Braze

To create a webhook template, from the Braze dashboard, navigate to __Templates & Media__ and select __Blank Template__ under __Webhook Templates__. Name your template.

### Step 2: Fill Out Your Template

In your new Webhook template, fill out the following fields:

- `Webhook URL`: https://www.optilyz.com/api/v2/automations/OPTILYZ_AUTOMATION_ID/recipient
- `Request Body`: Raw Text

In the following request body, you can use any Liquid personalization tags and build a custom request template according to optilyz' [API documentation][2].

The `variation` field is optional and can be used to define which design inside the automation should be used. If a variation is omitted, optilyz will assign one of the defined variations randomly.

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

### Step 3: Define Request Headers and HTTP Method

optilyz also requires an HTTP Header for authorization and an HTTP method. In the __Settings__ tab of the webhook editor, create a key-value pair and replace the `OPTILYZ_API_KEY` with your optilyz API key.

- `HTTP Method`: POST
- `Request Headers`:
  - `Authorization`: {% raw %} `{{ 'OPTILYZ_API_KEY:' | base64_encode }}` {% endraw %}
  - `Content-Type`: application/json

![optilyz_settings][6]{: style="max-width:50%"}

### Step 4: Preview Your Request and Save Your Template

Next, preview your request in the left-hand panel or navigate to the __Test__ tab, where you can select a random user, an existing user, or customize your own to test your webhook. Remember to save your template before leaving the page!

![optilyz_testing][7]{: style="max-width:80%"}

## Using This Integration

Create a campaign, select __Webhook__, and choose your template from the __Saved Webhook Template__ list.<br>For more information, check out our documentation on [Webhooks][9]!

## Use Cases

Running direct mail like a digital channel means moving away from mass mailings and leveraging the channel as part of your (digital) customer journeys.

Reach out to your optilyz customer success manager if you're interested in understanding how companies in your industry leverage letters, postcards, and more to enhance their customer experience. Our best practice and benchmark database help us assist you in setting up high-performing automation. These may be geared at converting one-time buyers into loyal fans, exciting your most valuable customers, and preventing churn.

The benefits of a modern approach to direct mail are:
- Increased conversion rates via increased relevance, additional use cases, easier A/B testing & cross-channel effects
- Reduced effort via automation & an end-to-end solution
- Reduced cost via frame contracts & cost transparency

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/