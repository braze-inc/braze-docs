---
nav_title: "Configuración avanzada de campañas push"
article_title: Configuración avanzada de campañas push
page_order: 5
page_layout: reference
description: "Este artículo de referencia cubre algunas configuraciones de Campañas Push Avanzadas como prioridad, URLs personalizadas, opciones de entrega y más."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Configuración avanzada de la campaña push

> Hay muchos ajustes avanzados disponibles para las notificaciones push de Android y Fire OS enviadas a través del panel Braze. En este artículo se describirán estas características y cómo utilizarlas con éxito.

## ID de notificación {#notification-id}

Un ID de notificación es un identificador único para una categoría de mensajes de su elección que informa al servicio de mensajería para que sólo respete el mensaje más reciente de ese ID. Establecer un ID de notificación te permite enviar sólo el mensaje más reciente y relevante, en lugar de una pila de mensajes desfasados e irrelevantes.

Para asignar un ID de notificación, vaya a la página de composición de la notificación push a la que desea añadir el ID y seleccione la pestaña **Configuración**. Introduzca un número entero en la sección **ID de notificación**. Para actualizar esta notificación después de haberla emitido, envíe otra notificación con el mismo ID que utilizó anteriormente.

![Campo ID de notificación.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Tiempo de vida (TTL) {#ttl}

El campo **Tiempo de vida** te permite establecer un tiempo personalizado para almacenar mensajes con el servicio de mensajería push. Si el dispositivo permanece desconectado más allá del TTL, el mensaje caducará y no se entregará.

Para editar el tiempo de vida de tu push de Android, ve al compositor y selecciona la pestaña **Configuración**. Busca el campo **Tiempo de vida** e introduce un valor en días, horas o segundos.

Los valores predeterminados para el tiempo de vida los define tu administrador en la página [Configuración push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Por defecto, Braze establece el TTL de push en el valor máximo para cada servicio de mensajería push. Aunque la configuración predeterminada de TTL se aplica globalmente, puedes anularla a nivel de mensaje durante la creación de la campaña. Esto es útil cuando diferentes campañas requieren diferentes plazos de urgencia o entrega.

Por ejemplo, supongamos que tu aplicación organiza un concurso semanal de preguntas y respuestas. Envía una notificación push una hora antes de que empiece. Al establecer el TTL en 1 hora, te aseguras de que los usuarios que abran la aplicación después de que comience el concurso no reciban una notificación sobre un evento que ya ha comenzado.

{% details Buenas prácticas %}

#### Cuándo utilizar TTL más corto

Los TTL más cortos garantizan que los usuarios reciban notificaciones puntuales de eventos o promociones que pierden relevancia rápidamente. Por ejemplo:

- **Comercio minorista:** Envío de un push para una venta flash que finaliza en 2 horas (TTL: 1-2 horas)
- **Entrega de comida:** Notificar a los usuarios cuando su pedido está cerca (TTL: 10-15 minutos)
- **Aplicaciones de transporte:** Actualizaciones de llegada de trayectos compartidos (TTL: unos minutos)
- **Recordatorios de eventos:** Notificar a los usuarios el próximo inicio de un seminario web (TTL: menos de 1 hora)

#### Cuándo evitar un TTL más corto

- Si el mensaje de tu campaña sigue siendo relevante durante varios días o semanas, como los recordatorios de renovación de suscripción o las promociones en curso.
- Cuando maximizar el alcance es más importante que la urgencia, como con los anuncios de actualizaciones de la aplicación o las promociones de características.

{% enddetails %}

## Prioridad de entrega de la mensajería Firebase {#fcm-priority}

El campo **Firebase Messaging Delivery Priority** permite controlar si un push se envía con prioridad "normal" o "alta" a Firebase Cloud Messaging. Esta configuración determina la rapidez con la que se entregan los mensajes y cómo afectan a la duración de la batería del dispositivo.

| Prioridad | Descripción | Lo mejor para |
|---------|-------------|----------|
| Normal | Entrega optimizada para la batería que puede retrasarse para conservarla | Contenido no urgente, ofertas promocionales, actualizaciones de noticias |
| Alta | Entrega inmediata con mayor consumo de batería | Notificaciones sensibles al tiempo, alertas críticas, actualizaciones de eventos en vivo, alertas de cuentas, noticias de última hora o recordatorios urgentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Consideraciones

- **Configuración predeterminada**: Puedes establecer una prioridad FCM predeterminada para todas las campañas de Android en tu [Configuración push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Esta configuración a nivel de campaña anulará la predeterminada si es necesario.
- **Despriorización**: Si FCM detecta que tu aplicación envía con frecuencia mensajes de alta prioridad que no dan lugar a notificaciones visibles para el usuario o a la interacción del usuario, esos mensajes pueden ser automáticamente despriorizados a la prioridad normal.
- **Impacto de la batería**: Los mensajes de alta prioridad despiertan más agresivamente a los dispositivos dormidos y consumen más batería. Utiliza esta prioridad con criterio.

Para obtener información más detallada sobre la [gestión](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize) y [despriorización](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize) de mensajes, consulta la [documentación de FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) y [Gestión y despriorización de mensajes en Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texto de resumen

El texto de resumen te permite establecer texto adicional en la vista ampliada de notificaciones. También sirve como pie de foto para las notificaciones con imágenes.

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

El texto del resumen aparecerá debajo del cuerpo del mensaje en la vista ampliada. 

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

En las notificaciones push que incluyen imágenes, el texto del mensaje se mostrará en la vista contraída, mientras que el texto resumido se mostrará como pie de imagen cuando se amplíe la notificación. 

## URI personalizados

La función **URI personalizada** permite especificar una URL Web o un recurso Android al que navegar cuando se hace clic en la notificación. Si no se especifica ningún URI personalizado, al hacer clic en la notificación los usuarios accederán a su aplicación. Puede utilizar el URI personalizado para crear enlaces profundos dentro de su aplicación, así como para dirigir a los usuarios a recursos que también existen fuera de su aplicación. Puedes especificarlo a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en la pestaña **Componer** del compositor push.

![Campo URI personalizado.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridad de visualización de notificaciones

{% alert important %}
El ajuste Prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o posterior. Para los dispositivos más nuevos, establezca la prioridad a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

El nivel de prioridad de una notificación push afecta a cómo se muestra su notificación en la bandeja de notificaciones en relación con otras notificaciones. También puede afectar a la velocidad y la forma de entrega, ya que los mensajes normales y de menor prioridad pueden enviarse con una latencia ligeramente superior o por lotes para preservar la duración de la batería, mientras que los mensajes de alta prioridad siempre se envían inmediatamente.

Esta función es útil para diferenciar los mensajes en función de su importancia o de si son urgentes. Por ejemplo, una notificación sobre las condiciones peligrosas de una carretera sería una buena candidata para recibir una prioridad alta, mientras que una notificación sobre una venta en curso debería recibir una prioridad más baja. Debe considerar si el uso de una prioridad perturbadora es realmente necesario para la notificación que está enviando, ya que ocupar constantemente el primer lugar en la bandeja de entrada de sus usuarios o interrumpir sus otras actividades puede tener un impacto negativo.

En Android O, la prioridad de las notificaciones pasó a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir la prioridad de un canal durante su configuración y luego utilizar el panel de control para seleccionar el canal adecuado al enviar tus sonidos de notificación. En el caso de los dispositivos con versiones de Android anteriores a O, es posible especificar un nivel de prioridad para las notificaciones de Android y Fire OS a través del panel de control y la API de mensajería de Braze.

Para enviar mensajes a toda tu base de usuarios con una prioridad específica, te recomendamos que especifiques indirectamente la prioridad mediante la [configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance) (para dirigirte a dispositivos O+) y envíes la prioridad individual desde el panel (para dirigirte a dispositivos <O).

Consulte en la siguiente tabla los niveles de prioridad que puede establecer en las notificaciones push de Android o Fire OS:

| Prioridad | Descripción| `priority` valor (para mensajes API) |
|------|-----------|----------------------------|
| Máx. | Mensajes urgentes o en los que el tiempo es un factor crítico. | `2` |
| Alta | Comunicación importante, como un nuevo mensaje de un amigo. | `1` |
| Predeterminado | La mayoría de las notificaciones. Utilícelo si su mensaje no entra explícitamente en ninguno de los otros tipos de prioridad. | `0` |
| Baja | Información que desea que los usuarios conozcan pero que no requiere una acción inmediata. | `-1`|
| Mín. | Información contextual o de fondo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más información, consulte la documentación de Google sobre [notificaciones en Android](http://developer.android.com/design/patterns/notifications.html).

## Categoría Push

Las notificaciones push de Android ofrecen la opción de especificar si la notificación pertenece a una categoría predefinida. La interfaz de usuario del sistema Android puede utilizar esta categoría para tomar decisiones de clasificación o filtrado sobre dónde colocar la notificación en la bandeja de notificaciones del usuario.

![Pestaña de configuración con la Categoría establecida en Ninguna, que es la configuración predeterminada.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoría | Descripción |
|---|-------|
| Ninguno | Opción por defecto. |
| Alarma | Alarma o temporizador. |
| Llamada | Llamada entrante (voz o vídeo) o solicitud de comunicación sincrónica similar. |
| Correo electrónico | Mensaje masivo asíncrono (correo electrónico). |
| Error | Error en el funcionamiento en segundo plano o en el estado de autenticación. |
| Evento | Evento del calendario. |
| Mensaje | Mensaje directo entrante (SMS, mensaje instantáneo, etc.). |
| Progreso | Progreso de una operación en segundo plano de larga duración. |
| Promoción | Promoción o publicidad. |
| Recomendación | Una recomendación concreta y puntual para una sola cosa. |
| Recordatorio | Recordatorio programado por el usuario. |
| Servicio | Indicación de servicio en segundo plano en ejecución. |
| Social | Actualización de redes sociales o para compartir. |
| Estado | Información continua sobre el estado del dispositivo o del contexto. |
| Sistema | Actualización del estado del sistema o del dispositivo. Reservado para uso del sistema. |
| Transporte | Control de transporte multimedia para la reproducción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilidad push

Las notificaciones push de Android proporcionan un campo opcional para determinar cómo aparece una notificación en la pantalla de bloqueo del usuario. Consulte la tabla siguiente para ver las opciones de visibilidad y sus descripciones.

| Visibilidad | Descripción |
|---|-----|
| Pública | Aparece una notificación en la pantalla de bloqueo |
| Privada | La notificación se muestra con el mensaje "Contenido oculto |
| Secreta | Las notificaciones no se muestran en la pantalla de bloqueo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Además, los usuarios de Android pueden anular el modo en que las notificaciones push aparecen en su pantalla de bloqueo cambiando la configuración de privacidad de las notificaciones en su dispositivo. Esta configuración anulará la visibilidad de la notificación push.

![Ubicación de la prioridad push del panel de control con la configuración de visibilidad habilitada y establecida en Privado.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independientemente de la visibilidad, todas las notificaciones se mostrarán en la pantalla de bloqueo del usuario si la configuración de privacidad de notificaciones de su dispositivo es **Mostrar todo el contenido** (configuración predeterminada). Del mismo modo, las notificaciones no se mostrarán en la pantalla de bloqueo si la privacidad de las notificaciones está configurada como **No mostrar notificaciones**. La visibilidad sólo tiene efecto si su privacidad de notificación está configurada en **Ocultar contenido sensible**.

La visibilidad no tiene efecto en los dispositivos anteriores a Android Lollipop 5.0.0, lo que significa que todas las notificaciones se mostrarán en estos dispositivos.

Consulta nuestra [documentación sobre Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para obtener más información.

## Sonidos de notificación

En Android O, los sonidos de notificación pasaron a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir el sonido de un canal durante su configuración y luego utilizar el panel de control para seleccionar el canal adecuado al enviar tus notificaciones.

Para los dispositivos que ejecutan versiones de Android anteriores a Android O, Braze permite configurar el sonido de un mensaje push individual a través del compositor del panel. Puedes hacerlo especificando un recurso de sonido local en el dispositivo (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`). 

Si selecciona **Predeterminado** en este campo, se reproducirá el sonido de notificación predeterminado en el dispositivo. Esto se puede especificar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en la **configuración** del compositor push.

![El campo "Sonido".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Introduce el URI completo del recurso de sonido (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`) en la consulta del panel.

Para enviar un mensaje a toda tu base de usuarios con un sonido específico, te recomendamos que especifiques indirectamente el sonido a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels) (para dirigirte a dispositivos O+) y envíes el sonido individual desde el panel (para dirigirte a dispositivos <O).

