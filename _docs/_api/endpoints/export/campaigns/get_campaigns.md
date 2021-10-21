---
nav_title: "GET: Campaigns List"
article_title: "GET: Campaigns Lists"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Get Campaigns List endpoint."

---
{% api %}
# Campaigns list endpoint
{% apimethod get %}
/campaigns/list
{% endapimethod %}

This endpoint allows you to export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer   | The page of campaigns to return, defaults to 0 (returns the first set of up to 100). |
| `include_archived` | Optional | Boolean | Whether or not to include archived campaigns, defaults to false. |
| `sort_direction` | Optional | String | - Sort creation time from newest to oldest: pass in the value `desc`.<br> - Sort creation time from oldest to newest: pass in the value `asc`. <br><br>If `sort_direction` is not included, the default order is oldest to newest. |
| `last_edit.time[gt]` | Optional | Time | Filters the results and only returns campaigns that were edited greater than the time provided till now. Format is `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request 
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Campaign list endpoint api response

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
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
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
