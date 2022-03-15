---
nav_title: Drag & Drop Editor
article_title: Drag & Drop Editor
alias: "/dnd/"
channel: email
page_order: 1
description: "This reference article covers various creative details of Drag & Drop editor blocks."
tool: 
  - Campaigns
  - Canvas
  
---

# Drag & Drop Editor

{% include video.html id="4dTrkxe8DLo" align="right" %}

> With the Drag & Drop Editor, you can create completely custom and personalized email messages in either Campaigns or Canvas using the drag & drop editing experience.

## Create a drag & drop email

Not sure whether your email message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys. 

Once you've selected where to build your message, let's dive into the steps to create a drag & drop email! 

### Step 1: Select your template

After selecting the Drag & Drop Editor as your editing experience, you can choose to:
- Build a new template
- Use a Braze drag & drop email template 
- Select a saved drag & drop email template

![Basic Drag and Drop Email Templates section that shows the option to select a blank template or a Braze template. There is also a section underneath for saved drag and drop email templates.][1]

If you want to use your existing custom email templates, they must be recreated in the Drag & Drop Editor. 

{% alert tip %}
You can also access all templates in the **Templates & Media** page under the **Engagement** section.
{% endalert %}

After selecting your template, you'll see an overview of your email where you can edit the sending information and email body, and view any errors or warnings to resolve before sending. Click **Edit Email Body** to begin designing your email structure in the Drag & Drop Editor! 

![][8]

### Step 2: Build your email 

The drag & drop editing experience is divided into three sections: **Sending Settings**, **Content**, and **Preview & Test**.

Before building your email, it's important to understand the key components to help guide your email building experience.

#### Email content {#content}

![][10]{: style="float:right;max-width:25%;margin-left:10px;"}
![][9]{: style="float:right;max-width:25%;margin-left:10px;"}

The Drag & Drop Editor uses two key components to make email composition quick and easy: **Content** and **Rows**. 

**Content** includes a series of tiles that represent different types of content you can use in your message such as a title, text blocks, icons, and spacers. Simply drag one inside an existing row segment, and it will auto-adjust to the column width. 

Every block in **Content** has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element. For more information see [Editor Block Properties]({{site.baseurl}}/dnd/editor_blocks/). 

**Rows** are structural units that define the horizontal composition of a section of the message by using columns. Using more than one column allows you to put different content elements side by side. You can add all the structural elements you need to your message, regardless of the template you selected when you started.

The **Settings** panel in the **Design and Build** section includes general settings for the email message. These settings are inherited by the **Content** and **Rows** sections. For example, the **Default Font** set in this section is used everywhere in your message except where you use a custom setting.

![][11]{: style="width:300px;height:auto;"} 

Once you've selected your template, you'll see the **Design and Build** tab in the **Content** section of the Drag & Drop Editor. This is where you can leverage the [creative details](#creative-details) to the design of your email layout.

1. Select the **Rows** panel. Drag & drop the row configurations into the main editor. This will map the layout of your email content. Note that new configurations must be dragged to the beginning or end of an existing section.
- When you select a row configuration, the **Row Properties** settings appear for further customization for row background colors, images, and custom column sizes.
2. Select the **Content** panel. Drag & drop the desired content tiles to the row components. 
- You can further refine the tile by selecting the tile and adjusting the fields in **Content Properties** and **Block Options**. This includes editing letter spacing, padding, line height, and more.

After you've finished designing and building your email message, go to **Sending Settings** to add the sending information.

### Step 3: Add sending information

The **Sending Settings** section allows you to configure your **From Display Name + Address** and **Reply-To Address** and set the subject line or preheader. Here, you can also see a preview of your message.

{% alert note %}
Advanced functionality will appear in the campaign or Canvas step composer. In advanced functionality, you can modify your inline CSS setting, set a BCC email address, and enter in a header or extra key-value pairs (if configured).
{% endalert %}

### Step 4: Test your email

The **Preview & Test** section allows you to preview of your emails across different email clients and devices. By previewing your email campaign as a user, you can ensure that the details are aligned across all platforms.

{% alert important %}
Inbox Vision for the Drag & Drop Editor is currently in early access. Please contact your Braze account manager if you are interested in participating in early access.
{% endalert %}

You can also view your email previews with these user types:

- **Random User:** Braze will randomly select a user from the database and preview the email based on their attributes or event information.
- **Select User:** You can select a specific user based on their email address or `external_id`. The email will preview based on that user's attributes and event information
- **Custom User:** You can customize a user. Braze will offer inputs for all available attributes and events. You can enter any information you would like to see in the preview email.

{% alert note %}
The random user may or may not be part of your segmentation criteria. Segmentation is selected afterward, so Braze is unaware of your target audience at this point.
{% endalert %}

After using the Drag & Drop Editor to design and create your email message, [build][12] the remainder of your campaign or Canvas.

## Creative details {#creative-details}

### Auto width images

Images added to your email will automatically be set to **Auto width**. To adjust this setting, toggle off **Auto width** and adjust the width percentage as needed. 

![Auto width option in the Content tab of the Drag & Drop Editor.][2]

### Color layering

The Drag & Drop Editor allows you to change the color of the email background, content area, and different content components. The color ordering from front to back is content component color, content area background color, and background color. 

![Example of the color layering in the Drag & Drop Editor.][3]

### Content padding

![Block Options for the Drag & Drop Editor.][4]{: style="float:right;max-width:25%;margin-left:15px;"}

To adjust padding, scroll down to **Block Options**, and toggle **More Options**. This will allow you to fine-tune your padding to get your email looking just right!

### Adding Liquid 

![Options for adding personalization for the Drag & Drop Editor.][5]{: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid is supported in our Drag & Drop Editor. To add Liquid into your email, select **Personalization** under **Design / Build**. 

Here, you can add various personalization types such as default attributes, device attributes, custom attributes, and more! 

Next, take your generated Liquid snippet and add it to your email.

[1]: {% image_buster /assets/img/dnd/dnd_template1.png %}
[2]: {% image_buster /assets/img/dnd/dnd1.png %}
[3]: {% image_buster /assets/img/dnd/dnd2.png %}
[4]: {% image_buster /assets/img/dnd/dnd3.png %}
[5]: {% image_buster /assets/img/dnd/dnd4.png %}
[7]: {site.baseurl}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/
[8]: {% image_buster /assets/img/dnd/dnd_emailvariant.png %}
[9]: {% image_buster /assets/img/dnd/dnd_content.png %}
[10]: {% image_buster /assets/img/dnd/dnd_rows.png %}
[11]: {% image_buster /assets/img/dnd/dnd_contentsettings.png %}
[12]: {site.baseurl}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas