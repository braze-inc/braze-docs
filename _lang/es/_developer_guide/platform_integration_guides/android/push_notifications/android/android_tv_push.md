---
nav_title: Android TV Push
article_title: Android TV Push
platform: Android
page_order: 8
description: "En este artículo se muestra cómo implementar y probar Android TV Push."
channel:
  - push

---

# Android TV Push
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> Aunque no es una característica nativa, la integración push de Android TV es posible aprovechando el SDK de Android Braze y Firebase Cloud Messaging para registrar un token de notificaciones push para Android TV. Sin embargo, es necesario crear una interfaz de usuario que muestre la carga útil de la notificación una vez recibida.

## Aplicación

1. **Integrar el SDK para Android de Braze**<br>
En primer lugar, debes integrar el [SDK para Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) (si aún no lo has completado).<br><br>
2. **Integrar notificaciones push**<br>
A continuación, debes integrar [las notificaciones push de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) (si aún no lo has hecho).<br><br>
3. **Crear una vista personalizada del mensaje toast**<br>
A continuación, crea una vista personalizada en tu aplicación para mostrar tus notificaciones.<br><br>
4. **Crear una fábrica de notificaciones personalizada**<br>
Por último, debes crear una [fábrica de notificaciones personalizada]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications). Esto anulará el comportamiento predeterminado del SDK y te permitirá mostrar manualmente las notificaciones. Una devolución de `null` impedirá que el SDK lo procese y requerirá código personalizado para mostrar la notificación. Una vez completados estos pasos, ¡ya puedes empezar a enviar push a Android TV!<br><br>
5. **Configurar el seguimiento del análisis de clics (opcional)**<br>
Para realizar un seguimiento eficaz de los análisis de clics, es necesario gestionarlo manualmente, ya que Braze no gestiona la visualización de los mensajes automáticamente. Esto puede conseguirse creando una [devolución de llamada push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) para escuchar las intenciones Braze push abiertas y recibidas.

{% alert note %}
Ten en cuenta que estas notificaciones **no persistirán** y sólo serán visibles para el usuario cuando el dispositivo las muestre. Esto se debe a que el centro de notificaciones de Android TV no es compatible con las notificaciones históricas.
{% endalert %} 

## Cómo probar push en Android TV

Para probar si tu implementación push tiene éxito, envía una notificación desde el panel de Braze como harías normalmente para un dispositivo Android.

- **Si la aplicación está cerrada**: El mensaje push mostrará una notificación push en la pantalla.
- **Si la aplicación está abierta**: Tienes la oportunidad de mostrar el mensaje en tu propia interfaz de usuario alojada. Te recomendamos que sigas el estilo de la interfaz de usuario de nuestros mensajes dentro de la aplicación Android Mobile SDK.

## Información adicional
Para un usuario final de marketing en Braze, lanzar una campaña a Android TV será idéntico a lanzar un push a aplicaciones móviles de Android. Para dirigirte exclusivamente a estos dispositivos, te recomendamos que selecciones la aplicación Android TV en la segmentación. 

La respuesta entregada y cliqueada devuelta por FCM seguirá la misma convención que un dispositivo móvil Android; por tanto, cualquier error será visible en el registro de actividad del mensaje.

