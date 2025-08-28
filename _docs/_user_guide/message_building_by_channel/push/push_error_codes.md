---
nav_title: Common push error messages
article_title: Common Push Error Messages
page_order: 22
page_type: reference
description: "This article covers common push-related error messages for iOS and Android, and walks you through potential solutions."
channel: push
platform:
- iOS
- Android
---

# Common push error messages

> This page covers common error messages for push messaging.

{% tabs %}
{% tab Android %} 
### Push bounced: MismatchSenderId
`MismatchSenderId` indicates an authentication failure. Firebase Cloud Messaging (FCM) authenticates with a couple key pieces of data: senderID and FCM API key.  These should both be validated for accuracy. For more information see the [Android documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) about this issue.

Common failures may include:
- Bad [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Multiple registration if they register with another push service with a different senderID

### Push bounced: InvalidRegistration
`InvalidRegistration` can happen when a push token is malformed. Common failures may include when:
- People are passing Braze registration tokens manually but don't call `getToken()`. For example, they may pass the entire instance ID. The token in the error message looks like `&#124;ID&#124;1&#124;:[regular token]`.  
- People are registering with multiple services. We currently expect push registration intents to arrive old-style, so if folks are registering in multiple places and we catch intents from other services we can get malformed push tokens.

### Push bounced: NotRegistered
`NotRegistered` usually means that the app has been deleted from the device (such as our signal for Uninstall). This can also occur if multiple registration is happening and a second registration is invalidating the push token that Braze receives.

{% endtab %}
{% tab iOS %}

### Push bounced: BadToken

The `BadToken` error may occur for several reasons:
- The push token isn't being sent to us correctly in `[[Appboy sharedInstance] registerPushToken:]`
	- Check the token in the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). It should generally look like a long string of letters and numbers (such as `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). If it doesn't, check the code involved in sending Braze push token errors.<br><br>
- Mismatched provisioning environment:
	- If you register with a development certificate and try to send with a production one, you can see this error.  
	- Braze only supports universal certificates for production environments. Testing push on development environments with a universal certificate will not work. 
	- This reporting sends bouncing in production but not development.<br><br>
- Mismatched provisioning profile:
	- This can happen if your certificate doesn't match the one that was used to get the token. If this is suspected, the next steps include:
		- Ensuring that the push certificate being used to send push from the Braze dashboard and the provisioning profile are configured correctly.
		- Recreating the APNS certification and then recreate the provisioning profile after the APNS certificate is configured to the `app_id`. This can sometimes solve some more visible problems.

### Push bounced: APNS feedback service removed

This generally happens when someone uninstalls. Braze queries the APNS Feedback Service each night to get a list of invalid tokens. For more information, refer to Apple's [Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}
