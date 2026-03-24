---
nav_title: Crear un Webhook Braze to Braze
article_title: Crear un Webhook Braze to Braze
page_order: 3
channel:
  - webhooks
description: "Este artículo de referencia trata sobre cuándo utilizar User Update frente a los Webhooks Braze to Braze y cómo crear un Webhook Braze to Braze."

---

# Crear un Webhook Braze to Braze

> Los webhooks Braze to Braze te permiten llamar a la [API REST de Braze]({{site.baseurl}}/api/basics/) desde dentro de Braze utilizando un [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en una [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) o [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/). Utiliza esto para tareas de orquestación, como desencadonar un [Canvas desencadentado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Para actualizar [los atributos de usuario]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) o [las compras]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) desde Canvas, utiliza la opción [Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/). Está diseñado para cambios en el perfil de usuario y procesa las actualizaciones de manera más eficiente.

Para sacar el máximo partido a este artículo, debes estar familiarizado con [el funcionamiento de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) y con cómo [crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en Braze.

## Utiliza la actualización de usuario para los cambios en los datos de usuario.

Para actualizar los perfiles de usuario desde Canvas, incluyendo la modificación [de atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), el registro [de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) o el registro [de compras]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), utiliza [la actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) en lugar de un Webhook Braze to Braze. 

La actualización de usuarios agrupa varios cambios y los envía por lotes, lo que la hace más rápida que los webhooks. Es más fácil de configurar que un webhook y admite actualizaciones complejas a través de tu [compositor JSON avanzado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer). Por ejemplo, para contar cuántas veces un usuario ha visto un mensaje, utiliza [la característica Incrementar y disminuir]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values) de User Update en lugar de un Webhook Braze to Braze.

{% alert tip %}
Añade [Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) a tu Canvas para actualizar los atributos, eventos y compras de un usuario utilizando un compositor JSON.
{% endalert %}

## Cuándo utilizar un webhook Braze to Braze

La actualización de usuarios puede realizar casi todas las mismas tareas que un Webhook Braze to Braze para actualizar los perfiles de usuario. Para actualizaciones complejas que vayan más allá de los simples atributos personalizados, puedes utilizar el [compositor JSON avanzado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer).

Puedes utilizar un webhook Braze to Braze cuando necesites llamar a [la API REST]({{site.baseurl}}/api/basics/) de Braze desde dentro de Braze para situaciones distintas a las actualizaciones directas de los usuarios desde los pasos en Canvas. Algunos ejemplos comunes son:

- Desencadenar un [Canvas activado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) desde otro Canvas
- Llamar a otros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/) para patrones de orquestación en los que un flujo de trabajo en Braze necesita invocar una API que no tiene un componente Canvas dedicado.

Para las actualizaciones de usuarios dentro de Canvas, el método recomendado es utilizar la función [Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

## Requisitos previos

Para crear un Webhook Braze to Braze, necesitas una [clave de API]({{site.baseurl}}/api/api_key/) con permisos para el punto final al que deseas acceder. Por ejemplo, para desencadear un Canvas desencadentado por API, necesitas una clave de API con el`canvas.trigger.send`permiso.

## Configuración de tu Webhook Braze to Braze

El flujo de trabajo general para crear un Webhook Braze to Braze sigue estos pasos:

1. [Crea un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como campaña o componente de Canvas. 
2. Elija **Plantilla en blanco**.
3. En la pestaña **Componer**, especifica la **URL del webhook** y **el cuerpo de la solicitud** para tu caso de uso de la API.
4. En la pestaña **Configuración**, especifica tu **método HTTP** y **los encabezados de solicitud** según lo requiera el punto final.
5. Configura cualquier configuración de entrega adicional (por ejemplo, desencadenar desde un evento personalizado) y crea el resto de tu campaña o Canvas.

## Activar un segundo lienzo a partir de un lienzo inicial

En este caso de uso, creas dos Canvas y utilizas un Webhook Braze to Braze para desencadear el segundo Canvas desde el primero. Esto actúa como un disparador de entrada para cuando un usuario alcanza un cierto punto en otro Canvas.

1. Empieza creando tu segundo Canvas, el Canvas que debe desencadenar tu Canvas inicial.
2. Para la **Programación de entrada en** Canvas, selecciona **Desencadenado por API**.
3. Anota tu **ID de Canvas**. Lo necesitarás en un paso posterior.
4. Continúa construyendo los pasos de tu segundo lienzo y guárdalo.
5. Por último, crea tu primer lienzo. Busque el paso en el que desea activar el segundo Canvas y cree un nuevo paso con un webhook.

Consulte lo siguiente cuando configure su webhook:

- **URL del webhook:** [La URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) de tu [punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `/canvas/trigger/send`. Por ejemplo, para la instancia `US-06`, la URL sería `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Cuerpo de la solicitud:** Texto sin procesar

#### Encabezados de solicitud y método

Braze requiere un encabezado HTTP para la autorización que incluya tu clave de API y otro que declare tu tipo de contenido.

- **Encabezados de solicitud:**
  - **Autorización:** `Bearer YOUR_API_KEY`
  - **Tipo de contenido:** `application/json`
- **Método HTTP:** `POST`

Reemplaza`YOUR_API_KEY`  por una clave de API de Braze que tenga`canvas.trigger.send`los permisos necesarios. Puedes crear una clave de API en el panel de Braze yendo a **Configuración** > **Claves de API**.

![Encabezados de solicitud para el webhook que muestran los campos Autorización y Tipo de contenido en el panel de Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Añada su solicitud `/canvas/trigger/send` en el campo de texto. Para obtener más información, consulta [Envío de mensajes de Canvas mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). El siguiente es un ejemplo del cuerpo de la solicitud para este punto final, donde `your_canvas_id` es el ID del lienzo de su segundo lienzo:

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

Cuando un usuario llega a este paso del webhook en el primer Canvas, Braze desencadena el segundo Canvas para ese usuario a través de la API.

## Consideraciones

- **Actualizaciones de los usuarios:** Para actualizar los perfiles de usuario desde Canvas (atributos, eventos, compras), utiliza [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) en lugar de los Webhook Braze to Braze para obtener una mayor eficiencia y rentabilidad.
- Los webhooks Braze to Braze están sujetos a [límites de velocidad]({{site.baseurl}}/api/api_limits/) de los puntos finales.
- Las actualizaciones del perfil de usuario generan [puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) que se contabilizan en tu consumo total, mientras que el envío de otro mensaje a través de los puntos finales de mensajería no lo hace.
- Para dirigirte a [usuarios anónimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), utiliza`braze_id`  en lugar de`external_id`  en el cuerpo de la solicitud de tu webhook.
- Puedes guardar tu Webhook Braze to Braze como [plantilla]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) de [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para volver a utilizarlo.
- Puede consultar el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para ver y solucionar los fallos de los webhooks.


