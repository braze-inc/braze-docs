---
nav_title: Creating an In-App Message
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 1
---
# Creating an In-App Message

In-App Messages help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

To see examples of in-app messages, check out our [Client Integration Gallery][11].

## Step 1: Create New Campaign {#create-new-campaign-in-app}

Click __Create Campaign__ to open a new messaging wizard for in-app message campaigns. Then, follow the flow of the messaging wizard to quickly create and launch your in-app message campaign.

![createyouriam][21]


1. Name your campaign something clear and meaningful.
2. Add __Teams__ and __Tags__, as necessary.
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.
  - _If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown._
4. Choose a __Platform__, __Message Type__, __Layout__, and __Enforced Device Orientation__ as necessary.

### Variant Options by Platform

Click on your desired Platform tab to learn more about the Message Types, Layouts, and other options associated with it.

{% tabs local %}
{% tab Universal %}

Universal In-App Messages are accepted by both mobile apps and web applications.

#### Message Options

| Message Type | Type Description | Available Layouts| Other Options |
|---|---|---|
|Full-Screen| Messages that cover the entire screen with a message block. | __Image & Text__ and __Image Only__ | Enforced Device Orientation (Portrait or Landscape)|
|Modal|  Messages that cover the entire screen with a screen overlay and a message block. | __Text (with Optional Image)__ and __Image Only__ | None |
|Slideup |  Messages that slide into view in a designated place without blocking the rest of the screen. | None | None |

{% endtab %}
{% tab Mobile App %}

Mobile App In-App Messages are only accepted by mobile apps.

#### Message Options

| Message Type | Type Description |Available Layouts| Other Options |
|---|---|---|
|Custom HTML| Custom messages that perform as defined in your custom code (HTML, CSS, and/or Javascript).  |None | None |

{% alert important %}
If Braze detects that you don't have a close or dismissal button included in your code, we will request that you add one in. For your convenience, we have provided a snippet that you can copy and pasted into your code: `<a href="appboy://close">X</a>`.
{% endalert %}

{% endtab %}
{% tab Web %}

Web In-App Messages are only accepted by websites and applications.

#### Message Options

| Message Type | Type Description | Available Layouts| Other Options |
|---|---|---|
|Email Capture Form | Typically used to capture the viewer's email.  | None | None |
|Custom Web Message | Custom messages that perform as defined in your custom code (HTML, CSS, and/or Javascript). | None | None |
|Web Modal with CSS | Modal messages for web with customizable CSS. | __Text (with Optional Image)__ and __Image Only__ | None |

{% endtab %}
{% endtabs %}


## Step 2: Compose In-App Message

The Compose tab allows you to edit all aspects of your message’s content and behavior.

![composeyouriam][22]


The content of the Compose tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Lanaguages__ and select your desired languages from the provided list. This will insert liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the liquid. |
|Image | __Upload Image__, __Pick a Badge__, or use __Font Awesome__. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have it's own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Button Text & On Click Behavior| Add up to two buttons. | You can create and edit custom button text and color. You can also add  Terms of Service Link within Web Email Capture forms.  |
|Device Options | Restrict send to only iOS devices. | Click __Change__ and check the box as desired. |
|Message Close Options | __Dismiss Automatically__ or __Wait for User Swipe or Touch__. | __Dismiss Automatically__ allows you to select how many seconds the message will remain on the scree. __Wait for User Swipe or Touch__ will require a dismissal or close option.  |
|Header & Body Text | Completely custom copy (often with custom HTML capabilities) with the options to include liquid and other types of personalization. | Some message types do not need and therefore do not ask for headers. |
|Position | __From Bottom of App Screen__ or __From Top of App Screen__. | This only exists in the Universal Slideup message builder.|
|HTML & Assets | Completely custom via upload, URL, or copy and paste. | Copy and paste HTML into the available space and upload your assets via ZIP. |
|Email Capture Input Placeholder | Custom copy. | This is used solely in the Web Email Capture Form and will direct your users to input the desired content into the space. |

### Buttons

When available for your message type, you can have up to two buttons appear below your body of text. By default, the button on the right (Button 2) is formatted to be more visually drawing to your user. We recommend using this button for singular or primary actions.

If you choose to only use one button, it will automatically adjust to take over the available space at the bottom of your message, instead of leaving room for an additional button.

{% alert tip %}
  If you decide to format these buttons with your own colors, we recommend that you use Button 2 for your more preferred result. In other words, if you want your user to click on one button more than the other, make sure it is on the right. The right button has often displayed better potential to get clicked, especially if it has a somewhat contrasting or otherwise stand-out color from the rest of the message. This is only emphasized when the button on the left blends more visually with the message.
{% endalert %}

## Step 3: Design In-App Message

The Style tab allows you to adjust all visual aspects of your message. Upload an image or badge, or pick a pre-designed badge icon. Change the colors of the header and body text, buttons and background by selecting from a palette or entering a hex, RGB or HSB code.

The content of the Style tab vary based on your chosen Message Options in the last step, but may include any of the options below:

| Formatting | Input | Description |
|---|---|---|
|Color Profile | Apply from In-App Message Templates Gallery. | Click __Apply Template__ and select from gallery. Then, click __Save__. |
|Text Alignment | Left, Center, or Right.  | Only available for newer Braze SDK versions. |
|Header | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color.  |
|Text | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
|Buttons | HEX color code. | Your desired HEX colors will display. You will also be able to choose the opacity of the colors. You can choose colors for: the message's Close Button Background as well as each button's Background, Text, and Border. |
|Background Color | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. This is the background of the entire message and will clearly display behind your text body. |
|Frame Color | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. Only available for newer Braze SDK versions. This is the frame around the entire message. |
|Chevron or other Close Message Option | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |

{% alert important %}
Mobile Apps and Custom Web Messages do not have the option for Styling beyond uploading custom HTML (and/or CSS and/or Javascript) and assets via ZIP, as described in the Compose step above. Web Modal with CSS allows you to upload or write custom CSS to create beautiful, all around custom-styled messaging.
{% endalert %}

### Web Modal CSS

If you choose to use a web-only, Web Modal with CSS message, you can [apply your own template][20] or write your own CSS in the provided space. This space is already pre-filled with the CSS shown in your message preview, and you should feel free to adjust it slightly to meet your needs.

If you choose to apply your own template, click __Apply Template__ and choose from the In-App Message Template Gallery. If you don't have any options, you can upload a [CSS Template using the CSS Template builder][2].

## Step 4: Configure Additional Settings

Add [key-value pairs][19] to your message if needed.

![InAppNewComposer3][13]

## Step 5: Preview Message

Preview what your message will look like to a random user, a specific user or a customized user - the latter two are especially useful if your message contains personalization or multiple languages. You can also preview messages for either mobile devices or tablets to get a better idea of what users will experience.

![InAppNewComposer4][14]

{% alert tip %}
Additional customization of the appearance of your In-App Messages can be accomplished by your developers. See [our integration documentation on In-App Messages]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/) for more details.
{% endalert %}

## Step 6: Trigger Your Delivery

![Schedule][6]

In-app message delivery is entirely based off of of the following action triggers:

- Making a purchase
- Opening the app/webpage
- Performing a custom event (only works with events sent via the SDK)
- Opening a specific push message
- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

{% alert warning %}
Unless you check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.
{% endalert %}

A start date and time must be selected, however, an end date is optional. An end date will stop that specific in-app message from showing up on devices after the specified date/time.

{% comment %}
  Need to check whether this statement is true: An end date will stop that specific in-app message from showing up on devices after the specified date/time. - also whether "Opening a specific push message" trigger is direct opens or also includes influenced opens."
{% endcomment %}

Additionally, unless you check the box titled "Allow users to become re-eligible to receive campaign" in the campaign wizard, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.

Finally, once you've selected the action the in-app message will be triggered off of, you should also set a priority. If two messages are triggered off of the same action, high priority messages will be scheduled to appear on users' devices before messages with lower priorities.

![Event Prioritization][16]

{% alert important %}
  The high, medium, and low options for triggered message priorities are buckets, and as such multiple messages could have the same selected priority. To set priorities within these buckets, click __Set Exact Priority__ and you will be able to drag and drop campaigns to order them with the correct priority.
{% endalert %}

![Bucket Prioritization][17]

## Step 7: Choose Target Segment

Next, you need to choose the target segment from the dropdown menu. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

![Target Page][7]

## Step 8: Choose Conversion Events

Braze allows you to track how often users perform specific actions (Conversion Events) after receiving a campaign. You can specify any of the following actions as a "Conversion Event":

- Opens App
- Makes Purchase
  - This can be a generic purchase or a specific item
- Performs specific custom event

You have the option of allowing up to a 30 day window during which a conversion will be counted if the user takes the specified action.

![Conversion Event][12]

## Step 9: Review and Deploy

The final page will give you a summary of the campaign you've just designed. Clicking "Start Campaign" will enable it to send. Confirm all the relevant details and watch the data roll in!

![confirm][8]

## Step 10: Analyze Results Data

For each in-app message campaign, Braze will show you impressions, unique impressions, clicks, revenue, and conversions.

![Results][9]

## Original In-App Messages {#original-in-app-messages}

Braze moved over to a new form of in-app messages with the following SDK releases:

- iOS: 2.19.0
- Android: 1.13.0
- Web: 1.3.0

Prior to these releases, Braze supported "original in-app messages." Support for original in-app messages will be provided for any customer who ran an in-app campaign prior to the new release. All of the campaign stats are unaffected by the change, and those who've sent original in-app messages will have the opportunity to send others via the "Create Campaign" button on the campaign screen.

![Choices][15]

[1]: {% image_buster /assets/img_archive/newcampaign.png %}
[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/in_app_message_color_templates/
[3]: {% image_buster /assets/img_archive/InAppNewComposer.png %}
[4]: {% image_buster /assets/img_archive/InAppNewComposer2.png %}
[6]: {% image_buster /assets/img_archive/in-app-schedule.png %}
[7]: {% image_buster /assets/img_archive/target_page.png %}
[8]: {% image_buster /assets/img_archive/confirm.png %}
[9]: {% image_buster /assets/img_archive/new-iam-stats.png %}
[10]: {% image_buster /assets/img_archive/intelligent_delivery.png %}
[11]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-iam
[12]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[13]: {% image_buster /assets/img_archive/InAppNewComposer3.png %}
[14]: {% image_buster /assets/img_archive/InAppNewComposer4.png %}
[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
[16]: {% image_buster /assets/img_archive/prioritization_options.png %}
[17]: {% image_buster /assets/img_archive/bucket_prioritization.png %}
[18]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[20]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/in_app_message_color_templates/#css-template
[21]: {% image_buster /assets/img/create_iam.gif %}
[22]: {% image_buster /assets/img/compose_iam.gif %}
