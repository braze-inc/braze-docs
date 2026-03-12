{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Push-Deeplinking aktivieren

Standardmäßig verarbeitet das Braze Cordova SDK Push-Deeplinks aus Push-Benachrichtigungen nicht automatisch. Um Push-Deeplinking zu aktivieren, fügen Sie bitte die folgenden Einstellungen zum`platform`Element in der Datei `config.xml`Ihres Projekts hinzu.

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

Um das Verhalten des Backstacks beim Folgen von Deeplinks anzupassen, können Sie auch die folgenden optionalen Einstellungen hinzufügen:

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

Eine vollständige Liste der verfügbaren Push-Konfigurationsoptionen finden Sie unter [Optionale Konfigurationen]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).
