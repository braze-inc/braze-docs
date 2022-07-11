---
nav_title: Cloning Canvases
article_title: Cloning Canvases
page_order: 0
alias: "/cloning_canvases/"
description: "This reference article describes how to clone a Canvas from the original Canvas editor into the Canvas Flow workflow."
tool: Canvas

---

# Cloning Canvases to Canvas Flow

By switching to the Canvas Flow workflow, you gain access to lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components), [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/), and [post-launch editing]({{site.baseurl}}/post-launch_edits). If you have an existing Canvas from the original editor, you can clone this Canvas to create a copy in Canvas Flow. Your original Canvas will not be altered or deleted.

{% alert note %}
You can only clone Canvases with a **Stopped** status. After cloning, the new Canvas will have a **Draft** status. 
{% endalert %}

To clone your Canvas, first go to the Canvas dashboard. Next, identify the Canvas you want to create a copy of in the Canvas Flow workflow. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** for the Canvas and select **Clone to Canvas Flow**. 

To clone your Canvas, first go to the Canvas dashboard. Next, identify the Canvas you want to create a copy of in the Canvas Flow workflow. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** and select **Clone to Canvas Flow**.

![][1]{: style="max-width:25%;"}

Next, enter the name for your new Canvas and click **Clone to Canvas Flow**. 

![][2]{: style="max-width:70%;"}

Now, you’ll have two versions of your Canvas: the original Canvas and the Canvas Flow version. Your original Canvas will still have a **Stopped** status, and the cloned Canvas will have a **Draft** status. You can still access the original Canvas, but Braze recommends using the Canvas Flow workflow to continue building your Canvases.

![Canvas dashboard with two Canvases listed: V2 Copy of Canvas V1 and Canvas V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas Flow workflow.][3]

You've completed cloning your Canvas into the Canvas Flow workflow. Now, you can continue building your Canvases in this updated experience!

## Limitations

If your Canvas matches any of the following details, then your Canvas can't be cloned to Canvas Flow:

- Status is **Active** 
- Status is **Draft**
- Has full steps that have exception events and use the delay filter "in" or "on the next"
- Has a full step that branches out into multiple steps, and is not the first step of the Canvas

For more information about the differences between the original Canvas editor and Canvas Flow experience, check out [Canvas FAQs]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


[1]: {% image_buster /assets/img_archive/clone_to_v2_workflow.png %}
[2]: {% image_buster /assets/img_archive/clone_to_v2_modal.png %}
[3]: {% image_buster /assets/img_archive/clone_to_v2_dashboard.png %}