---
nav_title: Preferencias de notificación
article_title: Preferencias de notificación
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre las opciones disponibles para supervisar la mensajería y la actividad en la cuenta de tu empresa."

---

# Preferencias de notificación

> Si quieres supervisar la mensajería y la actividad en la cuenta de tu empresa, puedes optar por configurar notificaciones específicas y seleccionar a dónde van.

La página **Preferencias de notificación** es donde puedes configurar quién (si alguien) recibe notificaciones sobre tu empresa. Puedes configurar quién debe recibir notificaciones sobre la entrega de campañas o errores técnicos. También puedes especificar destinatarios para el informe de análisis semanal. Para la mayoría de las notificaciones, Braze admite canales de correo electrónico y webhook.

![Página de preferencias de notificación en el panel de Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Para acceder a esta página, ve a **Configuración** > **Configuración del administrador** > **Preferencias de notificación**.

{% alert tip %}
También puedes integrarte con Slack para recibir notificaciones. Para conocer los pasos, consulta [Enviar mensajes utilizando webhooks entrantes](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notificaciones disponibles

La siguiente tabla describe las notificaciones disponibles y qué canales se utilizan para entregarlas.

{% alert note %}
Si eliminas el valor predeterminado de **Destinatarios** de **Todos los usuarios del dashboard** y quieres volver a añadirlo, puedes introducirlo manualmente en el campo desplegable.
{% endalert %}

| Notificación | Descripción | Canales de notificación disponibles |
|--------------|-------------|-----------------|
| Alertas de uso de API | Al seleccionar esta opción, accedes al **Dashboard de uso de API**, donde puedes ir a la pestaña [**Alertas de uso de API**]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/) y configurar alertas para rastrear volúmenes clave de solicitudes de API. | Correo electrónico, Webhook |
| Errores de credenciales de AWS | Notifica a los destinatarios cuando Braze recibe un error al intentar usar tus credenciales de Amazon Web Services para una exportación de datos. Esto incluye notificaciones de error de credencial para Google Cloud Services y Azure (Microsoft Cloud Services). | Correo electrónico, Webhook |
| La campaña se ha detenido automáticamente | Notifica a los destinatarios cuando Braze ha detenido una campaña. | Correo electrónico |
| Canvas detenido automáticamente | Notifica a los destinatarios cuando Braze ha detenido un Canvas. | Correo electrónico |
| Caducidad de interacciones de la campaña | Notifica a los destinatarios sobre cualquier campaña que esté a punto de caducar en sus datos de interacción, junto con cualquier información sobre segmentos, campañas o Canvas que hagan referencia a ella en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| La campaña/el Canvas se ha actualizado | Notifica a los destinatarios cuando se actualiza o desactiva una campaña o Canvas activo, así como cuando se reactiva una campaña o Canvas inactivo o se lanzan borradores. | Correo electrónico |
| Límite de volumen de campaña/Canvas alcanzado | Notifica a los destinatarios cuando una campaña o Canvas alcanza su límite de volumen. | Correo electrónico | 
| Caducidad de interacciones del Canvas | Notifica a los destinatarios sobre cualquier Canvas que esté a punto de caducar en sus datos de interacción, junto con cualquier información sobre segmentos, campañas o Canvas que hagan referencia a él en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| Comentarios en Canvas | Notifica a los destinatarios cuando un Canvas tiene nuevos comentarios. | Correo electrónico |
| Errores de contenido conectado | Notifica a los destinatarios cuando un punto de conexión de contenido conectado tiene errores. | Correo electrónico |
| Errores de push | Notifica a los destinatarios cuando un punto de conexión push tiene errores. | Correo electrónico, Webhook |
| Límite de campaña planificada alcanzado | Notifica a los destinatarios cuando se ha alcanzado el límite de una campaña planificada recurrente. | Correo electrónico, Webhook |
| La campaña planificada ha finalizado el envío | Notifica a los destinatarios cuando una campaña planificada ha completado los envíos. | Correo electrónico, Webhook |
| Errores de webhook | Notifica a los destinatarios cuando un punto de conexión de webhook tiene errores. | Correo electrónico |
| Informe de análisis semanal | Envía a los destinatarios, cada lunes, un resumen de la actividad del espacio de trabajo de la semana pasada. Los destinatarios reciben un resumen de cada espacio de trabajo al que pertenecen. | Correo electrónico |
| Límites diarios de volumen de entrada en Canvas/campaña | Envía notificaciones cada vez que se alcanza un límite de envío. | Correo electrónico |
| Error en la consola de agentes | Notifica a los destinatarios cuando un [agente de la consola de agentes]({{site.baseurl}}/user_guide/brazeai/agents) ha alcanzado su límite de ejecución con la funcionalidad actual. | Correo electrónico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Los [usuarios suspendidos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/#suspending-company-users) pueden seguir recibiendo notificaciones de Braze.
{% endalert %}

## Informes de análisis semanales

Braze envía opcionalmente un informe semanal por correo electrónico a las personas que designes dentro de tu empresa todos los lunes a las 5 am EST. Puedes seleccionar los eventos personalizados que se incluirán en el informe semanal desde **Configuración de datos** > **Eventos personalizados**.

Puedes seleccionar hasta cinco eventos para incluirlos en tu informe semanal:

![Seleccionar los eventos que se incluirán en el informe de análisis]({% image_buster /assets/img_archive/company_analytics_report_new.png %})