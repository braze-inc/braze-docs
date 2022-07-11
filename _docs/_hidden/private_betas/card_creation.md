---
nav_title: Card Creation
article_title: Card creation
permalink: /card_creation/
description: "This article describes the differences between Content Card creation at campaign launch versus at first impression."
hidden: true
---

# Card creation

You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns by specifying when the card is created.

{% alert important %}
Control over card creation is currently in early access and is unavailable for use in Canvas steps. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Prerequisites

To take advantage of this feature, you must upgrade to the following minimum SDK versions:

> TO DO: Update placeholder SDK with correct versions

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

After upgrading the SDK, your mobile users must upgrade their app. You can filter your campaign audience to only [target users on these minimum app versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Overview

You can choose when Braze creates a card on the **Delivery** step when creating a new [Content Card campaign]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) with scheduled delivery.

> TO DO: Add screenshot of UI

The following options are available:

- **At campaign launch:** The previous default behavior for Content Cards. Braze calculates audience eligibility and personalization when the campaign launches, then creates the card and stores it until the user opens your app.
- **At first impression:** When the user next opens your app (that is, starts a new [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze determines which Content Cards the user is eligible for, templates any personalization like Liquid or Connected Content, then creates the card.

{% alert note %}
For both options, after a card is created, Braze does not recalculate audience eligibility or personalization. This information is only evaluated once when the card is first created. Fully dynamic Content Cards are coming later this year.
{% endalert %}

### Differences between creating cards at launch versus at first impression

This section describes the main differences between card creation at launch versus at first impression.

#### Audience and personalization

- **At campaign launch:** Braze calculates audience membership and personalization when the campaign sends. Users who enter the target audience after the campaign sends won't receive the card.
- **At first impression:** Braze calculates audience membership and personalization when the user next opens your app (starts a session). Any new users in the target audience can receive the card. Audience and personalization are not re-evaluated after this content is templated.

#### Analytics

While your reachable users and impressions will not change, you can expect a decrease in send volume (Messages Sent) when cards are created at first impression compared to if the same card was created at campaign launch. This is because of how Braze defines Message Sent for Content Cards.

- **At campaign launch:** Messages Sent refers to the number of cards created and available to be seen and doesn't count whether users viewed the card. 
- **At first impression:** Messages Sent refers to the number of cards displayed to users.

This change, combined with the fact that eligibility is evaluated closer to when users would view the card for cards created at first impression, results in a decrease in sends.

## Considerations

### Changing card creation after launch

Braze recommends not changing how cards are created after a campaign has launched. Due to the differences in how Messages Sent is calculated between the two card creation types, changing how cards are created after the campaign has launched can affect the accuracy of your send volume.

### Potential processing time

When cards are created at first impression, it may take 1–2 seconds for the cards to process, resulting in a slight delay before the card is visible to the user. The length of this delay depends on various factors, such as the card size and the complexity of the message templating options. For example, the processing time for cards using Connected Content will be at least as long as the Connected Content response time.

### Previous SDK versions

If a user's app is running a previous version of the SDK, they will still receive Content Cards sent with a specified card creation. However, cards will take longer to appear to these users, and may not appear until the next Content Card sync.
