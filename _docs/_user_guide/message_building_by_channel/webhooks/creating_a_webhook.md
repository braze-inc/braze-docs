---
nav_title: Creating a Webhook
platform: Message_Building_and_Personalization
subplatform: Webhooks
page_order: 1

tool:
  - Dashboard
  - Canvas
  - Campaign

channel:
  - webhooks

description: "This reference article covers how to create and configure a webhook, as well as how to utilize them to with certain Braze technology partners."

---

# Creating a Webhook

## Feature Overview

Creating a webhook campaign or including a webhook in a multi-channel campaign allows you to trigger non-app actions. More specifically, [webhooks][14] can be used to provide other systems and applications with real-time information. You can use webhooks to send information to systems such as Salesforce or Marketo. You can also use webhooks to send information to your backend systems. For example, you might want to credit your customers' accounts with a promotion once they've performed a custom event a certain number of times.

## Step 1: Set Up a Webhook

Add a new webhook message to a Campaign or Canvas. You can then choose to build a webhook from scratch or use one of our existing templates.

## Step 2: Enter the URL for Your Webhook

### HTTP URL
Enter the HTTP URL. This HTTP URL specifies your endpoint. The endpoint is the place where you'll be sending the information that you're capturing in the webhook. If you'd like to send information to a vendor, the vendor should provide this URL in their API documentation. If you're sending information to your own systems, check with your development or engineering team to ensure that you're using the correct URL. Braze only allows URLs that communicate over standard ports 80 (HTTP) and 443 (HTTPS).

### Personalization

[Personalization][15] is supported in our HTTP URLs. At times, certain endpoints may require you to identify a user or provide user-specific information as part of your URL. You'll want to be sure to include a [default value][19] for each piece of user-specific information that you use in your URL.

### Internationalization

[Internationalization][16] is supported in the URL and the request body. To internationalize your message, click 'add languages' and fill out the flyout.

## Step 3: Create the Request Body

Create the body of your webhook request. This is the information that will be sent to the URL that you specified. There are two ways to create the body of your webhook request:

### JSON Key-Value Pairs

JSON key-value pairs allow you to easily write a request for an endpoint that expects a JSON format. Do note that you can only use this feature with an endpoint that expects a JSON request. For example, if your key is "message_body," the corresponding value might be "Your order just arrived." Once you've entered your key-value pair, the composer will configure your request in JSON syntax, and a preview of your JSON request will automatically populate.

![Webhook_JSON][21]

### Raw Text

The raw text option gives you the flexibility to write a request for an endpoint that expects a body of any format. For example, you might use this feature to write a request for an endpoint that expects your request to be in XML format.

![webhook_rawtext][22]

### Personalization

[Personalization][15] is supported in both the JSON key-value pairs option and the raw text option. You can include any user attribute, [custom attribute][17], or [event property][18] in your request. For example, you can include a customer's first name and email in your request. Don’t forget to include a [default value][19] for each attribute.

### Internationalization

[Internationalization][16] is supported in raw text.

## Step 4: Request Headers and HTTP Method

Certain endpoints may require that you include headers in your request. In the settings section of the composer, you can add as many headers as you'd like. Common use cases for request headers include a content-type specification (e.g., XML or JSON) and authorization headers that contain your credentials with your vendor or system. Content type specifications have the key "Content-Type" and common values are "application/json" or "application/x-www-form-urlencoded".

The HTTP method that you should use will vary depending on the endpoint to which you are sending information. The majority of the time, you'll be using POST.

![Webhook_Request_Header][26]

## Step 5: Test Send Your Message

Before making your campaign go live, you may wish to test the webhook to make sure the request is formatted properly. To do so, navigate to the preview tab and send the test webhook. You can test the webhook for a random user, a specific user (by entering their email address of external user ID), or a customized user with attributes of your choosing.  If the request is successful, a small message will appear at the top of your screen. If the webhook request is unsuccessful, a modal will appear with the error response message. The screenshot below is an example of the response of a webhook with an invalid webhook URL.

![Webhook Test Feature][64]

## Step 6: Continue Campaign Creation
Continuing creating your campaign the way that you normally would. As with all of our message types, you can preview what your request will look like for a particular user, random user, or user with specific attributes in the preview section of the webhook composer.

## Errors, Retry Logic, and Timeouts

Webhooks rely on Braze's servers making requests to an external endpoint, and syntax and other errors may arise. The first step to avoiding webhook errors is to test your webhook campaign for syntax errors and to make sure that personalized variables have a default value. However, webhooks may still fail due to issues like expired API keys, rate limits, or unexpected server errors. If your webhook fails to send, an error message gets logged to the [Developer Console][42], under "Message Activity Log." This description contains the time the error occurred, the app name, and the error message:

![Webhook error][43]

If the message body is not clear enough regarding the source of the error, you should check the documentation of the API endpoint you're using. These typically provide an explanation of the error codes the endpoint uses as well as what they're typically caused by.

Like other campaigns, Braze tracks the delivery of your webhook campaigns and conversions resulting from them. When the webhook request is sent, the receiving server will return a response code indicating what happened with the request. The below table summarizes the different responses the server may send, how they impact campaign analytics and whether, in the case of errors, Braze will try to redeliver the campaign:

| Response code | Marked as received? | Retries? |
|---------------|-----------|----------|
| 20x (success)  | Yes |   N/A  |
| 30x (redirection)  | No | No |
| 408 (request timeout)  | No | Yes |
| 429 (rate limited)  | No | Yes |
| Other 4xx (client error)  | No | No |
| 5xx (server error)   | No | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

When retrying, Braze will make five attempts using exponential backoff for a period of approximately 30 minutes before aborting the individual webhook call.

Each webhook is allowed 90 seconds before it times out.

## IP Whitelisting

When a Webhook is sent from Braze, the Braze servers make network requests to our customers or third parties servers.

With IP whitelisting, you can verify that Webhooks requests are actually coming from Braze, adding an additional layer of security.

Braze will send Webhooks from the IP ranges below.

{% alert important %}
  If you're making a Braze-to-Braze webhook and using whitelisting, you should whitelist all the IPs listed above, including `127.0.0.1`.
{% endalert %}

| For Instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, and `US-06`: |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| For Instance `EU-01`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`

| For Instance `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

# Utilizing Webhooks

There are many ways to utilize webhooks, and with Braze's technology partners (Alloys), you can use webhooks to uplevel your communication directly with your customers and users.

Check out:
* [Messenger]({{site.baseurl}}/partners/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/advertising_technologies/retargeting/remerge/)
* [Twilio]({{site.baseurl}}/partners/additional_channels/sms/twilio/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels/direct_mail/lob/)
* And many more in our [technology partners]({{site.baseurl}}/partners/home/) section of Braze Docs!

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[21]: {% image_buster /assets/img/webhook_JSON1.jpg %}
[22]: {% image_buster /assets/img_archive/webhook_rawtext.png %}
[26]: {% image_buster /assets/img_archive/Webhook_Request_Header.png %}
[42]: https://dashboard-01.braze.com/app_settings/developer_console/
[43]: {% image_buster /assets/img_archive/webhook-error.png %}
[64]: {% image_buster /assets/img_archive/webhook_test_send.png %}
