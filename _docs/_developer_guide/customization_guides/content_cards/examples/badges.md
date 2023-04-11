---
nav_title: Badges
article_title: Content Card Badges for iOS
platform: Swift
page_order: 1
description: "This article covers adding badges to your Content Cards in your iOS application."
channel:
  - content cards

---

# Content card badges for iOS

Badges are small icons that are ideal for getting a user's attention. Using badges to alert the user about new Content Card content can attract users back to your app and increase sessions.

![An iPhone home screen showing a Braze sample app named Swifty with a red badge displaying the number 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

## Displaying the number of unread Content Cards as a badge

You can display the number of unread Content Cards your user has as a badge on your app's icon. The following sample uses `braze.contentCards` to request and display the number of unread Content Cards. Once the app is closed and the user's session ends, this code requests a card count, filtering the number of cards based on the `viewed` property.

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
