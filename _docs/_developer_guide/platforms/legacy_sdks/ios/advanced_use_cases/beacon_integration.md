---
nav_title: Beacon integration
article_title: Beacon Integration for iOS
platform: iOS
page_order: 4
description: "This article covers logging custom events using Infillion Beacons for iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Beacon integration

Here, we will walk through how to integrate specific kinds of beacons with Braze to allow for segmentation and messaging.

## Infillion Beacons

Once you have your Infillion Beacons set up and integrated into your app, you can log custom events like a visit starting or ending or a beacon being sighted. You can also log properties for these events, like the place name or the dwell time.

To log a custom event when a user enters a place, input this code into the `didBeginVisit` method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

The `flushDataAndProcessRequestQueue` confirms that your event will log even if the app is in the background, and the same process can be implemented for leaving a location. Note that this will create and increment a unique custom event for each new place that the user enters. If you anticipate creating more than 50 places, we recommend you create one generic "Place Entered" custom event and include the place name as an event property.
