---
nav_title: "Acerca de SMS"
article_title: Acerca de SMS
page_order: 1
description: "Este artículo de referencia cubre casos generales de uso del canal SMS y los requisitos necesarios para ponerlo en marcha."
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Acerca de SMS

> En este artículo se exponen algunos casos de uso comunes, requisitos y términos que conviene conocer para facilitar la integración de SMS y permitir una comunicación eficaz y estratégica con los clientes.![Mensaje SMS con el texto "¡Bienvenido a Braze! Estamos encantados de tenerte a bordo. Consulte nuestra documentación para empezar. https://www.braze.com/docs/ Escriba HELP para obtener ayuda y STOP para parar."][picture]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

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
| Un número de teléfono específico (código corto o largo) | Un número de teléfono dedicado exclusivamente a una sola marca o anfitrión. | Braze se encarga de adquirir estos números por usted. Más información sobre [códigos cortos y largos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).|
| Lista de usuarios con números de teléfono | Antes de empezar a enviar mensajes, debes añadir usuarios a tu cuenta. Además, debes conocer el tamaño aproximado de tu audiencia.  | Los usuarios se añaden inicialmente a Braze a través de nuestro backend. Debe pasarnos esta lista para que la carguemos por usted. Los números de teléfono deben tener un formato de 10 dígitos, así como el prefijo del país. Más información sobre [números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [Palabras clave y respuestas de los SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Todas las palabras clave base deben tener respuestas atribuidas antes de poder empezar a enviar mensajes. | Deberá enumerarlas y enviarlas a su representante de Braze o al gestor de incorporación durante el proceso de incorporación. Ver [plantillas de palabras clave para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Términos que debe conocer

- **Código abreviado:** Un código de 5 a 6 dígitos, más corto que un número de teléfono completo. Este código se utiliza para direccionar y enviar mensajes SMS.<br><br>
- **Códigos largos:** Código de 10 dígitos que se utiliza para direccionar los mensajes SMS. La mayoría de los números de teléfono medios se consideran códigos largos (e.g 123-456-7891). Estos códigos se utilizan para direccionar y enviar mensajes SMS.<br><br>
- **Grupo de suscripción:** Una colección de números de teléfono de envío (como códigos cortos, códigos largos y/o ID alfanuméricos de remitente) que se utilizan para un tipo específico de propósito de mensajería. Por ejemplo, si una marca tiene previsto enviar mensajes SMS transaccionales y promocionales, deberá configurar dos grupos de suscripción con grupos separados de números de teléfono de envío en el panel de control de Braze.<br><br>
- **Límites de segmentos y caracteres del mensaje:** Un segmento de mensaje hace referencia al número de segmentos en que se dividirá su mensaje SMS inicial. Cada mensaje tiene un límite de caracteres que, si se sobrepasa, hará que el mensaje se divida en segmentos. En función de los estándares de codificación que utilices (UTF-2 o GSM-7), los límites de caracteres varían. Consulte nuestros [límites de copia de mensajes][2] para obtener más información sobre la segmentación de mensajes y los límites de caracteres de los mensajes.<br><br>
- **Métricas habituales de las campañas de SMS:** <br>*Enviados*, *Enviar al transportista*, *Fallo de entrega*, *Entrega confirmada*, *Rechazos*, *Exclusión* y *Ayuda*. <br>Para obtener información sobre éstas y otras métricas de SMS, consulta [Informes de SMS][1]. Tenga en cuenta que *el envío al transportista* está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tengan.

<br><br>

Para obtener una lista completa de términos, visita nuestros [Términos SMS que debes conocer]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/).

[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy
