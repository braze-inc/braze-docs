---
nav_title: Usuarios anónimos
article_title: Usuarios anónimos
page_order: 0
page_type: reference
description: "Este artículo ofrece un resumen de los usuarios anónimos y los alias de usuario, destacando su importancia y cómo pueden aprovecharse en tus mensajes."

---

# Usuarios anónimos

> Los usuarios que visitan tu sitio web o aplicación sin iniciar sesión, como un visitante invitado, son reconocidos como usuarios anónimos. Estos usuarios no tienen `external_ids`, que se utilizan para actualizar los perfiles de usuario con la API de Braze, pero siguen teniendo [puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) asignados y pueden ser incluidos en tus segmentos.

Cuando un usuario anónimo visita tu sitio web o aplicación, el SDK de Braze crea y le asigna un perfil de usuario "anónimo". Mientras el usuario navega, el SDK captura automáticamente datos para su perfil de usuario anónimo, como información de uso, información del dispositivo y más, si has configurado atributos personalizados y eventos personalizados.

Puedes hacer lo siguiente con los usuarios anónimos capturados:

- Envía mensajes a los usuarios antes de que se conecten
- Recopila el perfil de un usuario antes de que se conecte, para que no se te escapen datos relevantes
- Animar a completar el perfil con un mensaje cuando un usuario sólo completa parcialmente su perfil.
- Completa el perfil de un usuario cuando se conecte, para que puedas cancelar la mensajería en otras plataformas (como no enviar un mensaje de "envío gratuito en el 1er pedido de la aplicación" cuando el usuario ya ha realizado pedidos en la aplicación).
- Interactúa con los usuarios que muestren intención de salir animándoles a crear un perfil, pasar por caja o realizar otra acción.

## Cómo funciona

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## Asignar alias de usuario

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Fusionar usuarios anónimos  

A veces, los perfiles de usuario anónimos son duplicados que tienen el mismo número de teléfono o dirección de correo electrónico que otros perfiles de usuario. Uno de los duplicados puede ser incluso un perfil de usuario identificado. Estos duplicados pueden fusionarse en un solo perfil de usuario utilizando el POST [: Fusiona el punto final de los usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) o una de las herramientas de fusión de la plataforma Braze, como la [fusión basada en reglas]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

## Casos de uso

### Dirígete a usuarios anónimos de tu segmento

Como los usuarios anónimos no tienen un `external_id`, puedes dirigirte a ellos de forma masiva utilizando el filtro de segmentación **ID de usuario externo está en blanco**. Para mayor precisión, puedes añadir un atributo personalizado a los usuarios anónimos a los que quieras dirigirte y filtrar por ello.

Digamos que asignas el atributo personalizado "is_lead_profile" a cada perfil de usuario anónimo. Podrías dirigirte a estos perfiles con uno de estos filtros o con ambos:

- **El ID de usuario externo está en blanco**
- "is_lead_profile" **es cierto**

\![Filtros de segmento para un ID externo de usuario en blanco y un atributo personalizado verdadero "is_lead_profile".]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Capturar datos de pago de un usuario anónimo

Puedes capturar datos de pago de un usuario anónimo (o visitante invitado) creando un perfil de alias de usuario durante el proceso de pago. Cuando un usuario anónimo realiza una compra utilizando un formulario de captura Web, haz que se desencadene una llamada a la API para crear un perfil de alias de usuario y registrar un evento de compra. Entonces podrás actualizar el perfil de usuario creado a través de la API de Braze.

Aquí tienes un ejemplo de carga útil que se generará cuando se envíe el formulario de captura Web:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

