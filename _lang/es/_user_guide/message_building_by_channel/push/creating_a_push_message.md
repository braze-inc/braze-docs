---
nav_title: "Crear un mensaje push"
article_title: Crear una campaña push
page_order: 4
page_type: tutorial
description: "Esta página del tutorial cubre los diferentes componentes que intervienen en la creación de un mensaje push, incluyendo la configuración, el envío, la orientación y mucho más."
channel: push
tool:
  - Campaigns
  
---

# Crear un mensaje push

> Las notificaciones push son estupendas para las llamadas a la acción sensibles al tiempo, así como para reactivar la interacción de los usuarios que no han entrado en la aplicación desde hace tiempo. Las campañas push exitosas llevan al usuario directamente al contenido y demuestran el valor de tu aplicación. Para ver ejemplos de notificaciones push, consulta nuestros [casos de estudio](https://www.braze.com/customers).

## Paso 1: Elige dónde construir tu mensaje {#create-new-campaign-push}

{% alert tip %}
¿No estás seguro de si utilizar una campaña o un Canvas? Las campañas son mejores para campañas de mensajería sencillas y únicas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campañas** y, a continuación, selecciona **Crear campaña**.
2. Para campañas dirigidas a varios canales, selecciona **Multicanal**. Si no, selecciona **Notificación push**. Si aún no estás seguro, consulta **Decidir entre una campaña push normal o multicanal** más abajo.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario. 

{% alert tip %}
Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
{% endalert %}

{: start="5"}
5\. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Deciding between regular or multichannel push campaign %}

Si pretendes dirigirte a varios dispositivos y plataformas, como cualquier combinación de móvil, Web, Kindle, iOS y Android, tu selección en este paso puede afectar a la disponibilidad de algunas características y configuraciones más adelante.

Consulta el siguiente cuadro de decisiones antes de crear una campaña multicanal o de notificaciones push:

\!["Diagrama de flujo para seleccionar el tipo de campaña. Empieza por decidir si te diriges a varios dispositivos y plataformas. Si no, te lleva a "Seleccionar notificación push". En caso afirmativo, pregunta "¿Qué tipo de mensaje push?" y las opciones son "Push estándar", lo que lleva a un punto de decisión "¿Necesitas utilizar una configuración específica del dispositivo?". Si no, te lleva a 'Seleccionar notificación push y utilizar push rápido'. Si la respuesta es sí, pasa a "Seleccionar Multicanal". De vuelta a "¿Qué tipo de mensaje push?", si la respuesta es "Historias push o imagen en línea", te dirige a "Seleccionar multicanal".]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si seleccionas **Notificación push** y eliges dirigirte a varios dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Con el push rápido, algunas configuraciones específicas del dispositivo no están disponibles:

- Botones de acción push
- Canales y grupos de notificación
- Tiempo de vida push (TTL)
- Mostrar prioridad
- Suena

Antes de continuar, consulta [Campañas push rápidas]({{site.baseurl}}/quick_push) para entender qué es diferente en esta experiencia de edición.

{% enddetails %}

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Elige un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Selecciona plataformas push

A continuación, elige qué combinación de plataforma y dispositivo móvil debe recibir el push. Utiliza esta selección para limitar la entrega de una notificación push a un conjunto específico de aplicaciones.

Hay varias formas de hacerlo, dependiendo de tus selecciones anteriores:

| Selección previa | Opciones |
| --- | --- | 
| Campaña de notificación push | Selecciona una o varias plataformas y dispositivos. Si eliges dirigirte a varios dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Esto proporciona una experiencia de mensajería optimizada para elaborar un mensaje para todas las plataformas seleccionadas en un único editor. Consulta [Campañas push rápidas]({{site.baseurl}}/quick_push) para entender qué hay de diferente en esta experiencia de edición. |
| Campaña multicanal | Selecciona **Añadir canal de mensajería** para añadir plataformas push adicionales. Como las selecciones de plataforma son específicas de cada variante, puedes probar la interacción de los mensajes por plataforma.
| Canvas | En el paso Mensajes, selecciona **\+ Añadir más** para añadir plataformas push adicionales. Al igual que en las campañas multicanal, la selección de plataformas es específica para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Selecciona el tipo de notificación (iOS y Android)

Si estás creando una campaña push rápida, el tipo de notificación se establece automáticamente en **Push estándar** y no se puede cambiar.

\![Tipo de notificación con Push estándar seleccionado como ejemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

De lo contrario, para iOS y Android, selecciona tu tipo de notificación:

- Push estándar
- [Historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Imagen en línea (sólo Android)

Si quieres incluir imágenes en tu campaña push, consulta las siguientes guías sobre cómo crear una notificación enriquecida para [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) o [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Paso 4: Redacta tu mensaje push

¡Ahora es el momento de escribir tu mensaje push! La pestaña **Redactar** te permite editar todos los aspectos del contenido y comportamiento de tu mensaje.

\![Pestaña de composición de la creación de una notificación push.]({% image_buster /assets/img_archive/push_compose.png %})

El contenido de la pestaña **Redactar** varía en función del tipo de notificación que hayas elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

#### Canal o grupo de notificaciones (iOS y Android)

Para más información sobre las opciones de notificación específicas de cada plataforma, consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) u [Opciones de notificación de Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Lengua

Añade copia en varios idiomas utilizando el botón **Añadir idiomas**. Te recomendamos que selecciones tus idiomas antes de escribir el contenido, para que puedas rellenar el texto donde corresponda en el Liquid. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si añades texto en un idioma escrito de derecha a izquierda, ten en cuenta que el aspecto final de los mensajes escritos de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título y cuerpo

{% tabs local %}
{% tab ios %}
Empieza a escribir en el cuadro de mensaje y observa cómo aparece una vista previa en el cuadro de vista previa de la izquierda. Los mensajes push deben estar formateados en texto plano. 

Añade un titular utilizando el campo **Título**. Para que tu push sea personalizado y dirigido, puedes incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Empieza a escribir en el cuadro de mensaje y observa cómo aparece una vista previa en el cuadro de vista previa de la izquierda. Los mensajes push deben estar formateados en texto plano. 

Para que tu push sea personalizado y dirigido, puedes incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
**No puedes** enviar un mensaje push de Android sin un título; sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que si tu mensaje sólo contiene un espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
¿Necesitas ayuda para crear un texto impresionante? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

\![Lanzar el botón AI Copywriter, situado en el campo Cuerpo del compositor push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Imagen

Cuando sea compatible, el icono de tu aplicación se añadirá automáticamente como imagen de tu notificación push. También tienes la opción de enviar notificaciones enriquecidas, que permiten una mayor personalización en tus notificaciones push añadiendo contenido adicional más allá de la copia.

Para obtener más información sobre el uso de imágenes en tus notificaciones push, consulta los siguientes artículos:

- [Crear notificaciones enriquecidas para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Crear notificaciones enriquecidas para Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportamiento al hacer clic

Especifica qué ocurre cuando un usuario selecciona el cuerpo de una notificación push con **Comportamiento al hacer clic**. Por ejemplo, puedes pedir a los clientes que abran tu aplicación, redirigirlos a una URL Web específica o incluso abrir una página concreta de tu aplicación con un [vínculo profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Aquí también puedes configurar avisos de botón dentro de tu notificación push, como por ejemplo:

- Aceptar/Rechazar
- Sí/No
- Confirmar/Cancelar
- Más 

#### Opciones de envío

Si un usuario tiene tu aplicación instalada en varios dispositivos, por defecto, tu mensaje push se envía a todos los dispositivos que tengan asignado un token de notificaciones push válido. Si lo deseas, puedes seleccionar **el dispositivo utilizado más recientemente**.

Casilla de verificación de opciones de dispositivo para enviar este push sólo al dispositivo utilizado más recientemente por el usuario.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Esta configuración tiene algunos matices. Si se selecciona esta opción, Braze limitará los envíos múltiples, excepto cuando una campaña se dirija a varias plataformas, como iOS y Android. Si el usuario tiene tu aplicación tanto en un dispositivo iOS como Android, recibirá un push para ambas plataformas. Si el dispositivo utilizado más recientemente por un usuario no está [habilitado para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), el mensaje no se enviará.

Para iOS, puedes limitar aún más la mensajería enviando notificaciones push sólo a dispositivos iPad, o sólo a dispositivos iPhone y iPod.

## Paso 5: Vista previa y prueba de tu mensaje (opcional)

Podría decirse que las pruebas son uno de los pasos más críticos. Cuando termines de componer tu mensaje push perfecto, pruébalo antes de enviarlo. Selecciona la pestaña **Prueba** para elegir entre las opciones sobre cómo probar tu mensaje push. En **Destinatarios de prueba**, puedes seleccionar un grupo de prueba de contenido o usuarios individuales. También puedes utilizar **Vista previa del mensaje como usuario** para hacerte una idea de cómo puede verse tu mensaje en el móvil para un usuario aleatorio, un usuario existente, un usuario personalizado o un usuario multilingüe.

## Paso 6: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña; consulta las secciones siguientes para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para construir notificaciones push.

#### Elige el calendario o desencadenar la entrega

Los mensajes push pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las horas tranquilas.

En este paso también puedes especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una vista previa de cómo es la población aproximada de ese segmento en este momento. Las estadísticas detalladas de audiencia de los canales a los que se dirige tu campaña están disponibles en el pie de página. Para ver a qué porcentaje de tu base de usuarios se dirige y el valor de duración del ciclo de vida de este segmento, selecciona **Mostrar estadísticas adicionales**.

{% multi_lang_include target_audiences.md %}

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

Cuando veas el Total de usuarios alcanzables de tu audiencia filtrada, puede que observes que la suma de las columnas individuales es menor que el Total de usuarios alcanzables. Este vacío suele deberse a que hay una serie de usuarios que cumplen los requisitos para el segmento o los filtros de la campaña, pero a los que no se puede llegar mediante push (por ejemplo, porque no tienen [tokens de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) válidos o activos).

{% enddetails %}

\![Tabla de estadísticas detalladas de audiencia de Usuarios alcanzables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

También puedes elegir enviar tu campaña sólo a usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como los que estén suscritos y hayan optado por el push.

Opcionalmente, también puedes limitar la entrega a un número determinado de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces al repetirse la campaña.

##### Campañas multicanal con correo electrónico y push

Para las campañas multicanal dirigidas tanto al correo electrónico como a los canales push, puede que quieras limitar tu campaña para que sólo reciban el mensaje los usuarios que hayan optado explícitamente por ello (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

- **El usuario A** está suscrito al correo electrónico y está habilitado para push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibe el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, en **Resumen de audiencia**, selecciona enviar esta campaña a "sólo usuarios con adhesión voluntaria". Esta opción garantizará que sólo los usuarios con adhesión voluntaria reciban tu correo electrónico, y Braze sólo enviará tu push a los usuarios que estén habilitados para push de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencias objetivo** que limite la audiencia a un único canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

## Paso 7: Revisar y desplegar {#review-and-deploy-push}

Cuando hayas terminado de construir lo último de tu campaña o Canvas, revisa sus detalles. Para las campañas, la página final te ofrecerá un resumen de la campaña que acabas de diseñar. Confirma todos los detalles relevantes, asegúrate de que has probado tu mensaje, luego envíalo y ¡mira cómo llegan los datos!

A continuación, consulta [Informes push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber cómo puedes acceder a los resultados de tu campaña push. Para las notificaciones push, podrás ver las estadísticas del número de mensajes enviados, entregados, rebotados, abiertos y abiertos directamente.

