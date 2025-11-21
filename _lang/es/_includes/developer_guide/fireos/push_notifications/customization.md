{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configuración

Hay muchas configuraciones avanzadas disponibles para las notificaciones push de FireOS enviadas a través del panel Braze. En este artículo se describirán estas características y cómo utilizarlas con éxito.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Tiempo de vida (TTL) {#ttl}

El campo **Tiempo de vida** (TTL) te permite establecer un tiempo personalizado para almacenar mensajes con el servicio de mensajería push. Los valores predeterminados para el tiempo de vida son cuatro semanas para FCM y 31 días para ADM.

### Texto resumido {#summary-text}

El texto de resumen te permite establecer texto adicional en la vista ampliada de notificaciones. También sirve como pie de foto para las notificaciones con imágenes.

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

El texto resumido se mostrará bajo el cuerpo del mensaje en la vista ampliada. 

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para las notificaciones push que incluyan imágenes, el texto del mensaje se mostrará en la vista contraída, mientras que el texto del resumen se mostrará como pie de imagen cuando se expanda la notificación. 

### URIs personalizadas {#custom-uri}

La característica **URI personalizada** te permite especificar una URL Web o un recurso Android al que navegar cuando se haga clic en la notificación. Si no se especifica una URI personalizada, al hacer clic en la notificación los usuarios acceden a tu aplicación. Puedes utilizar el URI personalizado para establecer vínculos profundos dentro de tu aplicación y dirigir a los usuarios a recursos que existen fuera de ella. Esto puede especificarse a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging) o de nuestro panel en **Configuración avanzada** en el compositor push, como se muestra en la imagen:

![La configuración avanzada de vinculación en profundidad en el compositor push de Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Prioridad de visualización de notificaciones

{% alert important %}
El ajuste Prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o posterior. Para los dispositivos más nuevos, establezca la prioridad a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

El nivel de prioridad de una notificación push afecta a cómo se muestra su notificación en la bandeja de notificaciones en relación con otras notificaciones. También puede afectar a la velocidad y la forma de entrega, ya que los mensajes normales y de menor prioridad pueden enviarse con una latencia ligeramente superior o por lotes para preservar la duración de la batería, mientras que los mensajes de alta prioridad siempre se envían inmediatamente.

En Android O, la prioridad de notificación pasó a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir la prioridad de un canal durante su configuración y luego utilizar el panel de control para seleccionar el canal adecuado al enviar tus sonidos de notificación. Para los dispositivos que ejecutan versiones de Android anteriores a O, es posible especificar un nivel de prioridad para las notificaciones de FireOS a través del panel de Braze y la API de mensajería. 

Para enviar mensajes a toda tu base de usuarios con una prioridad específica, te recomendamos que especifiques indirectamente la prioridad mediante la [configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance) (para dirigirte a dispositivos O+) *y* envíes la prioridad individual desde el panel (para dirigirte a dispositivos <O).

Los niveles de prioridad que puedes establecer en las notificaciones push de Fire OS son:

| Prioridad | Descripción/uso previsto | `priority` valor (para mensajes API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensajes urgentes o en los que el tiempo es un factor crítico | `2` |
| Alta     | Comunicación importante, como un nuevo mensaje de un amigo | `1` |
| Predeterminado  | La mayoría de las notificaciones: utilízalo si tu mensaje no entra explícitamente en ninguno de los otros tipos de prioridad. | `0` |
| Baja      | Información que quieres que conozcan los usuarios pero que no requiere una acción inmediata | `-1` |
| Mín.      | Información contextual o de fondo. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más información, consulta la documentación de [notificaciones de Android](http://developer.android.com/design/patterns/notifications.html) de Google.

### Sonidos {#sounds}

En Android O, los sonidos de notificación pasaron a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir el sonido de un canal durante su configuración y luego utilizar el panel para seleccionar el canal adecuado al enviar tus notificaciones.

Para los dispositivos que ejecutan versiones de Android anteriores a O, Braze te permite configurar el sonido de un mensaje push individual a través del compositor del panel. Puedes hacerlo especificando un recurso de sonido local en el dispositivo (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Si especificas "predeterminado" en este campo, se reproducirá el sonido de notificación predeterminado en el dispositivo. Esto puede especificarse a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging) o del panel en **Configuración** en el compositor push.

![La configuración avanzada del sonido en el compositor push de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Introduce el URI completo del recurso de sonido (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`) en la consulta del panel.

Para enviar un mensaje a toda tu base de usuarios con un sonido específico, te recomendamos que especifiques indirectamente el sonido a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels) (para dirigirte a dispositivos O+) *y* envíes el sonido individual desde el panel (para dirigirte a dispositivos <O).
