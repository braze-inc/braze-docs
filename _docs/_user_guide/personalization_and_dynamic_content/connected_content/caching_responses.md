---
nav_title: Caching responses
article_title: Cache Connected Content Responses
page_order: 2.5
description: "This article covers how to cache Connected Content responses across different campaigns or messages in the same workspace to optimize sending speeds."
---

# Cache Connected Content responses

> Connected Content responses can be cached across different campaigns or messages (in the same workspace) to optimize send speeds.

Braze doesn’t permanently log or store Connected Content responses. If you explicitly choose to store a Connected Content call response as a Liquid variable, Braze only stores this in-memory, meaning on temporary storage that’s deleted after a short period of time, to render the Liquid variable and send the message.

To prevent caching, you can specify `:no_cache`, which may cause increased network traffic. To help troubleshoot and monitor system health, Braze may also log Connected Content calls that fail (such as `404` and `429`). These logs are kept for up to 30 days.

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
