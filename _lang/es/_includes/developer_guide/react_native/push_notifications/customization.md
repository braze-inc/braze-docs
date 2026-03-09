{% multi_lang_include developer_guide/prerequisites/react_native.md %} También debes [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Personalización de push en React Native

El SDK Braze React Native no permite personalizar las notificaciones push (botones de acción, categorías, fábricas de notificaciones personalizadas) a través de su API JavaScript. Estas características requieren una configuración nativa en tus proyectos iOS y Android.

La siguiente tabla muestra cuáles son las características que requieren una configuración nativa:

| Característica | iOS | Android |
| --- | --- | --- |
| Botones de acción | Configurar en SWIFT/Objective-C nativo | Configurar en Java/Kotlin nativo |
| Categorías de empuje | Configurar en SWIFT/Objective-C nativo | Configurar en Java/Kotlin nativo |
| Fábrica de notificaciones personalizadas | N/A | Configurar en Java/Kotlin nativo |
| Personalización de señales | Configurar en SWIFT/Objective-C nativo | N/A |
| Sonidos personalizados | Configurar en SWIFT/Objective-C nativo | Configurar en Java/Kotlin nativo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Personalización de iOS

Para añadir botones de acción para notificación push, categorías, señales o sonidos personalizados en iOS, implementa la configuración nativa en tu aplicación`AppDelegate`(SWIFT u Objective-C). Consulta [Personalizar notificaciones push – SWIFT]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift) para obtener instrucciones paso a paso.

### Personalización de Android

Para añadir botones de acción para notificación push, categorías o una fábrica de notificaciones personalizada en Android, implementa la configuración nativa en tu proyecto Android. Consulta [Personalizar notificaciones push – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android) para obtener instrucciones paso a paso.
