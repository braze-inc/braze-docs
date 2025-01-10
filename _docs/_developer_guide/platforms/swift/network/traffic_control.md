---
nav_title: Network Traffic Control
article_title: Fine Network Traffic Control for the Braze Swift SDK
platform: Swift
page_order: 0
description: "This article covers implementing network traffic control for the Swift SDK."

---

# Network traffic control

> Learn how to implement network traffic control for the Braze Swift SDK.

## Requesting processing policies

Braze allows the user the option to control network traffic using the following protocols:

### Automatic request processing

***`RequestPolicy` enum value: `automatic`***

This is the **default request policy** value. With this value, immediate server requests are performed when user-facing data is required for Braze features, such as in-app messages.

The Braze SDK will automatically handle all server communication, including:
- Flushing custom events and attributes data to Braze servers
- Updating Content Cards and geofences
- Requesting new in-app messages

To minimize server load, Braze performs periodic flushes of new user data every few seconds.

### Manual request processing

***`RequestPolicy` enum value: `manual`***

This protocol is the same as automatic request processing except:
- Custom attributes and custom event data are not automatically flushed to the server throughout the user session.
- Braze will still perform automatic network requests for internal features, such as requesting in-app messages, Liquid templating in in-app messages, geofences, and location tracking. For more details, see the `Braze.Configuration.Api.RequestPolicy.manual` [documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual). When these internal requests are made, locally stored custom attributes and custom event data may be flushed to the Braze server, depending on the request type.

### Manually flushing user data

Data can be manually flushed to Braze servers at any time using the following method:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% endtabs %}
## Setting the request processing policy

### Set request policy on startup

These policies can be set at app startup time when you initialize the Braze configuration. In the `configuration` object, set the [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)) as shown in the following code snippet:

{% tabs %}
{% tab swift %}

```swift
configuration.api.requestPolicy = .automatic
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```

{% endtab %}
{% endtabs %}


