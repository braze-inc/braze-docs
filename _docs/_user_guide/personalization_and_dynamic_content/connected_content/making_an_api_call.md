---
nav_title: Making a Connected Content call
article_title: Making a Connected Content API Call
page_order: 0
description: "This reference article covers how to make a Connected Content API call, as well as helpful examples and advanced Connected Content use cases."
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Making a Connected Content API call

> Use Connected Content to insert any information accessible by API directly into messages you send to users. You can pull content either directly from your web server or from publicly accessible APIs.<br><br>This page covers how to make Connected Content API calls, advanced Connected Content use cases, error handling, and more.

## Sending a Connected Content call

{% raw %}

To send a Connected Content call, use the `{% connected_content %}` tag. With this tag, you can assign or declare variables by using `:save`. Aspects of these variables can be referenced later in the message with [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

For example, the following message body will access the URL `http://numbersapi.com/random/trivia` and include a fun trivia fact in your message:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Adding variables

You can also include user profile attributes as variables in the URL string when making Connected Content requests. 

For example, you may have a web service that returns content based on a user's email address and ID. If you're passing attributes containing special characters, such as the at sign (@), make sure to use the Liquid filter `url_param_escape` to replace any characters not allowed in URLs with their URL-friendly escaped versions, as shown in the following email address attribute.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Attribute values must be surrounded by `${}` to operate properly within our version of Liquid syntax.
{% endalert %}

Connected Content requests support GET and POST requests only.

## Error handling

If the URL is unavailable and reaches a 404 page, Braze will render an empty string in its place. If the URL reaches an HTTP 500 or 502 page, the URL will fail on the retry logic.

If the endpoint returns JSON, you can detect that by checking if the `connected` value is null, and then [conditionally abort the message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze only allows URLs that communicate over port 80 (HTTP) and 443 (HTTPS).

### Unhealthy host detection

Connected Content employs an unhealthy host detection mechanism to detect when the target host experiences a high rate of significant slowness or overload, resulting in timeouts, too many requests, or other outcomes that prevent Braze from successfully communicating with the target endpoint. It acts as a safeguard to reduce unnecessary load that may be causing the target host to struggle. It also serves to stabilize Braze infrastructure and maintain fast messaging speeds.

If the target host experiences a high rate of significant slowness or overload, Braze temporarily will halt requests to the target host for one minute, instead simulating responses indicating the failure. After one minute, Braze will probe the host's health using a small number of requests before resuming requests at full speed if the host is found to be healthy. If the host is still unhealthy, Braze will wait another minute before trying again.

If requests to the target host are halted by the unhealthy host detector, Braze will continue to render messages and follow your Liquid logic as if it received an error response code. If you want to ensure that these Connected Content requests are retried when they're halted by the unhealthy host detector, use the `:retry` option. For more information on the `:retry` option, see [Connected Content retries]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

If you believe the unhealthy host detection may be causing issues, contact [Braze Support]({{site.baseurl}}/support_contact/).

{% alert tip %}
Visit [Troubleshooting webhook and Connected Content requests]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) to learn more on how to troubleshoot common error codes.
{% endalert %}

## Allowing for efficient performance

Because Braze delivers messages at a very fast rate, be sure that your server can handle thousands of concurrent connections so the servers don't get overloaded when pulling down content. When using public APIs, confirm your usage won't violate any rate-limiting that the API provider may employ. Braze requires the server response time to be less than two seconds for performance reasons; if the server takes longer than two seconds to respond, the content won't be inserted.

Braze systems may make the same Connected Content API call more than once per recipient. That is because Braze may need to make a Connected Content API call to render a message payload, and message payloads can be rendered multiple times per recipient for validation, retry logic, or other internal purposes. Your systems should be able to tolerate the same Connected Content call being made more than once per recipient.

## Things to know

* Braze does not charge for API calls and will not count toward your given data point usage.
* There is a 1 MB limit for Connected Content responses.
* Connected Content calls will happen when the message is sent, except for in-app messages, which will make this call when the message is viewed.
* Connected Content calls do not follow redirects.

## Authentication types

### Using basic authentication

If the URL requires basic authentication, Braze can generate a basic authentication credential for you to use in your API call. You can manage existing basic authentication credentials and add new ones from **Settings** > **Connected Content**.

![The 'Connected Content' settings in the Braze dashboard.]({% image_buster /assets/img_archive/basic_auth_mgmt.png %})

To add a new credential, select **Add Credential**. Give your credential a name and enter the username and password.

![The 'Create New Credential' window with the option to enter a name, username, and password.]({% image_buster /assets/img_archive/basic_auth_token.png %}){: style="max-width:30%" }

You can then use this basic authentication credential in your API calls by referencing the token's name:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
If you delete a credential, keep in mind that any Connected Content calls trying to use it will be aborted.
{% endalert %}

### Using token authentication

When using Braze Connected Content, you may find that certain APIs require a token instead of a username and password. For those APIs, you can reference the code snippet in the following call as a model for your message.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
     }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Using Open Authentication (OAuth)

Some API configurations require the retrieval of an access token that can then be used to authenticate the API endpoint that you want to access.

#### Step 1: Retrieve the access token

The following example illustrates retrieving and saving an access token to a local variable, which can then be used to authenticate the subsequent API call. A `:cache_max_age` parameter can be added to match the time that the access token is valid for and reduce the number of outbound Connected Content calls. See [Configurable Caching]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching) for more information.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Step 2: Authorize the API using the retrieved access token

After the token is saved, it can be dynamically templated into the subsequent Connected Content call to authorize the request:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

## Connected Content IP allowlisting

When a message using Connected Content is sent from Braze, the Braze servers automatically make network requests to our customers' or third parties' servers to pull back data. With IP allowlisting, you can verify that Connected Content requests are actually coming from Braze, adding an additional layer of security.

Braze will send Connected Content requests from the following IP ranges. The listed ranges are automatically and dynamically added to any API keys that have been opted in for allowlisting. 

Braze has a reserved set of IPs used for all services, not all of which are active at a given time. This is designed for Braze to send from a different data center or do maintenance, if necessary, without impacting customers. Braze may use one, a subset, or all of the following IPs listed when making Connected Content requests.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` header

Braze includes a `User-Agent` header in all Connected Content and webhook requests that is similar to the following:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Keep in mind that the hash value changes regularly. If you're filtering traffic by `User-Agent`, allow all values that start with `Braze Sender`.
{% endalert %}

## Troubleshooting

Use [Webhook.site](https://webhook.site/) to troubleshoot your Connected Content calls. 

1. Switch the URL in your Connected Content call with the unique URL generated on the site.
2. Preview and test your campaign or Canvas step to see the requests come through to this website.

Using this tool, you can diagnose issues with the request headers, request body, and other information that is being sent in the call.

## Frequently asked questions

### Why are there more Connected Content calls than users or sends? 

Braze may make the same Connected Content API call more than once per recipient because we may need to make a Connected Content API call to render a message payload. Message payloads can be rendered multiple times per recipient for validation, retry logic, or other internal purposes.

It’s expected that a Connected Content API call can be made more than once per recipient, even if the retry logic is not used in the call. We recommend setting the rate limit of any messages that contain Connected Content or configuring your servers to be better able to handle the expected volume.

### How does rate limiting work with Connected Content?

Connected Content doesn’t have its own rate limit. Instead, the rate limit is based on the message-sending rate. We recommend setting the messaging rate limit below your intended Connected Content rate limit if there are more Connected Content calls than messages sent.  

### What’s caching behavior?

By default, POST requests do not cache. However, you can add the `:cache_max_age` parameter to force the POST call to cache.
Caching can help reduce duplicate Connected Content calls. However, it isn’t guaranteed to always result in a single Connected Content call per user.


[16]: [success@braze.com](mailto:success@braze.com)
