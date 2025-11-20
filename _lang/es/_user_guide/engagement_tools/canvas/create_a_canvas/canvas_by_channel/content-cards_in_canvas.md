---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido en Canvas
page_order: 1
page_type: reference
description: "Este artículo de referencia describe características y matices específicos del uso de las Tarjetas de contenido como canal de mensajería dentro de Canvas."
tool: Canvas
channel: content cards

---

# Tarjetas de contenido en Canvas

> Puedes enviar tarjetas de contenido a tus clientes como parte de su recorrido por Canvas. Este artículo describe características y matices específicos del uso de las tarjetas de contenido como canal de mensajería dentro de Canvas.

Al igual que ocurre con otros canales de mensajería de Canvas, las tarjetas de contenido se enviarán al dispositivo de un usuario cuando éste cumpla los criterios de audiencia y segmentación especificados para su paso. Una vez enviada la tarjeta de contenido, estará disponible en la fuente de cada usuario elegible la próxima vez que se actualice su fuente de tarjetas.

\![Tarjetas de contenido seleccionadas como canal de mensajería para un paso de Mensaje.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Dos opciones que cambiarán el modo en que el paso en Tarjeta de contenido interactuará con Canvas son su [caducidad](#content-card-expiration) y su [eliminación](#removal).

## Caducidad de la tarjeta de contenido {#content-card-expiration}

Al componer una nueva tarjeta de contenido, puedes elegir cuándo debe caducar de la fuente del usuario en función de su hora de envío. La cuenta atrás para la caducidad de una tarjeta de contenido comienza cuando el usuario llega al paso en Canvas Mensaje, donde se envía la tarjeta. La tarjeta estará activa en la fuente del usuario desde este momento hasta que caduque. Una tarjeta puede existir en la fuente de un usuario hasta 30 días. 

\![Configuración de caducidad de una tarjeta de contenido para un paso de mensaje que se eliminará al cabo de tres horas en la fuente de un usuario.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de caducidad

Tienes dos formas de establecer cuándo debe desaparecer una tarjeta de la fuente de un usuario: una fecha relativa o una fecha absoluta.

#### Fechas relativas

Cuando eliges una fecha relativa, como "Eliminar tarjetas enviadas tras 5 días en la fuente de un usuario", puedes establecer una fecha de caducidad de hasta 30 días.

#### Fechas absolutas

Cuando eliges una fecha absoluta, como "Eliminar las tarjetas enviadas el 1 de diciembre de 2023 a las 16:00", hay algunos matices.

Aunque puedes especificar una duración de caducidad superior a 30 días, la tarjeta de contenido existirá en la fuente de un usuario durante un máximo de 30 días. Especificar una duración superior a 30 días te permite tener en cuenta cualquier retraso antes de desencadenar el paso Mensaje, pero no amplía la vida máxima de la tarjeta en la fuente del usuario.

Ten cuidado al establecer una fecha de caducidad con más de 30 días de antelación desde el inicio del Canvas. Si un usuario llega al paso Mensaje más de 30 días antes de la fecha de caducidad especificada, no se enviará la tarjeta.

### Comportamiento de caducidad

La tarjeta de contenido permanece disponible en la fuente del usuario hasta que llega a su fecha de caducidad, incluso si el usuario avanza a pasos posteriores en el recorrido por Canvas. Si no quieres que la tarjeta de contenido esté en vivo cuando se entreguen los pasos siguientes en el Canvas, asegúrate de que la caducidad es más corta que el retraso en los pasos siguientes.

Cuando caduque una tarjeta de contenido, se eliminará automáticamente de la fuente del usuario en la siguiente actualización, aunque no la haya visto todavía.

## Eliminación de la tarjeta de contenido {#removal}

Las tarjetas de contenido se pueden eliminar cuando los usuarios completan una compra o realizan un evento personalizado. Puedes seleccionar uno de los siguientes como evento de eliminación: **Realiza un evento personalizado** y **efectúa una compra**. A continuación, selecciona **Añadir Evento**.

\!["Quitar tarjetas cuando los usuarios completen una compra o realicen un evento personalizado." seleccionado con el desencadenante para quitar tarjetas a los usuarios que realicen una compra específica para "Pulsera".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Informes y análisis

Después de lanzar un paso de Tarjetas de contenido en Canvas, puedes empezar a analizar varias métricas diferentes para este paso. Estas métricas incluyen el número de mensajes enviados, los destinatarios únicos, las tasas de conversión, los ingresos totales y mucho más.

\![Análisis de un paso de mensajes con el rendimiento de los mensajes de la tarjeta de contenido.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para más información sobre las métricas disponibles y sus definiciones, consulta nuestro [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/).

## Casos de uso

#### Ofertas promocionales

Añade tarjetas a la fuente de un usuario cuando cumpla los requisitos para promociones y anuncios específicos. Por ejemplo, si un usuario resulta elegible para una nueva oferta tras realizar una acción o efectuar una compra, utilizando Canvas puedes enviarle una tarjeta de contenido, además de otros canales de mensajería, para que la próxima vez que abra la aplicación tenga la oferta a su disposición.

#### Buzón de entrada de notificaciones push

Hay ocasiones en las que un usuario puede descartar una notificación push o eliminar un correo electrónico, pero quieres recordárselo o promocionar la oferta por si cambia de opinión.

Utilizando Canvas, puedes añadir un componente que envíe tanto una tarjeta de contenido como una notificación push para dar a los usuarios un "buzón de entrada" persistente de tarjetas que se alineen con los mensajes promocionales enviados mediante push. 

#### Múltiples fuentes basadas en categorías

Puedes separar tus tarjetas de contenido en varias fuentes basadas en categorías, como los distintos temas por los que pueden navegar los usuarios, o fuentes transaccionales y de marketing. Para más información sobre la creación de múltiples fuentes utilizando pares clave-valor, consulta nuestra guía para [personalizar las fuentes de la tarjeta de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


