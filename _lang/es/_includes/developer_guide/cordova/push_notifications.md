{% multi_lang_include developer_guide/prerequisites/cordova.md %} Después de integrar el SDK, la funcionalidad básica de notificación push está habilitada por defecto. Para utilizar las [notificaciones push enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) y las [historias push]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), tendrás que configurarlas individualmente. Para utilizar los mensajes push de iOS, también tienes que subir un certificado push válido.

{% alert warning %}
Cada vez que añadas, elimines o actualices tus plugins de Cordova, Cordova sobrescribirá el archivo de bibliotecas del proyecto Xcode de tu aplicación para iOS. Esto significa que tendrás que volver a configurar estas características cada vez que modifiques tus plugins de Cordova.
{% endalert %}

## Desactivar las notificaciones push básicas (sólo iOS)

Después de integrar el SDK Braze Cordova para iOS, la funcionalidad básica de notificaciones push está habilitada de forma predeterminada. Para desactivar esta funcionalidad en tu aplicación para iOS, añade lo siguiente a tu archivo `config.xml`. Para más información, consulta [Configuraciones opcionales]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
