---
nav_title: "Números de teléfono de usuario"
article_title: Números de teléfono de usuarios de WhatsApp
page_order: 1.5
description: "Este artículo de referencia trata sobre el formato de los números de teléfono de WhatsApp, cómo importar números de teléfono y cómo añadir usuarios a los grupos de suscripción de WhatsApp."
page_type: reference
channel: 
  - WhatsApp
  
---

# Números de teléfono de los usuarios

> Este artículo tratará diferentes temas en torno a los números de teléfono de sus usuarios o clientes.

Los números de teléfono se muestran en el perfil de usuario en formatos locales, pero no estarán en el formato que utilice para importar el número (`(724) 123 4567`).

## Importar números de teléfono

Puede importar números de teléfono [cargando un CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) o [a través de la API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) para crear un usuario.

### Formato

Es importante importar los números noU.S. en [`E.164`](https://en.wikipedia.org/wiki/e.164), incluyendo el "+" y el código de país. Cualquier número de teléfono que no se facilite en este formato se interpretará como un número estadounidense.  

Si un número de teléfono se fuerza en el formato E.164 pero no pasa la validación, Braze no podrá enviar mensajes de WhatsApp a este número. Los usuarios con números de teléfono no formateables saldrán automáticamente de un paso de Canvas que incluya WhatsApp

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

### Añadir usuarios a grupo de suscripción de WhatsApp

Para que un cliente reciba un mensaje de WhatsApp, debe tener un número de teléfono válido y estar incluido en un grupo de suscripción. Para más información, consulta los [grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).


### Varios usuarios con el mismo número de teléfono

Si varios usuarios tienen el mismo número de teléfono dentro de un segmento de una sola campaña o paso de Canvas, Braze deduplicará el envío y enviará un solo mensaje a ese único número de teléfono. 

[picture]: {% image_buster /assets/img/sms/e164.png %}

