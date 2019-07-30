---
nav_title: SAML & Single Sign On
page_order: 5
layout: featured
guide_top_header: "SAML & Single Sign On"
guide_top_text: "Do you want to ensure a secure login for your company's Braze users through a company you're already using? Well, you're in luck! Braze has an integration for that!"

guide_featured_title: "Which secure sign on option would you like to use?"
guide_featured_list:
- name: Azure AD
  link: /docs/user_guide/administrative/access_braze/single-sign-on/azure_ad/
  image: /assets/img/azure_ad.png
- name: Okta IdF
  link: /docs/user_guide/administrative/access_braze/single-sign-on/okta/
  image: /assets/img/okta.png
- name: OneLogin
  link: /docs/user_guide/administrative/access_braze/single-sign-on/onelogin/
  image: /assets/img/onelogin.png

---

# SAML & Single Sign On

Single Sign-On (SSO) provides companies a secure and centralized way of controlling access to the Braze dashboard. In short, a single set of credentials can be used to access different applications, including Braze.

Braze supports Google SSO support via Open ID Connect and SAML SSO which supports the latest Security Assertion Markup Language (SAML 2.0) industry standards.

Google SSO and SAML SSO support are only available to Enterprise and Pro customers. Please contact your Account Manager or Customer Success Manager for more details.

## SAML SSO Requirements

- If you are an Enterprise or Pro customer, SAML SSO must be turned on for your account. Reach out to your Account Manager or Customer Success Manager for access.
- You must have admin privileges for both your IdP and Braze.

{% alert warning %}
We currently do not support user SAML SSO provisioning or de-provisioning. At this time, your company admins can manually add or remove dashboard users.
<br>
<br>
Braze also does not publish a SAML logout URL to invalidate tokens.
{% endalert %}

## Initiated Login Options

Braze’s SAML SSO support allows you to use any SAML-based Identity Provider (IdP) including:

- [Okta]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)
- [Azure Active Directory]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)

Even if your IdP is not listed, Braze should work with any SAML 2.0 compliant provider. We are planning to add more popular IdPs in the future.

{% tabs %}
  {% tab Service Provider %}
### Service Provider (SP) Initiated Login

You will need to create an application for Braze within your IdP. Braze currently has seamless integrations with Okta and Azure Active Directory, but you can simply create a custom SAML application for all other IdPs.

Upon setup, you will be asked to provide a Sign-On URL and an Assertion Consumer Service (ACS) URL.  

Sign-On URL: `https://<SUBDOMAIN>.braze.com/sign_in`

Assertion Consumer Service (ACS) URL: `https://<SUBDOMAIN>/auth/saml/callback`
For some IdPs, this can also be referred to as the Reply URL, Entity ID, Audience URL, or Audience URI.

Enter the appropriate domain based on your cluster.

In addition, you’ll need to setup SAML attribute mapping.

| SAML Attribute | Required? | Schema |
|---|---|---|
|`emailAddress` | Required | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze only requires `emailAddress` in the SAML Assertion.
{% endalert %}

Once you have setup Braze within your IdP, the IdP will provide a Target URL and x.509 certificate which you will input into the Braze dashboard.

After your Customer Success Manager has enabled SAML SSO for your account, you should Company Settings > Security Settings and toggle the SAML SSO section on.
On this page, you will be asked to input:

SAML Name: This will appear as the button text on the login screen. This is typically your IdP name, like “Okta.”

Target URL: This is provided after setting up Braze within your IdP. Some IdPs reference this as the SSO URL or SAML 2.0 Endpoint.

Certificate: The x.509 certificate is provided by your IdP.

When you save your Security Settings and logout, you should now be able to sign in with your IdP.

If you want your dashboard users to only sign in with SAML SSO, you can restrict single sign-on authentication within Company Settings.

  {% endtab %}
  {% tab Identity Provider %}
### Service Provider (SP) Initiated Login

To enable IdP initiated login, you will first need to create an API key in Developer Settings > API Settings.

Input the generated API Key as the RelayState parameter within your IdP which will be used to identity which company the user is trying to log into.


  {% endtab %}
{% endtabs %}

## Restriction

You can also choose to restrict the members of your organization to sign-in with either Google SSO or SAML SSO. In order to enable, go to Company Settings > Security Settings and select Restrict Single Sign-On.



By enabling this option, your company's Braze users will no longer be able to log in using a password, even if they have logged in with a password before.
