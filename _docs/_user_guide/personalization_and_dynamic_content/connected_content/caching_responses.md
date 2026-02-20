---
nav_title: Caching responses
article_title: Cache Connected Content Responses
page_order: 2.5
description: "This article covers how to cache Connected Content responses across different campaigns or messages in the same workspace to optimize sending speeds."
---

# Cache Connected Content responses

> Connected Content responses can be cached across different campaigns or messages (in the same workspace) to optimize send speeds.

Braze doesn’t permanently log or store Connected Content **response bodies**. During message rendering, responses can be held temporarily (for example, in memory and in cache) so Braze can render Liquid and send the message.

To prevent caching, you can specify `:no_cache`, which may cause increased network traffic. To help troubleshoot and monitor system health, Braze logs Connected Content request metadata (such as the fully rendered request URL and response status code) for successful and failed calls. These logs are kept for up to 30 days.

{% details Connected Content rendering and data handling (advanced) %}
This section provides a more detailed, end-to-end view of how Braze renders Liquid and Connected Content and where data can exist temporarily before a message is sent. This may help with privacy and data-handling reviews.

#### What is and isn’t stored

- **Connected Content response body:** Not permanently stored by Braze. It can be held temporarily in memory and, when caching is enabled, stored in cache with a time-to-live (TTL).
- **Connected Content request metadata:** Request metadata, such as the fully rendered URL, HTTP status code, and response duration, are logged for troubleshooting and monitoring. These logs are kept for up to 30 days. 
- **Final rendered message:** Exists in memory during rendering. This may also be stored elsewhere depending on your configuration and channel (for example, Message Archiving or Content Cards).

#### Rendering flow (high level)

The following flow describes how Braze renders and sends messages for provider-based channels such as email, SMS, and push. SDK-delivered channels like  Content Cards use the same underlying Liquid and Connected Content rendering but differ in when the content is generated and how it is delivered.

1. A background worker renders the Liquid template for a message when the message is prepared to be delivered.
2. Connected Content tags are evaluated during Liquid rendering.
3. For each Connected Content tag, Braze checks a multi-tier cache. If no cached value exists (or caching is disabled), Braze calls your endpoint and receives the response.
4. The response is injected into the Liquid template and the message is fully rendered.
5. For provider-based channels, the rendered message is sent to the channel provider and then to the user. For SDK-delivered channels such as Content Cards, the rendered content is synced to the Braze SDK and can be generated at first impression or display time, at which point it is shown to the user.

#### Where Connected Content responses can live temporarily

Braze uses a multi-tier cache for Connected Content responses with TTLs between five minutes and four hours, depending on your use of `:cache_max_age` and other caching rules:

- **In-process memory cache:** Transient cache within the worker process. Data can live only for the duration of the job (up to ~11 minutes based on worker timeout).
- **Local machine cache:** A per-worker cache, such as a local Memcached instance.
- **Cluster-wide cache:** A distributed cache shared across workers, such as a Memcached cluster.

These cache layers are volatile and can evict data earlier than the configured TTL.

#### What changes when you use `:no_cache`

For endpoints that are not hosted inside Braze infrastructure, using `:no_cache` prevents the Connected Content response body from being stored in Memcached. In these cases, the response only lives in the worker process memory for the duration of the rendering job (up to ~11 minutes). For endpoints that resolve to hosts internal to Braze, responses may still be cached as described in [Cache busting](#cache-busting).

#### Where the final rendered output can live

- **Message Archiving:** If Message Archiving is enabled, Braze may write the final rendered message to your configured cloud storage bucket. If your Connected Content response is included in the rendered message, it will be included in the archived copy.
- **User devices:** After delivery, the fully rendered message content can persist on user devices for an unknown amount of time.
- **Content Cards:** Rendered content for Content Cards is stored in a Braze database until the card expires.
{% enddetails %}

## Default cache settings

The cache age is up to five minutes (300 seconds). You can update this by adding the `:cache_max_age` parameter to the Connected Content call. An example is:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

GET requests are cached. You can configure this by adding the :no_cache parameter to the Connected Content call.

POST requests are not cached. This can be forced by adding the :cache_max_age parameter to the Connected Content call. The minimum cache time is 5 minutes, and the maximum cache time is 4 hours.

{% alert note %}
Cache settings aren’t guaranteed. Caching can reduce calls to your endpoints, so we recommend using multiple calls per endpoint within the cache duration rather than being overly reliant on caching.
{% endalert %}

### Cache size limit

The Connected Content response body can be up to 1&nbsp;MB. If the response body is larger than 1&nbsp;MB, it will not cache.

## Cache time 

Connected Content will cache the value it returns from GET endpoints for a minimum of five minutes. If a cache time is not specified, the default cache time is five minutes.

Connected Content cache time can be configured to be longer with :cache_max_age, as shown in the following example. The minimum cache time is five minutes and the maximum cache time is four hours. Connected Content data is cached in-memory using a volatile cache system, such as Memcached. 

As a result, regardless of the specified cache time, Connected Content data may be evicted from Braze’s in-memory cache earlier than specified. This means the cache durations are suggestions and may not actually represent the duration that the data is guaranteed to be cached by Braze and you may see more Connected Content requests than you may expect with a given cache duration.

### Cache for specified seconds

This example will cache for 900 seconds (or 15 minutes).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache busting

To prevent Connected Content from caching the value it returns from a GET request, you can use the `:no_cache` configuration. However, responses from hosts internal to Braze will still be cached.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Be certain the provided Connected Content endpoint can handle large bursts of traffic before using this option, or you will likely see increased sending latency (increased delays or wider time intervals between request and response) due to Braze making Connected Content requests for every single message.
{% endalert %}

With a POST you don’t need to cache bust, as Braze never caches the results from POST requests.

## Things to know

- Caching can help reduce duplicate Connected Content calls. However, it isn’t guaranteed to always result in a single Connected Content call per user.
- Connected Content caching is based on the URL and workspace. If the Connected Content call is to the identical URL, it can be cached across campaigns and Canvases.
- The cache is based on a unique URL, not a user ID or campaign. This means the cached version of a Connected Content call might be used across multiple users and campaigns in a workspace if the URL is the same.
