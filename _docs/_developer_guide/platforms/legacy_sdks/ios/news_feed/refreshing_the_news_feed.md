---
nav_title: Refreshing the Feed
article_title: Refreshing the News Feed for iOS
platform: iOS
page_order: 6
description: "This reference article shows how to refresh the News Feed in your iOS application."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Refreshing the News Feed

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

You can manually request Braze to refresh the user's News Feed in `Appboy.h` using `- (void) requestFeedRefresh;`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

For more information, see the `Appboy.h` [header file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).


