---
page_order: 2.0
nav_title: Rate Limits
article_title: Braze SDK rate limits
description: "Learn about the Braze SDK's intelligent, client-side rate limiting that optimizes battery life, reduces bandwidth usage, and ensures reliable data delivery."
---

# Braze SDK rate limits

> Learn about the Braze SDK's intelligent, client-side rate limiting that optimizes battery life, reduces bandwidth usage, and ensures reliable data delivery.

## Understanding SDK rate limits

Braze SDK rate limiting uses the following features to optimize performance, minimize battery drain, reduce data usage, and ensure reliable data delivery:

### Asynchronous processing

The Braze SDK uses a token bucket algorithm for rate limiting. This approach allows for bursts of activity while maintaining long-term rate control. Instead of processing requests in a strict queue, the token bucket operates asynchronously:

- **Token generation**: Tokens are replenished at a steady rate into the bucket.
- **Request handling**: Any SDK call that arrives when a token is available proceeds immediately, regardless of when other calls arrived.
- **No strict ordering**: Requests don’t wait in line; multiple calls may compete for the next available token.
- **Burst handling**: Short bursts of activity are allowed if enough tokens are available at the time of the requests.
- **Rate control**: Long-term throughput is limited by the steady token replenishment rate.

This asynchronous flow helps the SDK respond quickly to available network capacity while maintaining predictable overall traffic levels.

### Adaptive rate limiting

The Braze SDK can adjust rate limits in real time to protect network infrastructure and maintain optimal performance. This approach:

- **Prevents overload**: Adjusts limits to avoid network congestion.
- **Optimizes performance**: Maintains smooth SDK operation under varying conditions.
- **Responds to conditions**: Adapts based on current network and usage patterns.

{% alert note %}
Because limits adapt in real time, exact bucket sizes and static values are not provided. They may change depending on network conditions and usage.
{% endalert %}

### Networking optimizations

The Braze SDK includes several built-in behaviors to improve efficiency, reduce battery usage, and handle varying network conditions:

- **Automatic batching**: Queues events and sends them in efficient batches.
- **Network-aware behavior**: Adjusts flush rates based on connectivity quality.
- **Battery optimization**: Minimizes radio wake-ups and network calls.
- **Graceful degradation**: Maintains functionality during poor network conditions.
- **Background/foreground awareness**: Optimizes behavior as the app’s lifecycle changes.

## Best practices

Follow these best practices to help avoid rate limit issues:

| Do this | Not this |
| --- | --- |
| Track meaningful user actions and milestones | Track every minor interaction or UI event |
| Refresh content only when necessary | Refresh content on every user action (like scroll events) |
| Let the SDK handle batching automatically | Force immediate data transmission unless absolutely necessary |
| Focus on events that add value to analytics | Call SDK methods in rapid succession without considering frequency |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Getting Help

When contacting [support@braze.com](mailto:support@braze.com) about SDK rate limit issues, please include the following information:

```plaintext
Call frequency for each networking SDK method:
- requestImmediateDataFlush(): [frequency]
- requestContentCardsRefresh(): [frequency]
- refreshFeatureFlags(): [frequency]
- logCustomEvent(): [frequency]
- logPurchase(): [frequency]
- Other: [method and frequency]

Context in which these calls occur (e.g., scroll events, button clicks):
[describe]

Patterns in user flow that may trigger excessive calls:
[describe]
```
