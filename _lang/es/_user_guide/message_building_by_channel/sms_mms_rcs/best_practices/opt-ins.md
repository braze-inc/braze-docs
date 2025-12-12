---
nav_title: "Recoger las adhesiones voluntarias de los usuarios"
article_title: Buenas prácticas para recoger las adhesiones voluntarias de los usuarios a los SMS
page_order: 7
description: "Este artículo de referencia cubre tres buenas prácticas para recopilar las adhesiones voluntarias de los usuarios."
page_type: reference
channel:
  - SMS
  
---

# Recoger las adhesiones voluntarias de los usuarios

> En el siguiente artículo se enumeran algunos métodos habituales de adhesión voluntaria por SMS.

## Opción 1: Pide a los usuarios que envíen por SMS tu código abreviado o largo

Pide a los usuarios que envíen por SMS "INICIAR", "DETENER", "SÍ" o una palabra clave de adhesión voluntaria personalizada a tu número para añadirlos automáticamente a tu grupo de suscripción. En tu sitio web, aplicación móvil o incluso publicidad, puedes pedir a los usuarios que hagan esto para la adhesión voluntaria, y puedes ofrecer un incentivo si resulta útil.

## Opción 2: Adhesión voluntaria de los usuarios mediante mensaje dentro de la aplicación

Para permitir que los usuarios opten por recibir SMS desde un mensaje dentro de la aplicación, utiliza el [formulario de captura de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) proporcionado por Braze para crear un formulario de marca que te permita recopilar números de teléfono y hacer crecer tu lista de SMS.

Creador de mensajes dentro de la aplicación con una plantilla para capturar números de teléfono.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recomienda que utilices también la característica [de doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Esta característica funciona automáticamente con el formulario de captura del número de teléfono del mensaje dentro de la aplicación, pidiendo a los usuarios que confirmen su intención después de enviar su número de teléfono a través del formulario.

## Opción 3: Flujo de registro

Cuando un nuevo usuario se da de alta o se registra en el sitio web o en la aplicación, pídele su número de teléfono y su correo electrónico. Incluye una casilla para recibir correos electrónicos promocionales y SMS. 

Después de que el usuario se registre, haz lo siguiente:

1. Utiliza el [punto final`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para crear el usuario y guardar sus atributos.

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
2\. Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para suscribir al usuario a SMS.

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

