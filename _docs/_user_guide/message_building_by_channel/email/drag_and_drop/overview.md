---
nav_title: Overview
article_title: Create a Drag-And-Drop Email
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "This article covers how to set up and properly use the drag-and-drop editor for email messages."
tool: 
  - Campaigns
  - Canvas
---

# Drag-and-drop editor overview

> With the drag-and-drop editor, you can create completely custom and personalized email messages in either campaigns or Canvas using the drag-and-drop editing experience.

{% multi_lang_include video.html id="4dTrkxe8DLo" align="right" %}

Not sure whether your email message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys. 

Once you've selected where to build your message, let's dive into the steps to create a drag-and-drop email! 

## Step 1: Select your template

After selecting the drag-and-drop editor as your editing experience, you can choose to:
- Start with a blank template
- Use a Braze drag-and-drop email template 
- Select a saved drag-and-drop email template

![Basic Drag-and-Drop Email Templates section that shows the option to select a blank template or a Braze template. There is also a section underneath for saved drag-and-drop email templates.][1]

If you want to use your existing custom HTML templates or templates created by a third party, they must be recreated in the drag-and-drop editor. 

You can also access all templates from the **Templates** section.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), templates are under **Templates & Media**.
{% endalert %}

After selecting your template, you'll see an overview of your email where you can edit the sending information and email body, and view any errors or warnings to resolve before sending. Click **Edit Email Body** to begin designing your email structure in the drag-and-drop editor. 

![][8]

## Step 2: Build your email 

The drag-and-drop editing experience is divided into three sections: **Sending Settings**, **Content**, and **Preview & Test**.

Before building your email, it's important to understand the key components to help guide your email building experience.

### Drag and drop email components {#content}

The drag-and-drop editor uses two key components to make email composition quick and easy: **Content** and **Rows**. 

![][10]{: style="float:right;max-width:30%;margin-left:10px;"}
![][9]{: style="float:right;max-width:30%;margin-left:10px;"}

**Content** includes a series of tiles that represent different types of content you can use in your message. These are organized into three categories: basic, media, and advanced. Basic Content Blocks are the foundation of your email such as title and paragraph blocks, buttons, and spacers. Media Content Blocks allow you to include images, videos, social media information, and icons. With the advanced Content Blocks, you can insert HTML blocks or add a menu to your email.

Simply drag one inside an existing row segment, and it will auto-adjust to the column width. Every block in **Content** has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element. For more information, see [Editor Block Properties]({{site.baseurl}}/dnd/editor_blocks/). 

**Rows** are structural units that define the horizontal composition of a section of the message by using columns. Using more than one column allows you to put different content elements side by side. You can add all the structural elements you need to your message, regardless of the template you selected when you started.

The **Settings** panel in the **Design and Build** section includes general settings for the email message. These settings are inherited by the **Content** and **Rows** sections. For example, the **Default Font** set in this section is used everywhere in your message except where you use a custom setting. 

![][11]{: style="width:300px;height:auto;"} 

### Use email content

When you first load into the drag-and-drop editor, you'll see the **Design and Build** tab in the **Content** section of the drag-and-drop editor. This is where you can leverage the [creative details](#creative-details) to the design of your email layout.

1. Select the **Rows** panel. Drag and drop the row configurations into the main editor. This will map the layout of your email content. Note that new configurations must be dragged to the beginning or end of an existing section.
- When you select a row configuration, the **Row Properties** settings appear for further customization for row background colors, images, and custom column sizes.
2. Select the **Content** panel. Drag abd drio the desired content tiles to the row components. 
- You can further refine the tile by selecting the tile and adjusting the fields in **Content Properties** and **Block Options**. This includes editing letter spacing, padding, line height, and more.

As you build your email, you can toggle between a desktop and mobile view to preview how your email messaging will look for your user groups. This will ensure that your content is responsive, and you can make any necessary adjustments along the way. 

{% alert tip %}
Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Copywriter button, located in the Content panel next to Style Settings in the drag-and-drop editor.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Creative details {#creative-details}

{% alert tip %}
You can create a custom theme for your drag-and-drop editor using [global style settings]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

#### Auto width images

Images added to your email will automatically be set to **Auto width**. To adjust this setting, toggle off **Auto width** and adjust the width percentage as needed. 

![Auto width option in the Content tab of the drag-and-drop editor.][2]

#### Color layering

The Drag & Drop Editor allows you to change the color of the email background, content area, and different content components. The color ordering from front to back is content component color, content area background color, and background color. 

![Example of the color layering in the drag-and-drop editor.][3]

#### Content padding

![Block Options for the drag-and-drop editor.][4]{: style="float:right;max-width:25%;margin-left:15px;"}

To adjust padding, scroll down to **Block Options**, and toggle **More Options**. This will allow you to fine-tune your padding to get your email looking just right!
<br>

#### Content background

You can add a background image to your row configuration, allowing you to incorporate more design and content in your email campaign.

#### Adding Liquid 

![Options for adding personalization for the drag-and-drop editor.][5]{: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid is supported in our drag-and-drop editor. To add Liquid into your email, select **Personalization** under **Design / Build**. Here, you can add various personalization types such as standard (default) attributes, device attributes, custom attributes, and more! Next, take your generated Liquid snippet and add it to your email.

##### Dynamic images

You can choose to include dynamic images into your email messaging by including Liquid in your image source attribute. For example, instead of a static image, you can insert {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} as the image URL to include a user's first name in the image. This helps personalize your emails to each user.

Once you've finished designing and building your email message, go to **Sending Settings** to add the sending information.

#### Adding HTML attributes to links

![][6]{: style="float:right;max-width:35%;margin-left:15px;"}

With attributes, you can easily append additional information to HTML tags in emails. These attributes can be applied to links, both in text blocks and buttons, and images. This can be especially useful for message personalization, segmentation, and styling. 

A common use case is to insert an attribute into your anchor tag to disable click tracking when sending through Braze:

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Another common use case is to flag specific links as universal links. Universal links are those that redirect to your app:

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"`, a [custom sub-path](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) must be configured.

## Step 3: Add sending information

The **Sending Settings** section allows you to configure your **From Display Name + Address** and **Reply-To Address** and set the subject line or preheader. Here, you can also see a preview of your message.

{% alert note %}
Advanced functionality will appear in the campaign or Canvas composer. In advanced functionality, you can modify your inline CSS setting and enter in a header or extra key-value pairs (if configured).
{% endalert %}

## Step 4: Test your email

The **Preview & Test** section allows you to preview of your emails across different email clients and devices with **Preview & Test Send** and **Inbox Vision**.

Because you can view three different versions of the same email in the actual editor, in Inbox Vision, and as an actual test email, it's important to align the details across all your platforms. 

### Preview & Test Send

You can also view your email previews with these user types:

- **Random User:** Braze will randomly select a user from the database and preview the email based on their attributes or event information.
- **Select User:** You can select a specific user based on their email address or external ID. The email will preview based on that user's attributes and event information
- **Custom User:** You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.

{% alert note %}
The random user may or may not be part of your segmentation criteria. Segmentation is selected afterward, so Braze is unaware of your target audience at this point.
{% endalert %}

Here, you can also use the **Dark Mode Preview** toggle to preview your email in dark mode and adjust your email as needed.

### Inbox Vision

[Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/) allows you to view your email campaigns from the perspective of email clients and mobile devices. To test your email message using Inbox Vision, select **Inbox Vision** in the **Preview & Test** section and click **Run Inbox Vision**. 

{% alert tip %}
Background images in email messaging may sometimes cause white lines or disconnects to appear between images, so it's important to test and check the finer details of your email message.
{% endalert %}

After using the Drag-and-Drop Editor to design and create your email message, continue to [build][12] the remainder of your campaign or Canvas.

### Updated HTML engine

The underlying engine that produces HTML from the  Drag-and-Drop Editor has been optimized and updated, resulting in benefits related to HTML file compression and rendering.

#### File compression

Our average exported HTML data footprint size has been reduced, leading to faster loading and rendering, reduced mobile clipping, and reduced bandwidth consumption.

#### HTML rendering

HTML rendering has improved based on these following updates that minimize the number of conditional comments and CSS media queries. As a result, HTML files are smaller and more efficiently coded. 

- Migration from a `<div>` element-based design to a standard `<table>` formatted codebase
- [Editor blocks][7] have been re-coded for conciseness
- Final HTML code is compressed to remove whitespace between tags
- Transparent dividers are automatically converted into content padding

[1]: {% image_buster /assets/img/dnd/dnd_template1.png %}
[2]: {% image_buster /assets/img/dnd/dnd1.png %}
[3]: {% image_buster /assets/img/dnd/dnd2.png %}
[4]: {% image_buster /assets/img/dnd/dnd3.png %}
[5]: {% image_buster /assets/img/dnd/dnd4.png %}
[6]: {% image_buster /assets/img/dnd_custom_attributes.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/
[8]: {% image_buster /assets/img/dnd/dnd_emailvariant.png %}
[9]: {% image_buster /assets/img/dnd/dnd_content.png %}
[10]: {% image_buster /assets/img/dnd/dnd_rows.png %}
[11]: {% image_buster /assets/img/dnd/dnd_contentsettings.png %}
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/
