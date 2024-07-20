---
nav_title: Copying Across Workspaces
article_title: Copying Across Workspaces
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "This article provides an overview of how to copy campaigns to different workspaces."
tool: Campaigns
---

# Copying across workspaces

> Copying campaigns across workspaces lets you jumpstart your message composition by starting with a copy of a campaign in a different workspace. This copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

{% alert important %}
Copying campaigns across workspaces is generally available for the following supported channels: SMS, in-app messages, email, email templates, and Content Blocks. Other channel support will be coming soon.
{% endalert %}

## How to copy a campaign to a different workspace

![]({% image_buster /assets/img_archive/clone_campaign.png %}){: style="float:right;max-width:70%;margin-left:15px;"}

Select the <i class="fas fa-cog"></i> gear icon next to the selected campaign, and click **Copy to Workspace**. After copying, we recommend reviewing and testing your campaign to ensure that all fields are working properly.

When you copy a campaign across workspaces, fields such as campaign name and description, variants, delivery schedule type, and conversion behaviors are copied. For email campaigns, fields such as email body, subject, and preheader are also copied over to the destination workspace. 

Note that multi-channel campaigns with unsupported channels can't be copied over to a different workspace.

### Copying campaigns that contain Liquid

For message bodies that include Liquid references, the references are copied over to the destination workspace, but they may not function as expected. This means if a campaign from Workspace A is copied to Workspace B, then Workspace B can't reference Workspace A's details, including Liquid references. For example, fields like trigger actions and audience filters aren't copied over.

Note the following Liquid references with dependencies when copying campaigns across workspaces:

- Catalog item tags
- Connected Content tags
- Content Blocks
- Custom attributes
- Preference centers
- Product recommendations
- Subscription state tags
- Voucher and promotion tags

When you copy a campaign across workspaces, Content Blocks won't be copied. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid errors when launching a campaign.

### What's copied across workspaces

Note the following is not a comprehensive list of what is copied across workspaces and what is omitted. As a best practice, check the campaign details and test to ensure your campaign works as expected.

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
| Reoccurring schedule |  | 
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
| [Email body]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | From address |
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
| HTML and drag-and-drop content |  | 
| Preheader |  | 
| Inline CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Email Templates %}

| Copied | Omitted |
|---|---|
| [Email body]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | API IDs |
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
| HTML and drag-and-drop content | Tags | 
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

