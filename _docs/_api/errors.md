---
nav_title: Errors & responses
article_title: API Errors & Responses
description: "This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them."
page_type: reference
page_order: 2.3

---
# API errors and responses

> This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them.

{% raw %}

## Server responses

If your POST payload was accepted by our servers, then successful messages will be met with the following response:

```json
{
  "message" : "success"
}
```

Note that success only means that the RESTful API payload was correctly formed and passed onto our push notification or email or other messaging services. It does not mean that the messages were actually delivered, as additional factors could prevent the message from being delivered (for example, a device could be offline, the push token could be rejected by Apple's servers, you may have provided an unknown user ID).

If your message is successful but has non-fatal errors you will receive the following response:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

In the case of a success, any messages that were not affected by an error in the `errors` array will still be delivered. If your message has a fatal error you will receive the following response:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Responses for tracked send IDs

Analytics are always available for campaigns. In addition, analytics are available for a specific campaign send instance when the campaign is sent as a broadcast. When tracking is available for a specific campaign send instance, you will receive the following response:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

The provided send id can be used as a parameter for the `/send/data_series` endpoint to pull back send specific analytics.

## Errors

The status code element of a server response is a 3-digit number where the first digit of the code defines the class of response.

- The **2XX class** of status code (non-fatal) indicates that **your request** was successfully received, understood, and accepted.
- The **4XX class** of status code (fatal) indicates a **client error**. Refer to the fatal errors chart for a full list of 4XX error codes and descriptions.
- The **5XX class** of status code (fatal) indicates a **server error**. There are several potential causes, for example, the server you're trying to access is unable to execute the request, the server is undergoing maintenance making it unable to execute the request, or the server is experiencing high levels of traffic. When this happens, we recommend you retry your request with exponential backoff. In the event of an incident or outage, Braze is not able to replay any REST API call that failed during the incident window. You will need to retry any calls that failed during the incident window.
  - A **502 error** is a failure before it reaches the destination server.
  - A **503 error** means that the request made it to the destination server, but we can't complete the request because there isn't enough capacity, or there is a network issue, or similar.
  - A **504 error** indicates a server didn't receive a response from another server upstream.

### Fatal errors

The following status codes and associated error messages will be returned if your request encounters a fatal error.

{% endraw %}
{% alert warning %}
All of the following error codes indicate that no messages will be sent.
{% endalert %}
{% raw %}

| Error Code | Description |
|---|---|
| `5XX Internal Server Error` | Retry your request with exponential backoff.|
| `400 Bad Request` | Bad syntax.|
| `400 No Recipients` | There are no external IDs or segment IDs, or no push tokens in the request.|
| `400 Invalid Campaign ID` | No messaging API campaign was found for your provided campaign ID.|
| `400 Message Variant Unspecified` | You provide a campaign ID but no message variation ID.|
| `400 Invalid Message Variant` | You provided a valid campaign ID, but the message variation ID doesn't match any of that campaign's messages.|
| `400 Mismatched Message Type` | You provided a message variation of the wrong message type for at least one of your messages.|
| `400 Invalid Extra Push Payload` | You provide the `extra` key for either `apple_push` or `android_push` but it is not a dictionary.|
| `400 Max Input Length Exceeded` | Caused by calling more than 75 external IDs when hitting the `/users/track` endpoint.|
| `400 The max number of external_ids and aliases per request was exceeded` | Caused by calling more than 50 external IDs.|
| `400 The max number of ids per request was exceeded` | Caused by calling more than 50 external IDs.|
| `400 No message to send` | No payload is specified for the message.|
| `400 Slideup Message Length Exceeded` | Slideup message contains more than 140 characters.|
| `400 Apple Push Length Exceeded` | JSON payload is more than 1,912 bytes.|
| `400 Android Push Length Exceeded` | JSON payload is more than 4,000 bytes.|
| `400 Bad Request` | Cannot parse `send_at` datetime.|
| `400 Bad Request` | In your request, `in_local_time` is true but `time` has passed in your company’s time zone.|
| `401 Unauthorized` | Invalid API key. This error can also occur if:<br><br> - You're sending the request to the incorrect [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For example, if your account is on our EU instance (`https://dashboard-01.braze.eu`), the request should be sent to `https://rest.fra-01.braze.eu`.<br>- The API key syntax is using single or double quotes. The correct syntax is `Authorization: Bearer {YOUR-API-KEY}`. |
| `403 Forbidden` | The rate plan doesn't support, or the account is otherwise inactivated.|
| `403 Access Denied` | The REST API key you are using does not have sufficient permissions, check the API key permissions under the **Settings** page.|
| `404 Not Found` | Invalid URL. |
| `429 Rate Limited` | Over rate limit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}
