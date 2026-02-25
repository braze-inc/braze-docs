---
nav_title: Deep linking to in-app content
article_title: Deep Linking to In-App Content
page_order: 3
description: "This reference article covers guidance on how to add deep linking to your in-app message content."

---

# Deep linking to in-app content

## What is deep linking?

Deep linking is a way of launching a native app and providing additional information telling it to do a specific action or show specific content.

There are three parts to this:

1. Identify which app to launch.
2. Instruct the app on which action to perform.
3. Provide the action with any additional data it will need.

Deep links are custom URIs that link to a specific part of the app and contain all three of these parts. The key is defining a custom scheme. `http:` is the scheme with which almost everyone is familiar but schemes can begin with any word. A scheme must start with a letter, but can then contain letters, numbers, plus-signs, minus-signs or dots. Practically speaking, there is no central registry to prevent conflicts, so it is a best practice to include your domain name in the scheme. For example, `twitter://` is the iOS URI to launch the mobile app for X, formerly Twitter.

Everything after the colon within a deep link is free-form text. It's up to you to define its structure and interpretation; however, a common convention is to model it after `http:` URLs, including a leading `//` and query parameters (for example, `?foo=1&bar=2`). For the previous example, `twitter://user?screen_name=[id]` would be used to launch a specific profile in the app.

{% alert important %}
Braze doesn't support using a wrapper like Flutter to send deep links. To use this feature, you must configure deep links at the native layer.
{% endalert %}

## UTM tags and campaign attribution

### What is a UTM tag?

[UTM (Urchin Traffic Manager) tags](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) allow you to include campaign attribution details directly within links. UTM tags are used by Google Analytics to collect campaign attribution data, and can be used to track the following properties:

- `utm_source`: The identifier for the source of the traffic (for example,`my_app`)
- `utm_medium`: The campaign medium (for example,`newsfeed`)
- `utm_campaign`: The identifier for the campaign (for example,`spring_2016_campaign`)
- `utm_term`: Identifier for a paid search term that brought the user to your app or website (for example,`pizza`)
- `utm_content`: An identifier for the specific link or content that the user clicked on (for example,`toplink` or `android_iam_button2`)

UTM tags can be embedded into both regular HTTP (web) links and deep links and tracked using Google Analytics.

### Using UTM tags with Braze

If you want to use UTM tags with regular HTTP (web) links (for example, to do campaign attribution for your email campaigns) and your organization already uses Google Analytics, you can use [Google's URL builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) to generate UTM links. These links can be readily embedded into Braze campaign copy just like any other link.

To use UTM tags in deep links to your app, your app must have the relevant [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) integrated and correctly configured to handle deep links. Check with your developers if you're unsure about this.

After the Analytics SDK is integrated and configured, UTM tags can be used with deep links in Braze campaigns. To set up UTM tags for your campaign, include the necessary UTM tags in the destination URL or deep links. The following examples show how to use UTM tags in push notifications and in-app messages.

#### Attributing push opens with UTM tags

To include UTM tags in your deep links for push notifications, set the on-click behavior of the push message to be a deep link, then write the deep link address and include the desired UTM tags in the following fashion:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### Attributing in-app message clicks with UTM tags

To include UTM tags in the deep links in your in-app messages, use the following:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

