---
nav_title: "Recopilación de adhesiones voluntarias de los usuarios"
article_title: Buenas prácticas para recopilar las adhesiones voluntarias de los usuarios de SMS
page_order: 7
description: "En este artículo de referencia se describen tres prácticas recomendadas para recopilar las adhesiones voluntarias de los usuarios."
page_type: reference
channel:
  - SMS
  
---

# Recopilación de adhesiones voluntarias de los usuarios

> En el siguiente artículo se enumeran algunos métodos habituales de adhesión voluntaria por SMS.

## Opción 1: Pide a los usuarios que envíen un SMS con tu código corto o código largo

Pide a los usuarios que envíen un mensaje de texto con las palabras "START", "UNSTOP", "YES" o una palabra clave personalizada de adhesión voluntaria a tu número para añadirlos automáticamente a tu grupo de suscripción. En tu sitio web, aplicación móvil o incluso publicidad, puedes solicitar a los usuarios que hagan esto para la adhesión voluntaria, y puedes ofrecer un incentivo si resulta útil.

## Opción 2: Adhesión voluntaria de los usuarios a través de un mensaje dentro de la aplicación

Para permitir que los usuarios se adhieran a los SMS desde un mensaje dentro de la aplicación, utiliza el [formulario de captura de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) proporcionado por Braze para crear un formulario de marca que te permita recopilar números de teléfono y hacer crecer tu lista de SMS.

![Creador de mensajes dentro de la aplicación con una plantilla para capturar números de teléfono.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recomienda que utilices también la característica de [doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Esta característica funciona automáticamente con el formulario de captura de números de teléfono para mensajes dentro de la aplicación, solicitando a los usuarios que confirmen su intención después de enviar su número de teléfono a través del formulario.

## Opción 3: Flujo de registro

Cuando un nuevo usuario se registre en el sitio web o la aplicación, pídele su número de teléfono y correo electrónico. Incluye una casilla para recibir correos electrónicos y SMS promocionales. 

Después de que el usuario se registre, haz lo siguiente:

1. Utiliza el [punto de conexión `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para crear el usuario y guardar sus atributos.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Utiliza el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para suscribir al usuario a SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
Para que los usuarios entren en el flujo de trabajo de [doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) al suscribirlos a través de la API REST, establece el parámetro `use_double_opt_in_logic` en `true` en tu solicitud. Si omites este parámetro, los usuarios se suscriben sin recibir una confirmación de doble adhesión voluntaria.

Este parámetro es compatible con los siguientes puntos de conexión:<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}