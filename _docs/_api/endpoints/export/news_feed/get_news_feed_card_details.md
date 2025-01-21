---
nav_title: "GET: Export News Feed Card Details"
article_title: "GET: Export News Feed Card Details"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export News Feed card details Braze endpoint."

---
{% api %}
# Export News Feed card details
{% apimethod get %}
/feed/details
{% endapimethod %}

> Use this endpoint to retrieve relevant information on a card, which can be identified by the `card_id`.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `feed.details` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Required | String | See [Card API identifier]({{site.baseurl}}/api/identifier_types/). <br><br> The `card_id` for a given card can be found on the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page and on the card details page within your dashboard, or you can use the [Export News Feed cards list endpoint]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
