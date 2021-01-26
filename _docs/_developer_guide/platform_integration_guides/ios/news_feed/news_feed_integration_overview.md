---
nav_title: News Feed Integration Overview
platform: iOS
page_order: 1

---

# News Feed Integration Overview
Integrating the view controller `ABKNewsFeedViewController` will display the Braze News Feed.

You have a great deal of flexibility in how you choose to display the view controllers. There are different versions of the view controllers to accommodate different navigation structures.

>  The News Feed that is called by the default behavior of an in-app message click will not respect any delegates that you set for the News Feed. If you want to respect that, you must [set the delegate on `ABKInAppMessageUIController`][1] and implement the `ABKInAppMessageUIDelegate` delegate method [`onInAppMessageClicked:`][2].

# News Feed View Controller Integration Options

The News Feed can be integrated with 2 view controller contexts, either in code or via a storyboard implementation.

## Navigation Context -- ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
To customize the navigation bar's title, set the title property of the `ABKNewsFeedTableViewController` instance's `navigationItem`.
{% endalert %}

## Modal Context -- ABKFeedViewControllerModalContext

- Used to present the view controller in a modal view, with a navigation bar on top and a Done button on the right side of the bar
- Set the modal's title via the embedded `ABKNewsFeedTableViewController` instance's `navigationItem`'s `title` property
- If a delegate __is NOT set__ the Done button will dismiss the modal view
- If a delegate __is set__ the Done button will call the delegate, and the delegate itself will be responsible for dismissing the view

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

>  The [News Feed sample app][3] contains examples of the view controllers.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#setting-delegates
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#customizing-in-app-message-behavior-on-click
[3]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/FeedAndFeedbackUIViewController.m
[10]: {% image_buster /assets/img_archive/UONewsFeed.png %} "Urban Outfitters News Feed"
[11]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h "Appboy.h Header File"
[28]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[40]: {{site.baseurl}}/help/best_practices/news_feed/
[42]: {% image_buster /assets/img_archive/badge_example.png %} "Badge Example"
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}
