---
nav_title: Notificaciones push silenciosas
article_title: Notificaciones push silenciosas para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia cubre la implementación de notificaciones push silenciosas en tu aplicación iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notificaciones push silenciosas

Las notificaciones push te permiten avisar a tu aplicación cuando se producen eventos importantes. Puedes enviar una notificación push cuando tengas nuevos mensajes instantáneos que entregar, alertas de noticias de última hora que enviar o el último episodio del programa de TV favorito de tu usuario listo para que lo descargue para verlo sin conexión. Las notificaciones push también pueden ser silenciosas, no contener ningún mensaje de alerta ni sonido, y utilizarse sólo para actualizar la interfaz de tu aplicación o desencadenar trabajo en segundo plano. 

Las notificaciones push son estupendas para contenidos esporádicos pero de importancia inmediata, en los que la demora entre las búsquedas en segundo plano puede no ser aceptable. Las notificaciones push también pueden ser mucho más eficientes que la obtención en segundo plano, ya que tu aplicación sólo se lanza cuando es necesario. 

Las notificaciones push tienen una tasa limitada, así que no temas enviar tantas como necesite tu aplicación. iOS y los servidores APN controlarán la frecuencia con la que se entregan, y no te meterás en problemas por enviar demasiadas. Si tus notificaciones push están estranguladas, podrían retrasarse hasta la próxima vez que el dispositivo envíe un paquete de mantenimiento de conexión o reciba otra notificación.

## Enviar notificaciones push silenciosas

Para enviar una notificación push silenciosa, establece la bandera `content-available` en `1` en una carga útil de notificación push. Al enviar una notificación push silenciosa, puede que también quieras incluir algunos datos en la carga útil de la notificación, para que tu aplicación pueda hacer referencia al evento. Esto podría ahorrarte unas cuantas peticiones de red y aumentar la capacidad de respuesta de tu aplicación.

{% alert warning %}
No se recomienda adjuntar un título y un cuerpo con `content-available=1` porque puede provocar un comportamiento indefinido. Para asegurarte de que una notificación es realmente silenciosa, excluye tanto el título como el cuerpo cuando configures la flag `content-available` en `1.`. Para más detalles, consulta la [documentación de Apple sobre actualizaciones en segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) oficial.
{% endalert %}

La bandera `content-available` puede establecerse en el panel de Braze, así como dentro de nuestro [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) en la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/).

![El panel de Braze muestra la casilla "contenido disponible" que se encuentra en la pestaña "configuración" del compositor push.]({% image_buster /assets/img_archive/remote_notification.png %} "contenido disponible")

## Utiliza notificaciones push silenciosas para desencadenar el trabajo en segundo plano

Las notificaciones push silenciosas pueden despertar tu aplicación de un estado "Suspendido" o "No en ejecución" para actualizar contenidos o ejecutar determinadas tareas sin notificárselo a tus usuarios. 

Para utilizar notificaciones push silenciosas para desencadenar el trabajo en segundo plano, configura la bandera `content-available` siguiendo las instrucciones anteriores sin mensaje ni sonido. Configura el modo de fondo de tu aplicación para habilitar `remote notifications` en la pestaña **Capacidades** de la configuración de tu proyecto. Una notificación push remota no es más que una notificación push normal con la bandera `content-available` activada. 

![Xcode muestra la casilla de verificación del modo "notificaciones remotas" en "capacidades".]({% image_buster /assets/img_archive/background_mode.png %} "modo en segundo plano habilitado")

Habilitar el modo en segundo plano para las notificaciones remotas es necesario para el [seguimiento de la desinstalación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/).

Incluso con el modo de fondo de notificaciones remotas habilitado, el sistema no lanzará tu aplicación en segundo plano si el usuario ha forzado la salida de la aplicación. El usuario debe iniciar explícitamente la aplicación o reiniciar el dispositivo para que el sistema pueda iniciar automáticamente la aplicación en segundo plano.

Para más información, consulta [empujar actualizaciones en segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) y [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Limitaciones de las notificaciones silenciosas de iOS

El sistema operativo iOS puede incluir notificaciones para algunas características. Ten en cuenta que si experimentas dificultades con estas características, la puerta de notificaciones silenciosas de iOS podría ser la causa.

Braze tiene varias características que dependen de las notificaciones push silenciosas de iOS:

|Característica|Experiencia del usuario|
|---|---|
|Desinstalar seguimiento | El usuario recibe un push silencioso y nocturno de seguimiento de la desinstalación.|
|Geovallas | Sincronización silenciosa de geovallas del servidor al dispositivo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Consulta la documentación de Apple sobre [el método de instancia](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) y [las notificaciones no recibidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) para obtener más detalles.

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23