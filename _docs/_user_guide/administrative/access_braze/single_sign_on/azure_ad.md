---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutorial
description: "This article will walk you through how to set up Azure AD sign-on capabilities with Braze."

---

# Azure active directory

> This article will walk you through how to set up Azure AD sign-on capabilities with Braze.

[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) is Microsoft’s cloud-based identity and access management service, which helps your employee's sign in and access resources. You can use Azure AD to control access to your apps and your app resources, based on your business requirements.

## Requirements

upon setup, you will be asked to provide a sign-on url and an assertion consumer service (acs) url.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` <br> For the subdomain, use the coordinating subdomain listed in [your Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI.* |
| **Entity ID** | `braze_dashboard`|
{: .reset-td-br-1 .reset-td-br-2}


## Service provider (sp) initiated login within azure ad

### Step 1: add braze from the gallery

#### Step 1a: go to the azure active directory 

Go to the Azure Portal and click **Azure Active Directory** in the left navigation panel. 
![Azure_AD1]({% image_buster /assets/img/azure_ad1.png %})

#### Step 1b: find applications
Navigate to **Enterprise Applications**, then select **All applications**.
![Azure_AD2]({% image_buster /assets/img/azure_ad2.png %})

#### Step 1c: create a new application
Add a new application by clicking **+ New application** in the top of the dialog.
![Azure_AD3]({% image_buster /assets/img/azure_ad3.png %})

#### Step 1d: add braze
Search for **Braze** in the search box, then select it from the result panel, then click **Add**.
![Azure_AD4]({% image_buster /assets/img/azure_ad4.png %})

### Step 2: configure azure ad single sign-on

#### Step 2a: select single sign-on
In your Azure Portal, go to the **Braze Application Integration** page and select **Single sign-on**.

![Azure_AD5]({% image_buster /assets/img/azure_ad5.png %})

#### Step 2b: select sso method
Select **SAML/WS-Fed** as your method from the **Select a single sign-on method** dialog to open the **Set up Single Sign-On with SAML** page.

![Azure_AD6]({% image_buster /assets/img/azure_ad6.png %})

#### Step 2c: open configure dialog
From there, click the edit icon to open the **Basic SAML Configuration** dialog.

![Azure_AD7]({% image_buster /assets/img/azure_ad7.png %})

#### Step 2d: configure in idp mode
If you want to configure the application in IdP-initiated mode, enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.

![Azure_AD8]({% image_buster /assets/img/azure_ad8.png %})

#### Step 2e: configure in sp mode
If you want to configure the application in SP-initiated mode, click **Set additional URLs** and enter a URL that combines [your Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.

![Azure_AD9]({% image_buster /assets/img/azure_ad9.png %})

#### Step 2f: format saml assertions

Braze expects the SAML assertions in a specific format. Refer to the following tabs on user attributes and user claims to understand how these attributes and values must be formatted.

{% tabs %}
{% tab User Attributes %}
You can manage the values of these attributes from the **User Attributes** section on the **Application Integration** page.

![Azure_AD10]({% image_buster /assets/img/azure_ad10.png %})

Use the following attribute pairings:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.userprincipalname`
- `name` = `user.userprincipalname`
- `Unique User Identifier` = `user.userprincipalname`

{% endtab %}
{% tab User Claims %}

On the **Set up Single Sign-On with SAML** page, click **Edit** to open the **User Attributes** dialog. Then, edit the claims according to the proper format, shown below.

![Azure_AD11]({% image_buster /assets/img/azure_ad11.png %})

Use the following claim name pairings:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

You can manage these user claims and values from the **Manage user claims** dialog:

![Azure_AD12]({% image_buster /assets/img/azure_ad12.png %})

{% endtab %}
{% endtabs %}

#### Step 2g: download certificate
Go to the **Set up Single Sign-On with SAML** page, then scroll to the **SAML Signing Certificate** section and download the appropriate **Certificate (Base64)** based on your requirements.

![Azure_AD13]({% image_buster /assets/img/azure_ad13.png %})

#### Step 2h: copy urls for configuration in braze
Go to the **Set up Braze** section and copy the appropriate URLs for use in the [Braze configuration](#step-3-configure-braze-single-sign-on).

![Azure_AD14]({% image_buster /assets/img/azure_ad14.png %})

### Step 3: configure azure ad within braze

Once you have set up Braze within your Azure AD, they will provide a Target URL (Login URL) and **x.509** certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to **Company Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

On this page, you will add the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your IdP name, like "Azure AD.” |
| `Target URL` | This is the Login URL provided by Azure AD.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your IdP. |
{: .reset-td-br-1 .reset-td-br-2}

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Create and enable a braze api key for idp login (optional)

To enable IdP-initiated login, you will first need to create an API Key in **Developer Console** > **API Settings**.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within Azure AD, which will be used to identity which company the user is trying to log into.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the **Company Settings** page.
{% endalert %}
