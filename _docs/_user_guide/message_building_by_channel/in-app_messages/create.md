---
nav_title: Create an In-App Message
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 0
description: "You can create an in-app message using the Braze platform using Campaigns, Canvas, or as an API campaign."
---

# Creating an In-App Message

You can create an in-app message using the Braze platform using Campaigns, Canvas, or as an API campaign. We highly recommend planning out your messages and preparing all materials ahead of time using our handy [In-App Message Prep Guide]({{site.baseurl}}/help/best_practices/in-app_messages/prep_guide/).


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
 After you have [created and set up your Canvas using the Canvas wizard]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/),

1. Name your step something clear and meaningful.
2. Add a Delay, as necessary. Note that steps containing in-app messages cannot be action based.
3. Filter your Audience, as necessary.
4. Choose your advancement options, as necessary.
5. Choose all other messaging channels which you would like to pair with your message.

{% alert important %}
You cannot have multiple in-app message variants in a single step.
{% endalert %}

{% endtab %}
{% endtabs %}


## Step 1: Specify Delivery Platform(s)
Start by choosing which platform(s) should receive the message. Use this selection to limit the delivery of a campaign to a specific set of apps. You might choose __Web Browsers__ for a campaign encouraging users to download your mobile app to ensure they do not receive the message after already getting your app. Because Platform selections are specific to each variant, you could try testing message engagement per platform!

Web Email Capture and Web Modal with CSS are both unique to the Web SDK, and can only be used after selecting __Web Browsers__.

| Platform | Message Delivery |
|---|---|
| Mobile Apps | iOS & Android SDKs|
| Web Browsers | Web SDK|
| Both Mobile Apps & Web Browsers | iOS, Android & Web SDKs|
{: .reset-td-br-1 .reset-td-br-2}


## Step 2: Specify Your Message Types

Choose a __Message Type__, __Layout__, and __Enforced Device Orientation__ as necessary.

### Message Types

Once you've selected a sending platform, browse the Message Types, Layouts, and other options associated with it. Learn more about the expected behavior and look of each of these messages on our [Creative Details page]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), or by clicking on the linked message types in the tables.

{% tabs local %}
{% tab In-App Message Options %}

These in-app messages are accepted by both mobile apps and web applications.

#### Message Options

| Message Type | Type Description | Available Layouts| Other Options |
|---|---|---|
|[Full-Screen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen)| Messages that cover the entire screen with a message block. | __Image & Text__ and __Image Only__ | Enforced Device Orientation (Portrait or Landscape)|
|[Modal]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal)|  Messages that cover the entire screen with a screen overlay and a message block. | __Text (with Optional Image)__ and __Image Only__ | None |
|[Slideup]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup)|  Messages that slide into view in a designated place without blocking the rest of the screen. | None | None |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Advanced %}

These in-app messages are customizable to your needs.

#### Message Options

| Message Type | Type Description |Available Layouts| Other Options |
|---|---|---|
|[Custom Web Message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-web-messages)| Custom messages that perform as defined in your custom code (HTML, CSS, and/or JavaScript).  |None | Must set `enableHtmlInAppMessages` initialization option to `true` for your In-App Message to work. |
|[Email Capture Form]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form) | Typically used to capture the viewer's email.  | None | Must set `enableHtmlInAppMessages` initialization option to `true` for your IAM to work. |
|[Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) | Modal messages for web with customizable CSS. | __Text (with Optional Image)__ and __Image Only__ | None |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
If Braze detects that you don't have a close or dismissal button included in your code, we will request that you add one in. For your convenience, we have provided a snippet that you can copy and paste into your code: `<a href="appboy://close">X</a>`.
{% endalert %}

{% endtab %}
{% endtabs %}


## Step 3: Compose In-App Message

The Compose tab allows you to edit all aspects of your message’s content and behavior.

![composeyouriam][24]


The content of the Compose tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert Liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. |
|Image | __Upload Image__, __Pick a Badge__, or use __Font Awesome__. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have its own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Button Text & On Click Behavior| Add up to two buttons. | You can create and edit custom button text and color. You can also add  Terms of Service Link within Web Email Capture forms.  |
|Device Options | Restrict send to only iOS devices. | Click __Change__ and check the box as desired. |
|Message Close Options | __Dismiss Automatically__ or __Wait for User Swipe or Touch__. | __Dismiss Automatically__ allows you to select how many seconds the message will remain on the screen. __Wait for User Swipe or Touch__ will require a dismissal or close option.  |
|Header & Body Text | Completely custom copy (often with custom HTML capabilities) with the options to include Liquid and other types of personalization. | Some message types do not need and therefore do not ask for headers. |
|Position | __From Bottom of App Screen__ or __From Top of App Screen__. | This only exists in the Universal Slideup message builder.|
|HTML & Assets | Completely custom via upload, URL, or copy and paste. | Copy and paste HTML into the available space and upload your assets via ZIP. |
|Email Capture Input Placeholder | Custom copy. | This is used solely in the Web Email Capture Form and will direct your users to input the desired content into the space. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Buttons

When available for your message type, you can have up to two buttons appear below your body of text. By default, the button on the right (Button 2) is formatted to be more visually drawing to your user. We recommend using this button for singular or primary actions.

![Primary_Secondary][2]{: height="40%" width="40%"}

If you choose to only use one button, it will automatically adjust to take over the available space at the bottom of your message, instead of leaving room for an additional button.

{% alert tip %}
  If you decide to format these buttons with your own colors, we recommend that you use Button 2 for your more preferred result. In other words, if you want your user to click on one button more than the other, make sure it is on the right. The right button has often displayed better potential to get clicked, especially if it has a somewhat contrasting or otherwise stand-out color from the rest of the message. This is only emphasized when the button on the left blends more visually with the message.
{% endalert %}

### Generations

Braze has three Generations of in-app messages available. You can fine-tune to which devices your messages should be sent, based on which Generation they support, in the [Preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) section which composing your in-app message.

![In-App_Messages_Generations][22]{: style="max-width:50%"}

Depending on what SDK Versions your users are on, you may or may not see this option. You are only asked to select a generation when you have users on more than one generation. A Generation is defined as a collection of SDK Versions that contain a large number of major upgrades. For example, Generation 3 is the latest one that encompasses the latest style updates. 

By checking __Send to all Generations that support this message__, Braze will deliver to users that can receive any form of the message. For example, if you have users on all three Generations, a modal will deliver to users on Generations 2 and 3, as Generation 1 doesn't support modals. The message will look different for your two groups of users: Generation 3 users will receive the message in the latest styles, while Generation 2 users will see the older styles (cosmetic differences, and absence of button border).

You could uncheck the __Send to all Generations that support this message__ and select __Send only to users on Generation 3 (the latest)__ if you do not want to allow users to receive the older message styles. Users on Generation 3 will be the only ones to receive the message.


## Step 4: Style Your In-App Message

The Style tab allows you to adjust all visual aspects of your message. Upload an image or badge, or pick a pre-designed badge icon. Change the colors of the header and body text, buttons and background by selecting from a palette or entering a hex, RGB or HSB code.

The content of the Style tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Formatting | Input | Description |
|---|---|---|
|Color Profile | Apply from In-App Message Templates Gallery. | Click __Apply Template__ and select from the gallery. Then, click __Save__. |
|Text Alignment | Left, Center, or Right.  | Only available for newer Braze SDK versions. |
|Header | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color.  |
|Text | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
|Buttons | HEX color code. | Your desired HEX colors will display. You will also be able to choose the opacity of the colors. You can choose colors for: the message's Close Button Background as well as each button's Background, Text, and Border. |
| Button Border | HEX color code. | New! This will allow you to set your primary and secondary buttons apart from one another. We suggest outlining buttons with contrasting colors. |
|Background Color | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. This is the background of the entire message and will clearly display behind your text body. |
|Screen Overlay | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. Only available for newer Braze SDK versions. This is the frame around the entire message. |
|Chevron or other Close Message Option | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Always [preview and test]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) your message before sending.

{% alert important %}
Some in-app message types do not have the option for styling beyond uploading custom HTML (and/or CSS and/or JavaScript) and assets via ZIP, as described in the steps above. [Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) allows you to upload or write custom CSS to create beautiful, all around custom-styled messaging.
{% endalert %}

## Step 5: Configure Additional Settings

### Key Value Pairs

Add [key value pairs][19] to send extra custom fields to user devices. 

### Re-evaluate Campaign Eligibility and Liquid

In some scenarios, you may want to re-evaluate a user's eligibility as they trigger an in-app message to display. Examples include campaigns that target a custom attribute that frequently changes, or messages that should reflect any last-minute profile changes.

![Re-evaluate IAM Membership][27]

When you enable this "Re-evaluate Campaign Eligibility" option, an additional request to Braze will be made to confirm that the user is still eligible for this message. Additionally, any [Liquid][25] variables or [Connected Content][26] will be templated at that moment before the message is displayed.

{% alert note %}
Enabling this option will result in a slight delay (< 100ms) between when a user triggers an in-app message and when the message is displayed due to the added eligibility and templating request.

Do not use this option for messages that can be triggered while a user is offline, or when eligibility and Liquid re-evaluation are not required.
{% endalert %}

## Step 6: Build the Remainder of Your Campaign or Canvas

Build the remainder of your campaign or Canvas, see the sections below for further details on how to best utilize our tools to build in-app messages. For more information on Canvas specific in-app messaging options like expiry and steps, [check out our documentation][16]. 

{% tabs %}
{% tab Triggering %}

### Triggering 

{% alert important %}
Please note that if you intend to trigger your in-app message based off a custom event, that custom event __must be sent via the SDK__.
{% endalert %}

![Schedule]({% image_buster /assets/img_archive/in-app-schedule.png %}){: style="max-width:70%"}

In-app message delivery is entirely based off of of the following action triggers:
- Making a purchase
- Opening the app/webpage
- Performing a custom event (only works with events sent via the SDK)
- Opening a specific push message
- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

A start date and time must be selected, however, an end date is optional. An end date will stop that specific in-app message from showing up on devices after the specified date/time.

Please refer to our developer documentation for [server-side event triggering]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-message-delivery) and [local in-app message delivery]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#local-in-app-messages).

#### Online vs. Offline Triggering

In-app messages's work by sending the message and triggers to the user's device. Once the in-app messages are on a device it waits to display until the trigger condition is met. __If the in-app messages are already cached on the user's device, you can even trigger in-app messages offline with no connection to Braze__ (for example, in Airplane mode). When you stop a campaign, the trigger condition is set to null and updated on the user's next session. For a user's current session, they may still see the in-app messages until the triggers are updated on their next session. 

{% endtab %}
{% tab Prioritize %}

### Prioritize

#### Campaigns
Finally, once you've selected the action the in-app message will be triggered off of, you should also set a priority. If two messages are triggered off of the same action, high priority messages will be scheduled to appear on users' devices before messages with lower priorities.

![Event Prioritization]({% image_buster /assets/img_archive/prioritization_options.png %}){: style="max-width:80%"}

The high, medium and low options for triggered message priorities are buckets, and as such multiple messages could have the same selected priority. To set priorities within these buckets, click __Set Exact Priority__ and you will be able to drag and drop campaigns to order them with the correct priority.

![Bucket Prioritization]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Canvas
A customer may trigger two in-app messages within your Canvas at the same time. When this occurs, Braze will follow the priority order below to determine which in-app message is displayed. Drag different Canvas steps to re-order their priority. By default, steps earlier in a Canvas variant will display before later steps.

![step_priority]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:70%"}

Navigate to the “send settings” of the canvas section to prioritize in-app messages from a canvas against in-app messages from other canvases and campaigns.

By default, canvas step priority is set to medium with the most recently created steps having the highest relative priority. Canvas/campaign level priorities also default to medium with the highest relative priority defaulting to the most recently created items.

![canvas_priority]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:70%"}

{% endtab %}
{% tab Target Segment %}

### Target Segment

Next, you need to choose the target segment from the dropdown menu. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

![Target Page]({% image_buster /assets/img_archive/target_page.png %}){: style="max-width:50%"}

{% endtab %}
{% tab Conversion Events %}

### Conversion Events
Braze allows you to track how often users perform specific actions (Conversion Events) after receiving a campaign. You can specify any of the following actions as a "Conversion Event":

- Opens App
- Makes Purchase
  - This can be a generic purchase or a specific item
- Performs specific custom event

You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

![Conversion Event]({% image_buster /assets/img_archive/conversion_event_selection.png %}){: style="max-width:50%"}

{% endtab %}
{% endtabs %}

After you've finished building the last of your campaign or Canvas, review its details, then send it!

## Active In-App Message Campaign Limits

Braze values reliability and speed. Just like we suggest you send only the data you need to Braze, we also recommend __turning off__ any campaigns that are no longer adding any value to your brand.

Processing action-based in-app message campaigns that are still in an active state but no longer sending messages or are no longer needed slows down the overall performance of the Braze services for you and other customers.

This extra time needed to process these large numbers of idle campaigns means that any in-app messages will take longer to appear on the end-users’ devices, which impacts the end user’s experience.

__We have implemented a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts.__

The 200 count includes active IAM campaigns that have not yet reached end time and those that have no end time. Active IAM campaigns that have passed their end times will not be counted.

The average Braze customer has a total of 26 campaigns active at once - so it is unlikely that this limitation will impact you. 

[2]: {% image_buster /assets/img/primary-secondary-buttons.png %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[22]: {% image_buster /assets/img/iam-generations.gif %}
[24]: {% image_buster /assets/img/iam_compose.gif %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
