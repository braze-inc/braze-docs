---
nav_title: WhatsApp Template Builder
article_title: WhatsApp Template Builder
description: "This reference article covers the WhatsApp Template Builder."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp Template Builder

> The WhatsApp Template Builder lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you'd like.

{% alert note %}
The WhatsApp Template Builder is currently in early access. Contact your Braze account manager for access.
{% endalert %}

## Prerequisites

Before creating a WhatsApp template in Braze, complete the [WhatsApp setup](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/).

## Create a template

### Step 1: Create a template

Go to **Templates** > **WhatsApp Templates**, then select **Create new template**.

![WhatsApp templates page with button to create a new template.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Step 2: Configure template settings

Fill in the following fields:

| Field | Description |
| ----- | ----- |
| **Account** | The WhatsApp Business Account (WABA) you’d like to submit the template to. All subscription groups and phone numbers within a WABA will share template access. |
| **Language** | The language for this template. WhatsApp requires a separate template for each language. |
| **Template name** | A unique name for your template. Template names can only contain lowercase letters, numbers, and underscores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 3: Choose a layout

Under **Layout**, select the template type:

- **Default:** A standard WhatsApp message. This is the layout covered in this article.  
- **Carousel:** A message with horizontally scrollable cards. Refer to [Carousel templates]({{site.baseurl}}/whatsapp_carousel_templates/) for details.

### Step 4: Build your template

#### Header (optional)

Add a header to appear above the message body. You can choose:

- **Text:** A short text header.  
- **Media:** An image, video or document (URL only). Braze will store the media reference and submit a sample to Meta for approval.  
- **None:** No header 

#### Body

Enter the main content of your message. You can personalize the body using Liquid or generic variables:

{% raw %}
- Use Liquid tags (for example, `{{${first_name}}}`). Braze saves your Liquid and surfaces it when you use the template in a campaign or Canvas composer.  
- Use generic variables, such as numbered placeholders (for example, `{{1}}`), if you prefer to add personalization later when building your message.
{% endraw %}

You can add personalization wherever the **+** plus button appears. Not all fields support personalization.

#### Footer (optional)

Add a short footer to appear below the message body.

#### Buttons (optional)

Add up to 10 buttons to your template. Button types have different character limits; Braze displays your remaining character count as you add buttons.

![WhatsApp template composer with quick reply and call to action buttons.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Step 5: Preview your template

Before submitting, preview how your message will appear to recipients:

- **Preview as a user:** See a generic preview of the message.  
- **Preview as a specific user:** Select a user profile to preview how the template will render with that user's data.

{% alert note %}
Templates must be approved by Meta before they can be sent. After approval, you can test the template within campaigns and Canvases.
{% endalert %}

### Step 6: Submit for review

Select **Submit** to send your template to Meta for review, which typically takes around five minutes but can take up to 24 hours. The template appears on your **WhatsApp templates** page when it's submitted, and the status will be updated on refresh of the **WhatsApp templates** page.

## Supported template categories

At this time, only Marketing templates are available in the WhatsApp Template Builder.

## Use an approved template in a campaign

After Meta approves your template, you can use it in a WhatsApp campaign or Canvas.

1. Go to **Campaigns** and select **Create Campaign** > **WhatsApp**.  
2. In the message composer, select your approved template.  
3. Braze will automatically populate the template's content—including any media and Liquid you entered during template creation—so you don't have to re-enter it.  
4. Update any variable content or personalization as needed. Fields locked by Meta (shown in gray) cannot be edited. To change locked content, you'll need to edit and resubmit the template for approval.  
5. Use the **Test** tab to preview the message, update body variables, and confirm the message looks as expected before launch.

For more details on building WhatsApp campaigns, refer to [Create a WhatsApp message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/).

## Frequently asked questions

### How long does Meta template review take?

Reviews typically complete within five minutes, but can take up to 24 hours.

### Can I edit a template after it's been approved? 

Any changes to locked content (body copy or other Meta-controlled fields) require resubmitting the template for approval, which must be done from the WhatsApp Business Manager. Variable content and personalization can be updated when building your campaign or canvas.

### What happens to templates I submitted before the Template Builder was available?

Templates created in Meta Business Manager are still available to use in Braze. The Template Builder is an additional way to create and manage templates without leaving the Braze dashboard.

### Why can't I add personalization to every field?

Meta restricts which parts of a template can be personalized. The **+** plus button only appears in fields that support variable content.