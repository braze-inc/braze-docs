---
nav_title: Email Global Style Settings
article_title: Email Global Style Settings
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "This reference article covers how to set global email style settings in the drag and drop editor for your campaigns and Canvases."
tool: 
  - Campaigns
  - Canvas
---

# Email global style settings

> With global style settings, you can personalize the look of your email campaigns and Canvases. You can add and customize a default theme for your drag and drop editor. This includes editing your styles for email titles, text, buttons, and more.

To edit your global style settings, go to **Settings** > **Email Preferences** > **Drag-and-Drop Email Preferences**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Manage Settings** > **Email Settings** > **Drag-and-Drop Email Editor Settings**.
{% endalert %}

![][1]

{% alert note %}
Updates made to the global style settings will apply to all future email campaigns and Canvases. 
{% endalert %} 

## Basic styling 

For **Basic Styling**, you can set your default email and content background colors for your email campaigns and Canvases. You can also select a default font, add a custom font, and edit link colors.

![Basic styling options that include options to edit the email and content background colors, default font name, and default link color.][2] 

## Custom font

With custom fonts, you can manually add a web font for branding consistency across various email platforms. You can add one custom font per section. 

To add a custom font:

1. Click **Add a custom font** below the **Default Font Name** of the styling section.
2. Enter the font's name and source file URL. This source file URL must point to a style sheet like a CSS file. For the **Font Name** field, enter the same font name as your custom font source file. Ensure that the name is capitalized and spaced correctly. Enter the corresponding **Font URL**. 
3. Check that the preview shows your custom font before saving. 
4. Click **Save** to use the custom font as your default email font. 

{% alert important %}
Gmail does not support custom fonts, so your custom font may display as a default system font. For other email platforms, check that your custom font displays correctly prior to sending your email messaging.
{% endalert %}

To use alternative custom fonts in your email campaigns, you have the option to create an [email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) or [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Be sure to check that your font choice is still web-safe and supported on your email platforms. 

### Fallback font

Fallback fonts are used for the title, header, and body text when your default font choice isn't supported by the inbox provider or operating system. By default, Braze automatically sets Arial as a fallback font when global style settings are saved. You also have the option of adding serif or sans serif as options for your default font family.

![][11]

You can add up to 17 fallback fonts. The first fallback font selected will be the one attempted first. The fallback font will only be applied for newly created templates, email campaigns, and Canvas components. The fallback font isn't automatically set for messages that were created before the fallbak font was specified. We highly recommend selecting fallback fonts that are similar to your email messaging to maintain consistency across your branding.

## Title styling

Here, you can adjust the styles of your email titles by editing the font size, font color, and text alignment. This applies to the main header and secondary header. 

![][9]

Optionally, you can override the default style of your drag-and-drop editor theme. Click **Override default style** to apply your choice of title styling. This can include setting a different font and link color.

## Paragraph styling

To set a default paragraph style, go to  the **Paragraph Styling**, enter the **Font Size** and select **Font Color** to choose a font color. You can also adjust the block styling for the body text by editing the **Padding Top**, **Padding Right**, **Padding Bottom**, and **Padding Left** values. This will apply to the spacing around all four areas surrounding the paragraph block.

![][7]

## List styling

When adding lists to your messaging, the **List Styling** section creates the consistency in how your lists are styled. This incudes details like font size, font color, line weight, alignment, text direction, list item spacing and indentation.

Here, you can also set the **List Type** to be either numbered or bulleted. The **List Style Type** provides additional customization for the style of your lists. For example, you can set the list types to always be bulleted, and for each bullet to be a square.  

![][10]

## Button styling

In the **Button Styling** section, you can edit the following default styles for the button:
- Background color
- Font size
- Font color
- Border radius
- Border color
- Border weight
- Button padding

![][12]

As with all other styling sections, you can adjust the block styling by editing the **Padding Top**, **Padding Right**, **Padding Bottom**, and **Padding Left** values.

After editing the styles in the drag-and-drop email editor, click **Save**. To further customize your email campaigns and Canvases, check out how you can incorporate [drag-and-drop editor blocks][8].

[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks