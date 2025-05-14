---
nav_title: "Email Love"
article_title: Email Love
description: "Learn how to integrate Braze with Email Love, a Figma plugin that enables you to design and export responsive and accessible HTML emails directly from Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) is a Figma plugin that empowers you to design and export responsive and accessible HTML emails directly from Figma. Email Love’s Export to Braze feature uses the Braze API to seamlessly upload your email templates to Braze.

## Prerequisites

| Requirement            | Description                                                      |
|------------------------|------------------------------------------------------------------|
| **Email Love account** | An Email Love account is required to take advantage of this partnership. |
| **Braze REST API key** | A Braze REST API key with full `Templates` permission enabled. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Using Email Love with Braze

### Step 1: Run the plugin

To design your email template, you'll first need to load the plugin. For more detailed instructions, refer to Email Love’s documentation for [uploading your email to Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Step 2: Create your first frame

In the plugin, select the **[+ No Template Selected]** button to create a new frame for your email design.

### Step 3: Design the template with Email Love's pre-built components

Select the frame you created and begin adding components (headers, content blocks, CTAs, and footers) from the plugin’s **Assets** library to structure your email.

![Email Love's pre-built components.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Step 4: Customize the Components

Modify components using Figma's tools to adjust your text, images, colors, and layout elements to align the template's design with your brand. If you add a footer component, a Braze unsubscribe link will automatically be included when you export.

![Customize compoments in Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Step 5: Export your email template to Braze

1. When you're finished, select the frame you want to export. Note that you'll need to use an Email Love footer that contains an unsubscribe link for the export to work.
2. Select the **Export** button in the plugin and select **Braze** from the dropdown menu.
3. Copy and paste your API key into the **Braze API Key** box within the Email Love Figma plugin.
4. Select the **Set API Key** button.
5. Select **Change Instance ID**, then select your Braze instance ID.

![Exporting a template to Braze from the Email Love plugin.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Step 6: Edit your email in Braze

In Braze, go to **Templates** > **Edit Templates** > **Edit Message**. Inside the template editor, you can either edit your email HTML or use the **Rich Text editor** in the **Classic** tab.

## Support and troubleshooting

For more detailed instructions, refer to Email Love’s documentation on [exporting an email design](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). For additional support, contact the Email Love support team.
