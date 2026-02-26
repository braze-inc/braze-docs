{% multi_lang_include developer_guide/prerequisites/cordova.md %} After you integrate the SDK, basic push notification functionality is enabled by default. To use [rich push notifications]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) and [push stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), you'll need to set them up individually. To use iOS push messages, you also need to upload a valid push certificate.

{% alert warning %}
Anytime you add, remove, or update your Cordova plugins, Cordova will overwrite the Podfile in your iOS app's Xcode project. This means you’ll need to set these features up again anytime you modify your Cordova plugins.
{% endalert %}

## Enabling push deep linking

By default, the Braze Cordova SDK doesn't automatically handle deep links from push notifications. To enable push deep linking, add the following preferences to your `config.xml` file.

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_forward_universal_links" value="YES" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
</platform>
```
{% endtab %}
{% endtabs %}

For more details about these and other push configuration options, see [Optional configurations]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Disabling basic push notifications (iOS only)

After you integrate the Braze Cordova SDK for iOS, basic push notification functionality is enabled by default. To disable this functionality in your iOS app, add the following to your `config.xml` file. For more information, see [Optional configurations]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
