---
nav_title: Deep Linking to In-App Content
article_title: Deep Linking to In-App Content
page_order: 2
description: "Deep linking is a way of launching a native app and providing additional information telling it to do some specific action or show specific content. This reference article covers how to deep-link in your in-app message content."

---

# Deep linking to in-app content

## What is deep linking?

Deep linking is a way of launching a native app and providing additional information telling it to do some specific action or show specific content.

There are three parts to this:

1. Identify which app to launch
2. Instruct the app which action to perform
3. Provide the action with any additional data it will need

Deep links are custom URIs that link to a specific part of the app and contain all of the above parts. The key is defining a custom scheme. `http:` is the scheme with which almost everyone is familiar but schemes can begin with any word. A scheme must start with a letter, but can then contain letters, numbers, plus-signs, minus-signs or dots. Practically speaking, there is no central registry to prevent conflicts, so it is a best practice to include your domain name in the scheme. For example, `twitter://` is the iOS URI to launch Twitter's mobile app.

Everything after the colon within a deep link is free-form text. It's up to you to define its structure and interpretation, however, a common convention is to model it after `http:` URLs, including a leading `//` and query parameters (e.g. `?foo=1&bar=2`). For the Twitter example, `twitter://user?screen_name=[id]` would be utilized to launch a specific profile in the app.

These deep links are a powerful tool when used in tandem with the Braze [News Feed][11]. Providing deep links as the URI within News Feed items allows you to use the News Feed as an individualized navigation tool to direct users to content inside in your app. They can also be used to direct users from [push notifications][1] and in-app messages to relevant app sections and content.

{% alert note %}
Keep in mind that enabling these deep links requires some additional setup within your app. Please reference our documentation on [deep links for iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links) and on how to [deep link to the News Feed for Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance) to understand the requirements for implementation.
{% endalert %}

## UTM tags and campaign attribution

### What is a utm tag?

[UTM (Urchin Traffic Manager) tags][4] allow you to include campaign attribution details directly within links. UTM tags are used by Google Analytics to collect campaign attribution data, and can be used to track the following properties:

- `utm_source`: the identifier for the source of the traffic (e.g. `my_app`)
- `utm_medium`: the campaign medium (e.g. `newsfeed`)
- `utm_campaign`: the identifier for the campaign (e.g. `spring_2016_campaign`)
- `utm_term`: identifier for a paid search term that brought the user to your app or website (e.g. `pizza`)
- `utm_content`: an identifier for the specific link/content that the user clicked on (e.g. `toplink` or `android_iam_button2`)

UTM tags can be embedded into both regular HTTP (web) links and deep links and tracked using Google Analytics.

### Using utm tags with braze

If you want to use UTM tags with regular HTTP (web) links—for example, to do campaign attribution for your email campaigns—and your organization already uses Google Analytics, you can simply use [Google's URL builder][6] to generate UTM links. These links can be readily embedded into Braze campaign copy just like any other link.

In order to use UTM tags in deep links to your app, your app must have the relevant [Google Analytics SDK][5] integrated and [correctly configured to handle deep links][7]. Check with your developers if you're unsure about this.

Once the Analytics SDK is integrated and configured, UTM tags can be used with deep links in Braze campaigns. To set up UTM tags for your campaign, simply include the necessary UTM tags in the destination URL or deep links. The examples below show how to use UTM tags in push notifications, News Feed cards and in-app messages.

#### Attributing push opens with utm tags

To include UTM tags in your deep links for push notifications, simply set the on click behavior of the push message to be a deep link, write the deep link address and include the desired UTM tags in the following fashion:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![UTM Tags in Push Message][8]

#### Attributing news feed clicks with utm tags

News Feed items deep linking into your app can be configured to use UTM tags as well. Note that you can use `utm_content` to separate between deep links on different OSes.

![UTM Tags in News Feed][9]

#### Attributing in-app message clicks with utm tags

Similarly to push notifications and News Feed cards, you can include UTM tags in the deep links included within your in-app messages.

![UTM Tags in In-App Message][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[7]: https://developers.google.com/analytics/solutions/mobile-campaign-deep-link
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
