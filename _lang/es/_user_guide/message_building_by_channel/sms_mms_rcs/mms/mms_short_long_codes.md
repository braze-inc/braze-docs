---
nav_title: "Códigos MMS cortos y largos"
article_title: Códigos MMS cortos y largos
page_order: 1
description: "Este artículo de referencia cubre las diferencias entre los códigos cortos y largos de SMS y MMS."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# Códigos MMS cortos y largos

> Tanto los MMS como los SMS están vinculados al canal Braze SMS. Para acceder a MMS en su cuenta se requiere la compra de SMS para aquellos que aún no han comprado el acceso. Los clientes actuales de SMS pueden acceder a MMS tras adquirirlo. 

Actualmente, se admiten MMS para códigos abreviados de EE. UU. (números de 5-6 dígitos), códigos largos de EE. UU. y CA (números de 10 dígitos) y números de cliente de EE. UU. y Canadá. Es posible enviar MMS a números de fuera de EE.UU./Canadá, pero los mensajes MMS se convertirán en un mensaje SMS con un enlace al activo multimedia. Para más información, consulte [Códigos cortos y largos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Códigos cortos MMS

Es posible que algunos usuarios no implanten o utilicen los códigos cortos MMS, pero estarán disponibles si se necesitan más adelante.

Para los usuarios que obtuvieron sus códigos abreviados antes de que Braze admitiera MMS, todos los clientes existentes con códigos abreviados de EE. UU. son elegibles para habilitar MMS al instante. Ponte en contacto con tu administrador del éxito del cliente si te encuentras en esta situación y deseas habilitar el MMS.

{% alert important %}
Cuando se habilitan los MMS para códigos cortos que anteriormente no los tenían habilitados, puede ser necesario volver a aprobar los códigos cortos en un proceso de aprobación que puede llevar semanas. Es importante tener en cuenta este momento cuando decidas habilitar el MMS.
{% endalert %}

### Mejores prácticas para códigos cortos MMS

- En Braze, recomendamos encarecidamente mantener separados los mensajes transaccionales y promocionales, cada uno con códigos cortos diferentes. Como el MMS está vinculado al canal SMS, y el canal SMS está muy regulado, los clientes pueden verse obligados a pagar una sanción económica por hacer un mal uso del canal y ver suspendido su código corto (lo que es irreversible). Mantener la mensajería transaccional y promocional vinculada a códigos cortos diferentes salvaguarda su mensajería transaccional.
- Si los clientes ya tienen un código corto dedicado a la mensajería promocional, y está habilitado para MMS, no necesitan otro código corto para MMS.

## Códigos largos MMS

Los clientes pueden enviar MMS con códigos largos. Para ello, debes asegurarte de que tus códigos largos están habilitados para MMS. Esto puede hacerse inicialmente durante la configuración, o más tarde desde tu cuenta. 

Tenga en cuenta que nuestros mensajes MMS no pueden enviarse con un ID de remitente alfanumérico. Para saber más sobre los ID alfanuméricos, consulta [ID de remitente alfanumérico]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
