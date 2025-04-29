---
nav_title: Conector de campaña
article_title: Conector de campaña
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artículo explica qué es el Conector de Campaña y cómo utilizarlo para ofrecer contenido relevante y específico en el momento adecuado."

---
# Conector de campaña

> Campaign Connector te permite crear campañas que se activan cuando los usuarios interactúan con campañas activas o tarjetas de noticias. Esta función es útil porque le permite ofrecer contenidos específicos y pertinentes en el momento adecuado. 

{% alert note %}
Este artículo incluye información sobre la Fuente de noticias, que está siendo obsoleta. Braze recomienda a los clientes que utilizan nuestra herramienta News Feed que se pasen a nuestro canal de mensajería Content Cards: es más flexible, personalizable y fiable. Consulta la [guía de]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) migración para obtener más información.
{% endalert %}

Esta función le permite dirigirse a usuarios que completen las siguientes interacciones con campañas activas:

- Ver mensaje en la aplicación
- Haz clic en el mensaje de la aplicación
- Pulsa los botones de mensajes de la aplicación
- Hacer clic en el correo electrónico
- Hacer clic en el alias del correo electrónico
- Abrir correo electrónico
- Abrir directamente una notificación push
- Haga clic en el botón de notificación push
- Hacer clic en la página de historias push
- Realizar evento de conversión
- Recibir correo electrónico
- Recibir SMS
- Haz clic en el enlace SMS acortado
- Recibir notificaciones push
- Recibir webhook
- Están inscritos en un grupo de control
- Ver ficha de contenido
- Haga clic en la tarjeta de contenido
- Descartar tarjeta de contenido

Así como los usuarios que completen las siguientes interacciones con las News Feed Cards activas:

- Visualizar
- Clic

## Normas de entrega

La función Conector de campaña sólo funciona con campañas activas. Además, no puedes utilizar el Conector de Campaña para enviar un mensaje a un usuario después de que haya completado una interacción con una campaña. Por ejemplo, si estás ejecutando una campaña de marketing durante nueve semanas y configuras una campaña de seguimiento que utiliza el Conector de Campaña al principio de la cuarta semana, la campaña de seguimiento sólo enviará mensajes a los usuarios que interactuaron con la campaña de marketing después de que se publicara la campaña de seguimiento (semanas 4-9). Por lo tanto, para asegurarse de que sus campañas de seguimiento llegan a todos los usuarios a los que se dirige, debería:

- Configura tu campaña original como borrador
- Configura y publica tu campaña de seguimiento
- Publicar la campaña original

Estas reglas de entrega son especialmente pertinentes si se dirige a usuarios que están inscritos en un grupo de control, reciben un correo electrónico o reciben una notificación push. Dado que los usuarios se incluirán en el grupo de control en cuanto publique la campaña original, debe publicar la campaña de seguimiento antes de publicar la campaña original. Del mismo modo, si publicas la campaña original antes que la campaña de seguimiento, muchos usuarios pueden recibir tu correo electrónico y/o notificación push antes de que se publique la campaña de seguimiento.

## Cómo utilizar la función Conector de campaña

### Paso 1: Crear una nueva campaña

Redacte los mensajes que desea enviar a sus usuarios. Puede seleccionar una campaña clásica o una campaña monocanal, en función de su caso de uso.

### Paso 2: Seleccione la interacción y la campaña de destino

Puede dirigirse a los usuarios que interactúan con una campaña activa o a los usuarios que interactúan con una tarjeta de noticias activa.

#### Dirigirse a los usuarios que interactúan con una campaña

Selecciona [Entrega basada en acciones][7] y añade el desencadenante "Interactuar con la campaña". A continuación, elija la interacción desencadenante. A continuación, seleccionarás la campaña activa a la que te gustaría dirigirte.

![][4]

#### Dirigirse a los usuarios que interactúan con una tarjeta de noticias (obsoleto)

Seleccione **Entrega basada en acciones** y añada el activador "Interactuar con tarjeta". A continuación, elija si desea dirigirse a los usuarios que ven una tarjeta de noticias o a los usuarios que hacen clic en una tarjeta de noticias. Selecciona la tarjeta de canal de noticias activa a la que quieras dirigirte.

![][5]

### Paso 3: Establece el retraso de la programación y añade excepciones si es necesario

Si decides establecer un retraso en la programación, puedes añadir una excepción a la acción desencadenante. Por ejemplo, es posible que desee reenviar una campaña de correo electrónico a usuarios que no abrieron el mensaje original.  En este caso, puede elegir "Correo electrónico recibido" como desencadenante y establecer un retraso de programación de una semana. A continuación, puede añadir "Abrir correo electrónico" como excepción. Ahora, volverá a enviar el correo electrónico a los usuarios que no abrieron el correo original en el plazo de una semana tras recibirlo.

![][6]

Los eventos de excepción sólo se activarán mientras un usuario esté esperando recibir el mensaje al que están asociados. Si un usuario realiza la acción antes de esperar el mensaje, el evento de excepción no se activará.

### Paso 4: Proceder a la creación de la campaña

Continúe creando su campaña como lo haría normalmente. Tenga en cuenta que si quiere asegurarse de que envía un mensaje a cada usuario que va a interactuar con una campaña específica, entonces lo mejor sería dirigirse a un segmento que contenga a todos los usuarios de su aplicación.

## Casos de uso

Puedes utilizar Campaign Connector para dirigirte a los usuarios que participan o no en las campañas activas.

Por ejemplo, puede seleccionar a los usuarios que han hecho clic en un mensaje push promocional que anunciaba un envío gratuito para enviarles un mensaje push promocional con un descuento del 15% en una compra.

O puedes hacer un seguimiento de los usuarios que han hecho clic en un vínculo profundo en un mensaje dentro de la aplicación de incorporación enviándoles otro mensaje dentro de la aplicación que destaque características adicionales.  De este modo, puede dirigirse a los usuarios que han demostrado estar interesados en conocer mejor las funciones de su aplicación y evitar molestar a los usuarios que prefieren descubrir estas funciones por sí mismos.

Campaign Connector también puede dirigirse a los usuarios que reciben una notificación push recordándoles que han abandonado su carrito. Por ejemplo, es posible que desee reenviar la notificación a los usuarios que no la abrieron directamente. Sin embargo, es probable que desee excluir a los usuarios que hayan realizado una compra desde que envió la notificación original, aunque no la hayan abierto directamente. Puede conseguir este caso de uso añadiendo un activador de "Notificación push recibida" para la campaña "Carrito abandonado", estableciendo un retraso de programación y añadiendo "Realiza compra" y "Notificaciones push abiertas directamente" como excepciones.

[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %}
[5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %}
[6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/