---
nav_title: SAML Just-in-Time provisioning
article_title: SAML Just-in-Time Provisioning
page_order: 1
page_type: tutorial
description: "This article will walk you through how to configure SAML just-in-time provisioning to allow new dashboard users to create a Braze account on their first sign in." 

---

# SAML just-in-time provisioning 

> Just-in-time provisioning works with [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) to allow new dashboard users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new dashboard user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

## Prerequisites

This feature requires that SAML SSO is set up and integrated, and is not compatible with Google SSO.

## Setting up SAML just-in-time provisioning

Have a Braze administrator do the following:

1. Navigate to **Settings** > **Security Settings**.
2. In the **SAML SSO** section, toggle on the **Automatic user provisioning** option.
3. Select a default workspace to add a new dashboard user.
4. Select the default permission set to assign to that new dashboard user. To learn how to create a permission set, see [Setting user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Select **Save changes** at the bottom of the page
7. In your SSO provider’s settings, add all users that need Braze access to your SSO provider's directory.
8. Now users can sign up or log in.
