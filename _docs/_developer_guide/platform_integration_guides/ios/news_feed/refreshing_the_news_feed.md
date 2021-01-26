---
nav_title: Refreshing the News Feed
platform: iOS
page_order: 4

---

# Refreshing the News Feed

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

For more information see the [`Appboy.h` header file][15].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#setting-delegates
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#customizing-in-app-message-behavior-on-click
[3]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Example/Stopwatch
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/FeedAndFeedbackUIViewController.m
[10]: {% image_buster /assets/img_archive/UONewsFeed.png %} "Urban Outfitters News Feed"
[11]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h "Appboy.h Header File"
[28]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[40]: {{site.baseurl}}/help/best_practices/news_feed/
[42]: {% image_buster /assets/img_archive/badge_example.png %} "Badge Example"
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}
