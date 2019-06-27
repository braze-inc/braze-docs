---
nav_title: OneLogin
page_order: 1
---

# OneLogin
Okta connects any person with any application on any device. It's an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications. With Okta, IT can manage any employee's access to any application or device.

## Setting up Okta with Braze
Braze, acting as a service provider, has created a simple step-by-step guide to setup Okta as your Identification Provider. This will ensure all control is handled based on your companies security settings.

_Prerequisites:_

- Okta must be turned on for your account.  Reach out to your success manager to have this turned on.
- You must have admin privileges for both Okta and Braze.


### Step 1
Login to Okta.  Click _Add Applications._

![okta_addapplication1][77]


### Step 2
Find the Braze app.

![okta_addapplication2][78]

### Step 3
Enter the appropriate domain based on your cluster.

Instance  | Dashboard URL
----------|-------------------------
Braze 01 | https://dashboard-01.braze.com
Braze 02 | https://dashboard-02.braze.com
Braze 03 | https://dashboard-03.braze.com
Braze EU | https://dashboard-01.braze.eu

![okta_entersetup1][79]

### Step 4
Select SAML as your sign on option.

![okta_entersetup2][80]


Click _View Setup Instructions_ and copy the target URL and certificate that is generated.


### Step 5

_Setup the Braze Dashboard._

* Log on to Braze Dashboard using an admin account.
* Click on the drop down from your user name in the upper right corner, select _Company Settings._
* Select the _Security Settings_ tab.
* Turn on the _Okta Single Sign-On (SSO)_ switch.
* Enter the Target URL with the Embed Link from the Okta Admin Console.
* Enter the Certificate with the Certificate you downloaded from the Okta Admin Console (open the file, copy, and paste).
* Click _Save Changes_ at the bottom of the page.

![okta_companysettings][81]


### Step 6
Back on the Okta Admin page, you can now assign people or groups to the Braze app.

![okta_assignusers][82]

#### Optional: Okta-Only Log In
Go to Company Settings on the Braze app, then the Security Settings tab to utilize _Restrict Single Sign-On(SSO)_ and force all users to log in via Okta only. This will prevent users from logging in via password.  Leaving this unchecked will allow your users to login via Okta or their password. This method can be used to help test when first implementing Okta.


[77]: {% image_buster /assets/img_archive/okta_addapplication1.png %}
[78]: {% image_buster /assets/img_archive/okta_addapplication2.png %}
[79]: {% image_buster /assets/img_archive/okta_entersetup1.png %}
[80]: {% image_buster /assets/img_archive/okta_entersetup2.png %}
[81]: {% image_buster /assets/img_archive/okta_companysettings.png %}
[82]: {% image_buster /assets/img_archive/okta_assignusers.png %}
