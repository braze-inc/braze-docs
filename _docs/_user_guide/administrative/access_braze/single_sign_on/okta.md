---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "This article will walk you through how to configure Braze to use Okta for single sign-on." 

---

# Okta 

> Okta connects any person with any application on any device. It's an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications. With Okta, your IT team can manage any employee's access to any application or device.

## Requirements

| Requirement | Details |
| ----------- | ------- |
| Okta turned on for your account | Contact your Braze account manager to have this turned on for your account. |
| Okta admin privileges | Make sure you have admin privileges before setting up Okta. |
| Braze admin privileges | Make sure you have admin privileges before setting up Okta. |
| RelayState API key | To enable IdP login, go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Configure Braze

### Step 1a: Navigate to Security Settings in Braze

After your account manager has enabled SAML SSO for your account, go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

![Okta SAML SSO enabled on the Security Settings page.]({% image_buster/assets/img/Okta/okta1.png %})

### Step 1b: Edit SAML SSO settings

From your Okta Admin dashboard, Okta provides you with a target URL (login URL) and `x.509` certificate, which you must input into your Braze account's **Security Settings** page.

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your identity provider's name, For example, "Okta". |
| `Target URL` | This is the login URL provided by Okta Admin dashboard. Find it by going to **Applications** > your application > **General** tab > **App Embed Link** > **Embed Link**. |
| `Certificate` | The `x.509` PEM encoded certificate is provided by your identity provider. You must copy and paste it into this field. Retrieve it in Okta by going to **SAML Signing Certificates** and selecting **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Select **Save Changes** at the bottom of the page when completed.

## Step 2: Configure Okta

In Okta, select the **Sign On** tab for the Braze SAML app, then click **Edit**. 

Next, enter the RelayState API key with `sso.saml.login` permission in the **Default Relay State** field. 

![Okta Default RelayState in the Sign On tab.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Make sure to save these new settings.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) from the **Company Settings** page.
{% endalert %}

## Step 3: Log in

You should now be able to log in to Braze using Okta!

![Braze dashboard login with Okta SSO enabled.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

