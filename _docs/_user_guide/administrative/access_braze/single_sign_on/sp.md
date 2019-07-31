---
nav_title: Service Provider Initiated Login
page_order: 0
---

# Service Provider (SP) Initiated Login

## Requirements

Upon setup, you will be asked to provide a Sign-On URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Entity ID, Audience URL, or Audience URI.* |

## Configure Your SP Account

Then, enter the appropriate [domain based on your cluster]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/#braze-instances) - for example: `https://dashboard-01.braze.com`.

In addition, you’ll need to setup SAML attribute mapping.

| SAML Attribute | Required? | Accepted SAML Attributes |
|---|---|---|
|`email` | Required | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze only requires `email` in the SAML Assertion.
{% endalert %}

## Configure Braze

Once you have setup Braze within your SP, they will provide a Target URL and `x.509` certificate which you will input into the Braze dashboard.

After your Account Manager has enabled SAML SSO for your account, go to `Company Settings` > `Security Settings` and toggle the SAML SSO section to `ON`.

On this page, you, input:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your IdP name, like “Okta.” |
| `Target URL` | This is provided after setting up Braze within your IdP. Some IdPs reference this as the SSO URL or SAML 2.0 Endpoint. |
| `Certificate` | The `x.509` certificate is provided by your IdP. |

When you save your Security Settings and log out, you should now be able to sign in with your IdP.

![Login Page with SSO]({% image_buster /assets/img/sso1.png %})

If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{ site.baseurl }}/user_guide/administrative/access_braze/single-sign-on/restriction/) from the `Company Settings` page.
