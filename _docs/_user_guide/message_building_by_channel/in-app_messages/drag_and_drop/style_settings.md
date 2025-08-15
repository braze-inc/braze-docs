---
nav_title: Style settings
article_title: "In-App Message Style Settings"
description: "This reference article covers the styling options available when creating an in-app message with the drag-and-drop editor."
page_order: 3
---

# In-app message style settings

> The drag-and-drop editing experience is divided into two sections: **Build** and **Preview & Test**. This article covers what you need to know for working within the **Build** tab of the editor and assumes you've already [created an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/).

!["Message styles" tab.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Message-level styles

You can set certain styles to be applied across all relevant blocks in your in-app message from the **Message Styles** tab. For example, you may want to customize the font of all the text or the color of all links in your message.

The styles in this section are used everywhere in your message except where you override it for a specific block. If your message has [multiple pages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), you can also override the message-level styles for individual pages, except for display type and max width.

For an easier design experience, we recommend setting up message-level styles before you customize styles at the block level.

To return to the **Message Styles** tab at any time:

- Click the close X button on individual block properties
- Select the message container, message close X button, or editor background

### Custom fonts

We accept the following file types for fonts: `.ttf`, `.woff`, `.otf`, and `.woff2`. For more information, see [Asset files]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

You can add multiple variations of a font family, as some styling options may not be available for custom fonts. Currently, we don't support adding fonts via URL.

To add a custom font:

1. Go to the **Content** section in the **Message styles** tab.
2. Click **Add custom font**.
3. Upload your font using the media library. 

{% alert note %}
The message-level font will only apply to the current message and any duplicated messages, but not to future templates.
{% endalert %}

## Message components

![A GIF showing a promotional in-app message being created.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

The drag-and-drop editor uses two key components for composing in-app messages: **rows** and **blocks**. All blocks must be placed in a row.

### Close x button

For Modal and Fullscreen in-app messages, you can customize the close button displayed as <i class="fa-solid fa-xmark"></i> in the top-right corner of your message. Customization options include button position, size, fill color, background color, border style, and border radius.

![Options to customize the close x button in in-app messages including button size, fill color, background color, border style, and border radius.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Rows

Rows are structural units that define the horizontal composition of a section of the message by using cells.

![Rows you can add in your in-app message.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

When a row is selected, you can add or remove the number of columns you need from the **Column customization** section to put different content elements side by side. 

You can also slide to adjust the size of existing columns.

![Adjusting columns from the "Column customization" section.]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

As a best practice, format your row and column properties before formatting any of the blocks inside the rows. There are many places where you can adjust the spacing and alignment, so starting from the foundation makes it easier to edit as you go.

### Blocks

Blocks represent different types of content you can use in your message. Drag one inside an existing row segment, and it will auto-adjust to the cell width.

{% alert tip %}
Before you add blocks, set up [message-level styles](#set-message-level-styles) for the message container, font, colors, and anything else you want to customize. You can then customize individual blocks as needed. The **Close Button** will remain at the top section of your message so that users always have the option to dismiss the message.
{% endalert %}

![Drag-and-drop boxes to select from.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Every block has its settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor block properties]({{site.baseurl}}/editor_blocks_dnd_iam/).

As you build your in-app message, you can select a mobile, tablet, or desktop view in the toolbar to preview how your in-app message will look for your user groups. This will ensure that your content is responsive, and you can make any necessary adjustments along the way.

## Creative details

### Fullscreen on larger screens {#fullscreen}

On a tablet or desktop browser, a fullscreen in-app message will sit in the center of the app screen. Any edits to the max width of the fullscreen message will only apply to tablet and desktop devices. 

![Full screen in-app message example.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Adding a background image

You can add an image to the background of your message from the **Message styles** tab. 

1. In the canvas area, select the background container. This is the scrollable section of your message.
2. In the **Message styles** tab, turn on **Background image**.
3. Add an image from your media library, or enter the URL where your image is hosted.

{% alert tip %}
If you're having trouble selecting a certain block, you can use the up arrow in the block's inline toolbar to move focus up to each parent block.
{% endalert %}

### Adding Liquid

![Icon to add Liquid personalization.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

To add [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) into your in-app message, select <i class="fa-solid fa-circle-plus"></i> **Add Personalization** from the editor toolbar. Here, you can add various personalization types such as default attributes, device attributes, custom attributes, and more.

Next, take your generated Liquid snippet and insert it into your message. After designing and building your in-app message, go to **Preview & Test** to preview your message.

### Using the AI copywriter

When a text block is selected in your in-app message, click <i class="fa-solid fa-wand-magic-sparkles" title="AI copywriter"></i> in the block toolbar to launch the [AI-powered copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). The AI copywriting assistant passes a brief product name or description to OpenAI’s GPT3 copy generation tool to generate human-like marketing copy for your messaging.

{% alert tip %}
You can save a few clicks by highlighting text inside the block before clicking the icon. The highlighted text will be added to the tool, and copy will be generated immediately.
{% endalert %}

![GIF of the AI copywriter.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Resetting styles to default

Properties that you have changed from their default styling are marked with an orange dot. To reset a specific property to its default style, hover over the field and select **Reset to default**.

![Orange dot that resets a text size to its default size.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

You can also reset all styling for a selected element by selecting the <i class="fas fa-paintbrush" title="Copy or paste styles button"></i> next to the properties panel name and selecting **Reset to default styles**.

### Copying and pasting styles

After making changes to the styling of an element, you can copy and paste those styles to another element. When pasting styles, only the properties relevant to that element are applied.

![Dropdown menu with option to copy styles.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. With the element selected, select <i class="fas fa-paintbrush" title="Copy or paste styles"></i> next to the properties panel name (For example, if you have a button selected, next to "Button properties").
2. Click **Copy styles** and select the element where you would like to apply the copied style.
3. Select <i class="fas fa-paintbrush" title="Copy or paste styles"></i> again and choose **Paste styles**.

#### Keyboard shortcuts

You can also use keyboard shortcuts to copy and paste styles:

| Action       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copy styles  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Paste styles | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
