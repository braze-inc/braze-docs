---
nav_title: Conector de campaña
article_title: Conector de campaña
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artículo explica qué es el conector de campaña y cómo utilizarlo para entregar contenido específico y relevante en el momento adecuado."

---
# Conector de campaña

> El conector de campañas te permite crear campañas que se desencadenan cuando los usuarios interactúan con las campañas activas. Puedes entregar contenido específico y relevante en el momento adecuado.

## Cómo funciona

Esta característica te permite dirigirte a usuarios que completen las siguientes interacciones con campañas activas:

- Ver mensaje dentro de la aplicación
- Haz clic en el mensaje dentro de la aplicación
- Haz clic en los botones de mensajes dentro de la aplicación
- Haz clic en correo electrónico
- Haz clic en alias en el correo electrónico
- Abrir correo electrónico
- Abrir directamente la notificación push
- Haz clic en el botón de notificación push
- Haz clic en la página de historias push
- Realizar evento de conversión
- Recibir correo electrónico
- Recibir SMS
- Haz clic en el enlace SMS acortado
- Recibir notificación push
- Recibir webhook
- Están inscritos en un grupo de control
- Ver tarjeta de contenido
- Haz clic en la tarjeta de contenido
- Descartar tarjeta de contenido

{% alert important %}
Los activadores del conector de campaña no pueden utilizarse para activar campañas de mensajes dentro de la aplicación. Los mensajes dentro de la aplicación sólo pueden activarse mediante eventos SDK, como eventos personalizados o el inicio de sesión. Para más información, consulta [Crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).
{% endalert %}

### Normas de entrega

Ten en cuenta que no puedes utilizar el conector de campaña para enviar un mensaje a un usuario después de que haya completado una interacción con una campaña. Por ejemplo, si estás ejecutando una campaña de marketing durante nueve semanas y configuras una campaña de seguimiento que utilice el conector de campaña al principio de la cuarta semana, la campaña de seguimiento sólo entregará mensajes a los usuarios que hayan interactuado con la campaña de marketing después de que se haya publicado la campaña de seguimiento (semanas 4-9). Por tanto, para asegurarte de que tus campañas de seguimiento llegan a todos los usuarios a los que te diriges, debes

- Configura tu campaña original como borrador
- Configura y publica tu campaña de seguimiento
- Publica la campaña original

Estas reglas de entrega son especialmente pertinentes si te diriges a usuarios que están inscritos en un grupo de control, reciben un correo electrónico o reciben una notificación push. Como los usuarios se inscribirán en el grupo de control en cuanto publiques la campaña original, debes publicar la campaña de seguimiento antes de publicar la campaña original. Del mismo modo, si publicas la campaña original antes que la campaña de seguimiento, muchos usuarios pueden recibir tu correo electrónico y/o notificación push antes de que se publique la campaña de seguimiento.

## Utilizar el conector de campaña con tus campañas

### Paso 1: Crear una nueva campaña

Redacta los mensajes que quieras enviar a tus usuarios. Puedes seleccionar una campaña monocanal o multicanal, según tu caso de uso.

### Paso 2: Selecciona la interacción y la campaña objetivo

1. Selecciona [Entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) y añade el desencadenante "Interactuar con la campaña" para dirigirte a los usuarios que interactúan con una campaña activa. 
2. Elige la interacción desencadenante. 
3. A continuación, seleccionarás la campaña activa a la que te gustaría dirigirte.

\![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Paso 3: Establece el retraso de la programación y añade excepciones (opcional)

Si decides establecer un retraso en la programación, puedes añadir una excepción a la acción desencadenante. Por ejemplo, puede que quieras reenviar una campaña de correo electrónico a usuarios que no abrieron el correo electrónico original.  En este caso, puedes elegir "Correo electrónico recibido" como desencadenante y establecer un retraso de programación de una semana. Entonces, puedes añadir "Abrir correo electrónico" como excepción. Ahora, volverás a enviar el correo electrónico a los usuarios que no abrieron el correo electrónico original en el plazo de una semana desde que lo recibieron.

\![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Los eventos de excepción sólo se desencadenarán mientras un usuario esté esperando recibir el mensaje al que están asociados. Si un usuario realiza la acción antes de esperar el mensaje, no se desencadenará el evento de excepción.

### Paso 4: Proceder a la creación de la campaña

Continúa creando tu campaña como lo harías normalmente. Ten en cuenta que si quieres asegurarte de que envías un mensaje a todos los usuarios que van a interactuar con una campaña específica, entonces lo mejor sería dirigirte a un segmento que contenga a todos los usuarios de tu aplicación.

## Casos de uso

Puedes utilizar el Conector de Campaña para dirigirte a los usuarios que participan o no en las campañas activas.

Por ejemplo, puedes dirigirte a los usuarios que han hecho clic en un mensaje push promocional que anunciaba un envío gratuito para enviarles un mensaje push promocional que anuncie un 15% de descuento en una compra.

El conector de campaña también puede dirigirse a usuarios que reciben una notificación push recordándoles que han abandonado su carrito. Por ejemplo, puede que quieras reenviar la notificación a usuarios que no la abrieron directamente. Sin embargo, es probable que quieras excluir a los usuarios que hayan realizado una compra desde que enviaste la notificación original, aunque no la hayan abierto directamente. Puedes conseguir este caso de uso añadiendo un desencadenante de "Notificación push recibida" para la campaña "Carrito abandonado", configurando un retraso en la programación y añadiendo "Realiza compra" y "Notificaciones push de apertura directa" como excepciones.

