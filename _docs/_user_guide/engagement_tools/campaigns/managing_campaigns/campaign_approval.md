---
nav_title: Approving Campaigns
article_title: Approving Campaigns
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "This page provides an overview of the campaign approval process."
tool: Campaigns
---

# Approving campaigns

Campaign approval adds a review process to your workflow before launching a campaign. Available exclusively for campaigns, this feature adds new states available in the campaign confirmation workflow step. Now, you can ensure that each confirmation is approved in order to launch the campaign.

## Turning on campaign approval

By default, the campaign approval setting is turned off. To enable this feature, go to **Manage Settings** > **Approval Workflow**.

{% alert note %}
Only admins and users with permission to manage approval settings will see this page.
{% endalert %}

## Using approvals

In the **Review Summary** step of the campaign building workflow, there is an approval option to approve or deny your campaign's key components: **Messages**, **Delivery**, **Target Population**, and **Conversion Events**. The default state for campaign approval is **Pending Approval**. 

![][1]

Once each section is approved, the **Launch** button will be enabled and you can launch your campaign! 

{% alert important %}
Campaign approval is not supported in the building workflow for Canvases or API campaigns.
{% endalert %}

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
