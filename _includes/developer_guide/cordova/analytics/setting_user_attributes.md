{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Setting custom user attributes

To set custom user attributes, use the `setCustomUserAttribute()` method. For more in-depth information, refer to the relevant [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) and [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) information.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
