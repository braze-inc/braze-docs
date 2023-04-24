---
nav_title: Approving Canvases
permalink: "/canvas_approval/"
hidden: true
layout: dev_guide
---

# Approving Canvases

Canvas approval adds a review process to your workflow before launch. Now, you can ensure that each confirmation is approved in order to launch the Canvas.

{% alert important %}
The approval workflow for Canvases is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

## Turning on Canvas approval

To turn on the approval workflow for Canvas, go to **Manage Settings > Approval Settings**. By default, this feature is turned off.

![The Approval Workflow settings where the option to use the approval workflow for campaigns and Canvases are enabled.][1]

{% alert note %}
Only admins and users with permission to manage approval settings will see this page. Be sure to check that you have the proper [user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/) to approve Canvases.
{% endalert %}

## Using approvals

When the approval workflow is enabled, you'll have access to the **Summary** step of the Canvas builder. This page provides a summary of the key Canvas details with the option to approve or deny these details, including conversion events, entry schedule, and the type and amount of components in your Canvas. Note the default state for Canvas approval is **Pending Approval**.

Once approval statuses are set on the **Summary** step, any subsequent changes made to the Canvas will reset all approval statuses once saved. This applies to any changes made either in a draft Canvas or a post-launch Canvas. For example, if you only make changes to the target audience, the **Summary** step will revert approval statuses for all sections back to the default state, pending.

![An example of the Canvas approval workflow where the Conversion Events and Entry Schedule details have been marked as approved.][2]{: style="max-width:85%" }

Once each section is approved, the **Launch** button will be available, and you can launch your Canvas.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}