---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutorial
description: "This article will walk you through how to set up Azure AD sign-on capabilities with Braze."

---

# Azure Active Directory

> [Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) is Microsoft's cloud-based identity and access management service, which helps your employees sign in and access resources. You can use Azure AD to control access to your apps and your app resources, based on your business requirements.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Sign-On URL | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> For the subdomain, use the coordinating subdomain listed in your [Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> For some identity providers, this can also be referred to as the Reply URL, Audience URL, or Audience URI. |
| Entity ID | `braze_dashboard`|
| RelayState API key | To enable identity provider login, go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find your API keys under **Settings** at **Developer Console** > **API Settings**.
{% endalert %}

## Service Provider (SP) initiated login within Azure AD

### Step 1: Add Braze from the gallery

1. Go to the Azure Portal and click **Azure Active Directory** in the left navigation panel.
2. Go to **Enterprise Applications**, then select **All applications**. <br><br>![Azure portal selecting all enterprise applications.]({% image_buster /assets/img/azure_2.png %})

{: start="3"}
3. Add a new application by clicking **+ New application** in the top of the dialog.
4. Search for **Braze** in the search box, select it from the result panel, then click **Add**.

### Step 2: Configure Azure AD single sign-on

1. In your Azure Portal, go to the **Braze Application Integration** page and select **Single sign-on**.
2. Select **SAML/WS-Fed** as your method from the **Select a single sign-on method** dialog to open the **Set up Single Sign-On with SAML** page.<br><br>![Azure portal select a single sign-on method dialog.]({% image_buster /assets/img/azure_6.png %})

{: start="3"}
3. Click the edit icon to open the **Basic SAML Configuration** dialog.<br><br>![Azure portal editing basic SAML configuration.]({% image_buster /assets/img/azure_7.png %})

{: start="4"}
4. Configure the application in IdP-initiated mode by entering a URL that combines your [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.<br><br>![Azure portal editing basic SAML configuration.]({% image_buster /assets/img/azure_8.png %})

{: start="5"}
5. Configure RelayState by inputting your RelayState generated API key in the RelayState box.<br><br>![]({% image_buster /assets/img/relaystate2.png %})

{: start="6"}
6. If you want to configure the application in SP-initiated mode, click **Set additional URLs** and enter a URL that combines your [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.<br><br>![Azure portal setting additional sign on URLs.]({% image_buster /assets/img/azure_9.png %})

{: start="7"}
7. Format SAML assertions in the specific format expected by Braze. Refer to the following tabs on user attributes and user claims to understand how these attributes and values must be formatted.

{% tabs %}
{% tab User Attributes %}
You can manage the values of these attributes from the **User Attributes** section on the **Application Integration** page.

![User Attributes section of the Application Integration page in Azure.]({% image_buster /assets/img/azure_10.png %})

Use the following attribute pairings:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
It is critically important that the email field match what is set up for your users in Braze. In most cases, this will be the same as `user.userprincipalname` however, if you have a different configuration, work with your system administrator to ensure that these fields match exactly.
{% endalert %}

{% endtab %}
{% tab User Claims %}

On the **Set up Single Sign-On with SAML** page, click **Edit** to open the **User Attributes** dialog. Then, edit the claims according to the proper format.

![User Attributes dialog in Azure.]({% image_buster /assets/img/azure_11.png %})

Use the following claim name pairings:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
It is critically important that the email field match what is set up for your users in Braze. In most cases, this will be the same as `user.userprincipalname` however, if you have a different configuration, work with your system administrator to ensure that these fields match exactly.
{% endalert %}

You can manage these user claims and values from the **Manage user claims** dialog:

![Manage claim dialog in Azure]({% image_buster /assets/img/azure_12.png %})

{% endtab %}
{% endtabs %}

{: start="8"}
8. Go to the **Set up Single Sign-On with SAML** page, then scroll to the **SAML Signing Certificate** section and download the appropriate **Certificate (Base64)** based on your requirements.<br><br>![Azure download SAML signing certificate.]({% image_buster /assets/img/azure_13.png %})

{: start="9"}
9. Go to the **Set up Braze** section and copy the appropriate URLs for use in the [Braze configuration](#step-3).<br><br>![Azure URLs for configuration.]({% image_buster /assets/img/azure_14.png %})

### Step 3: Configure Azure AD within Braze {#step-3}

Once you have set up Braze within your Azure AD, they will provide a target URL (login URL) and **x.509** certificate which you will input into your Braze account.

After your account manager has enabled SAML SSO for your account, do the following:

1. Go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), select your account icon and go to **Company Settings** > **Security Settings** to find the SAML SSO section.
{% endalert %}

{: start="2"}
2. On the same page, add the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your identity provider's name, like "Azure AD." |
| `Target URL` | This is the login URL provided by Azure AD.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your identity provider. |
{: .reset-td-br-1 .reset-td-br-2}

![Opening Security Settings and adding SAML SSO details.]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) from the **Company Settings** page.
{% endalert %}
