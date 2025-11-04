---
nav_title: Campañas de API
article_title: Campañas de API
page_order: 5
description: "Este artículo de referencia explica cómo generar un campaign_id para incluirlo en tus llamadas a la API y cómo configurar esa campaña."
page_type: reference
tool: Campaigns

---
# Campañas API

> Este artículo de referencia explica cómo generar un `campaign_id` para incluirlo en tus llamadas a la API y cómo configurar esa campaña.

Las campañas de API suelen utilizarse para mensajes transaccionales. Al crear campañas API (no [campañas desencadenadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)), el panel de Braze sólo se utiliza para generar un `campaign_id`, que te permite hacer un seguimiento de los análisis para los informes de campaña. También puedes generar un ID de variación del mensaje, que es diferente para cada variante de tu campaña. 

A continuación, enviarás esa información a tu equipo de desarrollo para que la utilice en la solicitud de API, junto con lo siguiente:
- Texto de campaña
- Membresía de la audiencia
- Activos

Una vez iniciada la campaña, puedes ver los resultados en el panel. Las campañas API utilizan [las API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze, que tienen las mismas opciones detalladas de informes y reorientación que las campañas creadas completamente a través del panel.

{% alert warning %}
Como las campañas API suelen ser transaccionales, todos los usuarios son elegibles para las campañas API, incluso los de tu grupo de control global. En estos envíos no se añade un encabezado de [cancelar suscripción con un clic]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe). Si deseas añadir un encabezado de cancelación de suscripción con un solo clic a todas las campañas de API, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Crear una nueva campaña

Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña** y, a continuación, **Campañas API**. Ahora, puedes avanzar para configurar tu campaña de API.

Una [campaña desencadenada por]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) API es diferente de una campaña de API.

## Configura tu campaña

Para configurar tu campaña, realiza los siguientes pasos:

1. Añade un título descriptivo para que puedas encontrar los resultados en nuestra página de campañas después de haber enviado tus mensajes.
2. Haz clic en **Añadir mensaje** y añade los tipos de mensajes que se incluirán en tu campaña API. Esto te permitirá generar un `campaign_id` y un ID de variación del mensaje, que difiere para cada canal que incluyas. 
3. Opcionalmente, puedes añadir un evento de conversión para hacer un seguimiento de las conversiones de usuarios en una acción específica o en un objetivo de campaña.
4. Haz clic en **Guardar campaña** y ¡ya estás listo para empezar tu campaña API!

## Llamadas a la API

Después de guardar tu campaña de API incluye lo siguiente en tu solicitud API: 
- Los campos `campaign_id` generados con tu solicitud API según se haya indicado en los [puntos finales Enviar mensajes]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints).
- Un [objeto de mensaje]({{site.baseurl}}/api/objects_filters/#messaging-objects) para cada plataforma incluida en la campaña. En el objeto mensaje, proporciona el ID de variación del mensaje. Esto especificará que las estadísticas deben recopilarse y mostrarse bajo esa variante. Se admiten los siguientes objetos de mensaje: Android, tarjetas de contenido, correo electrónico, iOS, Kindle, SMS/MMS, notificación push web y webhook.


