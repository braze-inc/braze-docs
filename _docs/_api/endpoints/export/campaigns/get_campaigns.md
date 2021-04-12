---
nav_title: "GET: Campaigns List"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Segments
description: "This article outlines details about a specified campaign."
---
{% api %}
# Campaigns List Endpoint
{% apimethod get %}
/campaigns/list
{% endapimethod %}

This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Campaign%20export%20%20list%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `page` | No | Integer   | The page of campaigns to return, defaults to 0 (returns the first set of up to 100) |
| `include_archived` | No | Boolean | Whether or not to include archived campaigns, defaults to false |
| `sort_direction` | No | String | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. |
| `last_edit.time[gt]` | No | Time | Filters the results and only returns campaigns that were edited greater than the time provided till NOW. Format is yyyy-MM-DDTHH:mm:ss |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Example URL
`https://{{instance_url}}/campaigns/list?page=0&include_archived=false&sort_direction=desc`

### Example Request 
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Campaign List Endpoint API Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) Campaign API Identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message 
            "name" : (string) campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API Campaign,
            "tags" : (array) tag names associated with the campaign
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
