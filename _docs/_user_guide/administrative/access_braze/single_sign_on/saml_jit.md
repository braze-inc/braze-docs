---
nav_title: SAML Just-in-Time provisioning
article_title: SAML Just-in-Time Provisioning
page_order: 1
page_type: tutorial
description: "This article will walk you through how to configure SAML just-in-time provisioning to allow new dashboard users to create a Braze account on their first sign in." 

---

# SAML just-in-time provisioning 

> Just-in-time provisioning works with [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) to allow new dashboard users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new dashboard user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

{% alert important %}
**Security Requirement**: As a security measure, SAML just-in-time provisioning only works for users with email domains that already exist in your Braze company. JITP is only possible for domains where there is already at least one confirmed, non-impersonation developer in the company.
{% endalert %}

## Prerequisites

This feature requires the following:

- SAML SSO is set up and integrated (not compatible with Google SSO)
- At least one confirmed user with the same email domain already exists in your Braze company
- Proper SAML attribute mapping configured in your identity provider

## Setting up SAML just-in-time provisioning

Have a Braze administrator do the following:

1. Navigate to **Settings** > **Security Settings**.
2. In the **SAML SSO** section, toggle on the **Automatic user provisioning** option.
3. Select a default workspace to add a new dashboard user.
4. Select the default permission set to assign to that new dashboard user. To learn how to create a permission set, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
5. Select **Save changes** at the bottom of the page.
6. In your SSO provider's settings, add all users that need Braze access to your SSO provider's directory.
7. Ensure your identity provider is configured to send the required SAML attributes (`email`, `first_name`, `last_name`) to Braze during authentication.
8. Test the configuration with a user whose email domain already exists in your Braze company.

## Expected behavior

When SAML just-in-time provisioning is enabled:

- **New users**: When a user with a matching email domain signs in for the first time through SAML SSO, Braze automatically creates their account with the default workspace and permission set you configured.
- **Existing users**: Users who already have Braze accounts continue to sign in normally through SAML SSO.
- **Domain validation**: Users with email domains that don't exist in your Braze company will be unable to create accounts through JITP, even if they authenticate successfully through your identity provider.
- **Permission inheritance**: New users receive the exact permissions defined in your default permission set and are assigned to the default workspace you specified.

## Troubleshooting

### JITP not working for valid users

If just-in-time provisioning isn't working for users who should have access:

1. Verify that at least one user with the same email domain already exists in your Braze company.
2. Check that your identity provider is sending the required SAML attributes (`email`, `first_name`, `last_name`).
3. Confirm that the **Automatic user provisioning** option is enabled in **Settings** > **Security Settings**.
4. Ensure the user is authenticating through the correct SAML SSO login flow.

### Sign-On URL issues with Microsoft Entra ID

If you're using Microsoft Entra ID (formerly Azure AD) and experiencing issues with IdP-initiated login:

{% alert warning %}
**Known Issue**: Setting the **Sign-On URL** field in Microsoft Entra's "Basic SAML Configuration" can break IdP-initiated login. To prevent this issue, leave the **Sign-On URL** field blank when configuring Braze in your Microsoft Entra admin center.
{% endalert %}

To resolve this issue:

1. In your Microsoft Entra admin center, navigate to your Braze application.
2. Go to **Single sign-on** > **Basic SAML Configuration**.
3. Clear the **Sign-On URL** field and leave it blank.
4. Save your configuration.
5. Test IdP-initiated login to confirm the issue is resolved.

### Users created but with wrong permissions

If users are being created through JITP but with incorrect permissions:

1. Review the default permission set configured in **Settings** > **Security Settings**.
2. Update the permission set to match your requirements.
3. For existing users created with incorrect permissions, manually update their permissions in **Settings** > **Company Users**.

## Frequently asked questions

**Q: Can I use JITP with Google SSO?**
A: No, SAML just-in-time provisioning is not compatible with Google SSO. You must use SAML SSO.

**Q: What happens if I disable JITP after users have been created?**
A: Existing users continue to have access and can sign in normally. New users will no longer be automatically provisioned and must be manually created.

**Q: Can I change the default workspace or permissions after enabling JITP?**
A: Yes, you can update the default workspace and permission set at any time in **Settings** > **Security Settings**. Changes only apply to new users created after the update.