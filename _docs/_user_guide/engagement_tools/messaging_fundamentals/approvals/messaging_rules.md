---
nav_title: Messaging rules
article_title: Messaging Rules
page_order: 1
page_type: reference
description: "This page covers how to use messaging rules in the approval workflow for campaigns and Canvases with a large send volume."
---

# Messaging rules

> Use messaging rules in your approval workflow to limit the number of reachable users before an additional approval is required&#8212;this way, you can review your campaigns and Canvases before you target a larger audience.

## How it works

Messaging rules apply to a workspace and are made up of a message type and a maximum number of reachable users.

- **Message type:** Defines what message type the rule will be applied to: campaign, Canvas, or both Canvas and campaigns.
- **Maximum reachable users:** Determines what audience size that will require an additional approval.

### Shared message types and maximum reachable users

Two rules can exist with the same number of reachable users for the same message type. For example, you can set a maximum of 10,000 users for Canvas and 10,000 users for both Canvas and campaigns. 

### Separate approvers

Two rules can share the same user maximum so that you can organize and separate your rules by approvers. For example, you create the following two rules:

- Rule A for Canvas with a maximum of 100,000 users with approvers on your legal team
- Rule B for Canvas with a maximum of 100,000 users with approvers on your marketing team 

### No overlapping reachable users

You can’t set rules with an overlapping number of users for the same message type. For example, the following messaging rule **can't** be set: 

- Rule C for Canvas with a maximum of 10,000 users 
- Rule D for Canvas with a maximum of 1,000,000 users

## Creating a messaging rule

### Prerequisites

Only Braze administrators can set messaging rules, but any Braze user can be a messaging rule approver (including users without general approval permissions).

### Step 1: Add a rule

{% alert note %}
You can create up to five messaging rules.
{% endalert %}

1. Go to **Settings** > **Approval Workflow** > **Messaging Rules**.
2. Select **Create rule**.
3. Give this rule a name (for example, "All user subscriptions").
4. For **Message type**, select **Campaign**, **Canvas**, or **Both Canvas and Campaigns** to apply the approval rule.
5. Enter a number for **Maximum reachable users**. For more information, refer to [Audience statistics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Select **Save**.

![An example messaging rule "Rule 1" for campaigns with 100,000 users as the maximum. There is one user who can approve the Canvas and campaign to launch.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Step 2: Determine launching with approval (optional)

Select **Allow launching with approval**. Next, for **With Approval From**, select the approvers who have permission to approve the Canvas or campaign if the maximum is met.

Note the following details on launching messages with approval:

- If the maximum is met and an approver is selected, the Braze user with the approval permission will be able to select **Approved** from the **Target Audience** approval dropdown.
- If the maximum is met an an approve is not selected, the Canvas or campaign will be prevented from launching.

![The "Summary" step of the Canvas workflow that shows you need an approval to launch.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Frequently asked questions

### Do I have to reconfigure my permissions to use messaging rules?

No. Any user, regardless of their current permissions, can be selected as a target population approver.

### How do messaging rules relate to the Target Audience step?

Messaging rules don't take into account details such as triggering events. For example, a campaign might target all your users. However, the campaign is event triggered, so the actual users who receive it is lower.

### Will anything automatically change when messaging rules are turned on?

No. After this feature is turned on, you must manually enter the maximum number of users and select approvers to use the feature.

