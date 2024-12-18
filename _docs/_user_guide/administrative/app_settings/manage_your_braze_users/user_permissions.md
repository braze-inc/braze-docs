---
nav_title: Permissions
article_title: Braze permissions
page_order: 2
page_type: reference
description: "This reference article covers how user permissions work at Braze. Here, you can learn how to edit and set user permissions, choosing who can access your apps in the dashboard."
tool: Dashboard

---

# Braze permissions

> Learn how to create permission sets, create roles, edit user permissions, and export user permissions, so you can ensure your users only access the workspaces and features they need most.

## Creating a permission set

Use permission sets to bundle permissions related to specific subject areas or actions. They can be applied to dashboard users who need the same access across different workspaces. To create a permission set, go to **Settings** > **Permission Settings**, then select **Create permission set**. For a description of each permission, see [List of permissions](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Permissions|
|-----------|----------------|
|Developers|“Access Dev Console”|
|Marketers|“Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br> “Manage Media Library Assets”|
|User Management|“Manage Dashboard Users” <br> “Manage Teams”|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Creating a role

Roles allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. For a description of each permission, see [List of permissions](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Role Name    | Workspace | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>“Manage Media Library Assets” |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br>“Manage Media Library Assets” |
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Manage Dashboard Users”<br>“Manage Teams” |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

### How do permission sets and roles differ from teams?

Refer to [Company users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) for a breakdown of the differences among teams, permission sets, and roles.

## Editing a user's permissions

To edit a user's current [admin](#admin), [company](#company), or [workspace](#workspace) permissions, go to **Settings** > **Company Users**, then select their name.

![The "Company Users" page in Braze with one user listed in the results.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

### Admin

Admins have access to all features and the ability to modify any company setting. There are also a few things that only admins can do in Braze. 

Only admins can:

- Change [approval settings]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Add, edit, delete, suspend, or unsuspend other [Braze users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Export Braze users as a CSV

To grant or remove admin privileges, select **This user is an admin**, then select **Update user**.

![The details of the selected user with the admin checkbox in focus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
If you remove admin privileges from a user, they won't be able to access Braze until you assign them at least one [company-level](#company) or [workspace-level](#workspace) permission.
{% endalert %}

### Company

To manage the following company-level permissions for a user, check or uncheck the box next to that permission. When you're finished, select **Update user**.

|Permission name|Description|
|----------|-----------|
|Manage company settings|Allows users to modify any company setting.|
|Create and delete workspaces|Allows users to create and delete workspaces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Workspace

You can give a user different permissions for each workspace they belong to in Braze. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually select or assign a permission set [you previously created](#creating-a-permission-set).

If you need to give a user different permissions for different workspaces, repeat this process as many times as needed. For a description of each permission, see [List of permissions](#list-of-permissions).

{% tabs local %}
{% tab select manually %}
Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permissions** choose one or more permissions from the dropdown. They will be assigned these permissions only for the workspaces you have selected. Optionally, you can select **Enable Admin Access** if you'd like to give them full permissions for this workspace instead.

When you're finished, select **Update user**.

![Workspace-level permissions being manually selected in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})
{% endtab %}

{% tab assign permission set %}
Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permission Sets**, choose one permission set. They will be assigned these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a permission set in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})
{% endtab %}
{% endtabs %}

## Exporting user permissions

To download list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. A CSV file will be sent to your email address shortly.

![The "Company Users" page in Braze with the "Export Users" option in focus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## List of permissions

{% alert important %}
As of April 2024, to create or update promotion code lists, Braze users need the “Access Campaigns, Canvases, Cards, Segments, Media Library” permission.
{% endalert %}

|Level|Name|Definition|
|---|---|---|
|Admin|Admin|Allows users to access all available features. This is the default setting for all new users. Can update company settings (company name and time zone), which limited users cannot do.|
|Company|Create and delete workspaces|Allows users to create and delete workspaces.|
|Company|Manage company settings|Allows users to modify any company setting.|
|Workspace|Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers|Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of News Feed, segments, templates and media, create templates, upload media, create or update promotion code lists, view engagement reports, and view global message settings in the dashboard. However, users with this permission cannot pause or edit existing live content.|
|Workspace|Access Dev Console|Allows full access to the following settings and logs:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API Keys</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Internal Groups</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Message Activity Log</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event User Log</a></li><li><a href='/docs/user_guide/data_and_analytics/cloud_ingestion/'>Manage Cloud Data Ingestion</a></li></ul>{:/}|
|Workspace|Approve and Deny Campaigns|Allows users to approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you're interested in participating in the early access.|
|Workspace|Approve and Deny Canvases|Allows users to approve or deny Canvases. The [approval workflow for Canvases]({{site.baseurl}}/canvas_approval) must be turned on for this permission to apply.|
|Workspace|Edit Currents Integrations|Allows users to modify a Currents connection, including credentials. By default, users assigned the "External Integrations" permission are also assigned this permission.|
|Workspace|Edit Segments|Allows users to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Workspace|Export User Data|Allows users to export their user data from segments, campaigns, and Canvases.|
|Workspace|Import and Update User Data|Allows users to import CSV and update files of app users as well as view the User Import page. This also allows you to edit the subscription status of a user and their subscription group opt-in/opt-out rules.|
|Workspace|Launch Content Blocks|Allows users to launch [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Workspace|Launch Preference Centers|Allows users to launch [preference centers]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Workspace|Manage Apps|Allows users to edit **App Settings**.|
|Workspace|Manage Catalogs Dashboard Permission|Allows users to create and manage catalogs.|
|Workspace|Manage Dashboard Users|Allows users to view, edit, and manage the **Company Users** page. Users with this permission can modify the permissions of any user, including themselves. As such, this permission should be viewed as an administrative access level. This permission doesn't allow users to delete users because only administrators can delete users.|
|Workspace|Manage Email Settings|Allows users to save email configuration changes (**Settings** > **Email Preferences**).|
|Workspace|Manage Events, Attributes, Purchases|Allows users to edit custom attributes (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**.|
|Workspace|Manage External Integrations|Allows access to all tabs under **Technology Partners** and the ability to sync Braze with other platforms.|
|Workspace|Manage Feature Flags|Allows users to create or edit [feature flags]({{site.baseurl}}/developer_guide/feature_flags/).|
|Workspace|Manage Media Library Assets|Allows users to add, edit, and delete media library assets.|
|Workspace|Manage Subscription Groups|Allows users to create and manage subscription groups.|
|Workspace|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Workspace|Manage Teams|Allows users to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.|
|Workspace|Manage Transformations|Allows users to create and manage Data Transformations.|
|Workspace|Publish Cards|This permission is only visible if your account is enabled for News Feed, which is being deprecated. This does not affect Content Cards. Allows users to create and edit News Feed cards. You can still view News Feed cards without this permission. If your account is enabled for News Feed and a user should be able to launch existing Content Blocks, they need both "Publish Cards" and "Launch Content Blocks" permissions.|
|Workspace|Send Campaigns, Canvases|Allows users to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases.|
|Workspace|View Billing Details|Allows users to view subscriptions and billing.|
|Workspace|View Currents Integration|Allows users to view all information about a Currents connection, excluding credentials. By default, users assigned the "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers" permission are also assigned this permission.|
|Workspace|View Custom Attributes Marked as PII|Allows this user to view custom attributes that are marked as PII without being an admin.|
|Workspace|View PII|Allows users to view the personally identifiable information (PII) fields as defined by your company within the dashboard. Users can also view PII fields in the **Preview as a User** tab of message previews. |
|Workspace|View User Profiles PII Compliant|Allows users to view user profiles but redacts fields your company has defined as personally identifiable information.|
|Workspace|View Transformations|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/).|
|Workspace|View Usage Data|Allows users to view app usage, including the channel performance dashboards.|
|Workspace|Merge Duplicate Users|Allows users to merge duplicate user profiles.|
|Workspace|Preview Duplicate Users|Allows users to preview which user profiles are duplicated.|
|Workspace|Create and Edit Canvas Templates|Allows users to create and edit Canvas templates.|
|Workspace|View Canvas Templates|Allows users to view Canvas templates.|
|Workspace|Archive Canvas Templates|Allows users to archive Canvas templates.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
