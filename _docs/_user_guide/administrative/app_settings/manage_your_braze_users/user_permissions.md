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

> The user permissions feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin or limited permissions. The creator of the workspace will automatically be granted administrator access.

These settings can be found at **Settings** > **Company Users**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
{% endalert %}

![Account users list on the Manage Settings page][30]

|Level of Access|Permissions|
|---|---|
|Administrator|Administrators have access to all available features.|
|Limited|Limited users are completely customized at several levels, outlined in the following sections. When you switch a user's permissions from **Administrator** to **Limited**, that user no longer has access to any portion of the Braze dashboard until you deem it so using the checkboxes that appear under the **Edit User** section.|
{: .reset-td-br-1 .reset-td-br-2}

## Editing user permissions

To edit a specific user's permissions, either by allowing them to remain as the default **Administrator** role or changing them to a **Limited** role, do the following:

1. Go to the **Company Users** page. 
2. Click the edit icon in the user's row.
3. Select **Limited** in the **User Role** dropdown.

![Selecting Administrator or Limited when editing a user][29]{: style="border:none"}

When you switch a user's permissions from **Administrator** to **Limited**, that user no longer has access to any portion of Braze until you set those specific permissions using the checkboxes that appear under the **Edit User** section.

## Managing limited and team role permissions

You can manage user permissions by group or on an individual basis when editing or adding a user from the **Company Users** page.

![Manage User Permissions][89]

|Permission Name|Definition/Parameters|
|---|---|
|Admin|Allows users to access all available features. This is the default setting for all new users. Can update company settings (company name and time zone), which limited users cannot do.|
|Access Campaigns, Canvases, Cards, Segments, Media Library| Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of News Feed, segments, templates and media, create templates, upload media, view engagement reports, and be granted global message settings in the dashboard. <br><br>However, users with this permission cannot pause or edit existing live content. |
|Send Campaigns, Canvases| Allows users to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases. To launch existing Content Blocks, the **Send campaigns, Canvases** permission is required. |
|Publish Cards| This permission is only visible if your account is enabled for News Feed, which is being deprecated. This does not affect Content Cards.<br><br>Allows users to create and edit News Feed cards. You can still view News Feed cards without this permission. If your account is enabled for News Feed and a user should be able to launch existing Content Blocks, they need both **Publish Cards** and **Send campaigns, Canvases** permissions. |
|Edit Segments| Allows users to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Export User Data| Allows users to export their user data from segments, campaigns, and Canvases. |
|View PII | Allows users to view the personally identifiable information fields as defined by your company within the dashboard. |
|View User Profiles PII Compliant| Allows users to view user profiles but redacts fields your company has defined as personally identifiable information (PII). |
|Manage Dashboard Users| Allows users to view, edit, and manage the **Company Users** page. Users with this permission can modify the permissions of any user, including themselves. As such, this permission should be viewed as an administrative access level.|
|Manage Media Library| Allows users to upload images to the library. You can still upload pictures and audio directly to a campaign without this permission.|
|View Usage Data| Allows users to view app usage.|
|Import and Update User Data| Allows users to import CSV and update files of app users as well as view the User Import page. This also allows you to edit the subscription status of a user and their subscription group opt-in/opt-out rules. |
|View Billing Details| Allows users to view subscriptions and billing. |
|Access Dev Console| Allows access to Developer Console (where you can view API keys, API campaign activity log, event user log, and internal groups for testing messages).|
|Manage External Integrations| Allows access to all tabs under **Technology Partners** and the ability to sync Braze with other platforms.|
|Manage Apps| Allows users to edit **App Settings**.|
|Manage Teams|Allows users to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.|
|Manage Events, Attributes, Purchases|Allows users to edit custom attributes (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**. If you turn this on for a non-admin Braze user, **Access Campaigns, Canvases, Cards, Segments, Media Library** permissions must also be granted. |
|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Manage Email Settings|Allows users to save email configuration changes (**Settings** > **Email Preferences**).|
|Manage Subscription Groups| Allows users to create and manage subscription groups. |
|View Transformations|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/).|
|Manage Transformations|Allows users to create and manage Data Transformations. |
|Manage Feature Flags| Allows users to create or edit [feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/).|
|Launch Preference Centers| Allows users to launch [preference centers]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Approve and Deny Campaigns| Allows users to approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you're interested in participating in the early access. |
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

## Permission sets

On the **Permission Sets** page found at **Settings** > **Permission Settings**, you can create, edit, and delete custom permission assignments for your Braze dashboard users. 

Permission sets can be assigned by selecting an existing user or creating a new one on the **Company Users** page, then choosing the appropriate permission set under **Workspace Level Permissions**.

![The Permission Sets tab opens a Manage Permissions Sets page with a table of permission set names and selected permissions.][5]

Each permission set can be defined for a specific group of users, such as in the following example:

Permission Set Name    | Permissions  
----------- | ---------------- 
Developers | “Access Dev Console”
Marketers | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br> “Manage Media Library”
User Management | “Manage Dashboard Users” <br> “Manage Teams”
{: .reset-td-br-1 .reset-td-br-2}

## Exporting user permissions

You can download a CSV of your dashboard users and their associated permissions by clicking **Export Users** on the **Company Users** page. A CSV will be sent to the email address associated with your Braze account.

[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[76]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/
[89]: {% image_buster /assets/img/user_permissions_selection.png %}
[5]: {% image_buster /assets/img/permission_sets_manage.png %}
