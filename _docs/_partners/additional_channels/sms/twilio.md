---
nav_title: Twilio
alias: /partners/twilio/

description: "This article outlines the partnership between Braze and Twilio."
page_type: partner
---

# Twilio

For this example, we'll configure the Braze webhook channel to send SMS and MMS to your users, via Twilio's [message sending API][20]. For your convenience, a Twilio webhook template is included on the dashboard.

## HTTP URL

The Webhook URL is provided by Twilio in your dashboard. This URL is unique to your Twilio account, since it contains your Twilio account ID (`TWILIO_ACCOUNT_SID`).

In our Twilio example, the webhook URL is `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. You can find this URL in the *Getting Started* section of the Twilio console.

![Twilio_Console][28]

## Request Body

The Twilio API expects the request body to be URL-encoded, so we have to start by changing the request type in the Braze webhook composer to `Raw Text`. The required parameters for the body of the request are *To*, *From* and *Body*.

The screenshot below is an example of what your request might look like if you are sending an SMS to each user’s phone number, with the body "Hello from Braze!".

- You'll need to have valid phone numbers on each user profile in your target audience.
- In order to meet Twilio's request format, use the `url_param_escape` Liquid filter on your message contents. This filter encodes a string so all the characters are allowed in an HTML request; for example, the plus character (`+`) in the phone number `+12125551212` is forbidden in URL-encoded data, and will be converted  to `%2B12125551212`.

![Webhook Body][29]

## Request Headers and Method

Twilio requires two request headers, the request Content-Type and an [HTTP Basic Authentication][32] header. Add them to your webhook by clicking the gear icon on the right side of the webhook composer, then clicking *Add New Pair* twice.

Header Name | Header Value
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authentication | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Be sure to replace `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` with values from your Twilio dashboard. Lastly, Twilio’s API endpoint is expecting an HTTP POST request, so choose that option in the dropdown for *HTTP Method*.

![Webhook Method][30]

## Preview Your Request

Use the webhook composer to preview the request for a random user, or for a user with particular credentials, to ensure that the request is rendering properly.

![Webhook Preview][31]

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[16]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#setting-default-values
[20]: https://www.twilio.com/docs/api/rest/sending-messages
[21]: {% image_buster /assets/img_archive/webhook_JSON1.png %}
[22]: {% image_buster /assets/img_archive/webhook_rawtext.png %}
[26]: {% image_buster /assets/img_archive/Webhook_Request_Header.png %}
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %}
[29]: {% image_buster /assets/img_archive/Webhook_Body.png %}
[30]: {% image_buster /assets/img_archive/Webhook_Method.png %}
[31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side
[41]: https://en.wikipedia.org/wiki/JSON#Example
[42]: https://dashboard-01.braze.com/app_settings/developer_console/
[43]: {% image_buster /assets/img_archive/webhook-error.png %}
[44]: {{ site.baseurl }}/partners/messenger
[45]: https://developers.facebook.com/docs/messenger-platform/product-overview/setup
[46]: https://github.com/Appboy/appboy-fb-messenger-bot
[47]: https://developers.facebook.com/docs/messenger-platform/product-overview/setup#page_access_token
[48]: https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable
[49]: https://developers.facebook.com/docs/messenger-platform/guidelines
[50]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#custom-attributes
[51]: https://developers.facebook.com/docs/messenger-platform/app-review
[52]: {% image_buster /assets/img_archive/fbm-webhook-header.png %}
[53]: {% image_buster /assets/img_archive/fbm-webhook.png %}
[54]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[55]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[56]: {% image_buster /assets/img_archive/fbm-text.png %}
[57]: {% image_buster /assets/img_archive/fbm-image.png %}
[58]: {% image_buster /assets/img_archive/fbm-structured.png %}
[59]: https://developers.facebook.com/docs/messenger-platform/send-api-reference
[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{ site.baseurl }}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[62]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}
[64]: {% image_buster /assets/img_archive/webhook_test_send.png %}
[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
