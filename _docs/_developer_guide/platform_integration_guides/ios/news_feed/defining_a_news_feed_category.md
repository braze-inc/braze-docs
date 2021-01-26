---
nav_title: Defining a News Feed Category
platform: iOS
page_order: 2

---

# Defining a News Feed Category

Instances of the Braze News Feed can be configured to only receive cards from a certain "category". This allows for the effective integration of multiple News Feed streams within a single application. For more information on this feature visit our [News Feed Best Practices][40] doc.

News Feed Categories can be defined by calling the following methods as you load the News Feed:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAll];
[newsFeed setCategories:ABKCardCategoryAnnouncements];
[newsFeed setCategories:ABKCardCategoryAdvertising];
[newsFeed setCategories:ABKCardCategorySocial];
[newsFeed setCategories:ABKCardCategoryNews];
[newsFeed setCategories:ABKCardCategoryNoCategory];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory.all
newsFeed.categories = ABKCardCategory.announcements
newsFeed.categories = ABKCardCategory.advertising
newsFeed.categories = ABKCardCategory.social
newsFeed.categories = ABKCardCategory.news
newsFeed.categories = ABKCardCategory.noCategory
```

{% endtab %}
{% endtabs %}


You can also populate a feed with a combination of categories as in the following example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory([.announcements, .advertising])
```

{% endtab %}
{% endtabs %}

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
