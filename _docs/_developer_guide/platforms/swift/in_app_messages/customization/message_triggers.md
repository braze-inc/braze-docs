---
nav_title: Message Triggers
article_title: Custom in-app message triggers for the Braze Swift SDK
platform: Swift
description: "This reference article covers custom iOS in-app messaging triggering for the Swift SDK."
channel:
  - in-app messages
---

# Custom message triggers

> By default, in-app messages are triggered by events logged by the SDK. Alternatively, you can trigger in-app messages by server-sent events.

## Using server-side events

To trigger in-app messages using server-side events, send a silent push to the device to allow the device to log an SDK-based event. This SDK event can subsequently trigger the user-facing in-app message.

## Customizing message triggers

### Step 1: Handle silent push and key-value pairs

Implement the following function and call it within the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

When the silent push is received, an SDK recorded event "in-app message trigger" will be logged against the user profile. 

{% alert important %}
Due to a push message being used to record an SDK logged custom event, Braze will need to store a push token for each user to enable this solution. For iOS users, Braze will only store a token from the point that a user has been served the OS's push prompt. Before this, the user will not be reachable using push, and the preceding solution will not be possible.
{% endalert %}

### Step 2: Create a silent push campaign

Create a [silent push campaign]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/silent/) that is triggered via the server-sent event. 

![An action-based delivery in-app message campaign that will be delivered to users whose user profiles have the custom event "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

The push campaign must include key-value pair extras, which indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![An action-based delivery in-app message campaign that has two key-value pairs. "CAMPAIGN_NAME" set as "In-app message name example", and "IS_SERVER_EVENT" set to "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

The code within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method checks for key `IS_SERVER_EVENT` and will log an SDK custom event if this is present.

You can alter either the event name or event properties by sending the desired value within the key-value pair extras of the push payload. When logging the custom event, these extras can be used as the parameter of either the event name or as an event property.

### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery in-app message campaign that will be delivered to users who perform the custom event "In-app message trigger" where "campaign_name" equals "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note that these in-app messages will only trigger if the silent push is received while the application is in the foreground.
{% endalert %}
