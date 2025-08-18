---
nav_title: Creating an Email
article_title: Creating an Email with Drag-and-Drop
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "This article covers how to set up and properly use the drag-and-drop editor for email messages."
tool:
- Campaigns
- Canvas
---

# Creating an email with drag-and-drop

> Using the drag-and-drop editor, you can create completely custom and personalized email messages for either campaigns or Canvases, all without using HTML to build your email body.

## About the editor

The drag-and-drop editor uses [Content](#content) and [Rows](#rows) as the two key components to simplify your workflow, without additional use of HTML.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Content</th>
        <th style="width: 50%;">Rows</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="The 'Rows' tab that includes different structural combinations for your email layout." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="The 'Content' tab that includes basic blocks, media, and advanced" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### Content

**Content** includes a series of tiles that represent different types of content you can use in your message. These are organized into three categories: basic, media, and advanced. 

{% tabs %}
{% tab Basic %}

Basic blocks are the foundation of your email. Using these blocks, you can add any of the following elements into your email body:

- Title
- Paragraph
- List
- Button
- Divider
- Spacer

{% endtab %}
{% tab Media %}

With media blocks, you can add different visual content such as images, videos, social media icons and links, and customizable icons.

{% endtab %}
{% tab Advanced %}

Although the drag-and-drop editor simplifies your workflow with these blocks, you can also use advanced blocks to insert HTML or to add a menu to your email body. Note that using your own HTML may affect how the message is rendered.

{% endtab %}
{% endtabs %}

### Rows

**Rows** are structural units that define the horizontal composition of a section of the message by using columns. You can either empty rows or [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Using more than one column allows you to put different content elements side by side. This way, you can add all the structural elements you need to your message, regardless of the template you selected when you started.

#### Cards Style

**Cards Style** is a row property that lets you add spacing between columns and round their corners. With card-style formatting, you can create more visually engaging layouts to help highlight your most important content, such as new product features, testimonials, special offers, news updates, and more.

## Using the drag-and-drop editor

Not sure whether your email message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

After you've selected where to build your message, let's dive into the steps to create a drag-and-drop email.

### Step 1: Select your template

After selecting the drag-and-drop editor as your editing experience, you can choose to:

- Start with a blank template.
- Use a predesigned Braze drag-and-drop email template.
- Use a saved drag-and-drop email template.

{% alert note %}
To use an existing custom HTML template or templates created by a third party, you must recreate the template by going to **Templates** > **Email Templates** and selecting **Drag-And-Drop Editor** as your editing experience.
{% endalert %}

You can also access all templates from the **Templates** section.

After selecting your template, you’ll see an overview of your email under **Email Variants** that includes the sending information and email body. 

Then, select **Edit Email Body** to begin designing the email structure in the drag-and-drop editor. 

![The "Email Variants" section with an example email body.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Step 2: Build your email

The drag-and-drop editing experience is divided into three sections: **Sending Settings**, **Content**, and **Preview & Test**. The magic of building your email body happens in the **Content** section. Before building your email, it’s important to understand the key components that guide your email-building experience. If you need to review, see [About the editor](#about-the-editor).

When you're ready, use the drag-and-drop content blocks to build your email.

1. Select the **Rows** panel. Drag and drop the row configurations into the main editor. This will map the layout of your email content.
- Note that new configurations must be dragged to the top or bottom of an existing section.
- When you select a row configuration, the **Row Properties** settings appear for further customization of row background colors, images, and custom column sizes.
2. Select the **Content** panel. Drag and drop your desired content tiles to the row components.
- You can also drag any of the **Content** tiles into the main editor. This creates a row for the tile.
- You can further refine the tile by selecting the tile and adjusting the fields in **Content Properties** and **Block Options**. This includes editing letter spacing, padding, line height, and more.

Check out [Other customizations](#other-customizations) for other ways to further customize your drag-and-drop email.

As you build your email, you can toggle between a desktop and mobile view to preview how your email messaging will look for your user groups. This will check that your content is responsive, and you can make any necessary adjustments along the way.

{% alert tip %}
Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description, and the AI will generate human-like marketing copy for use in your messaging.

![Copywriter button, located in the Content panel next to Style Settings in the drag-and-drop editor.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Step 3: Add your sending information

Once you've finished designing and building your email message, it's time to add your sending information in the **Sending Settings** section.

1. Under **Sending Info**, select an email as the **From Display Name + Address**. You can also customize this by selecting **Customize From Display Name + Address**.
2. Select an email as the **Reply-To Address**. You can also customize this by selecting **Customize Reply-To Address**.
3. Next, select an email as the **BCC Address** to make your email visible to this address.
4. Add a subject line to your email. Optionally, you can also add a preheader and a whitespace after the preheader.

{% alert tip %}
You can use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) in the **From Display Name + Address** and **Reply-To Address** fields to dynamically template these based on custom attributes. This allows you to send from different brands, regions, or departments using a single email campaign or Canvas step.
{% endalert %}

A preview in the right-hand panel will populate with the sending information you've added. This information can also be updated by navigating to **Settings** > **Email Preferences** > **Sending Configuration**.

#### Personalizing your email header (advanced)

Under **Sending Settings**, you can add personalization for email headers and email extras, which allows you to send additional data back to other email service providers. Personalizing an email header, such as including a recipient's name, can also contribute to the likelihood of your email being opened.

{% alert note %}
Advanced functionality will appear in the campaign or Canvas composer. In advanced functionality, you can modify your inline CSS setting and enter a header or extra key-value pairs (if configured).
{% endalert %}

### Step 4: Test your email

After adding your sending information, it's time to finally test your email. 

Go to the **Preview and Test** section. Here, you have the option of previewing your email as a user or sending a test message. This section also includes [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), which allows you to check that your email has rendered correctly across different mobile and web clients.

{% alert tip %}
You can also use the **Dark Mode Preview** toggle in the preview panel to view your email body in dark mode and adjust your email as needed. 
{% endalert %}

Because you can view three different versions of the same email in the actual editor, in Inbox Vision, and as an actual test email, it's important to align the details across all your platforms.

#### Preview and test send
 
Under the **Preview as a User** tab, you can select the following user types to preview your message.

- **Random User:** Braze will randomly select a user from the database and preview the email based on their attributes or event information.
- **Select User:** You can select a specific user based on their email address or external ID. The email will be previewed based on that user's attributes and event information
- **Custom User:** You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.

{% alert note %}
The random user may or may not be part of your segmentation criteria. Segmentation is selected afterward, so Braze is unaware of your target audience at this point.
{% endalert %}

You can also select **Copy preview link** to generate and copy a shareable preview link that shows what the email will look like for a random user. The link will last for seven days before it needs to be regenerated. 

Note that any edits made to an email template won't reflect in a previously generated link. You'll need to generate a new link preview to see any edits.

![Email preview with a button to "Copy preview link" and copy the generated link.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Use Inbox Vision

Inbox Vision allows you to view your email campaigns from the perspective of email clients and mobile devices. To test your email message using Inbox Vision, select **Inbox Vision** in the **Preview & Test** section and select **Run Inbox Vision**.

{% alert tip %}
Background images in email messaging may sometimes cause white lines or disconnects to appear between images, so it's important to test and check the finer details of your email message.
{% endalert %}

After using the drag-and-drop editor to design and create your email message, continue to [build]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) the remainder of your campaign or Canvas.

{% details About the updated HTML engine %}
The underlying engine that produces HTML from the drag-and-drop editor has been optimized and updated, resulting in benefits related to HTML file compression and rendering.

Our average exported HTML data footprint size has been reduced, leading to faster loading and rendering, reduced mobile clipping, and reduced bandwidth consumption.

HTML rendering has improved based on the following updates that minimize the number of conditional comments and CSS media queries. As a result, HTML files are smaller and more efficiently coded.
- Migration from a `<div>` element-based design to a standard `<table>` formatted codebase
- [Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) have been re-coded for conciseness
- The final HTML code is compressed to remove whitespace between tags
- Transparent dividers are automatically converted into content padding
{% enddetails %}

## Other customizations

As you continue building drag-and-drop emails, you can further customize each email body by using a combination of these creative details to capture your audience's attention and interest in your message.

{% alert tip %}
You can create a custom theme for your drag-and-drop editor using [global style settings]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Auto-width images

Images added to your email will automatically be set to **Auto width**. To adjust this setting, toggle off **Auto width** and adjust the width percentage as needed.

![Auto width option in the Content tab of the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd1.png %})

### Color layering

Using color layering, you can change the color of the email background, content area, and different content components. The color ordering from front to back is: content component color, content area background color, and background color.

![Example of the color layering in the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd2.png %})

### Content padding

![Block Options for the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

To adjust padding, scroll down to **Block Options** and select **More Options**. You can fine-tune your padding to get your email looking just right.

### Content background

You can add a background image to your row configuration, allowing you to incorporate more design and visual content in your email campaign.

### Language attribute

You can set the language attribute by going to the **Settings** tab and selecting the desired language. You can also target the user attribute {%raw%} `{{${language}}}` {%endraw%} if the message is intended for users with dynamic language values.

![Setting the "Language" value for an email.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalization

![Options for adding personalization for the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid is supported in the drag-and-drop email editor. To add personalization to your email:

1. Select **Personalization** under the **Content** section. 
2. Select the personalization type. This includes default (standard) attributes, device attributes, custom attributes, and more. 
3. Search for the attribute to be added.
4. Copy your generated Liquid snippet and paste it in your email body.

Liquid personalization is not supported for image blocks and button link type fields. 

#### Dynamic images

You can choose to include dynamic images in your email messaging by including Liquid in your image source attribute. For example, instead of a static image, you can insert {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} as the image URL to include a user's first name in the image. This helps personalize your emails to each user.

### Text direction

When composing your message, you can toggle the text direction between left-to-right to right-to-left by selecting the respective **Text direction** button. You might use this option when creating messages in languages like Arabic and Hebrew.

![Email drag-and-drop editor menu with button to toggle text alignment between right-to-left and left-to-right.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

### HTML

#### HTML attributes to links

![The "Attributes" section with the attribute "clicktracking" turned off for a link.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

When using links, buttons, images, and videos in the drag-and-drop editor, select **Add new attribute** under **Attributes** in the **Content** section to append additional information to HTML tags in emails. This can be especially useful for message personalization, segmentation, and styling.

A common use case is to insert an attribute into your anchor tag to disable click tracking when sending through Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Another common use case is to flag specific links as universal links. Universal links are links that redirect to your app, giving your users an integrated experience.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (a [custom sub-path](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) must be configured)

To set up universal links, refer to [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Alternatively, you can integrate with one of our attribution partners, such as [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) or [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), to manage universal links.

Lastly, predefined attributes are available to help make your message accessible. Learn more at our dedicated [Building accessible messages in Braze]({{site.baseurl}}/help/accessibility) article.

#### Custom head tags

Use `<head>` tags to add CSS and metadata in your email message. For example, you can use these tags to add a stylesheet or favicon. Liquid is supported in `<head>` tags.

Anything added outside of `<head>` tags will be added after the `<body>` tag in your email. This means the added content will display in the email.

##### Allowed tags and attributes by tag

| Tag name | Description | Example |
| --- | --- | --- |
| `base` | Specifies the base URL for all relative URLs in the message. | `<base href="https://example.com" target="_blank">` |
| `link`| Defines relationships between the message and external resources. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Provides metadata such as page description or keywords. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Embeds internal CSS styles. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Sets the title of the document shown in browser tabs. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

| Tag | Attribute | Description | Example |
| --- | --- | --- | --- |
| `base` | `href` | Base URL to use for relative URLs. | ```<base href="https://braze.com">``` |
| `base` | `target`| Default target for all hyperlinks and forms. | ```<base target="_blank">``` |
| `link` | `href` | URL to the external resource. | ```<link href="style.css">``` |
| `link` | `rel` | Defines relationships between the current and linked message. | ```<link rel="stylesheet">``` |
| `link` | `type` | Type of linked resource. | ```<link type="text/css">``` |
| `link` | `sizes` | Specifies the sizes of icons. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Specifies the media or device for which styles apply. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Sets the title of the document shown in browser tabs. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Sets the title of the document shown in browser tabs. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Declares the character encoding. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Sets the title of the document shown in browser tabs. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | MIME type of the style content. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Specifies the media or device for which styles apply. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | No attributes | The `title` tag doesn't accept any attributes. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
