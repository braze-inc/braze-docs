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

For message bodies that include Liquid references, the references are copied over to a workspace, but they may not function as expected. This means if a campaign from Workspace A is copied to Workspace B, then Workspace B can't reference Workspace A's details, including Liquid references. For example, fields such as trigger actions and audience filters aren't copied across workspaces.

Note the following Liquid references with dependencies when copying campaigns across workspaces:
- Catalog item tags
- Connected Content tags
- Content Blocks
- Custom attributes
- Preference centers
- Product recommendations
- Subscription state tags
- Voucher and promotion tags

When you copy a campaign across a workspace, Content Blocks won't be copied. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid errors when launching a campaign.

### What's copied across workspaces

Note the following is not a comprehensive list of what is copied across a workspace and what is omitted. As a best practice, check the campaign details and test to ensure your campaign works as expected.

{% tabs %}
{% tab Campaigns %}

| Copied | Omitted |
|---|---|
| Description | Territories | 
| Type | Tags | 
| Actions (nested) | Segments | 
| Conversion behaviors (nested) | Approvals | 
| Quiet time configurations | Trigger schedule | 
| Frequency capping configurations | Campaign summaries | 
| Recipient subscription state |  | 
| Reoccuring schedule |  | 
| Is Transactional |  | 

{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Conversion Behaviors %}

| Copied | Omitted |
|---|---|
| Type behavior | Workspace IDs |
| Campaign interaction |  Campaign ID | 
| Custom event name |  | 
| Product name |  | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Actions %}

| Copied | Omitted |
|---|---|
| Action types | Send count |
| Message variations |  |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Message Variations %}

| Copied | Omitted |
|---|---|
| Send percentage | API ID |
| Type |  Seed group IDs | 
|  |  Link template IDs | 
|  |  Internal user group IDs | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Email Message Variation %}

| Copied | Omitted |
|---|---|
| Body | From address |
| Message extras |  Reply to | 
| Title |  BCC | 
| Subject |  Link template | 
|  |  Link aliasing |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Email Body %}

| Copied | Omitted |
|---|---|
| Plain text | Link aliasing |
| HTML |  | 
| Preheader |  | 
| Inline CSS |  | 
| AMP HTML |  |
| Drag-and-drop JSON |  |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Email Templates %}

| Copied | Omitted |
|---|---|
| Body | API IDs |
| Description | Image IDs | 
| Subject | Territories | 
| Headers | Tags | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Content Blocks %}

| Copied | Omitted |
|---|---|
| Name | Link aliasing |
| Description | API keys | 
| Content | Territories | 
| Drag-and-drop JSON | Tags | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab SMS Message Variation %}

| Copied | Omitted |
|---|---|
| Body | Messaging service |
| Link shortening | VCF media items | 
| Click tracking |  | 
| Media items |  | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

