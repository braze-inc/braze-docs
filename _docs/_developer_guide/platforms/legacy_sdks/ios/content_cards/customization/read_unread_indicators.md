---
nav_title: Read & unread indicators
article_title: Content Card Read & Unread Indicators for iOS
platform: iOS
page_order: 4
description: "This reference article covers iOS read and unread indicators and how to implement them in your Content Cards."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Read and unread indicators

## Disabling the unviewed indicator

![Two Content Cards displayed side by side. The card on the left has a blue line at the bottom, indicating it has not been seen. The card on the right does not have a blue line, indicating it has already been seen.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

You can choose to disable the blue line at the bottom of the card, which indicates whether or not the card has been viewed by setting the `disableUnviewedIndicator` property in `ABKContentCardsTableViewController` to `YES`.

## Customizing the unviewed indicator

The unviewed indicator can be accessed through the `unviewedLineView` property of the `ABKBaseContentCardCell` class. If you use `UITableViewCell` implementations, you should access the property before the cell is drawn.

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
