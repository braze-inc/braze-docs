---
nav_title: News Feed Categories
page_order: 9

page_type: reference
description: "This reference article describes News Feed Categories, which make it possible to integrate multiple instances of the News Feed into your application."
tool: Dashboard
channel: news feed
---

# News Feed categories

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

> News Feed categories make it possible to integrate multiple instances of the News Feed into your application. It's possible to integrate feeds within different windows that only display News Feed cards of a certain category.

![The News Feed panel with a Captioned Image Card Preview for a News Feed item titled "Sweet Teeth - Buy candy in bulk!" with the message "Satisfy your sweet tooth and stop by our store! Mention this ad and get 50% off your first bag of candy." There are four News Feed categories checkboxes: News, Announcements, Advertising, and Social. None of the categories are selected.]({% image_buster /assets/img_archive/Newsfeed_category.png %})

Marking a News Feed as being from a specific category is not visible to the end user. By default, the Braze News Feed will display cards of all categories, unless a feed is specifically configured in the app code to display specific categories. For more information on the app code configuration, see [Defining a News Feed Category]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/).

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
