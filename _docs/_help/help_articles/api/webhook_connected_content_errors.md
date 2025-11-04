---
nav_title: Troubleshooting webhook and connected content requests
article_title: Troubleshooting Webhook and Connected Content Requests
page_order: 3
channel:
  - webhooks
description: "This article covers how to troubleshoot webhook and Connected Content error codes, including what the errors are and steps to resolve them."
---

# Troubleshooting webhook and Connected Content requests

> This article covers how to troubleshoot common error codes for webhooks and Connected Content, and provides further explanations on how these errors can occur in your requests.

## 4XX errors

`4XX` errors indicate that there's an issue with the request sent to the endpoint. These errors are typically caused by erroneous requests, including malformed parameters, missing authentication headers, or incorrect URLs.

Refer to the following table for error code details and steps to resolve:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Error code</th>
      <th>What it means</th>
      <th>Steps to resolve</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>There's invalid syntax in the request.</td>
      <td>
        <ul>
          <li>Check the request payload for any syntax errors.</li>
          <li>Confirm that all required fields are included and correctly formatted.</li>
          <li>If you're sending a JSON payload, validate the JSON structure.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>The request requires user authentication.</td>
      <td>
        <ul>
          <li>Verify that the correct authentication credentials (such as API keys or tokens) are included in the request headers.</li>
          <li>Confirm that you have the user permissions to access the endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>The endpoint understands the request but refuses to authorize it.</td>
      <td>
        <ul>
          <li>Check if the API key or token has the required permissions.</li>
          <li>Confirm that you have the user permissions to access the endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>The endpoint cannot find the requested resource.</td>
      <td>
        <ul>
          <li>Check the endpoint URL for any typos or incorrect paths.</li>
          <li>Confirm that the resource you're trying to access exists.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>The request method is known by the endpoint but is not supported by the target resource.</td>
      <td>
        <ul>
          <li>Check the HTTP method (DELETE, GET, POST, PUT) used in the request.</li>
          <li>Confirm that the endpoint supports the method you're using.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>The endpoint timed out processing the request.</td>
      <td>
        <ul>
          <li>Check the HTTP method (DELETE, GET, POST, PUT) used in the request.</li>
          <li>Confirm that the endpoint supports the method you're using.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>The request is incomplete because of a conflict with the current state of the resource.</td>
      <td>
        <ul>
          <li>Check the HTTP method (DELETE, GET, POST, PUT) used in the request.</li>
          <li>Confirm that the endpoint supports the method you're using.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>There are too many requests sent in a given amount of time.</td>
      <td>
        <ul>
          <li>Lower the rate limit on your campaign or Canvas step.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX errors

`5XX` errors indicate that there's an issue with the endpoint. These errors are typically caused by server-side issues.

| Error code                    | What it means                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | The endpoint encountered an unexpected condition that prevented it from completing the request.                                                       |
| **502 Bad Gateway**           | The endpoint received an invalid response from the upstream server.                                                                                   |
| **503 Service Unavailable**   | The endpoint is currently unable to handle the request due to a temporary overload or maintenance.                                                    |
| **504 Gateway Timeout**       | The endpoint didn't receive a timely response from the upstream server.                                                                               |
| **529 Host Overloaded**       | The endpoint host is overloaded and could not respond. |
| **598 Host Unhealthy**        | Braze simulated the response because the endpoint host temporarily is marked as unhealthy. See [Unhealthy host detection](#unhealthy-host-detection) to learn more. |
| **599 Connection Error**      | Braze experienced a network connect timeout error while trying to establish a connection to the endpoint, meaning the endpoint may be unstable or down. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolving 5XX errors

Here are tips for troubleshooting common `5XX` errors:

- Review the error message for specific details available in the **Message Activity Log**. For webhooks, go to the **Performance Over Time** section on the Braze home page and select the statistics for webhooks. From here, you can find the timestamp that indicates when the errors occurred.
- Make sure you're not sending too many requests that overload the endpoint. You can send in batches or adjust the rate limit to check if this reduces any errors.

## Unhealthy host detection

Braze webhooks and Connected Content employ an unhealthy host detection mechanism to detect when the target host experiences a high rate of significant slowness or overload resulting in timeouts, too many requests, or other outcomes that prevent Braze from successfully communicating with the target endpoint. It acts as a safeguard to reduce unnecessary load that may be causing the target host to struggle. It also serves to stabilize Braze infrastructure and maintain fast messaging speeds.

The detection thresholds differ between webhooks and Connected Content:
- **For webhooks**: If the number of **failures exceeds 3,000 in any one-minute moving time window** (per unique combination of host name and app group&#8212;**not** per endpoint path), Braze temporarily will halt requests to the target host for one minute.
- **For Connected Content**: If the number of **failures exceeds 3,000 AND the error rate exceeds 90% in any one-minute moving time window** (per unique combination of host name and app group&#8212;**not** per endpoint path), Braze temporarily will halt requests to the target host for one minute.

When requests are halted, Braze simulates responses with a `598` error code to indicate the poor health. After one minute, Braze will resume requests at full speed if the host is found to be healthy. If the host is still unhealthy, Braze will wait another minute before trying again.

The following error codes contribute to the unhealthy host detector failure count: `408`, `429`, `502`, `503`, `504`, `529`.

For webhooks, Braze will automatically retry HTTP requests that were halted by the unhealthy host detector. This automatic retry uses exponential backoff and will retry only a few times before failing. For more information on webhook errors, refer to [Errors, retry logic, and timeouts]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

For Connected Content, if requests to the target host are halted by the unhealthy host detector, Braze will continue to render messages and follow your Liquid logic as if it received an error response code. If you want to ensure these Connected Content requests are retried when they're halted by the unhealthy host detector, use the `:retry` option. For more information on the `:retry` option, see [Connected Content retries]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

If you believe the unhealthy host detection may be causing issues, contact [Braze Support]({{site.baseurl}}/support_contact/).

## Automated emails and Message Activity Log entries

### Setting up automated emails

If you experience more than 100,000 webhook or Connected Content endpoint errors (including retries) in a workspace in a 24-hour period, you will receive an email that includes the following information on how to resolve the errors. 

- Name of the workspace
- A link to the Canvas or campaign
- Endpoint URL
- Error code
- Time the error was last observed
- Links to the Message Activity Log and related documentation

{% alert note %}
You can configure the error threshold per workspace. To adjust this threshold, contact [Braze Support]({{site.baseurl}}/support_contact/).
{% endalert %}

The endpoint errors are:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

These emails are only sent once per day at the workspace level. If no users sign up for these emails, then all company administrators will be notified.

To sign up to receive these emails, do the following:

1. Go to **Settings** > **Admin Settings** > **Notification Preferences**.
2. Select **Connected Content Errors** and **Webhook Errors** in the **Canvas & Campaigns** section.

### Message Activity Log entries

There will be at least one entry in the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) related to the error that triggered the automated email.

### Additional failure insights in Braze Currents

To increase transparency into webhook-related issues, Braze streams detailed webhook failure events to Currents and Snowflake Data Sharing. These events include failed webhook requests (such as HTTP `4xx` or `5xx` responses), providing more observability into how webhook issues may impact message delivery. Note that failure events include terminal errors as well as errors that are being retried.

{% alert note %}
Connected Content requests are not included in these webhook failure events.
{% endalert %}

For more information, refer to the [Message engagement events glossary]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).
