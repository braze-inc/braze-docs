---
nav_title: Read & Unread Indicators
article_title: Content Card Read & Unread Indicators for iOS
platform: Swift
page_order: 3
description: "This reference article covers iOS read and unread indicators and how to implement them in your Content Cards."
channel:
  - content cards

---

# Content Card read and unread indicators for iOS

Content Cards contain a blue line at the bottom of the card which indicates whether or not the card has been viewed. This article provides examples of modifying this behavior. For more information on customizing Content Cards UI attributes, refer to [Customizing Feed]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/).

![Two Content Cards displayed side by side. The card on the left has a blue line at the bottom, indicating it has not been seen. The card on the right does not have a blue line, indicating it has already been seen.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

## Disabling the unviewed indicator

Disable the unviewed indicator line by setting the `attributes.cellAttributes.unviewedIndicatorColor` property in your `Attributes` struct to `.clear`. 

## Changing colors

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
