{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Habilitar la vinculación en profundidad push

De forma predeterminada, el SDK de Braze Cordova no gestiona automáticamente la vinculación en profundidad desde las notificaciones push. Para habilitar la vinculación en profundidad, añade las siguientes preferencias al`platform`elemento  del archivo  `config.xml`de tu proyecto.

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

Para personalizar el comportamiento de la pila de retroceso cuando se siguen vínculos profundos, también puedes añadir estas preferencias opcionales:

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

Para obtener una lista completa de las opciones de configuración push disponibles, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).
