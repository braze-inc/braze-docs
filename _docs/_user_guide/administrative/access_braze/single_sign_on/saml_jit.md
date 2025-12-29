---
nav_title: SAML Just-in-Time provisioning
article_title: SAML Just-in-Time Provisioning
page_order: 1
page_type: tutorial
description: "This article will walk you through how to configure SAML just-in-time provisioning to allow new dashboard users to create a Braze account on their first sign in." 

---

# SAML just-in-time provisioning 

> Just-in-time provisioning works with [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) to allow new dashboard users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new dashboard user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

As a security measure, SAML just-in-time provisioning (JITP) only works for users with email domains that already exist in your company. JITP is only possible for domains where there is already at least one confirmed, non-impersonation developer in the company. 

For example, let's say the account ```jon.smith@decorumsoft.com``` can use JITP to log into Decorumsoft. The account ```jane.smith@decorumsoft.com``` has the same domain and can also be allowed provisioning. However, if you try to use JITP with ```jon.smith@decorumsoft.eu```, provisioning won't be allowed because there isn't a ```decorumsoft.eu``` account within the Decorumsoft Braze dashboard. 

To make an exception for a company, contact [Support]({{site.baseurl}}/braze_support/).

## Prerequisites

SAML JITP requires that SAML SSO is set up and integrated. It is not compatible with Google SSO, and is only supported for Identity Provider Initiated (IdP-initiated) login workflows.

## Setting up SAML just-in-time provisioning (JITP)

Have a Braze administrator do the following:

1. Navigate to **Settings** > **Admin Settings** > **Security Settings**.
2. In the **SAML SSO** section, toggle on the **Automatic user provisioning** option.
3. Select a default workspace to add a new dashboard user.
4. Select the default permission set to assign to that new dashboard user. To learn how to create a permission set, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Select **Save changes** at the bottom of the page
7. In your SSO provider’s settings, add all users that need Braze access to your SSO provider's directory.
8. Instruct users to access Braze through your IdP portal for their first login. After this, the SAML single sign-on button displays for future logins.

## Frequently asked questions

### How do I disable SAML JITP?

After setting up JITP, you must [contact Support]({{site.baseurl}}/braze_support/) to have it turned off.

## Troubleshooting

### Single sign-button doesn't appear with Microsoft Entra ID

The **Sign-On URL** field in Microsoft Entra's **Basic SAML Configuration** form for Braze may cause users to only see a password option, not an SSO button, with IdP-initiated login. To prevent this issue, leave the **Sign-On URL** field blank when configuring Braze in your Microsoft Entra admin center.