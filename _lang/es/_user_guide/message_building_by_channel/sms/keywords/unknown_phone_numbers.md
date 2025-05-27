---
nav_title: Tratamiento de números de teléfono desconocidos
article_title: Tratamiento de números de teléfono SMS desconocidos
page_order: 4
description: "Este artículo de referencia explica cómo procesa Braze los números de teléfono SMS desconocidos de nuevos usuarios."
page_type: reference
channel:
  - SMS
  
---

# Tratamiento de números de teléfono desconocidos - nuevos usuarios

> Es posible que, después de poner en marcha los SMS con Braze, recibas mensajes de usuarios desconocidos. Los siguientes pasos describen cómo se procesan un usuario y un número no identificados.

{% alert important %}
¿Es usted actualmente un cliente no nativo de SMS? Si es así, visita la [documentación sobre SMS no nativos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) para consultar el artículo correspondiente sobre la gestión de números de teléfono desconocidos.
{% endalert %}

## Flujo de trabajo Opt-in/out y palabras clave personalizadas para números desconocidos

Braze se dirige automáticamente a un número desconocido de una de estas tres maneras:

1. Si se envía un mensaje de texto con una palabra clave:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Suscribe al usuario al grupo de suscripción correspondiente en función de la palabra clave de suscripción recibida por Braze.<br><br>
2. Si se envía una palabra clave de adhesión voluntaria:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Cancela la suscripción del usuario del grupo de suscripción correspondiente en función de la palabra clave de cancelación recibida por Braze.<br><br>
3. Si se escribe cualquier otra palabra clave personalizada:
  * Braze ignora el mensaje de texto y no hace nada.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164