---
nav_title: Card creation
article_title: Card Creation
alias: /card_creation/
description: "This article describes the differences between Content Card creation at campaign launch or Canvas step entry versus at first impression."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Card creation

> You can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns and Canvas steps by specifying when the card is created.

## Prerequisites

To take advantage of this feature, you must upgrade to the following minimum SDK versions:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

After upgrading the SDK, your mobile users must upgrade their app. You can filter your campaign or Canvas audience to only [target users on these minimum app versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Overview

{% tabs %}
{% tab Campaign %}

You can choose when Braze creates a card on the **Delivery** step when creating a new [Content Card campaign]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) with scheduled delivery.

![Content Card Controls section when editing the delivery of a scheduled Content Card.]({% image_buster /assets/img_archive/card_creation.png %})

The following options are available:

- **At campaign launch:** The previous default behavior for Content Cards. Braze calculates audience eligibility and personalization when the campaign launches, then creates the card and stores it until the user opens your app. 
- **At first impression (recommended):** When the user next opens your app (that is, starts a new [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze determines which Content Cards the user is eligible for, templates any personalization like Liquid or Connected Content, then creates the card. This option will usually see better performance in card deliveries.

Regardless of your selected option, the Content Card expiration date countdown will begin when the campaign launches.

{% endtab %}
{% tab Canvas %}

You can choose when Braze creates a card on the **Messaging Channels** tab of a Content Card [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![Content Card Controls section when editing the delivery of a scheduled Content Card.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

The following options are available:

- **At step entry:** The previous default behavior for Content Cards. Braze calculates audience eligibility when the user enters the Canvas step, then creates the card and stores it until the user opens your app.
- **At first impression (recommended):** Braze calculates audience eligibility when the user enters the Canvas step. When the user next opens your app (that is, starts a new [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze templates any personalization like Liquid or Connected Content, then creates the card. This option will see better performance in card deliveries and more up to date personalization.

Regardless of your selected option, the Content Card expiration date countdown will begin when the user enters the Canvas step.

{% alert tip %}
If you want anonymous users to see a Content Card in their very first session, use a campaign instead of a Canvas. This is because when an anonymous user enters a Canvas, their session has already started, so they won't get the Content Card until they start a new session.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
For both options, after a card is created, Braze does not recalculate audience eligibility or personalization.
{% endalert %}

### Differences between creating cards at launch or entry versus at first impression {#differences}

This section describes the main differences between card creation at campaign launch or step entry versus at first impression.

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
    <th class="tg-0pky">When campaign is launched / At Canvas step entry</th>
    <th class="tg-0pky">At first impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">When to use this</td>
    <td class="tg-0pky">If you need content to be snapshot at a specific time (the launch time).</td>
    <td class="tg-0pky"><ul><li>If you need to display cards to new or anonymous users who may enter the segment after launch (<a href="#campaign_note">campaigns only*</a>).</li><li>If you're using personalization and want the latest content to be available on the card.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze evaluates audience membership when the campaign sends.<br><br>New or anonymous users will not be evaluated for eligibility if they try to view the card after the campaign sends. For recurring campaigns, this will be at the next recurrence interval.</td>
    <td class="tg-0pky">Braze evaluates membership when the user next opens your app (starts a session, <a href="#campaign_note">campaigns only*</a>).<br><br> This setting will have a wider audience reach because any new or anonymous users will always be evaluated for eligibility when they try to view the card. <br><br>Additionally, rate limiting (limiting the number of people who will receive the card) is not applicable when set to at first impression.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalization</td>
    <td class="tg-0pky">Braze evaluates Liquid, Connected Content, and Content Blocks at the time the campaign is launched or when a user enters the Canvas step. For recurring campaigns, this will be at the next recurrence interval.</td>
    <td class="tg-0pky">Braze evaluates Liquid, Connected Content, and Content Blocks at the time of first impression or after the next recurrence interval.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytics</td>
    <td class="tg-0pky"><em>Messages Sent</em> refers to the number of cards created and available to be seen. This doesn't count whether the users viewed the card.</td>
    <td class="tg-0pky"><em>Messages Sent</em> refers to the number of cards sent to a user after a session start. In Canvas, users entering the step without starting a session will not have a card sent, which is why this metric may not align with the number of users entering a step.<br><br>While your reachable users and impressions will not change, you can expect to see a decrease in send volume (<em>Messages Sent</em>) when a card is created at first impression compared to if the same card was created at campaign launch or Canvas step entry.</td>
  </tr>
  <tr>
    <td class="leftHeader">Processing time</td>
    <td class="tg-0pky">Cards are created for every eligible user in the segment at the time of launch. For large audiences, we recommend to select <b>At First Impression</b>, as cards will be available more quickly after launch.</td>
    <td class="tg-0pky">Cards are created the first time a user tries to view the card, so it may take 1-2 seconds to display on the first impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* This scenario only applies to campaigns, as Canvas audience is evaluated at Canvas entry, not at the step level.</sup></p>

## Considerations

### Changing card creation after launch

Braze recommends not changing how cards are created after a campaign has launched. Due to the differences in how Messages Sent is calculated between the two card creation types, changing how cards are created after the campaign has launched can affect the accuracy of your send volume.

### Potential processing time

We recommend that campaigns with large audiences select the option to create cards at first impression, as cards will be available much more quickly after the campaign is launched. Campaigns which are triggered on session start may also want to consider moving to create card at first impression (available through scheduled delivery) to realize performance improvements.

When cards are created at first impression, it may take 1–2 seconds for the cards to process. The length of this processing time depends on various factors, such as the card size and the complexity of the message templating options. For example, the processing time for cards using Connected Content will be at least as long as the Connected Content response time.

### Previous SDK versions

If a user's app is running a previous version of the SDK, they will still receive Content Cards sent with a specified card creation. However, cards will take longer to appear to these users, and may not appear until the next Content Card sync.

