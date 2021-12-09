---
nav_title: Braze Account User Permissions
article_title: Braze Account User Permissions
page_order: 2
page_type: reference
description: "This reference article covers user permissions in Braze, such as choosing who can access your apps on the Braze dashboard."
tool: Dashboard
---

# Setting user permissions

Braze’s user permission feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin (designated by a yellow crown next to your username) or limited permission. The creator of the app group will automatically be granted Administrator access. These settings can be found by navigating to your name in the upper right corner of the dashboard and selecting "Manage Users" from the drop-down.

!\[User Permissions\]\[30\]

| Level of Access | Permissions                                                                                                                                                                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator   | Administrators have access to all available features.                                                                                                                                                                                                                                       |
| Limited         | Limited users are completely customized at several levels (outlined below). When you switch a user’s permissions from admin to limited, that user no longer has access to any portion of the Braze dashboard until you deem it so using the checkboxes that appear below the Edit User box. |
{: .reset-td-br-1 .reset-td-br-2}

## Editing user permissions

From the Manage Users page, you can edit a specific user’s permissions, either by allowing them to remain as the default Administrator role, or changing them to a Limited role. To change their role, click on the edit icon in the user’s row and select Limited from the User Role drop down.

!\[Edit User Permission\]\[29\]

When you switch a user’s permissions from Admin to Limited, that user no longer has access to any portion of Braze until you set those specific permissions using the checkboxes that appear below the Edit User box. Explanations for each of these permissions can be found in the Level of Access chart at the top of this page.

## Limited and team role permissions

You can manage user permissions by group or on an individual basis using the User Permissions page.

!\[userpermissions\]\[89\]

| Permission Name                                            | Definition/Parameters                                                                                                                                                                                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin                                                      | Has access to all available features, default setting for all new users. Can update company settings (company name and time zone), which Limited Users are unable to do.                                                                          |
| Access Campaigns, Canvases, Cards, Segments, Media Library | User can view campaign and Canvas performance metrics, create drafts of campaigns and canvases, view News Feed, segments, templates and media, create templates, upload media, and view engagement reports.                                       |
| Send Campaigns, Canvases                                   | Allows user to edit, archive, stop, duplicate campaigns and canvases, create campaigns, launch canvases. To launch existing content blocks, both **Send campaigns, Canvases** and **Publish Cards** permissions are required.                     |
| Publish Cards                                              | Allows user to create and edit News Feed cards. You can still view cards without this permission. To launch existing content blocks, both **Publish Cards** and **Send campaigns, Canvases** permissions are required.                            |
| Edit Segments                                              | Allows users to create and edit segment. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV. |
| Export User Data                                           | Allows user to export your user data from Segments, campaigns and Canvases.                                                                                                                                                                       |
| View PII                                                   | Allows user to view personally identifiable information within the dashboard. Note that both email addresses and phone number will be visible.                                                                                                    |
| View User Profile                                          | Allows user to access User Search page.                                                                                                                                                                                                           |
| Manage Dashboard Users                                     | Allows user to view, edit and manage the Manage Users tab. Users with this permission can modify the permissions of any user, including themselves. As such, this permission should be viewed as an administrative access level.                  |
| Manage Media Library                                       | Allows user to upload images to library. You can still upload pictures/audio etc. directly to a campaign without this permission.                                                                                                                 |
| View Usage Data                                            | Allows user to view app usage.                                                                                                                                                                                                                    |
| Import and Update User Data                                | Allows user to import CSV and update files of app users as well as view the User Import page.                                                                                                                                                     |
| View Billing Details                                       | Allows user to view subscriptions and billing.                                                                                                                                                                                                    |
| Access Dev Console                                         | Allows access to Developer Console (where you can view API keys, API campaign activity log, event user log, and internal groups for testing messages).                                                                                            |
| Manage External Integrations                               | Allows access to all tabs under Technology Partners and the ability to sync Braze with other platforms.                                                                                                                                           |
| Manage Apps                                                | Allows user to edit settings (under Manage Settings).                                                                                                                                                                                             |
| Manage Teams                                               | Allows user to manage teams which is under "Manage Settings". The ability to select this permission depends on your contract with Braze.                                                                                                          |
| Manage Events, Attributes, Purchases                       | Allows user to edit custom attributes, (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products (all under Manage Settings).                         |
| Manage Tags                                                | Allows users to edit or delete tags (under Manage Settings). You do not need this permission to add tags to campaigns or segments.                                                                                                                |
| Manage Email Settings                                      | Allows user to save email configuration changes (email settings tab under "Manage Settings").                                                                                                                                                     |
| Manage Subscription Groups                                 | Allows user to create and manage subscription groups.                                                                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2}

## App-by-app user permissions

Individual users can be granted different degrees of access on an app-by-app basis.

| Limited Permission Degree   | Details                                                     |
| --------------------------- | ----------------------------------------------------------- |
| Company Level               | Regarding managing the company's app and group settings.    |
| App Group Level Permissions | Which App Groups should the limited user be able to manage? |
| App Level Settings          | What level of editing access should this limited user have? |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission" [30]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %} [89]: {% image_buster /assets/img/user_permissions_selection.png %}
