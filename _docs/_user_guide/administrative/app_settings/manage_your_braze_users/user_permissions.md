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

## How do permission sets and roles differ from Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Considerations for adding user permissions to Teams

You may encounter difficulties when trying to save permissions in the Braze dashboard, particularly when adding or removing users from a workspace, or adding them to a Team. The **Save/Update Users** button may become greyed out if the permissions for the user are identical to those they already have at the workspace level. This restriction exists because there is no benefit to having a Team if all users possess the same permissions as the entire workspace.

To successfully add a user to a Team while maintaining the same permissions, don't assign any permissions at the workspace level. Instead, assign permissions exclusively at the team level.

## Limited users

Limited users have specific permissions that allow them to manage certain aspects of the Braze dashboard while having restrictions compared to company admins and workspace admins.

| Permissions | Limited users can edit the permissions of other limited users if they have the "Manage Dashboard Users" permission checked. They can also create new limited users and modify their permission sets. However, they can't create or manage company admin accounts. |
| Role limitations | If a limited user has all permissions except "App Group Admin", they will still have access to all other permissions typically granted to an workspace admin. |
| Visibility of permissions | If a limited user has "Manage Dashboard Users" checked for one app group (such as Dev) but not for another (such as Prod), they won't see the Prod app group permissions in their "Manage Users" profile. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparing limited users

| Limited user type | Description |
| --- | --- |
| App group admin | App Group Admins have permissions specific to managing app groups but do not have the same authority as Company Admins. Limited Users can inherit permissions similar to those of App Group Admins if they have the necessary permissions checked. |
| Company admin | Company Admins have broader permissions, including the ability to delete dashboard users. However, they cannot delete their own accounts and must contact another Company Admin for that action. |
| Basic read-only permission | To access certain parts of the dashboard, such as the Technology Partners page, users must have a basic read-only permission. This includes having "Manage External Integrations" enabled, along with permissions for Access Campaigns, Canvases, Cards, Segments, and Media Library. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Limited access error

Users may encounter messages like "Limited Access. You do not have permissions to access this Page." In such cases, the account admin should check if they can resolve the issue by disabling and re-enabling the user's permissions.

{% alert note %}
It isn't possible to merge or import user permissions from one dashboard user to another.
{% endalert %}

## Editing a user's permissions

To edit a user's current admin, company, or workspace permissions, go to **Settings** > **Company Users**, then select their name.

![The "Company Users" page in Braze with one user listed in the results.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Admin

Admins have access to all features and the ability to modify any company setting. They can:

- Change [approval settings]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Add, edit, delete, suspend, or unsuspend other [Braze users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Export Braze users as a CSV

To grant or remove admin privileges, select **This user is an admin**, then select **Update user**.

![The details of the selected user with the admin checkbox in focus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
If you remove admin privileges from a user, they won't be able to access Braze until you assign them at least one [company-level](#company) or [workspace-level](#workspace) permission.
{% endalert %}

{% endtab %}
{% tab Company %}

### Company

To manage the following company-level permissions for a user, check or uncheck the box next to that permission. When you're finished, select **Update user**.

|Permission name|Description|
|----------|-----------|
|Manage company settings|Allows users to modify any company setting.|
|Create and delete workspaces|Allows users to create and delete workspaces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

You can give a user different permissions for each workspace they belong to in Braze. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually to select or assign a permission set [you previously created](#creating-a-permission-set).

If you need to give a user different permissions for different workspaces, repeat this process as many times as needed. For a description of each permission, see [List of permissions](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permissions**, choose one or more permissions from the dropdown. Braze assigns these permissions only for the workspaces you have selected. Optionally, you can select **Enable Admin Access** if you'd like to give them full permissions for this workspace instead.

When you're finished, select **Update user**.

![Workspace-level permissions being manually selected in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permission Sets**, choose one permission set. Braze assigns these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a permission set in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporting user permissions

To download a list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. A CSV file will be sent to your email address shortly.

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
|Workspace|Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers|Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of segments, templates and media, create templates, upload media, create or update promotion code lists, view engagement reports, and view global message settings in the dashboard. However, users with this permission cannot pause or edit existing live content.|
|Workspace|Access Dev Console|Allows full access to the following settings and logs:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API Keys</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Internal Groups</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Message Activity Log</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event User Log</a></li></ul>{:/}|
|Workspace|Approve and Deny Campaigns|Allows users to approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you're interested in participating in the early access.|
|Workspace|Approve and Deny Canvases|Allows users to approve or deny Canvases. The [approval workflow for Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply.|
|Workspace|Edit Currents Integrations|Allows users to modify a Currents connection, including credentials. By default, users assigned the "External Integrations" permission are also assigned this permission.|
|Workspace|Edit Segments|Allows users to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Workspace|Export User Data|Allows users to export their user data from segments, campaigns, and Canvases. This permission includes sensitive user information like names, email addresses, and other collected personally identifiable information (PII). To export CSVs from the dashboard, users need both this permission and the "View PII" permission.|
|Workspace|Import and Update User Data|Allows users to import CSV and update files of app users as well as view the User Import page. This also allows you to edit the subscription status of a user and their subscription group opt-in/opt-out rules.|
|Workspace|Launch and Manage Content Blocks|Allows users to launch and manage [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Workspace|Launch Preference Centers|Allows users to launch [preference centers]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Workspace|Manage Apps|Allows users to edit **App Settings**.|
|Workspace|Manage Catalogs Dashboard Permission|Allows users to create and manage catalogs.|
|Workspace|Manage Dashboard Users| Allows non-admins the ability to view, edit, and manage the **Company Users** page, and manage the dashboard users in their workspace by modifying the permissions of any user, including themselves. Users with this permission can’t delete users (only administrators can delete users).<br><br>This corresponds to the legacy permission `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Workspace|Manage Email Settings|Allows users to save email configuration changes (**Settings** > **Email Preferences**).|
|Workspace|Manage Events, Attributes, Purchases|Allows users to edit custom attributes (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**.|
|Workspace|Manage External Integrations|Allows access to all tabs under **Technology Partners**, ability to sync Braze with other platforms, and access to manage [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Workspace|Manage Feature Flags|Allows users to create or edit [feature flags]({{site.baseurl}}/developer_guide/feature_flags/).|
|Workspace|Manage Media Library Assets|Allows users to add, edit, and delete media library assets.|
|Workspace|Manage Subscription Groups|Allows users to create and manage subscription groups.|
|Workspace|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Workspace|Manage Teams|Allows users to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.<br><br>This corresponds to the legacy permission `MANAGE_TERRITORIES`.|
|Workspace|Manage Transformations|Allows users to create and manage Data Transformations.|
|Workspace|Send Campaigns, Canvases|Allows users to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases. |
|Workspace|View Billing Details|Allows users to view subscriptions and billing.|
|Workspace|View Currents Integration|Allows users to view all information about a Currents connection, excluding credentials. By default, users assigned the "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers" permission are also assigned this permission.|
|Workspace|View Custom Attributes Marked as PII|Allows non-admin users to view custom attributes that contain sensitive information and are marked as personally identifiable information (PII).|
|Workspace|View PII|Allows users to view personally identifiable information (PII) fields as defined by your company within the dashboard. Users can also view PII fields in the **Preview as a User** tab of message previews.<br><br>You need this permission to use [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), because it allows direct access to some customer data. To export CSVs from the dashboard, users need both this permission and the "Export User Data" permission.|
|Workspace|View User Profiles PII Compliant|Allows users to view user profiles that contain fields your company has defined as personally identifiable information (PII), but redacts the PII fields.<br><br>You need this permission to use the user search tool. |
|Workspace|View Transformations|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Workspace|View Usage Data|Allows users to view app usage, including the channel performance dashboards.|
|Workspace|Merge Duplicate Users|Allows users to merge duplicate user profiles.|
|Workspace|Preview Duplicate Users|Allows users to preview which user profiles are duplicated.|
|Workspace|Create and Edit Canvas Templates|Allows users to create and edit Canvas templates.|
|Workspace|View Canvas Templates|Allows users to view Canvas templates.|
|Workspace|Archive Canvas Templates|Allows users to archive Canvas templates.|
|Workspace|Manage Custom Event Property Segmentation|Allows users to create segments based on event property recency and frequency.|
|Workspace|Publish Landing Pages|Allows users to publish [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Workspace|Create Landing Page Drafts|Allows users to create and save landing page drafts.|
|Workspace|Access Landing Pages|Allows users to access the **Landing Pages** page.|
|Workspace|Create and Edit Landing Page Templates|Allows users to create and edit landing page templates.|
|Workspace|View Landing Page Templates|Allows users to view landing page templates.|
|Workspace|Archive Landing Page Templates|Allows users to archive landing page templates.|
|Workspace|View Custom AI Agents|Allows users to view [custom AI agents]({{site.baseurl}}/user_guide/brazeai/agents/). This feature is currently in beta.|
|Workspace|Create Custom AI Agents|Allows users to create custom AI agents. This feature is currently in beta.|
|Workspace|Edit Custom AI Agents|Allows users to edit custom AI agents. This feature is currently in beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
