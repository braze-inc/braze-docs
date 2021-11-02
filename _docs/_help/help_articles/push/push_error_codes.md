---
nav_title: Common Push Error Messages
article_title: Common Push Error Messages
page_order: 0

page_type: solution
description: "This help article covers common push-related error messages for iOS and Android, and walks you through potential solutions."
channel: push
platform:
- iOS
- Android
---

# Common push error messages

{% tabs %}
{% tab Android %} 
### Push bounced: MismatchSenderId
MismatchSenderId indicates an authentication failure.  Google Cloud Messaging (GCM) authenticates with a couple key pieces of data: senderID and GCM API key.  These should both be validated for accuracy. For more information see the [public documentation](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) about this issue.

Common failures may include:
- Bad [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Multiple registration if they register with another push service with a different senderID

### Push bounced: InvalidRegistration
InvalidRegistration can happen when a push token is malformed.  

Common failures may include:
- People are passing Braze registration tokens manually but don’t call getToken() (i.e. they instead pass the entire instance id). <br>The token in the error message looks like &#124;ID&#124;1&#124;:[regular token].  
- Multiple registration, people are registering with multiple services. <br>We currently expect push registration intents to arrive old-style, so if folks are registering in multiple places and we catch intents from other services we can get malformed push tokens.

### Push bounced: NotRegistered
NotRegistered usually means that the app has been deleted from the device (i.e. Braze's signal for Uninstall).  
This can also happen if multiple registration is happening and a second registration is invalidating the push token Braze recieves.

{% endtab %}
{% tab iOS %}

### Push bounced: Error sending to bad push token

This can happen for several reasons:
- __The push token isn’t being sent to us correctly in [[Appboy sharedInstance] registerPushToken:]__
	- Check the token in the Message Activity Log. It should generally look like a long string of letters and numbers. (e.g `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`)
	- If it doesn’t, check the code involved in sending Braze push token errors.<br><br>
- __Provisioning environment mismatch__
	- If you register with a development certificate and try to send with a production one, you can see this error.  
	- Braze only supports universal certificates for production environments. Testing Push on development environments with a universal certificate will not work. 
	- This reporting sends bouncing in production but not development.<br><br>
- __Bad provisioning profile/mismatch__
	- If your certificate doesn’t match the one that was used to get the token, this error can happen.
	- If this is suspected, the next steps include:
		- Ensuring that the push certificate being used to send push from the Braze dashboard and the provisioning profile are configured correctly.
		- If this does not work, consider recreating the APNS certification and then recreate the provisioning profile once the APNS certificate is configured to the app id. This can sometimes solve some more opaque problems.

### Push bounced: APNS feedback service removed

This generally happens when someone uninstalls. Braze queries the APNS Feedback Service each night to get a list of invalid tokens. See [Apple’s Docs and Description on the Feedback Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).


{% endtab %}
{% endtabs %}

_Last updated on August 17, 2021_
