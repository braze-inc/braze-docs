---
nav_title: "POST: Rename External ID"
article_title: "POST: Rename External ID"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the Rename external IDs endpoint."

---
{% api %}
# Rename external ID
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Use this endpoint to rename your users' external IDs. 

You can send up to 50 rename objects per request. You will need to create a new [API key]({{site.baseurl}}/api/api_key/) with permissions for this endpoint.

This endpoint sets a new (primary) `external_id` for the user and deprecates their existing `external_id`. This means that the user can be identified by either `external_id` until the deprecated one is removed. Having multiple external IDs allows for a migration period so that older versions of your apps that use the previous external ID naming schema don't break. 

After your old naming schema is no longer in use, we highly recommend removing deprecated external IDs using the [`/users/external_ids/remove` endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Make sure to remove deprecated external IDs with the `/users/external_ids/remove` endpoint instead of `/users/delete`. Sending a request to `/users/delete` with the deprecated external ID deletes the user profile entirely and cannot be undone.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Required | Array of external identifier rename objects | View request example and the following limitations for the structure of the external identifier rename object. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- The `current_external_id` must be the user's primary ID, and cannot be a deprecated ID
- The `new_external_id` must not already be in use as either a primary ID or a deprecated ID
- The `current_external_id` and `new_external_id` cannot be the same

## Request example
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Response 
The response will confirm all successful renames, as well as unsuccessful renames with any associated errors. Error messages in the `rename_errors` field will reference the index of the object in the array of the original request.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

The `message` field will return `success` for any valid request. More specific errors are captured in the `rename_errors` array. The `message` field returns an error in the case of:
- Invalid API key
- Empty `external_id_renames` array
- `external_id_renames` array with more than 50 objects
- Rate limit hit (more than 1,000 requests/minute)

## Frequently asked questions

**Does this impact MAU?**<br>
No, since the number of users will stay the same, they'll just have a new `external_id`.

**Does user behavior change historically?**<br>
No, since the user is still the same, and all their historical behavior is still connected to them.

**Can it be run on dev/staging workspaces?**<br>
Yes. In fact, we highly recommend running a test migration on a staging or development workspace, and ensuring everything has gone smoothly before executing on production data.

**Does this consume data points?**<br>
This feature does not cost data points.

**What is the recommended deprecation period?**<br>
We have no hard limit on how long you can keep deprecated external IDs around, but we highly recommend removing them once there is no longer a need to reference users by the deprecated ID.

{% endapi %}
