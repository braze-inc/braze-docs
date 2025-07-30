---
nav_title: Políticas de Puesta de Sol
article_title: Normas de expiración para el correo electrónico
page_order: 8
page_type: reference
description: "Este artículo aborda las mejores prácticas en torno a las políticas de suspensión y la comprensión de las situaciones en las que es mejor interrumpir los mensajes a los usuarios desvinculados."
channel: email

---

# Políticas de extinción

> Aunque tengas la tentación de enviar campañas a tantos usuarios como puedas, hay situaciones en las que es realmente ventajoso detener los mensajes a los usuarios que no participan. 

En el caso del correo electrónico, la IP de envío tiene una puntuación de reputación que tiene en cuenta la participación, los informes de spam, las listas de bloqueo, etc. Puedes utilizar herramientas como [Sender Score](https://www.senderscore.org/) o [el servicio de datos de red inteligente de Outlook](https://postmaster.live.com/snds/) para controlar tu puntuación de reputación. Si su puntuación de reputación es constantemente baja, los filtros de los ISP y de los buzones de correo podrían clasificar automáticamente sus correos electrónicos en una carpeta de spam o de baja prioridad para todos los destinatarios, incluso los comprometidos. Crear una política de suspensión ayuda a entregar tus correos electrónicos sólo a los destinatarios activos. 

Los filtros de segmentación ayudan a evitar que tus mensajes parezcan spam, ya que te permiten implementar fácilmente políticas de bloqueo para correos electrónicos, notificaciones push y notificaciones dentro de la aplicación. Aquí tienes algunas cosas que debes tener en cuenta cuando crees una política de extinción:

- ¿Qué se considera un usuario "no comprometido"? 
- ¿La participación se define por los clics, las compras, el uso de la aplicación o una combinación de estos comportamientos? 
- ¿Cuánto tiempo tiene que durar la falta de compromiso para que dejes de enviar mensajes?
- ¿Proporcionará campañas especiales a los usuarios antes de excluirlos de sus segmentos?
- ¿A qué canales de mensajería se aplicará tu política de extinción? 

Por ejemplo, si tiene usuarios que optan por [la protección de la privacidad del correo (MPP) de Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), considere cómo puede afectar esto a sus campañas de correo electrónico y a las métricas de entregabilidad, y determine cuál es la mejor manera de estructurar su política de suspensión.

Para incorporar políticas de bloqueo a tus campañas, crea un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) que excluya automáticamente a los usuarios que hayan marcado tus correos como spam o que no hayan interactuado con tus mensajes durante un determinado periodo de tiempo.  

Para configurar estos segmentos, elige los filtros `Has Marked You As Spam` y `Last Engaged With Message` que se encuentran en la sección **Reorientación**, en el desplegable de filtros. 

Cuando aplique el filtro `Last Engaged With Message`, especifique el tipo de mensajería (push, correo electrónico o notificación dentro de la aplicación) con la que el usuario ha interactuado o no, así como el número de días que han pasado desde la última vez que el usuario interactuó. Después de crear un segmento, elija dirigirse a este segmento con cualquier [canal de mensajería]({{site.baseurl}}/user_guide/message_building_by_channel/).

![Página de detalles del segmento con el filtro "Última interacción con el mensaje" seleccionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Aunque Braze detiene automáticamente el envío de correos electrónicos a los usuarios que te han marcado como spam, el filtro `Has Marked You As Spam` te permite también enviar a estos usuarios mensajes push dirigidos y notificaciones dentro de la aplicación. Este filtro es útil para [campañas de reorientación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Por ejemplo, puede enviar mensajes a los usuarios que no participan para recordarles las funciones y ofertas que se pierden por no abrir sus correos electrónicos.

Las políticas de caducidad pueden ser especialmente útiles en campañas de correo electrónico dirigidas a usuarios inactivos. Aunque estas campañas se centran en segmentos que no han interactuado con su aplicación durante un periodo de tiempo, pueden poner en peligro la capacidad de entrega de sus mensajes de correo electrónico si incluyen repetidamente destinatarios no comprometidos. Las políticas de extinción te permiten dirigirte a los usuarios inactivos sin que acaben en la carpeta de correo no deseado.

