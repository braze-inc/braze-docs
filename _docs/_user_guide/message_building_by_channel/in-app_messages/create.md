---
nav_title: Create an In-App Message
article_title: Create an In-App Message
page_order: 0
description: "You can create an in-app message using the Braze platform using campaigns, Canvas, or as an API campaign. This article will guide you through this process."
channel:
  - in-app messages
tool:
  - Campaigns

---

# Creating an in-app message

You can create an in-app message or in-browser message using the Braze platform using campaigns, Canvas, or as an API campaign. We highly recommend planning out your messages and preparing all materials ahead of time using our handy [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Step 1: Choose where to build your message {#create-new-campaign-in-app}

{% tabs %}
  {% tab Campaigns %}
  Click __Create Campaign__ to open a new messaging wizard for in-app message campaigns. Then, follow the flow of the messaging wizard to quickly create and launch your in-app message campaign.

  ![Platform Picker]({% image_buster /assets/img/iam_platforms.gif %})

1. Name your campaign something clear and meaningful.
2. Add __Teams__ and __Tags__, as necessary.
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.

  {% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

 {% endtab %}
 {% tab Canvas %}
 After you have [created your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard,

1. Name your step something clear and meaningful.
2. Add a Delay, as necessary. Note that steps containing in-app messages cannot be action-based.
3. Filter your Audience, as necessary.
4. Choose your advancement options, as necessary.
5. Choose all other messaging channels which you would like to pair with your message.

{% alert important %}
You cannot have multiple in-app message variants in a single step.
{% endalert %}

You can find more Canvas-specific information in [In-app messages in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Step 2: Specify delivery platforms

Start by choosing which platforms should receive the message. Use this selection to limit the delivery of a campaign to a specific set of apps. You might choose __Web Browsers__ for an in-browser message encouraging users to download your mobile app to ensure they do not receive the message after already getting your app. Because platform selections are specific to each variant, you could try testing message engagement per platform!

Web Email Capture and Web Modal with CSS are both unique to the Web SDK and can only be used after selecting __Web Browsers__.

| Platform | Message Delivery |
|---|---|
| Mobile Apps | iOS & Android SDKs|
| Web Browsers | Web SDK|
| Both Mobile Apps & Web Browsers | iOS, Android & Web SDKs|
{: .reset-td-br-1 .reset-td-br-2}

## Step 3: Specify your message types

Once you've selected a sending platform, browse the message types, layouts, and other options associated with it. Learn more about the expected behavior and look of each of these messages on our [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) page, or by clicking on the linked message types in the following tables.

When deciding which message type to use, you should consider how intrusive your in-app message campaign needs to be. This is a measure how much screen real estate the message will take up and how much this interrupts your customer's regular experience in your app or site. The more rich content you want to deliver, the more intrusive your message will need to be.

![Graphic showing a scale of less instrusive to more intrusive, with Slider being the least intrusive, followed by Modal, and Full screen being the most intrusive]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### Message types

These in-app messages are accepted by both mobile apps and web applications.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Message Type</th>
    <th>Type Description</th>
    <th>Available Layouts</th>
    <th>Other Options</th>
    <th>Recommended Use</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Full-Screen</a></td>
    <td>Messages that cover the entire screen with a message block.</td>
    <td>
      <ul>
      <li>Image & Text</li>
      <li>Image Only</li>
      </ul>
    </td>
    <td>Enforced Device Orientation (Portrait or Landscape)</td>
    <td>Big and bold! Use when you want to make sure users see your content, such as your most critical campaigns, important notifications, or massive promotions.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Messages that cover the entire screen with a screen overlay and a message block.</td>
    <td>
      <ul>
      <li>Text (with Optional Image)</li>
      <li>Image Only</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>A good middle ground. Use when you need an apparent way to catch your user's attention, such as encouraging users to try a new feature or take advantage of a promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Slideup</a></td>
    <td>Messages that slide into view in a designated place without blocking the rest of the screen.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Unobtrusive—takes up the least amount of screen real estate. Use when alerting users to small snippets of information, such as new features, announcements, use of cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Advanced message types

These in-app messages are customizable to your needs.

<table class="tg">
<thead>
  <tr>
    <th>Message Type</th>
    <th>Type Description</th>
    <th>Available Layouts</th>
    <th>Requirements</th>
    <th>Recommended Use</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Custom HTML Message</a></td>
    <td>Custom messages that perform as defined in your custom code (HTML, CSS, and/or JavaScript).</td>
    <td>N/A</td>
    <td>Must set <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> initialization option to <code>true</code> for your in-app message to work.</td>
    <td>This is a good option if you want all the advantages of IAMs but need additional functionality or for the appearance to stay "on brand". You can alter every little detail of the message—font, color, shape, size, buttons, etc. <br><br>Example use cases include asking users for app feedback, email capture forms, or paginated messages</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Web Email Capture Form</a></td>
    <td>Typically used to capture the viewer’s email.</td>
    <td>N/A</td>
    <td>Must set <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> initialization option to <code>true</code> for your in-app message to work.</td>
    <td>When prompting users to submit their email address.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Web Modal with CSS</a></td>
    <td>Modal messages for web with customizable CSS.</td>
    <td>
      <ul>
      <li>Text (with Optional Image)</li>
      <li>Image Only</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>When you want to upload or write custom CSS to create beautiful, all around custom-styled messaging. </td>
  </tr>
</tbody>
</table>

{% alert important %}
If Braze detects that you don't have a close or dismissal button included in your code, we will request that you add one in. For your convenience, we have provided a snippet that you can copy and paste into your code: `<a href= "appboy://close">X</a>`.
{% endalert %}

## Step 4: Compose in-app message

The **Compose** tab allows you to edit all aspects of your message's content and behavior.

![Compose your in-app message][24]

The content of the Compose tab varies based on your chosen message options in the previous step, but may include any of the options below:

| Content | Options| Description |
|---|---|---|
|Language | See our [full list of available languages][18]. | Click __Add Languages__ and select your desired languages from the provided list. This will insert Liquid into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. |
|Image | __Upload Image__, __Pick a Badge__, or use __Font Awesome__. | Where applicable, click __Include Image__ or __Upload Image__ and follow the presented instructions. Each message type and platform may have its own suggested proportions and requirements - be sure to check what those are before commissioning or making an image from scratch! |
|Button Text & On Click Behavior| Add up to two [buttons](#buttons). | You can create and edit custom button text and color. You can also add  Terms of Service Link within Web Email Capture forms.  |
|Device Options | Restrict send to only iOS devices. | Click __Change__ and check the box as desired. |
|Message Close Options | __Dismiss Automatically__ or __Wait for User Swipe or Touch__. | __Dismiss Automatically__ allows you to select how many seconds the message will remain on the screen. __Wait for User Swipe or Touch__ will require a dismissal or close option.  |
|Header & Body Text | Completely custom copy (often with custom HTML capabilities) with the options to include Liquid and other types of personalization. | Some message types do not need and therefore do not ask for headers. |
|Position | __From Bottom of App Screen__ or __From Top of App Screen__. | This only exists in the Universal Slideup message builder.|
|HTML & Assets | Completely custom via upload, URL, or copy and paste. | Copy and paste HTML into the available space and upload your assets via ZIP. |
|Email Capture Input Placeholder | Custom copy. | This is used solely in the Web Email Capture Form and will direct your users to input the desired content into the space. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Additional settings

#### Buttons {#buttons}

When available for your message type, you can have up to two buttons appear below your body of text.

![Primary_Secondary]({% image_buster /assets/img/primary-secondary-buttons.png %}){: height="40%" width="40%"}

If you choose to only use one button, it will automatically adjust to take over the available space at the bottom of your message instead of leaving room for an additional button.

{% alert tip %}
  If you decide to format these buttons with your own colors, we recommend that you use Button 2 for your more preferred result. In other words, if you want your user to click on one button more than the other, make sure it is on the right. The right button has often displayed better potential to get clicked, especially if it has a somewhat contrasting or otherwise stand-out color from the rest of the message. This is only emphasized when the button on the left blends more visually with the message.
{% endalert %}

#### Generations

Braze has three generations of in-app messages available. You can fine-tune to which devices your messages should be sent, based on which generation they support, in the [preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) section while composing your in-app message.

![In-App_Messages_Generations][2]{: height="50%" width="50%"}

Depending on what SDK versions your users are on, you may or may not see this option. You are only asked to select a generation when you have users on more than one generation.

{% details What is a generation? %}
A Generation is defined as a collection of SDK versions that contain a large number of major upgrades. For example, Generation 3 is the latest one that encompasses the latest style updates.

By selecting __Send to all Generations that support this message__, Braze will deliver to users that can receive any form of the message. For example, if you have users on all three Generations, a modal will deliver to users on Generations 2 and 3, as Generation 1 doesn't support modals. The message will look different for your two groups of users: Generation 3 users will receive the message in the latest styles, while Generation 2 users will see the older styles (cosmetic differences and absence of button border).

You could clear the __Send to all Generations that support this message__ checkbox and select __Send only to users on Generation 3 (the latest)__ if you do not want to allow users to receive the older message styles. Users on Generation 3 will be the only ones to receive the message.
{% enddetails %}

## Step 5: Style your in-app message

The **Style** tab allows you to adjust all visual aspects of your message. Upload an image or badge, or pick a pre-designed badge icon. Change the colors of the header and body text, buttons, and background by selecting from a palette or entering a hex, RGB, or HSB code.

The content of the **Style** tab varies based on your chosen Message Options in the last step, but may include any of the options below:

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

## Step 6: Configure additional settings

### Key-value pairs

Add [key-value pairs][19] to send extra custom fields to user devices.

### Re-evaluate campaign eligibility and Liquid

In some scenarios, you may want to re-evaluate a user's eligibility as they trigger an in-app message to display. Examples include campaigns that target a custom attribute that frequently changes or messages that should reflect any last-minute profile changes.

![Re-evaluate IAM Membership][27]

When you select **Re-evaluate campaign eligibility before displaying**, an additional request to Braze will be made to confirm that the user is still eligible for this message before sending. Additionally, any [Liquid][25] variables or [Connected Content][26] will be templated at that moment before the message is displayed.

{% alert note %}
Enabling this option will result in a slight delay (< 100ms) between when a user triggers an in-app message and when the message is displayed due to the added eligibility and templating request.
<br><br>
Do not use this option for messages that can be triggered while a user is offline or when eligibility and Liquid re-evaluation are not required.
{% endalert %}

## Step 7: Build the remainder of your campaign or Canvas

Build the remainder of your campaign or Canvas; see the sections below for further guidance on how to best use our tools to build in-app messages. For more information on Canvas-specific in-app messaging options like expiry and steps, refer to [In-app messages in Canvas][16].

### Triggering

Select the action you'd like to trigger your message off of, as well as the start and end times for your campaign or Canvas.

{% alert important %}
Please note that if you intend to trigger your in-app message based off a custom event, that custom event must be sent via the SDK.
{% endalert %}

![Schedule]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

In-app message delivery is entirely based on the following action triggers:
- Making a purchase
- Opening the app/webpage
- Performing a custom event (only works with events sent via the SDK)
- Opening a specific push message
- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

A start date and time must be selected; however, an end date is optional. An end date will stop that specific in-app message from showing up on devices after the specified date/time.

Please refer to our developer documentation for [server-side event triggering]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) and [local in-app message delivery]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

#### Online vs. offline triggering

In-app messages work by sending the message and triggers to the user's device. Once the in-app messages are on a device, it waits to display until the trigger condition is met. If the in-app messages are already cached on the user's device, you can even trigger in-app messages offline with no connection to Braze (for example, in Airplane mode).

{% alert important %}
Once an in-app message campaign has been stopped, there may be some users that already received the message but have not seen it because they haven't opened your app. These users will still see your in-app message and be counted as a unique impression—even after your campaign has been stopped.
{% endalert %}

### Prioritize

{% tabs %}
{% tab Campaigns %}

Finally, once you've selected the action the in-app message will be triggered off of, you should also set a priority. If two messages are triggered off of the same action, high priority messages will be scheduled to appear on users' devices before messages with lower priorities.

![Event Prioritization]({% image_buster /assets/img_archive/prioritization_options.png %}){: style="max-width:80%"}

The high, medium, and low options for triggered message priorities are buckets, and as such multiple messages could have the same selected priority. To set priorities within these buckets, click __Set Exact Priority__, and you will be able to drag and drop campaigns to order them with the correct priority.

![Bucket Prioritization]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

{% endtab %}
{% tab Canvas %}

A customer may trigger two in-app messages within your Canvas at the same time. When this occurs, Braze will follow the priority order below to determine which in-app message is displayed. Drag different Canvas steps to re-order their priority. By default, steps earlier in a Canvas variant will display before later steps.

![step_priority]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Navigate to the **Send Settings** of the Canvas section to prioritize in-app messages from a Canvas against in-app messages from other Canvases and campaigns.

By default, Canvas step priority is set to medium, with the most recently created steps having the highest relative priority. Canvas and campaign-level priorities also default to medium, with the highest relative priority defaulting to the most recently created items.

![canvas_priority]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

### Target segment

Next, you need to choose the target segment from the dropdown menu. You are automatically given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

![Target Page]({% image_buster /assets/img_archive/target_page.png %}){: style="max-width:50%"}

{% alert note %} 
If there's a delay on the in-app message step, segment membership will be evaluated after the delay. If the user is eligible, the in-app message will sync on the next available session.
{% endalert %}

### Conversion events

Braze allows you to track how often users perform specific actions (conversion events) after receiving a campaign. You can specify any of the following actions as a conversion event":

- Opens App
- Makes Purchase (This can be a generic purchase or a specific item)
- Performs specific custom event

You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action.

![Conversion Event]({% image_buster /assets/img_archive/conversion_event_selection.png %}){: style="max-width:50%"}

> After you've finished building the last of your campaign or Canvas, review its details, then send it!

## Active in-app message campaign limits

Braze values reliability and speed. Just like we suggest you send only the data you need to Braze, we also recommend turning off any campaigns that are no longer adding any value to your brand.

Processing action-based in-app message campaigns that are still in an active state but no longer sending messages or are no longer needed slows down the overall performance of the Braze services for you and other customers. This extra time needed to process these large numbers of idle campaigns means that any in-app messages will take longer to appear on the end-user's devices, which impacts the end user's experience.

There is a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts.

The 200 count includes active IAM campaigns that have not yet reached end time and those that have no end time. Active IAM campaigns that have passed their end times will not be counted. The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation will impact you.


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img/iam_compose.gif %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
