---
nav_title: Email Global Style Settings
article_title: Email Global Style Settings
permalink: "/global_style_settings/"
hidden: true
channel: email
page_order: 3
description: "This reference article covers how to set global email style settings for your campaigns and Canvases."
tool: 
  - Campaigns
  - Canvas
---

# Drag & Drop Editor settings

With global style settings, you can personalize the look of your email campaigns and Canvases. You can add and customize a default theme for your Drag & Drop Editor. This includes editing your styles for email titles, text, buttons, and more.

{% alert important %}
Global style settings for the Drag & Drop Editor are currently in early access. Please contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

To edit your global style settings, go to the **Manage Settings** page and select the **Email Settings** tab. Select **Drag & Drop Email Editor Settings**.

![Drag & Drop Email Editor Settings][1]

{% alert note %}
Updates made to the Email Global Style Settings will apply to all future email campaigns and Canvases. 
{% endalert %} 

## Basic styling 

In the **Basic Styling** dropdown, you can set your default email and content background colors for your email campaigns and Canvases. You can also select a default font, add a custom font, and edit link colors.

![Basic Styling Options][2]

### Add a custom font
To add a custom font, click **Add a custom font** and enter the font's name and source file URL. For the **Font Name** field, enter the same font name as your custom font source file. Ensure that the name is capitalized and spaced correctly. Enter the corresponding **Font URL**. Check that the preview shows your custom font before saving. Click **Save** to use the custom font as your default email font. 

Currently, you can only add one custom font for the global style settings.

![Add Custom Font][3]{: style="max-width:80%;"}

## Title styling
Here, you can adjust the styles of your email titles by editing the font size, font color, and text alignment. This applies to the main header and secondary header. 

![Heading Styling Options][6]

Optionally, you can override the default style of your Drag & Drop Editor theme. Click **Override default style** to apply your choice of title styling. This can include setting a different font and link color.

![Default Override][7]{: style="max-width:60%;"}

## Text styling
To set a default text style, in the **Text Styling** dropdown, enter the **Font Size** and select **Font Color** to choose a font color from the color picker. 

You can also adjust the block styling for the body text by editing the **Padding Top**, **Padding Right**, **Padding Bottom**, and **Padding Left** values. This will apply to the spacing around all four areas surrounding the text block.

![Text Styling Options][4]{: style="max-width:60%;"}

## Button styling

In the **Button Styling** dropdown, you can edit the following defaut styles for the button:
- Background color
- Font size
- Font color
- Border radius
- Border color
- Border weight
- Button padding

Adjust the block styling for buttons by editing the **Padding Top**, **Padding Right**, **Padding Bottom**, and **Padding Left** values.

![Button Styling Options][5]{: style="max-width:50%;"}

After editing the styles in the Drag & Drop Email editor, click **Save**. To further customize your email campaigns and Canvases, check out [Drag & Drop Editor blocks][8]!

[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[4]: {% image_buster /assets/img_archive/dnd_text_styling.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_default_override.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks