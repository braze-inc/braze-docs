---
nav_title: "Email Love"
article_title: Email Love
description: "Learn how to integrate Email Love with Braze."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love: Figma Plugin for HTML Emails

> [Email Love](https://emaillove.com/) is a Figma Plugin that enables you to design and export responsive and accessible HTML emails directly from Figma.

Email Love’s **Export to Braze** feature uses the Braze API to seamlessly upload your email templates to Braze.

## Prerequisites

| Requirement            | Description                                                      |
|------------------------|------------------------------------------------------------------|
| **Email Love account** | An Email Love account is required to take advantage of this partnership. |
| **Braze REST API key** | A Braze REST API key with full `Templates` permission enabled. |

## Implementation

### Step 1: Running the Plugin

You will now need to load the plugin so that you can use it to design your email template. For more detailed instructions, please refer to [Email Love’s documentation](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Step 2: Creating Your First Frame

Click the **[+ No Template Selected]** button in the plugin interface to create a new frame for your email design.

### Step 3: Designing the Template Using Email Love's Pre-Built Components

Select the frame and start adding components like **headers, content blocks, CTAs, and footers** from the plugin’s Assets library to structure your email.

![Email Love's Pre-Built Components]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Step 4: Customizing the Components

Modify components using Figma’s design tools by adjusting text, images, colors, and layout elements, ensuring the design matches your brand. If a Footer component is added, a Braze Unsubscribe link will be automatically included during export.

![Customize Components]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Step 5: Exporting Your Email to Braze

#### 1. Create Braze API Key:

- Login to your Braze Account and navigate to **Settings > API & Identifiers**.
- Click the **"New API Key"** button.
- Give your API key a name and select **Templates** in the Permissions section. Click **Create API Key.**

#### 2. Export Configuration in Email Love:

- Ensure that your email design is finalized and ready for export, then click on the frame you want to export to ensure it is selected.  
  *Note: You will need to use an Email Love Footer with an Unsubscribe link for the export to work.*
- Click the **Export** button located in the top right corner of the Plugin interface and select **"Braze"** from the dropdown menu.
- Copy and paste your API key into the **"Braze API Key"** box in the Email Love Figma Plugin. Click the **"Set API Key"** button.
- Click **"Change Instance ID"** and select your Braze instance ID.

![Export Template to Braze]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %})

### Step 6: Edit Your Email Inside of Braze

Once you have exported your email, navigate to **Templates > Edit Templates > Edit Message**. Inside the template editor, you will have the option to either edit your email HTML or use a **Rich Text editor** when you click on the **"Classic"** tab.

## Support and Troubleshooting

For more detailed instructions, please refer to [Email Love’s documentation](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). For additional support, contact the Email Love support team.
