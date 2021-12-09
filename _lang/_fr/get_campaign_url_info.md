---
nav_title: "GET: Retrieve Link Aliases (Campaign)"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/
platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns
description: "This article outlines details about the GET Link Alias endpoint, which allows you to fetch the aliases set on a campaign message variant."
---

{% api %}
# Campaign Link Alias Endpoint
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

Use this endpoint to list the link alias set in a particular campaign message variant.

{% apiref postman %}  {% endapiref %}

## Request Parameters

| Parameter              | Required | Data Type | Description                                                                                                                          |
| ---------------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `campaign_id`          | Required | String    | See [campaign API identifier]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier).                                       |
| `message_variation_id` | Required | String    | Message variant API identifier. You can find this on the campaign details page for a campaign, under the **API Identifier** section. |
| `includes_link_id`     | Optional | String    | A specific link identifier (as assigned by Braze) or `null`. This is used to filter the results by a specific `link_id`.             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Request
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Possible Errors

- `Missing/Invalid Campaign ID` - The Campaign API ID must be an API identifier. You can find this using the [Campaigns List Endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) or by logging into the dashboard.

- `Missing/Invalid Message Variant ID` - The Message Variant API ID must be an API identifier. You can find this using the [Campaign Details Endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) or by logging into the dashboard.


{% endapi %}
