---
nav_title: Azure Active Directory
page_order: 3
---

# Azure Active Directory

[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) is Microsoft’s cloud-based identity and access management service, which helps your employee's sign in and access resources. You can use Azure AD to control access to your apps and your app resources, based on your business requirements.

## Requirements

- An Azure AD account.
- A Braze account with SAML SSO enabled.
- You must have admin privileges for both Azure and Braze.

## Step 1: Add Braze from the Gallery

1. Go to the Azure Portal and click `Azure Active Directory` in the left navigation panel.
2. Navigate to `Enterprise Applications`, then select `All applications`.
3. Add a new application by clicking `+ New application` in the top of the dialog.
4. Search for `Braze` in the search box, then select it from the result panel, then click `Add`.

## Step 2: Configure Azure AD Single Sign-On

1. In your `Azure Portal`, go to the Braze Application Integration page and select `Single Sign-On`.
2. Select `SAML/WS-Fed` as your method from the `Single Sign-On method` dialog to open the `Set up Single Sign-On with SAML` page.
3. From there, click the `Edit` icon to open the `Basic SAML Configuration` dialog.
4. If you wish to configure the application in IDP initiated mode, enter a URL that combines [your Braze instance]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. If you wish to configure the application in SP initiated mode, click `Set additional URLs` and enter a URL that combines [your Braze instance]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.
6. Braze expects the SAML assertions in a [specific format](#user-claims-configuration-format). You can manage the values of these attributes from the User Attributes section on the `Application Integration` page. On the `Set up Single Sign-On with SAML` page, click `Edit` to open the `User Attributes` dialog. Then, edit the claims [according to the proper format, shown below](#user-claims-configuration-format).
7. Go to the `Set up Single Sign-On with SAML` page, then scroll to the `SAML Signing Certificate` section and download the appropriate `Certificate (Base64)` based on your requirements.
8. Go to the `Set up Braze` section and copy the appropriate URLs for use in the [Braze configuration](#step-3-configure-braze-single-sign-on).

### User Claims Configuration Format
Click `+ Add new claim` to open the `Manage user claims` dialog and enter each of these as an `Attribute`.

| Claim Name | Value |
|---|---|
|`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email`	| `user.userprincipalname`|
|`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name`	|`user.givenname`|
|`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name`	|`user.surname`|
|`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/login`|	`user.mail`|

## Step 3: Configure Braze Single Sign-On

Send the downloaded `Certificate (Base64)` to [Braze support]({{ site.baseurl }}/support_contact) so they can turn on your SAML SSO connection.  

## Step 4: Test Azure AD Single Sign-On

Test Azure Single Sign-On as described in [Azure's instructions here](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial#create-an-azure-ad-test-user).

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the `Company Settings` page.
{% endalert %}
