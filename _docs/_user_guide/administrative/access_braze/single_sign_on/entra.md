---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "This article will walk you through how to set up Microsoft Entra single sign-on capabilities with Braze."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) is Microsoft's cloud-based identity and access management service, which helps your employees sign in and access resources. You can use Entra SSO to control access to your apps and your app resources, based on your business requirements.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Sign-On URL | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> For the subdomain, use the coordinating subdomain listed in your [Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> For some identity providers, this can also be referred to as the Reply URL, Audience URL, or Audience URI. |
| Entity ID | `braze_dashboard`|
| RelayState API key | To enable identity provider login, go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Service Provider (SP) initiated login within Microsoft Entra SSO

### Step 1: Add Braze from the gallery

1. In your Microsoft Entra admin center, go to **Identity** > **Applications** > **Enterprise Applications**, and then select **New application**.
2. Search for **Braze** in the search box, select it from the result panel, and then select **Add**.

### Step 2: Configure Microsoft Entra SSO

1. In your Microsoft Entra admin center, go to your Braze application integration page and select **Single sign-on**.
2. On the **Select a single sign-on method** page, select **SAML** as your method.
3. On the **Set up Single Sign-On with SAML** page, select the edit icon for **Basic SAML Configuration**.
4. Configure the application in IdP-initiated mode by entering a **Reply URL** that combines your [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Optionally configure RelayState by entering your Relay State generated API key into the **Relay State (Optional)** field.
6. If you want to configure the application in SP-initiated mode, select **Set additional URLs** and enter a sign on URL that combines your [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) with the following pattern: `https://<SUBDOMAIN>.braze.com/sign_in`.
7. Format SAML assertions in the specific format expected by Braze. Refer to the following tabs on user attributes and user claims to understand how these attributes and values must be formatted.

{% tabs %}
{% tab User Attributes %}
You can manage the values of these attributes from the **User Attributes** section on the **Application Integration** page.

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

On the **Set up Single Sign-On with SAML** page, select **Edit** to open the **User Attributes** dialog. Then, edit the user claims according to the proper format.

Use the following claim name pairings:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
It is critically important that the email field match what is set up for your users in Braze. In most cases, this will be the same as `user.userprincipalname` however, if you have a different configuration, work with your system administrator to ensure that these fields match exactly.
{% endalert %}

You can manage these user claims and values from the **Manage claim** section.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Go to the **Set up Single Sign-On with SAML** page, then scroll to the **SAML Signing Certificate** section and download the appropriate **Certificate (Base64)** based on your requirements.
9. Go to the **Set up Braze** section and copy the appropriate URLs for use in the [Braze configuration](#step-3).

### Step 3: Configure Microsoft Entra SSO within Braze {#step-3}

After you've set up Braze within Microsoft Entra admin center, Microsoft Entra will provide a target URL (login URL) and **x.509** certificate which you will input into your Braze account.

After your account manager has enabled SAML SSO for your account, do the following:

1. Go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.
2. On the same page, add the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your identity provider's name, like "Microsoft Entra." |
| `Target URL` | This is the login URL provided by Microsoft Entra.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your identity provider. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) from the **Company Settings** page.
{% endalert %}
