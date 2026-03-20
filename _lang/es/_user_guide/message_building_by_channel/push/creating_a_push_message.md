---
nav_title: Crear un mensaje push
article_title: Crear una campaña push
page_order: 4
page_type: tutorial
description: "Esta página tutorial cubre los diferentes componentes involucrados en la creación de un mensaje push, incluyendo la configuración, el envío, la segmentación y más."
channel: push
tool:
  - Campaigns
  
---

# Crear un mensaje push

> Las notificaciones push son magníficas para las llamadas a la acción urgentes, así como para volver a atraer a los usuarios que hace tiempo que no entran en la aplicación. Las campañas push exitosas llevan al usuario directamente al contenido y demuestran el valor de tu aplicación. Para ver ejemplos de notificaciones push, consulta nuestros [casos de estudio](https://www.braze.com/customers).

## Paso 1: Elige dónde construir tu mensaje {#create-new-campaign-push}

{% alert tip %}
¿No tienes claro si usar una campaña o un Canvas? Las campañas son más adecuadas para campañas de mensajería única y específica, mientras que los Canvas son más adecuados para recorridos de usuarios de varios pasos.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Para campañas dirigidas a varios canales, selecciona **Multicanal**. De lo contrario, selecciona **Notificación push**. Si aún no estás seguro, consulta **Decidir entre una campaña push normal o multicanal** más abajo.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario. 

{% alert tip %} 
Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por etiquetas concretas.
{% endalert %}

{: start="5"}
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Decidir entre una campaña push normal o multicanal %}

Si tienes intención de dirigirte a varios dispositivos y plataformas, como cualquier combinación de móvil, web, Kindle, iOS y Android, tu selección en este paso puede afectar a la disponibilidad de algunas características y configuraciones más adelante.

Consulta el siguiente diagrama de decisión antes de crear una campaña multicanal o de notificaciones push:

!["Diagrama de flujo para seleccionar el tipo de campaña. Empieza por decidir si te diriges a varios dispositivos y plataformas. Si no, te lleva a 'Seleccionar notificación push'. En caso afirmativo, pregunta '¿Qué tipo de mensaje push?' y las opciones son 'Push estándar', lo que lleva a un punto de decisión '¿Necesitas utilizar una configuración específica del dispositivo?'. Si no, te lleva a 'Seleccionar notificación push y utilizar push rápido'. Si la respuesta es sí, pasa a 'Seleccionar multicanal'. Volviendo a '¿Qué tipo de mensaje push?', si la respuesta es 'Push Stories o imagen en línea', se redirige a 'Seleccionar multicanal'."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si seleccionas **Notificación push** y eliges dirigirte a múltiples dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Con el push rápido, algunas configuraciones específicas del dispositivo no están disponibles:

- Botones de acción para notificación push
- Canales y grupos de notificación
- Tiempo de vida push (TTL)
- Prioridad de visualización
- Sonidos

Antes de continuar, consulta [Campañas de push rápidas]({{site.baseurl}}/quick_push) para comprender en qué se diferencia esta experiencia de edición.

{% enddetails %}

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Una vez que hayas configurado tu Canvas, añade un paso en el constructor de Canvas. Ponle a tu paso un nombre claro y significativo.
3. Elige una [planificación de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que desees asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Seleccionar plataformas push

A continuación, elige qué combinación de plataforma y dispositivo móvil debe recibir la notificación push. Utiliza esta selección para limitar la entrega de una notificación push a un conjunto específico de aplicaciones.

Hay varias formas de hacerlo en función de tus selecciones anteriores:

| Selección previa | Opciones |
| --- | --- | 
| Campaña de notificaciones push | Selecciona una o varias plataformas y dispositivos. Si eliges dirigirte a varios dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Esto proporciona una experiencia de edición optimizada para elaborar un mensaje para todas las plataformas seleccionadas en un único editor. Consulta [Campañas de push rápidas]({{site.baseurl}}/quick_push) para comprender las diferencias de esta experiencia de edición. |
| Campaña multicanal | Selecciona **Añadir canal de mensajería** para añadir plataformas push adicionales. Dado que las selecciones de plataforma son específicas de cada variante, puedes probar la interacción del mensaje por plataforma.
| Canvas | En el paso Mensajes, selecciona **+ Añadir más** para añadir plataformas push adicionales. Al igual que en las campañas multicanal, la selección de plataformas es específica para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Selecciona el tipo de notificación (iOS y Android)

Si estás creando una campaña push rápida, el tipo de notificación se establece automáticamente en **Push estándar** y no se puede cambiar.

![Tipo de notificación con push estándar seleccionado como ejemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

De lo contrario, para iOS y Android, selecciona tu tipo de notificación:

- Push estándar
- [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Imagen en línea (solo Android)

Si deseas incluir imágenes en tu campaña push, consulta las siguientes guías sobre cómo crear una notificación enriquecida para [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) o [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Paso 4: Redacta tu mensaje push

Ahora es el momento de escribir tu mensaje push. La pestaña **Redactar** te permite editar todos los aspectos del contenido y el comportamiento de tu mensaje.

![Pestaña Redactar para crear una notificación push.]({% image_buster /assets/img_archive/push_compose.png %})

El contenido de la pestaña **Redactar** varía en función del tipo de notificación elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

#### Canal o grupo de notificaciones (iOS y Android)

Para obtener más información sobre las opciones de notificación específicas de cada plataforma, consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) u [Opciones de notificación de Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Idioma

Añade textos en varios idiomas con el botón **Añadir idiomas**. Te recomendamos que selecciones tus idiomas antes de escribir el contenido para que puedas rellenar el texto donde corresponda en Liquid. Para consultar nuestra lista completa de idiomas disponibles, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si añades texto en un idioma escrito de derecha a izquierda, ten en cuenta que el aspecto final de los mensajes escritos de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

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
**No puedes** enviar un mensaje push de Android sin un título; sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que si tu mensaje solo contiene un espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
¿Necesitas ayuda para crear textos impactantes? Prueba a utilizar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para utilizarlo en tus mensajes.

![Botón Abrir asistente de redacción con IA, ubicado en el campo Cuerpo del compositor push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Imagen

Cuando es compatible, el icono de tu aplicación se añade automáticamente como imagen de tu notificación push. También tienes la opción de enviar notificaciones enriquecidas, que permiten una mayor personalización en tus notificaciones push añadiendo contenido adicional más allá del texto.

Para más información sobre el uso de imágenes en las notificaciones push, consulta los siguientes artículos:

- [Crear notificaciones enriquecidas para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Crear notificaciones enriquecidas para Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Comportamiento al hacer clic

Especifica qué ocurre cuando un usuario selecciona el cuerpo de una notificación push con **Comportamiento al hacer clic**. Por ejemplo, puedes pedir a los clientes que abran tu aplicación, redirigirlos a una URL web específica o incluso abrir una página concreta de tu aplicación con un [vínculo profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Aquí también puedes configurar avisos de botón dentro de tu notificación push, como:

- Aceptar/Rechazar
- Sí/No
- Confirmar/Cancelar
- Más 

#### Opciones de envío

Si un usuario tiene tu aplicación instalada en varios dispositivos, de forma predeterminada, tu mensaje push se envía a todos los dispositivos que tengan asignado un token de notificaciones push válido. Si lo deseas, puedes seleccionar **Dispositivo utilizado más recientemente**.

![Casilla de verificación de opciones de dispositivo para enviar esta notificación push únicamente al último dispositivo utilizado por el usuario.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }


De forma predeterminada, Braze envía mensajes a todos los dispositivos que un usuario posee y que tienen un token de notificaciones push válido. Para iOS, puedes afinar aún más tu alcance eligiendo enviar notificaciones solo a dispositivos iPad, o solo a dispositivos iPhone y iPod.

Si lo deseas, puedes establecer el destino push en **Dispositivo utilizado más recientemente**. 

##### Dispositivo utilizado más recientemente

"Utilizado más recientemente" es un estado técnico, no conductual. Dado que Braze envía de forma predeterminada a todos los dispositivos, cambiar a esta configuración reduce significativamente tu alcance y depende completamente del estado del único dispositivo con el token más reciente.

![Casilla de verificación de opciones de dispositivo para enviar esta notificación push únicamente al último dispositivo utilizado por el usuario.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

El dispositivo utilizado más recientemente se determina por cuál tiene el token de notificaciones push actualizado más recientemente, no por cuál tuvo la sesión más reciente. 
* Si se añade un token de notificaciones push de un nuevo dispositivo a un perfil de usuario a través de la API, ese dispositivo se considera inmediatamente como el utilizado más recientemente, incluso si el usuario aún no ha iniciado una sesión en él. 
* Si el dispositivo utilizado más recientemente de un usuario no está [habilitado para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), el mensaje no se enviará en absoluto.

Pueden producirse envíos múltiples si una campaña se dirige a diferentes plataformas, como iOS y Android. Si un usuario tiene la aplicación en ambas, puede recibir una notificación push para ambas plataformas.

Para iOS, puedes limitar aún más la mensajería enviando notificaciones push solo a dispositivos iPad, o solo a dispositivos iPhone y iPod.

## Paso 5: Vista previa y prueba de tu mensaje (opcional)

Podría decirse que las pruebas son uno de los pasos más críticos. Cuando termines de redactar el mensaje push perfecto, pruébalo antes de enviarlo. Selecciona la pestaña **Prueba** para elegir entre las opciones disponibles sobre cómo probar tu mensaje push. En **Destinatarios de la prueba**, puedes seleccionar un grupo de prueba de contenido o usuarios individuales. También puedes utilizar **Vista previa del mensaje como usuario** para hacerte una idea de cómo se verá tu mensaje en el móvil para un usuario aleatorio, un usuario existente, un usuario personalizado o un usuario multilingüe.

## Paso 6: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña; consulta las siguientes secciones para obtener más detalles sobre la mejor manera de utilizar nuestras herramientas para construir notificaciones push.

#### Elige la planificación o desencadenante de la entrega

Los mensajes push pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) seleccionando segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una vista previa de cómo es aproximadamente la población de ese segmento. En el pie de página encontrarás estadísticas detalladas sobre la audiencia de los canales a los que se dirige tu campaña. Para ver a qué porcentaje de tu base de usuarios se dirige y el valor de duración del ciclo de vida de este segmento, selecciona **Mostrar estadísticas adicionales**.

{% multi_lang_include target_audiences.md %}

{% details ¿Por qué mi métrica de total de usuarios alcanzables no coincide con la suma de todos los canales? %}

Cuando veas el total de usuarios alcanzables para tu audiencia filtrada, es posible que observes que la suma de las columnas individuales es menor que el total de usuarios alcanzables. Esta diferencia suele deberse a que hay una serie de usuarios que cumplen los requisitos para el segmento o los filtros de la campaña, pero a los que no se puede llegar a través de push (por ejemplo, porque no tienen [tokens de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) válidos o activos).

{% enddetails %}

![Tabla con estadísticas detalladas de audiencia para usuarios alcanzables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de enviar el mensaje.

También puedes optar por enviar tu campaña solo a los usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como los que estén suscritos y hayan optado por recibir push.

Opcionalmente, también puedes limitar la entrega a un número determinado de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces al repetirse la campaña.

##### Campañas multicanal con correo electrónico y push

En el caso de las campañas multicanal dirigidas tanto al correo electrónico como a los canales push, es posible que desees limitar tu campaña para que solo los usuarios que hayan optado explícitamente por ello reciban el mensaje (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

- **El usuario A** está suscrito al correo electrónico y tiene activado push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibirá el push.
- **El usuario C** tiene la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, en **Resumen de audiencia**, selecciona enviar esta campaña solo a "usuarios con adhesión voluntaria". Esta opción garantizará que solo los usuarios con adhesión voluntaria reciban tu correo electrónico, y Braze solo enviará tu push a los usuarios que estén habilitados para push de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencias objetivo** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

#### Elegir eventos de conversión

Braze te permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante e Intelligent Selection, y más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 7: Revisar y desplegar {#review-and-deploy-push}

Cuando hayas terminado de crear la última parte de tu campaña o Canvas, revisa sus detalles. En el caso de las campañas, la página final te ofrece un resumen de la campaña que has diseñado. Confirma todos los datos relevantes, asegúrate de que has probado tu mensaje y, a continuación, envíalo para ver cómo llegan los datos.

A continuación, consulta [Informes push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber cómo puedes acceder a los resultados de tu campaña push. En el caso de las notificaciones push, podrás ver estadísticas sobre el número de mensajes enviados, entregados, rebotados, abiertos y abiertos directamente.