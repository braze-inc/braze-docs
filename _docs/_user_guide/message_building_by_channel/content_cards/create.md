---
nav_title: Create a Content Card
platform: Message_Building_and_Personalization
subplatform: Content Cards
page_order: 0
---

# Creating a Content Card

You can create a Content Card using the Braze platform using Campaigns. Content Cards will appear in a feed.

## Build Your Message

Click __Create Campaign__ to open a new messaging wizard for your Content Card. Then, follow the flow of the messaging wizard to quickly create and launch your Content Card.

![Create Your Content Card]({% image_buster /assets/img/create-cc.gif %})

1. Name your Campaign something clear and meaningful.
2. Add __Teams__ and __Tags__, as necessary.
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

## Step 1: Specify Your Message Types

Choose a __Platform__, __Message Type__, __Layout__, and __Enforced Device Orientation__ as necessary.

### Message Types

Learn more about the expected behavior and look of each of these messages on our [Creative Details page]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/), or by clicking on the linked message types in the tables.

These Content Card types are accepted by both mobile apps and web applications.

| Message Type | Type Description |
|---|---|---|
|[Classic]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| This Card has a simple layout with a bolded title, message text, and an optional image that sits to the left of the title and text. It is best to use a square image or icon with the Classic Card. |
|[Captioned Image]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| This Card allows you to showcase your content with copy and an attention-grabbing image! |
|[Banner]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)|  The Banner Card allows you to get creative and command attention with space for images, gifs, and other non-text based content. |

## Step 2: Compose a Content Card

The Compose tab allows you to edit all aspects of your message’s content and behavior.

![Compose Content Card][24]

The content of the Compose tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the liquid. |
|Image | Click __Add Image__ or use an image URL. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have it's own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Pinning | A pinned card will display at the top of a user’s feed and cannot be dismissed by the user. | If more than one card in a user’s feed is pinned, the pinned cards will display in chronological order. Once a card has been sent you can not update its pinned option retroactively. Changing this option after a campaign has been sent will only affect future sends. |
|Expiration | Set the specific expiration date or the days until a Card expires. | All variants have identical expiration dates. |
| On Click Behavior | For either Android, iOS, or Web: <br> __Redirect to Web URL__, __Deep Link into App__ or __None__. | When your customer clicks on a presented link in the Card, your link can either lead them deeper into your app or to another site. |
|Title & Message Text | We recommend clear and concise titles and message content. | Write anything you want. There are no limits, but the faster you can get your message across and get your customer clicking - the better! |

{% alert warning %}
The combined size of all fields in a Content Card message (header, image, and body message) should not exceed 2Kb in total.
{% endalert %}

{% alert note %}

Braze will store up to 100 non-expired Content Cards in their feed. The oldest card will be removed from the feed, even if unread, once more than 100 cards have entered the feed.

{% endalert %}

## Step 3: Configure Additional Settings

Add [key-value pairs][19] to your message, if needed.

You can use key-value pairs to create categories for your Cards, create multiple Content Card Feeds ([Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/), [Web]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/), iOS to come), and customize how Cards are sorted.

## Step 4: Build the Remainder of Your Campaign or Canvas

Build the remainder of your campaign or Canvas, see the sections below for further details on how to best utilize our tools to build in-app messages.

{% details Choose Delivery Schedule or Trigger %}

Content Cards can be delivered based on a scheduled time, an action, or based on an API trigger.

You can also set the campaign's duration and Quiet Hours in this step.

__Frequency Capping does not apply to Content Cards.__

{% enddetails %}

{% details Choose Target Segment %}

Next, you need to choose the target segment from the dropdown menu.

You'll automatically be given a snapshot of what that approximate segment population looks like right now.

Keep in mind that exact segment membership is always calculated just before the message is sent.

{% enddetails %}

{% details Choose Conversion Events %}

Braze allows you to track how often users perform specific actions (Conversion Events) after receiving a campaign.

You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% enddetails %}

<br>

After you've finished building the last of your campaign, review it's details, [test it]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/testing/), then send it!

## Things to Know

The following capabilities are not yet supported for Content Cards:

- Vouchers
- Frequency Capping
- Re-ordering Content Cards from the Braze UI
- Post-launch Edits

{% alert warning %}
Once a Content Card is launched, it cannot be edited. It can only stopped from sending to new users and removed from users' feeds.
{% endalert %}

[1]: {% image_buster /assets/img_archive/newcampaign.png %}
[2]: {% image_buster /assets/img/primary-secondary-buttons.png %}
[3]: {% image_buster /assets/img_archive/InAppNewComposer.png %}
[4]: {% image_buster /assets/img_archive/InAppNewComposer2.png %}
[10]: {% image_buster /assets/img_archive/intelligent_delivery.png %}
[11]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-iam
[13]: {% image_buster /assets/img_archive/InAppNewComposer3.png %}
[14]: {% image_buster /assets/img_archive/InAppNewComposer4.png %}
[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
[18]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[22]: {% image_buster /assets/img/compose_iam.gif %}
[22]: {% image_buster /assets/img/iam-generations.gif %}
[24]: {% image_buster /assets/img/compose-cc.gif %}
