---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "This article will walk you through how to configure Braze to use OneLogin for single sign-on."
---

# OneLogin

> This article will walk you through how to configure braze to use onelogin for single sign-on.

[OneLogin](https://www.onelogin.com/) is a cloud identity platform that provides a comprehensive solution for managing user identities. OneLogin integrates with cloud and on-premise applications using SAML 2.0, for Single Sign-On (SSO), user provisioning, multi-factor authentication, and more.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.

| Requirement      | Details                                                                                                                                                                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Braze Domain** | You will need your Braze domain to set up Braze within OneLogin. If your instance is `US-01`, you will need to input your dashboard URL into the OneLogin dashboard. <br> For example, if your dashboard URL is `https://dashboard-01.braze.com`, you need to input `dashboard-01.braze.com`. |
{: .reset-td-br-1 .reset-td-br-2}

## Service Provider (SP) initiated login within OneLogin

### Step 1: Configure the Braze app

1. Log into [OneLogin](https://app.onelogin.com/login). Click on **Administration**.<br><br> ![Administration]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>

2. Go to **Apps** > **Add Apps** in the top navigation bar. Search for "Braze" and select the Braze app.<br><br> ![Braze result]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>

3. Save the Braze app to your Company.<br><br> ![Braze app]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>

4. Once saved, go to **Configuration** and add your **Braze Domain**.<br><br> ![Configuration]({% image_buster /assets/img/onelogin_4.png %})<br><br>

5. Braze expects the SAML assertions in a [specific format][1]. Under **Parameters** the [attributes][1] supported by Braze should be pre-populated. Simply verify that this is correct.<br><br> ![SAML]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>

6. Copy the **Certificate** and **SAML 2.0 Endpoint (HTTP)** needed to set up the Braze dashboard from under the **SSO** tab.<br><br> ![Certifications]({% image_buster /assets/img/onelogin_6.jpg %})

### Step 2: Configure OneLogin within Braze

Once you have set up Braze within your OneLogin, they will provide a Target URL (`SAML 2.0 Endpoint (HTTP)`) and `x.509` certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to **Company Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

On this page, you, input:

| Requirement   | Details                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| `SAML Name`   | This will appear as the button text on the login screen. This is typically your IdP name, like "OneLogin". |
| `Target URL`  | This is the `SAML 2.0 Endpoint (HTTP)` URL provided by OneLogin.                                           |
| `Certificate` | The `x.509` PEM encoded certificate is provided by your OneLogin.                                          |
{: .reset-td-br-1 .reset-td-br-2}

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Create and enable a Braze API key for IdP login (optional)

To enable IdP initiated login, you will first need to create an API Key in **Developer Console** > **API Settings**.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within OneLogin under **Configuration**, which will be used to identify which company the user is trying to log into.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the **Company Settings** page.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider
