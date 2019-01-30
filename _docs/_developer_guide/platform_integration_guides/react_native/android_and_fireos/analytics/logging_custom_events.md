---
nav_title: Logging Custom Events
platform: React Native
subplatform: Android and FireOS
page_order: 1
---
## Logging Custom Events

See [the Android integration instructions][1] for in depth discussion of event tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
ReactAppboy.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
