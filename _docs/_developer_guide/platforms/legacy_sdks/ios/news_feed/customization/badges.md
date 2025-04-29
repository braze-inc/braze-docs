---
nav_title: Badges
article_title: News Feed Badges for iOS
platform: iOS
page_order: 3
description: "This reference article covers how to implement News Feed badge counts in your iOS application."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Badges

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Requesting unread News Feed card counts

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Badges are a great way to call attention to new content awaiting your users in the News Feed. If you'd like to add a badge to your News Feed, the Braze SDK provides methods to query the following:

- Unread News Feed cards for the current user
- Total viewable News Feed cards for the current user

The following method declarations in [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html) describe this in detail:

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## Displaying the number of unread News Feed items on the app badge count

In addition to serving as push notification reminders for an app, badges can also denote unviewed items in the user's News Feed. Updating the badge count based on unread News Feed updates can be a valuable tool in attracting users back to your app and increasing sessions.

Call this method which records the badge count after the app is closed and the user's session ends:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

At any point, for example, in the `applicationDidBecomeActive` method, use the following code to clear the badge count:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

For more information, see the `Appboy.h` [header file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).

