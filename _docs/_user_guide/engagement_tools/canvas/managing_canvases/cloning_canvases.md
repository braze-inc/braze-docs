---
nav_title: Cloning Canvases
article_title: Cloning Canvases
page_order: 3
alias: "/cloning_canvases/"
description: "This reference article describes how to clone a Canvas from the original Canvas editor into the Canvas Flow workflow."
tool: Canvas
---

# Cloning Canvases to Canvas Flow

{% alert important %}
You can no longer create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow, the current Canvas experience.
{% endalert %}

> If you have an existing Canvas from the original editor, you can clone this Canvas to create a copy in Canvas Flow. By switching to the current Canvas workflow, you gain access to lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/), and [post-launch editing]({{site.baseurl}}/post-launch_edits). Your original Canvas will not be altered or deleted.

To clone your Canvas, do the following:

1. Go to the Canvas dashboard. 
2. Identify the Canvas you want to create a copy of in the Canvas Flow workflow. You can clone Canvases with a **Draft**, **Active**, or **Stopped** status. 
3. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** and select **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. Enter the name of your new Canvas and click **Clone to Canvas Flow**. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Now, you have two versions of your Canvas: the original Canvas and the Canvas Flow version. Your original Canvas still has its original status, and the cloned Canvas has a **Draft** status. You can still access the original Canvas, but Braze recommends using the Canvas Flow workflow to continue building your Canvases.

Previously, some Canvases with branching were unable to be cloned. Now, you can clone Canvases with branching. Note that cloning Canvases with branching may result in disconnected steps. Resolve these disconnected steps (steps that don't have a preceding step connected to them) to makes sure your Canvas journey is mapped properly.

{% alert note %}
If you clone an active Canvas, Braze will continue to send users through the original Canvas. We recommend stopping a Canvas before cloning to avoid sending duplicate messages to users from both Canvases.
{% endalert %}

![Canvas dashboard with two Canvases listed: V2 Copy of Canvas V1 and Canvas V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas Flow workflow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

You've completed cloning your Canvas into the Canvas Flow workflow. Now, you can continue building your Canvases in this updated experience!

## Recommendations

To allow existing users to continue their user journey after you've cloned your original Canvas to Canvas Flow, you can add filters to your existing Canvas which prevent new users from entering the new Canvas.

If re-eligibility is off, add the filter "Entered Canvas Variation". If re-eligibility is on, these are the possible methods to consider to ensure that users don't enter the same Canvas twice:
- Update the existing Canvas to include a unique tag. For the new Canvas, add a filter "Last Received Message from Campaign or Canvas with Tag". This prevents users from entering the Canvas twice after a specific entry date (total number of days after the last message is sent from the original Canvas plus the conversion window). 
- **The following method will consume data points.** Update the original Canvas to include a Braze-to-Braze webhook that triggers a custom attribute date timestamp upon entry. This attribute can be used to prevent users from entering the new Canvas after the specified date (total number of days after the last message is sent from the original Canvas plus the conversion window).

For API-triggered Canvases, coordinate with your engineering team to ensure that these Canvases are using the new Canvas ID when the new Canvases are ready to launch.

For more information about the differences between the original Canvas editor and Canvas Flow experience, check out [Canvas FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


