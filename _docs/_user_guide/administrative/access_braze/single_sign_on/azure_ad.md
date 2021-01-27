---
nav_title: Azure Active Directory
page_order: 3

page_type: tutorial
tool: dashboard
description: "This article will walk you through how to set up Azure AD sign on capabilities with Braze."
---

# Azure Active Directory

[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) is Microsoft’s cloud-based identity and access management service, which helps your employee's sign in and access resources. You can use Azure AD to control access to your apps and your app resources, based on your business requirements.

## Requirements

Upon setup, you will be asked to provide a Sign-On URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` <br> For the subdomain, use the coordinating subdomain listed in [your Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI.* |
| **Entity ID** | `braze_dashboard`|
{: .reset-td-br-1 .reset-td-br-2}


## Service Provider (SP) Initiated Login within Azure AD

### Step 1: Add Braze from the Gallery

#### Step 1a: Go to the Azure Active Directory

Go to the Azure Portal and click `Azure Active Directory` in the left navigation panel.
![Azure_AD1]({% image_buster /assets/img/azure_ad1.png %})

#### Step 1b: Find Applications
Navigate to `Enterprise Applications`, then select `All applications`.
![Azure_AD2]({% image_buster /assets/img/azure_ad2.png %})

#### Step 1c: Create a New Application
Add a new application by clicking `+ New application` in the top of the dialog.
![Azure_AD3]({% image_buster /assets/img/azure_ad3.png %})

#### Step 1d: Add Braze
Search for `Braze` in the search box, then select it from the result panel, then click `Add`.
![Azure_AD4]({% image_buster /assets/img/azure_ad4.png %})

### Step 2: Configure Azure AD Single Sign-On

#### Step 2a: Select Single Sign-On
In your `Azure Portal`, go to the Braze Application Integration page and select `Single Sign-On`.

![Azure_AD5]({% image_buster /assets/img/azure_ad5.png %})

#### Step 2b: Select SSO Method
Select `SAML/WS-Fed` as your method from the `Single Sign-On method` dialog to open the `Set up Single Sign-On with SAML` page.

![Azure_AD6]({% image_buster /assets/img/azure_ad6.png %})

#### Step 2c: Open Configure Dialog
From there, click the `Edit` icon to open the `Basic SAML Configuration` dialog.

![Azure_AD7]({% image_buster /assets/img/azure_ad7.png %})

#### Step 2d: Configure in IDP Mode
If you wish to configure the application in IDP initiated mode, enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.

![Azure_AD8]({% image_buster /assets/img/azure_ad8.png %})

#### Step 2e: Configure in SP Mode
If you wish to configure the application in SP initiated mode, click `Set additional URLs` and enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.

![Azure_AD9]({% image_buster /assets/img/azure_ad9.png %})

#### Step 2f: Format SAML Assertions
Braze expects the SAML assertions in a [specific format](#user-claims-configuration-format). You can manage the values of these attributes from the User Attributes section on the `Application Integration` page. On the `Set up Single Sign-On with SAML` page, click `Edit` to open the `User Attributes` dialog. Then, edit the claims [according to the proper format, shown below](#user-claims-configuration-format).

{% gallery %}
{{site.baseurl}}/assets/img/azure_ad10.png?bf892368baf287cba5ab9a6e3b09431d  <br> Use the following attribute pairings (the image above shows the incorrect value for `emailaddress`): <br> `givenname` = `user.givenname` <br> `surname` = `user.surname` <br> `emailaddress` = `user.userprincipalname` <br> `name` = `user.userprincipalname` <br> `Unique User Identifier` = `user.userprincipalname`
{{site.baseurl}}/assets/img/azure_ad11.png?ecd2c8fe148939b7de957fe85cd6317e  <br> Use the following Claim Name pairings (the image above shows the incorrect Value for `claims/emailaddress`): <br> `claims/givenname` = `user.givenname` <br> `claims/surname` = `user.surname` <br> `claims/emailaddress` = `user.userprincipalname` <br> `claims/name` = `user.userprincipalname` <br> `claims/nameidentifier` = `user.userprincipalname`.
{{site.baseurl}}/assets/img/azure_ad12.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is where you can manage those User Claims and values.
{% endgallery %}

#### Step 2g: Download Certificate
Go to the `Set up Single Sign-On with SAML` page, then scroll to the `SAML Signing Certificate` section and download the appropriate `Certificate (Base64)` based on your requirements.

![Azure_AD13]({% image_buster /assets/img/azure_ad13.png %})

#### Step 2h: Copy URLs for Configuration in Braze
Go to the `Set up Braze` section and copy the appropriate URLs for use in the [Braze configuration](#step-3-configure-braze-single-sign-on).

![Azure_AD14]({% image_buster /assets/img/azure_ad14.png %})


### Step 3: Configure Azure AD within Braze

Once you have setup Braze within your Azure AD, they will provide a Target URL (Login URL) and `x.509` certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to `Company Settings` > `Security Settings` and toggle the SAML SSO section to `ON`.

On this page, you, input:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your IdP name, like "Azure AD.” |
| `Target URL` | This is the Login URL provided by Azure AD.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your IdP. |
{: .reset-td-br-1 .reset-td-br-2}

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Create and Enable a Braze API Key for IdP Login (Optional)

To enable IdP initiated login, you will first need to create an API Key in `Developer Console` > `API Settings`.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within Azure AD, which will be used to identity which company the user is trying to log into.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the `Company Settings` page.
{% endalert %}
