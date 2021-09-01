---
nav_title: Push Token Migration
page_order: 1

page_type: solution
description: "This article covers how to migrate push tokens so you can continue sending push messages to your users after switching to Braze."
channel: push
noindex: true
---

# Push Token Migration

A push token is a unique key, created and assigned by Apple or Google to create a connection between an app and an iOS, Android, or web device. Push Token migration is the importing of those already-generated keys into Braze’s platform.

Braze customers who were previously sending push notifications, either on their own or with a different provider, often have a list of users with registered push tokens.

To continue sending push messages to these users during the Braze SDK integration process, you can import these tokens into Braze and target those users using Braze's campaign tool.

{% comment %}
These campaigns will have to be configured with proper key-value pairs to ensure that the client’s existing push notification setup will recognize and display the push payload we send to users’ devices. While we will record the number of pushes we send, no data on open rates or conversion events is tracked as that requires the Braze’s SDK to be integrated.
{% endcomment %}

## Migration via API

Push tokens can either be uploaded for identified users or anonymous users. This means that either an `external_id` needs to present, or the anonymous users must have the `push_token_import` flag set to `true`. 

The `app_id` required can be found in the **Developer Console**, under the **API Settings** tab in the **Identification** section. Each app (iOS, Android, Web, etc.) has its own `app_id` - be sure to use the correct platform's `app_id`.

#### Migration if External ID is Present
```json
"attributes" : [
  {
	"push_token_import" : false,
	"external_id": "external_id1",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
	]
  }
]
```

{% alert note %}
When importing push tokens from other systems, an `external_id` is not always available. To maintain communication with these users during your transition to Braze, you can import the legacy tokens for anonymous users without providing `external_id` by specifying `push_token_import` as `true`.
{% endalert %}

#### Migration if External ID is not Present

These tokens can be migrated by [importing them with our API]({{site.baseurl}}/api/endpoints/user_data/#push-token-import).

To do this, use the `users/track` endpoint and post the following information:

```json
"attributes" : [
  {
	"push_token_import" : true,
	"push_tokens": [
	  { "app_id": "", "token": "", "device_id": "" }
	]
  }
]
```

Example:

```json
"attributes": [ 
  {
    "push_token_import" : true,
	"email": "braze.test1@testbraze.com",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
	]
  },
    
  {
	"push_token_import" : true,
	"email": "braze.test2@testbraze.com",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
	"YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
	]
  }
]
```

When specifying `push_token_import` as `true`:

* `external_id` and `braze_id` should __not__ be specified
* The attribute object __must__ contain a push token
* If the token already exists in Braze, the request is ignored; otherwise, Braze will create a temporary, anonymous user profile for each token to enable you to continue to message these individuals

After import, as each user launches the Braze-enabled version of your app, Braze will automatically move their imported push token to their Braze user profile and clean up the temporary profile.

Braze will check once a month to find any anonymous profile with the `push_token_import` flag that doesn’t have a push token. If the anonymous profile no longer has a push token, we will delete the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to login to the device with said push token, we will do nothing.

### Web Push Tokens
Web push tokens contain extra fields that other platforms do not. As a result, we recommend that you integrate push and allow your token-base to repopulate naturally.

## Sending Push before Braze SDK Integration (Android Only)

{% alert warning %}
Please note that this solution only applies for Android users. iOS users will not receive push with this method. iOS does not require these steps because there is only one framework for displaying push. Push notifications will render immediately as long as Braze has the necessary push tokens and certificates.
{% endalert %}

If you find that you must send a push notification to your users before the Braze SDK integration is complete, you can use key-value pairs to validate push notifications.

__You must have a receiver to handle and display push payloads.__

To notify the receiver of the push payload, add the necessary key-value pairs to the push campaign. The values of these pairs is contingent on the specific push partner you used before Braze.

_For some push notification providers, Braze will need to flatten the key-value pairs so that they can be properly interpreted. To flatten key-value pairs for a specific Android app, contact your Customer Onboarding/Success Manager._
