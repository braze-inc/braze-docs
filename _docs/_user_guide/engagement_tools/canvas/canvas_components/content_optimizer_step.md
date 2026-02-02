---
nav_title: Content Optimizer
article_title: Content Optimizer agent step 
alias: "/content_optimizer_step/"
page_order: 5
description: "The Content Optimizer agent step lets you configure and test multiple versions of content components within a single step. It helps you experiment with content variations and automatically optimizes toward the best-performing combinations over time."
page_type: reference

---

# Content Optimizer agent step

> The Content Optimizer agent step lets you configure and test multiple versions of content components within a single step. It helps you experiment with content variations and automatically optimizes toward the best-performing combinations over time. For an introduction, see [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer is currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Creating a Content Optimizer step

For best results, use the Content Optimizer agent in Canvases where users enter the step gradually over time. If all users enter the step at once, the agent won’t have time to learn from early results. 

### Step 1: Add a step

Drag and drop the **Content Optimizer** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Content Optimizer**.

### Step 2: Create your base message

The base message is the starting point for your step. Variants for each content component are dynamically inserted based on the combinations defined in the **Content Optimizer Settings** tab. 

{% alert note %}
During the beta period, email is the only supported channel. 
{% endalert %}

From the **Messaging Channels** tab, select **Email** and create your base email message. Refer to our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section for help. 

The Content Optimizer agent will use the send settings (such as the email domain and reply-to address) specified in this variant to send all messages. You can either start with a new design or select an existing template for this message. At this step, it may be helpful to consider which components of the message you want to optimize for. You will define these in [step 4](#step-4).

Supported components to optimize include:

- Subject
- Body Header
- Body Content
- Primary CTA

### Step 3: Specify delivery settings

In the Delivery Settings tab, you can specify if the step should use Intelligent Timing or delivery validations. For more details, refer to [Edit delivery settings]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) in Message step.

### Step 4: Add content components and variants {#step-4}

Content components are the individual elements of your message that you want to test—such as different subject lines, headlines, body text, or primary calls to action. These components allow you to generate multiple versions of a message and automatically optimize based on performance over time.

You can add up to 3 content components per step and up to 5 variants per component, for a total of 125 unique content combinations.

![Options for adding and configuring content components in the Content Optimizer interface. The interface displays selectable components such as Subject, Body Header, Body Content, and Primary CTA, each with fields to enter different variants.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Step 4a: Configure content components

To configure components:

1. Go to the **Content Optimizer Settings** tab.
2. Choose which components you want to optimize. Supported options:
  - Subject
  - Body Header
  - Body Content
  - Primary CTA
3. For each selected component, define a set of alternative versions of that content (variants). Use clear, distinct variants that differ in tone, structure, or content. This helps Content Optimizer identify top performers more effectively. You can:
  - Write your own variants manually.
  - Use AI-generated suggestions to explore new options quickly.

![Content Optimizer Settings interface showing options to add and configure content components for email optimization. Each component has input fields for entering different variants. Visible text includes component names and fields for entering variant text.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Step 4b: Add Liquid to your message

After defining at least two variants for each component, copy the associated Liquid tag for each one and paste it into the corresponding location in your base message.

- For example, if you're optimizing the subject line, paste the {% raw %}`{% message_component "Subject" %}`{% endraw %} tag in the subject field of the email composer.
- You can also include component tags inside longer text to test just a portion of the component. For example: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options for adding and configuring content components such as Subject, Body Header, Body Content, and Primary CTA. Each component has fields for entering different variants.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

If you don’t add a Liquid tag for a selected content component, you’ll see a warning on the **Content Optimizer Settings** tab and an error on the **Messaging Channels** tab. The Canvas can’t be launched until all selected components are properly added to your base message.

As the Canvas runs, the agent will mix and match variants across components to generate different content combinations. Over time, higher-performing combinations are prioritized for delivery, helping you improve performance without manual intervention.

#### Liquid reference

| Component | Liquid snippet |
| --- | --- | 
| Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 5: Select optimization event

The optimization event determines how the Content Optimizer agent evaluates performance and allocates traffic to content combinations over time. 

For email, you can optimize for one of the following events. The agent uses opens and clicks that are registered within 7 days of sending a message to shift delivery toward higher-performing content combinations.

| Event | Description | Use cases |
| --- | --- | --- |
| Opens | Optimizes for combinations that get recipients to open the email. | Testing subject lines or aiming to increase visibility |
| Clicks | Optimizes for combinations that drive engagement with links. Does not include bot clicks or Braze-recognized unsubscribe clicks. | Driving traffic, engagement, or conversion from links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Your selected optimization event applies to all content components in this step. 

## Analytics

To review performance, open the step-level analytics panel to see metrics by content variant and overall combination performance. The Content Optimizer step uses the same analytics as the Message step. For details, see [Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics) in Message step.  

## Troubleshooting

| Issue | Description | Fix |
| --- | --- | --- |
| Missing Liquid tags | If you add a content component (such as Subject or CTA) but don’t insert the corresponding Liquid tag into your base message, you’ll see: <br>- A warning on the **Content Optimizer Settings** tab <br>- An error on the **Messaging Channels** tab | Copy the Liquid snippet shown under each component in the **Content Optimizer Settings** tab and paste it into the appropriate part of your message. |
| Orphaned Liquid tags | If you delete a content component but leave its Liquid tag in the base message, the message may not render as expected when sent. | Remove any unused `message_component` tags from your base message before launching. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

