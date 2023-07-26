---
nav_title: Cloning to Workspaces
article_title: Cloning to Workspaces
permalink: "/cloning_to_workspaces/"
hidden: true
description: "This article provides an overview of the cloning process for workspaces."
---

# Cloning campaigns to workspaces

> You can clone campaigns to a different workspace to keep and build off your successful strategies. 

{% alert important %}
Cloning campaigns to workspaces is currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

To clone to a workspace, select the <i class="fas fa-cog"></i> gear icon next to the selected campaign, and click **Clone to Workspace**. After cloning to a workspace, we recommend reviewing and testing your campaign to ensure that all fields are working properly.

![][1]

When you clone a campaign to a workspace, fields such as campaign name and description, variants, delivery schedule type, and conversion behaviors are cloned. When cloning an email campaign, fields such as email body, subject, and preheader are also copied over to the destination workspace. 

For message bodies that include Liquid references, the references are copied over to a workspace, but they may not function as expected. For example, Content Blocks **will not** be cloned. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. This applies for catalogs, preference centers, and custom attributes. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid any errors when launching a campaign.

Fields such as trigger actions and audience filters aren't cloned to a workspace.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

