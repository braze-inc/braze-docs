## Retrieving your integration ID

To retrieve your `integration_id`, you can use one of the following methods:

### From the Braze dashboard

Navigate to **Data Settings** > **Cloud Data Ingestion** and select your integration. The `integration_id` is located in the URL of the integration details page. For example, in the URL `https://dashboard.braze.com/integrations/cloud_data_ingestion/00000000-0000-0000-0000-000000000000`, the `integration_id` is `00000000-0000-0000-0000-000000000000`.

### Using the List integrations API

You can also retrieve your `integration_id` by calling the [GET: List integrations endpoint]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/). The response includes the `integration_id` for each integration in your workspace.

```json
{
  "results": [
    {
      "integration_id": "00000000-0000-0000-0000-000000000000",
      "app_group_id": "12345678-1234-1234-1234-123456789012",
      "integration_name": "my_integration_name",
      "integration_type": "SNOWFLAKE",
      "integration_status": "ACTIVE",
      ...
    }
  ],
  "message": "success"
}
```
