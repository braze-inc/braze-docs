---
nav_title: "Códigos abreviados y largos MMS"
article_title: Códigos abreviados y largos de MMS
page_order: 1
description: "Este artículo de referencia cubre las diferencias entre códigos abreviados y códigos largos de SMS y MMS."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# Códigos abreviados y largos MMS

> Tanto los MMS como los SMS están vinculados al canal SMS de Braze. Para acceder a MMS en tu cuenta se requiere la compra de SMS para aquellos que aún no hayan comprado el acceso. Los clientes actuales de SMS pueden acceder a MMS después de comprarlo. 

Actualmente se admiten MMS para códigos abreviados de EE.UU. (números de 5-6 dígitos), códigos largos de EE.UU. y CA (números de 10 dígitos) y números de cliente de EE.UU. y Canadá. Es posible enviar MMS a números de fuera de EE.UU./Canadá, pero los mensajes MMS se convertirán en un mensaje SMS con un enlace al activo multimedia. Para saber más, consulta [Códigos abreviados y códigos largos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Códigos abreviados MMS

Puede que algunos usuarios no implementen o utilicen códigos abreviados MMS, pero estarán disponibles si se necesitan más adelante.

Para los usuarios que obtuvieron sus códigos abreviados antes de que Braze admitiera MMS, todos los clientes existentes con códigos abreviados estadounidenses son elegibles para habilitar MMS al instante. Ponte en contacto con tu administrador del éxito del cliente si te encuentras en esta situación y deseas habilitar el MMS.

{% alert important %}
Al habilitar el MMS para códigos abreviados que anteriormente no tenían habilitado el MMS, es posible que haya que volver a aprobar los códigos abreviados en un proceso de aprobación que podría llevar semanas. Es importante tener en cuenta este momento cuando decidas habilitar el MMS.
{% endalert %}

### Mejores prácticas de código abreviado MMS

- En Braze, recomendamos encarecidamente mantener separados los mensajes de transacción y de mensajería promocional, cada uno con códigos abreviados diferentes. Como el MMS está vinculado al canal SMS, y el canal SMS está muy regulado, los clientes pueden tener que pagar una sanción económica por hacer un mal uso del canal y ver suspendido su código abreviado (lo que es irreversible). Mantener la mensajería transaccional y promocional vinculada a códigos abreviados diferentes salvaguarda su mensajería transaccional.
- Si los clientes ya tienen un código abreviado dedicado a la mensajería promocional, y está habilitado para MMS, no necesitan otro código abreviado para MMS.

## Códigos largos MMS

Los clientes pueden enviar MMS con códigos largos. Para ello, debes asegurarte de que tus códigos largos están habilitados para MMS. Esto puede hacerse inicialmente durante la configuración, o más tarde desde tu cuenta. 

Ten en cuenta que nuestros mensajes MMS no pueden enviarse con un ID de remitente alfanumérico. Para saber más sobre los ID [alfanuméricos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id), consulta [ID de remitente alfanumérico]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
