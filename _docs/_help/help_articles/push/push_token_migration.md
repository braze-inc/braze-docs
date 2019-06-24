---
nav_title: Push Token Migration
page_order: 1
---

# Push Token Migration

A push token is a unique key, created and assigned by Apple or Google to create a connection between an app and an iOS, Android, or web device. Push Token migration is the importing of those already-generated keys into Braze’s platform.

Braze customers who were previously sending push notifications, either on their own or with a different provider, often have a list of users with registered push tokens.

To continue sending push messages to these users during the Braze SDK integration process, you can import these tokens into Braze and target those users using Braze's Campaign tool.

{% comment %}
These campaigns will have to be configured with proper key-value pairs to ensure that the client’s existing push notification setup will recognize and display the push payload we send to users’ devices. While we will record the number of pushes we send, no data on open rates or conversion events is tracked as that requires the Braze’s SDK to be integrated.
{% endcomment %}

## Migration via API

You can migrate your tokens by [importing them with our API]({{ site.baseurl }}/api/endpoints/user_data/#push-token-import).

Use the `users/track` endpoint and post the following information:

```json
"app_group_id" :
"attributes" : [
    {
      "push_token_import" : true
      "push_tokens": [
          "app_id": ""
          "token": ""
          "device_id": ""
      ]
    }
]
```

When specifying push_token_import as `true`:

- The `external_id` and `braze_id` should __not__ be specified.
- The attribute object must contain a push token
- If the token already exists in Braze, the request is ignored. Otherwise, Braze will create a temporary, anonymous user profile for each token to enable you to continue to message those users.

After import, as each user launches the Braze-enabled version of your app, Braze will automatically move their imported push token to their Braze user profile and clean up the temporary profile.

Braze will check once a month to find any anonymous profile with the `push_token_import` flag that doesn’t have a push token. If the anonymous profile no longer has a push token, we will delete the profile. However, if the anonymous profile still has a push token, suggesting that the actual user has yet to login to the device with said push token, we will do nothing.

## Sending Push before Braze SDK Integration (Android Only)

{% alert warning %}
Please note that this solution only applies for Android users. iOS users will not receive push with this method. iOS does not require these steps because there is only one framework for displaying push. Push notifications will render immediately as long as Braze has the necessary push tokens and certificates.
{% endalert %}

If you find that you must send a push notification to your users before the Braze SDK integration is complete, you can use key-value pairs to validate push notifications.

__You must have a receiver to handle and display push payloads.__

To notify the receiver of the push payload, add the necessary key-value pairs to the push campaign. The values of these pairs is contingent on the specific push partner you used before Braze.

_For some push notification providers, you will need to flatten the key-value pairs so that they can be properly interpreted. To flatten key-value pairs for a specific Android app, navigate to the “Internal Tools Page”, then “Company Settings”. Scroll to the “Flatten Push Payload” section, where you can add the setting for specific apps in your  company’s app group._
