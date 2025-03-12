## Prerequisites

Before you can use this feature, you'll need to integrate the [Braze Cordova SDK]({{site.baseurl}}/developer_guide/platforms/cordova/sdk_integration/) into your app.  After you integrate the SDK, basic push notification functionality is enabled by default. To use [rich push notifications](#setting-up-rich-push-notifications) and [push stories](#setting-up-push-stories), you'll need to set them up individually.

{% alert warning %}
Anytime you add, remove, or update your Cordova plugins, Cordova will overwrite the Podfile in your iOS app's Xcode project. This means you’ll need to set these features up again anytime you modify your Cordova plugins.
{% endalert %}

## Disabling basic push notifications (iOS only)

After you integrate the Braze Cordova SDK for iOS, basic push notification functionality is enabled by default. To disable this functionality in your iOS app, add the following to your `config.xml` file. For more information, see [Optional configurations]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/sdk_integration#optional-configurations).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
