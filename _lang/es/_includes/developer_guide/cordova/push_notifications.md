{% multi_lang_include developer_guide/prerequisites/cordova.md %} Después de la integración del SDK, la funcionalidad básica de notificaciones push se habilita de forma predeterminada. Para utilizar [notificaciones push enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) e [historias push]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), deberás configurarlas individualmente. Para utilizar los mensajes push de iOS, también debes cargar un certificado push válido.

{% alert warning %}
Cada vez que añadas, elimines o actualices tus complementos de Cordova, Cordova sobrescribirá el archivo de bibliotecas en el proyecto Xcode de tu aplicación para iOS. Esto significa que tendrás que volver a configurar estas características cada vez que modifiques tus complementos de Cordova.
{% endalert %}

## Habilitar la vinculación en profundidad push

De forma predeterminada, el SDK de Braze Cordova no gestiona automáticamente los vínculos profundos de las notificaciones push. Para habilitar la vinculación en profundidad push, sigue los pasos de configuración que se indican en [Vinculación en profundidad]({{site.baseurl}}/developer_guide/cordova/deep_linking/).
Para obtener más información sobre estas y otras opciones de configuración push, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Desactivar las notificaciones push básicas (solo iOS)

Después de la integración del SDK de Braze Cordova para iOS, la funcionalidad básica de notificaciones push se habilita de forma predeterminada. Para desactivar esta funcionalidad en tu aplicación iOS, añade lo siguiente a tu`config.xml`archivo. Para obtener más información, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
