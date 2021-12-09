---
nav_title: Read & Unread Indicators
article_title: Content Card Read & Unread Indicators for iOS
platform: iOS
page_order: 3
description: "This reference article covers iOS read and unread indicators and how to implement them in your Content Cards."
channel:
  - content cards
---

# Read and unread indicators

## Disabling the unviewed indicator

 ![Read & Unread Indicator]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: height="50%" width="50%"}

You can choose to disable the blue line at the bottom of the card which indicates whether or not the card has been viewed by setting the `disableUnviewedIndicator` property in `ABKContentCardsTableViewController` to YES.

## Customizing the unviewed indicator

The Unviewed indicator can be accessed through the `unviewedLineView` property of the `ABKBaseContentCardCell` class. If you are utilizing Braze's `UITableViewCell` implementations, you should access the property before the cell is drawn.

For example, to set the color of the unviewed indicator to red:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
