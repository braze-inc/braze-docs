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

{% alert tip %}
You can also [add custom attributes]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details/) to any URL within the `Image`, `Button`, or `Text` editor blocks.
{% endalert %}

## Types

The following table describes how users can use each editor block type.

| name | description |
|---|---|
|`Title`| Adds text with H1, H2, and H3 tags for email. | 
|`Text`| Enters text into their message. A toolbar helps with font and text editing functionality. | 
|`Image`| Inserts an image from the Media Library. | 
|`Button`| Adds a standard button. Properties for this block allow for editing and setting links easily. | 
|`Divider`| Inserts a solid, dotted, or dashed line to help with spacing.|
|`HTML`| Inserts raw HTML. Great for advanced Liquid such as Connected Content or conditional statements. | 
|`Menu`| Creates a flexible menu for the message you're designing. |
|`Spacer`| Adds space, or "padding", between other blocks. |
|`Social Icon`| Inserts social media platform icon. Custom images can be uploaded for brand specific icons. An oversized placeholder icon will be used until an image is uploaded. |
| `Video` | Creates a link to the video content. |
{: .reset-td-br-1 .reset-td-br-2} 

## Properties

Details for each editor block's properties are provided in the following tables.

### Title

| properties | description |
|---|---|
|`Title`| Selects the heading style. Only H1, H2, or H3 are available. | 
|`Font family`| This is the font style for your title. |
|`Font weight`| This is the overall boldness of the font. |
|`Font size`| Determines the size of your text. |
|`Text color`| Modifies the color of the title. |
|`Link color`| Modifies the color of the link. |
|`Align`| Moves the title to be left, center or right-oriented. |
|`Line height`| Modifies the distance between lines of text. |
|`Line spacing`| Modifies the distance in between each character. |
|`Text direction`| Default left-to-right, but can be edited to be right-to-left. |
{: .reset-td-br-1 .reset-td-br-2}

### Paragraph

Refer to the following table for details on the `Paragraph` editor block properties.

| properties | description |
|---|---|
|`Font family`| This is the font style for your paragraph text. |
|`Font weight`| This is the overall boldness of the font. |
|`Font size`| Determines the size of your text. |
|`Text color`| Modifies the color of the title. |
|`Link color`| Modifies the color of the link. |
|`Align`| Moves the title to be left, center or right-oriented. |
|`Paragraph spacing`| Modifies the space between paragraphs. |
|`Line height`| Modifies the distance between lines of text. |
|`Letter spacing`| Modifies the distance in between each character. |
|`Text direction`| Default left-to-right, but can be edited to be right-to-left. |
{: .reset-td-br-1 .reset-td-br-2}

### List

Refer to the following table for details on the `List` editor block properties.

| properties | description |
|---|---|
|`List type`| This is the type of list. Can be either bulleted or numbered. |
|`List style type`| Determines the style of your list. |
|`Start list from`| Determines the starting number for your list. |
|`Font family`| This is the font style for your paragraph text. |
|`Font weight`| This is the overall boldness of the font. |
|`Font size`| Determines the size of your text. |
|`Text color`| Modifies the color of the title. |
|`Link color`| Modifies the color of the link. |
|`Align`| Moves the title to be left, center or right-oriented. |
|`List items spacing`| Modifies the space between list items. |
|`List items indent`| Modifies the indentation of list items. |
|`Line height`| Modifies the distance between lines of text. |
|`Letter spacing`| Modifies the distance in between each character. |
|`Text direction`| Default left-to-right, but can be edited to be right-to-left. |
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
|`Line`| The different line formats, whether dotted, spotted, or solid.  In addition, you can modify the thickness and color of the divider line. |
|`Width `| Adjusts the spread of the divider in increments of 5.  |
|`Align`| Moves the line to be either left, center, or right-oriented. |
{: .reset-td-br-1 .reset-td-br-2}

### HTML

Refer to the following table for details on the `HTML` editor block.

| properties | description |
|---|---|
|`html editor`| Enter the raw HTML. |
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
|`Height`| Adjusts the height of the spacer block. The default is 60px.|
{: .reset-td-br-1 .reset-td-br-2}

### Social icon

Refer to the following table for details on the `Social Icon` editor block.

| properties | description |
|---|---|
|`Select icon collection`| The style of your icon collection. |
|`Configure icon collection`| Sets the URL for each social icon. Includes the **More options** toggle to edit the title and alternative text. |
{: .reset-td-br-1 .reset-td-br-2}

### Video

Refer to the following table for details on the `Video` editor block.

| properties | description |
|---|---|
|`URL`| The URL for the video. |
|`Title`| Auto-generated from the video meta data or can be customized.  Note that only Youtube and Vimeo are supported. |
|`Play Icon Style`| Includes different options for the play button located at the top of a video image. |
|`Play Icon Color`| Option to select either **Light** or **Dark** for the play button. |
|`Play Icon Size`| Choose the pixel size for the play button. Pre-fixed range from 50 px to 80 px (incremented by 5 px). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Videos hosted by Vimeo will only work if they are set to public. All other security settings available within Vimeo (e.g., "Hide from Vimeo.com") will generate a different link format that is not supported by this content block. These types of links are altered by the builder, which prevents Braze from generating a thumbnail.
{% endalert %}

### Add Liquid personalization

Refer to the following table for details on `Add Personalization`.

| name | description |
|---|---|
| `Add Personalization` | Allows you to lookup standard Liquid snippets such as standard (default) attributes, custom attributes, Content Blocks, and more. | 
{: .reset-td-br-1 .reset-td-br-2}
