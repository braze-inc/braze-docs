---
nav_title: Creating an In-App Message
article_title: "Creating an in-app message with Drag and Drop"
description: "With the Drag & Drop Editor, you can create completely custom and personalized in-app messages in either campaigns or Canvas using the drag & drop editing experience."
permalink: "/create_dnd_iam/"
hidden: true
---

# Creating an in-app message with Drag and Drop

With the Drag & Drop Editor, you can create completely custom and personalized in-app messages in either campaigns or Canvas using the drag & drop editing experience.

{% alert important %}
This feature is currently in beta. Please reach out to your custommer success representative for access.
{% endalert %}

If you want to use your existing custom HTML templates or templates created by a third party, they must be recreated in the Drag & Drop Editor.

> TO DO: Add video how-to

Not sure whether your in-app message should be sent using a campaign or a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys. Once you’ve selected where to build your message, let’s dive into the steps to create a drag & drop in-app message!

## Prerequisites

Messages created using the Drag and Drop editor can only be sent to users on the following minimum SDK versions:

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

If a user hasn't updated their application (that is, they're on an older SDK version) they will not receive the in-app message.

## Step 1: Specify delivery platforms

After selecting the Drag & Drop Editor as your editing experience, select the message platform you would like to send your message to: Mobile Apps, Web Browsers or Both Mobile Apps & Web Browsers.

## Step 2: Build and design your in-app message

The drag & drop editing experience is divided into three sections: **Build**, **Settings**, and **Preview & Test**.

### Drag and drop in-app message components

When you open the Drag & Drop Editor, you’ll see a basic modal layout on the editing canvas, which you can use to start building your message. You can keep this layout or add, delete, and move around the Rows and Blocks. The **Close Button** will remain at the top section of your message so that users always have an option to dismiss the modal.

![Replace with GIF]({% image_buster /assets/img_archive/dnd_iam_placeholderimg.png %})

The Drag & Drop editor uses two key components to make in-app message composition quick and easy: **Rows** and **Blocks**.

![]({% image_buster /assets/img_archive/dnd_iam_rows_blocks.png %}){: style="float:right;max-width:25%;margin-left:15px"}

- **Rows** are structural units that define the horizontal composition of a section of the message by using cells. Using more than one cell allows you to put different content elements side by side. You can add all the structural elements you need to your message.
- **Blocks** represent different types of content you can use in your message. Simply drag one inside an existing row segment, and it will auto-adjust to the cell width.

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor Block Properties]({{site.baseurl}}/editor_blocks_dnd_iam/).

As you build your in-app message, you can select a mobile, tablet, or desktop view in the toolbar to preview how your in-app message will look for your user groups. This will ensure that your content is responsive, and you can make any necessary adjustments along the way.

### Set default font settings

You can select a default font or add a custom font to be applied across all possible in-app message text in the **Settings** tab. The default font set in this section is used everywhere in your message except where you use a custom setting.

#### Add a custom font

To add a custom font, go to the **Settings** tab, click **Add a custom font**, and upload your font using the Media Library. We accept the following file types for fonts: `.ttf`, `.woff`, `.otf`, `.woff2`. For more information, see [Asset files]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

You can add multiple variations of a font family, as some styling options may not be available for custom fonts. Currently, we don't support adding fonts via URL.

{% alert note %}
The default font will only apply to the current message and any duplicated messages, but not to future templates.
{% endalert %}

### Creative details

#### Adding Liquid

![]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

To add [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) into your in-app message, select <i class="fa-solid fa-circle-plus"></i> **Liquid Personalization** from the editor toolbar. Here, you can add various personalization types such as default attributes, device attributes, custom attributes, and more!

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

