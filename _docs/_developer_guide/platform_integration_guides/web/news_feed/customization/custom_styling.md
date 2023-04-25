---
nav_title: Custom Styling
article_title: News Feed Custom Styling for Web
platform: Web
page_order: 0
page_type: reference
description: "This article covers custom News Feeds styling options for your web application."
channel: news feed

---

# Custom Styling

> This article covers custom News Feeds styling options for your web application.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

Braze UI elements come with a default look and feel that matches the composers within the Braze dashboard and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more.

For instance, the following is an example override that will cause the News Feed to appear 800 px wide:

``` css
body .ab-feed {
  width: 800px;
}
```