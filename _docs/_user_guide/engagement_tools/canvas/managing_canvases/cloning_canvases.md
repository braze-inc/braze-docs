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

To clone your Canvas, first go to the Canvas dashboard. Next, identify the Canvas you want to create a copy of in the Canvas Flow workflow. You can clone Canvases with a **Draft**, **Active**, or **Stopped** status. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** and select **Clone to Canvas Flow**.

![][1]{: style="max-width:25%;"}

Next, enter the name for your new Canvas and click **Clone to Canvas Flow**. 

![][2]{: style="max-width:70%;"}

Now, you’ll have two versions of your Canvas: the original Canvas and the Canvas Flow version. Your original Canvas will still have its original status, and the cloned Canvas will have a **Draft** status. You can still access the original Canvas, but Braze recommends using the Canvas Flow workflow to continue building your Canvases.

Note that if you clone an active Canvas, Braze will continue to send users through the original Canvas. We recommend stopping a Canvas before cloning to avoid sending duplicate messages to users from both Canvases.

![Canvas dashboard with two Canvases listed: V2 Copy of Canvas V1 and Canvas V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas Flow workflow.][3]

You've completed cloning your Canvas into the Canvas Flow workflow. Now, you can continue building your Canvases in this updated experience!

## Limitations

If a Canvas has full steps that have exception events and uses the delay filter "in" or "on the next", then it can't be cloned to Canvas Flow. 

In order for a Canvas with branching to be cloned to Canvas Flow, all of the following has to be true:
- Delay conditions of the branch are the same
- Audience section is not empty
- No exception events are used
- The variant branches into multiple full steps (no full steps branch into multiple steps)

Otherwise if a Canvas has branching and the aforementioned conditions are not meant, the Canvas can't be cloned to Canvas Flow.

For more information about the differences between the original Canvas editor and Canvas Flow experience, check out [Canvas FAQs]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


[1]: {% image_buster /assets/img_archive/clone_to_v2_workflow.png %}
[2]: {% image_buster /assets/img_archive/clone_to_v2_modal.png %}
[3]: {% image_buster /assets/img_archive/clone_to_v2_dashboard.png %}
