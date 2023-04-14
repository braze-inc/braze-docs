---
nav_title: Customizing Card Behavior
article_title: Customizing Content Card Behavior
page_order: 2
description: "This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations."
channel:
  - content cards
---

# Customizing Content Card behavior

> This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations.

## Key-value pairs
Key-value pairs can control the layout, text, font, colors, position, and general info.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% alert note %}
We do not recommend sending nested JSON values as key-value pairs. Instead, flatten the JSON before sending it. 
{% endalert %}

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}



### Retrieving key-value pairs

Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

## Interactive Content Cards

![]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

### Dashboard configuration
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. 

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:35%;float:left;margin-right:15px;border:none;"}

Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:35%;float:left;margin-right:15px;border:none;"}

Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:35%;float:left;margin-right:15px;border:none;"}

Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

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

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/#content-cards
