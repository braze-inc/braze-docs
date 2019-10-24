---
nav_title: Create an In-App Message
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 0
---

# Creating an In-App Message

You can create an in-app message using the Braze platform using Campaigns, Canvas, or as an API campaign. We highly recommend planning out your messages and preparing all materials ahead of time using our handy [In-App Message Prep Guide]({{ site.baseurl }}/help/best_practices/in-app_messages/prep_guide/).


## Choose Where to Build Your Message {#create-new-campaign-in-app}

{% tabs local %}
  {% tab Campaigns %}
  Click __Create Campaign__ to open a new messaging wizard for in-app message campaigns. Then, follow the flow of the messaging wizard to quickly create and launch your in-app message campaign.

  ![Platform Picker]({% image_buster /assets/img/iam_platforms.gif %})

1. Name your Campaign something clear and meaningful.
2. Add __Teams__ and __Tags__, as necessary.
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.

  {% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

 {% endtab %}
 {% tab Canvas %}
 After you have [created and set up your Canvas using the Canvas wizard]({{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/),

1. Name your step something clear and meaningful.
2. Add a Delay, as necessary.
3. Filter your Audience, as necessary.
4. Choose your advancement options, as necessary.
5. Choose all other messaging channels which you would like to pair with your message.

{% alert important %}
You cannot have multiple in-app message variants in a single step.
{% endalert %}

{% endtab %}
{% endtabs %}


## Step 1: Specify Your Message Types

Choose a __Platform__, __Message Type__, __Layout__, and __Enforced Device Orientation__ as necessary.

### Message Types

Click on your desired Platform tab to learn more about the Message Types, Layouts, and other options associated with it. Learn more about the expected behavior and look of each of these messages on our [Creative Details page]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creative_details/), or by clicking on the linked message types in the tables.

{% tabs local %}
{% tab In-App Message Options %}

These in-app messages are accepted by both mobile apps and web applications.

#### Message Options

| Message Type | Type Description | Available Layouts| Other Options |
|---|---|---|
|[Full-Screen]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen)| Messages that cover the entire screen with a message block. | __Image & Text__ and __Image Only__ | Enforced Device Orientation (Portrait or Landscape)|
|[Modal]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal)|  Messages that cover the entire screen with a screen overlay and a message block. | __Text (with Optional Image)__ and __Image Only__ | None |
|[Slideup]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup)|  Messages that slide into view in a designated place without blocking the rest of the screen. | None | None |

{% endtab %}
{% tab Advanced %}

These in-app messages are customizable to your needs.

#### Message Options

| Message Type | Type Description |Available Layouts| Other Options |
|---|---|---|
|[Custom Web Message]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-web-messages)| Custom messages that perform as defined in your custom code (HTML, CSS, and/or Javascript).  |None | None |
|[Email Capture Form]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form) | Typically used to capture the viewer's email.  | None | None |
|[Web Modal with CSS]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) | Modal messages for web with customizable CSS. | __Text (with Optional Image)__ and __Image Only__ | None |

{% alert important %}
If Braze detects that you don't have a close or dismissal button included in your code, we will request that you add one in. For your convenience, we have provided a snippet that you can copy and pasted into your code: `<a href="appboy://close">X</a>`.
{% endalert %}

{% endtab %}
{% endtabs %}


## Step 2: Compose In-App Message

The Compose tab allows you to edit all aspects of your message’s content and behavior.

![composeyouriam][24]


The content of the Compose tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the liquid. |
|Image | __Upload Image__, __Pick a Badge__, or use __Font Awesome__. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have its own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Button Text & On Click Behavior| Add up to two buttons. | You can create and edit custom button text and color. You can also add  Terms of Service Link within Web Email Capture forms.  |
|Device Options | Restrict send to only iOS devices. | Click __Change__ and check the box as desired. |
|Message Close Options | __Dismiss Automatically__ or __Wait for User Swipe or Touch__. | __Dismiss Automatically__ allows you to select how many seconds the message will remain on the scree. __Wait for User Swipe or Touch__ will require a dismissal or close option.  |
|Header & Body Text | Completely custom copy (often with custom HTML capabilities) with the options to include liquid and other types of personalization. | Some message types do not need and therefore do not ask for headers. |
|Position | __From Bottom of App Screen__ or __From Top of App Screen__. | This only exists in the Universal Slideup message builder.|
|HTML & Assets | Completely custom via upload, URL, or copy and paste. | Copy and paste HTML into the available space and upload your assets via ZIP. |
|Email Capture Input Placeholder | Custom copy. | This is used solely in the Web Email Capture Form and will direct your users to input the desired content into the space. |

### Buttons

When available for your message type, you can have up to two buttons appear below your body of text. By default, the button on the right (Button 2) is formatted to be more visually drawing to your user. We recommend using this button for singular or primary actions.

![Primary_Secondary][2]{: height="40%" width="40%"}

If you choose to only use one button, it will automatically adjust to take over the available space at the bottom of your message, instead of leaving room for an additional button.

{% alert tip %}
  If you decide to format these buttons with your own colors, we recommend that you use Button 2 for your more preferred result. In other words, if you want your user to click on one button more than the other, make sure it is on the right. The right button has often displayed better potential to get clicked, especially if it has a somewhat contrasting or otherwise stand-out color from the rest of the message. This is only emphasized when the button on the left blends more visually with the message.
{% endalert %}

### Generations

Braze has three Generations of in-app messages available. You can fine-tune to which devices your messages should be sent, based on which Generation they support, in the [Preview]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) section which composing your in-app message.

![In-App_Messages_Generations][22]{: height="50%" width="50%"}

## Step 3: Style Your In-App Message

The Style tab allows you to adjust all visual aspects of your message. Upload an image or badge, or pick a pre-designed badge icon. Change the colors of the header and body text, buttons and background by selecting from a palette or entering a hex, RGB or HSB code.

The content of the Style tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Formatting | Input | Description |
|---|---|---|
|Color Profile | Apply from In-App Message Templates Gallery. | Click __Apply Template__ and select from gallery. Then, click __Save__. |
|Text Alignment | Left, Center, or Right.  | Only available for newer Braze SDK versions. |
|Header | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color.  |
|Text | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
|Buttons | HEX color code. | Your desired HEX colors will display. You will also be able to choose the opacity of the colors. You can choose colors for: the message's Close Button Background as well as each button's Background, Text, and Border. |
| Button Border | HEX color code. | New! This will allow you to set your primary and secondary buttons apart from one another. We suggest outlining buttons with contrasting colors. |
|Background Color | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. This is the background of the entire message and will clearly display behind your text body. |
|Screen Overlay | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. Only available for newer Braze SDK versions. This is the frame around the entire message. |
|Chevron or other Close Message Option | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |

Always [preview and test]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) your message before sending.

{% alert important %}
Some in-app message types do not have the option for styling beyond uploading custom HTML (and/or CSS and/or Javascript) and assets via ZIP, as described in the steps above. [Web Modal with CSS]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) allows you to upload or write custom CSS to create beautiful, all around custom-styled messaging.
{% endalert %}

## Step 4: Configure Additional Settings

Add [key-value pairs][19] to your message if needed.

## Step 5: Build the Remainder of Your Campaign or Canvas

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

Please refer to our developer documentation for [server-side event triggering]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-message-delivery) and [local in-app message delivery]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#local-in-app-messages).

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

After you've finished building the last of your campaign or Canvas, review its details, then send it!

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
