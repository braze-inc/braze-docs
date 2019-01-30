---
nav_title: Security Settings
page_order: 3
---

# Security Settings

As an admin, security is a high priority on your list of concerns. This page can help you manage the generic, cross-company security settings, including authentication rules, IP whitelisting, and two-factor authentication.

## Authentication Rules

### Password Length
The default minimum length is 8 characters.

### Password Complexity
Require passwords that include at least one of each of the following: uppercase letter, lowercase letter, number and special character.

### Password Reusability
Determines the minimum number of new passwords that must be set before a user can reuse a password. The default is 3.

### Password Expiration Rules
Use this field to set when you want your Braze account users to reset their password.

### Session Duration Rules
Use this field to define how long Braze will keep your session active. Once Braze deems your session inactive (no activity for the defined number of minutes), the user will be logged out. The maximum number of minutes you can enter is 1440 (equal to 24 hours).

### Restrict SSO
You can restrict your users from logging in using a password or Okta.

For those clients that use [Okta SSO Login][1], there is a form on this page that allows them to configure that login service by providing their Okta URL and certificate.

## Dashboard IP Whitelisting

Use the field shown to whitelist specific IP addresses and subnets from which users can log in to your account (for example, from a company network or VPN). Specify IP addresses and subnets as CIDR ranges in a comma separated list. If not specified, users will be able to log in from any IP address.

## Two-Factor Authentication
Two-factor authentication adds a second level of identity verification to an account log in making it more secure than just a username and password. Toggling this switch to __On__ will make two-factor authentication mandatory for all Braze account users in your company.

When two-factor authentication is enabled, in addition to entering a password, users will be required to enter a verification code sent to their mobile device when logging in to their Braze account.

Two-factor authentication is optional by default. However, when enabled, users who fail to set up their two-factor authentication will be locked out of their Braze account.

{% alert tip %}
Any Braze account user can set up two-factor authentication (under Account Settings in the dropdown) on their own, even if not required by the administrator.
{% endalert %}


Be sure to save your changes before leaving the page!


[1]: {{ site.baseurl }}/user_guide/administrative/logging_in_and_security/single_sign_on/okta_single_sign_on/
