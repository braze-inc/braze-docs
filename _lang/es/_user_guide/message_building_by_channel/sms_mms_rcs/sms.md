---
nav_title: "SMS"
article_title: Sobre SMS
page_order: 13
description: "Este artículo de referencia cubre casos generales de uso del canal SMS y los requisitos necesarios para ponerlo en marcha."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"} Acerca de los SMS

> ¡En este artículo se comparten algunos casos de uso comunes, requisitos y términos que debes conocer y que te ayudarán en tu integración de SMS y te permitirán comunicarte de forma eficaz y estratégica con tus clientes.\![Mensaje SMS con el texto "¡Bienvenido a Braze! Estamos encantados de tenerte a bordo. Consulta nuestra documentación para empezar. https://www.braze.com/docs/ Escribe AYUDA para obtener ayuda y STOP para detenerte".]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
El SMS, también conocido como servicio de mensajes cortos, se utiliza para enviar mensajes de texto a teléfonos móviles. Actualmente, se envían más de 23.000 millones de mensajes de texto al día en todo el mundo, y los SMS son la forma más directa de llegar a usuarios y clientes. Este uso generalizado y su valor demostrado han convertido a los SMS en una herramienta de marketing eficaz para empresas de todos los tamaños. 
<br><br>
## Posibles casos de uso

| Casos de uso | Explicación |
|---|---|
| Especialista en marketing general | Los mensajes SMS son una forma directa, flexible y eficaz de comunicar a tus clientes las próximas ofertas, las ventas favorables y los productos actuales o previstos. |
| Recordatorios | Los mensajes SMS pueden ser eficaces para notificar a los usuarios que han concertado una cita para un servicio. Por ejemplo, enviar un mensaje SMS recordando a un cliente la víspera de una cita con el médico ayudará a minimizar las citas perdidas, ahorrando tiempo y dinero tanto a ti como a tus clientes. |
| Mensajes de transacción | Los mensajes SMS son una forma eficaz de enviar notificaciones de transacciones, como confirmaciones de pedidos e información sobre envíos, proporcionándoles toda la información que necesitan en un único y cómodo lugar. Ten en cuenta que existen directrices legales que deben respetarse al enviar mensajes transaccionales. Si no estás seguro de estas directrices, ponte en contacto con tu equipo jurídico interno.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos

Antes de empezar a enviar SMS, necesitas algunas cosas. Consulta el siguiente cuadro para saber más.

|Requisito | Descripción | Adquisición |
|---|---|---|
| Un número de teléfono específico (un código abreviado o un código largo) | Un número de teléfono dedicado exclusivamente a una sola marca o anfitrión. | Braze se encarga de adquirir estos números por ti. Más información sobre [los códigos abreviados y largos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).|
| Lista de usuarios con números de teléfono | Antes de empezar a enviar mensajes, debes añadir usuarios a tu cuenta. Además, debes conocer el tamaño aproximado de tu audiencia.  | Los usuarios se añaden inicialmente a Braze a través de nuestro backend. Debes pasarnos esta lista para que la carguemos por ti. Los números de teléfono deben tener un formato de 10 dígitos, así como un código de área del país. Más información sobre [los números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| [Palabras clave y respuestas SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | Todas las palabras clave base deben tener atribuidas respuestas antes de que puedas empezar a enviar mensajes | Debes enumerarlas y enviarlas a tu representante Braze o administrador de incorporación durante el proceso de incorporación. Ver [plantillas de palabras clave para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Términos que debes conocer

Para obtener una lista completa de términos, visita nuestros [Términos]({{site.baseurl}}/sms_terms_to_know/) SMS [que debes conocer]({{site.baseurl}}/sms_terms_to_know/).

