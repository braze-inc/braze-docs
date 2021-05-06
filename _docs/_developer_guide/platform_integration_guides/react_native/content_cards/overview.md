---
nav_title: Overview
page_order: 0

platform: Cordova
---

# Content Cards 
{% include video.html id="4FUPxkIq2xc" align="right" %}

With **Content Cards**, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics, and easy coordination with push notifications.
<br><br><br><br>
{% alert note %}
Braze recommends that customers who use our News Feed tool, move over to our Content Cards messaging channel - it is more flexible, customizable, and reliable. It is also easier to find and use in the Braze product. Contact your Braze account manager for more information.
{% endalert %}

## When to Use Content Cards

Content Cards typically sit in a feed of sorts (but not necessarily) and help you take advantage of the visual space by incorporating images and graphics that stand out. You can personalize the cards based on user actions, onboard your customers with a checklist, and much more!

#### Great Use Cases

- Showcase new content.
- Coordinate with push messages to illustrate a persistent record of promotions.
- Give customers without push enabled access to promotions.
- Trigger order confirmations or other personalized communication with your customer.
- Develop and deliver an onboarding schedule.

## Content Cards & Feed

This is what it looks like for your users to open a basic Content Card feed. As you can see, there are three basic types of cards that can sit in the feed - a Banner Card, a Captioned Content Card, and a Classic Content Card.

![Content Cards Feed]({% image_buster /assets/img/sample-torchy-feed-content-cards-braze.png %}){: height="50%" width="50%"}

{% alert note %}
Content Cards have a maximum size of **2kb** (including images, links, and all content) - anything that exceeds that amount will prevent the card from sending.
{% endalert %}

## Content Cards Integration Overview {#content-cards-integration-for-react-native}

In a React Native app, Content Cards can be accessed and displayed directly in JavaScript. To learn more visit our [Integration Guide][1].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/react_native/content_cards/integration/
