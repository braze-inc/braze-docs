---
nav_title: "GET: Retrieve Link Aliases (Canvas)"
layout: api_page
page_type: reference
hidden: true
alias: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "This article outlines details about the GET Link Alias endpoint, which allows you to fetch the aliases set on a Canvas Email step."
---
{% api %}
# Canvas Link Alias Endpoint
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

Use this endpoint to list the link alias set in a particular Email Canvas step.

{% apiref postman %}  {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `canvas_step_id`  | Yes | String | Canvas Step API identifier. |
| `message_variation_id `  |  Yes | String | Message variant API identifier (for the Email message variant in that step). |
| `includes_link_id` | No | String | A specific link identifier (as assigned by Braze) or `null`. This is used to filter the results by a specific `link_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Example Request

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

- `Missing/Invalid Canvas ID` - The Canvas API ID must be an API identifier. You can find this using the [Canvas List Endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) or by logging into the Dashboard.

- `Missing/Invalid Message Variant ID` - The Message Variant API ID must be an API identifier. You can find this using the [Canvas Details Endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) or by logging into the Dashboard.


{% endapi %}
