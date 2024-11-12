---
nav_title: "Target Population Approvals"
article_title: "Target Population Approvals"
permalink: "/target_approvals/"
hidden: true
description: "This article describes how to use target population approvals for campaigns and Canvases with a large send volume."
---

# Target population approval

> Using target population approval, you can set volume thresholds for campaigns and Canvases to require an additional approval for your messaging rules. This way, you can have an additional review when a larger audience is targeted in your messaging.

{% alert important %}
Target population approval is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

Before you can set up target population approval, both Canvas and campaign approval workflows must be turned on.

To turn on Canvas and campaign approval workflows, go to **Settings** > **Approval Workflow** > **Always-On Approvals**. 

## Setting up target population approval

1. Go to **Settings** > **Approval Workflow** > **Messaging Rules**.
2. Select **Create rule**.
3. Give your rule a name for identification at a glance (for example, "All user subscriptions").
4. For **Object**, select **Campaign**, **Canvas**, or **Both Canvas and Campaigns** to apply the approval rule.
5. Enter a number for **Reachable Users Threshold**.

![An example messaging rule "Medium user group" for both Canvas and campaigns with 10,000 users as the threshold. "Test User" is the approver who can approve the Canvas and campaign to launch.}][1]

You can set up to five messaging rules. When setting up your messaging rule, two rules can exist with the same volume threshold for the same object. For example, you can set a threshold of 10,000 users for Canvas and 10,000 users for both Canvas and campaigns. 

Similarly, if you set up two thresholds for 10,0000 users for Canvas with different approvers, this rule can be saved. This way, you can organize and separate your approvers (such as your legal team and your design team) into specific rules.

Note that you can't set rules with overlapping volume thresholds. For example, the following messaging rule can't be set: one rule with a threshold of 10,000 users and one rule with a threshold of 1,000,000 users.

### Selecting approvers

You can optionally select approvers who, if the threshold is met, have permission to approve the Canvas or campaign. If you don't select approvers, the Canvas or campaign will be blocked from launching.

Only Braze administrators can set messaging rules, but any Braze user can be a target population approver (including users without general approval permissions). 

If a threshold is met and an approver is selected, the user with the approval permission will be able to select **Approved** from the **Target Audience** approval dropdown.

### Rules in Canvas and campaigns

The target population approval controls who can approve the **Target Audience** step of a Canvas and campaign. If a rule is met but approvers are not selected, the Canvas or campaign **Launch** or **Update** button will be disabled.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}