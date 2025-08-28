---
nav_title: Accessing your account
article_title: Accessing Your Account
page_order: 2
page_type: reference
description: "This article covers how to get your Braze account, how to log in after granted access, and how to go about resetting your Braze password."

---

# Accessing your account

> This article covers how to get your Braze account, how to log in after being granted access, and how to troubleshoot your dashboard access and dashboard performance.

If you are your company's first Braze user and logging in for the first time, you will receive a welcome email from `@alerts.braze.com` asking you to confirm your email and log in on the first day of your contract.

After confirming your account, you can add additional users from the [Company Users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) page of your dashboard. All users will receive an email asking them to confirm their account after they have been added.

If you aren't the first user on your company's Braze account, contact your company's Braze account administrator and ask them to create your account. You will then receive a welcome email from `@alerts.braze.com` asking you to confirm your email and log in.

## Logging in

Let's talk about how to log in, whether it's the first time or the millionth! If you are your company's first user, follow the guidance in the preceding section. If not, you can log in after your company's Braze admin creates your account.

You can either log in from the [Braze.com](https://www.braze.com) home site, or just use your dashboard URL that corresponds to your specific [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For your convenience, Braze has several single sign-on (SSO) options such as:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
After you log into Braze with SSO, you can no longer use your password to log into the dashboard. 
{% endalert %}

## Supported browsers

The Braze dashboard supports the following browsers:
- Chrome (version 87 or newer)
- Firefox (version 85 or newer)
- Safari (version 15.4 or newer)
- Edge (version 87 or newer)

If your Braze dashboard says you have an unexpected error and your browser console tool shows the error `ReferenceError: structuredClone is not defined`, your browser is outdated. If this error keeps reoccurring, uninstall and reinstall your browser.

## Accessing multiple Braze dashboards

Braze doesn't allow you to register the same email address to multiple dashboard users in the same cluster (for example, if you have two dashboards on US-01). You can use the same email to create accounts on different clusters (for example, if you have one dashboard on US-01 and one on US-05). If you need to access multiple Braze dashboards in the same cluster, you can do the following:

### Use email aliases

If your email provider is Gmail, you can create aliases by adding a `+` sign followed by any text to your email address. For example:
- **Original email:** `rocky@gmail.com`
- **Alias email:** `rocky+1@gmail.com`

Both email addresses will direct emails to the same inbox, but Braze will recognize them as separate accounts when you log in.

### Create separate aliases with other providers

If your email provider doesn't support `+` aliasing, you can still create separate aliases, such as setting up `rocky@braze.com` to forward to `rocky.lotito@braze.com`. This allows multiple addresses to funnel to the same inbox while being recognized as different emails by Braze.

### Use multi-company developers

The multi-company developers feature allows sharing of a single user account across multiple companies. Users can toggle between different company dashboards from their user profile menu.

If you have SSO and want to set up multi-company developers, you need to enable a SAML Custom Entity ID by setting up a custom SAML SSO integration. Follow the steps in [Service Provider (SP) initiated login]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), but apply these changes:
- Change **Entity ID** to `braze_dashboard_<companyID>` for each dashboard integration.
- Reach out to your customer success manager or account manager to enable the `saml_sso_custom_entity_id` feature flipper for each dashboard.

### Considerations for Single Sign-On (SSO)

If you use Single Sign-On (SSO), be aware that having multiple different email addresses could lead to complications. Confirm that your SSO settings are configured correctly to avoid access issues.

## Troubleshooting

### Resetting your password

To reset your password, select the **Forgot your password?** link on the dashboard login page. You'll be prompted to input your email to receive a link to reset your password.

![Dashboard login with "Forgot your password?" prompt.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Clearing your browser cache and cookies

If you're having issues with dashboard performance, such as your dashboard or segment performance list not loading, try clearing your browser cache and cookies by following the steps for your respective browser.

{% alert important %}
Clearing cookies will log you out, so unsaved work will be lost.
{% endalert %}

- [Clear cache & cookies in Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Clear cookies in Safari on Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Clear cookies and site data in Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Delete all cookies in Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

If clearing your browser cache and cookies doesn't resolve your issues, contact [Support]({{site.baseurl}}/support_contact/).

### Accessing the drag-and-drop editor

For most Braze users, the drag-and-drop editor should load. However, if you're using a VPN or are behind a firewall, you may need to allowlist a domain. Contact your IT administrator to check that `*.bz-rndr.com` is allowlisted.

The editor may experience loading issues due to the following:

- **Transient error:** These are temporary failures that may affect connectivity, communication, or data transfer. Fortunately, they typically resolve on their own without requiring significant intervention, as they're often caused by short-lived conditions and do not indicate systemic problems.
- **Major error:** This may involve an underlying infrastructure or product issue.  You can check our [Braze system status page](https://braze.statuspage.io/) as we are likely aware of the situation and actively working to resolve it.

{% alert important %}
If you're still experiencing issues, [open a support ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Before doing so, check that your IT administrator has confirmed that `*.bz-rndr.com` is allowlisted on your end.
{% endalert %}

### Accessing Braze Learning

If you're experiencing issues logging into Braze Learning and find yourself stuck in a loop that redirects you to the dashboard, do the following steps:

1. If you have multiple Braze accounts, logging in with the wrong account twice will send you to the Braze dashboard. Confirm you're logging into the correct account. 
2. If you have an ad blocker, confirm it is turned off. It may block cookies necessary for single sign-on functionality.
3. Go to Company Settings > Security Settings and verify that single sign-on (SSO) is turned on.
4. Confirm that your dashboard user profile includes both a first and last name. Not having a last name can disrupt the login process.
5. Access Braze Learning from your dashboard by going to **Support** > **Braze Learning**. 
6. If you continue to experience issues, consider re-creating your account. Users who accessed Braze Learning during the free trial phase may have difficulties accessing it now.

### Two-factor authentication (2FA) issues

If a user is experiencing issues with Two-Factor Authentication (2FA) and can't access the Braze dashboard, it may be due to several reasons. Most commonly, they may no longer have access to the registered phone number or the device where the Authy app is installed.

An admin should reset the 2FA for the affected user by doing the following: 

1. Go to **Manage Users**.
2. Select **Edit User** for the user experiencing 2FA issues.
3. Choose the option to Reset 2FA.
4. Confirm the 2FA reset when prompted.
5. If the reset doesn't immediately resolve the issue, clear your cookies and cache.

Braze cannot reset 2FA on behalf of users for security reasons, so if the admin is unable to reset 2FA, a support ticket should be created.

#### Considerations

- If 2FA is enforced at the company level: After the reset, the user will be prompted to set up their 2FA again the next time they log in.
- If 2FA is not enforced at the company level: The user will log into the dashboard without needing to set up 2FA again. If they wish to enable 2FA, they can do so in Account Settings.

{% alert note %}
This reset process also applies to users who have been locked out of their account due to requesting too many tokens within the last hour.
{% endalert %}