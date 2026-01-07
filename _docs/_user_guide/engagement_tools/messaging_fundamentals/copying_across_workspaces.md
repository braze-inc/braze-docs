---
nav_title: Copy across workspaces
article_title: Copy Across Workspaces
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "This reference article provides an overview of how to copy campaigns and Canvases to different workspaces."
tool:
    - Campaigns
    - Canvas
---

# Copy campaigns and Canvases across workspaces

> Copying campaigns across workspaces lets you jumpstart your message composition by starting with a copy of a campaign in a different workspace. This page covers how to copy campaigns to different workspaces and lists what is and isn't copied over.

When you copy a campaign or Canvas to a different workspace, the copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
Copying campaigns across workspaces is generally available. Channel support for Content Cards isn't currently available.
{% endalert %}

You can copy campaigns across workspaces for these supported channels: SMS, in-app messages, push notifications, email, and webhooks. You can also copy across email templates, feature flags, and Content Blocks. Note that multi-channel campaigns with unsupported channels can't be copied over to a different workspace.

To copy a campaign to a different workspace:

1. Select the <i class="fas fa-cog"></i> gear icon next to the selected campaign.
2. Select **Copy to workspace**. 
3. After copying, review and test your campaign to confirm that all fields work properly.

{% endtab %}
{% tab canvas %}

{% alert important %}
Copying Canvases across workspaces is generally available. The following channels aren't currently supported: LINE, Content Cards, and WhatsApp.
{% endalert %}

You can copy Canvases across workspaces for these supported channels: email, in-app messages, push, webhooks, and SMS.

To copy a Canvas to a different workspace:

1. Select the <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;menu next to the selected Canvas.
2. Select **Copy to workspace**. 
3. After copying, review and test your Canvas to confirm that all fields work properly.

When copying a Canvas with Audience Sync steps, the settings will not be copied over to the destination workspace, but the steps in the journey will be.

{% endtab %}
{% endtabs %}

## What's copied across workspaces

Note that the following is not a comprehensive list of what is copied across workspaces and what is omitted. As a best practice, check the campaign and Canvas details and test to confirm your message works as expected.

### Details

{% tabs local %}
{% tab campaigns %}

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Description | Territories | 
| Type | Tags | 
| Actions (nested) | Segments | 
| Conversion behaviors (nested) | Approvals | 
| Quiet time configurations | Trigger schedule | 
| Frequency capping configurations | Canvas summaries | 
| Recipient subscription state |  | 
| Reoccurring schedule |  | 
| Is Transactional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Conversion behaviors

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Type behavior | Workspace IDs |
| Campaign interaction |  Campaign ID | 
| Custom event name |  | 
| Product name |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Type behavior | Workspace IDs |
| Canvas interaction |  Canvas ID | 
| Custom event name |  | 
| Product name |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Actions

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Type behavior | Workspace IDs |
| Campaign interaction |  Campaign ID | 
| Custom event name |  | 
| Product name |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Type behavior | Workspace IDs |
| Canvas interaction |  Canvas ID | 
| Custom event name |  | 
| Product name |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Message variations

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Send percentage | API ID |
| Type |  Seed group IDs | 
|  |  Link template IDs | 
|  |  Internal user group IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Send percentage | API ID |
| Type |  Seed group IDs | 
|  |  Link template IDs | 
|  |  Internal user group IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### Email message variation

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Email body | From address |
| Message extras |  Reply to | 
| Title |  BCC | 
| Subject |  Link template | 
|  |  Link aliasing |
|  | Translations |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Email body | From address |
| Message extras |  Reply to | 
| Title |  BCC | 
| Subject |  Link template | 
|  |  Link aliasing |
|  | Translations |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Email body

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Plain text | Link aliasing |
| HTML and drag-and-drop content | Translations | 
| Preheader |  | 
| Inline CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Plain text | Link aliasing |
| HTML and drag-and-drop content | Translations | 
| Preheader |  | 
| Inline CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Email templates

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Email body | API IDs |
| Description | Image IDs | 
| Subject | Territories | 
| Headers | Tags | 
| | Translations |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Email body | API IDs |
| Description | Image IDs | 
| Subject | Territories | 
| Headers | Tags | 
| | Translations |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Name | Link aliasing |
| Description | API keys | 
| Content | Territories | 
| HTML and drag-and-drop content | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Name | Link aliasing |
| Description | API keys | 
| Content | Territories | 
| HTML and drag-and-drop content | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### SMS message variation

{% tabs local %}
{% tab campaigns %}

| Copied | Omitted |
|---|---|
| Body | Messaging service |
| Link shortening | VCF media items | 
| Click tracking |  | 
| Media items |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copied | Omitted |
|---|---|
| Body | Messaging service |
| Link shortening | VCF media items | 
| Click tracking |  | 
| Media items |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Copying messages that contain Liquid

Liquid references within message bodies are copied over to the destination workspace, but the references may not function as expected. This means if a Canvas from Workspace A is copied to Workspace B, then Workspace B can't reference Workspace A's details, including Liquid references. For example, fields like trigger actions and audience filters aren't copied over.

Keep track of the following Liquid references with dependencies when copying campaigns and Canvases across workspaces:

- Catalog item tags
- Connected Content tags
- Content Blocks
- Custom attributes
- Preference centers
- Product recommendations
- Subscription state tags
- Voucher and promotion tags

## Copying messages with feature flags

To copy a feature flag campaign and a Canvas with a Feature Flag step between workspaces, make sure the destination workspace has a [feature flag experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) configured with an ID that matches either the feature flag referenced in the original campaign or the Feature Flag step referenced in the original Canvas.

If you copy a campaign or Canvas that has a Feature Flag step with a feature flag ID that doesn't exist in the destination workspace, the Feature Flag step will be copied but its contents will not be.

## Copying messages with Content Blocks

When you copy a campaign across workspaces, Content Blocks won't be copied. However, a Content Block can be referenced in the destination workspace if a block with the same name exists. Alternatively, you can create the Content Block (or these Liquid references) in the destination workspace to avoid errors when launching a campaign.

For Canvases that reference a Content Block, the Content Block must first be copied to the destination workspace.
