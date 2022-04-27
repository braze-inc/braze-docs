---
nav_title: Editor Blocks
article_title: Drag & Drop Editor Blocks
alias: "/dnd/editor_blocks/"
channel: email
page_order: 1
description: "This reference article covers the different editor blocks that are provided in the email Drag & Drop Editor."
tool: Media

---

# Editor blocks

Editor blocks are the various blocks available in the Drag & Drop Editor under the **Content** section. This section includes a series of tiles that represent the different kinds of content you can use in your message.

To use them, drag an editor block inside a column. It will auto-adjust to the column width. Each editor block has its owns settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

## Types

The following table describes how users can use each editor block type.

| name | description |
|---|---|
| `Title`  | Adds text with H1, H2, and H3 tags for email. | 
| `Text`  |  Enters text into their message. A toolbar helps with font and text editing functionality. | 
| `Image` | Inserts an image from the Media Library. | 
| `Button` |  Adds a standard button. Properties for this block allow for editing and setting links easily.  | 
| `Divider` |  Inserts a solid, dotted, or dashed line to help with spacing.|
| `HTML` |  Inserts raw HTML. Great for advanced Liquid such as Connected Content or conditional statements. | 
| `Menu` |  Creates a flexible menu for the message you're designing. |
| `Spacer` |  Adds space, or "padding", between other blocks. |
{: .reset-td-br-1 .reset-td-br-2} 

## Properties

Details for each editor block's properties are provided in the following tables.

### Title

| properties | description |
|---|---|
| `Title`  | Selects the heading style. Only H1, H2, or H3 are available. | 
|`Font Family`| This is the font style for your title. |
|`Font Size`| Determines the size of your text. |
|`Text Color`| Modifies the color of the title. |
|`Link Color`| Modifies the color of the link. |
|`Align`| Moves the title to be left, center or right-oriented. |
|`Line Height`| Modifies the distance between lines of text. |
|`Line spacing`| Modifies the distance in between each character. |
|`Text direction`| Default left-to-right, but can be edited to be right-to-left. |
{: .reset-td-br-1 .reset-td-br-2}

### Text

Refer to the following table for details on the `Text` editor block properties.

| properties | description |
|---|---|
|`Text Color`| Modifies the color of the title. |
|`Link Color`| Modifies the color of the link. |
|`Line Height`| Modifies the distance between lines of text|
|`Line spacing`| Modifies the distance in between each character|
{: .reset-td-br-1 .reset-td-br-2}

### Image

Refer to the following table for details on the `Image` editor block.

| properties | description |
|---|---|
|`Auto Width`| Modifies the pixels of the image. |
|`Align`| Moves the image to be either left, center or right-oriented. |
|`URL`| The hosted address for your image. |
|`Alternate text`| The written copy that appears in place of an image when the image fails to load. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
For `Auto Width`, automatic image resizing picks the best size for the image based on a combination of image width and available space in the layout:
- Images wider than the available space will be set at 100% width and will keep this ratio on mobile, using the entire device display width.
- Images smaller than the available space will use the image's natural size to avoid distortion effects or blurry pictures.
{% endalert %}

### Button

Refer to the following table for details on the `Button` editor block.

| properties | description |
|---|---|
|`Link Type`| Determines the action when clicking the button and sets the appropriate link protocol. |
|`URL`| Dynamic based on the selected `Link Type`.|
{: .reset-td-br-1 .reset-td-br-2}

### Divider

Refer to the following table for details on the `Divider` editor block.

| properties | description |
|---|---|
|`Transparent`| If enabled, 'line' and 'width' options are removed. |
|`Line `| The different line formats, whether dotted, spotted, or solid.  In addition, you can modify the thickness and color of the divider line|
|`Width `| Adjusts the spread of the divider in increments of 5  |
|`Align`| Moves the line to be either left, center, or right-oriented |
{: .reset-td-br-1 .reset-td-br-2}

### HTML

Refer to the following table for details on the `HTML` editor block.

| properties | description |
|---|---|
|`html editor`| Enter the raw HTML |
{: .reset-td-br-1 .reset-td-br-2}

### Menu

Refer to the following table for details on the `Menu` editor block.

| properties | description |
|---|---|
|`Configure menu items`| Add a menu item. |
|`Font Family`| The style to be used for your menu. |
|`Font Size`| The size of your menu. |
|`Text Color`| Modifies the color of the menu. |
|`Link Color`| Modifies the color of the menu text. |
|`Align`| Moves the menu to be left, center or right-oriented. |
|`Letter spacing`| Modifies the distance in between each character. |
|`Layout`| Determines the layout to be either horizontal or vertical. |
|`Separator`| Add character(s) between the menu options. |
|`Mobile menu`| Includes options to modify the icon size, color, and icon type when shown on a mobile device. |
|`Item padding`| Modifies the padding by using either the **+** or **-** button, or by entering a specific number. |
|`All sides`| Sets a consistent padding number if `Item padding` is disabled. |
{: .reset-td-br-1 .reset-td-br-2}

### Spacer

Refer to the following table for details on the `Spacer` editor block.

| properties | description |
|---|---|
|`height`| Adjusts the height of the spacer block. The default is 60px.|
{: .reset-td-br-1 .reset-td-br-2}

### Add Liquid personalization

Refer to the following table for details on `Add Personalization`.

| name | description |
|---|---|
| `Add Personalization` | Allows you to lookup standard Liquid snippets such as default attributes, custom attributes, Content Blocks, and more. | 
{: .reset-td-br-1 .reset-td-br-2}
