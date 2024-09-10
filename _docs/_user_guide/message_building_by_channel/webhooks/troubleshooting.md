---
nav_title: Troubleshooting
article_title: Troubleshooting
page_order: 3
channel:
  - webhooks
description: "This article covers how to troubleshoot webhook error codes, including what the errors are and steps to resolve them."
---

# Troubleshooting

> This article covers how to troubleshoot common webhook error codes and provides further explanations on how these errors can occur in endpoint requests.

## 4XX errors

`4XX` errors indicate that there's an issue with the request sent to the endpoint. These errors are typically caused by erroneous requests, including malformed parameters, missing authentication headers, or incorrect URLs.

Refer to the following table for error code details and steps to resolve:

| Error code | What it means | Steps to resolve |
| `400 Bad Request` | There's invalid syntax in the request. | {::nomarkdown} <ul> <li> Check the request payload for any syntax errors. </li> <li> Check that all required fields are included and correctly formatted. </li> <li> Validate the JSON structure if you are sending a JSON payload. </li> </ul> {:/} |
| `401 Unauthorized` | The request requires user authentication. | {::nomarkdown} <ul> <li> Verify that the correct authentication credentials (e.g., API keys, tokens) are included in the request headers. </li> <li> Ensure that the credentials have the necessary permissions to access the endpoint. </li> </ul> {:/} |
| 403 Forbidden | The endpoint understands the request but refuses to authorize it. | {::nomarkdown} <ul> <li> Check if the API key or token has the necessary permissions. </li> <li> Ensure that the endpoint you are trying to access is allowed for your credentials. </li> </ul> {:/} |
| 404 Not Found | The endpoint cannot find the requested resource. | {::nomarkdown} <ul> <li> Verify the endpoint URL for any typos or incorrect paths. </li> <li> Ensure that the resource you are trying to access exists. </li> </ul> {:/} |
| 405 Method Not Allowed | The request method is known by the endpoint but is not supported by the target resource. |  {::nomarkdown} <ul> <li> Check the HTTP method (GET, POST, PUT, DELETE, etc.) used in the request. </li> <li> Ensure that the endpoint supports the method you are using. </li> </ul> {:/} |
| 408 Request Timeout | The endpoint timed out processing the request. | {::nomarkdown} <ul> <li> Check the HTTP method (GET, POST, PUT, DELETE, etc.) used in the request. </li> <li> Ensure that the endpoint supports the method you are using. </li> </ul> {:/} |
| 409 Conflict | The request is incomplete because of a conflict with the current state of the resource. | ::nomarkdown} <ul> <li> Check the HTTP method (GET, POST, PUT, DELETE, etc.) used in the request. </li> <li> Ensure that the endpoint supports the method you are using. </li> </ul> {:/} |
| 429 Too Many Requests | There are too many requests sent in a given amount of time. | {::nomarkdown} <ul> <li> Lower the canvas/campaign/canvas rate limit frequency capping on your campaign/canvas step. </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 5XX errors

`5XX` errors indicate that there's an issue with the endpoint. These errors are typically caused by server-side issues.

Refer to the following table for error code details and steps to resolve:


###