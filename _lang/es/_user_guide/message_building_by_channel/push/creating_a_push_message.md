---
nav_title: "Creación de un mensaje push"
article_title: Creación de una campaña Push
page_order: 4
page_type: tutorial
description: "Esta página tutorial cubre los diferentes componentes involucrados en la creación de un Mensaje Push, incluyendo la configuración, el envío, la orientación, y más."
channel: push
tool:
  - Campaigns
  
---

# Crear un mensaje push

> Las notificaciones push son magníficas para las llamadas a la acción urgentes, así como para volver a atraer a los usuarios que hace tiempo que no entran en la aplicación. Las campañas push exitosas llevan al usuario directamente al contenido y demuestran el valor de su aplicación. Para ver ejemplos de notificaciones push, consulta nuestros [casos de estudio](https://www.braze.com/customers).

## Paso 1: Elige dónde construir tu mensaje {#create-new-campaign-push}

{% alert tip %}
¿No estás seguro de si utilizar una campaña o un Canvas? Las campañas son mejores para campañas de mensajería sencillas y únicas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.
{% endalert %}

{% tabs %}
{% tab Campaña %}
1. Ve a **Mensajería** > **Campañas** y, a continuación, selecciona **Crear campaña**.
2. Para campañas dirigidas a varios canales, selecciona **Multicanal**. Si no, selecciona **Notificación push**. Si aún no estás seguro, consulta **Decidir entre una campaña push normal o multicanal** más abajo.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [Equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [Etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario. 

{% alert tip %}
Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.
{% endalert %}

{: start="5"}
5\. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Decidir entre una campaña push normal o multicanal %}

Si tiene intención de dirigirse a varios dispositivos y plataformas, como cualquier combinación de móvil, web, Kindle, iOS y Android, su selección en este paso puede afectar a la disponibilidad de algunas funciones y ajustes más adelante.

Consulte el siguiente cuadro de decisiones antes de crear una campaña multicanal o de notificaciones push:

!["Diagrama de flujo para seleccionar el tipo de campaña. Empieza por decidir si te diriges a varios dispositivos y plataformas. Si no, te lleva a "Seleccionar notificación push". En caso afirmativo, pregunta "¿Qué tipo de mensaje push?" y las opciones son "Push estándar", lo que lleva a un punto de decisión "¿Necesitas utilizar una configuración específica del dispositivo?". Si no, te lleva a 'Seleccionar notificación push y utilizar push rápido'. Si la respuesta es sí, pasa a "Seleccionar Multicanal". De vuelta a "¿Qué tipo de mensaje push?", si la respuesta es "Historias push o imagen en línea", te dirige a "Seleccionar multicanal".]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si seleccionas **Notificación Push** y eliges dirigirte a múltiples dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Con la pulsación rápida, algunos ajustes específicos del dispositivo no están disponibles:

- Botones de acción para notificación push
- Canales y grupos de notificación
- Tiempo de vida push (TTL)
- Prioridad de visualización
- Sonidos

Antes de continuar, consulta [Campañas push rápidas]({{site.baseurl}}/quick_push) para entender qué es diferente en esta experiencia de edición.

{% enddetails %}

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que haya configurado su lienzo, añada un paso en el constructor de lienzos. Nombra tu paso con algo claro y significativo.
3. Elija un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifique un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puede afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elija cualquier otro canal de mensajería que desee asociar a su mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Selecciona plataformas push

A continuación, elige qué combinación de plataforma y dispositivo móvil debe recibir el push. Utilice esta selección para limitar la entrega de una notificación push a un conjunto específico de aplicaciones.

Hay varias formas de hacerlo en función de tus selecciones anteriores:

| Selección previa | Opciones |
| --- | --- | 
| Campaña de notificaciones push | Seleccione una o varias plataformas y dispositivos. Si eliges dirigirte a varios dispositivos y plataformas, estarás creando automáticamente una campaña push rápida. Esto proporciona una experiencia de edición optimizada para elaborar un mensaje para todas las plataformas seleccionadas en un único editor. Consulte [Campañas rápidas]({{site.baseurl}}/quick_push) para comprender las diferencias de esta experiencia de edición. |
| Campaña multicanal | Selecciona **Añadir canal de mensajería** para añadir plataformas push adicionales. Dado que las selecciones de plataforma son específicas de cada variante, puede probar la participación del mensaje por plataforma.
| Canvas | En el paso Mensajes, selecciona **\+ Añadir más** para añadir plataformas push adicionales. Al igual que en las campañas multicanal, la selección de plataformas es específica para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Seleccione el tipo de notificación (iOS y Android)

Si estás creando una campaña push rápida, el tipo de notificación se establece automáticamente en **Push estándar** y no se puede cambiar.

![Tipo de notificación con Push Estándar seleccionado como ejemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

De lo contrario, para iOS y Android, selecciona tu tipo de notificación:

- Notificación push estándar
- [Historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Imagen en línea (sólo Android)

Si desea incluir imágenes en su campaña push, consulte las siguientes guías sobre cómo crear una notificación enriquecida para [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) o [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Paso 4: Redacta tu mensaje push

Ahora es el momento de escribir tu mensaje push. La pestaña **Redactar** te permite editar todos los aspectos del contenido y el comportamiento de tu mensaje.

![Pestaña de creación de una notificación push.]({% image_buster /assets/img_archive/push_compose.png %})

El contenido de la pestaña **Redactar** varía en función del tipo de notificación elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

#### Canal o grupo de notificaciones (iOS y Android)

Para obtener más información sobre las opciones de notificación específicas de cada plataforma, consulte [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) u [Opciones de notificación de Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Idioma

Añada copias en varios idiomas con el botón **Añadir idiomas**. Le recomendamos que seleccione sus idiomas antes de escribir el contenido para que pueda rellenar el texto donde corresponda en el Líquido. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

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
**No puedes** enviar un mensaje push de Android sin un título; sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que si tu mensaje sólo contiene un espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
¿Necesitas ayuda para crear textos impactantes? Prueba a utilizar el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduzca el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para utilizarlo en sus mensajes.

![Botón de Lanzar el redactor de IA, situado en la pestaña Cuerpo del compositor de correo electrónico.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Imagen

Cuando es compatible, el icono de tu aplicación se añade automáticamente como imagen de tu notificación push. También tienes la opción de enviar notificaciones enriquecidas, que permiten una mayor personalización en tus notificaciones push añadiendo contenido adicional más allá del copy.

Para más información sobre el uso de imágenes en las notificaciones push, consulta los siguientes artículos:

- [Crear notificaciones enriquecidas para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Crear notificaciones enriquecidas para Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportamiento al hacer clic

Especifica qué ocurre cuando un usuario selecciona el cuerpo de una notificación push con **Comportamiento al hacer clic**. Por ejemplo, puede pedir a los clientes que abran su aplicación, redirigirlos a una URL Web específica o incluso abrir una página concreta de su aplicación con un [enlace profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Aquí también puedes configurar avisos de botón dentro de tu notificación push, como:

- Aceptar/Rechazar
- Sí/No
- Confirmar/Cancelar
- Más 

#### Opciones de envío

Si un usuario tiene su aplicación instalada en varios dispositivos, por defecto, su mensaje push se envía a todos los dispositivos que tengan asignado un token push válido. Si lo deseas, puedes seleccionar **el dispositivo utilizado más recientemente**.

![Casilla de opciones del dispositivo para enviar este push sólo al dispositivo utilizado más recientemente por el usuario.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Esta configuración tiene algunos matices. Si se selecciona esta opción, Braze limitará los envíos múltiples, excepto cuando una campaña se dirija a varias plataformas, como iOS y Android. Si el usuario tiene tu aplicación tanto en un dispositivo iOS como Android, recibirá un push para ambas plataformas. Si el último dispositivo utilizado por un usuario no está [habilitado para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled), el mensaje no se enviará.

Para iOS, puedes limitar aún más la mensajería enviando notificaciones push solo a dispositivos iPad, o solo a dispositivos iPhone y iPod.

## Paso 5: Vista previa y prueba de tu mensaje (opcional)

Podría decirse que las pruebas son uno de los pasos más críticos. Cuando termine de redactar el mensaje push perfecto, pruébelo antes de enviarlo. Selecciona la pestaña **Prueba** para elegir entre las opciones sobre cómo probar tu mensaje push. En **Destinatarios de prueba**, puedes seleccionar un grupo de prueba de contenido o usuarios individuales. También puedes utilizar **Vista previa del mensaje como usuario** para hacerte una idea de cómo puede verse tu mensaje en el móvil para un usuario aleatorio, un usuario existente, un usuario personalizado o un usuario multilingüe.

## Paso 6: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaña %}

Construya el resto de su campaña; consulte las siguientes secciones para obtener más detalles sobre la mejor manera de utilizar nuestras herramientas para construir notificaciones push.

#### Elige la programación o desencadenante de la entrega

Los mensajes push pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

En este paso también puede especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente obtendrá una instantánea de cómo es la población de ese segmento aproximado en este momento. En el pie de página encontrará estadísticas detalladas sobre la audiencia de los canales a los que se dirige su campaña. Para ver a qué porcentaje de tu base de usuarios se dirige y el valor de duración del ciclo de vida de este segmento, selecciona **Mostrar estadísticas adicionales**.

{% details ¿Por qué mi métrica de usuarios alcanzables totales no coincide con la suma de todos los canales? %}

Cuando vea el Total de usuarios a los que se puede llegar para su audiencia filtrada, es posible que observe que la suma de las columnas individuales es menor que el Total de usuarios a los que se puede llegar. Esta brecha suele deberse a que hay una serie de usuarios que cumplen los requisitos para el segmento o los filtros de la campaña, pero a los que no se puede llegar a través de push (por ejemplo, porque no tienen [tokens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) válidos o activos).

{% enddetails %}

![Tabla de estadísticas detalladas de audiencia para los usuarios alcanzables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

También puede optar por enviar su campaña sólo a los usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como los que estén suscritos y hayan optado por recibir push.

Opcionalmente, también puede limitar la entrega a un número determinado de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces al repetirse la campaña.

##### Campañas multicanal con correo electrónico y push

En el caso de las campañas multicanal dirigidas tanto al correo electrónico como a los canales push, es posible que desee limitar su campaña para que sólo los usuarios que hayan optado explícitamente por recibir el mensaje (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tiene tres usuarios con diferentes estados de suscripción:

- **El usuario A** está suscrito al correo electrónico y tiene activada la función push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el email pero no recibirá el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, en **Resumen de audiencia**, seleccione enviar esta campaña sólo a "usuarios que hayan optado por ella". Esta opción garantizará que sólo los usuarios que hayan optado por recibirla reciban su correo electrónico, y Braze sólo enviará su push a los usuarios que estén habilitados para push de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencias objetivo** que limite la audiencia a un único canal (por ejemplo, `Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de su Canvas, implementar pruebas multivariantes y Selección Inteligente, y más, consulte el paso [Construya su Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 7: Revisar y desplegar {#review-and-deploy-push}

Cuando hayas terminado de crear la última parte de tu campaña o Canvas, revisa sus detalles. En el caso de las campañas, la última página le ofrecerá un resumen de la campaña que acaba de diseñar. Confirme todos los datos relevantes, asegúrese de que ha probado su mensaje y, a continuación, envíelo para ver cómo llegan los datos.

A continuación, consulte [Informes push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber cómo puede acceder a los resultados de su campaña push. En el caso de las notificaciones push, podrás ver estadísticas sobre el número de mensajes enviados, entregados, rebotados, abiertos y abiertos directamente.

