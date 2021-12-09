---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutorial
description: "This article will walk you through how to set up Azure AD sign-on capabilities with Braze."
---

# Azure Active Directory

> This article will walk you through how to set up Azure AD sign-on capabilities with Braze.

[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) is Microsoft’s cloud-based identity and access management service, which helps your employee's sign in and access resources. You can use Azure AD to control access to your apps and your app resources, based on your business requirements.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.

| Requirement                              | Details                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sign-On URL**                          | `https://<SUBDOMAIN>.braze.com/sign_in` <br> For the subdomain, use the coordinating subdomain listed in [your Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI.*                                                                                                                                                                                                                 |
| **Entity ID**                            | `braze_dashboard`                                                                                                                                                                                                                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Service Provider (SP) initiated login within Azure AD

### Step 1: Add Braze from the gallery

#### Step 1a: Go to the Azure Active Directory

Go to the Azure Portal and click **Azure Active Directory** in the left navigation panel.

![Azure active directory]({% image_buster /assets/img/azure_1.png %})

#### Step 1b: Find applications

Navigate to **Enterprise Applications**, then select **All applications**.

![Azure find application]({% image_buster /assets/img/azure_2.png %})

#### Step 1c: Create a new application

Add a new application by clicking **+ New application** in the top of the dialog.

#### Step 1d: Add Braze

Search for **Braze** in the search box, then select it from the result panel, then click **Add**.

### Step 2: Configure Azure AD single sign-on

#### Step 2a: Select single sign-on

In your Azure Portal, go to the **Braze Application Integration** page and select **Single sign-on**.

![Azure portal]({% image_buster /assets/img/azure_5.png %})

#### Step 2b: Select SSO method

Select **SAML/WS-Fed** as your method from the **Select a single sign-on method** dialog to open the **Set up Single Sign-On with SAML** page.

![Azure SSO]({% image_buster /assets/img/azure_6.png %})

#### Step 2c: Open configure dialog

From there, click the edit icon to open the **Basic SAML Configuration** dialog.

![Azure config]({% image_buster /assets/img/azure_7.png %})

#### Step 2d: Configure in IdP mode

If you want to configure the application in IdP-initiated mode, enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.

![Azure Idp]({% image_buster /assets/img/azure_8.png %})

#### Step 2e: Configure in SP mode

If you want to configure the application in SP-initiated mode, click **Set additional URLs** and enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.

![Azure SP mode]({% image_buster /assets/img/azure_9.png %})

#### Step 2f: Format SAML assertions

Braze expects the SAML assertions in a specific format. Refer to the following tabs on user attributes and user claims to understand how these attributes and values must be formatted.

{% tabs %}
{% tab User Attributes %}
You can manage the values of these attributes from the **User Attributes** section on the **Application Integration** page.

![Azure SAML]({% image_buster /assets/img/azure_10.png %})

Use the following attribute pairings:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.userprincipalname`
- `name` = `user.userprincipalname`
- `Unique User Identifier` = `user.userprincipalname`

{% endtab %}
{% tab User Claims %}

On the **Set up Single Sign-On with SAML** page, click **Edit** to open the **User Attributes** dialog. Then, edit the claims according to the proper format, shown below.

![Azure SSO]({% image_buster /assets/img/azure_11.png %})

Use the following claim name pairings:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

You can manage these user claims and values from the **Manage user claims** dialog:

![Azure user claims]({% image_buster /assets/img/azure_12.png %})

{% endtab %}
{% endtabs %}

#### Step 2g: Download certificate

Go to the **Set up Single Sign-On with SAML** page, then scroll to the **SAML Signing Certificate** section and download the appropriate **Certificate (Base64)** based on your requirements.

![Azure download certificate]({% image_buster /assets/img/azure_13.png %})

#### Step 2h: Copy URLs for configuration in Braze

Go to the **Set up Braze** section and copy the appropriate URLs for use in the [Braze configuration](#step-3-configure-braze-single-sign-on).

![Azure URLs for config]({% image_buster /assets/img/azure_14.png %})

### Step 3: Configure Azure AD within Braze

Once you have set up Braze within your Azure AD, they will provide a Target URL (Login URL) and **x.509** certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to **Company Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

On this page, you will add the following:

| Requirement   | Details                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| `SAML Name`   | This will appear as the button text on the login screen. This is typically your IdP name, like "Azure AD.” |
| `Target URL`  | This is the Login URL provided by Azure AD.                                                                |
| `Certificate` | The `x.509` PEM encoded certificate is provided by your IdP.                                               |
{: .reset-td-br-1 .reset-td-br-2}

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Create and enable a Braze API key for IdP login (optional)

To enable IdP-initiated login, you will first need to create an API Key in **Developer Console** > **API Settings**.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within Azure AD, which will be used to identity which company the user is trying to log into.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the **Company Settings** page.
{% endalert %}
