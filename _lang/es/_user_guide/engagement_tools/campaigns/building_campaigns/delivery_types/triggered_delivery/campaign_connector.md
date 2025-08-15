---
nav_title: Conector de campaña
article_title: Conector de campaña
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artículo explica qué es el Conector de Campaña y cómo utilizarlo para ofrecer contenido relevante y específico en el momento adecuado."

---
# Conector de campaña

> El conector de campañas te permite crear campañas que se desencadenan cuando los usuarios interactúan con las campañas activas. Puedes entregar contenido específico y relevante en el momento adecuado.

## Cómo funciona

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

### Normas de entrega

Ten en cuenta que no puedes utilizar el conector de campaña para enviar un mensaje a un usuario después de que haya completado una interacción con una campaña. Por ejemplo, si estás ejecutando una campaña de marketing durante nueve semanas y configuras una campaña de seguimiento que utilice el conector de campaña al principio de la cuarta semana, la campaña de seguimiento sólo entregará mensajes a los usuarios que hayan interactuado con la campaña de marketing después de que se haya publicado la campaña de seguimiento (semanas 4-9). Por lo tanto, para asegurarse de que sus campañas de seguimiento llegan a todos los usuarios a los que se dirige, debería:

- Configura tu campaña original como borrador
- Configura y publica tu campaña de seguimiento
- Publicar la campaña original

Estas reglas de entrega son especialmente pertinentes si se dirige a usuarios que están inscritos en un grupo de control, reciben un correo electrónico o reciben una notificación push. Dado que los usuarios se incluirán en el grupo de control en cuanto publique la campaña original, debe publicar la campaña de seguimiento antes de publicar la campaña original. Del mismo modo, si publicas la campaña original antes que la campaña de seguimiento, muchos usuarios pueden recibir tu correo electrónico y/o notificación push antes de que se publique la campaña de seguimiento.

## Utilizar el conector de campaña con tus campañas

### Paso 1: Crear una nueva campaña

Redacte los mensajes que desea enviar a sus usuarios. Puedes seleccionar una campaña monocanal o multicanal, según tu caso de uso.

### Paso 2: Seleccione la interacción y la campaña de destino

1. Selecciona [Entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) y añade el desencadenante "Interactuar con la campaña" para dirigirte a los usuarios que interactúan con una campaña activa. 
2. Elige la interacción desencadenante. 
3. A continuación, seleccionarás la campaña activa a la que te gustaría dirigirte.

![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Paso 3: Establece el retraso de la programación y añade excepciones (opcional)

Si decides establecer un retraso en la programación, puedes añadir una excepción a la acción desencadenante. Por ejemplo, es posible que desee reenviar una campaña de correo electrónico a usuarios que no abrieron el mensaje original.  En este caso, puede elegir "Correo electrónico recibido" como desencadenante y establecer un retraso de programación de una semana. A continuación, puede añadir "Abrir correo electrónico" como excepción. Ahora, volverá a enviar el correo electrónico a los usuarios que no abrieron el correo original en el plazo de una semana tras recibirlo.

![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Los eventos de excepción sólo se activarán mientras un usuario esté esperando recibir el mensaje al que están asociados. Si un usuario realiza la acción antes de esperar el mensaje, el evento de excepción no se activará.

### Paso 4: Proceder a la creación de la campaña

Continúe creando su campaña como lo haría normalmente. Tenga en cuenta que si quiere asegurarse de que envía un mensaje a cada usuario que va a interactuar con una campaña específica, entonces lo mejor sería dirigirse a un segmento que contenga a todos los usuarios de su aplicación.

## Casos de uso

Puedes utilizar Campaign Connector para dirigirte a los usuarios que participan o no en las campañas activas.

Por ejemplo, puede seleccionar a los usuarios que han hecho clic en un mensaje push promocional que anunciaba un envío gratuito para enviarles un mensaje push promocional con un descuento del 15% en una compra.

O puedes hacer un seguimiento de los usuarios que han hecho clic en un vínculo profundo en un mensaje dentro de la aplicación de incorporación enviándoles otro mensaje dentro de la aplicación que destaque características adicionales.  De este modo, puede dirigirse a los usuarios que han demostrado estar interesados en conocer mejor las funciones de su aplicación y evitar molestar a los usuarios que prefieren descubrir estas funciones por sí mismos.

Campaign Connector también puede dirigirse a los usuarios que reciben una notificación push recordándoles que han abandonado su carrito. Por ejemplo, es posible que desee reenviar la notificación a los usuarios que no la abrieron directamente. Sin embargo, es probable que desee excluir a los usuarios que hayan realizado una compra desde que envió la notificación original, aunque no la hayan abierto directamente. Puede conseguir este caso de uso añadiendo un activador de "Notificación push recibida" para la campaña "Carrito abandonado", estableciendo un retraso de programación y añadiendo "Realiza compra" y "Notificaciones push abiertas directamente" como excepciones.

