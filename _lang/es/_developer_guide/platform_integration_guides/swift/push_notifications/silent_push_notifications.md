---
nav_title: Notificaciones push silenciosas
article_title: Notificaciones push silenciosas para iOS
platform: Swift
page_order: 4
description: "Este artículo explica cómo implementar notificaciones push silenciosas de iOS para el SDK de Swift."
channel:
  - push

---

# Notificaciones push silenciosas para iOS

> Las notificaciones push te permiten enviar notificaciones desde tu aplicación cuando se producen eventos importantes. 

Puedes enviar una notificación push cuando tengas una alerta importante para un usuario. Las notificaciones push también pueden ser silenciosas, no contener ningún mensaje de alerta ni sonido, y utilizarse sólo para actualizar la interfaz de tu aplicación o desencadenar trabajo en segundo plano. Las notificaciones push silenciosas pueden despertar tu aplicación de un estado "Suspendido" o "No en ejecución" para actualizar contenidos o ejecutar determinadas tareas sin notificárselo a tus usuarios.

Braze tiene varias características que se basan en notificaciones push silenciosas:

|Característica|Experiencia del usuario|
|---|---|
|[Desinstalar seguimiento]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | El usuario recibe un push silencioso y nocturno de seguimiento de la desinstalación.|
|[Geovallas]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | Sincronización silenciosa de geovallas del servidor al dispositivo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de notificaciones push silenciosas

Para utilizar las notificaciones push silenciosas para desencadenar el trabajo en segundo plano, debes configurar tu aplicación para que reciba notificaciones incluso cuando esté en segundo plano. Para ello, añade la capacidad Modos de fondo utilizando el panel **Firma y capacidades** al objetivo principal de la aplicación en Xcode. Selecciona la casilla **Notificaciones remotas**.

![Xcode muestra la casilla de verificación del modo "notificaciones remotas" en "capacidades".]({% image_buster /assets/img_archive/background_mode.png %} "modo en segundo plano habilitado")

Incluso con el modo de fondo de notificaciones remotas habilitado, el sistema no lanzará tu aplicación en segundo plano si el usuario ha forzado la salida de la aplicación. El usuario debe iniciar explícitamente la aplicación o reiniciar el dispositivo para que el sistema pueda iniciar automáticamente la aplicación en segundo plano.

Para más información, consulta la sección ["push background updates"](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) y la [documentación](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) de `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Enviar notificaciones push silenciosas

Para enviar una notificación push silenciosa, establece la bandera `content-available` en `1` en una carga útil de notificación push. 

{% alert note %}
Lo que Apple llama notificación remota no es más que una notificación push normal con la bandera `content-available` activada.
{% endalert %}

La bandera `content-available` puede establecerse en el panel de Braze, así como dentro de nuestro [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) en la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
No se recomienda adjuntar un título y un cuerpo con `content-available=1` porque puede provocar un comportamiento indefinido. Para asegurarte de que una notificación es realmente silenciosa, excluye tanto el título como el cuerpo cuando configures la flag `content-available` en `1.`. Para más detalles, consulta la [documentación de Apple sobre actualizaciones en segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) oficial.
{% endalert %}

![El panel de Braze muestra la casilla "contenido disponible" que se encuentra en la pestaña "configuración" del compositor push.]({% image_buster /assets/img_archive/remote_notification.png %} "contenido disponible")

Al enviar una notificación push silenciosa, puede que también quieras incluir algunos datos en la carga útil de la notificación, para que tu aplicación pueda hacer referencia al evento. Esto podría ahorrarte unas cuantas peticiones de red y aumentar la capacidad de respuesta de tu aplicación.

## Limitaciones de las notificaciones silenciosas de iOS

El sistema operativo iOS puede incluir notificaciones para algunas características. Ten en cuenta que si experimentas dificultades con estas características, la puerta de notificaciones silenciosas de iOS podría ser la causa.

Consulta la documentación de Apple sobre [el método de instancia](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) y [las notificaciones no recibidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) para obtener más detalles.

