The following table lists the possible `abort_type` values. An abort type describes the specific reason a message was not sent.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### General

These abort types can occur on any messaging channel.

| `abort_type` value | Description |
| --- | --- |
| `liquid_abort_message` | The [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) Liquid tag was called, so the send was canceled. |
| `template_parse_error` | The message template could not be parsed due to a syntax or rendering error, so the send was canceled. |
| `quiet_hours` | The message was suppressed because it fell within [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) with the fallback set to abort. |
| `rate_limit` | The message was aborted because it exceeded the configured [rate limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). |
| `no_longer_in_availability_window` | The message could not be sent within the configured availability window, so it was aborted. |
| `campaign_disabled` | The campaign was disabled before the message could be sent. |
| `campaign_does_not_exist` | The campaign associated with this message no longer exists. |
| `campaign_action_does_not_exist` | The campaign action associated with this message no longer exists. |
| `message_variation_does_not_exist` | The message variation assigned to this user no longer exists. |
| `user_not_in_segment` | The user is not in the target segment, so the message was not sent. |
| `trigger_event_blacklisted` | The trigger event is blocklisted, so the message was not sent. |
| `exhausted_retries` | The message could not be sent after the maximum number of retry attempts. |
| `connected_content_not_supported` | [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) is not supported in this context, so the message was aborted. |
| `promo_codes_not_supported` | Promotion codes are not supported in this context, so the message was aborted. |
| `catalog_items_rerender_not_supported` | Catalog item re-rendering is not supported in this context, so the message was aborted. |
| `frequency_capped` | The user already received the maximum number of messages allowed by your workspace's [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) rules. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "banner" or ch == "newsfeedcard" or ch == "rcs" %}

### Content and rendering

| `abort_type` value | Description |
| --- | --- |
| `exhausted_cc_retries` | Connected Content failed after the maximum number of retries, so the message was aborted. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | The media URL is blocklisted and cannot be used in messages. |
| `blocked_media_url` | The media URL was blocked by security policies. |
| `invalid_media_url` | The media URL is not valid or could not be resolved. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | An SSL error occurred while making a request. |
| `invalid_http_status` | An HTTP request returned a non-successful status code. |
| `http_timeout` | An HTTP request timed out before receiving a response. |
| `missing_hostname` | The request URL is missing a hostname. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### Email

| `abort_type` value | Description |
| --- | --- |
| `exhausted_link_shortening_retries` | Link shortening failed after the maximum number of retries. |
| `no_email_body_content` | The email body is empty and cannot be sent. |
| `missing_email` | The user does not have an email address on their profile. |
| `invalid_domain` | The email address has an invalid domain. |
| `invalid_email_address_after_decryption` | The email address was invalid after being decrypted. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| `abort_type` value | Description |
| --- | --- |
| `invalid_push_payload` | The push notification payload is invalid or malformed. |
| `sdk_not_supported` | The SDK version on the user's device does not support this type of push notification. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| `abort_type` value | Description |
| --- | --- |
| `exhausted_link_shortening_retries` | Link shortening failed after the maximum number of retries. |
| `sms_empty_payload` | The SMS message body is empty. |
| `sms_no_sending_numbers` | No sending phone numbers are available for this subscription group. |
| `sms_fatal_provider_error` | A fatal error occurred with the SMS provider, preventing message delivery. |
| `sms_gateway_domain_not_allowed` | The SMS gateway domain is not on the allowlist. |
| `blocked_recipient_country` | The recipient's phone number is in a country that is blocked by your [geographic permissions]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/). |
| `mms_not_supported` | MMS is not supported for this recipient or sending number. |
| `No current Messaging Service` | No active messaging service is configured for this subscription group. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| `abort_type` value | Description |
| --- | --- |
| `whats_app_no_sending_numbers` | No sending phone numbers are available for this WhatsApp subscription group. |
| `whats_app_invalid_template_message` | The WhatsApp template message is invalid or not approved. |
| `whats_app_invalid_response_message` | The WhatsApp response message is invalid. |
| `whats_app_fatal_provider_error` | A fatal error occurred with the WhatsApp provider, preventing message delivery. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| `abort_type` value | Description |
| --- | --- |
| `line_fatal_provider_error` | A fatal error occurred with the LINE provider, preventing message delivery. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| `abort_type` value | Description |
| --- | --- |
| `kakao_fatal_provider_error` | A fatal error occurred with the Kakao provider, preventing message delivery. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Content Cards

| `abort_type` value | Description |
| --- | --- |
| `content_card_size_exceeded` | The Content Card payload exceeds the maximum size limit (2 KB). |
| `content_card_content_invalid` | The Content Card content is invalid or contains unsupported characters. |
| `content_card_expiration_invalid` | The Content Card expiration date is invalid. |
| `content_card_general` | The Content Card could not be created due to a general error. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### In-app messages

| `abort_type` value | Description |
| --- | --- |
| `maximum_impressions_reached` | The in-app message has already reached its maximum number of impressions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| `abort_type` value | Description |
| --- | --- |
| `blocked_webhook_url` | The webhook URL was blocked by security policies. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}
