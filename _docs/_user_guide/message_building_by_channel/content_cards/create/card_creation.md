---
nav_title: Card Creation
article_title: Card creation
alias: /card_creation/
description: "This article describes the differences between Content Card creation at campaign launch versus at first impression."
page_order: 1
tool: Campaigns
channel:
  - content cards
---

# Card creation

> You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns by specifying when the card is created.

{% alert important %}
Control over card creation is unavailable for use in Canvas steps.
{% endalert %}

## Prerequisites

To take advantage of this feature, you must upgrade to the following minimum SDK versions:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

After upgrading the SDK, your mobile users must upgrade their app. You can filter your campaign audience to only [target users on these minimum app versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Overview

You can choose when Braze creates a card on the **Delivery** step when creating a new [Content Card campaign][2] with scheduled delivery.

![Content Card Controls section when editing the delivery of a scheduled Content Card.][1]

The following options are available:

- **At campaign launch:** The previous default behavior for Content Cards. Braze calculates audience eligibility and personalization when the campaign launches, then creates the card and stores it until the user opens your app.
- **At first impression:** When the user next opens your app (that is, starts a new [session][3]), Braze determines which Content Cards the user is eligible for, templates any personalization like Liquid or Connected Content, then creates the card.

{% alert note %}
For both options, after a card is created, Braze does not recalculate audience eligibility or personalization.
{% endalert %}

### Differences between creating cards at launch versus at first impression

This section describes the main differences between card creation at launch versus at first impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">When campaign is launched</th>
    <th class="tg-0pky">At first impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">When to use this</td>
    <td class="tg-0pky">If you need content to be snapshot at a specific time (the launch time).</td>
    <td class="tg-0pky">If you need to display cards to new or anonymous users who may enter the segment after launch.<br><br>If you're using personalization and want the latest content to be available on the card.</td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze evaluates audience membership when the campaign sends.<br><br>New or anonymous users will not be evaluated for eligibility if they try to view the card after the campaign sends. For recurring campaigns, this will be at the next recurrence interval.</td>
    <td class="tg-0pky">Braze evaluates membership when the user next opens your app (starts a session).<br><br> This setting will have a wider audience reach because any new or anonymous users will always be evaluated for eligibility when they try to view the card.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalization</td>
    <td class="tg-0pky">Braze evaluates Liquid, Connected Content, and Content Blocks at the time the campaign is launched. For recurring campaigns, this will be at the next recurrence interval.</td>
    <td class="tg-0pky">Braze evaluates Liquid, Connected Content, and Content Blocks at the time of first impression or after the next recurrence interval.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytics</td>
    <td class="tg-0pky"><em>Messages Sent</em> refers to the number of cards created and available to be seen. This doesn't count whether the users viewed the card.</td>
    <td class="tg-0pky"><em>Messages Sent</em> refers to the number of cards displayed to users. <br><br>While your reachable users and impressions will not change, you can expect to see a decrease in send volume (<em>Messages Sent</em>) when a card is created at first impression compared to if the same card was created at campaign launch.</td>
  </tr>
  <tr>
    <td class="leftHeader">Processing time</td>
    <td class="tg-0pky">Cards are created for every eligible user in the segment at the time of launch. For large audiences, we recommend to select <b>At First Impression</b>, as cards will be available more quickly after launch.</td>
    <td class="tg-0pky">Cards are created the first time a user tries to view the card, so it may take 1-2 seconds to display on the first impression.</td>
  </tr>
</tbody>
</table>

## Considerations

### Changing card creation after launch

Braze recommends not changing how cards are created after a campaign has launched. Due to the differences in how Messages Sent is calculated between the two card creation types, changing how cards are created after the campaign has launched can affect the accuracy of your send volume.

### Potential processing time

We recommend that campaigns with large audiences select the option to create cards at first impression, as cards will be available much more quickly after the campaign is launched. Campaigns which are triggered on session start may also want to consider moving to create card at first impression to realize performance improvements.

When cards are created at first impression, it may take 1–2 seconds for the cards to process. The length of this processing time depends on various factors, such as the card size and the complexity of the message templating options. For example, the processing time for cards using Connected Content will be at least as long as the Connected Content response time.

### Previous SDK versions

If a user's app is running a previous version of the SDK, they will still receive Content Cards sent with a specified card creation. However, cards will take longer to appear to these users, and may not appear until the next Content Card sync.

[1]: {% image_buster /assets/img_archive/card_creation.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/
[3]: https://www.braze.com/resources/articles/whats-an-app-session-anyway
