---
nav_title: "Configuración avanzada de la campaña push"
article_title: Configuración avanzada de la campaña push
page_order: 5
page_layout: reference
description: "Este artículo de referencia cubre algunas configuraciones avanzadas de las campañas push, como la prioridad, las URL personalizadas, las opciones de entrega y mucho más."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Configuración avanzada de la campaña push

> Hay muchas configuraciones avanzadas disponibles para las notificaciones push de Android y Fire OS enviadas a través del panel Braze. Este artículo describirá estas características y cómo utilizarlas con éxito.

## ID de notificación {#notification-id}

Un ID de notificación es un identificador único para una categoría de mensajes de tu elección que informa al servicio de mensajería para que sólo respete el mensaje más reciente de ese ID. Establecer un ID de notificación te permite enviar sólo el mensaje más reciente y relevante, en lugar de una pila de mensajes desfasados e irrelevantes.

Para asignar un ID de notificación, ve a la página de composición del push al que quieras añadir el ID y selecciona la pestaña **Configuración**. Introduce un número entero en la sección **ID de notificación**. Para actualizar esta notificación después de haberla emitido, envía otra notificación con el mismo ID que utilizaste anteriormente.

\![Campo ID de notificación.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Tiempo de vida (TTL) {#ttl}

El campo **Tiempo de vida** te permite establecer un tiempo personalizado para almacenar mensajes con el servicio de mensajería push. Si el dispositivo permanece desconectado más allá del TTL, el mensaje caducará y no se entregará.

Para editar el tiempo de vida de tu push de Android, ve al compositor y selecciona la pestaña **Configuración**. Busca el campo **Tiempo de vida** e introduce un valor en días, horas o segundos.

Los valores predeterminados para el tiempo de vida los define tu administrador en la página [Configuración push]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). Por defecto, Braze establece el TTL de push en el valor máximo para cada servicio de mensajería push. Aunque la configuración predeterminada de TTL se aplica globalmente, puedes anularla a nivel de mensaje durante la creación de la campaña. Esto es útil cuando diferentes campañas requieren diferentes plazos de urgencia o entrega.

Por ejemplo, supongamos que tu aplicación organiza un concurso semanal de preguntas y respuestas. Envía una notificación push una hora antes de que empiece. Al establecer el TTL en 1 hora, te aseguras de que los usuarios que abran la aplicación después de que comience el concurso no reciban una notificación sobre un evento que ya ha comenzado.

{% details Best practices %}

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

El campo **Prioridad de entrega de la mensajería** de Firebase te permite controlar si un push se envía con prioridad "normal" o "alta" a la mensajería en la nube de Firebase. Esta configuración determina la rapidez con la que se entregan los mensajes y cómo afectan a la duración de la batería del dispositivo.

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

## Texto resumido

El texto de resumen te permite establecer texto adicional en la vista ampliada de notificaciones. También sirve como pie de foto para las notificaciones con imágenes.

\![Un mensaje Android con el título "Este es el título de la notificación" y el texto de resumen "Este es el texto de resumen de la notificación".]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

El texto resumido se mostrará bajo el cuerpo del mensaje en la vista ampliada. 

\![Un mensaje Android con el título "Este es el título de la notificación" y el texto de resumen "Este es el texto de resumen de la notificación".]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para las notificaciones push que incluyan imágenes, el texto del mensaje se mostrará en la vista contraída, mientras que el texto del resumen se mostrará como pie de imagen cuando se expanda la notificación. 

## URIs personalizadas

La característica **URI personalizada** te permite especificar una URL Web o un recurso Android al que navegar cuando se haga clic en la notificación. Si no se especifica una URI personalizada, al hacer clic en la notificación los usuarios acceden a tu aplicación. Puedes utilizar el URI personalizado para establecer vínculos profundos dentro de tu aplicación, así como para dirigir a los usuarios a recursos que también existen fuera de tu aplicación. Puedes especificarlo a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en la pestaña **Componer** del compositor push.

\![Campo URI personalizado.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridad de visualización de notificaciones

{% alert important %}
La configuración de Prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o posterior. Para los dispositivos más nuevos, establece la prioridad mediante [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

El nivel de prioridad de una notificación push afecta a cómo se muestra su notificación en la bandeja de notificaciones en relación con otras notificaciones. También puede afectar a la velocidad y forma de entrega, ya que los mensajes normales y de menor prioridad pueden enviarse con una latencia ligeramente superior o por lotes para preservar la duración de la batería, mientras que los mensajes de alta prioridad siempre se envían inmediatamente.

Esta característica es útil para diferenciar tus mensajes en función de lo críticos o urgentes que sean. Por ejemplo, una notificación sobre el estado peligroso de una carretera sería una buena candidata para recibir una prioridad alta, mientras que una notificación sobre una venta en curso debería recibir una prioridad más baja. Debes considerar si el uso de una prioridad perturbadora es realmente necesario para la notificación que estás enviando, ya que ocupar constantemente el primer lugar en el buzón de entrada de tus usuarios o interrumpir sus otras actividades puede tener un impacto negativo.

En Android O, la prioridad de notificación pasó a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir la prioridad de un canal durante su configuración y luego utilizar el panel para seleccionar el canal adecuado cuando envíes tus sonidos de notificación. Para los dispositivos que ejecutan versiones de Android anteriores a O, es posible especificar un nivel de prioridad para las notificaciones de Android y Fire OS mediante el panel de Braze y la API de mensajería.

Para enviar mensajes a toda tu base de usuarios con una prioridad específica, te recomendamos que especifiques indirectamente la prioridad a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance) (para dirigirte a dispositivos O+) y envíes la prioridad individual desde el panel (para dirigirte a dispositivos <O).

Consulta la siguiente tabla para conocer los niveles de prioridad que puedes establecer en las notificaciones push de Android o Fire OS:

| Prioridad | Descripción| `priority` valor (para mensajes API) |
|------|-----------|----------------------------|
| Max | Mensajes urgentes o en los que el tiempo es un factor crítico. | `2` |
| Alta | Comunicación importante, como un nuevo mensaje de un amigo. | `1` |
| Predeterminado | La mayoría de las notificaciones. Utilízalo si tu mensaje no entra explícitamente en ninguno de los otros tipos de prioridad. | `0` |
| Baja | Información que quieres que conozcan los usuarios pero que no requiere una acción inmediata. | `-1`|
| Min | Información contextual o de fondo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más información, consulta la documentación de Google sobre [las notificaciones de Android](http://developer.android.com/design/patterns/notifications.html).

## Categoría push

Las notificaciones push de Android ofrecen la opción de especificar si tu notificación pertenece a una categoría predefinida. La interfaz de usuario del sistema Android puede utilizar esta categoría para tomar decisiones de clasificación o filtrado sobre dónde colocar la notificación en la bandeja de notificaciones del usuario.

\![Pestaña Configuración con la Categoría establecida en Ninguna, que es la configuración predeterminada.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoría | Descripción |
|---|-------|
| Ninguno | Opción predeterminada. |
| Alarma | Alarma o temporizador. |
| Llama a | Llamada entrante (voz o video) o solicitud de comunicación sincrónica similar. |
| Correo electrónico | Mensaje masivo asíncrono (correo electrónico). |
| Error | Error en el funcionamiento en segundo plano o en el estado de autenticación. |
| Evento | Evento del calendario. |
| Mensaje | Mensaje directo entrante (SMS, mensaje instantáneo, etc.). |
| Progreso | Progreso de una operación en segundo plano de larga duración. |
| Promoción | Promoción o publicidad. |
| Recomendación | Una recomendación concreta y puntual para una sola cosa. |
| Recordatorio | Recordatorio programado por el usuario. |
| Servicio | Indicación de servicio en segundo plano en ejecución. |
| Social | Red social o actualización de compartir. |
| Estado | Información continua sobre el estado del dispositivo o contextual. |
| Sistema | Actualización del estado del sistema o del dispositivo. Reservado para uso del sistema. |
| Transporte | Control de transporte multimedia para la reproducción. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visibilidad push

Las notificaciones push de Android proporcionan un campo opcional para determinar cómo aparece una notificación en la pantalla de bloqueo del usuario. Consulta la tabla siguiente para ver las opciones de visibilidad y sus descripciones.

| Visibilidad | Descripción |
|---|-----|
| Público | Aparece una notificación en la pantalla de bloqueo |
| Privado | La notificación se muestra con "Contenido oculto" como mensaje |
| Secreto | La notificación no se muestra en la pantalla de bloqueo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Además, los usuarios de Android pueden anular cómo aparecen las notificaciones push en su pantalla de bloqueo cambiando la configuración de privacidad de las notificaciones en su dispositivo. Esta configuración anulará la visibilidad de la notificación push.

\![Ubicación de prioridad push del panel de control con Establecer visibilidad habilitado y configurado como Privado.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independientemente de la visibilidad, todas las notificaciones se mostrarán en la pantalla de bloqueo del usuario si la configuración de privacidad de las notificaciones de su dispositivo es **Mostrar todo el contenido** (configuración predeterminada). Asimismo, las notificaciones no se mostrarán en su pantalla de bloqueo si su privacidad de notificaciones está configurada como **No mostrar notificaciones**. La visibilidad sólo tiene efecto si su privacidad de notificación está configurada como **Ocultar contenido sensible**.

La visibilidad no tiene efecto en dispositivos anteriores a Android Lollipop 5.0.0, lo que significa que todas las notificaciones se mostrarán en estos dispositivos.

Consulta nuestra [documentación sobre Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para obtener más información.

## Sonidos de notificación

En Android O, los sonidos de notificación pasaron a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir el sonido de un canal durante su configuración y luego utilizar el panel para seleccionar el canal adecuado al enviar tus notificaciones.

Para los dispositivos que ejecutan versiones de Android anteriores a Android O, Braze te permite configurar el sonido de un mensaje push individual a través del compositor del panel. Puedes hacerlo especificando un recurso de sonido local en el dispositivo (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`). 

Si seleccionas **Predeterminado** en este campo, se reproducirá el sonido de notificación predeterminado en el dispositivo. Esto se puede especificar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en la **configuración** del compositor push.

El campo "Sonido".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

A continuación, introduce el URI completo del recurso de sonido (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`) en la consulta del panel.

Para enviar un mensaje a toda tu base de usuarios con un sonido específico, te recomendamos que especifiques indirectamente el sonido a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels) (para dirigirte a dispositivos O+) y envíes el sonido individual desde el panel (para dirigirte a dispositivos <O).

