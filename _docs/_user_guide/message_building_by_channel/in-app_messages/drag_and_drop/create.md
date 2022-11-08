---
nav_title: Creating an In-App Message
article_title: "Creating an in-app message with Drag & Drop"
description: "With the Drag & Drop Editor, you can create completely custom and personalized in-app messages in either campaigns or Canvas using the drag & drop editing experience."
alias: "/create_dnd_iam/"
---

# Creating an in-app message with Drag & Drop

With the Drag & Drop Editor, you can create completely custom and personalized in-app messages in either campaigns or Canvas using the drag & drop editing experience.

{% alert important %}
This feature is currently in early access. Please reach out to your customer success representative for access.
{% endalert %}

If you want to use your existing custom HTML templates or templates created by a third party, they must be recreated in the Drag & Drop Editor.

Not sure whether your in-app message should be sent using a campaign or a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys. Once you’ve selected where to build your message, let’s dive into the steps to create a drag & drop in-app message!

## Prerequisites

Messages created using the Drag & Drop Editor can only be sent to users on the following minimum SDK versions:

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

If a user hasn't updated their application (that is, they're on an older SDK version), they will not receive the in-app message.

**Additional Web SDK prerequisite**<br>
The initialization option [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) must be set to `true`. The `enableHtmlInAppMessages` option will also allow these messages to function, but is deprecated and should be updated to `allowUserSuppliedJavascript`.

## Step 1: Create an in-app message

Create a new in-app message or Canvas step, then select **Drag & Drop Editor** as your editing experience.

## Step 2: Build and design your in-app message

The drag & drop editing experience is divided into two sections: **Build** and **Preview & Test**.

### Set message-level styles

You can set certain styles to be applied across all relevant blocks in your in-app message from the **Message Styles** tab. The styles set in this section are used everywhere in your message except where you override it for a specific block.

To return to the **Message Styles** tab at any time:

- Click the close X button on individual block properties
- Select the message container, message close X button, or editor background

#### Add a custom font

To add a custom font:

1. Go to the **Content** section in the **Message styles** tab.
2. Click **Add custom font**.
3. Upload your font using the Media Library. 

We accept the following file types for fonts: `.ttf`, `.woff`, `.otf`, `.woff2`. For more information, see [Asset files]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

You can add multiple variations of a font family as some styling options may not be available for custom fonts. Currently, we don't support adding fonts via URL.

{% alert note %}
The message-level font will only apply to the current message and any duplicated messages, but not to future templates.
{% endalert %}

### Drag and drop in-app message components

When you open the Drag & Drop Editor, you’ll see a basic modal layout on the editing canvas, which you can use to start building your message. You can keep this layout or add, delete, and move around the Rows and Blocks. The **Close Button** will remain at the top section of your message so that users always have an option to dismiss the modal.

![]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

The Drag & Drop Editor uses two key components to make in-app message composition quick and easy: **rows** and **blocks**. All blocks must be placed in a row.

#### Rows

Rows are structural units that define the horizontal composition of a section of the message by using cells. 

![]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

When a row is selected, you can add or remove the number of columns you need from the **Column customization** section to put different content elements side by side. 

You can also slide to adjust the size of existing columns.

![]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

#### Blocks

Blocks represent different types of content you can use in your message. Simply drag one inside an existing row segment, and it will auto-adjust to the cell width.

![]({% image_buster /assets/img_archive/dnd_iam_blocks.png %}){: style="max-width:40%"}

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor Block Properties]({{site.baseurl}}/editor_blocks_dnd_iam/).

As you build your in-app message, you can select a mobile, tablet, or desktop view in the toolbar to preview how your in-app message will look for your user groups. This will ensure that your content is responsive, and you can make any necessary adjustments along the way.

### Creative details

#### Customize background image 

You can add an image to the background of your message from the **Message styles** tab. The scrollable section of your message must be selected to add a background for the entire message.

{% alert tip %}
If you're having trouble selecting a certain block, you can use the up arrow in the block's inline toolbar to move focus up to each parent block.
{% endalert %}

#### Adding Liquid

![]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

To add [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) into your in-app message, select <i class="fa-solid fa-circle-plus"></i> **Add Personalization** from the editor toolbar. Here, you can add various personalization types such as default attributes, device attributes, custom attributes, and more!

Next, take your generated Liquid snippet and insert it into your message. Once you’ve finished designing and building your in-app message, go to **Preview & Test** to preview your message.

## Step 3: Test your in-app message

The **Preview & Test** section allows you to preview your in-app messages across different devices and send a test message to yourdevice. Here you can ensure that the details are aligned across all your platforms for your drag & drop in-app message campaign. It's extremely important to always test your in-app messages before sending your campaigns to help you visualize what your final message will look like from your user’s perspective.

### Preview message as a user

{% alert warning %}
To send a test to either Content Test Groups or individual users, push must be enabled on your test devices before sending.
{% endalert %}

You can preview messages from the **Preview & Test** tab, as though you were a user. You can select a specific user, a random user, or create a custom user:

- **Random User:** Braze will randomly select a user from the database and preview the in-app message based on their attributes or event information.
- **Select User:** You can select a specific user based on their email address or external_id. The in-app message will preview based on that user’s attributes and event information.
- **Custom User:** You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.

### Test checklist

- Have you tested the message on different devices?
- Do the images and media show up and act as expected?
- Does the Liquid function as expected? Have you accounted for a default attribute value in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
- Do your buttons direct the user where they should go?

## FAQs

**Can I customize my in-app message using custom HTML or Javascript or transfer existing HTML messages into the editor?**<br>
No.

**Can I save my in-app message as a template after I build it within my campaign or Canvas?**<br>
No, you have to recreate the in-app message in the Drag & Drop Editor or duplicate an existing message in order to save.

**How can I create a full-screen or slideup in-app message?**<br>
Currently the editor is limited to modal messages only.
