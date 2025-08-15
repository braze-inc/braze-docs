---
nav_title: "Recopilación de la adhesión voluntaria de los usuarios"
article_title: Buenas prácticas para recopilar las preferencias de adhesión voluntaria de los usuarios de SMS
page_order: 7
description: "En este artículo de referencia se describen tres prácticas recomendadas para recopilar las preferencias de adhesión voluntaria de los usuarios."
page_type: reference
channel:
  - SMS
  
---

# Recopilación de preferencias de adhesión voluntaria de los usuarios

> En el siguiente artículo se enumeran algunos métodos de adhesión voluntaria por SMS habituales.

## Opción 1: Pide a los usuarios que envíen un SMS con tu código corto o largo

Pida a los usuarios que envíen un mensaje de texto con las palabras "START", "UNSTOP", "YES" o una palabra clave personalizada a su número para añadirlos automáticamente a su grupo de suscripción. En su sitio web, aplicación móvil o incluso publicidad, puede solicitar a los usuarios que hagan esto para registrarse, y puede ofrecer un incentivo si resulta útil.

## Opción 2: Adhesión voluntaria de los usuarios a través de un mensaje dentro de la aplicación

Para permitir que los usuarios opten por los SMS desde un mensaje de la aplicación, utiliza el [formulario de captura de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) proporcionado por Braze para crear un formulario de marca que te permita recopilar números de teléfono y hacer crecer tu lista de SMS.

![Creador de mensajes dentro de la aplicación con una plantilla para la captura de números de teléfono.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recomienda que utilices también la característica [de doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Esta función funciona automáticamente con el formulario de captura de números de teléfono para mensajes dentro de la aplicación, solicitando a los usuarios que confirmen su intención después de enviar su número de teléfono a través del formulario.

## Opción 3: Flujo de inscripción

Cuando un nuevo usuario se registre en el sitio web o la aplicación, pídale su número de teléfono y correo electrónico. Incluya una casilla para recibir correos electrónicos y SMS promocionales. 

Después de que el usuario se registre, haz lo siguiente:

1. Utilice el [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para crear el usuario y guardar sus atributos.

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\. Utiliza el [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para suscribir al usuario a SMS.

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

