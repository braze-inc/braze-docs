---
nav_title: View PII User permission
permalink: /view_pii/
hidden: true
---

# View PII

This will cover a new permission that is only accessible for a few select customers.  You can read about the existing team permission capabilities [here]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## How it works

By default, all admins will have their 'view pii' permission enabled.  This means they can see email addresses and phone numbers throughout the dashboard. When this permission is disabled, developers are not able to see the email address or phone number throughout the dashboard.

## Limited Areas

| Dashboard Navigation     | Result                                                                                                                                                                                                                                                                                                                         | Notes                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| User Search              | The developer who logs in is not able to search by email address or phone number anymore:<br><br>__&#45;__ Can not be shown the email address or phone number when viewing a user profile<br><br>__&#45;__ Can not edit the email address or phone number of a user profile from the dashboard | Access to this section, still requires access to 'view user profile' permission |
| User Import              | The developer no longer can download files from the user import page                                                                                                                                                                                                                                                           |                                                                                 |
| Segments/Campaign/Canvas | Under the User Data Dropdown: <br><br>__&#45;__ The developer no longer sees an option for 'CSV Export Email Address"<br><br>__&#45;__ The developer will no longer be provided with the email address or phone number in the CSV file, when selecting "CSV Export User Data"                  |                                                                                 |
| Internal Test Group      | The developer no longer can see the email address of any user added to the internal test group                                                                                                                                                                                                                                 |                                                                                 |
| Message Activity Log     | The developer will no longer see the email address or phone number for any users identified via the message activity log                                                                                                                                                                                                       |                                                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Images

!\[User Profile page\]\[1\]{: style="max-width:60%"}

!\[New User Permission\]\[2\]{: style="max-width:60%"}

!\[User Data Download options\]\[3\]{: style="max-width:60%"}

{% alert note %}
When previewing a message, the "view pii" permission is not applied, thus developers can see the email address or phone number if they were referenced in the message via Liquid.
{% endalert %}

 [1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1" [2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2" [3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

