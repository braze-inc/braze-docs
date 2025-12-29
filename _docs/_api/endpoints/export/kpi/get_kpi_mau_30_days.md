---
nav_title: "GET: Export monthly active users for last 30 days"
article_title: "GET: Export Monthly Active Users for Last 30 Days"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export monthly active users Braze endpoint."

---
{% api %}
# Export monthly active users for last 30 days
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> Use this endpoint to retrieve a daily series of the total number of unique active users over a 30-day rolling window.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `kpi.mau.data_series` permission.

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
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
