---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "This article outlines the partnership between Braze and Lob.com, which allows you to send direct mail like letters, postcards, and checks through the mail."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] is an online service that allows you to send direct mail to your users.

The Braze and Lob integration leverages Braze webhooks and the Lob API to send mail like letters, postcards, and checks through the mail.  

## Prerequisites

|Requirement| Description|
| ---| ---|
|Lob account | A Lob account is required to take advantage of this partnership. |
| Lob API key | You Lob API key can be found under the settings section under your name in the Lob dashboard. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Select Lob endpoint

The HTTP URL to request in the webhook is different for each action you can make to Lob. In the following example, we use the postcards API endpoint `https://api.lob.com/v1/postcards`. Visit the [complete endpoint list][39] to select the endpoint appropriate for your use case. 

| API endpoint | Available endpoints |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2}

### Step 2: Create your Braze webhook template

To create a Lob webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section in the Braze platform. If you would like to make a one-off Lob webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:
- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Request Body**: Raw Text

#### Request headers and method

Lob requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab, you must replace the `<LOB_API_KEY>` with your Lob API key. This key must include a ":" directly after the key and be encoded in base 64. 

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Request body code and webhook URL shown in the Braze webhook builder compose tab.][35]

#### Request body

The following is an example request body for the Lob postcards endpoint. While this request body is provided in the base Lob template in Braze, if you wish to use other endpoints, you must adjust your Liquid fields accordingly.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Step 3: Preview your request

At this point, your campaign should be ready to test and send. Check the Lob dashboard and the Braze developer console error message logs if you run into errors. For example, the following error was caused by an incorrectly formatted authentication header. 

![A message error log showing the time, app name, channel, and error message. The error message includes the message alert and the status code.][36]

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth
