# Read and unread indicators

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Braze allows you to optionally toggle on unread and read indicators on News Feed cards.

![A News Feed card showing an image of a watch along with some text. In the upper corner of the text is a blue or gray triangle that indicates if a card has been read or not. A blue triangle signifies that a card has been read.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Enabling the indicators

To enable this functionality add the following line to your `braze.xml` file:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Customizing the indicators

These indicators can be customized by altering the `icon_read` and `icon_unread` drawables.

