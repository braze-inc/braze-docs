---
nav_title: "Configuración avanzada de campañas push"
article_title: Configuración avanzada de campañas push
page_type: reference
page_order: 6
description: "Este artículo de referencia cubre varias configuraciones avanzadas de campañas push, como opciones de alerta, banderas, sonidos, caducidad, etc."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Configuración avanzada de la campaña push

> Este artículo de referencia cubre varias configuraciones avanzadas de campañas push, como opciones de alerta, banderas, sonidos, caducidad, etc.

Al crear un compromiso push, en el paso **Redactar**, puede seleccionar el icono de engranaje <i class="fas fa-cog"></i> para ver la configuración avanzada del mensaje.

![][1]

## Opciones de alerta

Al seleccionar esta casilla, verá un menú desplegable de valores clave disponibles para ajustar cómo aparecerá la notificación en los dispositivos.

## Añadir indicador de contenido disponible

La bandera `content-available` indica a los dispositivos que descarguen nuevos contenidos en segundo plano. Lo más habitual es que se active si le interesa enviar [notificaciones silenciosas][2].

## Añadir la bandera mutable-content

La bandera `mutable-content` habilita la personalización avanzada del receptor en dispositivos iOS 10+. Este indicador se enviará automáticamente al redactar una [notificación enriquecida][3], independientemente del valor de esta casilla de verificación.

## Sonidos

Aquí, puedes introducir una ruta a un archivo de sonido en el paquete de tu aplicación para especificar un sonido que se reproducirá cuando se reciba el mensaje push. Si el archivo de sonido especificado no existe o si se introduce la palabra clave "por defecto", Braze utilizará el sonido de alerta del dispositivo por defecto.

## ID de contracción
Especifica un ID de contracción para unirse a notificaciones similares. Si envías varias notificaciones con el mismo ID de contracción, el dispositivo solo mostrará la notificación más reciente que se haya recibido. Para más información, consulta la [documentación][4] de Apple.

## Caducidad

Seleccionar **Caducidad** ofrecerá la opción de configurar un plazo de caducidad para tu mensaje. Si el dispositivo de un usuario pierde la conectividad, Braze seguirá intentando enviar el mensaje hasta la hora especificada. Si no se configura, la plataforma tendrá una caducidad predeterminada de 30 días. Tenga en cuenta que las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como un rebote.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
