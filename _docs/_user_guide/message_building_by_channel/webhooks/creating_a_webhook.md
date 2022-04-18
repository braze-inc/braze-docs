---
nav_title: Creating a Webhook
article_title: Creating a Webhook
page_order: 1
channel:
  - webhooks
description: "This reference article covers how to create and configure a webhook, as well as how to utilize them to with certain Braze technology partners."

---

# Creating a webhook

Creating a webhook campaign or including a webhook in a multichannel campaign allows you to trigger non-app actions. More specifically, [webhooks][14] can be used to provide other systems and applications with real-time information. You can use webhooks to send information to systems such as Salesforce or Marketo. You can also use webhooks to send information to your backend systems. For example, you might want to credit your customers' accounts with a promotion once they've performed a custom event a certain number of times.

If you want to learn more about what webhooks are and how you can use them in Braze, check out [About webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) before proceeding.

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **Webhook**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different webhook templates for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Compose your webhook

You can choose to build a webhook from scratch or use one of our existing templates. Then, build your webhook in the **Compose** tab of the editor.

![Compose tab when creating a webhook in Braze]({% image_buster /assets/img_archive/webhook_compose.png %})

The **Compose** tab consists of the following fields:

#### Language {#internationalization}

[Internationalization][16] is supported in the URL and the request body. To internationalize your message, click **Add Languages** and fill out the flyout. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. See our full list of [available languages]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

#### Webhook URL

The webhook URL, or HTTP URL, specifies your endpoint. The endpoint is the place where you'll be sending the information that you're capturing in the webhook. If you'd like to send information to a vendor, the vendor should provide this URL in their API documentation. If you're sending information to your own systems, check with your development or engineering team to ensure that you're using the correct URL. 

Braze only allows URLs that communicate over standard ports `80` (HTTP) and `443` (HTTPS).

You can personalize your webhook URLs using [Liquid][15]. At times, certain endpoints may require you to identify a user or provide user-specific information as part of your URL. When using Liquid, make sure to include a [default value][19] for each piece of user-specific information that you use in your URL.

#### Request body

The request body is the information that will be sent to the URL that you specified. There are two ways to create the body of your webhook request:

##### JSON key-value pairs

JSON key-value pairs allow you to easily write a request for an endpoint that expects a JSON format. You can only use this feature with an endpoint that expects a JSON request. For example, if your key is `message_body`, the corresponding value might be `Your order just arrived!`. After you've entered your key-value pair, the composer will configure your request in JSON syntax, and a preview of your JSON request will automatically populate.

![Request body set to JSON key-value pairs][21]

You can personalize your key-value pairs using [Liquid][15], such as including any user attribute, [custom attribute][17], or [event property][18] in your request. For example, you can include a customer's first name and email in your request. Don’t forget to include a [default value][19] for each attribute!

##### Raw text

The raw text option gives you the flexibility to write a request for an endpoint that expects a body of any format. For example, you might use this feature to write a request for an endpoint that expects your request to be in XML format. Both [personalization][15] and [internationalization][16] using Liquid is supported in raw text.

![Request body set to raw text][22]

## Step 3: Configure additional settings

#### Request headers (optional)

Certain endpoints may require that you include headers in your request. In the **Settings** section of the composer, you can add as many headers as you'd like. Common request headers are content-type specifications (which describe what type of data to expect in the body, such as XML or JSON) and authorization headers that contain your credentials with your vendor or system. 

Content type specifications must use the key `Content-Type`. Common values are `application/json` or `application/x-www-form-urlencoded`.

Authorization headers must use the key `Authorization`. Common values are {% raw %} `Bearer {{YOUR_TOKEN}}` or `Basic {{YOUR_TOKEN}}` {% endraw %} where `YOUR_TOKEN` is the credentials provided by your vendor or system.

#### HTTP method

The [HTTP method]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) that you should use will vary depending on the endpoint to which you are sending information. The majority of the time, you'll be using POST.

![Specify request headers and HTTP method in the Settings tab of the composer][26]

## Step 4: Test send your message

Before making your campaign go live, Braze recommends that you test the webhook to make sure the request is formatted properly.

To do so, switch to the **Test** tab and send a test webhook. You can test the webhook as a random user, a specific user (by entering their email address of external user ID), or a customized user with attributes of your choosing.  

After sending the test webhook, a dialog will appear with the response message. If the webhook request is unsuccessful, refer to the error message for assistance in troubleshooting your webhook. The following example details the response of a webhook with an invalid webhook URL.

![Webhook 404 error for an unrecognized request URL][64]

## Step 5: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. See the following sections for further details on how to best utilize our tools to build webhooks.

#### Choose delivery schedule or trigger

Webhooks can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) by choosing segments or filters to narrow down your audience. In this step, you will select the larger audience from your segments, and narrow that segment further with our filters, if you choose. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas step. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 6: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, test it, then send it!

## Things to know

### Errors, retry logic, and timeouts

Webhooks rely on Braze's servers making requests to an external endpoint, and syntax and other errors may arise. The first step to avoiding webhook errors is to test your webhook campaign for syntax errors and to make sure that personalized variables have a default value. However, webhooks may still fail due to issues like expired API keys, rate limits, or unexpected server errors. If your webhook fails to send, an error message gets logged to the [Developer Console][42], under **Message Activity Log**. This description contains the time the error occurred, the app name, and the error message:

![Webhook error with the message "An active access toekn must be used to query information about the current user"][43]

If the message body is not clear enough regarding the source of the error, you should check the documentation of the API endpoint you're using. These typically provide an explanation of the error codes the endpoint uses as well as what they're typically caused by.

Like other campaigns, Braze tracks the delivery of your webhook campaigns and conversions resulting from them. When the webhook request is sent, the receiving server will return a response code indicating what happened with the request. The following table summarizes the different responses the server may send, how they impact campaign analytics and whether, in the case of errors, Braze will try to redeliver the campaign:

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

### IP whitelisting {#ip-whitelisting}

When a webhook is sent from Braze, the Braze servers make network requests to our customers or third parties servers. With IP whitelisting, you can verify that Webhooks requests are actually coming from Braze, adding an additional layer of security.

Braze will send webhooks from the following IP ranges. The listed ranges are automatically and dynamically added to any API keys that have been opted-in for whitelisting.

{% alert important %}
If you're making a Braze-to-Braze webhook and using whitelisting, you should whitelist all the following IPs, including `127.0.0.1`.
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

| For Instances `EU-01` and `EU-02`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

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

### Using webhooks with Braze partners {#utilizing-webhooks}

There are many ways to utilize webhooks, and with Braze's technology partners (Alloys), you can use webhooks to uplevel your communication directly with your customers and users.

Check out:
* [Messenger]({{site.baseurl}}/partners/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/advertising_technologies/retargeting/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels/direct_mail/lob/)
* And many more of our [technology partners]({{site.baseurl}}/partners/home/)!

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[21]: {% image_buster /assets/img/webhook_json_1.png %}
[22]: {% image_buster /assets/img_archive/webhook_rawtext.png %}
[26]: {% image_buster /assets/img_archive/webhook_request_header.png %}
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/
[43]: {% image_buster /assets/img_archive/webhook-error.png %}
[64]: {% image_buster /assets/img_archive/webhook_test_send.png %}
