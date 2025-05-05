---
nav_title: Messaging Rules
article_title: Messaging Rules
page_order: 1
page_type: reference
description: "This page covers describes how to use messaging rules in the approval workflow for campaigns and Canvases with a large send volume."
---

# Messaging rules

> Use messaging rules to set volume thresholds for campaigns and Canvases that will require additional approval before launch&#8212;this way, you can have another review when a larger audience is targeted in your messaging.

## How it works

Messaging rules apply to a workspace and are made up of an object and a reachable user threshold.

- **Object:** Defines what message type the rule will be applied to: campaign, Canvas, or both Canvas and campaigns.
- **Reachable users threshold:** Determines what audience size that will require an additional approval.

Only Braze administrators can set messaging rules, but any Braze user can be a messaging rule approver (including users without general approval permissions).

When setting up your messaging rule, two rules can exist with the same volume threshold for the same object. For example, you can set a threshold of 10,000 users for Canvas and 10,000 users for both Canvas and campaigns. 

Similarly, you can save two rules that share the same user threshold so that you can organize and separate your rules by approvers. For example, you create the following two rules:

- Rule A for Canvas with a threshold of 100,000 users with approvers on your legal team
- Rule B for Canvas with a threshold of 100,000 users with approvers on your marketing team 

However, you can’t set rules with overlapping volume thresholds for the same object. For example, the following messaging rule **can’t** be set: 

- Rule C for Canvas with a threshold of 10,000 users 
- Rule D for Canvas with a threshold of 1,000,000 users

## Create a messaging rule

### Step 1: Add a rule

{% alert note %}
You can create up to five messaging rules.
{% endalert %}

1. Go to **Settings** > **Approval Workflow** > **Messaging Rules**.
2. Select **Create rule**.
3. Give this rule a name (for example, "All user subscriptions").
4. For **Object**, select **Campaign**, **Canvas**, or **Both Canvas and Campaigns** to apply the approval rule.
5. Enter a number for **Reachable Users Threshold**. For more information, refer to [Audience statistics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Select **Save**.

![An example messaging rule "All user subscriptions" for both Canvas and campaigns with 300,000 users as the threshold. There is one user who can approve the Canvas and campaign to launch.][1]

### Step 2: Determine launching with approval (optional)

1. Select **Allow launching with approval**.
2. For **With Approval From**, select the approvers who have permission to approve the Canvas or campaign if the threshold is met.

Note the following details on launching messages with approval:

- If a threshold is met and an approver is selected, the Braze user with the approval permission will be able to select **Approved** from the **Target Audience** approval dropdown.
- If a threshold is met an an approve is not selected, the Canvas or campaign will be prevented from launching.

![The "Summary" step of the Canvas workflow that shows you need an approval to launch.][2]

## Frequently asked questions

### Do I have to reconfigure my permissions to use messaging rules?

No. Any user, regardless of their current permissions, can be selected as a target population approver.

### How do messaging rules relate to the Target Audience step of the campaign and Canvas editor?

Messaging rules don't take into account details such as triggering events. For example, a campaign might target all your users. However, the campaign is event triggered, so the actual users who receive it is lower.

### Will anything automatically change when this feature is turned on?

No. After this feature is turned on, you must manually enter a volume threshold and select approvers to use the feature.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}
[2]: {% image_buster /assets/img/non_approver_banner.png %}