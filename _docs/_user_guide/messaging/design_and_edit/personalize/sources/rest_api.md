---
nav_title: REST API
article_title: REST API
page_order: 1
description: "Learn how to use Connected Content to pull data from REST APIs into your messages for real-time personalization."
---

# REST API

> Pull data from external REST APIs directly into your messages at send time using [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). This lets you personalize messages with real-time information from your own servers, third-party services, or any publicly accessible API endpoint.

## How it works

{% raw %}
Connected Content makes an HTTP request to the URL you specify, then stores the response so you can reference it with Liquid. Add a `{% connected_content %}` tag to your message, and Braze calls the endpoint when the message is sent.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

Connected Content supports GET and POST requests. Braze requires the server to respond within two seconds, so design your endpoints for low latency.

## Common use cases

| Use case | Description |
| --- | --- |
| Product recommendations | Fetch personalized product picks from a recommendation engine |
| Real-time pricing or inventory | Display current prices or stock levels at send time |
| Weather-based content | Pull local weather data to tailor messaging |
| Loyalty point balances | Show up-to-date rewards or account balances |
| Content feeds | Insert the latest blog posts, articles, or news items |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Authentication

Braze supports basic authentication, token authentication, and OAuth for Connected Content requests. You can store credentials securely in the Braze dashboard under **Settings** > **Connected Content** and reference them in your API calls.

For more information, see [Making a Connected Content API call]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#authentication-types).

## Error handling

If the endpoint returns an error or times out, Braze renders an empty string in place of the Connected Content response. You can detect failures by checking if the saved variable is null and conditionally abort the message or display fallback content.

For more information, see [Aborting Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/).

## Performance considerations

Because Braze delivers messages at high volume, your server must handle thousands of concurrent connections. Use caching where appropriate and set rate limits on your messages to avoid overloading external endpoints.

For the complete Connected Content reference, see [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).
