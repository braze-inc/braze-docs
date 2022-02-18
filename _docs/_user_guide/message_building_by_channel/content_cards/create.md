---
nav_title: Creating a Content Card
article_title: Creating a Content Card
page_order: 0
description: "This reference article covers how to create, compose, configure and send Content Cards using Braze campaigns and Canvases."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards

---

# Creating a Content Card

> This article covers how to create a Content Card in Braze. Here, we'll cover choosing a messaging type, composing your card, and scheduling your message delivery.

You can create a Content Card using the Braze platform using campaigns and Canvases.

## Step 1: Choose where to build your message

Not sure whether your message should be send using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **Content Cards**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add **Teams** and **Tags** as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants.

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed. Steps containing Content Cards can be scheduled or action-based.
4. Filter your audience for this step, as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay, at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/). You can either **Advance when Message Sent**, which advances your users to the next steps when the Content Card is sent, or **Immediately Advance Audience**, which advances users when the Content Card is sent, or if the Content Card is aborted for any reason.
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Specify your message types

Next, select a **Card Type**. Braze provides three Content Card types out-of-the-box: Classic, Captioned Image, and Banner.

To learn more about the expected behavior and look of each of these message types, refer to [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), or check out the links in the following table. These Content Card types are accepted by both mobile apps and web applications.

| Message Type | Example | Description |
|---|---|---|
|[Classic]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Classic Content Card]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |The Classic Card has a simple layout with a bolded title, message text, and an optional image that sits to the left of the title and text. It's best to use a square image or icon with the Classic Card. |
|[Captioned Image]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Captioned Content Card]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | The Captioned Image Card allows you to showcase your content with copy and an attention-grabbing image. |
|[Banner]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Banner Content Card]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | The Banner Card allows you to get creative and command attention with space for images, GIFs, and other non-text based content. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Step 2: Compose a Content Card

You can edit all aspects of your message's content and behavior in the **Compose** tab of the message editor.

![Compose Content Card][24]

The content here varies based on the **Card Type** chosen in the previous step, but may include any of the following options:

#### Language

Click **Add Languages** and select your desired languages from the provided list. This will insert [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. See our [full list of available languages][18].

#### Title and message

Write anything you want. There are no limits, but the faster you can get your message across and get your customer clicking—the better! We recommend clear and concise titles and message content. These fields are not provided for Banner Cards.

#### Image

To add an image to your Content Card, click **Add Image** or provide an image URL. Clicking **Add Image** opens the **Media Library**, where you can select a previously uploaded image or add a new one. Each message type and platform may have its own suggested proportions and requirements—be sure to check what those are before commissioning or making an image from scratch! Content Card message fields are limited to 2KB in total size.

#### Pin to top

A pinned card will display at the top of a user's feed and can't be dismissed by the user. If more than one card in a user's feed is pinned, the pinned cards will display in chronological order. Once a card has been sent, you can not update its pinned option retroactively. Changing this option after a campaign has been sent will only affect future sends.

#### On-click behavior

When your customer clicks on a presented link in the card, your link can either lead them deeper into your app or to another site. If you choose an on-click behavior for your Content Card, remember to update your **Link Text** accordingly!

For Android, iOS, and Web, you can choose between:

* Redirect to Web URL
* [Deep Link into App]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)
* None

{% alert warning %}
Content Card message fields are limited to 2KB in total size, calculated by adding the byte-size length of the following fields: Title, Message, Image URL, Link Text, Link URL(s), and Key/Value Pairs (names + values). Messages that exceed this size will not be sent. Note that this does not include the size of the image but rather the length of the Image URL.
{% endalert %}

{% alert note %}
Each user is eligible to receive up to 100 non-expired and non-dismissed Content Cards. As a user becomes eligible for more than 100 cards, Braze will begin to remove older cards from their feed, even if they were unread.
{% endalert %}

## Step 3: Configure additional settings (optional)

You can use [key-value pairs][19] to create categories for your Cards, create multiple Content Card Feeds ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/), and customize how Cards are sorted.

To add key-value pairs to your message, switch to the **Settings** tab and click **Add New Pair**.

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign; see the sections below for further details on how to best utilize our tools to build Content Cards.

#### Choose delivery schedule or trigger

Content Cards can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

You can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) and determine the Content Card's expiration. Set a specific expiration date or the days until a Card expires, up to 30 days. All variants have identical expiration dates.

{% alert note %}
Frequency Capping does not apply to Content Cards.
{% endalert %}

#### Choose a target segment

Next, you need to choose the target segment from the dropdown menu. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas step. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 5: Test your card

After you've finished building the last of your campaign or Canvas, review its details, [test it]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/), then send it!

{% alert warning %}
After a Content Card is launched, it can't be edited. It can only be stopped from sending to new users and removed from users' feeds.
{% endalert %}

## Things to know

### Capabilities not yet supported

The following capabilities are not yet supported for Content Cards:

- Vouchers
- Frequency Capping
- Re-ordering Content Cards from the Braze UI
- Post-launch Edits


### Sending behavior

Once Content Cards have been sent, similar to emails, they sit waiting in an "inbox" ready to be delivered to the user. Once content is pulled into the Content Card (at time of displaying), the content cannot be changed during its lifespan. This applies even if you are calling an API through Connected Content, and the data from the endpoint changes; this data will not get updated. It can only be stopped from sending to new users and removed from users' feeds. If you modify a campaign, only future cards that are sent will have the update.

If you need to remove old cards, you must stop the campaign to do so. To stop a campaign, open your Content Card campaign and select **Stop Campaign**. Stopping the campaign will prompt you to decide how to handle users that have already received your card. If you would like to remove the Content Card from your users' feeds, select **Remove card from feed**. The card will then be hidden by the SDK on the next sync.

![Confirm Content Card deactivation dialog][25]{: style="max-width:75%" }

### Card removal events {#action-based-card-removal}

Some Content Cards are only relevant up until a user performs some action. For example, a card nudging users to activate their account shouldn't be shown once the user completes that onboarding task.

Within a campaign or Canvas Message, you can optionally add a __Removal Event__ to specify which custom events or purchases should cause previously sent cards to be removed from that user's feed; triggered via SDK or REST API.

{% alert tip %}
You can specify multiple custom events and purchases that should remove a card from a user's feed. Once **any** of those actions are performed by the user, any existing cards sent by the campaign's cards will be removed. Any future eligible cards will continue to be sent according to the message's schedule.
{% endalert %}

![Content Card Removal Event]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Updating already sent cards

If you find you need to make changes to cards that have already been sent:

1. Stop your campaign.
2. Remove active Content Cards from users' feeds.
3. Edit your campaign as needed.
4. Restart your campaign.

[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img/content_card_compose.png %}
[25]: {% image_buster /assets/img/cc_remove.png %}
