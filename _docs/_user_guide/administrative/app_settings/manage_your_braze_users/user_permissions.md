---
nav_title: User Permissions
article_title: Braze Account User Permissions
page_order: 2
page_type: reference
description: "This reference article covers how user permissions works at Braze. Here, you can learn how to edit and set user permissions, choosing who can access your apps in the dashboard."
tool: Dashboard

---

# User permissions

> The user permissions feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin or limited permissions. The creator of the workspace will automatically be granted administrator access.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
{% endalert %}

|Level of Access|Permissions|
|---|---|
|Administrator|Administrators have access to all available features.|
|Limited|Limited users are completely customized at several levels, outlined in the following sections. When you switch a user's permissions from **Administrator** to **Limited**, that user no longer has access to any portion of the Braze dashboard until you deem it so using the checkboxes that appear under the **Edit User** section.|
{: .reset-td-br-1 .reset-td-br-2}

## Editing a user's permissions

To edit a user's [admin](), [company-level](), or [workspace-level]() permissions, go to **Settings** > **Company Users**, then select their name.

![ALT_TEXT]()

### Admin permissions

Admins can access all features and update any company setting.

To grant or remove admin privileges, select **This user is an admin**. Keep in mind, if you remove admin privileges from a user, they can't access Braze until you assign them at least one [compnay-level]() or [workspace-level permission]().

![Selecting Administrator or Limited when editing a user][29]{: style="border:none"}

### Company-level permissions

To manage a user's company-level permissions, check or uncheck the box next to a permission.

- **Manage company settings:** DESCRIPTION.
- **Create and delete workspaces:** DESCRIPTION.

![ALT_TEXT]()

### Workspace-level permissions

To manage the user's workspace-level permissions, first select **Select workspaces and permissions**.

![Manage User Permissions][89]

You can either choose their permissions manually or assign a permission set.

{% tabs local %}
{% tab select manually %}
TODO.
{% endtab %}

{% tab assign permission set %}
TODO.
{% endtab %}
{% endtabs %}

#### List of workspace-level permissions

{% alert important %}
As of April 2024, to create or update promotion code lists, Braze users need the “Access Campaigns, Canvases, Cards, Segments, Media Library” permission.
{% endalert %}

TODO: Add currents permissions here:

|Permission Name|Definition/Parameters|
|---|---|
|Admin|Allows users to access all available features. This is the default setting for all new users. Can update company settings (company name and time zone), which limited users cannot do.|
|Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers| Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of News Feed, segments, templates and media, create templates, upload media, create or update promotion code lists, view engagement reports, and be granted global message settings in the dashboard.<br><br>However, users with this permission cannot pause or edit existing live content. |
|Send Campaigns, Canvases| Allows users to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases. |
|Publish Cards| This permission is only visible if your account is enabled for News Feed, which is being deprecated. This does not affect Content Cards.<br><br>Allows users to create and edit News Feed cards. You can still view News Feed cards without this permission. If your account is enabled for News Feed and a user should be able to launch existing Content Blocks, they need both "Publish Cards" and "Launch Content Blocks" permissions. |
|Edit Segments| Allows users to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Export User Data| Allows users to export their user data from segments, campaigns, and Canvases. |
|View PII | Allows users to view the personally identifiable information fields as defined by your company within the dashboard. |
|View User Profiles PII Compliant| Allows users to view user profiles but redacts fields your company has defined as personally identifiable information (PII). |
|Manage Dashboard Users| Allows users to view, edit, and manage the **Company Users** page. Users with this permission can modify the permissions of any user, including themselves. As such, this permission should be viewed as an administrative access level. This permission doesn't allow users to delete users because only administrators can delete users. |
|Manage Media Library Assets| Allows users to add, edit, and delete media library assets.|
|View Usage Data| Allows users to view app usage, including the channel performance dashboards.|
|Import and Update User Data| Allows users to import CSV and update files of app users as well as view the User Import page. This also allows you to edit the subscription status of a user and their subscription group opt-in/opt-out rules. |
|View Billing Details| Allows users to view subscriptions and billing. |
|Access Dev Console| Allows full access to the following settings and logs:<br> {::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API Keys</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Internal Groups</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Message Activity Log</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event User Log</a></li></ul>{:/}|
|Manage External Integrations| Allows access to all tabs under **Technology Partners** and the ability to sync Braze with other platforms.|
|Manage Apps| Allows users to edit **App Settings**.|
|Manage Teams|Allows users to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.|
|Manage Events, Attributes, Purchases|Allows users to edit custom attributes (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**. |
|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Manage Email Settings|Allows users to save email configuration changes (**Settings** > **Email Preferences**).|
|Manage Subscription Groups| Allows users to create and manage subscription groups. |
|View Transformations|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/).|
|Manage Transformations|Allows users to create and manage Data Transformations. |
|Manage Feature Flags| Allows users to create or edit [feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/).|
| Launch Content Blocks | Allows users to launch [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). |
|Launch Preference Centers| Allows users to launch [preference centers]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Approve and Deny Campaigns| Allows users to approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you're interested in participating in the early access. |
| Approve and Deny Canvases| Allows users to approve or deny Canvases. The [approval workflow for Canvases]({{site.baseurl}}/canvas_approval) must be turned on for this permission to apply. |
| View Custom Attributes Marked as PII | Allows this user to view custom attributes that are marked as PII without being an admin. |
| Manage Catalogs Dashboard Permission | Allows users to create and manage catalogs. |
{: .reset-td-br-1 .reset-td-br-2}

## App-by-app user permissions

Individual users can be granted different degrees of access on an app-by-app basis.

|Limited Permission Degree|Details|
|---|---|---|
|Company Level|Manages the company's app and group settings.|
|Workspace Level Permissions|Determines which workspaces should be managed by the user.|
|App Level Settings|Determines the user's level of editing access.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Permission sets and roles

You can bundle relevant permissions with permission sets and roles by navigating to **Settings** > **Permission Settings**.

### Permission sets

Use permission sets to bundle permissions related to specific subject areas or actions. They can be applied to dashboard users who need the same access across different workspaces, such as in the following example:

Permission Set Name    | Permissions  
----------- | ---------------- 
Developers | “Access Dev Console”
Marketers | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br> “Manage Media Library Assets”
User Management | “Manage Dashboard Users” <br> “Manage Teams”
{: .reset-td-br-1 .reset-td-br-2}

#### Assigning permission sets

Assign permission sets by selecting an existing user or creating a new one on the **Company Users** page, then choosing the appropriate permission set under **Workspace Level Permissions**.

### Roles

{% alert note %}
Roles are currently in early access. Contact your Braze customer success manager if you are interested in participating in the early access. 
{% endalert %}

Roles allow for more structure by bundling together individual custom permissions and workspace access controls. This is especially useful if you have many different brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions.

| Role Name    | Workspace | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>“Manage Media Library Assets” |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br>“Manage Media Library Assets” |
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Manage Dashboard Users”<br>“Manage Teams” |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Assigning roles

Assign roles by selecting an existing user or creating a new one on the **Company Users** page, then choosing the appropriate role under **Workspace Level Permissions**.

## Exporting user permissions

You can download a CSV of your dashboard users and their associated permissions by clicking **Export Users** on the **Company Users** page. A CSV will be sent to the email address associated with your Braze account.

[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[76]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/
[89]: {% image_buster /assets/img/user_permissions_selection.png %}
[5]: {% image_buster /assets/img/permission_sets_manage.png %}
