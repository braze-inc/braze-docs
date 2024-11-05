---
nav_title: Troubleshooting Webhook and Connected Content Requests
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
| **599 Connection Error**      | Braze experienced a network connect timeout error while trying to establish a connection to the endpoint, meaning the endpoint may be unstable or down. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolving 5XX errors

Here are tips for troubleshooting common `5XX` errors:

- Review the error message for specific details available in the **Message Activity Log**. For webhooks, go to the **Performance Over Time** section on the Braze home page and select the statistics for webhooks. From here, you can find the timestamp that indicates when the errors occurred.
- Make sure you're not sending too many requests that overload the endpoint. You can send in batches or adjust the rate limit to check if this reduces any errors.
