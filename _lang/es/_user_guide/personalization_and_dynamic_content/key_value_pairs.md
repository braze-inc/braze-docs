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

> Esta página explica cómo utilizar pares clave-valor para enviar cargas útiles de datos adicionales a dispositivos de usuario. Esta característica está disponible en los canales de mensajería push, dentro de la aplicación, correo electrónico y tarjeta de contenido.

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

En el creador de mensajes, selecciona la pestaña **Configuración**, selecciona **Añadir nuevo par** y especifica tus pares clave-valor.

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

![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
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

![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Los casos de uso de los pares clave-valor personalizados incluyen, entre otros, el mantenimiento de métricas internas y la configuración del contexto de la interfaz de usuario. Braze te permite enviar pares clave-valor adicionales junto con una notificación push que se utilizará a través de tu aplicación dentro de la [clave de extras]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). Si prefieres utilizar otra clave, confirma que tu aplicación puede manejar esta clave personalizada.

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

Las notificaciones push de Android pueden personalizarse aún más con las opciones de mensajes de FCM. Entre ellas se encuentran la [prioridad de notificación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), el [sonido]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), el retardo, la vida útil y la colapsabilidad. Estos valores pueden especificarse en la pestaña **Configuración** al crear un mensaje push. Consulte [Configuración avanzada de notificaciones]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) push para obtener más instrucciones sobre cómo configurar estas opciones en el compositor de mensajes Braze.

![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificaciones push silenciosas

Una notificación push silenciosa es una notificación push que no contiene ningún mensaje de alerta ni sonido y que se utiliza para actualizar la interfaz o el contenido de tu aplicación en segundo plano. Estas notificaciones hacen uso de pares clave-valor para desencadenar estas acciones de la aplicación en segundo plano. Las notificaciones push silenciosas también impulsan nuestro [seguimiento de desinstalaciones]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Los profesionales del marketing deben comprobar que las notificaciones push silenciosas desencadenan el comportamiento esperado antes de enviarlas a los usuarios de su aplicación. Después de redactar su notificación push silenciosa para [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) o [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), asegúrese de que solo se dirige a un usuario de prueba filtrando por [ID de usuario externo]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) o [dirección de correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Tras el lanzamiento de la campaña, debe comprobar que no ha recibido ninguna notificación push visible en su dispositivo de prueba.

{% alert note %}
El sistema operativo iOS puede [bloquear las notificaciones]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) de algunas características (Uninstall Tracking, geovallas e historias push). Ten en cuenta que si experimentas dificultades con estas funciones, la puerta de notificaciones silenciosas de iOS podría ser la causa.
{% endalert %}

## Mensajes dentro de la aplicación

Para añadir un par clave-valor a un mensaje dentro de la aplicación, selecciona la pestaña **Configuración** en el creador de mensajes, selecciona **Añadir nuevo par** y especifica tus pares clave-valor.

![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### Campañas activadas por API

Braze permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`. Para acceder a sus extras en campañas activadas por API y campañas programadas activadas por API, en el panel de control establezca una clave como "example_key", y un valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Esto dará lugar a una salida de la consola de desarrollador de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Correos electrónicos

Tanto SparkPost como SendGrid admiten pares clave-valor en los correos electrónicos. Si utiliza SendGrid, los pares clave-valor se enviarán como [argumentos únicos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid permite adjuntar un número ilimitado de pares clave-valor de hasta 10.000 bytes de datos. Estos pares clave-valor pueden verse en los mensajes del [webhook de eventos](https://sendgrid.com/docs/for-developers/tracking-events/event/) de SendGrid.

{% alert note %}
Los correos electrónicos devueltos no entregarán pares clave-valor a SparkPost o SendGrid.
{% endalert %}

![Pestaña de información de envío del creador de mensajes de correo electrónico en Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Tarjetas de contenido

Para añadir un par clave-valor a una tarjeta de contenido, ve a la pestaña **Configuración** del creador de mensajes Braze y selecciona **Añadir nuevo par**.

![Añade un par clave-valor a la tarjeta de contenido]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


