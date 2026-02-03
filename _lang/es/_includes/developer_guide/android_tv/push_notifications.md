## Acerca de las notificaciones push para Android TV

![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Aunque no es una característica nativa, la integración push de Android TV es posible aprovechando el SDK de Android Braze y Firebase Cloud Messaging para registrar un token de notificaciones push para Android TV. Sin embargo, es necesario crear una interfaz de usuario que muestre la carga útil de la notificación una vez recibida.

## Requisitos previos

Para utilizar esta característica, tendrás que completar lo siguiente:

- [Integrar el SDK para Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurar notificaciones push para el SDK de Android Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Configuración de las notificaciones push

Para configurar las notificaciones push para Android TV:

1. Crea una vista personalizada en tu aplicación para mostrar tus notificaciones.
2. Crea una [fábrica de notificaciones personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display). Esto anulará el comportamiento predeterminado del SDK y te permitirá mostrar manualmente las notificaciones. Una devolución de `null` impedirá que el SDK lo procese y requerirá código personalizado para mostrar la notificación. Una vez completados estos pasos, ¡ya puedes empezar a enviar push a Android TV!<br><br>
3. (Opcional) Para realizar un seguimiento eficaz del análisis de clics, configura el seguimiento del análisis de clics. Esto puede conseguirse creando una [devolución de llamada push]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback) para escuchar las intenciones Braze push abiertas y recibidas.

{% alert note %}
Estas notificaciones **no persistirán** y sólo serán visibles para el usuario cuando el dispositivo las muestre. Esto se debe a que el centro de notificaciones de Android TV no es compatible con las notificaciones históricas.
{% endalert %} 

## Probar las notificaciones push de Android TV

Para probar si tu implementación push tiene éxito, envía una notificación desde el panel de Braze como harías normalmente para un dispositivo Android.

- **Si la aplicación está cerrada**: El mensaje push mostrará una notificación push en la pantalla.
- **Si la aplicación está abierta**: Tienes la oportunidad de mostrar el mensaje en tu propia interfaz de usuario alojada. Te recomendamos que sigas el estilo de la interfaz de usuario de nuestros mensajes dentro de la aplicación Android Mobile SDK.

## Buenas prácticas

Para los especialistas en marketing que utilicen Braze, lanzar una campaña a Android TV será idéntico a lanzar un push a aplicaciones móviles de Android. Para dirigirte exclusivamente a estos dispositivos, te recomendamos que selecciones la aplicación Android TV en la segmentación.

La respuesta entregada y cliqueada devuelta por FCM seguirá la misma convención que un dispositivo móvil Android; por tanto, cualquier error será visible en el registro de actividad del mensaje.
