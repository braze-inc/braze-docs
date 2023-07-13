---
nav_title: Setting User Permissions
article_title: Braze Account User Permissions
page_order: 2
page_type: reference
description: "This reference article covers how user permissioning works at Braze. Here, you can learn how to edit and set user permissions, choosing who can access your apps in the dashboard."
tool: Dashboard

---

# Setting user permissions

<style>
.fa-crown {
  color: gold;
}
</style>

> Braze's user permission feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin or limited permission. The creator of the workspace will automatically be granted administrator access.

These settings can be found at **Settings** > **Company Users**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
{% endalert %}

![Account users list on the Manage Settings page][30]

|Level of Access|Permissions|
|---|---|
|Administrator|Administrators have access to all available features.|
|Limited|Limited users are completely customized at several levels, outlined in the following sections. When you switch a user's permissions from admin to limited, that user no longer has access to any portion of the Braze dashboard until you deem it so using the checkboxes that appear under the Edit User box.|
{: .reset-td-br-1 .reset-td-br-2}

## Editing user permissions

From the **Company Users** page, you can edit a specific user's permissions, either by allowing them to remain as the default administrator role, or changing them to a limited role. To change their role, click the edit icon in the user's row and select **Limited** from the **User Role** dropdown.

![Selecting Administrator or Limited when editing a user][29]{: style="border:none"}

When you switch a user's permissions from **Administrator** to **Limited**, that user no longer has access to any portion of Braze until you set those specific permissions using the checkboxes that appear under the Edit User box.

## Limited and team role permissions

You can manage user permissions by group or on an individual basis when editing or adding a user from the **Company Users** page.

![Manage User Permissions][89]

|Permission Name|Definition/Parameters|
|---|---|
|Admin|Has access to all available features, default setting for all new users. Can update company settings (company name and time zone), which limited users are unable to do.|
|Access Campaigns, Canvases, Cards, Segments, Media Library| User can view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of News Feed, segments, templates and media, create templates, upload media, view engagement reports, and be granted global message settings in the dashboard. However, users with this permission cannot pause or edit existing live content. |
|Send Campaigns, Canvases| Allows user to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases. To launch existing Content Blocks, **Send campaigns, Canvases** permission is required. |
|Publish Cards| This permission is only visible if your account is enabled for News Feed, which is being deprecated. This does not affect Content Cards.<br><br>Allows user to create and edit News Feed cards. You can still view News Feed cards without this permission. If your account is enabled for News Feed and a user should be able to launch existing Content Blocks, they need both **Publish Cards** and **Send campaigns, Canvases** permissions. |
|Edit Segments| Allows user to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Export User Data| Allows user to export your user data from segments, campaigns and Canvases. |
|View PII | Allows user to view the personally identifiable information fields as defined by your company within the dashboard. This also allows you to edit the subscription status of a user, and their subscription group opt-in/opt-out rules.|
|View User Profiles PII Compliant| Allows users to view user profiles but redacts fields your company has defined as personally identifiable information (PII). |
|Manage Dashboard Users| Allows user to view, edit, and manage the **Company Users** page. Users with this permission can modify the permissions of any user, including themselves. As such, this permission should be viewed as an administrative access level.|
|Manage Media Library| Allows user to upload images to library. You can still upload pictures/audio etc. directly to a campaign without this permission.|
|View Usage Data| Allows user to view app usage.|
|Import and Update User Data| Allows user to import CSV and update files of app users as well as view the User Import page.|
|View Billing Details| Allows user to view subscriptions and billing. |
|Access Dev Console| Allows access to Developer Console (where you can view API keys, API campaign activity log, event user log, and internal groups for testing messages).|
|Manage External Integrations| Allows access to all tabs under **Technology Partners** and the ability to sync Braze with other platforms.|
|Manage Apps| Allows user to edit **App Settings**.|
|Manage Teams|Allows user to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.|
|Manage Events, Attributes, Purchases|Allows user to edit custom attributes, (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**. If you are enabling this for a non-admin Braze user, **Access Campaigns, Canvases, Cards, Segments, Media Library** permissions must also be granted. |
|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Manage Email Settings|Allows user to save email configuration changes (**Settings** > **Email Preferences**).|
|Manage Subscription Groups | Allows user to create and manage subscription groups. |
|Manage Approval Settings| This setting has been removed. Only users with admin permissions can turn the [approval workflows]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) settings on or off for your workspace. |
|Approve and Deny Campaigns| Allows users to approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manage if you're interested in participating in the early access. |
| Approve and Deny Canvases| Allows users to approve or deny Canvases. The [approval workflow for Canvases]({{site.baseurl}}/canvas_approval) must be turned on for this permission to apply. |
{: .reset-td-br-1 .reset-td-br-2}

## App-by-app user permissions

Individual users can be granted different degrees of access on an app-by-app basis.

|Limited Permission Degree|Details|
|---|---|---|
|Company Level|Manages the company's app and group settings.|
|Workspace Level Permissions|Determines which workspaces should be managed by the user.|
|App Level Settings|Determines the user's level of editing access.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[76]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/
[89]: {% image_buster /assets/img/user_permissions_selection.png %}
