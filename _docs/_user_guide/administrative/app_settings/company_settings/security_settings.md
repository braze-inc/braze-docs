---
nav_title: Security Settings
article_title: Security Settings
page_order: 2
page_type: reference
description: "This reference article covers generic cross-company security settings, including authentication rules, IP whitelisting, PII, and two-factor authentication (2FA)."

---

# Security settings

> As an admin, security is a high priority on your list of concerns. This page can help you manage the generic, cross-company security settings, including authentication rules, IP whitelisting, and two-factor authentication.

To access this page, go to **Settings** > **Admin Settings** > **Security Settings**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), select your account dropdown and go to **Company Settings** > **Security Settings**.
{% endalert %}

## Authentication rules

### Password length

The default minimum length is eight characters.

### Password complexity

Require passwords to include at least one of each of the following: 
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

## Dashboard IP whitelisting

Use the field shown to whitelist specific IP addresses and subnets from which users can log in to your account (for example, from a company network or VPN). Specify IP addresses and subnets as CIDR ranges in a comma-separated list. If not specified, users will be able to log in from any IP address.

## Two-factor authentication

Two-factor authentication adds a second level of identity verification to an account log, making it more secure than just a username and password.

When two-factor authentication is turned on, in addition to entering a password, users will need to enter a verification code when logging in to their Braze account. The code can be sent via an authenticator app, email, or SMS.

Two-factor authentication can be optional for admins, and enabled for non-admin users by default. However, when turned on, users who fail to set up their two-factor authentication will be locked out of their Braze account. Braze account users also can set up two-factor authentication on their own in **Account Settings**, even if not required by the administrator.

### Remember me

![Remember this account for 30 days checkbox][04]{: style="float:right;max-width:40%;margin-left:15px;"}

After toggling on two-factor authentication for your company, the **Remember Me** checkbox becomes available to users. This feature stores a cookie on your device, only requiring you to log in with two-factor authentication once over the course of 30 days.

Customers with multiple accounts under a dashboard company may experience issues using this feature due to the cookie being tied to a specific device. If users use the same device to log in to multiple accounts, the cookie will be replaced for the previously authorized accounts on that device. Braze expects only one device to be associated with an account, not one device for multiple accounts.

Be sure to save your changes before leaving the page!

### Resetting user authentication

Users experiencing issues logging in via two-factor authentication can reach out to their company admins to reset their two-factor authentication. To do this, have an admin perform the following steps:

1. Navigate to **Manage Users**.
2. Select the user from the provided list.
3. Select **Reset** under **Two Factor Authentication**.

A reset can solve common authentication issues such as trouble with authenticator apps, email verification not sending, login failure due to SMS outages or user error, and more.

#### Two-factor authentication enforcement

- If two-factor authentication is not enforced at the company level, when reset, the user will log in normally and need to go to **Account Settings** to turn on and set up two-factor authentication.
- If two-factor authentication is enforced at the company level, the next time the user logs in, they’ll be asked to set up their two-factor authentication.

## Downloading a security event report

The Security Event report is a CSV report of security events such as account invitations, account removals, failed and successful login attempts, and other activities. 

To download this report, do the following:

1. Go to your user profile and select **Company Settings**.
2. Select the **Security Settings** tab and go to the **Security Event Download** section.
2. Select **Download report**. 

This report only contains the most recent 10,000 security events for your account. If you need specific event data, contact technical support.

## Viewing personally identifiable information (PII)

The **View PII** permission is only accessible to a few select Braze users. For the existing team permission capabilities, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

By default, all admins have their **View PII** permission enabled in [user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). This means they can see the following standard and custom attributes throughout the dashboard. When this permission is disabled for users, those users will not be able to see this information.

### Defining PII

Braze allows you to define which fields are designated as PII in your dashboard. To do this, navigate to **Company Settings > Security Settings**.

The following fields can be hidden from Braze users who don't have **View PII** permissions.

| Standard attributes | Custom attributes |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Email address </li> <li> Phone number </li> <li> First name </li> <li> Last name </li> <li> Gender </li> <li> Birthday </li> <li> Device IDs </li> <li> Most recent location </li> </ul> {:/} | {::nomarkdown} <ul> <li> All custom attributes </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

### Limited areas

The following assumes that all fields are set as PII and the users mentioned are those that use the Braze platform.

| Dashboard Navigation | Result | Notes |
| -------------------- | ------ | ----- |
| User search | The user who logs in is unable to search by email address, phone number, first name, or last name: {::nomarkdown} <ul> <li> Will not be shown the preceding standard and custom attributes when viewing a user profile. </li> <li> Cannot edit the preceding standard attributes of a user profile from the Braze dashboard. </li> </ul> {:/} | Access to this section still requires access to view the user profile. |
| User import | The user can't download files from the **User Import** page. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | In the **User Data** dropdown: {::nomarkdown} <ul> <li> The user won't have the <b>CSV Export Email Address</b> option. </li> <li> The user won't be provided the preceding standard and customer attributes in the CSV file when selecting <b>CSV Export User Data</b>. </li> </ul> {:/} | |
| Internal test group | The user won't have access to the preceding standard attributes of any user added to the internal test group. | |
| Message activity log | The user won't have access to the preceding standard attributes for any users identified in the message activity log. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
When previewing a message, the **View PII** permission is not applied, so users can see the preceding standard attributes if they were referenced in the message via Liquid.
{% endalert %}


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/