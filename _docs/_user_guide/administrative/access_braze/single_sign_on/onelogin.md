---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "This article will walk you through how to configure Braze to use OneLogin for single sign-on."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) is a cloud identity platform that provides a comprehensive solution for managing user identities. OneLogin integrates with cloud and on-premise applications using SAML 2.0, for Single Sign-On (SSO), user provisioning, multi-factor authentication, and more.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Braze Domain | You will need your Braze domain to set up Braze within OneLogin. If your instance is `US-01`, you will need to input your dashboard URL into the OneLogin dashboard. <br><br> For example, if your dashboard URL is `https://dashboard-01.braze.com`, you need to input `dashboard-01.braze.com`.  |
| RelayState API key | To enable IdP login, go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## IdP-initiated login within OneLogin

### Step 1: Configure the Braze app

1. Log into [OneLogin](https://app.onelogin.com/login). Click on **Administration**.![OneLogin Administration page.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Go to **Apps** > **Add Apps** in the top navigation bar. Search for "Braze" and select the Braze app.![Search results for Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Save the Braze app to your Company.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. When saved, go to **Configuration** and add your **Braze Domain** and **RelayState** API key.![OneLogin Configuration tab for the Braze app.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze expects the SAML assertions in a [specific format]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). Under **Parameters** the attributes supported by Braze should be pre-populated. Verify that they are correct.![Braze SAML parameters in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copy the **Certificate** and **SAML 2.0 Endpoint (HTTP)** needed to set up the Braze dashboard from under the **SSO** tab.![Certificates to copy from the Braze app SSO tab in OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Step 2: Configure OneLogin within Braze

Once you have set up Braze within your OneLogin, they will provide a target URL (`SAML 2.0 Endpoint (HTTP)`) and `x.509` certificate which you will input into your Braze account.

After your account manager has enabled SAML SSO for your account, go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**

On this page, input the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your identity provider's name, like "OneLogin". |
| `Target URL` | This is the `SAML 2.0 Endpoint (HTTP)` URL provided by OneLogin.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![SAML SSO settings with the toggle selected.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) from the **Company Settings** page.
{% endalert %}

