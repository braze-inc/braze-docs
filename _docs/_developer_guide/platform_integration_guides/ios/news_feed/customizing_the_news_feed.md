---
nav_title: Customization
platform: iOS
page_order: 5
search_rank: 5
---

# Customization

## Overriding Default Images in the News Feed

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app’s image bundle. Then, rename the file with the image’s name (see below) to override the default image in our library. The image names for the Read icon and Placeholder image (when a user has a poor connection) for News Feed are:
* Read icon indicator: “Icons_Read"
* Placeholder image: "img-noimage-lrg"

{{site.data.alerts.note}} Be sure to upload the `@2x` and `@3x` versions of the images as well to accommodate different phone sizes. {{site.data.alerts.end}}

## Creating a Custom News Feed

You can create your own News Feed interface by extending `ABKNewsFeedTableViewController`. You can customize all UI elements and News Feed behavior in this way.

For an example, see the [News Feed sample app][11].


[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#setting-delegates
[2]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#customizing-in-app-message-behavior-on-click
[3]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Example/Stopwatch
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/FeedAndFeedbackUIViewController.m
[10]: {% image_buster /assets/img_archive/UONewsFeed.png %} "Urban Outfitters News Feed"
[11]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h "Appboy.h Header File"
[28]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[40]: {{ site.baseurl }}/help/best_practices/news_feed/
[42]: {% image_buster /assets/img_archive/badge_example.png %} "Badge Example"
[43]: {% image_buster /assets/img_archive/sample_news_feed.png %}
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}
