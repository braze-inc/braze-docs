---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "This article will walk you through how to configure Braze to use Okta for single sign-on."
---

# Okta

!\[Okta SAML\]\[4\]{: style="float:right;height:200px;margin-left:15px;margin-bottom:15px;"}

> This article will walk you through how to configure Braze to use Okta for single sign-on.

Okta connects any person with any application on any device. It's an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications. With Okta, IT can manage any employee's access to any application or device.
<br>

## Requirements

| requirement                     | details                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------- |
| Okta turned on for your account | Reach out to your Braze Account Manager to have this turned on for your account |
| Okta Admin Privileges           | Please make sure you have Admin Privileges before setting up Okta               |
| Braze Admin Privileges          | Please make sure you have Admin Privileges before setting up Okta               |
{: .reset-td-br-1 .reset-td-br-2}

## Step 1: Configure Braze

### Step 1a: Log in to your Braze account and navigate to Security Settings

Log into your Braze account using an admin account.

Click on your user name and select **Company Settings** from the dropdown menu. Next, select the **Security Settings** tab.

Toggle the green **SAML SSO** switch to **ON** from the right side of the page.

!\[Okta SAML\]\[1\]

### Step 1b: Edit SAML SSO settings

From your Okta Admin Dashboard, you will be provided a `Target URL` (Login URL) and `x.509` certificate which you must input into your Braze account.

| Requirement   | Details                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| `SAML Name`   | This will appear as the button text on the login screen. This is typically your IdP name, For example, "Okta". |
| `Target URL`  | This is the Login URL provided by Okta Admin Dashboard.                                                        |
| `Certificate` | The `x.509` PEM encoded certificate is provided by your IdP. You must copy and paste it into this field.       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

!\[Enable SAML SSO\]\[5\]

Select **Save Changes** at the bottom of the page once completed.

## Step 2: Enable the IdP-initiated flow

Next, you must create your Braze API Key with `sso.saml.login` permission enabled.

- If you do not already have such a Braze API Key, one can be created by going to the **Developer Console** in **Settings**, then click **Create New API Key**.<br>From here, scroll down to the SSO section and check the `sso.saml.login` option and then save the API Key.<br>

!\[SSO Set Up\]\[5\]{: style="max-width:80%"}

## Step 3: Configure Okta

!\[Okta SAML\]\[2\]{: style="float:right;max-width:45%;margin-left:15px;"}

### Step 3a: Navigate to Okta

In Okta, select the **Sign On** tab for the Braze SAML app, then click **Edit**.

### Step 3b: Update default relay state

Enter the API key with `sso.saml.login` permission you made in Step 2, in the **Default Relay State** field.

__Save these new settings.__

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the **Company Settings** page.
{% endalert %}

## Step 4: Log in

You should now be able to log in to Braze using Okta!
[1]: {% image_buster/assets/img/Okta/okta1.png %} [2]: {% image_buster /assets/img/Okta/okta2.png %} [4]: {% image_buster /assets/img/Okta/okta4.png %} [5]: {% image_buster /assets/img/sso2.png %} [6]: {% image_buster /assets/img/samlsso.gif %}