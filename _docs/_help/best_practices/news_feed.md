---
nav_title: News Feed
page_order: 3
---
# News Feed

The Braze News Feed is a targeted, dynamic stream of rich content. It offers a powerful way to reach users with continuously updated content that does not require additional development work. This content can be targeted at various segments and scheduled in exactly the same way as other Braze messages. Each card consists of a title, short summary, an image and optionally a URL. The feed also includes the ability to deep link within the app, link directly to the App Store, Google Play etc. or direct users to a web view. This unique Braze UI element must be enabled during [integration][2]. Make sure to discuss it with your developers.

To learn about the different types of News Feed cards, how to create them, as well as card and image specifications, please read our [page on creating News Feed items][21].

> Braze improves load times by using a global CDN to host all News feed images.

# Use Cases {#news-feed-use-cases}

- Advertising app updates
- "Drip Marketing" Welcome Campaigns
- Teasing out a user's willingness to pay.
  - Offering a schedule of steadily increasing discounts using targeted News Feed cards can help you see exactly how much your service is worth to different user segments.
- Achievements and badges
  - When a user completes a noteworthy task or takes a desired action after being targeted by a marketing campaign, you can isolate that segment in order to recognize their accomplishment with a News Feed card.
    - You might even want to tie a specific reward to this acknowledgement such as an in-app discount.
- Prompting users to share to various social networks.
- Highlighting other apps or content your company has created via cross-promotion cards.
- ["Deep-linking"][8]
  - You can use protocol URLs to point users at any resource housed within your app.
  - For example, a video messaging app might want to have a News Feed card point at a video that is elsewhere within the app.
  - You could even potentially use this to design your entire app navigation scheme around our News Feed!

# Best Practices {#news-feed-best-practices}

- Use the News Feed to help make your app feel dynamic and regularly updated by showcasing new content.
- Provide announcements that encourage interaction, highlight news and promote sales.
- Take advantage of the visual space by incorporating images and graphics that stand out.
- Customize the News Feed to reflect your brand’s identity and create a seamless app experience.
- Keep in mind that targeted modules can immediately inspire action within the app, and protocol URLs can direct attention to different section of the app, encouraging specific behavior like reviews, purchases and more.
- Develop a schedule for campaigns like onboarding etc., and determine the proper cadence and frequency of messaging.
- Diversify the type of templated card announcements to keep the News Feed interesting
- Strengthen and reinforce campaigns by integrating other multi-channel messages in the News Feed
- Segment users and tailor certain announcements to inspire specific action.


## Integration Example

![shapefeed][9]

1-800-Flowers.com uses the News Feed to deliver relevant information to its users. The SDK integration remains entirely transparent: there is no mention of Braze in the app itself and the News Feed module has a design aesthetic that is consistent with the rest of the app.

You can view more examples of News Feeds in our [Client Integration Gallery][18].


[1]: {% image_buster /assets/img_archive/individualizednewsfeed.png %}
[2]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/
[3]: {% image_buster /assets/img_archive/classiccard.png %}
[4]: {% image_buster /assets/img_archive/captionedimage.png %}
[5]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/crosspromo.png %}
[8]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[9]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
[18]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-newsfeed
[21]:{{ site.baseurl }}/user_guide/engagement_tools/news_feed/
