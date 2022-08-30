---
nav_title: View PII User permission
permalink: /view_pii/
hidden: true
---

# View PII

> This article covers a permission only accessible to a few select customers. For the existing team permission capabilities, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## Define PII

Braze allows you to define which fields are designated as personally identifiable information (PII) in your dashboard. To do this, navigate to **Company Settings > Security Settings**.

The following fields can be hidden from Braze users who don't have **View PII** permissions.

| Standard attributes | Custom attributes |
| ------------------- | ----------------- |
| - Email address<br>- Phone number<br>- First name<br>- Last name<br>- Gender<br>- Birthday<br>- Device IDs<br>- Most recent location | - All custom attributes |
{: .reset-td-br-1 .reset-td-br-2}

By default, all admins will have their **View PII** permission enabled. This means they can see all standard and custom attributes throughout the dashboard. When this permission is disabled for users in [user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions), those users will not be able to see this information.

## Limited areas

The following assumes all fields are set as PII and that the users mentioned are those that use the Braze platform.

| Dashboard Navigation | Result | Notes |
| -------------------- | ------ | ----- |
| User search | The user who logs in is unable to search by email address, phone number, first name, or last name:<br><br>• Will not be shown the preceding standard and custom attributes when viewing a user profile.<br><br>• Cannot edit the preceding standard attributes of a user profile from the Braze dashboard.| Access to this section still requires access to view the user profile. |
| User import | The user can't download files from the **User Import** page. | |
| Segments<br>Campaigns<br>Canvas | In the **User Data** dropdown:<br><br>• The user won't have the **CSV Export Email Address** option.<br><br>• The user won't be provided the preceding standard and customer attributes in the CSV file when selecting **CSV Export User Data**. | |
| Internal test group | The user won't have access to the preceding standard attributes of any user added to the internal test group. | |
| Message activity log | The user won't have access to the preceding standard attributes for any users identified in the message activity log. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
When previewing a message, the **View PII** permission is not applied, so users can see the preceding standard attributes if they were referenced in the message via Liquid.
{% endalert %}

[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

