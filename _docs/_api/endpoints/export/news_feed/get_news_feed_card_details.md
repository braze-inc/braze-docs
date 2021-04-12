---
nav_title: "GET: News Feed Card Details"
page_order: 4

layout: api_page

page_type: reference
platform: API
channel: News Feed
tool: Segments
description: "This article outlines details about the News Feed Card Details endpoint."
---
{% api %}
# News Feed Card Details Endpoint
{% apimethod get %}
/feed/details
{% endapimethod %}

This endpoint allows you to retrieve relevant information on the card, which can be identified by the `card_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Yes      | String    | Card API Identifier    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Card ID](https://www.braze.com/docs/api/identifier_types/)
- [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)
<br><br>
The `card_id` for a given card can be found in the Developer Console page and on the card details page within your dashboard or you can use the [News Feed List Endpoint]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).

### Example URL
`https://rest.iad-01.braze.com/feed/details?card_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

### Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/details?card_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) Date created as ISO 8601 date,
    "updated_at" : (string) Date last updated as ISO 8601 date,
    "name" : (string) Card name,
    "publish_at" : (string) Date card was published as ISO 8601 date,
    "end_at" : (string) Date card will stop displaying for users as ISO 8601 date,
    "tags" : (array) Tag names associated with the card,
    "title" : (string) Title of the card,
    "image_url" : (string) Image URL used by this card,
    "extras" : (dictionary) Dictionary containing key-value pair data attached to this card,
    "description" : (string) Description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```
{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
