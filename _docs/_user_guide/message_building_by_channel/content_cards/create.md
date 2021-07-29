---
nav_title: Create a Content Card
platform: Message_Building_and_Personalization
subplatform: Content Cards
page_order: 0
description: "This reference article covers how to create, compose, configure and send Content Cards using Braze campaigns and Canvases."

tool:
  - Dashboard
  - Canvas
  - Campaigns

channel:
  - content cards

---

# Creating a Content Card

You can create a Content Card using the Braze platform using campaigns and Canvases.

## Content Card Creation in Campaigns and Canvases
{% tabs %}
{% tab Campaign %}
__Build Your Message__

Navigate to the Campaign section of the Dashboard and click __Create Campaign__ to open a new messaging wizard for your Content Card. Then, follow the flow of the messaging wizard to quickly create and launch your Content Card.

![Create Your Content Card]({% image_buster /assets/img/create-cc.gif %})

1. Name your campaign something clear and meaningful.<br><br>
2. Add __Teams__ and __Tags__, as necessary.<br><br>
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}
__Setup Your Canvas__

Navigate to the Canvas Section of the Dashboard and click __Create Canvas__ to open the Canvas Wizard to begin setting up your Canvas. Then, follow the flow of the Canvas wizard to quickly create and launch your Content Card.

1. __Name your Canvas__ something clear and meaningful.<br><br>
2. __Add Teams and Tags__, as necessary.<br><br>
3. __Define your conversion events__ - Canvas supports up to 4 conversion events. These events must be assigned during Canvas creation and cannot be changed once a Canvas has launched.<br><br>
4. __Set up your Entry Schedule__ - Canvas offers Scheduled, Action-Based and API-Triggered entry. <br><br>
5. __Select your Entry Audience__ - Here, you can determine who will enter this Canvas and target users by segments and filters; these conditions will not be re-evaluated at each step. Within this dialogue, you also have the option to select Entry Controls, such as allowing users to re-enter this Canvas and set an entry limit. You'll also automatically be given a snapshot of what that approximate target population looks like right now.<br><br>
6. __Set your Send Settings__ - Here, you can set messages sending options for all steps within Canvas. Some of these options include setting subscription settings, adjusting the rate limit, toggle frequency capping, and more.<br><br>
7. __Add a Step in the Canvas Builder__ - Within this step, click Messages and then select the Content Card Messaging Channel. Here you will create and configure your Content Card.<br>![Create Your Content Card]({% image_buster /assets/img/content_card.gif %}){: style="max-width:90%"}

For more in-depth details on setting up and configuring your Canvas, check out our [Canvas documentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/). 

{% endtab %}
{% endtabs %}

## Step 1: Specify Your Message Types

### Message Types

Learn more about the expected behavior and look of each of these messages on our [Creative Details page]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), or by clicking on the linked message types in the tables.

These Content Card types are accepted by both mobile apps and web applications.

| Message Type | Type Description |
|---|---|---|
|[Classic]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| This Card has a simple layout with a bolded title, message text, and an optional image that sits to the left of the title and text. It is best to use a square image or icon with the Classic Card. |
|[Captioned Image]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| This Card allows you to showcase your content with copy and an attention-grabbing image! |
|[Banner]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)|  The Banner Card allows you to get creative and command attention with space for images, gifs, and other non-text based content. |
{: .reset-td-br-1 .reset-td-br-2}

## Step 2: Compose a Content Card

The Compose tab in the Campaign Wizard (located in the step wizard in Canvas) allows you to edit all aspects of your message's content and behavior.

![Compose Content Card][24]

The content here varies based on the Message Type chosen in the last step but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert Liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. |
|Image | Click __Add Image__ or use an image URL. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have its own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! <br> <br> Content Card message fields are limited to 2kb in total size, as noted in the section below. |
|Pinning | A pinned card will display at the top of a user's feed and cannot be dismissed by the user. | If more than one card in a user's feed is pinned, the pinned cards will display in chronological order. Once a card has been sent, you can not update its pinned option retroactively. Changing this option after a campaign has been sent will only affect future sends. |
|Expiration | Set the specific expiration date or the days until a Card expires. | Currently, Braze supports a maximum expiration time of __30 days__. <br> <br> All variants have identical expiration dates. |
| On Click Behavior | For either Android, iOS, or Web: <br> __Redirect to Web URL__, __Deep Link into App__ or __None__. | When your customer clicks on a presented link in the card, your link can either lead them deeper into your app or to another site. |
|Title & Message Text | We recommend clear and concise titles and message content. | Write anything you want. There are no limits, but the faster you can get your message across and get your customer clicking - the better! |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert warning %}
Content Card message fields are limited to 2kb in total size, calculated by adding the byte-size length of the following fields: Title, Message, Image URL, Link Text, Link URL(s), and Key/Value Pairs (names + values). Messages that exceed this size will not be sent. Note that this does not include the size of the image but rather the length of the Image URL.
{% endalert %}

{% alert note %}

Each user is eligible to receive up to 100 non-expired and non-dismissed Content Cards. As a user becomes eligible for more than 100 cards, Braze will begin to remove older cards from their feed, even if they were unread.

{% endalert %}

## Step 3: Configure Additional Settings

Add [key-value pairs][19] to your message, if needed.

You can use key-value pairs to create categories for your Cards, create multiple Content Card Feeds ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/), and customize how Cards are sorted.

## Step 4: Build the Remainder of Your Campaign or Canvas.

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign; see the sections below for further details on how to best utilize our tools to build Content Cards.

#### Choose Delivery Schedule or Trigger
- Content Cards can be delivered based on a scheduled time, an action, or based on an API trigger.
- You can also set the campaign's duration and Quiet Hours in this step.
- __Frequency Capping does not apply to Content Cards.__

#### Choose Target Segment
- Next, you need to choose the target segment from the dropdown menu.
- You'll automatically be given a snapshot of what that approximate segment population looks like right now.
- Keep in mind that exact segment membership is always calculated just before the message is sent.

#### Choose Conversion Events
- Braze allows you to track how often users perform specific actions (i.e., conversion events) after receiving a campaign.
- You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

After you've finished building the last of your campaign, review its details, [test it]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/), then send it!

{% alert warning %}
Once a Content Card is launched, it cannot be edited. It can only be stopped from sending to new users and removed from users' feeds.
{% endalert %}

{% endtab %}

{% tab Canvas %}

Complete the remaining sections of your Canvas step; see the sections below for further details on how to best utilize our tools to build Content Cards. After you have created and configured your step, check out our [Canvas Documentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) for further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent selection, and more.

#### Choose Step Schedule
- Content Cards can be delivered based on a scheduled time or Action in Canvas

#### Choose Audience
- Next, you need to adjust Audience Options for this step. Here, you can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay, at the time messages are sent.

#### Choose Advancement Behavior
- Lastly, select your Advancement behavior for this step. Here you can choose to either "Advance when Message Sent" that advances your users to the next steps when the Content Card is sent, or "Immediately Advance Audience" that advances users when either the Content Card is sent, or the Content Card was not sent because it got aborted. 
- To read more about Canvas Advancement Behavior, check out of [Canvas Documentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/?redirected=true).

After you've finished building out your Canvas Step, review its details and [test it]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/)!

{% endtab %}
{% endtabs %}

## Things to Know

### Capabilities Not Yet Supported
The following capabilities are not yet supported for Content Cards:
- Vouchers
- Frequency Capping
- Re-ordering Content Cards from the Braze UI
- Post-launch Edits


### Sending Behavior

Once Content Cards have been sent, similar to emails, they sit waiting in an "inbox" ready to be delivered to the user. Once content is pulled into the Content Card (at time of displaying), the content cannot be changed during its lifespan. This applies even if you are calling an API through Connected Content, and the data from the endpoint changes; this data will not get updated. It can only be stopped from sending to new users and removed from users' feeds. If you modify a campaign, only __future__ cards that are sent will have the update. 

If you need to remove old cards, you must stop the campaign to do so. This can be done by navigating to your Content Card campaign and selecting `Stop Campaign`. Stopping the campaign brings up the prompt shown below. If you would like to remove Content Cards, check the box to remove any cards that have been sent. This will cause the card to be hidden by the SDK on the next sync. 

![Content Card][25]

### Card Removal Events {#action-based-card-removal}

Some Content Cards are only relevant up until a user performs some action. For example, a card nudging users to activate their account shouldn't be shown once the user completes that onboarding task.

Within a campaign or Canvas Message, you can optionally add a __Removal Event__ to specify which custom events or purchases should cause previously sent cards to be removed from that user's feed; triggered via SDK or REST API.

{% alert tip %}
You can specify multiple custom events and purchases that should remove a card from a user's feed. Once **any** of those actions are performed by the user, any existing cards sent by the campaign's cards will be removed. Any future eligible cards will continue to be sent according to the message's schedule.
{% endalert %}

![Content Card Removal Event]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Updating Already Sent Cards

If you find you need to make changes to cards that have already been sent:

1. Stop your campaign
2. Remove active Content Cards from users' feeds
3. Edit your campaign as needed
4. Restart your campaign

[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img/compose-cc.gif %}
[25]: {% image_buster /assets/img/cc_remove.png %}
