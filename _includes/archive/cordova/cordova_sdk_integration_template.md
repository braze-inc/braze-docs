# Push Notifications

If you use the Cordova SDK default setup you won't have to make any new changes client-side. For modified integrations, see [the {{ include.platform }} integration instructions][1].

# In-App Messaging

By default the Cordova SDK supports in-app messages with no changes. See [the {{ include.platform }} integration instructions][11] for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application][4] or the [sample {{ include.platform }} application][3] for implementation samples.

# Analytics

### Setting User IDs

See [the {{ include.platform }} integration instructions][6] for an in depth discussion of when to set and change a user ID.

```javascript
AppboyPlugin.changeUser("YOUR_USER_ID");
```

### Logging Custom Events

See [the {{ include.platform }} integration instructions][7] for in depth discussion of event tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Setting Custom Attributes

See [the {{ include.platform }} integration instructions][8] for in depth discussion of attribute tracking best practices and interfaces.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Logging Purchases

See [the {{ include.platform }} integration instructions][9] for in depth discussion of revenue tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("testPurchaseWithNullCurrency", 10, null, 5, properties);
```

# News Feed

See [the {{ include.platform }} integration instructions][5] for information on how to integrate the news feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal news feed without further integration.

The Braze Cordova SDK has several methods to get the number of read/unread News Feed cards for different categories. See our [sample project implementation][4] for an example.

You can look at the [sample {{ include.platform }} application][3] and [sample Cordova application][3] implementation samples.

# Setting a Custom API Endpoint

A custom API endpoint can be configured via the `config.xml`. For example, to use the EU endpoint, see the following:

```
<platform name="{{ include.config_platform }}">
    ...
    <preference name="{{ include.endpoint_preference_key }}" value="sdk.fra-01.braze.eu" />
</platform>
```

{% if include.platform == 'iOS' %}
[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: https://github.com/Appboy/appboy-cordova-sdk "Cordova Repo"
[3]: https://github.com/Appboy/appboy-ios-sdk "Platform sample app"
[4]: https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js "Sample Cordova Implementation"
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/
[6]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/
[10]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/customer_feedback/
[11]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/
{% endif %}

{% if include.platform == 'Android' %}
[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/
[2]: https://github.com/Appboy/appboy-cordova-sdk "Cordova Repo"
[3]: https://github.com/Appboy/appboy-android-sdk "Platform sample app"
[4]: https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js "Sample Cordova Implementation"
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/customer_feedback/#customer-feedback
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/
{% endif %}
