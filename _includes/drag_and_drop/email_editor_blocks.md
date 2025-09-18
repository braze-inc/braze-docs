## Using email editor blocks

Editor blocks are located under the **Content** section for email messages. To use an editor block, drag an editor block inside a column in the drag-and-drop editor. It will auto-adjust to the column width. Each editor block has its owns settings, such as granular control on padding.

For more information on how to use and customize these editor blocks in your email, check out [Other customizations]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#other-customizations).

{% alert tip %}
You can also add [custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) to any URL within the `Image`, `Button`, or `Text` editor blocks.
{% endalert %}

## Types

The following table describes how users can use each editor block type.

| Name | Description |
|---|---|
|Title| Adds text with H1, H2, and H3 tags for email. | 
|Paragraph| Enters text into their message. A toolbar helps with font and text editing functionality. | 
|List| Adds a bulleted list. |
|Button| Adds a standard button. Properties for this block allow for editing and setting links easily. | 
|Divider| Inserts a solid, dotted, or dashed line to help with spacing.|
|Spacer| Adds space, or "padding", between other blocks. |
|Image| Inserts an image from the [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). | 
|Video| Creates a link to the video content. |
|Social| Inserts social media platform icon. Custom images can be uploaded for brand specific icons. |
|Icons| Inserts an icon. Custom images can be uploaded. An oversized placeholder icon will be used until an image is uploaded. |
|HTML| Inserts raw HTML. Recommended for [Liquid]({{site.baseurl}}/liquid/), such as Connected Content or conditional statements. | 
|Menu| Creates a flexible menu for the message you're designing. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Properties

Details for each editor block's properties are provided in the following tables.

### Title
Refer to the following table for details on the `Title` editor block properties.

| Properties | Description |
|---|---|
|Title| Selects the heading style. Only H1, H2, or H3 are available. | 
|Font family| This is the font style for your title. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|Line height| Modifies the distance between lines of text. |
|Line spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paragraph

Refer to the following table for details on the `Paragraph` editor block properties.

| Properties | Description |
|---|---|
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|Paragraph spacing| Modifies the space between paragraphs. |
|Line height| Modifies the distance between lines of text. |
|Letter spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### List

Refer to the following table for details on the `List` editor block properties.

| Properties | Description |
|---|---|
|List type| This is the type of list. Can be either bulleted or numbered. |
|List style type| Determines the style of your list. |
|Start list from| Determines the starting number for your list. |
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|List items spacing| Modifies the space between list items. |
|List items indent| Modifies the indentation of list items. |
|Line height| Modifies the distance between lines of text. |
|Letter spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Divider

Refer to the following table for details on the `Divider` editor block.

| Properties | Description |
|---|---|
|Transparent| If enabled, 'line' and 'width' options are removed. |
|Line| The different line formats, whether dotted, spotted, or solid. In addition, you can modify the thickness and color of the divider line. |
|Width | Adjusts the spread of the divider in increments of 5.  |
|Align| Moves the line to be either left, center, or right-oriented. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

Refer to the following table for details on the `Spacer` editor block.

| Properties | Description |
|---|---|
|Height| Adjusts the height of the spacer block. The default is 60px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

Refer to the following table for details on the `Image` editor block. For dynamic images (images with Liquid), you must set a fallback image to use the auto-width settings. For image specifications, refer to our [email image specifications]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#email).

| Properties | Description |
|---|---|
|Auto Width| Modifies the width of the image in pixels. |
|Align| Orients the image to either the left, center or right of the block. |
|Image with Liquid| Use [Liquid]({{site.baseurl}}/liquid/) logic to dynamically set different images within the same block of content. |
|URL| Set an image using the address to where it's hosted. |
|Alternate text| A short description of the image that gives users the same information that's shown in the image. This is essential for screen-reader accessability or when the image fails to load. |
|Image with Rounded Corners| Render the image with rounded corners. By default, images are rendered with squared corners. |
|Action| Triggers an action when the user clicks the image.|
|Block Options| Sets padding around the image block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
For `Auto Width`, automatic image resizing picks the best size for the image based on a combination of image width and available space in the layout:
- Images wider than the available space will be set at 100% width and will keep this ratio on mobile, using the entire device display width.
- Images smaller than the available space will use the image's natural size to avoid distortion effects or blurry pictures.
{% endalert %}

### Video

Refer to the following table for details on the `Video` editor block.

| Properties | Description |
|---|---|
|URL| The URL for the video. |
|Title| Auto-generated from the video meta data or can be customized. Note that only YouTube and Vimeo are supported. |
|Play Icon Style| Includes different options for the play button located at the top of a video image. |
|Play Icon Color| Option to select either **Light** or **Dark** for the play button. |
|Play Icon Size| Choose the pixel size for the play button. Pre-fixed range from 50&nbsp;px to 80&nbsp;px (incremented by 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Videos hosted by Vimeo will only work if they are set to public. All other security settings available within Vimeo (for example, "Hide from Vimeo.com") will generate a different link format that is not supported by this Content Block. These types of links are altered by the builder, which prevents Braze from generating a thumbnail.
{% endalert %}

### Social

Refer to the following table for details on the `Social` editor block.

| Properties | Description |
|---|---|
|Select icon collection| Sets the style of your icon collection. |
|Configure icon collection| Sets the URL for each social icon. Includes the **More options** toggle to edit the title and alternative text. |
|Align| Moves the social icon to be left, center, or right-oriented. |
|Icon spacing| Determines the spacing between each social icon. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Icons

Refer to the following table for details on the `Icons` editor block.

| Properties | Description |
|---|---|
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the icon to be left, center, or right-oriented. |
|Letter spacing| Modifies the distance in between each character. |
|Icon size| Determines the size of your icon. |
|Icon spacing| Modifies the space of the icon. |
|Icon padding| Modifies the padding of the icon. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

Refer to the following table for details on the `HTML` editor block.

| properties | description |
|---|---|
|html editor| Enter the raw HTML. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menu

Refer to the following table for details on the `Menu` editor block.

| Properties | Description |
|---|---|
|Configure menu items| Add a menu item. |
|Font Family| The style to be used for your menu. |
|Font Size| The size of your menu. |
|Text Color| Modifies the color of the menu. |
|Link Color| Modifies the color of the menu text. |
|Align| Moves the menu to be left, center, or right-oriented. |
|Letter spacing| Modifies the distance in between each character. |
|Layout| Determines the layout to be either horizontal or vertical. |
|Separator| Add character(s) between the menu options. |
|Mobile menu| Includes options to modify the icon size, color, and icon type when shown on a mobile device. |
|Item padding| Modifies the padding by using either the **+** or **-** button, or by entering a specific number. |
|All sides| Sets a consistent padding number if Item padding is disabled. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

You can assign an action that occurs when a user taps a button, link, or image in the message. You can also use [Liquid]({{site.baseurl}}/liquid/) to personalize the actions. Details for each editor block's actions are provided in the following tables.

### Button

Refer to the following table for details on the `Button` editor block.

| Properties | Description |
|---|---|
|Link Type| Determines the action when clicking the button and sets the appropriate protocol. |
|URL| Dynamic based on the **Open web page** link type.|
|Mail to, Subject, and Body| For the **Send email** link type, this sets the receipent email address, subject, and content that will populate in a draft email when the user selects the button.|
|Tel| For the **Make call** and **Send SMS** link type, this sets the phone number the user will call or text when selecting the button.|
|Message| For the **Send SMS** link type, this sets the content that will populate in a draft SMS message when the user selects the button.|
|Button options| Sets various button options, such as font, width, color, and others.|
|Button Hover| The style of the button when a user hovers over it using a mouse or trackpad. This includes the button's background color, font color, and border styles.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }