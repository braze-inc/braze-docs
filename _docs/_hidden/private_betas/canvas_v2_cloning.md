---
nav_title: Cloning Canvases
permalink: "/cloning_canvases/"
hidden: true
---

# Cloning Canvases

Moving to the Canvas V2 workflow includes benefits such as access to lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components), [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/), and [post-launch editing]({{site.baseurl}}/post-launch_edits). With the Canvas cloning tool, you can create a copy of your Canvas in the Canvas V2 workflow. When you clone your Canvas to the Canvas V2 workflow, your original Canvas will not be altered or deleted. 

{% alert note %}
You can only clone Canvases with a **Stopped** status. After cloning, the new Canvas V2 will have a **Draft** status. 
{% endalert %}

To clone your Canvas, first go to the Canvas dashboard. Next, identify the Canvas you want to create a copy of in the Canvas V2 workflow. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** for the Canvas and select **Clone to V2 Workflow**. 

![][1]{: style="max-width:25%;"}

Next, enter the name for your new Canvas and click **Clone to V2 Workflow**. 

![][2]{: style="max-width:70%;"}

Now, you'll have two versions of your Canvas: the original Canvas and the V2 version. Your original Canvas will still have a **Stopped** status, and the cloned Canvas will have a **Draft** status. You can still access the original Canvas, but Braze recommends using the Canvas V2 workflow to continue building your Canvases. 

![Canvas dashboard with two Canvases listed: V2 Copy of Canvas V1 and Canvas V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas V2 Workflow.][3]

You've completed cloning your Canvas into the Canvas V2 workflow. Now, you can continue building your Canvases in this updated experience!

## Limitations

If your Canvas matches any of the following details, then your Canvas can't be cloned to Canvas V2:

- Status is **Active** 
- Status is **Draft**
- Contains Full Steps with exception events using delays "in" or "on the next"
- Contains branching past the first step

For more information about the differences between Canvas V1 and Canvas V2, check out our [Canvas V2 101]({{site.baseurl}}/canvas_v2_101/#what-are-the-main-differences-between-canvas-v2-and-canvas-v1) article.


[1]: {% image_buster /assets/img_archive/clone_to_v2_workflow.png %}
[2]: {% image_buster /assets/img_archive/clone_to_v2_modal.png %}
[3]: {% image_buster /assets/img_archive/clone_to_v2_dashboard.png %}