---
nav_title: "Acerca de SMS"
article_title: Acerca de SMS
page_order: 1
description: "Este artículo de referencia cubre casos generales de uso del canal SMS y los requisitos necesarios para ponerlo en marcha."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Acerca de SMS

> En este artículo se exponen algunos casos de uso comunes, requisitos y términos que conviene conocer para facilitar la integración de SMS y permitir una comunicación eficaz y estratégica con los clientes.![Mensaje SMS con el texto "¡Bienvenido a Braze! Estamos encantados de tenerte a bordo. Consulta nuestra documentación para empezar. https://www.braze.com/docs/ Escribe AYUDA para obtener ayuda y PARAR para detenerte."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
Los SMS, también conocidos como Short Message Service, se utilizan para enviar mensajes de texto a teléfonos móviles. Actualmente, se envían más de 23.000 millones de mensajes de texto al día en todo el mundo, y los SMS son la forma más directa de llegar a usuarios y clientes. Su uso generalizado y su valor demostrado han convertido a los SMS en una eficaz herramienta de marketing para empresas de todos los tamaños. 
<br><br>
## Posibles casos de uso

| Casos de uso | Explicación |
|---|---|
| Marketing general | Los mensajes SMS son una forma directa, flexible y eficaz de comunicar a sus clientes las próximas ofertas, las ventas favorables y los productos actuales o previstos. |
| Recordatorios | Los mensajes SMS pueden ser eficaces para notificar a los usuarios que han concertado una cita para un servicio. Por ejemplo, enviar un mensaje SMS recordando a un cliente la víspera de una cita con el médico ayudará a minimizar las citas perdidas, ahorrándole tiempo y dinero tanto a usted como a sus clientes. |
| Mensajes transaccionales | Los mensajes SMS son una forma eficaz de enviar notificaciones de transacciones, como confirmaciones de pedidos e información sobre envíos, proporcionándoles toda la información que necesitan en un único y cómodo lugar. Tenga en cuenta que existen directrices legales que deben respetarse al enviar Mensajes Transaccionales. Si no está seguro de estas directrices, póngase en contacto con su equipo jurídico interno.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos

Antes de empezar a enviar SMS, necesitas algunas cosas. Consulte el siguiente cuadro para obtener más información.

|Requisito | Descripción | Adquisición |
|---|---|---|
| Un número de teléfono específico (código corto o largo) | Un número de teléfono dedicado exclusivamente a una sola marca o anfitrión. | Braze se encarga de adquirir estos números por usted. Más información sobre [códigos cortos y largos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).|
| Lista de usuarios con números de teléfono | Antes de empezar a enviar mensajes, debes añadir usuarios a tu cuenta. Además, debes conocer el tamaño aproximado de tu audiencia.  | Los usuarios se añaden inicialmente a Braze a través de nuestro backend. Debe pasarnos esta lista para que la carguemos por usted. Los números de teléfono deben tener un formato de 10 dígitos, así como el prefijo del país. Más información sobre [números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| [Palabras clave y respuestas de los SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | Todas las palabras clave base deben tener respuestas atribuidas antes de poder empezar a enviar mensajes. | Deberá enumerarlas y enviarlas a su representante de Braze o al gestor de incorporación durante el proceso de incorporación. Ver [plantillas de palabras clave para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Términos que debe conocer

Para obtener una lista completa de términos, visita nuestros [Términos SMS que debes conocer]({{site.baseurl}}/sms_terms_to_know/).

