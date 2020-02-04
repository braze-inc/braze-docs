---
nav_title: Teams
page_order: 4
---

# Teams

Braze Admins can divide subsets of their Dashboard users into Teams with varying user roles and permissions. Teams can be set up across customer base location, language, and custom attributes such that members and non-members have different access to messaging features and customer data. With Teams, Braze Admins will be able to restrict a Braze User’s access and permit or deny them the ability to perform different actions depending on their Team membership.

## Adding a New Team

Go to the __Manage App Group Page__ and click __Manage Teams__. From there, you will see an option to __+Add Team__ that then populates a modal window. Here you will not only give the Team a name, but also have the option to use a Custom Attribute, Country, or Language to further define the access that will be granted.

![adding_a_team][68]

## Team Roles
Teams introduces a new user Role to the Dashboard. Braze Admins can assign Team Roles to their Dashboard users, who are limited to only read/write data available to their particular Teams. Predefined Team Roles include language and location (by Countries and Regions).

## User Permissions by Team or App
Individual users can be granted different degrees of access on an app-by-app basis. For more on setting user permissions and a breakdown of those permissions, check out our User Permissions section.

|Limited Permission Degree|Details |
|---|---|
|Company Level|Regarding managing the company’s app and group settings. |
|App Group Level Permissions|Which App Groups should the limited user be able to manage? |
|App Level Settings|What level of editing access should this limited user have? |

## Tags and Filters
Dashboard objects can be organized by Teams. Canvases, Campaigns, Cards, Segments, email templates, and media library assets can be labeled with a Team Tag. Similarly, a Team Filter can also be used to search for the following objects: Canvases, Campaigns, Cards, and Segments.

Teams is not available on all Braze contracts. If you’d like to access this feature, reach out to your account executive and customer success manager or contact us at hello@braze.com for a consultation.

## Archive an Existing Team
Teams can be archived by going to the Manage App Group > Manage teams page.  Select one or many teams to archive.

If the team is not associated with any object within Braze, the team will be archived immediately.
If the team is associated with an object, you will be presented with an option to 'remove the team after the archive process' or 'replace the team with another team' 
![archive_a_team][86]

Admins can unarchive a team by selecting the archived team and then clicking the unarchived button.



[1]: https://dashboard-01.braze.com/company_settings/company_settings/ "Company Settings Page"
[6]: https://dashboard-01.braze.com/app_settings/app_settings/analytics_report/
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[8]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[24]: {{ site.baseurl }}/support_contact/
[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/user_accesses_new.png %} "User Permissions"
[31]: {% image_buster /assets/img_archive/permission_diff_apps_new.png %} "Permissions App to App"
[33]: http://dashboard-01.braze.com/company_settings/manage_users/ "Manage Users Page"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %} "Delete a User"
[37]: http://dashboard-01.braze.com/company_settings/account_settings/ "Account Settings Page"
[43]: {{ site.baseurl }}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[45]: {% image_buster /assets/img_archive/Enable_reset.png %}
[49]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#user-permissions
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

[76]: {{ site.baseurl }}/user_guide/administrative/manage_your_braze_users/user_permissions/

[83]: https://dashboard-01.braze.com/company_settings/company_settings/security-management/
[84]: https://tools.ietf.org/html/rfc4632
[85]: https://lab.braze.com/braze-101
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
