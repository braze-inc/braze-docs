---
nav_title: "GET: List integrations"
article_title: "GET: List Integrations"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "This article outlines details about the List integrations Braze endpoint."

---
{% api %}
# List integrations
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> Use this endpoint to return a list of existing integrations.


{% alert note %}
To use this endpoint, you'll need to generate an API key with the `cdi.integration_list` permission.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Query parameters

Each call to this endpoint will return 10 items. For a list with more than 10 integrations, use the `Link` header to retrieve the data on the next page as shown in the example response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `cursor` | Optional | String | Determines the pagination of the integration list. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example request

### Without cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### With cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

### Example success response

The status code `200` could return the following response body.

{% alert note %}
The `Link` header won't exist if there are less than or equal to 10 integrations in total. For calls without a cursor, `prev` will not show. When looking at the last page of items, `next` will not show.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `400 Invalid cursor` | Check that your `cursor` is valid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For additional status codes and associated error messages, refer to [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
