---
nav_title: Defining a News Feed Category
article_itle: Defining a News Feed Category for Web
platform: Web
page_order: 3
page_type: reference
description: "This article covers how to define a News Feed category for your web application."
channel: news feed

---

# Defining a News Feed Category

Instances of the Braze News Feed can be configured to only receive cards from a certain “category”. This allows for the effective integration of multiple News Feed streams within a single application.

News Feed categories can be defined by providing the third `allowedCategories` parameter to `toggleFeed`:

``` javascript
appboy.display.toggleFeed(undefined, undefined, [appboy.Card.Category.NEWS]);
```

You can also populate a feed with a combination of categories like in the following example:

``` javascript
appboy.display.toggleFeed(undefined, undefined, [appboy.Card.Category.ANNOUNCEMENTS, appboy.Card.Category.NEWS]);
```
