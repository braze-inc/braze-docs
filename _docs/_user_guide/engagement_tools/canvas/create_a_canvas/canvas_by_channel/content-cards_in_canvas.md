---
nav_title: Content cards
article_title: Content Cards in Canvas
page_order: 1
page_type: reference
description: "This reference article describes features and nuances specific to using Content Cards as a messaging channel within Canvas."
tool: Canvas
channel: content cards

---

# Content Cards in Canvas

> Content Cards can be sent to your customers as part of their Canvas journey. This article describes features and nuances specific to using Content Cards as a messaging channel within Canvas.

As with other Canvas messaging channels, Content Cards will be sent to a user's device when they meet the audience and targeting criteria specified for its step. After the Content Card is sent, it will be available in each eligible user's feed the next time their cards feed is refreshed.

![Content Cards selected as the messaging channel for a Message step.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Two options that will change how the Content Card step will interact with Canvas are its [expiration](#content-card-expiration) and [removal](#removal).

## Content Card expiration {#content-card-expiration}

When composing a new Content Card you can choose when it should expire from the user’s feed based on its send time. The countdown for a Content Card's expiration starts when the user reaches the Message step in the Canvas where the card is sent. The card will be active in the user's feed from this point until it expires. A card can exist in a user's feed for up to 30 days. 

![Expiration settings for a Content Card for a Message step that will be removed after three hours in a user's feed.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Types of expiration

You have two ways to set when a card should disappear from a user's feed: a relative date or an absolute date.

#### Relative dates

When you choose a relative date, like "Remove sent cards after 5 days in a user's feed", you can set an expiration date of up to 30 days.

#### Absolute dates

When you choose an absolute date, like "Remove sent cards on December 1, 2023 at 4 pm", there's some nuance involved.

Although you can specify an expiration duration greater than 30 days, the Content Card will exist in a user's feed for a maximum of 30 days. Specifying a duration greater than 30 days allows you to account for any delays before triggering the Message step, but it does not extend the card's maximum life in the user's feed.

Use caution when setting an expiration date further in advance than 30 days from launching the Canvas. If a user reaches the Message step more than 30 days before the specified expiration date, the card will not be sent.

### Expiration behavior

The Content Card remains available in the user's feed until it reaches its expiration date, even if the user progresses to subsequent steps in the Canvas journey. If you don't want the Content Card to be live when the next steps in the Canvas are delivered, make sure that the expiration is shorter than the delay on subsequent steps.

After a Content Card expires, it will automatically be removed from the user's feed during the next refresh, even if they haven't viewed it yet.

## Content Card removal {#removal}

Content Cards can be removed when users complete a purchase or perform a custom event. You can select one of the following as the removal event: **Perform Custom Event** and **Make Purchase**. Then, select **Add Event**.

!["Remove cards when users complete a purchase or perform a custom event." selected with the trigger to remove cards for users who make a specific purchase for "Bracelet".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Reporting and analytics

After launching a Content Cards step in Canvas you can begin to analyze several different metrics for this step. These metrics include the number of messages sent, unique recipients, conversion rates, total revenue, and more.

![Analytics for a Message step with the Content Card message performance.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

For more information on the available metrics and their definitions, see our [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

## Use cases

#### Promotional offers

Add cards to a user's feed as they qualify for specific promotions and advertisements. For example, if a user becomes eligible for a new offer after performing an action or making a purchase, using Canvas you can send them a Content Card, in addition to other messaging channels, so that the next time they open the app the offer is available to them.

#### Push notification inbox

There are times when a user may dismiss a push notification or delete an email, but you want to remind them or promote the offer in case they change their mind.

Using Canvas, you can add a component that sends both a Content Card and push notification to give users a persistent "inbox" of cards that align with promotional messages sent via push. 

#### Multiple feeds based on categories

You can separate your Content Cards into multiple feeds based on categories such as different topics users can browse, or transactional and marketing feeds. For more information on creating multiple feeds using key-value pairs, check out our guide for [Customizing Content Card feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


