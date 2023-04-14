---
nav_title: Customizing Card Behavior
article_title: Customizing Content Card Behavior
page_order: 2
description: ""
channel:
  - content cards
---

# Customizing Content Card behavior

## Key-value pairs
Key-value pairs can control the layout, text, font, colors, position, and general info.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

### Retrieving key-value pairs

Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

## Interactive Content Cards

![]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

### Dashboard configuration
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:35%;float:left;margin-left:15px;border:none;"}

## Content card badges

Badges are small icons that are ideal for getting a user's attention. Using badges to alert the user about new Content Card content can attract users back to your app and increase sessions.

![An iPhone home screen showing a Braze sample app named Swifty with a red badge displaying the number 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

### Displaying the number of unread Content Cards as a badge

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

## Adding read/unread indicators

Content Cards contain a blue line at the bottom of the card which indicates whether or not the card has been viewed. This article provides examples of modifying this behavior. For more information on customizing Content Cards UI attributes, refer to [Customizing Feed]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/).

![Two Content Cards displayed side by side. The card on the left has a blue line at the bottom, indicating it has not been seen. The card on the right does not have a blue line, indicating it has already been seen.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

### Disabling the unread indicator

Disable the unviewed indicator line by setting the `attributes.cellAttributes.unviewedIndicatorColor` property in your `Attributes` struct to `.clear`. 

### Changing unread indicator color

The color of the unviewed indicator can be set by assigning a value to the tint color of your `BrazeContentCardUI.ViewController` instance:

{% tabs %}
{% tab swift %}

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

{% endtab %}
{% endtabs %}

However, if you wish to modify only the unviewed indicator, you can access the `unviewedIndicatorColor` property of your `BrazeContentCardUI.ViewController.Attributes` struct. If you utilize Braze's `UITableViewCell` implementations, you should access the property before the cell is drawn.

For example, to set the color of the unviewed indicator to red:

{% tabs %}
{% tab swift %}

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Customization via `Attributes` is only available in Swift.
{% endalert %}

