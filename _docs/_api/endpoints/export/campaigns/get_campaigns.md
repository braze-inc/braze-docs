---
nav_title: "GET: Export campaigns list"
article_title: "GET: Export Campaigns List"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export campaigns list Braze endpoint."

---
{% api %}
# Export campaigns list
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> Use this endpoint to export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign.

The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `campaigns.list` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | The page of campaigns to return, defaults to 0 (returns the first set of up to 100). |
| `include_archived` | Optional | Boolean | Whether or not to include archived campaigns, defaults to false. |
| `sort_direction` | Optional | String | - Sort creation time from newest to oldest: pass in the value `desc`.<br> - Sort creation time from oldest to newest: pass in the value `asc`. <br><br>If `sort_direction` is not included, the default order is oldest to newest. |
| `last_edit.time[gt]` | Optional | Time | Filters the results and only returns campaigns that were edited greater than the time provided till now. Format is `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
