---
nav_title: Identity Provider Initiated Login
page_order: 1
---

# Identity Provider (IdP) Initiated Login

## Requirements

Upon setup, you will be asked to provide a Sign-On URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Entity ID, Audience URL, or Audience URI.* |
| **IdP Enabled Braze Account** | Create in the Braze's API Settings page. |

## Create and Enable an API Key for IdP Login

To enable IdP initiated login, you will first need to create an API Key in `Developer Settings` > `API Settings`.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

Input the generated API Key as the `RelayState` parameter within your IdP, which will be used to identity which company the user is trying to log into.
