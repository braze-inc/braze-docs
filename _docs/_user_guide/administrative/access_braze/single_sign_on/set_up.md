---
nav_title: SAML SSO Setup
article_title: SAML SSO Setup
page_order: 0
page_type: tutorial
description: "This article will walk you through how to enable SAML single sign-on for your Braze account."

---

# Service provider (sp) initiated login

> This article will walk you through how to enable SAML single sign-on for your Braze account.

## Requirements

upon setup, you will be asked to provide a sign-on url and an assertion consumer service (acs) url.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> For the subdomain, use the coordinating subdomain listed in [your Braze instance URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br><br> *For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI.* |
| **Entity ID** | `braze_dashboard` |
{: .reset-td-br-1 .reset-td-br-2}

## SAML sso set up

### Configure your identity provider

First, you must set up Braze as a Service Provider (SP) in your Identity Provider (IdP) with the information below.

In addition, you’ll need to set up SAML attribute mapping.

| SAML Attribute | Required? | Accepted SAML Attributes |
|---|---|---|
|`email` | Required | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze only requires `email` in the SAML Assertion.
{% endalert %}

### Configure braze

Once you have set up Braze within your IdP, they will provide a Target URL and `x.509` certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to `Company Settings` > `Security Settings` and toggle the SAML SSO section to `ON`.

On this page, you, input:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen.<br>This is typically your IdP name, like “Okta.” |
| `Target URL` | This is provided after setting up Braze within your IdP.<br> Some IdPs reference this as the SSO URL or SAML 2.0 Endpoint. |
| `Certificate` | The `x.509` certificate is provided by your IdP.|
{: .reset-td-br-1 .reset-td-br-2}

Please make sure that your certificate follows this format when adding it to the dashboard:
```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

When you save your Security Settings and log out, you should now be able to sign in with your IdP.

![Login Page with SSO]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

### Create and enable a braze api key for idp login (optional)

To enable IdP initiated login, you will first need to create an API Key in `Developer Console` > `API Settings`.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within your IdP, which will be used to identify which company the user is trying to log into.

## SSO behavior

Members who opt to use SSO will __no longer be able to use their password as they did prior__. Users who continue to use their password will be able to unless restricted by the settings below. 

## Restriction

you can also choose to restrict the members of your organization to sign-in with either google sso or saml sso. in order to enable, go to `company settings` > `security settings` and select `restrict single sign-on`.

![SSO Restriction]({% image_buster /assets/img/sso3.png %})

By enabling this option, your company's Braze users will no longer be able to log in using a password, even if they have logged in with a password before.
