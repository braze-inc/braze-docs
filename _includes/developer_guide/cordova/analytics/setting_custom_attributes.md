{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Setting custom attributes

To set custom attributes, use the `setCustomUserAttribute()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platforms/android/analytics/setting_custom_attributes/) and [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/setting_custom_attributes/) guides setting custom attributes.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
