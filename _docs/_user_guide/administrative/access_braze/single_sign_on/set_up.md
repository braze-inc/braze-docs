---
nav_title: SAML SSO Setup
article_title: SAML SSO Setup
page_order: 0
page_type: tutorial
description: "This article will walk you through how to enable SAML single sign-on for your Braze account."

---

# Service Provider (SP) initiated login

> This article will walk you through how to enable SAML single sign-on for your Braze account.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Sign-On URL | `https://<SUBDOMAIN>.braze.com` <br><br> For the subdomain, use the coordinating subdomain listed in your [Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI. |
| Entity ID | `braze_dashboard` |
| RelayState API key | Go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions, and then input the generated API key as the `RelayState` parameter within your IdP. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find your API keys under **Settings** at **Developer Console** > **API Settings**.
{% endalert %}

## SAML SSO setup

### Configure your identity provider

First, you must set up Braze as a Service Provider (SP) in your Identity Provider (IdP) with the following information. In addition, you'll need to set up SAML attribute mapping.

{% alert important %}
If you plan on using Okta as your identity provider, make sure to use the pre-built integration found on the [Okta site](https://www.okta.com/integrations/braze/).
{% endalert %}

| SAML Attribute | Required? | Accepted SAML Attributes |
|---|---|---|
|`email` | Required | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze only requires `email` in the SAML Assertion.
{% endalert %}

### Configure Braze

Once you have set up Braze within your IdP, they will provide a Target URL and `x.509` certificate which you will input into your Braze account.

After your account manager has enabled SAML SSO for your account, go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), select your account icon and go to **Company Settings** > **Security Settings** to find the SAML SSO section.
{% endalert %}

On this page, input the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen.<br>This is typically your IdP name, like "Okta." |
| `Target URL` | This is provided after setting up Braze within your IdP.<br> Some IdPs reference this as the SSO URL or SAML 2.0 Endpoint. |
| `Certificate` | The `x.509` certificate is provided by your IdP.|
{: .reset-td-br-1 .reset-td-br-2}

Make sure that your certificate follows this format when adding it to the dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Opening Security Settings and adding SAML SSO details]({% image_buster /assets/img/samlsso.gif %})

When you save your Security Settings and log out, you should now be able to sign in with your IdP.

![Dashboard login screen with SSO enabled]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## SSO behavior

Members who opt to use SSO will no longer be able to use their password as they did prior. Users who continue to use their password will be able to unless restricted by the following settings.

## Restriction

You can also choose to restrict the members of your organization to sign-in with either Google SSO or SAML SSO. In order to enable, go to **Security Settings** and select either **Enforce Google SSO only login** or **Enforce custom SAML SSO only login**.

![Authentication Rules section of Security Settings page]({% image_buster /assets/img/sso3.png %})

By enabling this option, your company's Braze users will no longer be able to log in using a password, even if they have logged in with a password before.
