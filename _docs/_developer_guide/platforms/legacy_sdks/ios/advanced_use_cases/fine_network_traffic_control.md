---
nav_title: Fine network traffic control
article_title: Fine Network Traffic Control for iOS
platform: iOS
page_order: 1
description: "This article covers implementing fine network traffic control for your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fine network traffic control

## Request processing policies

Braze allows the user the option to control network traffic using the following protocols:

### Automatic request processing

***`ABKRequestProcessingPolicy` enum value: `ABKAutomaticRequestProcessing`***

- This is the **default request policy** value.
- The Braze SDK will automatically handle all server communication, including:
    - Flushing custom events and attributes data to Braze servers
    - Updating Content Cards and Geofences
    - Requesting new in-app messages
- Immediate server requests are performed when user-facing data is required for Braze features, such as in-app messages.
- To minimize server load, Braze performs periodic flushes of new user data every few seconds.

Data can be manually flushed to Braze servers at any time using the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### Manual request processing

***`ABKRequestProcessingPolicy` enum value: `ABKManualRequestProcessing`***

- This protocol is the same as automatic request processing except:
    - Custom attributes and custom event data are not automatically flushed to the server throughout the user session.
- Braze will still perform automatic network requests for internal features, such as requesting in-app messages, Liquid templating in in-app messages, Geofences, and location tracking. For more details, see the `ABKRequestProcessingPolicy` declaration in [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h). When these internal requests are made, locally stored custom attributes and custom event data may be flushed to the Braze server, depending on the request type.

Data can be manually flushed to Braze servers at any time using the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## Setting the request processing policy

### Set request policy on startup

These policies can be set at app startup time from the [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) method. In the `appboyOptions` dictionary, set the `ABKRequestProcessingPolicyOptionKey` as shown in the following code snippet:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Set request policy at runtime

The request processing policy can also be set during runtime via the `requestProcessingPolicy` property on `Appboy`:

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
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Manual shutdown of in-flight server communication

If at any time an "in-flight" server communication needs to be halted, you must call the following method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

After calling this method, you must reset the request processing mode to automatic. For this reason, we only recommend calling this if the OS is forcing you to stop background tasks or something similar.

