{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Enabling push deep linking

By default, the Braze Cordova SDK doesn't automatically handle push deep linking from notifications. To enable push deep linking, add the following preferences to the `platform` element in your project's `config.xml` file.

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

To customize back stack behavior when deep links are followed, you can also add these optional preferences:

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

For a full list of available push configuration options, see [Optional configurations]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).
