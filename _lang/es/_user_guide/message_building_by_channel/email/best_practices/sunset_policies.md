---
nav_title: Políticas de extinción
article_title: Políticas de extinción para el correo electrónico
page_order: 8
page_type: reference
description: "Este artículo trata de las mejores prácticas en torno a las políticas de extinción y la comprensión de las situaciones en las que es mejor interrumpir los mensajes a los usuarios desvinculados."
channel: email

---

# Políticas de extinción

> Aunque tengas la tentación de enviar campañas a todos los usuarios que puedas, hay situaciones en las que es realmente ventajoso dejar de enviar mensajes a los usuarios desvinculados. 

Para los correos electrónicos, tu IP de envío tiene una puntuación de reputación que tiene en cuenta la interacción, los informes de correos no deseados, las listas de bloqueo, etc. Puedes utilizar herramientas como [Sender Score](https://www.senderscore.org/) o [el servicio de datos de red inteligente de Outlook](https://postmaster.live.com/snds/) para controlar tu puntuación de reputación. Si tu puntuación de reputación es sistemáticamente baja, los filtros de los ISP y de los buzones de correo podrían clasificar automáticamente tus correos electrónicos en una carpeta de correo no deseado o de baja prioridad para todos los destinatarios, incluso para los comprometidos. Crear una política de suspensión ayuda a entregar tus correos electrónicos sólo a los destinatarios activos. 

Los filtros de segmentación te ayudan a evitar que tu mensajería parezca correo no deseado, permitiéndote aplicar fácilmente políticas de segmentación para correos electrónicos, notificaciones push y notificaciones dentro de la aplicación. Aquí tienes algunas cosas que debes tener en cuenta cuando crees una política de extinción:

- ¿Qué se considera un usuario "no comprometido"? 
- ¿La interacción se define por los clics, las compras, el uso de la aplicación o una combinación de estos comportamientos? 
- ¿Cuánto tiempo tiene que durar la falta de interacción para que dejes de enviar mensajes?
- ¿Vas a entregar alguna campaña especial a los usuarios antes de excluirlos de tus segmentos?
- ¿A qué canales de mensajería se aplicará tu política de extinción? 

Por ejemplo, si tienes usuarios que optan por la [Protección de la privacidad en los correos electrónicos (MPP) de Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), considera cómo puede afectar esto a tus campañas de correo electrónico y a las métricas de capacidad de entrega, y determina cuál es la mejor forma de estructurar tu política de extinción.

Para incorporar políticas de extinción en tus campañas, crea un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) que excluya automáticamente a los usuarios que hayan marcado tus correos electrónicos como spam o que no hayan interactuado con un tus mensajes durante un determinado periodo de tiempo.  

Para configurar estos segmentos, elige los filtros `Has Marked You As Spam` y `Last Engaged With Message` que se encuentran en la sección **Reorientar**, en el desplegable de filtros. 

Cuando apliques el filtro `Last Engaged With Message`, especifica el tipo de mensajería (push, correo electrónico o notificación dentro de la aplicación) con la que el usuario ha interactuado o no, así como el número de días que han pasado desde la última vez que el usuario interactuó. Después de crear un segmento, elige dirigirte a este segmento con cualquier [canal de mensajería]({{site.baseurl}}/user_guide/message_building_by_channel/).

\![Página de detalles del segmento con el filtro "Última interacción con el mensaje" seleccionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Mientras que Braze detiene automáticamente el envío por correo electrónico a los usuarios que te han marcado como spam, el filtro `Has Marked You As Spam` te permite también enviar a estos usuarios mensajes push dirigidos y notificaciones dentro de la aplicación. Este filtro es útil para [campañas de reorientación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Por ejemplo, puedes enviar a los usuarios no comprometidos mensajes que les recuerden las características y ofertas que se están perdiendo cuando no abren tus correos electrónicos.

Las políticas de caducidad pueden ser especialmente útiles en campañas de correo electrónico dirigidas a usuarios caducados. Aunque estas campañas se centran en segmentos que no han interactuado con tu aplicación durante un periodo de tiempo, pueden poner en peligro la capacidad de entrega de tus correos electrónicos si incluyen repetidamente destinatarios no comprometidos. Las políticas de extinción te permiten dirigirte a los usuarios rezagados sin que acaben en la carpeta de correo no deseado.

