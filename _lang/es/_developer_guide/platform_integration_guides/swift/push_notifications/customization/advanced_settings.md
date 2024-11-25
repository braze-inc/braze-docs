---
nav_title: Configuración de push
article_title: Configuración de push para iOS
platform: Swift
page_order: 7
description: "Este artículo de referencia trata sobre la configuración avanzada de las notificaciones push de iOS, como las opciones de alerta, los sonidos, la caducidad, etc., para el SDK de Swift."
channel:
  - push

---

# Configuración de push

> Al crear una campaña push a través del panel, haz clic en la pestaña **Configuración** del paso **Redactar** para ver la configuración avanzada disponible.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Pares clave-valor

Braze te permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`, junto con una notificación push a tu aplicación. Los extras pueden definirse a través del panel o de la API y estarán disponibles como pares clave-valor dentro del diccionario `notification` pasado a tus implementaciones de delegados push.

## Opciones de alerta

Selecciona la casilla **Opciones de alerta** para ver un desplegable de valores clave disponibles para ajustar cómo aparece la notificación en los dispositivos.

## Añadir la bandera de contenido disponible

Marca la casilla **Añadir indicador de contenido disponible** para indicar a los dispositivos que descarguen nuevos contenidos en segundo plano. Lo más habitual es marcar esta opción si te interesa enviar [notificaciones silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Añadir la bandera de contenido mutable

Marca la casilla **Añadir indicador de contenido mutable** para habilitar la personalización avanzada del receptor. Esta bandera se enviará automáticamente al componer una [notificación enriquecida]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), independientemente del valor de esta casilla.

## Actualizar recuento de credenciales de la aplicación

Introduce el número con el que quieres actualizar el recuento de tus señales o utiliza la sintaxis Liquid para establecer condiciones personalizadas. También puedes actualizar el recuento de una señal de mensaje mediante programación: consulta nuestro artículo dedicado [al recuento de señales]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/).

## Sonidos

Si quieres que tu notificación push vaya acompañada de un sonido personalizado cuando se reciba, utiliza el campo **Sonido** para especificar la URL del protocolo de tu archivo de sonido. Para más información sobre la personalización, consulta nuestro artículo [sobre sonidos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/).

## ID de contracción

Especifica un ID de colapso para agrupar notificaciones similares. Si envías varias notificaciones con el mismo ID de colapso, el dispositivo sólo mostrará la notificación recibida más recientemente. Consulta la documentación de Apple sobre [notificaciones agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Caducidad

Si marcas la casilla **Caducidad**, podrás establecer un tiempo de caducidad para tu mensaje. Si el dispositivo de un usuario pierde la conectividad, Braze seguirá intentando enviar el mensaje hasta la hora especificada. Si no se configura, la plataforma tendrá una caducidad predeterminada de 30 días. Ten en cuenta que las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.

