---
nav_title: Crear un Webhook Braze to Braze
article_title: Crear un Webhook Braze to Braze
page_order: 3
channel:
  - webhooks
description: "Este artículo explica cómo crear un webhook Braze to Braze para casos de uso clave."

---

# Crear un Webhook Braze to Braze

> Puedes utilizar webhooks para comunicarte con [la API REST]({{site.baseurl}}/api/basics/) de Braze, básicamente para hacer cualquier cosa que te permita nuestra API. Lo denominamos webhook Braze to Braze: un webhook que se comunica de Braze a Braze. Los casos de uso de esta página suponen que estás familiarizado con [el funcionamiento de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) y con la [creación de un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en Braze.

## Requisitos previos

Para crear un webhook Braze to Braze, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con permisos para el punto final al que quieres llegar.

## Configuración de tu Webhook Braze to Braze

Aunque los detalles de tu solicitud de webhook variarán de un caso de uso a otro, el flujo de trabajo general para crear un webhook Braze to Braze sigue siendo el mismo.

1. [Crea un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como componente de campaña o de Canvas. 
2. Elige la **plantilla en blanco**.
3. En la pestaña **Redactar**, especifica la **URL del webhook** y el **cuerpo de la solicitud** como se indica en tu caso de uso.
4. En la pestaña **Configuración**, especifica el **método HTTP** y **los encabezados de solicitud** según lo indicado para tu caso de uso.
5. Continúa construyendo el resto de tu webhook según sea necesario. Algunos casos de uso requieren una configuración de entrega específica, como desencadenar la campaña o el Canvas a partir de un evento personalizado.

## Casos de uso

Aunque puedes hacer muchas cosas con los webhooks Braze to Braze, aquí tienes algunos casos de uso para empezar:

- Incrementa un atributo personalizado entero para un contador cuando un usuario recibe un mensaje.
- Desencadena un segundo Canvas a partir de un Canvas inicial.

{% alert tip %}
Añade un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) a tu Canvas para hacer un seguimiento de los atributos, eventos y compras de un usuario en un compositor JSON. De este modo, estas actualizaciones se agrupan por lotes para que Braze pueda procesarlas con más eficacia que un webhook Braze to Braze.
{% endalert %}

### Casos de uso: Incrementa un atributo personalizado entero para un contador

Este caso de uso implica crear un atributo personalizado y utilizar Liquid para contar el número de veces que se ha producido una acción concreta. 

Por ejemplo, puede que quieras contar cuántas veces ha visto un usuario una campaña de mensajería dentro de la aplicación e impedir que vuelva a recibir la campaña después de haberla visto tres veces. Para más ideas sobre lo que puedes hacer con la lógica Liquid en Braze, consulta nuestra [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Sigue los pasos generales para crear un webhook Braze to Braze, y consulta lo siguiente cuando configures tu webhook:

- **URL del webhook:** La [URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) tu [punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `/users/track`. Por ejemplo, para la instancia `US-06`, la URL sería `https://rest.iad-06.braze.com/users/track`.
- **Cuerpo de la solicitud:** Texto en bruto

#### Encabezados de solicitud y método

Braze requiere una cabecera HTTP para la autorización que incluya tu clave de API y otra que declare tu `content-type`.

- **Encabezado de solicitud:**
  - **Autorización:** Portador {YOUR_API_KEY}
  - **Tipo de contenido:** application/json
- **Método HTTP:** POST

Sustituye `YOUR_API_KEY` por una clave de API Braze con permisos `users.track`. Puedes crear una clave de API dentro del panel de Braze en **Configuración** > **Claves de API**.

\![Los encabezados de solicitud del webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Añade tu solicitud de seguimiento del usuario en el cuerpo de la solicitud y el Liquid para asignar una variable contador. Para más detalles, consulta el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Lo siguiente es un ejemplo tanto del Liquid requerido como del cuerpo de la solicitud para este punto final, donde `your_attribute_count` es el atributo que estás utilizando para contar cuántas veces ha visto un usuario un mensaje:

{% raw %}
```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Cada vez que se actualice (aumente o disminuya) un contador de atributos personalizado, consumirá un [punto de datos]({{site.baseurl}}/user_guide/data/data_points/), que cuenta para tu consumo total.
{% endalert %}

### Casos de uso: Desencadenar un segundo Canvas a partir de un Canvas inicial

Para este caso de uso, crearás dos Canvas y utilizarás un webhook para desencadenar el segundo Canvas desde el primero. Esto actúa como un desencadenador de entrada para cuando un usuario alcanza un determinado punto en otro Canvas.

1. Empieza creando tu segundo Canvas, el Canvas que debe desencadenar tu Canvas inicial. 
2. Para el **Programa de entrada en** Canvas, selecciona **Desencadenado por API**.
3. Anota tu **ID de Canvas**. Lo necesitarás en un paso posterior.
4. Continúa construyendo los pasos de tu segundo Canvas y, a continuación, guárdalo.
5. Por último, crea tu primer Canvas. Busca el paso en el que quieres desencadenar el segundo Canvas y crea un nuevo paso con un webhook. 

Consulta lo siguiente cuando configures tu webhook:

- **URL del webhook:** La [URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) tu [punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `canvas/trigger/send`. Por ejemplo, para la instancia US-06, la URL sería `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Cuerpo de la solicitud:** Texto en bruto

#### Encabezados de solicitud y método

Braze requiere una cabecera HTTP para la autorización que incluya tu clave de API y otra que declare tu `content-type`.

- **Encabezado de solicitud:**
  - **Autorización:** Portador `YOUR_API_KEY`
  - **Tipo de contenido:** application/json
- **Método HTTP:** POST

Sustituye `YOUR_API_KEY` por una clave de API Braze con permisos `canvas.trigger.send`. Puedes crear una clave de API dentro del panel de Braze en **Configuración** > **Claves de API**.

\![Los encabezados de solicitud del webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Añade tu solicitud `canvas/trigger/send` en el campo de texto. Para más detalles, consulta [Enviar mensajes Canvas mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). El siguiente es un ejemplo del cuerpo de la solicitud para este punto final, donde `your_canvas_id` es el ID del Canvas de tu segundo Canvas: 

{% raw %}
```json
{
      "canvas_id": "your_canvas_id",
      "recipients": [
        {
          "external_user_id": "{{${user_id}}}"
         }
      ]
}
```
{% endraw %}

## Lo que debes saber

- Los webhook Braze to Braze están sujetos a los [límites de velocidad de]({{site.baseurl}}/api/api_limits/) los extremos.
- Las actualizaciones del perfil de usuario incurrirán en [puntos de datos]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) adicionales, mientras que desencadenar otro mensaje a través de los puntos finales de mensajería no lo hará.
- Si quieres dirigirte a [usuarios anónimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), puedes utilizar `braze_id` en lugar de `external_id` en el cuerpo de la solicitud de tu webhook.
- Puedes guardar tu webhook Braze to Braze como [plantilla]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para volver a utilizarlo.
- Puedes consultar [el Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para ver y solucionar problemas de fallos del webhook.


