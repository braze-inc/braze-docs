---
nav_title: Cloning Canvases
article_title: Cloning Canvases
page_order: 0
alias: "/cloning_canvases/"
description: "This reference article describes how to clone a Canvas from the original Canvas editor into the Canvas Flow workflow."
tool: Canvas

---

# Cloning Canvases to Canvas Flow

{% alert important %}
As of February 28, 2023, you will no longer be able to create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow.
{% endalert %}

If you have an existing Canvas from the original editor, you can clone this Canvas to create a copy in Canvas Flow. By switching to the Canvas Flow workflow, you gain access to lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components), [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/), and [post-launch editing]({{site.baseurl}}/post-launch_edits). Your original Canvas will not be altered or deleted.

To clone your Canvas, first go to the Canvas dashboard. Next, identify the Canvas you want to create a copy of in the Canvas Flow workflow. You can clone Canvases with a **Draft**, **Active**, or **Stopped** status. Click <i class="fas fa-ellipsis-vertical"></i> **More actions** and select **Clone to Canvas Flow**.

![][1]{: style="max-width:25%;"}

Next, enter the name for your new Canvas and click **Clone to Canvas Flow**. 

![][2]{: style="max-width:70%;"}

Now, you’ll have two versions of your Canvas: the original Canvas and the Canvas Flow version. Your original Canvas will still have its original status, and the cloned Canvas will have a **Draft** status. You can still access the original Canvas, but Braze recommends using the Canvas Flow workflow to continue building your Canvases.

Note that if you clone an active Canvas, Braze will continue to send users through the original Canvas. We recommend stopping a Canvas before cloning to avoid sending duplicate messages to users from both Canvases.

![Canvas dashboard with two Canvases listed: V2 Copy of Canvas V1 and Canvas V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas Flow workflow.][3]

You've completed cloning your Canvas into the Canvas Flow workflow. Now, you can continue building your Canvases in this updated experience!

## Limitations

When a Canvas has [branching]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/branching/), the following criteria must be met in order for the Canvas to be cloned to Canvas Flow.
- Delay conditions of the branch are the same.
- Audience section is not empty.
- No exception events are used.
- The variant branches into multiple full steps (no full steps branch into multiple steps).

### Examples

If a Canvas has multiple steps that trace back to the variant (variant-level branching), it can't be cloned to Canvas Flow.

However, if a Canvas has variant-level branching, and this variant branches out into full steps with the criteria listed in the previous section, then this Canvas can be cloned to Canvas Flow.

![Example of a Canvas that branches out into two full steps from the variant.][4]{: style="max-width:50%;"}

As another example, if a Canvas has a full step that has exception events and this full step also uses the delay filter "in" or "on the next", then it can't be cloned to Canvas Flow. However, if a Canvas step uses exception events with any other delay type, then the Canvas can be cloned to Canvas Flow.

## Recommendations

To allow existing users to continue their user journey after you've cloned your original Canvas to Canvas Flow, you can add filters to your existing Canvas which prevent new users from entering the new Canvas.

If re-eligibility is off, add the filter "Entered Canvas Variation". If re-eligibility is on, these are the possible methods to consider to ensure that users don't enter the same Canvas twice.
- Update the existing Canvas to include a unique tag. For the new Canvas, add a filter "Last Received Message from Campaign or Canvas with Tag". This will prevent users from entering the Canvas twice after a specific entry date (total number of days after the last message is sent from the original Canvas plus the conversion window). 
- **The following method will consume data points.** Update the original Canvas to include a Braze-to-Braze webhook that triggers a custom attribute date timestamp upon entry. This attribute can be used to prevent users from entering the new Canvas after the specified date (total number of days after the last message is sent from the original Canvas plus the conversion window).

For API-triggered Canvases, coordinate with your engineering team to ensure that these Canvases are using the new Canvas ID once the new Canvases are ready to launch.

For more information about the differences between the original Canvas editor and Canvas Flow experience, check out [Canvas FAQs]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


[1]: {% image_buster /assets/img_archive/clone_to_v2_workflow.png %}
[2]: {% image_buster /assets/img_archive/clone_to_v2_modal.png %}
[3]: {% image_buster /assets/img_archive/clone_to_v2_dashboard.png %}
[4]: {% image_buster /assets/img_archive/clone_to_flow_variant.png %}
