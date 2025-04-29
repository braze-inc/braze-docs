---
nav_title: Diferencias entre los atributos de campaña y Canvas en Braze
article_title: Diferencias entre los atributos de campaña y Canvas en Braze
page_order: 1

page_type: reference
description: "Este artículo de ayuda compara el nombre y los ID de los atributos de campaña y Canvas entre fuentes en Braze."
platform: API
---

# Cómo difieren los atributos de campaña y Canvas entre las fuentes en Braze

Los nombres e ID de las campañas, Canvas y pasos en Canvas están disponibles en Liquid, en nuestra API REST y en Currents. Estos atributos mapean el mismo valor en las tres fuentes, pero pueden tener nombres diferentes. Esta página pretende ayudarte a establecer conexiones entre los tres.

## Casos prácticos

### Liquid

Los atributos de campaña y Canvas están disponibles como etiquetas de Liquid en nuestro panel {% raw %}(como `{{campaign.${api_id}}}`){% endraw %}. Puedes utilizar Liquid para pasar estos atributos en el propio mensaje, en una llamada a Contenido conectado o como par clave-valor. Suele hacerse con fines de seguimiento.

### API REST

Los atributos de campaña y Canvas también están disponibles en el [punto final Exportar detalles de campaña]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) o [Exportar detalles de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/). Puedes utilizar nuestra API REST para crear mapeados, es decir, una lista de todos los nombres de Canvas y sus ID correspondientes.

### Currents

Los atributos de campaña y Canvas están vinculados a [eventos de interacción de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) de Currents. Esto es importante para que puedas determinar a qué campaña o componente de Canvas está asociado un envío push o una apertura de correo electrónico.

## Atributos de la campaña

| Atributo | Liquid | API REST | Currents |
| --- | --- | --- | --- |
| Nombre de la campaña | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID de campaña | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (se utiliza como entrada para la propia llamada a la API) | campaign_id |
| Nombre de variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (mapea el nombre de la variante al ID de la variante utilizando el punto final Exportar detalles de campaña) |
| ID de la variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Atributos de Canvas

| Atributo | Liquid | API REST | Currents |
| --- | --- | --- | --- |
| Nombre del Canvas | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID de Canvas | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (se utiliza como entrada para la propia llamada a la API) | canvas_id |
| Nombre de variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID de la variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nombre del paso | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID de paso | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal de mensajería | N/A | `steps.messages.message_variation_id.channel` | N/A (inherente al tipo de evento, como envío push o correo electrónico abierto) |
| ID del mensaje | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }