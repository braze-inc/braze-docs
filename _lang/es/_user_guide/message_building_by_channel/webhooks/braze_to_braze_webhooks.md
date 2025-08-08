---
nav_title: Crear un Webhook Braze to Braze
article_title: Crear un Webhook Braze to Braze
page_order: 3
channel:
  - webhooks
description: "Este artículo explica cómo crear un webhook Braze-to-Braze para casos de uso clave."

---

# Crear un Webhook Braze to Braze

> Puedes utilizar webhooks para comunicarte con [la API REST]({{site.baseurl}}/api/basics/) de Braze, básicamente para hacer cualquier cosa que te permita nuestra API. Se trata de un webhook de Braze a Braze, es decir, un webhook que se comunica de Braze a Braze. Los casos de uso de esta página suponen que estás familiarizado con [el funcionamiento de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) y con la [creación de un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en Braze.

## Requisitos previos

Para crear un webhook Braze to Braze, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con permisos para el punto final al que quieres llegar.

## Configuración de tu Webhook Braze to Braze

Aunque los detalles de su solicitud de webhook variarán de un caso de uso a otro, el flujo de trabajo general para crear un webhook Braze-to-Braze sigue siendo el mismo.

1. [Crea un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como componente de campaña o de Canvas. 
2. Elija **Plantilla en blanco**.
3. En la pestaña **Redactar**, especifique la **URL del Webhook** y el **cuerpo de la solicitud** según lo indicado para su caso de uso.
4. En la pestaña **Configuración**, especifique el **método HTTP** y **las cabeceras de solicitud** según lo indicado para su caso de uso.
5. Continúe construyendo el resto de su webhook según sea necesario. Algunos casos de uso requieren una configuración de entrega específica, como la activación de la campaña o Canvas a partir de un evento personalizado.

## Ejemplos

Aunque puedes hacer muchas cosas con los webhooks Braze to Braze, aquí tienes algunos casos de uso para empezar:

- Incrementa un atributo personalizado entero para un contador cuando un usuario recibe un mensaje.
- Activar un segundo lienzo a partir de un lienzo inicial.

{% alert tip %}
Añada un [paso de actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) a su Canvas para realizar un seguimiento de los atributos, eventos y compras de un usuario en un compositor JSON. De este modo, estas actualizaciones se agrupan por lotes para que Braze pueda procesarlas con mayor eficacia que un webhook Braze-a-Braze.
{% endalert %}

### Casos de uso: Incrementar un atributo personalizado entero para un contador

Este caso de uso implica la creación de un atributo personalizado y el uso de Liquid para contar el número de veces que se ha producido una acción específica. 

Por ejemplo, es posible que desee contar cuántas veces un usuario ha visto una campaña de mensajes activos en la aplicación y evitar que vuelva a recibir la campaña después de haberla visto tres veces. Para obtener más ideas sobre lo que puede hacer con la lógica Liquid en Braze, consulte nuestra [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Siga los pasos generales para crear un webhook Braze-to-Braze, y consulte lo siguiente cuando configure su webhook:

- **URL del webhook:** La [URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) tu [punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `/users/track`. Por ejemplo, para la instancia `US-06`, la URL sería `https://rest.iad-06.braze.com/users/track`.
- **Cuerpo de la solicitud:** Texto sin procesar

#### Encabezados de solicitud y método

Braze requiere un encabezado HTTP para la autorización que incluya tu clave API y otro que declare tu `content-type`.

- **Encabezado de la solicitud:**
  - **Autorización:** Portador {YOUR_API_KEY}
  - **Content-Type:** application/json
- **Método HTTP:** POST

Sustituye `YOUR_API_KEY` por una clave de API Braze con permisos `users.track`. Puede crear una clave de API en el panel de control de Braze en **Configuración** > **Claves de API**.

![Los encabezados de solicitud para el webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Añade tu petición de seguimiento de usuario en el cuerpo de la petición y el Liquid para asignar una variable contador. Para más detalles, consulta el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

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
Cada vez que un contador de atributos personalizado se actualiza (aumenta o disminuye) consumirá un [punto de datos]({{site.baseurl}}/user_guide/data/data_points/), que cuenta para el consumo total.
{% endalert %}

### Caso de uso: Activar un segundo lienzo a partir de un lienzo inicial

Para este caso de uso, crearás dos lienzos y utilizarás un webhook para activar el segundo lienzo desde el primero. Esto actúa como un disparador de entrada para cuando un usuario alcanza un cierto punto en otro Canvas.

1. Empieza creando tu segundo Canvas, el Canvas que debe desencadenar tu Canvas inicial. 
2. Para la **Programación de entrada en** Canvas, selecciona **Desencadenado por API**.
3. Anota tu **ID de Canvas**. Lo necesitarás en un paso posterior.
4. Continúa construyendo los pasos de tu segundo lienzo y guárdalo.
5. Por último, crea tu primer lienzo. Busque el paso en el que desea activar el segundo Canvas y cree un nuevo paso con un webhook. 

Consulte lo siguiente cuando configure su webhook:

- **URL del webhook:** La [URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) tu [punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `canvas/trigger/send`. Por ejemplo, para la instancia US-06, la URL sería `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Cuerpo de la solicitud:** Texto sin procesar

#### Encabezados de solicitud y método

Braze requiere un encabezado HTTP para la autorización que incluya tu clave API y otro que declare tu `content-type`.

- **Encabezado de la solicitud:**
  - **Autorización:** Portador `YOUR_API_KEY`
  - **Content-Type:** application/json
- **Método HTTP:** POST

Sustituye `YOUR_API_KEY` por una clave de API Braze con permisos `canvas.trigger.send`. Puede crear una clave de API en el panel de control de Braze en **Configuración** > **Claves de API**.

![Los encabezados de solicitud para el webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Añada su solicitud `canvas/trigger/send` en el campo de texto. Para más detalles, consulta [Enviar mensajes Canvas mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). El siguiente es un ejemplo del cuerpo de la solicitud para este punto final, donde `your_canvas_id` es el ID del lienzo de su segundo lienzo: 

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

## Lo que hay que saber

- Los webhook de Braze a Braze están sujetos a los [límites de velocidad de ]({{site.baseurl}}/api/api_limits/) los puntos finales.
- Las actualizaciones del perfil de usuario conllevarán [puntos de datos]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) adicionales, mientras que la activación de otro mensaje a través de los puntos finales de mensajería no lo hará.
- Si desea dirigirse a [usuarios anónimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), puede utilizar `braze_id` en lugar de `external_id` en el cuerpo de la solicitud de su webhook.
- Puedes guardar tu webhook Braze to Braze como [plantilla]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para volver a utilizarlo.
- Puede consultar el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para ver y solucionar los fallos de los webhooks.


