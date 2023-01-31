---
nav_title: About Content Cards
article_title: About Content Cards
page_order: 0
description: "This reference article provides an overview of the Braze Content Card channel and common use cases."
channel:
  - content cards
search_rank: 4
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} About Content Cards

> This reference article provides an overview of the Braze Content Card channel and common use cases.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics, and easy coordination with push notifications.

Content Cards are available as an add-on feature. To get started with Content Cards, reach out to your Braze customer success manager or our support team for more information.

{% alert note %}
If you're using our News Feed tool, we recommend that you move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. News Feed is being deprecated. See our [Migration Guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) or contact your Braze account manager for more information.
{% endalert %}

Content Cards are not available out-of-the-box and must be purchased. To get started with Content Cards, reach out to your Braze customer success manager or our support team.

## Advantages of using Content Cards

Wondering about the benefits of using Content Cards versus having your developers build content into your app? Here are some advantages of using Content Cards:

- **Easier segmentation and personalization:** Your user data lives in Braze, making it easy to define your audience and personalize your messages with Content Cards.
- **Centralized reporting:** Content Card analytics are tracked in Braze, so you have insight into all of your campaigns in one centralized location.
- **Cohesive customer journeys:** You can combine Content Cards with other channels in Braze to create consistent customer experiences. A popular use case is sending a push notification, then saving that notification as a Content Card in your app for anyone who didn’t engage with the push. If the content is built directly into your app by your developers, then it’s siloed from the rest of your messaging.
- **More control over the messaging experience:** While you’ll still need your developers to help with the initial setup of Content Cards, after that, you’ll be able to control the message, recipients, timing, and more straight from your Braze dashboard.

## Use cases

This section outlines some common use cases for Content Cards.

{% alert tip %}
For more inspiration, we highly recommend that you check out our [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), which includes over 20 customizable campaigns, including referral programs, new product launches, and subscription renewal.
{% endalert %}

### Onboarding and next steps

As new customers explore your app and website, walk them through the values and benefits of what you offer with strategically placed Content Cards. Encourage customers to opt into other communication channels with a Content Card on your homepage, and save outstanding onboarding tasks in a dedicated onboarding tab powered by Content Cards. Don’t forget to remove a card once a customer has completed the desired task!

> image placeholder

### Recommendations

Use the data you have on user behaviors and preferences to surface relevant content in real time from homepage or inbox Content Cards and draw them back into your product offering.

> image placeholder

### Sales and promotions

Take advantage of Content Cards to highlight promotional messages and unclaimed offers directly on your homepage or in a dedicated promotional inbox. Pull in relevant content based on each customer’s previous purchases to deliver attention-grabbing personalized promotions.

> image placeholder

### Event attendance

Showcase Content Cards at the top of a user’s homepage to encourage event attendance, using location targeting to reach potential customers where they are. Inviting users to relevant physical events makes them feel special, especially with personalized messaging that leverages their previous activity with your brand.

> image placeholder

## Content Card placements

This section provides an overview of the three most common ways to place Content Cards within your app or site:

- Message inbox
- Carousel
- Banner

> image placeholder

### Message inbox

> image placeholder

A message inbox (also called a notification center or feed) is a persistent place in your app or website where you can display Content Cards in whatever format you prefer. Each message in the inbox is its own Content Card. You can create a message inbox to house Content Cards using the default implementation.

#### Benefits

- No opt-in required
- Users can receive many cards in one place
- Easy way to resurface information missed or dismissed on other channels (especially push notifications)

#### Behavior

When implemented out-of-the-box, Content Cards in the inbox can appear as classic, banner, or captioned image cards. You choose where the message inbox will be located in your app. Content Cards come with a default style, but you can choose a custom implementation to display the cards and the feed according to the look and feel of your app.

When a user is eligible for a card, it will automatically appear in their inbox. Content Cards are inherently built to be viewed in bulk, so users will be able to view all cards that they’re eligible for at once.

#### How to implement

Your developers can create a message inbox when they first implement Content Cards. The container for the message inbox cards is included in the Bratze SDK, called a view controller. The view controller handles displaying your Content Cards, and is available for iOS, Android, and web.

### Carousel

Carousels display multiple pieces of content in a single space that your customers can swipe into view. They can be a slideshow of images, text, video, or a combination of all of them.

> pending content

### Banner

Content Cards can appear as a dynamic banner that persistently displays on your home page or at the top of other designated pages.

> pending content

## How Content Cards work

At their core, Content Cards are actually a payload of data, not what the data looks like. Braze provides template views (banner, modal, captioned image) to display the Content Card data, which is ultimately what your message looks like.

> image placeholder

Now let’s get a little technical (just a little). Behind the scenes, there are three main parts of a Content Card:

- **Model:** What kind of data lives in the card
- **View:** What the card looks like
- **Controller:** How the user interacts with the card

For an out-of-the-box implementation, you add the card content—the model—either from the dashboard or via APIs, and the view and controller are handled by what is called a view controller.

### View controller

A view controller is the “glue” between the overall application and the screen. It controls the views that it owns according to the logic of your application. Every app has one, some have more than one.

Braze Content Cards have their own view controller provided, meaning you can integrate Content Cards by adding a few lines of code to your app or site. Your developers can also create a custom Content Card view controller instead of using the standard Braze one for even more customization options.