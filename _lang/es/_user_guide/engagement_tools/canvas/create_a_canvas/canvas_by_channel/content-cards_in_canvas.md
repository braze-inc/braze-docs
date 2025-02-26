---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido en Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia describe las características y matices específicos del uso de las Tarjetas de contenido como canal de mensajería dentro de Canvas."
tool: Canvas
channel: content cards

---

# Tarjetas de contenido en Canvas

> Las tarjetas de contenido pueden enviarse a sus clientes como parte de su recorrido por Canvas. En este artículo se describen las características y los matices específicos del uso de las Tarjetas de contenido como canal de mensajería dentro de Canvas.

Al igual que ocurre con otros canales de mensajería de Canvas, las Tarjetas de contenido se enviarán al dispositivo de un usuario cuando éste cumpla los criterios de audiencia y segmentación especificados para su paso. Una vez enviada la tarjeta de contenido, estará disponible en el feed de cada usuario que cumpla los requisitos la próxima vez que se actualice su feed de tarjetas.

![][1]

Dos opciones que cambiarán la forma en que el paso Tarjeta de contenido interactuará con Canvas son su [Expiración](#content-card-expiration) y su [Comportamiento de avance](#advancement-behavior-options).

## Caducidad de la tarjeta de contenido {#content-card-expiration}

Al componer una nueva tarjeta de contenido, puede elegir cuándo debe caducar del feed del usuario en función de su hora de envío. La cuenta atrás para la caducidad de una Tarjeta de Contenido comienza cuando el usuario llega al paso Mensaje en el Canvas donde se envía la tarjeta. La tarjeta estará activa en el feed del usuario desde este momento hasta que caduque. Una tarjeta puede existir en el feed de un usuario durante un máximo de 30 días. 

### Fechas de caducidad relativas frente a absolutas

Hay dos formas de establecer cuándo debe desaparecer una tarjeta del feed de un usuario: una fecha relativa o una fecha absoluta. A continuación te explicamos cómo funciona cada uno:

#### Fechas relativas

Si elige una fecha relativa, como "Eliminar tarjetas enviadas después de 5 días en el feed de un usuario", puede establecer una fecha de caducidad máxima de 30 días.

#### Fechas absolutas

Cuando se elige una fecha absoluta, como "Retirar las tarjetas enviadas el 1 de diciembre de 2023 a las 16.00 horas", hay que matizar.

Aunque puede especificar una duración de caducidad superior a 30 días, la tarjeta de contenido existirá en el feed de un usuario durante un máximo de 30 días. Especificar una duración superior a 30 días le permite tener en cuenta cualquier retraso antes de activar el paso Mensaje, pero no prolonga la vida máxima de la tarjeta en el feed del usuario.

Tenga cuidado al fijar una fecha de caducidad con más de 30 días de antelación desde el lanzamiento del lienzo. Si un usuario llega al paso Mensaje más de 30 días antes de la fecha de caducidad especificada, la tarjeta no se enviará.

### Comportamiento de caducidad

La tarjeta de contenido permanece disponible en el feed del usuario hasta que llega a su fecha de caducidad, incluso si el usuario avanza a pasos posteriores en el recorrido Canvas. Si no desea que la tarjeta de contenido esté activa cuando se entreguen los siguientes pasos del lienzo, asegúrese de que la caducidad sea inferior al retraso de los pasos siguientes.

Cuando caduque una tarjeta de contenido, se eliminará automáticamente del feed del usuario durante la siguiente actualización, aunque no la haya visto todavía.

## Opciones de comportamiento de avance {#advancement-behavior-options}

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con Tarjetas de Contenido.
{% endalert %}

{% alert note %}
En el Flujo Canvas, los componentes de Mensaje hacen avanzar automáticamente a todos los usuarios que entran en el paso. No es necesario especificar el comportamiento de avance de los mensajes, lo que simplifica la configuración del paso general. Si desea implementar la opción **Avanzar cuando se envíe el mensaje**, añada una [Ruta de público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) independiente para filtrar los usuarios que no hayan recibido el paso anterior.
{% endalert %}

La opción Comportamiento de avance le permite controlar cuándo un usuario debe avanzar a su siguiente paso elegible. Los pasos que [sólo envían Tarjetas de contenido](#steps-with-in-content-cards-only) tienen diferentes opciones de avance que [los pasos con varios tipos de mensajes](#steps-with-multiple-message-channels) (push, correo electrónico, etc.). Para las Tarjetas de contenido en un flujo de trabajo de Canvas Flow, esta opción está configurada para que la audiencia avance siempre inmediatamente.

### Pasos solo con tarjetas de contenido {#steps-with-in-content-cards-only}

Si un paso sólo contiene Tarjetas de contenido (y ningún otro canal de mensajería), puede controlar el comportamiento de avance con las siguientes opciones:

| Opción | Descripción |
|---|---|
| Avanzar cuando el mensaje se haya enviado | Los usuarios avanzarán a los siguientes pasos del lienzo cuando la tarjeta de contenido se haya enviado correctamente. Utilice esta opción cuando desee que los usuarios sólo avancen si la tarjeta va a ser enviada y no abortada. |
| Avanzar audiencia inmediatamente | Los usuarios avanzarán a los siguientes pasos del lienzo cuando se intente enviar la tarjeta de contenido. Si la tarjeta se cancela y no se envía, los usuarios seguirán avanzando al siguiente paso. Utilice esta opción cuando desee que los usuarios avancen independientemente de si la tarjeta de contenido se envía correctamente o se cancela. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Componentes con varios canales {#steps-with-multiple-message-channels}

Los componentes del lienzo con una tarjeta de contenido y otro canal de mensajería tienen las siguientes opciones de avance:

| Opción | Descripción |
|---|---|
| Avanzar cuando el mensaje se haya enviado | Los usuarios avanzarán a los siguientes pasos del Canvas cuando al menos uno de los tipos de mensaje de este paso se haya enviado correctamente.|
| Avanzar audiencia inmediatamente | Cuando se selecciona esta opción, todas las personas del público del componente avanzarán a los pasos siguientes una vez transcurrido el retardo, hayan visto o no el mensaje señalado.  <br> <br> _Los usuarios deben coincidir con los criterios de segmento y filtro del componente para avanzar a los siguientes pasos._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

## Informes y análisis

Después de lanzar un paso de Tarjetas de contenido en Canvas, puede comenzar a analizar varias métricas diferentes para este paso. Estas métricas incluyen el número de mensajes enviados, los destinatarios únicos, las tasas de conversión, los ingresos totales, etc.

![][4]

Para más información sobre las métricas disponibles y sus definiciones, consulte nuestro [Glosario de métricas de los informes][6].

## Ejemplos

#### Ofertas promocionales

Añada tarjetas al feed de un usuario cuando reúna los requisitos para promociones y anuncios específicos. Por ejemplo, si un usuario se convierte en elegible para una nueva oferta después de realizar una acción o efectuar una compra, utilizando Canvas puedes enviarle una Content Card, además de otros canales de mensajería, para que la próxima vez que abra la app la oferta esté disponible para él.

#### Bandeja de entrada de notificaciones push

Hay ocasiones en las que un usuario puede descartar una notificación push o eliminar un correo electrónico, pero usted quiere recordárselo o promocionar la oferta por si cambia de opinión.

Mediante Canvas, puede añadir un componente que envíe tanto una tarjeta de contenido como una notificación push para ofrecer a los usuarios una "bandeja de entrada" persistente de tarjetas que se alineen con los mensajes promocionales enviados mediante push. 

#### Múltiples fuentes basadas en categorías

Puede separar sus tarjetas de contenido en varios feeds en función de categorías como, por ejemplo, los distintos temas que pueden consultar los usuarios, o los feeds transaccionales y de marketing. Si desea más información sobre la creación de múltiples feeds mediante pares clave-valor, consulte nuestra guía para [Personalizar los feeds de las tarjetas de contenido][7].


[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %}
[2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel.png %}
[3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %}
[4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}
[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[7]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds