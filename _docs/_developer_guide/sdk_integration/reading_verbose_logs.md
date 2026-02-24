---
page_order: 1.5
nav_title: Reading Verbose Logs
article_title: Reading verbose logs
description: "Learn how to read and interpret verbose log output from the Braze SDK, including key entries for push notifications, in-app messages, Content Cards, and deep links."
---

# Reading verbose logs

> This page explains how to interpret the verbose log output from the Braze SDK. For each messaging channel, you'll find the key log entries to look for, what they mean, and common issues to watch for.

Before you start, make sure you've [enabled verbose logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) and know how to collect logs on your platform.

## Sessions

Sessions are the foundation of Braze analytics and message delivery. Many messaging features—including in-app messages and Content Cards—depend on a valid session starting before they can function. If sessions aren't logging correctly, investigate this first. For more information about enabling session tracking, see [Step 5: Enable user session tracking]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking).

### Key log entries

{% tabs %}
{% tab Swift %}

**Session start:**

```
Started user session (id: <SESSION_ID>)
```

**Session end:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Session start:**

Look for the following entries:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filter network requests for your configured Braze endpoint (for example, sdk.iad-01.braze.com) to see the session start (`ss`) event.

**Session end:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### What to check

- Verify that a session start log appears when the app launches.
- If you don't see a session start, check that the SDK is properly initialized and that `openSession` (Android) is being called.
- On Android, confirm that a network request is being made to the Braze endpoint. If you don't see this, verify your API key and endpoint configuration.

## Push notifications

Push notification logs help you verify that device tokens are registered, notifications are delivered, and click events are tracked.

### Token registration

When a session starts, the SDK registers the device's push token with Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filter for requests to your configured Braze endpoint (for example, sdk.iad-01.braze.com) and look for `push_token` in the request body attributes:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Also confirm the device info includes:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Look for the FCM registration log:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Verify the following:

- `com_braze_firebase_cloud_messaging_registration_enabled` is `true`.
- The FCM sender ID matches your Firebase project.

A common error is `SENDER_ID_MISMATCH`, which means the configured sender ID doesn't match your Firebase project.

{% endtab %}
{% endtabs %}

### What to check

- If `push_token` is missing from the request body, the token wasn't captured. Verify push setup in your app configuration.
- If `ios_push_auth` shows `denied` or `provisional`, the user hasn't granted full push permission.
- On Android, if you see `SENDER_ID_MISMATCH`, update your FCM sender ID to match your Firebase project.

### Push delivery and click

When a push notification is tapped, the SDK logs the processing and click events.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Followed by the click event:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

If the push contains a deep link, you'll also see:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Followed by the push payload and display logs. For deep links, look for the Deep Link Delegate or `UriAction` entries.

{% endtab %}
{% endtabs %}

### What to check

- Verify the push payload contains the expected `title`, `body`, and any deep links (`ab_uri`).
- Confirm a `pushClick` event is logged after tapping.
- If the click event is missing, check that your app delegate or notification handler is properly forwarding push events to the Braze SDK.

## In-app messages

In-app message logs show you the full lifecycle: delivery from the server, triggering based on events, display, impression logging, and click tracking.

### Message delivery

When a user starts a session and is eligible for an in-app message, the SDK receives the message payload from the server.

{% tabs %}
{% tab Swift %}

Filter for responses from your configured Braze endpoint (for example, sdk.iad-01.braze.com) containing the in-app message data.

The response body contains the message payload, including:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Look for the trigger event matching log:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

This confirms the in-app message was matched to a trigger event.

{% endtab %}
{% endtabs %}

### Message display and impression

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Followed by the impression log:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Click and button events

When a user taps a button or closes the message:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

If no further triggered messages match, you'll also see:

```
No matching trigger for event.
```

This is expected behavior when no additional in-app messages are configured for the event.

{% endtab %}
{% tab Android %}

Filter for requests to your configured Braze endpoint (for example, sdk.iad-01.braze.com) and look for events with the name `sbc` (button click) or `si` (impression) in the request body.

{% endtab %}
{% endtabs %}

### What to check

- If the in-app message doesn't display, verify that a session start is logged first.
- Filter for responses from your configured Braze endpoint to confirm the message payload was delivered.
- If impressions aren't logging, verify you haven't implemented a custom `inAppMessageDisplay` delegate that suppresses logging.
- If "No matching trigger for event" appears, this is normal and indicates that no additional in-app messages are configured for that event.

## Content Cards

Content Card logs help you verify that cards are synced to the device, displayed to the user, and that interactions (impressions, clicks, dismissals) are tracked.

### Card sync

Content Cards sync on session start and when a manual refresh is requested. If no session is logged, no Content Cards are displayed.

{% tabs %}
{% tab Swift %}

Filter for responses from your configured Braze endpoint (for example, sdk.iad-01.braze.com) containing the card data.

The response body contains the card data, including:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Key fields:
- `v` (viewed): `0` = not viewed, `1` = viewed
- `cl` (clicked): `0` = not clicked, `1` = clicked
- `p` (pinned): `0` = not pinned, `1` = pinned
- `tp` (type): `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Followed by a POST request to your configured Braze endpoint (for example, sdk.iad-01.braze.com) containing user and device information.

{% endtab %}
{% endtabs %}

### Impressions, clicks, and dismissals

{% tabs %}
{% tab Swift %}

**Impression:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Click:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

If the card has a URL, you'll also see:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Dismissal:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filter for requests to your configured Braze endpoint (for example, sdk.iad-01.braze.com) and look for event names in the request body:
- `cci` — Content Card impression
- `ccc` — Content Card click
- `ccd` — Content Card dismissed

{% endtab %}
{% endtabs %}

### What to check

- **No cards displayed**: Verify that a session start is logged. Content Cards require an active session to sync.
- **Cards missing for new users**: New users on their first session may not see Content Cards until the next session. This is expected behavior.
- **Card exceeds size limit**: Content Cards over 2 KB aren't displayed and the message is aborted.
- **Card persists after stopping campaign**: Verify that the sync completed after the campaign was stopped. Content Cards are removed from the device after a successful sync. When stopping a campaign, ensure the option to remove active cards from user feeds is selected.

## Deep links

Deep link logs appear across push notifications, in-app messages, and Content Cards. The log structure is consistent regardless of the source channel.

{% tabs %}
{% tab Swift %}

When the SDK processes a deep link:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Where `<SOURCE_CHANNEL>` is one of: `notification`, `inAppMessage`, or `contentCard`.

{% endtab %}
{% tab Android %}

For deep links, look for the **Deep Link Delegate** or **UriAction** entries in Logcat. To test deep link resolution independently, run the following command:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

This confirms whether the deep link resolves correctly outside of the Braze SDK.

{% endtab %}
{% endtabs %}

### What to check

- Verify the deep link URL matches what you configured in the campaign.
- If the deep link works from one channel (for example, push) but not another (for example, Content Cards), check that your deep link handling implementation supports all channels.
- On iOS, universal links require additional handling. If universal links aren't working from Braze channels, verify that your app implements the `BrazeDelegate` protocol for URL handling.
- On Android, check that automatic deep link handling is disabled if you use a custom handler. Otherwise the default handler may conflict with your implementation.

## User identification

When a user is identified with an `external_id`, the SDK logs a change user event.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Key things to know:
- Call `changeUser` as soon as the user logs in—the sooner, the better.
- If a user logs out, there's no way to call `changeUser` to revert them to an anonymous user.
- If you don't want anonymous users, call `changeUser` during session start or app startup.

{% endtab %}
{% tab Swift %}

Filter for requests to your configured Braze endpoint (for example, sdk.iad-01.braze.com) and look for user identification in the request body:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Network requests

Verbose logs include full HTTP request and response details for SDK communication with Braze servers. These are useful for diagnosing connectivity issues.

### Request structure

Filter for requests to your configured Braze endpoint (for example, sdk.iad-01.braze.com). The request structure includes:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### What to check

- **API key**: Verify `XBraze-ApiKey` matches your workspace's API key.
- **Endpoint**: Confirm the request URL matches your configured SDK endpoint.
- **Retry attempts**: `XBraze-Req-Attempt` greater than 1 indicates the SDK is retrying a failed request, which may signal connectivity issues.
- **Rate limiting**: `XBraze-Req-Tokens-Remaining` shows the remaining request tokens. A low count may indicate the SDK is approaching rate limits.
- **Missing requests**: On Android, if you don't see a request to the Braze endpoint after session start, verify your API key and endpoint configuration.

## Common event abbreviations

In verbose log payloads, Braze uses abbreviated event names. Here's a reference:

| Abbreviation | Event |
|---|---|
| `ss` | Session start |
| `se` | Session end |
| `si` | In-app message impression |
| `sbc` | In-app message button click |
| `cci` | Content Card impression |
| `ccc` | Content Card click |
| `ccd` | Content Card dismissed |
| `lr` | Location recorded |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }