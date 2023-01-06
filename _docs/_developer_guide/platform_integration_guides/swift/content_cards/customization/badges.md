---
nav_title: Badges
article_title: Content Card Badges for iOS
platform: Swift
page_order: 5
description: "This article covers adding badges to your Content Cards in your iOS application."
channel:
  - content cards

---

# Badges

## Requesting unread Content Card counts

If you would like to display the number of unread Content Cards your user has, we suggest you request a card count and represent it with a Badge. Badges are a great way to call attention to new content awaiting your users in the Content Cards. If you'd like to add a badge to your Content Cards, you can filter the number of cards based on the `viewed` property.

## Displaying the number of unviewed Content Cards on the app badge count

In addition to serving as push notification reminders for an app, badges can also be utilized to denote unviewed items in the user's Content Cards feed. Updating the badge count based on unviewed Content Cards updates can be valuable in attracting users back to your app and increasing sessions.

The following sample uses `braze.contentCards` to record the badge count once the app is closed and the user's session ends:

{% tabs %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endtab %}
{% endtabs %}
