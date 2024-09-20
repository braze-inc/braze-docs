---
nav_title: Security Settings
article_title: Security Settings
page_order: 2
page_type: reference
description: "This reference article covers generic cross-company security settings, including authentication rules, IP allowlisting, PII, and two-factor authentication (2FA)."

---

# Security settings

> As an administrator, security is a high priority on your list of concerns. The **Security Settings** page can help you manage the generic, cross-company security settings, including authentication rules, IP allowlisting, and two-factor authentication.

To access this page, go to **Settings** > **Admin Settings** > **Security Settings**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), select your account dropdown and go to **Company Settings** > **Security Settings**.
{% endalert %}

## Authentication rules

### Password length

Use this field to change the minimum password length required. The default minimum is eight characters.

### Password complexity

Select **Enforce complex passwords** to require passwords to include at least one of each of the following: 
- Uppercase letter
- Lowercase letter
- Number
- Special character

### Password reusability

Determines the minimum number of new passwords that must be set before a user can reuse a password. The default is three.

### Password expiration rules

Use this field to set when you want your Braze account users to reset their password.

### Session duration rules

Use this field to define how long Braze will keep your session active. After Braze deems your session inactive (no activity for the defined number of minutes), the user will be logged out. The maximum number of minutes you can enter is 10,080 (equal to one week) if two-factor authentication is enforced for your company, otherwise the maximum session duration will be 1,440 minutes (equal to 24 hours).

### Single sign-on (SSO) authentication

You can restrict your users from logging in using a password or SSO.

For [SAML SSO][15], customers need to set up their SAML settings prior to enforcing. If customers use Google SSO, they only need to enforce the security settings page with no additional lift.

## Dashboard IP allowlisting

Use the field shown to allowlist specific IP addresses and subnets from which users can log in to your account (for example, from a company network or VPN). Specify IP addresses and subnets as CIDR ranges in a comma-separated list. If not specified, users will be able to log in from any IP address.

## Two-factor authentication

Two-factor authentication is required for all Braze users. It adds a second level of identity verification to an account log, making it more secure than just a username and password. If your dashboard cannot support two-factor authentication, contact your customer success manager. 

When two-factor authentication is turned on, in addition to entering a password, users will need to enter a verification code when logging in to their Braze account. The code can be sent via an authenticator app, email, or SMS.

Users who fail to set up their two-factor authentication will be locked out of their Braze account. Braze account users also can set up two-factor authentication on their own in **Account Settings**, even if not required by the administrator.

### Remember me

![Remember this account for 30 days checkbox][04]{: style="float:right;max-width:40%;margin-left:15px;"}

After toggling on two-factor authentication for your company, the **Remember Me** checkbox becomes available to users. This feature stores a cookie on your device, only requiring you to log in with two-factor authentication once over the course of 30 days.

Customers with multiple accounts under a dashboard company may experience issues using this feature due to the cookie being tied to a specific device. If users use the same device to log in to multiple accounts, the cookie will be replaced for the previously authorized accounts on that device. Braze expects only one device to be associated with an account, not one device for multiple accounts.

Be sure to save your changes before leaving the page!

### Resetting user authentication

Users experiencing issues logging in with two-factor authentication can contact their company administrators to reset their two-factor authentication. To do this, have an administrator perform the following steps:

1. Go to **Settings** > **Company Users**.
2. Select the user from the provided list.
3. Select **Reset** under **Two Factor Authentication**.

A reset can solve common authentication issues such as trouble with authenticator apps, email verification not sending, login failure due to SMS outages or user error, and more.

## Downloading a security event report

The Security Event report is a CSV report of security events such as account invitations, account removals, failed and successful login attempts, and other activities. You can use it to perform internal audits.

To download this report, do the following:

1. Go to **Settings** > **Admin Settings**.
2. Select the **Security Settings** tab and go to the **Security Event Download** section.
2. Select **Download report**. 

This report only contains the most recent 10,000 security events for your account. If you need specific event data, contact technical support.

{% details Reported security events %}
### Login and account 
- REMOVED_DEVELOPER_EVENT
- ADDED_DEVELOPER_EVENT
- SIGNED_IN_EVENT
- FAILED_LOGIN_EVENT
- TWO_FACTOR_AUTH_SETUP_COMPLETED
- TWO_FACTOR_AUTH_RESET_COMPLETED
- CLEARED_DEVELOPER_TWO_FACTOR_AUTH_EVENT
- DEVELOPER_SUSPENDED_EVENT
- DEVELOPER_UNSUSPENDED_EVENT

### Elevated access
- ELEVATED_ACCESS_FLOW_STARTED_EVENT
- ELEVATED_ACCESS_FLOW_COMPLETED_EVENT
- ELEVATED_ACCESS_FLOW_2FA_FAILED_EVENT

### Campaign
- ADDED_CAMPAIGN_EVENT
- EDITED_CAMPAIGN_EVENT

### Canvas
- ADDED_WORKFLOW_EVENT
- EDITED_WORKFLOW_EVENT

### Segment
- ADDED_SEGMENT_EVENT
- EDITED_SEGMENT_EVENT
- EXPORTED_SEGMENT_TO_CSV
- EXPORTED_SEGMENT_VIA_API

### REST API key
- ADDED_REST_API_KEY
- REMOVED_REST_API_KEY

### Basic authentication credential
- ADDED_BASIC_AUTH_CREDENTIAL
- UPDATED_BASIC_AUTH_CREDENTIAL
- REMOVED_BASIC_AUTH_CREDENTIAL

### Permission
- CLEARED_DEVELOPER_TWO_FACTOR_AUTH_EVENT
- UPDATED_DEVELOPER_PERMISSION_EVENT

### Company settings
- ADDED_APP_GROUP
- ADDED_APP_EVENT

### Email template
- ADDED_EMAIL_TEMPLATE
- UPDATED_EMAIL_TEMPLATE

### Push credential
- UPDATED_PUSH_CREDENTIAL
- REMOVED_PUSH_CREDENTIAL

### SDK Debugger
- STARTED_SDK_DEBUGGER_SESSION
- EXPORTED_SDK_DEBUGGER_LOGS
{% enddetails %}

## Viewing personally identifiable information (PII) {#view-pii}

The **View PII** permission is only accessible to a few select Braze users. For the existing team permission capabilities, refer to [Setting user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

By default, all admins have their **View PII** permission turned on in [user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). This means they can see the following standard and custom attributes throughout the dashboard. When this permission is turned off for users, those users won't be able to see this information.

### Defining PII

You can define which fields are designated as PII in the dashboard. To do this, go to **Company Settings** > **Security Settings**.

The following fields can be hidden from Braze users who don't have **View PII** permissions.

| Standard attributes | Custom attributes |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Email address </li> <li> Phone number </li> <li> First name </li> <li> Last name </li> <li> Gender </li> <li> Birthday </li> <li> Device IDs </li> <li> Most recent location </li> </ul> {:/} | {::nomarkdown} <ul> <li> All custom attributes<ul><li>Individual custom attributes can be marked as PII if you don't need to hide all attributes.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

### Limited areas

The following assumes that all fields are set as PII and the users mentioned are those that use the Braze platform.

| Dashboard Navigation | Result | Notes |
| -------------------- | ------ | ----- |
| User search | The user who logs in is unable to search by email address, phone number, first name, or last name: {::nomarkdown} <ul> <li> Won't be shown the preceding standard and custom attributes when viewing a user profile. </li> <li> Can't edit the preceding standard attributes of a user profile from the Braze dashboard. </li> </ul> {:/} | Access to this section still requires access to view the user profile. |
| User import | The user can't download files from the **User Import** page. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | In the **User Data** dropdown: {::nomarkdown} <ul> <li> The user won't have the <b>CSV Export Email Address</b> option. </li> <li> The user won't be provided the preceding standard and customer attributes in the CSV file when selecting <b>CSV Export User Data</b>. </li> </ul> {:/} | |
| Internal test group | The user won't have access to the preceding standard attributes of any user added to the internal test group. | |
| Message activity log | The user won't have access to the preceding standard attributes for any users identified in the message activity log. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
When previewing a message, the **View PII** permission isn't applied, so users can see the preceding standard attributes if they were referenced in the message through Liquid.
{% endalert %}

## Data deletion preferences 

You can use this setting to set preferences for whether certain fields should be deleted during the user delete process for events. These preferences only impact data for users that have been deleted from Braze. 

When a user is deleted, Braze removes all PII from events data but retains the anonymized data for analytics purposes. Some user-defined fields may contain PII if you send end-user information to Braze. If these fields contain PII, you can opt to delete the data when event data is anonymized for deleted users; if the fields contain no PII, they can be retained for analytics.

You are responsible for determining the correct preferences for your workspace. The best way to determine the appropriate settings is to review with internal teams sending events data to Braze and to teams using message extras in Braze to confirm whether the fields may contain PII.  

### Relevant fields  

| Event name or type | Field | Notes |
| -------------------- | ------ | ----- |
| Custom event | properties |  |
| Purchase event | properties |  |
| Message send | message_extras | Several event types contain a message_extras field. The preference applies to all message send event types that support message_extras, including event types added in the future. |

{% alert warning %}
**Deletion is permanent!** If you opt to remove any fields from Snowflake for deleted users, the setting will apply to all historical data in your workspaces and any events for users deleted in the future. After Braze has run the process to apply the settings to historical event data for deleted users, the data **cannot be restored**.
{% endalert %}

### Configure preferences

Set default preferences by checking boxes for any fields that should be removed if a user is deleted. Select any of the fields that contain PII. This preference will apply to all current and future workspaces unless workspaces are explicitly added to a preference group.

To customize preference by workspace, you may add preference groups with different settings from the default. We apply the default settings to any workspaces not added to an additional preference group, including workspaces created in the future.  

![]({% image_buster /assets/img/deletion_preferences_1.png %})


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
