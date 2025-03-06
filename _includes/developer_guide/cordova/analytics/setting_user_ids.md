{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Setting user IDs

To set user IDs, use the `changeUser()` method. For more in-depth instructions, see the [Android]({{site.baseurl}}/developer_guide/platforms/android/analytics/setting_user_ids/) and [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/setting_user_ids/) guides for setting user IDs.

```javascript
BrazePlugin.changeUser("USER_ID");
```
