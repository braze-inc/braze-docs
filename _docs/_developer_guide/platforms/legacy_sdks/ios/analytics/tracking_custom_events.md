---
nav_title: Track custom events
article_title: Track Custom Events for iOS
platform: iOS
page_order: 2
description: "This reference article covers how to add and track custom events for your iOS application."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Track custom events for iOS

You can record custom events in Braze to learn more about your app's usage patterns and to segment your users by their actions on the dashboard.

Before implementation, be sure to review examples of the segmentation options afforded by custom events, custom attributes, and purchase events in our [best practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), as well as our notes on [event naming conventions]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Adding a custom event

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Adding properties

You can add metadata about custom events by passing an `NSDictionary` populated with `NSNumber`, `NSString`, or `NSDate` values.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```

{% endtab %}
{% endtabs %}

Refer to our [class documentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79) for more information.

### Reserved keys {#event-reserved-keys}

The following keys are reserved and cannot be used as custom event properties:

- `time`
- `event_name`

## Additional resources

- See the method declaration within the `Appboy.h` [file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h). 
- Refer to the [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa) documentation for more information.

