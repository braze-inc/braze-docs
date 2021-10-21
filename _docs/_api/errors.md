---
nav_title: Errors & Responses
article_title: API Errors & Responses
description: "This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them." 
page_type: reference
page_order: 2.3

---
# Errors & responses

> This reference article covers the various errors and server responses that can come up while using the Braze API and how to troubleshoot them. 

{% raw %}

##  Server responses

If your POST payload was accepted by our servers, then successful messages will be met with the following response:

```json
{
  "message" : "success"
}
```

Note that success only means that the RESTful API payload was correctly formed and passed onto our push notification or email or other messaging services. It does not mean that the messages were actually delivered, as additional factors could prevent the message from being delivered (e.g., a device could be offline, the push token could be rejected by Apple's servers, you may have provided an unknown user ID, etc.)

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

## Queued responses {#messaging-queued}

During times of maintenance, Braze might pause real-time processing of the API. In these situations, the server will return an `HTTP Accepted 202` response code and the following body, which indicates that we have received and queued the API call but have not immediately processed it. All scheduled maintenance will be posted to [http://status.braze.com](http://status.braze.com) ahead of time.

```json
{
  "message" : "queued"
}
```

## Responses for tracked send ids

Analytics are always available for campaigns. In addition, analytics are available for a specific campaign send instance when the campaign is sent as a broadcast. When tracking is available for a specific campaign send instance, you will receive the following response:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

The provided send id can be used as a parameter for the send/data_series endpoint to pull back send specific analytics.

## Fatal errors

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no messages will be sent.

| Error Code | Description |
|---|---|
| `400 Bad Request` | Bad syntax.|
| `400 No Recipients` | There are no external IDs or segment IDs or no push tokens in the request.|
| `400 Invalid Campaign ID` | No Messaging API campaign was found for the campaign ID you provided.|
| `400 Message Variant Unspecified` | You provide a campaign ID but no message variation ID.|
| `400 Invalid Message Variant` | You provided a valid campaign ID, but the message variation ID doesn't match any of that campaign's messages.|
| `400 Mismatched Message Type` | You provided a message variation of the wrong message type for at least one of your messages.|
| `400 Invalid Extra Push Payload` | You provide the `extra` key for either `apple_push` or `android_push` but it is not a dictionary.|
| `400 Max Input Length Exceeded` | Caused by calling more than 75 external ids when hitting the User Track endpoint.|
| `400 The max number of external_ids and aliases per request was exceeded` | Caused by calling more than 50 external ids.|
| `400 The max number of ids per request was exceeded` | Caused by calling more than 50 external ids.|
| `400 No message to send` | No payload is specified for the message.|
| `400 Slideup Message Length Exceeded` | Slideup message contains more than 140 characters.|
| `400 Apple Push Length Exceeded` | JSON payload is more than 1912 bytes.|
| `400 Android Push Length Exceeded` | JSON payload is more than 4000 bytes.|
| `400 Bad Request` | Cannot parse send_at datetime.|
| `400 Bad Request` | In your request, `in_local_time` is true but `time` has passed in your company’s time zone.|
| `401 Unauthorized` | Unknown or missing REST API Key.|
| `403 Forbidden` | Rate plan doesn't support or account is otherwise inactivated.|
| `403 Access Denied` | The REST API Key you are using does not have sufficient permissions, check the API key permissions in the Braze Developer Console.|
| `404 Not Found` | Unknown REST API Key.|
| `429 Rate Limited` | Over rate limit.|
| `5XX Internal Server Error` | You should retry your request with exponential backoff.|
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}
