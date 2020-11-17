---
nav_title: Braze Account User Permissions
page_order: 2
description: "Braze’s user permission feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin or limited permission."
---

# Setting User Permissions
Braze’s user permission feature allows you to choose who can access your apps on the Braze dashboard by assigning different users with either admin (designated by a yellow crown next to your username) or limited permission. The creator of the app group will automatically be granted Administrator access.

![User Permissions][30]

|Level of Access|Permissions|
|---|---|
|Administrator|Administrators have access to all available features.|
|Limited|Limited users are completely customized at several levels (outlined below). When you switch a user’s permissions from admin to limited, that user no longer has access to any portion of the Braze dashboard until you deem it so using the checkboxes that appear below the Edit User box.|
{: .reset-td-br-1 .reset-td-br-2}

## Editing User Permissions
From the Manage Users page, you can edit a specific user’s permissions, either by allowing them to remain as the default Administrator role, or changing them to a Limited role. To change their role, click on the edit icon in the user’s row and select Limited from the User Role drop down.

![Edit User Permission][29]

When you switch a user’s permissions from Admin to Limited, that user no longer has access to any portion of Braze until you set those specific permissions using the checkboxes that appear below the Edit User box. Explanations for each of these permissions can be found in the Level of Access chart at the top of this page.

# Available Limited and Team Role Permissions

You can manage user permissions by group or on an individual basis using the User Permissions page.

![userpermissions][89]

|Permission Name|Definition/Parameters|
|---|---|
|Admin|Has access to all available features, default setting for all new users. Can update company settings (company name and time zone), which Limited Users are unable to do.|
|Access Campaigns, Canvases, Cards, Segments, Media Library| User can view campaign and canvas performance metrics, create drafts of campaigns and canvases, view news feed, segments, templates and media, create templates, upload media, and view engagement reports.<br><br>__Note: Users must have "Send Campaigns, Canvases" permissions checked to have this permission work as intended.__ |
|Send Campaigns, Canvases| Allows user to edit, archive, stop, duplicate campaigns and canvases, create campaigns, launch canvases.<br><br>__Note: Users must have "Access Campaigns, Canvases, Cards, Segments, Media Library" permissions checked to have this permission work as intended.__ |
|Publish Cards| Allows user to create and edit news feed cards. (You can still view cards without this permission).|
|Edit Segments| Allows users to create and edit segment. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Export User Data| Allows user to export your user data from Segments.|
|View User Profile| Allows user to access User Search page.|
|Manage Dashboard Users| Allows user to view the Manage Users tab.|
|Manage Media Library| Allows user to upload images to library. You can still upload pictures/audio etc. directly to a campaign without this permission.|
|View Usage Data| Allows user to view app usage.|
|Import and Update User Data| Allows user to import CSV and update files of app users as well as view the User Import page.|
|View Billing Details| Allows user to view subscriptions and billing. |
|Access Dev Console| Allows access to Developer Console (where you can view API keys, API campaign activity log, event user log, and internal groups for testing messages).|
|Manage External Integrations| Allows access to all tabs under Technology Partners and the ability to sync Braze with other platforms.|
|Manage Apps| Allows user to edit app settings (under Manage App Group).|
|Manage Events, Attributes, Purchases|Allows user to edit custom attributes, (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products (all under manage app group).|
|Manage Tags|Allows users to edit or delete tags (under manage app group). You do not need this permission to add tags to campaigns or segments.|
|Manage Email Settings|Allows user to save email configuration changes (email settings tab under "manage app group").|
|Manage Teams|Allows user to manage teams which is under "Manage App Group". The ability to select this permission depends on your contract with Braze.|
{: .reset-td-br-1 .reset-td-br-2}

## App-by-App User Permissions

Individual users can be granted different degrees of access on an app-by-app basis.

|Limited Permission Degree|Details|
|---|---|---|
|Company Level|Regarding managing the company's app and group settings.|
|App Group Level Permissions|Which App Groups should the limited user be able to manage?|
|App Level Settings|What level of editing access should this limited user have? (See sample image below or further details [here][76].)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

![Permissions App to App][31]



[1]: https://dashboard-01.braze.com/company_settings/company_settings/ "Company Settings Page"
[6]: https://dashboard-01.braze.com/app_settings/app_settings/analytics_report/
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[8]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[24]: {{site.baseurl}}/support_contact/
[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/user_accesses_new.png %} "User Permissions"
[31]: {% image_buster /assets/img_archive/permission_diff_apps_new.png %} "Permissions App to App"
[33]: http://dashboard-01.braze.com/company_settings/manage_users/ "Manage Users Page"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %} "Delete a User"
[37]: http://dashboard-01.braze.com/company_settings/account_settings/ "Account Settings Page"
[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[45]: {% image_buster /assets/img_archive/Enable_reset.png %}
[49]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#user-permissions
[50]: {% image_buster /assets/img_archive/security_settings_new.png %}
[51]: {% image_buster /assets/img_archive/authentication_rules_new.png %}
[52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %}
[53]: {% image_buster /assets/img_archive/two_factor_authentication_new.png %}
[55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[56]: https://www.authy.com
[57]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}
[60]: http://www.list-unsubscribe.com/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.gif %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}

[69]: {% image_buster /assets/img_archive/manageappgroupnavigation1.png %}

[70]: {% image_buster /assets/img_archive/appsettingsview1.png %}

[71]: {% image_buster /assets/img_archive/customattributessearch1.png %}

[72]: {% image_buster /assets/img_archive/customeventsview1.png %}

[73]: {% image_buster /assets/img_archive/manageproperties1.png %}

[74]: {% image_buster /assets/img_archive/customeventsviewblacklist1.png %}

[75]: {% image_buster /assets/img_archive/customeventsviewdatatypedropdown1.png %}

[76]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/

[83]: https://dashboard-01.braze.com/company_settings/company_settings/security-management/
[84]: https://tools.ietf.org/html/rfc4632
[85]: https://lab.braze.com/braze-101
[89]: {% image_buster /assets/img/user_permissions_selection.png %}
