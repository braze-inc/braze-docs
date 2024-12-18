---
nav_title: "Números de teléfono de usuario"
article_title: Números de teléfono de usuarios de SMS
page_order: 1
description: "Este artículo de referencia trata sobre el formato de los números de teléfono SMS, cómo importar números de teléfono y cómo añadir usuarios a grupos de suscripción SMS."
page_type: reference
channel: 
  - SMS
  
---

# Números de teléfono de los usuarios

> Este artículo tratará diferentes temas en torno a los números de teléfono de sus usuarios o clientes. Si busca información sobre sus propios números, vaya a nuestro artículo sobre el [envío de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).

Los números de teléfono se muestran en el perfil de usuario en formatos locales, pero no estarán en el formato que utilice para importar el número (`(724) 123 4567`).

## Importar números de teléfono

Puede importar números de teléfono cargando un [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) o a través de [la API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) para crear un usuario.

### Formato

Como práctica recomendada, la mejor forma de importar un número de teléfono es en formato [`E.164`](https://en.wikipedia.org/wiki/e.164). No obstante, Braze intentará interpretar o convertir cualquier número de U.S. lo mejor que pueda.

Todos los números de U.S. deben ser números de teléfono válidos de 10 dígitos con un prefijo válido. Pueden introducirse sin `+` ni el código de país, ya que Braze asumirá y asignará todos los números de teléfono válidos de 10 dígitos como números U.S.

Todos los números internacionales deben empezar por `+`, seguido del prefijo del país y, a continuación, el número de teléfono. (e.g `+442071838750`)

![][picture]{: style="max-width:50%;border: 0;"}

Sin embargo, para garantizar la precisión en caso de que envíe a varias regiones con diferentes códigos de país o de área, se recomienda utilizar el formato `E.164`, incluso para los números de teléfono basados en U.S.

En la siguiente tabla puede ver las diferencias entre el formato local de los números y el formato universal `E.164`:

| País | Local | Código del país | `E.164` |
|---|---|---|---|
| EE. UU. | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Añadir usuarios a grupos de suscripción SMS

Para que un cliente reciba un mensaje SMS, debe tener un número de teléfono válido y estar incluido en un grupo de suscripción. Los grupos de suscripción están vinculados al programa de SMS que estés ejecutando (asegúrate de cumplir los [requisitos legales para los SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) y de haber registrado el consentimiento de cada cliente). Para más información, consulta [Grupos de suscripción por SMS][1]. 

### Tratamiento de números de teléfono no válidos

Cuando un número de teléfono se considere inválido, Braze marcará el número de teléfono del usuario como inválido y no intentará enviar más comunicaciones a ese número de teléfono. Un número de teléfono no válido se marca en la **pestaña Compromiso** del perfil de un usuario.

![][picture2]{: style="max-width:50%;border: 0;"}

Un número de teléfono se considera inválido por las siguientes razones:
- **Error del proveedor**: se ha recibido un error permanente del proveedor de SMS. Esto indica que el número de teléfono suministrado tiene un formato incorrecto o no puede recibir mensajes SMS de forma permanente.
- **Desactivado**: el número de teléfono ha sido desactivado debido a que un abonado de telefonía móvil ha dado de baja su servicio y ha liberado su número de su operador (y eventualmente puede ser reciclado y asignado a un nuevo usuario).

Estos números de teléfono no válidos pueden gestionarse mediante [terminales SMS]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
Si varios perfiles de usuario tienen el mismo número de teléfono y ese número de teléfono está marcado como no válido, todos los perfiles de usuario existentes con ese número se mostrarán como no válidos. Los perfiles de usuario recién creados nunca se marcarán inicialmente como no válidos.
{% endalert %}

También puede incluir o excluir a los usuarios con números de teléfono no válidos al [crear un segmento][2]. 

### Abastecimiento y verificación por terceros

Braze se basa en herramientas de terceros para obtener números no válidos. Braze no se hace responsable de las interrupciones o la información errónea de estos servicios. Por lo tanto, no se debe confiar en esta herramienta como único método de cumplimiento para verificar los números no válidos.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}
[picture2]: {% image_buster /assets/img/sms/invalid_banner.png %}
