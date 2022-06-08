---
nav_title: Read & Unread Indicators
article_title: Content Card Read & Unread Indicators for Android and FireOS
page_order: 4.3
platform: 
  - Android
  - FireOS
description: "This reference article covers Android and FireOS read and unread indicators and how to implement them in your Content Cards."
channel:
  - content cards

---

# Read and unread indicators {#read-indicators-for-android}

Braze allows you to optionally toggle on unread and read indicators on Content Cards.

![Two Content Cards displayed side by side. The first card has a blue line at the bottom, indicating it has not been seen. The second card does not have a blue line, indicating it has already been seen.][1]

## Customizing the indicators {#customizing-the-indicators-for-android}
The color of these indicators can be customized by altering the values in `com_braze_content_cards_unread_bar_color` in your `colors.xml` file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

[1]: {% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}
