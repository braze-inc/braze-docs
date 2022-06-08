---
nav_title: View PII User permission
permalink: /view_pii/
hidden: true
---

# View PII

This article covers a new permission that is only accessible for a few select customers. For the existing team permission capabilities, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## How it works

By default, all admins will have their **View PII** permission enabled. This means they can see email addresses and phone numbers throughout the dashboard.
When this permission is disabled, developers are not able to see any email addresses or phone numbers throughout the Braze dashboard.

## Limited Areas

|Dashboard Navigation| Result| Notes|
|--------------------|-------|------|
| User Search | The developer who logs in is not able to search by email address or phone number anymore:<br><br>**&#45;** Cannot be shown the email address or phone number when viewing a user profile.<br><br>**&#45;** Cannot edit the email address or phone number of a user profile from the Braze dashboard.| Access to this section still requires access to view user profile. |
| User Import | The developer can't download files from the **User Import** page. | |
| Segments/Campaign/Canvas | In the **User Data** dropdown: <br><br>**&#45;** The developer won't have the **CSV Export Email Address** option. <br><br>**&#45;** The developer won't be provided with the email address or phone number in the CSV file when selecting **CSV Export User Data**. | |
| Internal Test Group | The developer won't have access to the email address of any user added to the internal test group. | | 
| Message Activity Log | The developer won't have access to the email address or phone number for any users identified via the message activity log. | | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

![A user profile with a hidden email address and phone number, indicating that the current developer permissions does not have View PII enabled.][1]{: style="max-width:60%"}

![The View PII checkbox is selected, which allows user email addresses and phone numbers to be visible.][2]{: style="max-width:60%"}

![The User Data dropdown with two download options: CSV Export All Recipient Data and CSV Export Recipient Email Addresses.][3]{: style="max-width:60%"}

{% alert note %}
When previewing a message, the **View PII** permission is not applied, so developers can see the email address or phone number if they were referenced in the message via Liquid.
{% endalert %}

[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

