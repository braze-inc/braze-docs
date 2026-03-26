---
nav_title: "Números de teléfono de los usuarios"
article_title: Números de teléfono de usuarios de SMS
page_order: 7
description: "Este artículo de referencia trata sobre el formato de los números de teléfono SMS, cómo importar números de teléfono y cómo añadir usuarios a grupos de suscripción SMS."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# Números de teléfono de los usuarios

> Este artículo tratará diferentes temas en torno a los números de teléfono de sus usuarios o clientes. Si busca información sobre sus propios números, vaya a nuestro artículo sobre el [envío de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Formato recomendado

Recomendamos importar los números de teléfono en[`E.164`](https://en.wikipedia.org/wiki/e.164)formato para garantizar la precisión en caso de que envíes mensajes a varias regiones con diferentes códigos de país o área, incluso para números de teléfonoU.S basados en .

- **U.S. números:** Todos los números de U.S. deben ser números de teléfono válidos de 10 dígitos con un prefijo válido. Si a algún número de teléfono de 10 dígitos le falta el prefijo`+`  y el código de país, Braze lo mapeará como U.S. números.
- **Números internacionales:** Todos los números internacionales deben comenzar con un `+`, seguido del código del país y luego el número de teléfono. Por ejemplo, `+442071838750`.

![Ejemplo de un número de teléfono internacional e164 válido.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

A continuación se muestran algunos ejemplos que ilustran las diferencias entre la localización y`E.164`el formato global:

| País | Local | Código del país | `E.164` |
|---|---|---|---|
| EE. UU. | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importar números de teléfono

Al importar números de teléfono, es importante que sigas el [formato recomendado](#recommended-format). Para importar números de teléfono, utiliza uno de los siguientes métodos:

- [Subir un archivo CSV a Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Uso del`/users/track`  punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Los números de teléfono de los usuarios aparecen en Braze como una cadena de dígitos. Si importas un número que contiene caracteres no numéricos (como `,`, `-`, o `(`) distintos del {% raw %}`+`{% endraw %}, los caracteres no numéricos se eliminan al representarse en Braze. Por ejemplo, importar`+1 (724) 123-4567`aparece como `+17241234567`.
{% endalert %}

## Tratamiento de números de teléfono no válidos

Cuando un número de teléfono se considere inválido, Braze marcará el número de teléfono del usuario como inválido y no intentará enviar más comunicaciones a ese número de teléfono. Un número de teléfono no válido se marca en la **pestaña Compromiso** del perfil de un usuario.

![Ejemplo de mensaje de error por números de teléfono no válidos en Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Un número de teléfono se considera inválido por las siguientes razones:

- **Error del proveedor**: se ha recibido un error permanente del proveedor de SMS y RCS. Esto indica que el número de teléfono proporcionado tiene un formato incorrecto o que no puede recibir mensajes SMS o RCS de forma permanente.
- **Desactivado**: el número de teléfono ha sido desactivado debido a que un abonado de telefonía móvil ha dado de baja su servicio y ha liberado su número de su operador (y eventualmente puede ser reciclado y asignado a un nuevo usuario).

Estos números de teléfono no válidos se pueden administrar mediante [terminales SMS y RCS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Si varios perfiles de usuario tienen el mismo número de teléfono y ese número de teléfono está marcado como no válido, todos los perfiles de usuario existentes con ese número se mostrarán como no válidos. Los perfiles de usuario recién creados nunca se marcarán inicialmente como no válidos.
{% endalert %}

También puede incluir o excluir a los usuarios con números de teléfono no válidos al [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

## Añadir usuarios a grupos de suscripción SMS y RCS

Para que un usuario pueda recibir un mensaje SMS o RCS, debe tener un número de teléfono válido y tener una adhesión voluntaria a un grupo de suscripción. Los grupos de suscripción están vinculados al programa SMS o RCS que estés ejecutando (asegúrate de cumplir con los [requisitos legales para SMS, MMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) y de haber registrado el consentimiento de cada cliente). Para obtener más información, consulta [Grupos de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) a [SMS y RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Abastecimiento y verificación por terceros

Braze se basa en herramientas de terceros para obtener números no válidos. Braze no se hace responsable de las interrupciones o la información errónea de estos servicios. Por lo tanto, no se debe confiar en esta herramienta como único método de cumplimiento para verificar los números no válidos.
