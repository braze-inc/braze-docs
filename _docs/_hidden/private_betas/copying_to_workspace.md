---
nav_title: Copying Across Workspaces
article_title: Copying Across Workspaces
permalink: "/copying_to_workspaces/"
hidden: true
description: "This article provides an overview of how to copy campaigns across workspaces."
---

# Copying campaigns across workspaces

> Copying campaigns across a workspace allows you to get a jumpstart on your message composition by starting with a copy of a campaign in a different workspace. This copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

{% alert important %}
Copying campaigns across workspaces is currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How to copy a campaign

![][1]{: style="float:right;max-width:70%;margin-left:15px;"}

To copy a campaign across a workspace, select the <i class="fas fa-cog"></i> gear icon next to the selected campaign, and click **Copy to Workspace**. After copying, we recommend reviewing and testing your campaign to ensure that all fields are working properly.

When you copy a campaign to a workspace, fields such as campaign name and description, variants, delivery schedule type, and conversion behaviors are copied. For email campaigns, fields such as email body, subject, and preheader are also copied over to the destination workspace. 

### Copying campaigns that contain Liquid

For message bodies that include Liquid references, the references are copied over to a workspace, but they may not function as expected. For example, Content Blocks **will not** be copied. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. This applies for catalogs, preference centers, and custom attributes. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid any errors when launching a campaign.

Fields such as trigger actions and audience filters aren't copied across a workspace.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

