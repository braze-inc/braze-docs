---
nav_title: "POST: Trigger sync"
article_title: "POST: Trigger Sync"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "This article outlines details about the Trigger sync Braze endpoint."

---
{% api %}
# Trigger a sync
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Use this endpoint to trigger a sync for a given integration.

{% alert note %}
To use this endpoint, you'll need to generate an API key with the `cdi.integration_sync` permission.
{% endalert %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `integration_id` | Required | String | Integration ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Example request

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Response

### Example success response

The status code `202` could return the following response body:

```json
{
  "message": "success"
}
```

## Troubleshooting

The following table lists possible returned errors and their associated troubleshooting steps.

| Error | Troubleshooting |
| --- | --- |
| `400 Invalid integration ID` | Check that your `integration_id` is valid. |
| `404 Integration not found` | No integration exists for the given integration ID. Make sure that your integration ID is valid. |
| `429 Another job is in progress` | There is a sync currently running for this integration. Try again after the sync has completed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For additional status codes and associated error messages, please refer to [Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
