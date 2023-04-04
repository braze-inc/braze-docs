---
nav_title: Migrating Push Tokens
article_title: Migrating Push Tokens
page_order: 2

page_type: solution
description: "This help article covers how to migrate push tokens so you can continue sending push messages to your users after switching to Braze."
channel: push
---

# Migrating push tokens

A [push token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) is a unique anonymous identifier that specifies where to send an app's notifications. Braze connects with push service providers like Firebase Cloud Messaging Service (FCMs) for Android and Apple Push Notification Service (APNs) for iOS, and those providers send unique device tokens that identify your app.

Push token migration is the process of importing these previously-created keys into your Braze platform through the API.

If you are a customer who was previously sending push notifications, either on your own or through another provider, push token migration allows you to continue sending push notifications to your users with registered push tokens during the SDK implementation process. Once the Braze SDKs are put in place, they handle push tokens automatically with no need to migrate them via the API.

## Migration via API

Programmatically migrate iOS (APNs) and Android (FCM) tokens to your platform by using the [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint. You can migrate both identified users (users with an associated `external_id`) and anonymous users (users without an `external_id`).

You need to specify your app's `app_id` during push token migration to associate the appropriate push token with the appropriate app. Each app (iOS, Android, etc.) has its own `app_id`, which can be found in the **Developer Console**, under the **API Settings** tab in the **Identification** section. Be sure to use the correct platform's `app_id`.

{% alert important %}
It is not possible to migrate web push tokens through the API. This is because web push tokens do not conform to the same schema as other platforms. 

<br>If you are attempting to migrate web push tokens programmatically, you might see an error like the following: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
As an alternative to API migration, we recommend that you integrate the SDK and allow your token base to repopulate naturally.
{% endalert %}

### Migration if external ID is present
For identified users, set the `push_token_import` flag to `false` (or omit the parameter) and specify the `external_id`, `app_id`, and `token` values in the user `attributes` object. 

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
"attributes" : [
  {
	"push_token_import" : false,
	"external_id": "example_external_id",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
	]
  }
]
```

### Migration if external ID is not present
When importing push tokens from other systems, an `external_id` is not always available. In this circumstance, set your `push_token_import` flag as `true` and specify the `app_id` and `token` values. Braze will create a temporary, anonymous user profile for each token to enable you to continue to message these individuals. If the token already exists in Braze, the request is ignored.

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
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

After import, once the anonymous user launches the Braze-enabled version of your app, Braze will automatically move their imported push token to their Braze user profile and clean up the temporary profile.

Braze will check once a month to find any anonymous profile with the `push_token_import` flag that doesn't have a push token. If the anonymous profile no longer has a push token, we will delete the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to log in to the device with said push token, we will do nothing.

## Importing Android push tokens

{% alert important %}
The following consideration only applies for Android apps. iOS apps will not require these steps because that platform has only one framework for displaying push, and push notifications will render immediately as long as Braze has the necessary push tokens and certificates.
{% endalert %}

If you must send Android push notifications to your users before the Braze SDK integration is complete, use key-value pairs to validate push notifications. 

You must have a receiver to handle and display push payloads. To notify the receiver of the push payload, add the necessary key-value pairs to the push campaign. The values of these pairs are contingent on the specific push partner you used before Braze.

{% alert note %}
For some push notification providers, Braze will need to flatten the key-value pairs so that they can be properly interpreted. To flatten key-value pairs for a specific Android app, contact your Customer Onboarding or Success Manager.
{% endalert %}

_Last updated on December 5, 2022_
