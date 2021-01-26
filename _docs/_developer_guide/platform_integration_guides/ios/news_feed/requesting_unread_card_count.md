---
nav_title: Requesting Unread Card Count
platform: iOS
page_order: 3

---

# Requesting Unread Card Count

![News Feed Badge Example][45]

Badges are a great way to call attention to new content awaiting your users in the News Feed. If you'd like to add a badge to your News Feed, the Braze SDK provides methods to query the following:

- Unread News Feed Cards for the current user
- Total Viewable News Feed Cards for the current user

The method declarations in [ABKFeedController][44] below describe this in detail:

```objc
/*!
 * This method returns the number of currently active cards that have not been viewed in the given categories.
 * A "view" happens when a card becomes visible in the feed view.  This differentiates
 * between cards which are off-screen in the scrolling view, and those which
 * are on-screen; when a card scrolls onto the screen, it's counted as viewed.
 *
 * Cards are counted as viewed only once -- if a card scrolls off the screen and
 * back on, it's not re-counted.
 *
 * Cards are counted only once even if they appear in multiple feed views or across multiple devices.
 */
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;

/*!
 * This method returns the total number of currently active cards belongs to given categories. Cards are
 * counted only once even if they appear in multiple feed views.
 */
- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
```

## Displaying Number of Unread News Feed Items on App Badge Count

![Badge Example][42]

In addition to serving as push notification reminders for an app, badges can also be utilized to denote unviewed items in the user's News Feed. Updating the badge count based on unread News Feed updates can be a valuable tool in attracting users back to your app and increasing sessions.

Call this method which records the badge count once the app is closed and the user's session ends.

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Within the above method, implement the following code which actively updates the badge count while the user views cards during a given session.

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

For more information see the [`Appboy.h` header file][15]. The Stopwatch sample application also has a sample implementation of a badge in [FeedAndFeedbackUIViewController.m][4], as well as code clearing the badge count in [`AppDelegate.m`][28].

[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/FeedAndFeedbackUIViewController.m
[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h "Appboy.h Header File"
[28]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[42]: {% image_buster /assets/img_archive/badge_example.png %} "Badge Example"
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}
