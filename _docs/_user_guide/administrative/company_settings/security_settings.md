---
nav_title: Security Settings
article_title: Security Settings
page_order: 2
page_type: reference
description: "This reference article covers generic cross-company security settings, including authentication rules, IP whitelisting, and two-factor authentication (2FA)."

---

# Security settings

As an admin, security is a high priority on your list of concerns. This page can help you manage the generic, cross-company security settings, including authentication rules, IP whitelisting, and two-factor authentication.

## Authentication rules

### Password length
The default minimum length is eight characters.

### Password complexity
Require passwords to include at least one of each of the following: an uppercase letter, lowercase letter, number, and special character.

### Password reusability
Determines the minimum number of new passwords that must be set before a user can reuse a password. The default is 3.

### Password expiration rules
Use this field to set when you want your Braze account users to reset their password.

### Session duration rules
Use this field to define how long Braze will keep your session active. Once Braze deems your session inactive (no activity for the defined number of minutes), the user will be logged out. The maximum number of minutes you can enter is 1440 (equal to 24 hours).

### Restrict SSO
You can restrict your users from logging in using a password or SSO.

For [SAML SSO][1], customers will need to set up their SAML settings prior to enforcing. If customers use Google SSO, they will simply have to enforce the security settings page with no additional lift.

## Dashboard IP whitelisting
Use the field shown to whitelist specific IP addresses and subnets from which users can log in to your account (for example, from a company network or VPN). Specify IP addresses and subnets as CIDR ranges in a comma-separated list. If not specified, users will be able to log in from any IP address.

## Two-factor authentication
Two-factor authentication adds a second level of identity verification to an account log, making it more secure than just a username and password. Toggling this switch to __On__ will make two-factor authentication mandatory for all Braze account users in your company.

When two-factor authentication is enabled, in addition to entering a password, users will need to enter a verification code sent to their mobile device when logging in to their Braze account.

{% alert tip %} Braze recommends setting up two-factor authentication via the Authy app rather than just SMS, in case you experience any issues receiving SMS in the future. {% endalert %}

Two-factor authentication is optional by default. However, when enabled, users who fail to set up their two-factor authentication will be locked out of their Braze account. Braze account users also can set up two-factor authentication on their own in __Account Settings__, even if not required by the administrator.

### Remember me
![Remember Me][0]{: style="float:right;max-width:30%;margin-left:15px;"}
Upon toggling on two-factor authentication for your company, the __Remember Me__ checkbox becomes available to users. This feature stores a cookie on your device, only requiring you to log in with two-factor authentication __once__ over the course of 30 days.

- Customers with multiple accounts under a Dashboard Company may experience issues using this feature due to the cookie being tied to a specific device. If users use the same device to log in to multiple accounts, the cookie will be replaced for the previously authorized accounts on that device. Braze expects only one device to be associated with an account, not one device for multiple accounts.

Be sure to save your changes before leaving the page!

### User authentication reset

Users experiencing issues logging in via two-factor authentication can reach out to their company admins to reset their two-factor authentication. To do this, have an admin navigate to __Manage Users__, select the user from the provided list, and select __Reset__ under __Two-Factor Authentication__. A reset can solve common authentication issues such as trouble with Authy, login failure due to SMS outages or user error, and more.

Two-factor authentication enforcement:
- If two-factor authentication is not enforced at the company level, once reset, the user will log in normally and need to go to __Account Settings__ to enable and set up two-factor authentication.
- If two-factor authentication is enforced at the company level, the next time the user logs in, they'll be asked to set up their two-factor authentication.

## Security event download

The Security Event report is a CSV report of security events such as account invitations, account removals, failed and successful login attempts, and other activities. To download this report, click **Download report** in the **Security Event Download** section.

[0]: {% image_buster /assets/img/remember_me.png %}
[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
