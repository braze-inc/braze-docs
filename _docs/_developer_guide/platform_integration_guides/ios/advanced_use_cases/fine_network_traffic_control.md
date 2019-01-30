---
nav_title: Fine Network Traffic Control
platform: iOS
page_order: 1
search_rank: 5
---
## Fine Network Traffic Control

### Request Processing Policies

Braze allows the user the option to finely control network traffic using the following protocols:

#### Automatic Request Processing

__*`ABKRequestProcessingPolicy` enum value: `ABKAutomaticRequestProcessing`*__

- This is the **default request policy** value.
- The Braze SDK will automatically handle all server communication, including:
	- Flushing custom events and attributes data to Braze's servers
	- Updating the News Feed
	- Requesting new in-app messages
	- Posting feedback
- Immediate server requests are performed when user-facing data is required for any of Braze's features, such as in-app messages.
- To minimize server load, Braze performs periodic flushes of new user data every few seconds.
- Data can be manually flushed to Braze's servers at any time using the following method:

	```
	[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
	```

#### Automatic Request Processing Except For Custom Event/Attribute Data Flushing

__*`ABKRequestProcessingPolicy` enum value: `ABKAutomaticRequestProcessingExceptForDataFlush`*__

- This protocol is the same as Automatic Request Processing **EXCEPT**:
	- Custom attributes and custom event data is not automatically flushed to the server
- Data can be manually flushed to Braze's servers at any time using the following method:

	```
	[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
	```

#### Manual Request Processing

__*`ABKRequestProcessingPolicy` enum value: `ABKManualRequestProcessing`*__

**This mode is only recommended for advanced use cases.** If you're merely trying to control background flush behavior, consider using `ABKAutomaticRequestProcessingExceptForDataFlush`.

- With the exception of network requests required for internal features, all network traffic is manually controlled. No other communication between the Braze servers and the app will happen unless prompted.
- Standard network requests (e.g., updating the News Feed, flushing custom events and attributes, etc.) are created and added to the network queue. However, server communication will not happen until the following method is called:

	```
	[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
	```

	Upon calling the above method, queued network requests will be performed and user data flushed immediately.
- While in Manual Request Processing mode, `flushDataAndProcessRequestQueue` must be called in order to flush all network-related activity in your app. For example:
	- Setting custom events and attributes
	- Data automatically collected by Braze (e.g., push token, device data)
	- Analytics events such as starting and ending sessions, in-app message impressions, etc.
- If the queue already contains a flush request for the current user, the new request will be merged into the pre-existing request such that only one request will be executed. This is done to minimize server load without impacting expected SDK behavior.
- Braze will still perform automatic network requests for internal features, such as Feedback, Liquid Templating in In-App Messages, Geofences, and Location Tracking. For more details, see the `ABKRequestProcessingPolicy` declaration in [`Appboy.h`][4].

### Setting the Request Processing Policy

#### Set Request Policy On Startup

These policies can be set at app startup time from the [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][3] method. In the `appboyOptions` dictionary, set the `ABKRequestProcessingPolicyOptionKey` to any of the following three `ABKRequestProcessingPolicy` enum values defined below:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
typedef NS_ENUM(NSInteger, ABKRequestProcessingPolicy) {
  ABKAutomaticRequestProcessing,
  ABKAutomaticRequestProcessingExceptForDataFlush,
  ABKManualRequestProcessing
};
```

{% endtab %}
{% tab swift %}

```swift
public enum ABKRequestProcessingPolicy : Int {
    case automaticRequestProcessing
    case automaticRequestProcessingExceptForDataFlush
    case manualRequestProcessing
}
```

{% endtab %}
{% endtabs %}

#### Set Request Policy At Runtime

The request processing policy can also be set during runtime via the `requestProcessingPolicy` property on `Appboy`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()!.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

### Manual Shutdown of In-Flight Server Communication

If at any time an "in-flight" server communication needs to be halted, you must call the following method:

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

After calling this method, you must reset the request processing mode back to Automatic. For this reason, we only recommend calling this if the OS if forcing you to stop background tasks or something similar.

### Policy Regarding Network Requests by the SDK

>  See the aforementioned enumeration values for more information on possible options. This value can be set at start-up as described above or at runtime.

```objc
@property (nonatomic, assign) ABKRequestProcessingPolicy requestProcessingPolicy;
```

##### Implementation Examples
[`MiscViewController.m`][2] in the Stopwatch sample application provides examples of changing the data request processing policy, as well as manually flushing data to Braze.


[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/MiscViewController.m
[3]: #customizing-appboy-on-startup
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h
