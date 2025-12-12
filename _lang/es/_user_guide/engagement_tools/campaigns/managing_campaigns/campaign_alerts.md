---
nav_title: Alertas de campaña
article_title: Alertas de campaña
page_order: 6

page_type: reference
description: "Este artículo de referencia ofrece un resumen de las alertas de campaña, sus ventajas y cómo configurarlas para que te proporcionen tranquilidad."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertas de campaña

> Queremos alertarte cuando algo no parezca lo esperado y darte la tranquilidad de que el barco navega sin problemas. Las alertas de umbral de campaña proporcionan tranquilidad: sé el primero en saber si una campaña importante envía más o menos mensajes de los que esperas.

Las alertas de campaña están disponibles para las siguientes campañas:

- Campañas programadas recurrentes
- Campañas basadas en la acción
- Campañas desencadenadas por la API

## Configurar la alerta de tu campaña

Navega hasta la página de análisis de tu campaña para empezar a configurar tu alerta. Cuando selecciones **Configurar alerta**, podrás especificar los umbrales de alerta superior e inferior, así como los destinatarios y canales de la alerta.

\![Cuadro de diálogo de Seguimiento de campaña con dos botones: Cancelar y Guardar.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Para una campaña recurrente programada, puedes establecer umbrales superiores e inferiores para los mensajes enviados cada vez que se envíe la campaña. Para una campaña desencadenada, puedes establecer umbrales superiores e inferiores para el número de mensajes enviados cada hora y cada día.

Puedes configurar una alerta por correo electrónico, una alerta webhook o ambas. Las alertas webhook pueden ser muy útiles, ya que te permiten enviar una alerta a un canal de Slack. Para más información sobre la integración de las alertas de campaña con Slack, consulta nuestra [documentación]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration).

{% alert note %}
Al configurar las alertas de campaña para futuras campañas, puedes recibir actualizaciones antes de que empiece la campaña y después de que termine. Esto se debe a que las alertas de campaña seguirán enviándose hasta que la campaña se haya detenido manualmente.
{% endalert %}

## Carga útil del webhook de alerta de campaña

A continuación se muestra un ejemplo de carga útil para el cuerpo de un webhook de alerta de campaña. Este ejemplo utiliza una alerta configurada para enviarse cuando los mensajes enviados sean inferiores a 500 para una campaña determinada.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

