{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Activation de la création de liens profonds push

Par défaut, le SDK Braze Cordova ne gère pas automatiquement la création de liens profonds push à partir des notifications. Pour activer la création de liens profonds push, veuillez ajouter les préférences suivantes à `platform`l'élément dans le fichier`config.xml` de votre projet.

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

Pour personnaliser le comportement de la pile arrière lorsque des liens profonds sont suivis, vous pouvez également ajouter ces préférences facultatives :

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

Pour obtenir la liste complète des options de configuration push disponibles, veuillez consulter [la section Configurations facultatives]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).
