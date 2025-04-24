---
nav_title: News Feed
article_title: News Feed for tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "This page describes how to fetch and display News Feed data in your tvOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# News Feed integration

> This article covers how to set up a News Feed for the tvOS platform.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## tvOS Feed integration

Our tvOS SDK supports fetching your News Feed data, such that you can display the News Feed in your application with your own custom UI. To fetch the News Feed, call the following methods and then parse each card by inspecting its class.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab swift %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
