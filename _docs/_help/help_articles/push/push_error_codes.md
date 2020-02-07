---
nav_title: Common Error Codes
page_order: 0
---

Questions to ask, who are "we" and "People", the clients? Our users? Their Users? 

# Common Push Related Error Codes

{% tabs %}
{% tab Android %} 
### Push Bounced: MismatchSenderId
MismatchSenderId indicates an authentication failure.  Gooogle Cloud Messaging (GCM) authenticates with a couple key pieces of data: senderID and GCM API key.  These should both be validated for accuracy. For more information see the [public documentation](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) about this issue.

Common failures:
- Bad [senderID]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/#firebase-integration)
- Multiple registration, this can happen if they register with another push service with a different senderID.

### Push Bounced: InvalidRegistration
InvalidRegistration can happen when a push token is malformed.  

Common failures:
- People are passing Braze registration tokens manually but don’t call getToken() (i.e. they instead pass the entire instance id). <br>The token in the error message looks like &#124;ID&#124;1&#124;:[regular token].  
- Multiple registration, people are registering with multiple services. <br>We currently expect push registration intents to arrive old-style, so if folks are registering in multiple places and we catch intents from other services we can get malformed push tokens.

### Push Bounced: NotRegistered
NotRegistered usually means that the app has been deleted from the device (i.e. Braze's signal for Uninstall).  
This can also happen if multiple registration is happening and a second registration is invalidating the push token Braze recieves.

{% endtab %}
{% tab iOS %}

### Push Bounced: Error sending to bad push token

This can happen for several reasons:
- The push token isn’t being sent to us correctly in [[Appboy sharedInstance] registerPushToken:].
	- Look at the token in the Message Activity Log 
	- It should generally look like `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`
	- i.e. a string about that length of letters and numbers
	- If it doesn’t, look at code for sending us the push token for errors
- Provisioning environment mismatch
	- If you register with a development certificate and try to send with a production one, you can see this error.  
	- Note:  Appboy only supports universal certificates for production environments and testing push on their development environments with a universal certificate will not work. 
	- Look for folks reporting sends bouncing in prod but not development
Bad provisioning profile/mismatch
	- If your certificate just doesn’t match the one that was used to get the token, this can also happen
	- If this is suspected
		- Ensure that the push certificate being used to send push from the Appboy dashboard and the provisioning profile are configured correctly.
		- If all else fails, a nuclear option, recreating the APNS cert and then recreating the provisioning profile once the APNS certificate is configured to the app id can sometimes solve some more opaque problems.

### Push Bounced: APNS Feedback Service Removed

This generally happens when someone uninstalls. Appboy query’s the APNS Feedback Service each night to get a list of invalid tokens. See Apple’s Docs and Description on the Feedback Service.

If push isn't delivered, check if it bounced by looking inthe de

| Status Code | Error String | Description |
| ----------- | ------------ | ----------- |
| 403 | `BadCertificate` | The certificate was bad.|
| 403 | `BadCertificateEnvironment` | The client certificate was for the wrong environment. |
| 403 | `ExpiredProviderToken` | The provider token is stale and a new token should be generated. |
| 403 | `Forbidden` | The specified action is not allowed. |
| 403 | `InvalidProviderToken` | The provider token is not valid or the token signature could not be verified. |
| 403 | `MissingProviderToken` | No provider certificate was used to connect to APNs and Authorization header was missing or no provider token was specified. |
| 404 | `BadPath` | The request contained a bad `:path` value. |
| 405 | `MethodNotAllowed` | The specified `:method` was not `POST`. |
| 410 | `Unregistered` | The device token is inactive for the specified topic.<br><br> Expected HTTP/2 status code is `410`; see [Table 8-4](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html). |

For a complete list of status codes. Check out the [Apple Developer Documentation](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}

[1]: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html

