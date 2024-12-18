---
nav_title: Styling
article_title: News Feed Custom Styling for Web
platform: Web
page_type: reference
description: "This article covers custom News Feeds styling options for your web application."
channel: news feed

---

# Custom News Feed styling

> This article covers custom News Feeds styling options for your web application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze UI elements come with a default look and feel that matches the composers within the Braze dashboard and aims for consistency with other Braze mobile platforms. Default styles in Braze are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more.

For instance, the following is an example override that will cause the News Feed to appear 800&nbsp;px wide:

``` css
body .ab-feed {
  width: 800px;
}
```