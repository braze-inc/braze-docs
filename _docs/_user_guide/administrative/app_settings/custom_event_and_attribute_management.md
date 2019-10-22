---
nav_title: Custom Event and Attribute Management
page_order: 2
---

# Custom Event and Attribute Management

## Adding Custom Attributes, Custom Events, Products, and Event Properties

To add a custom attribute, event, or product, go to the Custom Attributes, Custom Events, or Products pages, respectively, under “Manage App Groups” by clicking the “Add ..” button on the upper right hand corner of the lists of data. This will enable tracking on it.

![customattributessearch1.png][71]


You can also add event properties for custom events or products by clicking on the “Manage Properties” link in the “Event Properties” column:

![customeventsview1.png][72]
![manageproperties1.png][73]

To make these added custom attributes, events, products, or event properties trackable, you must ask your developer to create it in the SDK using the exact name you used to add it earlier. Or, you may use Braze's APIs to import data on that attribute. After that, the custom attribute, event, or other will be actionable and apply to your users!

{% alert note %}
All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. Custom Event Properties are stored and available for Segmentation for thirty (30) days. If you'd like to leverage Event Properties for Segmentation, please contact your Braze account or customer success manager. 
{% endalert %}

## Blacklisting Custom Attributes, Custom Events, and Products
If you want to stop tracking a specific custom attribute/custom event/product (e.g., accidental creation during testing, no longer useful), search for it in the Custom Events tab, then click Blacklist.

![customeventsviewblacklist1.png][74]

Once a custom event or attribute is blacklisted,
- No data will be collected regarding that event/attribute,
- Existing data will not be wiped,
- Blacklisted events/attributes will not show up in filters or graphs.

Changes to the blacklist may take a few minutes to propagate. You may re-enable any blacklisted event or attribute at anytime.

{% alert note %}
Please note that you should still remove the event/attribute from your app code during your next release.
{% endalert %}

## Forcing Data Type Comparisons
Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it really is. Click on the dropdown in the Data Type column to choose.

![customeventsviewdatatypedropdown1.png][75]

If you elect to force the data type for an attribute, any data that comes in that isn't the specified type will be ignored.

For more information on specific filter options exposed by different data type comparisons please see ["Configuring Reporting - Braze Academy"][43]. And for more information on the different available data types, please see the section on ["Custom Attribute Data Types"][44].

{% alert note %}
Please note that data sent to Braze is immutable and cannot be deleted or modified once we've received it. However, you can use any of the steps listed above to exercise control over what you're tracking in your dashboard.
{% endalert %}

[1]: https://dashboard-01.braze.com/company_settings/company_settings/ "Company Settings Page"
[2]: {% image_buster /assets/img_archive/add_new_user_company_settings.png %} "Add a New User"
[3]: {% image_buster /assets/img_archive/subscribe_delete_company_settings.png %} "Delete an Existing User"
[4]: {% image_buster /assets/img_archive/company_email_settings_new.png %}
[5]: {% image_buster /assets/img_archive/custom_event_report.png %}
[6]: https://dashboard-01.braze.com/app_settings/app_settings/analytics_report/
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[8]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[18]: {% image_buster /assets/img_archive/rename_app_group_new.png %}
[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[23]: {% image_buster /assets/img_archive/appboy_weekly_report_example.png %}
[24]: {{ site.baseurl }}/support_contact/
[27]: {% image_buster /assets/img_archive/add_new_user1_new.png %} "Add a New User1"
[28]: {% image_buster /assets/img_archive/add_new_user2_new.png %} "Add a New User2"
[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Edit User Permission"
[30]: {% image_buster /assets/img_archive/user_accesses_new.png %} "User Permissions"
[31]: {% image_buster /assets/img_archive/permission_diff_apps_new.png %} "Permissions App to App"
[33]: http://dashboard-01.braze.com/company_settings/manage_users/ "Manage Users Page"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %} "Delete a User"
[35]: {% image_buster /assets/img_archive/weekly_report1_new.png %} "Analytics Report 1"
[36]: {% image_buster /assets/img_archive/weekly_report2_new.png %} "Analytics Report 2"
[37]: http://dashboard-01.braze.com/company_settings/account_settings/ "Account Settings Page"
[41]: {% image_buster /assets/img_archive/blacklist_new.png %}
[42]: {% image_buster /assets/img_archive/force_data_type_new.png %}
[43]: {{ site.baseurl }}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[45]: {% image_buster /assets/img_archive/Enable_reset.png %}
[46]: {% image_buster /assets/img_archive/Reset_Password.png %}
[47]: {% image_buster /assets/img_archive/create-custom-attributes_new.png %}
[48]: {% image_buster /assets/img_archive/create-event-properties_new.png %}
[49]: {{ site.baseurl }}/user_guide/onboarding/platform_administrative_features/#user-permissions
[50]: {% image_buster /assets/img_archive/security_settings_new.png %}
[51]: {% image_buster /assets/img_archive/authentication_rules_new.png %}
[52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %}
[53]: {% image_buster /assets/img_archive/two_factor_authentication_new.png %}
[54]: {% image_buster /assets/img_archive/two_factor_authentication_account_settings.png %}
[55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[56]: https://www.authy.com
[57]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[58]: {% image_buster /assets/img_archive/list_unsub_img2.png %}
[59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}
[60]: http://www.list-unsubscribe.com/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.gif %}
[66]: {% image_buster /assets/img_archive/enter_url_f.png %}
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

[77]: {% image_buster /assets/img_archive/okta_addapplication1.png %}
[78]: {% image_buster /assets/img_archive/okta_addapplication2.png %}
[79]: {% image_buster /assets/img_archive/okta_entersetup1.png %}
[80]: {% image_buster /assets/img_archive/okta_entersetup2.png %}
[81]: {% image_buster /assets/img_archive/okta_companysettings.png %}
[82]: {% image_buster /assets/img_archive/okta_assignusers.png %}
[83]: https://dashboard-01.braze.com/company_settings/company_settings/security-management/
[84]: https://tools.ietf.org/html/rfc4632
[85]: https://lab.braze.com/braze-101
