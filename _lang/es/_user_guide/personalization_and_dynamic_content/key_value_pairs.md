---
nav_title: Pares clave-valor
article_title: Pares clave-valor
page_order: 4
description: "Este artículo de referencia trata de los pares clave-valor y de cómo utilizarlos para enviar cargas útiles de datos adicionales a dispositivos de usuario."
channel:
  - push
  - in-app messages
  - content cards

---

# Pares clave-valor

> Braze permite enviar cargas útiles de datos adicionales a los dispositivos de usuario mediante pares clave-valor. Esta característica está disponible en los canales de mensajería push, dentro de la aplicación, correo electrónico y tarjeta de contenido. 

Utiliza pares clave-valor para añadir metadatos estructurados a los mensajes. Estas cargas útiles de datos adicionales pueden enriquecer los mensajes con información contextual adicional que puede influir en la forma en que se representa o procesa un mensaje.

Como los pares clave-valor son metadatos, estos datos no son necesariamente visibles para el destinatario, pero pueden ser utilizados por tus sistemas o procesos conectados para personalizar la gestión de los mensajes. 

Cada pareja consta de:

- **Clave:** El identificador (Ejemplo: `utm_source`)
- **Valor:** Los datos asociados (Ejemplo: `newsletter`)

## Ejemplos

Aquí tienes algunos casos de uso de ejemplo para añadir metadatos con pares clave-valor:

1. **Parámetros de seguimiento:** Adjuntar parámetros UTM con fines de análisis
   - Clave: `utm_campaign`
   - Valor: `spring_sale`
2. **Etiquetas personalizadas:** Añadir etiquetas para enrutamiento interno o categorización
   - Clave: `priority`
   - Valor: `high`
3. **Desencadenantes del comportamiento:** Metadatos utilizados para desencadenar o personalizar comportamientos dentro de la aplicación
   - Clave: `deep_link`
   - Valor: `app://promo-page`

## Notificaciones push

Se pueden añadir pares clave-valor a las notificaciones push de Android, iOS y Web. Puedes utilizar pares clave-valor para actualizar las métricas internas y el contenido de la aplicación o personalizar las propiedades de las notificaciones push, como la priorización de alertas, la localización y los sonidos.

En el compositor de mensajes, seleccione la pestaña **Configuración**, haga clic en **Añadir nuevo par** y especifique sus pares clave-valor.

### iOS

El servicio de notificaciones push de Apple (APN) permite establecer preferencias de alerta y enviar datos personalizados mediante pares clave-valor. APNs hace uso de la biblioteca ```aps``` reservada por Apple, que incluye claves y valores predeterminados que rigen las propiedades de las alertas.

##### Biblioteca APS

| Clave  | Tipo de valor  | Descripción de valor |
|-------------------|-----------------------------|----------------------------------|
| alerta             | cadena u objeto diccionario | Para las entradas de cadena, muestra una alerta con la cadena como mensaje y los botones Cerrar y Ver; para las entradas que no son de cadena, muestra una alerta o un banner en función de las propiedades secundarias de la entrada. |
| insignia             | número                      | Regula el número que se muestra como distintivo en el icono de la aplicación.                                                                                                                              |
| sonido             | cadena                      | El nombre del archivo de sonido que se reproducirá como alerta; debe estar en la carpeta bundle o ```Library/Sounds``` de la aplicación.                                                                                    |
| content-available | número                      | Los valores de entrada de 1 indican a la aplicación la disponibilidad de nueva información al iniciar o reanudar la sesión. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Biblioteca de propiedades de alerta

| Clave            | Tipo de valor               | Descripción de valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| título         | cadena                   | Una cadena corta que Apple Watch muestra brevemente como parte de una notificación                                                                    |
| cuerpo         | cadena                   | Contenido de la notificación push                                                                                                                  |
| title-loc-key  | cadena o null           | Una clave que establece la cadena de título para la localización actual desde el archivo ```Localizable.strings```                                           |
| title-loc-args | array de cadenas o null | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización del título en title-loc-key                                           |
| action-loc-key | array de cadenas o null  | Si está presente, la cadena especificada establece la localización de los botones Cerrar y Ver                                                         |
| loc-key        | cadena o null           | Una clave que establece el mensaje de notificación para la localización actual desde el archivo ```Localizable.strings```                                   |
| loc-args       | matriz de cadenas         | Valores de cadena que pueden aparecer en lugar de los especificadores de formato de localización en loc-key                                                       |
| launch-image   | cadenas                  | El nombre de un archivo de imagen del paquete de aplicaciones que desea utilizar como imagen de inicio cuando los usuarios pulsen el botón de acción o desplacen la diapositiva de acción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

El compositor de mensajes Braze gestiona automáticamente la creación de las siguientes claves: **alerta** y **sus propiedades**, **contenido-disponible**, **sonido** y **categoría**. 

Estos valores pueden introducirse en la pestaña **Configuración** al crear un mensaje push. Seleccione **Opciones de alerta** y seleccione una clave del diccionario de alertas para que la clave se rellene automáticamente en una nueva entrada de clave-valor.

![][16]
{% raw %}
Cuando Braze envía una notificación push a los APN, la carga útil se formateará como JSON.

**Carga útil simple**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Carga útil compleja**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Pares clave-valor personalizados

Además de los valores de carga útil de la biblioteca ```aps```, puede enviar pares clave-valor personalizados al dispositivo de un usuario. Los valores de estos pares se limitan a los tipos primitivos: diccionario (objeto), matriz, cadena, número y booleano.

![][17]

Los casos de uso de los pares clave-valor personalizados incluyen, entre otros, el mantenimiento de métricas internas y el establecimiento del contexto para la interfaz de usuario. Braze le permite enviar pares clave-valor adicionales junto con una notificación push para que los utilice como desee a través de su aplicación dentro de la [clave de extras][1]. Si prefieres utilizar otra clave, asegúrate de que tu aplicación puede manejar esta clave personalizada.

{% alert warning %}
Debe evitar manejar una clave de nivel superior o diccionario llamado ab en su aplicación.
{% endalert %}

Apple aconseja a sus clientes que eviten incluir información de clientes o cualquier dato sensible como datos de carga útil personalizada. Además, Apple recomienda que ninguna acción asociada a un mensaje de alerta borre los datos de un dispositivo.

{% alert warning %}
Si utilizas la API del proveedor HTTP/2, cualquier carga útil individual que envíes a las APN no puede superar un tamaño de 4096 bytes. La interfaz binaria heredada, que pronto quedará obsoleta, solo admite un tamaño de carga útil de 2048 bytes.
{% endalert %}

###### Campañas activadas por API

Braze permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`. Para acceder a sus extras en campañas activadas por API y campañas programadas activadas por API, en el panel de control establezca una clave como "example_key", y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará lugar a una salida de consola de desarrollador de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze permite enviar cargas útiles de datos adicionales en las notificaciones push mediante pares clave-valor.

##### Carga de datos

De forma similar al push de iOS, puedes enviar pares clave-valor personalizados al dispositivo de un usuario.

Algunos casos de uso de los pares clave-valor personalizados incluyen el mantenimiento de métricas internas y el establecimiento del contexto para la interfaz de usuario, pero pueden utilizarse para cualquier propósito que usted elija.

{% alert important %}
El backend de su aplicación debe ser capaz de procesar pares clave-valor personalizados para que la carga de datos funcione correctamente.
{% endalert %}

###### Campañas activadas por API

Braze permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`. Para acceder a sus extras en campañas activadas por API y campañas programadas activadas por API, en el panel de control establezca una clave como "example_key", y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará lugar a una salida de la consola de desarrollador de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opciones de mensajería del FCM

Las notificaciones push de Android pueden personalizarse aún más con las opciones de mensajes de FCM. Entre ellas se encuentran la [prioridad de notificación][8], el [sonido][10], el retardo, la vida útil y la colapsabilidad. Estos valores pueden especificarse en la pestaña **Configuración** al crear un mensaje push. Consulte [Configuración avanzada de notificaciones][7] push para obtener más instrucciones sobre cómo configurar estas opciones en el compositor de mensajes Braze.

![][18]

### Notificaciones push silenciosas

Una notificación push silenciosa es una notificación push que no contiene ningún mensaje de alerta ni sonido y que se utiliza para actualizar la interfaz o el contenido de tu aplicación en segundo plano. Estas notificaciones hacen uso de pares clave-valor para desencadenar estas acciones de la aplicación en segundo plano. Las notificaciones push silenciosas también impulsan nuestro [seguimiento de desinstalaciones][4].

Los profesionales del marketing deben comprobar que las notificaciones push silenciosas desencadenan el comportamiento esperado antes de enviarlas a los usuarios de su aplicación. Después de redactar su notificación push silenciosa para [iOS][2] o [Android][13], asegúrese de que solo se dirige a un usuario de prueba filtrando por [ID de usuario externo][14] o [dirección de correo electrónico][15].

Tras el lanzamiento de la campaña, debe comprobar que no ha recibido ninguna notificación push visible en su dispositivo de prueba.

{% alert note %}
El sistema operativo iOS puede [bloquear las notificaciones]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) de algunas características (Uninstall Tracking, geovallas e historias push). Ten en cuenta que si experimentas dificultades con estas funciones, la puerta de notificaciones silenciosas de iOS podría ser la causa.
{% endalert %}

## Mensajes dentro de la aplicación

Para añadir un par clave-valor a un mensaje in-app, seleccione la pestaña **Configuración** en el compositor de mensajes, haga clic en **Añadir nuevo par** y especifique sus pares clave-valor.

![][21]

#### Campañas activadas por API

Braze permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`. Para acceder a sus extras en campañas activadas por API y campañas programadas activadas por API, en el panel de control establezca una clave como "example_key", y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará lugar a una salida de la consola de desarrollador de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Correos electrónicos

Tanto SparkPost como SendGrid admiten pares clave-valor en los correos electrónicos. Si utiliza SendGrid, los pares clave-valor se enviarán como [argumentos únicos][11]. SendGrid permite adjuntar un número ilimitado de pares clave-valor de hasta 10.000 bytes de datos. Estos pares clave-valor pueden verse en los mensajes del [webhook de eventos][12] de SendGrid.

{% alert note %}
Los correos electrónicos devueltos no entregarán pares clave-valor a SparkPost o SendGrid.
{% endalert %}

![Pestaña Información de envío del compositor de mensajes de correo electrónico en Braze.][22]

## Tarjetas de contenido

Para añadir un par clave-valor a una tarjeta de contenido, vaya a la pestaña **Configuración** del compositor de mensajes Braze y haga clic en **Añadir nuevo par**.

![Añadir par clave-valor a la tarjeta de contenido][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds
[11]: https://docs.sendgrid.com/for-developers/sending-email/unique-arguments
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}
