---
nav_title: Defining a category
article_title: Defining a News Feed Category for Web
platform: Web
page_order: 3
page_type: reference
description: "This article covers how to define a News Feed category for your web application."
channel: news feed

---

# Defining News Feed categories

> This article covers how to define a News Feed category for the Braze Web SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Defining a category

Instances of the Braze News Feed can be configured to only receive cards from a certain "category". This allows for the effective integration of multiple News Feed streams within a single application.

News Feed categories can be defined by providing the third `allowedCategories` parameter to `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

You can also populate a feed with a combination of categories like in the following example:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
