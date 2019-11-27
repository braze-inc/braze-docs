---
nav_title: Ping Identity
page_order: 5
---

# Ping Identity

[Ping Identity](https://www.pingidentity.com/en/cloud/pingid.html) is a cloud-based, multi-factor authentication (MFA) solution that drastically improves your security posture in minutes. PingID protects applications accessed via single sign-on (SSO), integrates seamlessly with Microsoft Azure AD, Active Directory Federation Services (AD FS) and Windows Login, and allows you to embed branded MFA functionality directly into your own mobile application.

Within PingID's suite of solutions, it offers [PingOne](https://www.pingidentity.com/en/cloud/pingone-enterprise.html) which is a cloud-based identity as a service (IDaaS) framework for secure identity access management. You will use PingOne to give members of your organization secure single sign-on (SSO) to cloud applications.

## Requirements

Upon setup, you will be asked to provide a Sign-On URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| **Sign-On URL** | `https://<SUBDOMAIN>.braze.com/sign_in` <br> For the subdomain, use the coordinating subdomain listed in [your Braze instance URL]({{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/). For example, if your instance is `US-01`, your URL is `https://dashboard-01.braze.com`. This means that your subdomain will be `dashboard-01`. |
| **Assertion Consumer Service (ACS) URL** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *For some IdPs, this can also be referred to as the Reply URL, Audience URL, or Audience URI.* |
| **Entity ID** | `braze_dashboard`|


## Service Provider (SP) Initiated Login within PingOne

### Step 1: Add Braze from the Application Catalog



### Step 2: Configure PingOne Single Sign-On




### Step 3: Configure PingOne within Braze

Once you have setup Braze within your PingOne, they will provide a Target URL (Login URL) and `x.509` certificate which you will input into your Braze account.

After your Account Manager has enabled SAML SSO for your account, go to `Company Settings` > `Security Settings` and toggle the SAML SSO section to `ON`.

On this page, you, input:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your IdP name, like "PingOne.” |
| `Target URL` | This is the Login URL provided by PingOne.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your IdP. |

![Enable SAML SSO]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the `Company Settings` page.
{% endalert %}
