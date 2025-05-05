---
nav_title: Target Population Approvals
article_title: Target Population Approvals
page_order: 1
page_type: reference
description: "This page covers describes how to use target population approvals for campaigns and Canvases with a large send volume."
---

# Target population approval

> This page covers how to set up target population approvals for your messaging rules. Using target population approval, you can set volume thresholds for campaigns and Canvases to require additional approval for your messaging rules. This way, you can have an additional review when a larger audience is targeted in your messaging.

## Prerequisite

Before you can set up target population approval, both Canvas and campaign approval workflows must be turned on.

To turn on Canvas and campaign approval workflows, go to **Settings** > **Approval Workflow** > **Always-On Approvals**. 

## Setting up target population approval

1. Go to **Settings** > **Approval Workflow** > **Messaging Rules**.
2. Select **Create rule**.
3. Give your rule a name for identification at a glance (for example, "All user subscriptions").
4. For **Object**, select **Campaign**, **Canvas**, or **Both Canvas and Campaigns** to apply the approval rule.
5. Enter a number for **Reachable Users Threshold**. For more information, refer to [Audience statistics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Select **Save**.

![An example messaging rule "Rule 1" for both Canvas and campaigns with 100,000 users as the threshold. There are three users who can approve the Canvas and campaign to launch.][1]

You can set up to five messaging rules. When setting up your messaging rule, two rules can exist with the same volume threshold for the same object. For example, you can set a threshold of 10,000 users for Canvas and 10,000 users for both Canvas and campaigns. 

Similarly, if you set up two thresholds for 10,0000 users for Canvas with different approvers, this rule can be saved. This way, you can organize and separate your approvers (such as your legal team and your design team) into specific rules.

Note that you can’t set rules with overlapping volume thresholds for the same object. For example, the following messaging rule **can’t** be set: one rule with a threshold of 10,000 users for Canvas and another rule with a threshold of 1,000,000 users for Canvas.

### Selecting approvers

{% alert important %}
You can optionally select approvers who, if the threshold is met, have permission to approve the Canvas or campaign. If you don’t select approvers, the Canvas or campaign will be blocked from launching.
{% endalert %}

Only Braze administrators can set messaging rules, but any Braze user can be a target population approver (including users without general approval permissions). 

If a threshold is met and an approver is selected, the user with the approval permission will be able to select **Approved** from the **Target Audience** approval dropdown.

### Rules in Canvas and campaigns

The target population approval controls who can approve the **Target Audience** step of a Canvas and campaign. If a rule is met but approvers are not selected, the Canvas or campaign **Launch** or **Update** button will be disabled.

![The "Summary" step of the Canvas workflow that shows you need an approval to launch.][2]

## Frequently asked questions

### Will anything automatically change when this feature is turned on?

No. After this feature is turned on, you must manually enter a volume threshold and select approvers to use the feature.

### Do I have to reconfigure my permissions to use this feature?

No. You don't need to change existing permissions. Any user, regardless of their current permissions, can be selected as a target population approver.

### Does the same threshold apply to all workspaces?

No. You must set up messaging rules for each workspace.

### Is the target population approval based on the Target Audience step?

Yes. The target population approval doesn't take into account details such as triggering events. For example, a campaign might target all your users; however, the campaign is event triggered, so the actual users who receive it is lower.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}
[2]: {% image_buster /assets/img/non_approver_banner.png %}