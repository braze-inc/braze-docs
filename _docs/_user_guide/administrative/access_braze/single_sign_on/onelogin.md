---
nav_title: OneLogin
page_order: 5
---

# OneLogin

## Requirements

- Braze account.
- OneLogin account.

## Step 1: Configure OneLogin

1. Log into [OneLogin](https://www.onelogin.com/learn/saml). Click on `Administration`.
2. Go to `Apps` > `Add Apps` in the top navigation bar. Search for “saml test connector” and select `SAML Test Connector (Advanced)`.
3. Name your app (include "Braze" in the Display name for easier distinction) and save it. The SSO configuration steps do not show until you save the app.
4. Go to `Apps` > `Company Apps`. You should see your app listed.
5. Click on your app to configure it.
6. Go to the `Configuration` tab first and fill out the appropriate information. The `RelayState` field should be [your Braze API Key that you can create in the Braze dashboard](#braze-api-key). _This is the only field specific to IdP initiated login._
5. Set the [attributes on the parameter](#attribute-requirements) page.
6. Copy the `Certificate` and `URL` needed to set up the Braze dashboard from under the `SSO` tab.

### Braze API Key

Create your Braze API Key with `sso.saml.login` permission enabled.

![SSO Set Up]({% image_buster /assets/img/sso2.png %})

{% alert important %}
If you do not already have a Braze API Key, go to the `Developer Console` in `App Settings`, then click `Create New API Key`.

Then, scroll down to the SSO section and check the `sso.saml.login` option and then save the API Key.
{% endalert %}


### Attribute Requirements

| SAML Attribute | Required? | Accepted SAML Attributes |
|---|---|---|
|`emailAddress` | Required | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |


## Step 2: Configure Braze

Send the `Certificate` and `URL` to [Braze support]({{ site.baseurl }}/support_contact) so they can turn on your SAML SSO connection.

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/restriction/) from the `Company Settings` page.
{% endalert %}
