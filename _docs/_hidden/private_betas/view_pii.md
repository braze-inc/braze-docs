---
nav_title: View PII User permission
permalink: /view_pii/
hidden: true
---

# View PII

This will cover a new permission that is only accessible for a few select customers.  You can read about the existing team permission capabilities [here](https://www.braze.com/docs/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## How it works

By default, all admins will have their 'view pii' permission enabled.  This means they can see email address and phone numbers throughout the dashboard.
When this permission is disabled developers are not able to see the email address or phone number throughout the dashboard.


## Limited Areas

|Dashboard Navigation| Result| Notes|
|--------------------|-------|------|
|User Search| The developer who logs in is not able to search by email address or phone number anymore.  <ul><li>Can not be shown the email address or phone number when viewing a user profile</li><li>Can not edit the email address or phone number of a user profile from the dashboard</li></ul> | Access to this section, still requires access to 'view user profile' permission|
|User Import| The developer no longer can download files from the user import page| |
|Segments/Campaign/Canvas |Under the User Data Dropdown 
<ul><li>The developer no longer sees an option for 'CSV Export Email Address"</li><li>The developer will no longer be provided with the email address or phone number in the csv file, when selecting "CSV Export User Data"</li></ul>||
|Internal Test Group| The developer no longer can see the email address of any user added to the internal test group | | 
|Message Activity Log | The developer will no longer see email address or phone number for any users identified via the messsage activity log | | 

## Images

!User Profile page [1]

!New User Permission [2] 

!User Data Download options [3]

**Note**

When previewing a message, the "view pii" permission is not applied, thus developers can see the email address or phone number if they were referenced in the message via liquid.

 [1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
 [2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
 [3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

