---
nav_title: Create a Content Card
platform: Message_Building_and_Personalization
subplatform: Content Cards
page_order: 1
---

# Creating a Content Card

You can create a Content Card using the Braze platform using Campaigns.

## Choose Where to Build Your Message

  Click __Create Campaign__ to open a new messaging wizard for your Content Card. Then, follow the flow of the messaging wizard to quickly create and launch your Content Card.

![Create Your Content Card]({% image_buster /assets/img/create_cc.gif %}){: height="70%" width="70%"}

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

Click on your desired Platform tab to learn more about the Message Types, Layouts, and other options associated with it. Learn more about the expected behavior and look of each of these messages on our [Creative Details page]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/), or by clicking on the linked message types in the tables.

These Content Card types are accepted by both mobile apps and web applications.

#### Message Options

| Message Type | Type Description |
|---|---|---|
|[Classic]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| This Card has a simple layout with a bolded title, message text, and an optional Image that sits to the left of the title and text. It is best to use a square image or icon with the Classic Card. |
|[Captioned Image]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned_image)| This Card  |
|[Banner]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)|  Messages that slide into view in a designated place without blocking the rest of the screen. |

## Step 2: Compose a Content Card

The Compose tab allows you to edit all aspects of your message’s content and behavior.

![composeyouriam][24]

The content of the Compose tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the liquid. |
|Image | __Upload Image__ or use __Font Awesome__. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have it's own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Pinning | Check pin a card, which will display at the top of a user’s feed and cannot be dismissed by the user. | If more than one card in a user’s feed is pinned, the pinned cards will display in chronological order. Cards cannot be retroactively pinned or unpinned - you must select the pin option you’d like to use before they are sent to users.  |
|Expiration | Set the specific expiration date or the days until a Card expires. | All variants have identical expiration dates. |
| On Click Behavior | For either Android, iOS, or Web: <br> __Redirect to Web URL__, __Deep Link into App__ or __None__. | When your customer clicks on a presented link in the Card, your link can either lead them deeper into your app or to another site. |
|Title & Message Text | We recommend clear and concise titles and message content. | Write anything you want. There are no limits, but the faster you can get your message across and get your customer clicking - the better! |

## Step 3: Configure Additional Settings

Add [key-value pairs][19] to your message if needed.

## Step 4: Build the Remainder of Your Campaign or Canvas

Build the remainder of your campaign or Canvas, see the sections below for further details on how to best utilize our tools to build in-app messages.

{% details Triggering %}
![Schedule]({% image_buster /assets/img_archive/in-app-schedule.png %}){: height="50%" width="50%"}

In-app message delivery is entirely based off of of the following action triggers:

- Making a purchase
- Opening the app/webpage
- Performing a custom event (only works with events sent via the SDK)
- Opening a specific push message
- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

A start date and time must be selected, however, an end date is optional. An end date will stop that specific in-app message from showing up on devices after the specified date/time.

__Frequency Capping does not apply to Content Cards.__

{% enddetails %}

{% details Prioritize %}

__Campaigns__
Finally, once you've selected the action the in-app message will be triggered off of, you should also set a priority. If two messages are triggered off of the same action, high priority messages will be scheduled to appear on users' devices before messages with lower priorities.

![Event Prioritization]({% image_buster /assets/img_archive/prioritization_options.png %}){: height="50%" width="50%"}

The high, medium, and low options for triggered message priorities are buckets, and as such multiple messages could have the same selected priority. To set priorities within these buckets, click __Set Exact Priority__ and you will be able to drag and drop campaigns to order them with the correct priority.

![Bucket Prioritization]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: height="50%" width="50%"}

__Canvas__

It is possible that a customer will trigger two in-app messages within your Canvas at the same time. When this occurs, Braze will follow the priority order below to determine which in-app message is displayed. Drag different Canvas steps to re-order their priority. By default, steps earlier in a Canvas variant will display before later steps.

![step_priority]({% image_buster /assets/img_archive/step_priority.png %}){: height="50%" width="50%"}

Navigate to the “send settings” of the canvas section to prioritize in-app messages from a canvas against in-app messages from other canvases and campaigns.

By default, canvas step priority is set to medium with the most recently created steps having the highest relative priority. Canvas/campaign level priorities also default to medium with the highest relative priority defaulting to the most recently created items.

![canvas_priority]({% image_buster /assets/img_archive/canvas_priority.png %}){: height="50%" width="50%"}

{% enddetails %}

{% details Choose Target Segment %}

Next, you need to choose the target segment from the dropdown menu. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

![Target Page]({% image_buster /assets/img_archive/target_page.png %}){: height="50%" width="50%"}

{% enddetails %}

{% details Choose Conversion Events %}

Braze allows you to track how often users perform specific actions (Conversion Events) after receiving a campaign. You can specify any of the following actions as a "Conversion Event":

- Opens App
- Makes Purchase
  - This can be a generic purchase or a specific item
- Performs specific custom event

You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

![Conversion Event]({% image_buster /assets/img_archive/conversion_event_selection.png %}){: height="50%" width="50%"}

{% enddetails %}

<br>

After you've finished building the last of your campaign or Canvas, review it's details, then send it!

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
[24]: {% image_buster /assets/img/iam_compose.gif %}
