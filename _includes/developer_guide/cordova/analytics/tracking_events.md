{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Logging custom events

To log custom events, use the `logCustomEvent()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) and [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/tracking_custom_events/) guides for logging custom events.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```
