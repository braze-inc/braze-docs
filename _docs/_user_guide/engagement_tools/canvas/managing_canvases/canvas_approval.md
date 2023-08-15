---
nav_title: Canvas Approval and Permissions
article_title: Canvas Approval and Permissions 
page_order: 0.5
alias: "/canvas_approval/"
description: "This reference article covers how to approve Canvases before launch and describes related user permissions."
tool: Canvas
---

# Canvas approval and permissions

Canvas approval adds a review process to your workflow before launch. Now, you can ensure that each confirmation is approved in order to launch the Canvas.

## Turning on Canvas approval

To turn on the approval workflow for Canvas, go to **Settings** > **Approval Workflow** under **Workplace Settings**. By default, this feature is turned off. 

![The Approval Workflow settings where the option to use the approval workflow for campaigns and Canvases are enabled.][1]

{% alert note %}
Only admins and users with permission to manage approval settings will see this page. Be sure to check that you have the proper [user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/) to approve Canvases.
{% endalert %}

### Setting user permissions

After the approval workflow for Canvas has been turned on, go to **Settings** > **Company Users** and select **Approve and Deny Canvases** to allow specific users to approve and deny Canvases immediately. A user with this permission could be able to do any of the following in the Canvas workflow:
- Approve but not launch the Canvas
- Launch but not approve the Canvas
- Approve and launch the Canvas
- Neither approve or launch the Canvas

![An example of an unselected checkbox for the Approve and Deny Canvases permission, meaning this user does not have permission to approve or deny Canvases.][3]{: style="max-width:70%" }

{% alert important %}
To edit a live campaign, you will need the "Approve and Deny Campaigns" permission. A user will need to approve their changes since a draft version of campaigns is not yet available. This is not the case for Canvases as a user can make changes and save as a draft, and another user can approve and launch the Canvas.
{% endalert %}

Depending on your team-level permissions, you'll be able to view all or selected Canvases. You'll still be able to save and launch your Canvas, but note that the team tag must be set.

## Using approvals

When the approval workflow is enabled, you'll have access to the **Summary** step of the Canvas builder. This page provides a summary of the key Canvas details with the option to approve or deny these details, including conversion events, entry schedule, and the type and amount of components in your Canvas. Note the default state for Canvas approval is **Pending Approval**.

Once approval statuses are set on the **Summary** step, any subsequent changes made to the Canvas will reset all approval statuses when saved. This applies to any changes made either in a draft Canvas or a post-launch Canvas. For example, if you only make changes to the target audience, the **Summary** step will revert approval statuses for all sections back to the default state, pending.

![An example of the Canvas approval workflow where the Conversion Events and Entry Schedule details have been marked as approved.][2]{: style="max-width:85%" }

Once each section is approved, the **Launch** button will be available, and you can launch your Canvas.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}