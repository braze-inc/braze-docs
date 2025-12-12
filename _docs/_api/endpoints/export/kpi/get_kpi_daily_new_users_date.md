---
nav_title: "GET: Export daily new users by date"
article_title: "GET: Export Daily News Users by Date"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export daily new users Braze endpoint."

---
{% api %}
# Export daily new users by date
{% apimethod get %}
/kpi/new_users/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of the total number of new users on each date.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `kpi.new_users.data_series` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter| Required | Data Type | Description |
| -------- | -------- | --------- | ----------- |
| `length` | Required | Integer | Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 (inclusive). |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Date on which the data series should end. Defaults to time of the request. |
| `app_id` | Optional | String | App API identifier retrieved from the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page. If excluded, results for all apps in workspace will be returned. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/new_users/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "new_users" : (int) the number of daily new users
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
