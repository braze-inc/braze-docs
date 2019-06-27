---
nav_title: Azure Active Directory
page_order: 1
---

# Azure Active Directory
Azure Active Directory, through Microsoft........

## Setting up Azure AD with Braze
Summary
_Prerequisites:_

- You must have admin privileges for both Azure AD and Braze.


### Step 1
Login to Azure.  Click _Add Applications._

![okta_addapplication1][77]


### Step 2
Find the Braze app.

![okta_addapplication2][78]

### Step 3
Enter the appropriate domain based on [your cluster][1].

![okta_entersetup1][79]

### Step 4
Select SAML as your sign on option.

![okta_entersetup2][80]


Click _View Setup Instructions_ and copy the target URL and certificate that is generated.


### Step 5

_Setup the Braze Dashboard._

![okta_companysettings][81]


### Step 6
Back on the Okta Admin page, you can now assign people or groups to the Braze app.

![okta_assignusers][82]

{% alert note %}
__SAML SSO-Only Login__
Go to `Company Settings` in Braze, then the `Security Settings` tab to utilize _Restrict Single Sign-On(SSO)_ and force all users to log in via your chosen SAML SSO method. This will prevent users from logging in via password.  Leaving this unchecked will allow your users to login via your chosen SAML SSO method __or__ their password. This method can be used to help test when first implementing your chosen SAML SSO method.
{% endalert %}

[1]: {{ site.baseurl }}/user_guide/administrative/access_braze/braze_instances/
[77]: {% image_buster /assets/img_archive/okta_addapplication1.png %}
[78]: {% image_buster /assets/img_archive/okta_addapplication2.png %}
[79]: {% image_buster /assets/img_archive/okta_entersetup1.png %}
[80]: {% image_buster /assets/img_archive/okta_entersetup2.png %}
[81]: {% image_buster /assets/img_archive/okta_companysettings.png %}
[82]: {% image_buster /assets/img_archive/okta_assignusers.png %}
