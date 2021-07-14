---
nav_title: Best Practices
page_title: News Feed Best Practices
page_order: 20

page_type: reference
description: "This article provides best practices for designing and customizing News Feed cards."
channel: news feed
no_index: true
---

# News Feed Best Practices

The Braze News Feed is a targeted, dynamic stream of rich content. It offers a powerful way to reach users with continuously updated content that does not require additional development work. This content can be targeted at various segments and scheduled in the same way as other Braze messages. Each card consists of a title, a summary, an image, and optionally a URL. The feed also includes the ability to deep-link within the app, link directly to the App Store, Google Play, etc. or direct users to a web view. This unique Braze UI element must be enabled during [integration][1]. Make sure to discuss it with your developers.

To learn about the different types of News Feed cards, how to create them, use cases, as well as card and image specifications, please read our [page on creating News Feed items][4].

> Braze improves load times by using a global CDN to host all News feed images.

{% alert note %}
Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel - it is more flexible, customizable, and reliable. It is also easier to find and use in the Braze product. Contact your Braze account manager for more information.
{% endalert %}

## Best Practices {#news-feed-best-practices}

At Braze, we value the customization that News Feed brings to the table. Here are some of our best practices and tips to help you get the most out of Braze.

### Make it Eye-Catching
The more noticeable, relevant and interesting your News Feed is, the more likely it will be seen by others.  

- Use the News Feed to help make your app feel dynamic and regularly updated by showcasing new content.
- Diversify the type of templated card announcements to keep the News Feed interesting
- Take advantage of the visual space by incorporating images and graphics that stand out.

### Make it Personal
Companies and their users love and value personalization.

- Customize the News Feed to reflect your brand’s identity and create a seamless app experience.
- Keep in mind that targeted modules can immediately inspire action within the app, and protocol URLs can direct attention to different sections of the app, encouraging specific behavior like reviews, purchases and more.
- Segment users and tailor certain announcements to inspire specific action.

### Make it Useful
The content you choose to show through the News Feed can range widely and work in tandem with campaigns.  

- Provide announcements that encourage interaction, highlight news and promote sales.
- Develop a schedule for campaigns like onboarding etc., and determine the proper cadence and frequency of messaging.
- Strengthen and reinforce campaigns by integrating other multichannel messages in the News Feed

## Integration Example

1-800-Flowers.com uses the News Feed to deliver relevant information to its users. The SDK integration remains entirely transparent: there is no mention of Braze in the app itself and the News Feed module has a design aesthetic that is consistent with the rest of the app.

![shapefeed][2]{: style="max-width:50%;"}

You can view more examples of News Feeds in our [Case Studies][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
[3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
