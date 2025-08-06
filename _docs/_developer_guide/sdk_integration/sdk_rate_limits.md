---
page_order: 10.1
nav_title: SDK Rate Limits
article_title: About rate limits for the Braze SDKs
description: "Learn about rate limits for the Braze SDKs."
---

# SDK Rate Limits

> Learn how Braze SDKs implement intelligent client-side rate limiting to optimize battery life, reduce bandwidth usage, and ensure reliable data delivery.

## How it works

Braze SDKs implement adaptive client-side rate limiting designed to protect both your users' experience and your app's performance. Our SDKs automatically batch events and adapt flush intervals based on network quality to provide the best user experience while maintaining data integrity.

### Token bucket rate limiting

Braze SDKs use a token bucket algorithm for rate limiting. This approach allows for bursts of activity while maintaining long-term rate control. The token bucket mechanism works by:

- **Token generation**: Tokens are added to the bucket at a steady rate
- **Request consumption**: Each SDK call consumes a token from the bucket
- **Burst handling**: Short bursts of activity are allowed if tokens are available
- **Rate control**: Long-term rate is controlled by the token generation rate

### Remote rate limit adaptation

Braze can dynamically adjust rate limits remotely to protect our network infrastructure and ensure optimal performance for all customers. This means:

- **Network protection**: Rate limits can be adjusted in real-time to prevent network overload
- **Performance optimization**: Dynamic adjustments help maintain optimal SDK performance
- **Infrastructure protection**: Remote control allows Braze to respond to network conditions

{% alert note %}
Because rate limits can be adjusted remotely to protect our network infrastructure, we cannot provide exact bucket numbers or static rate limit values. The limits are designed to be adaptive and may change based on network conditions and usage patterns.
{% endalert %}

### Key networking features of the SDKs

- **Automatic batching**: Events are queued and sent in efficient batches
- **Network-aware behavior**: Flush rates automatically adjust based on connectivity
- **Battery optimization**: Reduces radio wake-ups and network calls
- **Graceful degradation**: Handles poor network conditions seamlessly
- **Background/foreground awareness**: Optimizes behavior during app lifecycle transitions

## Review your integration approach

If you're experiencing rate limit issues, analyze your usage of SDK methods and their call frequency. For example:

- **`requestImmediateDataFlush()`**: Forces immediate data transmission
- **`requestContentCardsRefresh()`**: Refreshes Content Cards from the server
- **`refreshFeatureFlags()`**: Requests the latest Feature Flag data
- **`logCustomEvent()`**: Logs custom events
- **`logPurchase()`**: Logs purchase events

When reviewing your integration, consider:

1. **Event frequency**: Are you tracking meaningful actions or every interaction?
2. **Refresh patterns**: Are you refreshing content when necessary or on every user action?
3. **Batching strategy**: Are you letting the SDK handle batching automatically?

When contacting Support about rate limit issues, please provide:
- Which SDK methods you're calling
- How frequently each method is being called
- The context in which these calls are being made (e.g., scroll events, button clicks, etc.)
- Any patterns in your app's user flow that might trigger excessive calls
