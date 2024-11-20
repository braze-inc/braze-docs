---
nav_title: Tratamiento de números de teléfono desconocidos
article_title: Tratamiento de números de teléfono desconocidos
description: "Este artículo de referencia explica cómo Braze gestionará los números de teléfono desconocidos de los usuarios de WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Tratamiento de números de teléfono desconocidos

> Es posible que, después de poner en marcha WhatsApp con Braze, reciba mensajes de usuarios desconocidos. Los siguientes pasos describen cómo se procesan un usuario y un número no identificados.

## Flujo de trabajo Opt-in/out y palabras clave personalizadas para números desconocidos

Braze intentará primero encontrar un usuario con un número coincidente. Si no se encuentra ninguno, Braze se dirige automáticamente a un número desconocido de una de estas dos maneras:

1. **Si se configura una palabra desencadenante con una [adhesión voluntaria Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/):**
- Braze crea un perfil anónimo
- Asignamos un alias de usuario al perfil con los siguientes datos:
  - Un `alias_name` cuyo valor es el número de teléfono proporcionado por el usuario
  - Un `alias_label` con el valor `phone`
- Nuestro sistema establece el atributo de teléfono
- El usuario se suscribe al grupo de suscripción correspondiente en función de la lógica establecida en el Canvas.<br><br>
2. **Si no se ha configurado ningún lienzo de inclusión voluntaria:**
- Braze crea un perfil anónimo
- Asignamos un alias de usuario al perfil con los siguientes datos:
  - Un `alias_name` cuyo valor es el número de teléfono proporcionado por el usuario
  - Un `alias_label` con el valor `phone`
- Nuestro sistema establece el atributo de teléfono
- El estado de suscripción del usuario será por defecto `unsubscribed` para todos los grupos de suscripción de WhatsApp<br><br>

