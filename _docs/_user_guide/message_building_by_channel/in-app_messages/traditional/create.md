---
nav_title: Creating an in-app message
article_title: Creating an In-App Message
page_order: 1
description: "This reference article covers how to create an in-app message using the Braze platform using campaigns or Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Creating an in-app message

> You can create an in-app message or in-browser message using the Braze platform using campaigns, Canvas, or as an API campaign. We highly recommend planning out your messages and preparing all materials ahead of time using our handy [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Step 1: Choose where to build your message {#create-new-campaign-in-app}

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **In-App Message**. Note that in-app messages aren't available in multichannel campaigns.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed. Note that steps containing in-app messages cannot be action-based.
4. Filter your Audience for this step, as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay, at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% alert important %}
You can't have multiple in-app message variants in a single step.
{% endalert %}

You can find more Canvas-specific information in [In-app messages in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Step 2: Specify delivery platforms

Start by choosing which platforms should receive the message. Use this selection to limit the delivery of a campaign to a specific set of apps. For example, you might choose **Web Browsers** for an in-browser message encouraging users to download your mobile app to ensure they do not receive the message after already getting your app. Because platform selections are specific to each variant, you could try testing message engagement per platform.

| Platform                        | Message Delivery        |
|---------------------------------|-------------------------|
| Mobile Apps                     | iOS & Android SDKs      |
| Web Browsers                    | Web SDK                 |
| Both Mobile Apps & Web Browsers | iOS, Android & Web SDKs |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 3: Specify your message types

Once you've selected a sending platform, browse the message types, layouts, and other options associated with it. Learn more about the expected behavior and look of each of these messages on our [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) page, or by clicking on the linked message types in the following tables.

When deciding which message type to use, consider how much space your message will occupy and how disruptive it may feel to the user experience.

- **Slideup** messages are the least intrusive, appearing subtly without blocking content.
- **Modal** messages sit in the middle—prominent enough to catch attention without fully taking over the screen.
- **Fullscreen** messages are the most attention-grabbing and best for critical announcements or promotions.

The more complex your content, the more space you’ll need—and the more likely your message will interrupt the user’s flow.

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
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Fullscreen</a></td>
    <td>Messages that cover the entire screen with a message block.</td>
    <td>
      <ul>
      <li>Image & Text</li>
      <li>Image Only</li>
      </ul>
    </td>
    <td>Enforced Device Orientation (Portrait or Landscape)</td>
    <td>Big and bold! Use when you want to make sure users see your content, such as your most critical campaigns, important notifications, or massive promotions.<br><br>Note that on mobile devices, portrait and landscape messages won't display if the orientation of the device doesn't match the orientation of the message.</td>
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
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Email Capture Form</a></td>
    <td>Typically used to capture the viewer's email.</td>
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
    <td>Web Modal with CSS is unique to the Web SDK and can only be used after selecting <b>Web Browsers</b>.</td>
    <td>When you want to upload or write custom CSS to create beautiful, all-around custom-styled messaging. </td>
  </tr>
</tbody>
</table>

{% alert important %}
If Braze detects that you don't have a close or dismissal button included in your code, we will request that you add one in. For your convenience, we have provided a snippet that you can copy and paste into your code: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Step 4: Compose your in-app message

The **Compose** tab allows you to edit all aspects of your message's content and behavior.

![An example brand's in-app message to welcome new customers and prompt them to set up a user profile.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

The content of the **Compose** tab varies based on your chosen message options in the previous step, but may include any of the following options:

### Language

Select **Add Languages** and select your desired languages from the provided list. This will insert [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. See our [full list of available languages]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Image

Depending on your message type, you can **Upload Image**, **Pick a Badge**, or use **Font Awesome**. To upload an image, click **Add Image** or provide an image URL. Clicking **Add Image** opens the **Media Library**, where you can select a previously uploaded image or add a new one. Each message type and platform may have its own suggested proportions and requirements—be sure to check what those are before commissioning or making an image from scratch!

### Header and body

Write anything you want! Include completely custom copy (often with custom HTML capabilities) with the options to include [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) and other types of personalization. The faster you can get your message across and get your customer clicking—the better! We recommend clear and concise headers and message content.

Some message types do not need and therefore do not ask for headers.

#### Tips 

##### Generating AI copy

Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Launch AI Copywriter button, located in the Message field of the in-app message composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Creating right-to-left messages

Need help crafting right-to-left messages for languages like Arabic and Hebrew? Refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) for best practices.

### Button text {#buttons}

When available for your message type, you can have up to two buttons appear under your body of text. You can create and edit custom button text and color. You can also add Terms of Service Link within email capture forms.

If you choose to only use one button, it will automatically adjust to take over the available space at the bottom of your message instead of leaving room for an additional button.

#### Choosing a primary button

If you decide to format these buttons with your own colors, we recommend that you use Button 2 for your more preferred result.

In other words, if you want your user to click on one button more than the other, make sure it is on the right. The right button has often displayed better potential to get clicked, especially if it has a somewhat contrasting or otherwise stand-out color from the rest of the message. This is only emphasized when the button on the left blends more visually with the message.

![Primary and secondary buttons in an in-app message]({% image_buster /assets/img/primary-secondary-buttons.png %})

### On-click behavior {#button-actions}

When your customer clicks on a button in your in-app message, the following actions are available. 

| Action | Description |
|---|---|
| Redirect to Web URL | Open a non-native web page. |
| [Deep Link into App]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Deep link into an existing screen in your app. |
| Close Message | Closes the currently active message. |
| Log Custom Event | Choose a [custom event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) to trigger. Can be used to display another in-app message or trigger additional messaging. |
| Log Custom Attribute | Choose a [custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) to set for the current user. |
| Request Push Permission | Shows the native push permission. Read more about [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), as well as [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) for priming users for push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Note: the __Request Push Permission__, __Log Custom Event__, and __Log Custom Attribute__ options require the following SDK minimum versions:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOS device options

If desired, you can restrict your in-app message to only send to iOS devices. To do so, click **Change** and select **Only send to iOS devices**.

### Message close

Choose between the following options:
 
- **Dismiss Automatically:** Select how many seconds the message will remain on the screen.
- **Wait for User Swipe or Touch:** Requires a dismissal or close option.

### Slide up position

This setting only applies to the Slideup message type. Choose between having your slideup appear **From Bottom of App Screen** or **From Top of App Screen**.

### HTML and assets

This setting only applies to the Custom code message type. Copy and paste HTML into the available space and upload your assets using a ZIP file.

### Email capture input placeholder

This setting only applies to the email capture form message type. Enter custom copy that will appear as the placeholder text for the email input field. This defaults to "Enter your email address".

## Step 5: Style your in-app message

The **Style** tab allows you to adjust all visual aspects of your message. Upload an image or badge, or pick a pre-designed badge icon. Change the colors of the header and body text, buttons, and background by selecting from a palette or entering a hex, RGB, or HSB code.

The content of the **Style** tab varies based on your chosen message options in the previous step, but may include any of the following options:

| Formatting | Input | Description |
|---|---|---|
|[Color Profile]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Apply from in-app message templates gallery. | Select **Apply Template** and choose from the gallery. Then, select **Save**. |
|Text Alignment | Left, Center, or Right.  | Only available for newer Braze SDK versions. |
|Header | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color.  |
|Text | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
|Buttons | HEX color code. | Your desired HEX colors will display. You will also be able to choose the opacity of the colors. You can choose colors for: the message's Close Button Background as well as each button's Background, Text, and Border. |
| Button Border | HEX color code. | New! This will allow you to set your primary and secondary buttons apart from one another. We suggest outlining buttons with contrasting colors. |
|Background Color | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. This is the background of the entire message and will clearly display behind your text body. |
|Screen Overlay | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. Only available for newer Braze SDK versions. This is the frame around the entire message. |
|Chevron or other Close Message Option | HEX color code. | Your desired HEX color will display. You will also be able to choose the opacity of the color. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Always [preview and test]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) your message before sending.

{% alert important %}
Some in-app message types do not have the option for styling beyond uploading custom HTML (or CSS or JavaScript) and assets using a ZIP file. [Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) allows you to upload or write custom CSS to create beautiful, all-around custom-styled messaging.
{% endalert %}

## Step 6: Configure additional settings (optional)

### Key-value pairs

You can add [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) to send extra custom fields to user devices.

## Step 7: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign; see the following sections for further guidance on how to best use our tools to build in-app messages.

#### Choose a trigger

Select the action you'd like to trigger your message off of, as well as the start and end times for your campaign or Canvas.

{% alert important %}
Note that if you intend to trigger your in-app message based off a custom event, that custom event must be sent using the SDK.
{% endalert %}

![Action-based campaign with the trigger action set to "Start Session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

In-app message delivery is entirely based on the following action triggers:

- Making a purchase
- Opening the app/webpage
- Performing a custom event (only works with events sent using the SDK)
- Opening a specific push message
- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

A start date and time must be selected; however, an end date is optional. An end date will stop that specific in-app message from showing up on devices after the specified date/time.

Refer to our developer documentation for [server-side event triggering]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) and [local in-app message delivery]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Online versus offline triggering

In-app messages work by sending the message and triggers to the user's device. After the in-app messages are on a device, it waits to display until the trigger condition is met. If the in-app messages are already cached on the user's device, you can even trigger in-app messages offline with no connection to Braze (for example, in Airplane mode).

{% alert important %}
Once an in-app message has been stopped, there may be some users that continue to see the message if they started a session before the message was stopped and subsequently perform the trigger event. These users will be counted as a unique impression even after the campaign has been stopped.
{% endalert %}

#### Choose a priority

Finally, after you've selected the action the in-app message will be triggered off of, you should also set a priority. If two messages are triggered off of the same action, high priority messages will be scheduled to appear on users' devices before messages with lower priorities. 

You can choose between the following message priorities:

- Low priority (shown after other messages)
- Medium priority
- High priority (shown before other messages)

The high, medium, and low options for triggered message priorities are buckets, and as such multiple messages could have the same selected priority. To set priorities within these buckets, click **Set Exact Priority**, and you will be able to drag and drop campaigns to order them with the correct priority.

![An example of how priority is set for an in-app message campaign and Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

{% alert note %} 
If there's a delay on the in-app message step, segment membership will be evaluated after the delay. If the user is eligible, the in-app message will sync on the next available session.
{% endalert %}

##### Re-evaluate campaign eligibility and Liquid

In some scenarios, you may want to re-evaluate a user's eligibility as they trigger an in-app message to display. Examples include campaigns that target a custom attribute that frequently changes or messages that should reflect any last-minute profile changes.

![Checkbox for "Re-evaluate campaign eligibility before displaying" selected.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

When you select **Re-evaluate campaign eligibility before displaying**, an additional request to Braze will be made to confirm that the user is still eligible for this message before sending. Additionally, any [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) variables or [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) will be templated at that moment before the message is displayed.

This prevents in-app messages from being sent to users within expired or archived campaigns. If you don't re-evaluate a user's eligibility, the user will receive the in-app message even after the campaign has expired or is archived because the message is in your SDK and waiting for users to trigger it.

{% alert note %}
Enabling this option will result in a slight delay (< 100ms) between when a user triggers an in-app message and when the message is displayed due to the added eligibility and templating request.
<br><br>
Do not use this option for messages that can be triggered while a user is offline or when eligibility and Liquid re-evaluation are not required.
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}
{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

For information on Canvas-specific in-app messaging options, refer to [In-app messages in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Step 8: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, [test it]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/), then send it!

Next, check out [In-app message reporting]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) to learn how you can access the results of your messaging campaigns.

## Things to know

### Active in-app message campaign limits

Braze values reliability and speed. Just like we suggest you send only the data you need to Braze, we also recommend turning off any campaigns that are no longer adding any value to your brand.

Processing action-based in-app message campaigns that are still in an active state but no longer sending messages or are no longer needed slows down the overall performance of the Braze services for you and other customers. This extra time needed to process these large numbers of idle campaigns means that any in-app messages will take longer to appear on the end-user's devices, which impacts the end user's experience.

{% alert important %}
You can have up to 200 active, action-based in-app message campaigns per workspace to optimize the speed of message delivery and to prevent timeouts. This doesn't apply to Canvases.
{% endalert %}

The 200 count includes active in-app message campaigns that have not yet reached end time and those that have no end time. Active in-app message campaigns that have passed their end times will not be counted. The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation will impact you.


