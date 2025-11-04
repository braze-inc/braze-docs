---
nav_title: "Content card object"
article_title: Content Card Messaging Object
page_order: 4
page_type: reference
channel: content cards
description: "This reference article explains the different components of the Braze Content Card object."

---

# Content Card object

> The `content_card` object allows you to create Content Cards through our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

```json
{
  "type": (required, string) one of "CLASSIC", "CAPTIONED_IMAGE", or "BANNER",
  "title": (required, string) the card's title,
  "description": (required, string) the card's description,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Content Card Message),
  "pinned": (optional, boolean) whether the card is pinned. Defaults to false,
  "image_url": (optional, string) the card's image URL. Required for "CAPTIONED_IMAGE" and "BANNER",
  "time_to_live": (optional, integer) the number of seconds before the card expires. You must include either "time_to_live" or "expire_at",
  "expire_at": (optional, string) ISO 8601 date when the card expires. You must include either "time_to_live" or "expire_at", a maximum expiration time exists of 30 days,
  "expire_in_local_time": (optional, boolean) if using "expire_at", determines whether the card should expire in users' local time. Defaults to false,
  "ios_uri": (optional, string) a web URL, or Deep Link URI,
  "android_uri": (optional, string) a web URL, or Deep Link URI,
  "web_uri": (optional, string) a web URL, or Deep Link URI,
  "ios_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "android_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "uri_text": (optional, string) the card's link text,
  "extra": (optional, object) additional keys and values sent with the card,
}
```

{% alert important %}
Currently, Braze supports a maximum expiration time of 30 days.
{% endalert %}
