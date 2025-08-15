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

![Tarjetas de contenido seleccionadas como canal de mensajería para un paso de Mensaje.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Dos opciones que cambiarán el modo en que el paso en Tarjeta de contenido interactuará con Canvas son su [caducidad](#content-card-expiration) y su [eliminación](#removal).

## Caducidad de la tarjeta de contenido {#content-card-expiration}

Al componer una nueva tarjeta de contenido, puede elegir cuándo debe caducar del feed del usuario en función de su hora de envío. La cuenta atrás para la caducidad de una Tarjeta de Contenido comienza cuando el usuario llega al paso Mensaje en el Canvas donde se envía la tarjeta. La tarjeta estará activa en el feed del usuario desde este momento hasta que caduque. Una tarjeta puede existir en el feed de un usuario durante un máximo de 30 días. 

![Configuración de caducidad de una tarjeta de contenido para un paso de mensaje que se eliminará al cabo de tres horas en la fuente de un usuario.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de caducidad

Hay dos formas de establecer cuándo debe desaparecer una tarjeta del feed de un usuario: una fecha relativa o una fecha absoluta.

#### Fechas relativas

Cuando eliges una fecha relativa, como "Eliminar tarjetas enviadas tras 5 días en la fuente de un usuario", puedes establecer una fecha de caducidad de hasta 30 días.

#### Fechas absolutas

Cuando se elige una fecha absoluta, como "Retirar las tarjetas enviadas el 1 de diciembre de 2023 a las 16.00 horas", hay que matizar.

Aunque puede especificar una duración de caducidad superior a 30 días, la tarjeta de contenido existirá en el feed de un usuario durante un máximo de 30 días. Especificar una duración superior a 30 días le permite tener en cuenta cualquier retraso antes de activar el paso Mensaje, pero no prolonga la vida máxima de la tarjeta en el feed del usuario.

Tenga cuidado al fijar una fecha de caducidad con más de 30 días de antelación desde el lanzamiento del lienzo. Si un usuario llega al paso Mensaje más de 30 días antes de la fecha de caducidad especificada, la tarjeta no se enviará.

### Comportamiento de caducidad

La tarjeta de contenido permanece disponible en el feed del usuario hasta que llega a su fecha de caducidad, incluso si el usuario avanza a pasos posteriores en el recorrido Canvas. Si no desea que la tarjeta de contenido esté activa cuando se entreguen los siguientes pasos del lienzo, asegúrese de que la caducidad sea inferior al retraso de los pasos siguientes.

Cuando caduque una tarjeta de contenido, se eliminará automáticamente del feed del usuario durante la siguiente actualización, aunque no la haya visto todavía.

## Eliminación de la tarjeta de contenido {#removal}

Las tarjetas de contenido se pueden eliminar cuando los usuarios completan una compra o realizan un evento personalizado. Puedes seleccionar uno de los siguientes como evento de eliminación: **Realiza el evento personalizado** y **efectúa la compra**. A continuación, selecciona **Añadir Evento**.

!["Eliminar tarjetas cuando los usuarios completen una compra o realicen un evento personalizado" seleccionado con el desencadenante de eliminar tarjetas para los usuarios que realicen una compra específica para "Pulsera".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Informes y análisis

Después de lanzar un paso de Tarjetas de contenido en Canvas, puede comenzar a analizar varias métricas diferentes para este paso. Estas métricas incluyen el número de mensajes enviados, los destinatarios únicos, las tasas de conversión, los ingresos totales, etc.

![Análisis de un paso de mensaje con el rendimiento del mensaje de la tarjeta de contenido.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para más información sobre las métricas disponibles y sus definiciones, consulta nuestro [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/).

## Ejemplos

#### Ofertas promocionales

Añada tarjetas al feed de un usuario cuando reúna los requisitos para promociones y anuncios específicos. Por ejemplo, si un usuario se convierte en elegible para una nueva oferta después de realizar una acción o efectuar una compra, utilizando Canvas puedes enviarle una Content Card, además de otros canales de mensajería, para que la próxima vez que abra la app la oferta esté disponible para él.

#### Bandeja de entrada de notificaciones push

Hay ocasiones en las que un usuario puede descartar una notificación push o eliminar un correo electrónico, pero usted quiere recordárselo o promocionar la oferta por si cambia de opinión.

Mediante Canvas, puede añadir un componente que envíe tanto una tarjeta de contenido como una notificación push para ofrecer a los usuarios una "bandeja de entrada" persistente de tarjetas que se alineen con los mensajes promocionales enviados mediante push. 

#### Múltiples fuentes basadas en categorías

Puede separar sus tarjetas de contenido en varios feeds en función de categorías como, por ejemplo, los distintos temas que pueden consultar los usuarios, o los feeds transaccionales y de marketing. Para más información sobre la creación de múltiples fuentes utilizando pares clave-valor, consulta nuestra guía para [Personalizar las fuentes de la tarjeta de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


