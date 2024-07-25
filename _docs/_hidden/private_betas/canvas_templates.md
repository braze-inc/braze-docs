---
nav_title: Canvas Templates
article_title: Canvas Templates
permalink: "/canvas_templates/"
description: "This reference article covers how to create a template for Canvas."
page_type: reference
---

# Creating a Canvas template

> This reference article covers how to create and manage templates for Canvas. Using templates can refine your messaging by creating a consistent framework that can be easily customized to fit your specific goals across your Canvases.

{% alert important %}
Canvas templates are currently in early access. Contact your customer success manager if you're interested in participating in this early access.<br><br>
WhatsApp and push notifications with action buttons are not yet supported in Canvas templates.
{% endalert %}

## Method 1: Create from an existing Canvas

### Step 1: Select your existing Canvas

In the Braze dashboard, go to **Messaging** > **Canvas** and select an existing Canvas you want to use as a template.

### Step 2: Create your template

In the Canvas editor, select **Edit Canvas** or **Edit draft**, depending on if your Canvas is active or in a draft. Expand the **Save as draft** dropdown in the footer and select **Save as template**.

![][2]

### Step 3: Save your template

Next, give your template a name and add any relevant tags. Then, select **Save**. Your template is now ready to use for building a Canvas, giving you a head start with your basic settings and steps already in place.

## Method 2: Create via Canvas template editor

### Step 1: Go to the Canvas template editor

In the Braze dashboard, go to **Templates** > **Canvas Templates**.

{% alert note %}
If you are using the older navigation, you can find this page under **Engagement** > **Templates & Media** > **Canvas Templates**.
{% endalert %}

### Step 2: Create a new template

Select **Create template** and begin setting up your Canvas details. You can start by giving your Canvas template a name.

![An example Canvas template named "Annual sale Canvas template" with the description "Use for annual spring promotion".][1]

### Step 3: Customize your template

Next, customize your template by [setting up your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). You can decide when users should enter the Canvas, determine which users can enter this Canvas, adjust your send settings, and build your user journey for the template.

### Step 4: Save your template

After you've finished customizing your template, select the **Save template** button. On the **Canvas template** page, you can view your Canvas template details by selecting <i class="fas fa-list"></i> **Template details**. 

## Using Canvas templates

There are two ways to use your template when composing a Canvas:
- **From Messsaging**: Go to **Messaging** > **Canvas**. Select the **Create Canvas** button and **Use a Canvas Template**.
- **From Templates**: Go to **Templates** > **Canvas Templates** and find your desired template. Then, select the <i class="fas fa-ellipsis-vertical"></i> menu followed by **Apply template**. This will bring you to a new Canvas with the template applied in the Canvas composer.

## Managing Canvas templates

Canvas templates can be duplicated and archived, similar to an actual Canvas. To edit a Canvas template, select the template then **<i class="fas fa-pencil-alt"></i>Edit**.

At a workspace level, you can update user permissions to allow or limit the access to create, edit, view, or archive Canvas templates. These permissions are not yet available for [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams).

[1]: {% image_buster /assets/img/canvas_template_example.png %}
[2]: {% image_buster /assets/img/save_canvas_as_template.png %}