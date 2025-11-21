---
nav_title: API usage alerts
article_title: API Usage Alerts
description: "This article provides an overview of the API usage alerts, which allows you to proactively detect unexpected traffic."
page_order: 3.6
---

# API usage alerts

> API usage alerts provide critical visibility into your API usage, allowing you to proactively detect unexpected traffic. By setting up these alerts to track key API request volumes, you can receive real-time notifications and address problems before they impact your marketing campaigns.

## About API usage alerts

You can use API usage alerts to monitor request volumes for the following categories:

| API Category | Details |
|--------------|---------|
| REST API Endpoints | Tracks usage of all REST API calls made to Braze’s backend, such as sending messages, creating campaigns, or exporting users. |
| SDK API Requests | Tracks API requests made from Braze SDKs in client apps, such as triggering in-app messages or syncing user data.<br><br>_*Only available to customers who have purchased Monthly Active Users – CY 24–25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Creating an API usage alert

To create an API usage alert:

1. Go to **Settings** > **APIs and Identifiers** > **API Usage Alerts**, then create a new alert.
2. Enter a name for your alert and choose the REST API endpoints and API keys you'd like to be alerted for.
3. Define your alert criteria by choosing one or more response codes and specifying the [alert thresholds](#api-usage-alert-thresholds).
4. When you're finished, toggle **Alert enabled**.
    ![An example of an API usage alert that sends notifications when the Track users endpoint increases by 100 percent within one hour.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Alert thresholds {#api-usage-alert-thresholds}

When you define your alert criteria you can adjust the following thresholds:

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Threshold condition</td>
      <td>
        Defines the conditions leading up to the threshold volume that you’d like to be alerted on. The following are supported:<br><br>
        <ul>
          <li><strong>Increased by</strong> or <strong>Decreased by</strong>: Compares requests against the previous time window.</li>
          <li><strong>Increased by percentage</strong> or <strong>Decreased by percentage</strong>: Compares the percentage change in requests against the previous time window.</li>
          <li><strong>Greater than or equal</strong>, or <strong>less than or equal</strong>: Counts requests in a time window.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Threshold volume</td>
      <td>Used in conjunction with threshold condition.</td>
    </tr>
    <tr>
      <td>Within</td>
      <td>The time window for alert evaluation.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Setting up alert notifications

You can set up an email alert, a webhook alert or both. Webhook alerts can be very useful for use cases such as sending an alert to external platforms, such as a Slack channel. For an example, see our [documentation](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) on integrating alerts with Slack for our notification preferences.

![An email will be sent to the selected email when the criteria for the alert is reached.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Sample payload {#payload}

The following is a sample payload for the body of an API Usage Alert webhook.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Example alerts

Here are some ways to set up your API usage alert configurations to be notified in the following scenarios.

{% tabs local %}
{% tab api health %}
You can set up alerts to monitor the general health of your API. For example, you can set up these alerts when API errors increase drastically, such as 20% from the previous hour.

| Endpoint | API key | Response code | Threshold condition | Threshold volume | Within |
| --- | --- | --- | --- | --- | --- |
| All endpoints | All API keys | `4XX` and `5XX` | Increased by 10% | 10 | 1 hour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Be alerted when your workspace reaches its rate limit for `/users/track` endpoint. You can also apply this configuration for other Braze endpoints.

| Endpoint | API key | Response code | Threshold condition | Threshold volume | Within |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | All API keys | `429` | Greater than or equal to | 100 | 1 hour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
This alert configuration notifies you when errors occur for API triggered campaigns and Canvases, some of which may be high-priority.

| Endpoint | API key | Response code | Threshold condition | Threshold volume | Within |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | All API keys | `4XX` and `5XX` | Greater than or equal to | 1 | 1 hour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Use the following alert configuration to be alerted when a partner integration stops sending data to Braze.

| Endpoint | API key | Response code | Threshold condition | Threshold volume | Within |
| --- | --- | --- | --- | --- | --- |
| All endpoints | The API key used for your partner integration | All response codes | Less than or equal to | 0 | 1 day |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Considerations

- Each active alert will only send an email or webhook notification once every 8 hours. This is to prevent too many notifications from a single alert. If your alert is notifying you prematurely, consider editing the alert criteria to better match your use case.
- You can have up to 10 alerts per workspace.
