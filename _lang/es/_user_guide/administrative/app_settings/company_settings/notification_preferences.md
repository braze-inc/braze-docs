---
nav_title: Preferencias de notificación
article_title: Preferencias de notificación
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre las opciones disponibles para supervisar la mensajería y la actividad en la cuenta de tu empresa."

---

# Preferencias de notificación

> Si quieres controlar la mensajería y la actividad de la cuenta de tu empresa, puedes configurar notificaciones específicas y seleccionar a dónde van.

La página **Preferencias de notificación** es donde puedes configurar quién (si alguien) recibe notificaciones sobre tu empresa. Puedes configurar quién debe recibir notificaciones sobre la entrega de campañas o errores técnicos. También puedes especificar destinatarios para el informe semanal de análisis. Para la mayoría de las notificaciones, Braze admite canales de correo electrónico y webhook.

\![Página de preferencias de notificación en el panel de Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Para acceder a esta página, ve a **Configuración** > **Configuración del administrador** > **Preferencias de notificación**.

## Notificaciones disponibles

La siguiente tabla describe las notificaciones disponibles y qué canales se utilizan para entregarlas.

| Notificación | Descripción | Canales de notificación disponibles |
|--------------|-------------|-----------------|
| Errores de credenciales de AWS | Notifica a los destinatarios cuando Braze recibe un error al intentar utilizar tus credenciales de Amazon Web Services para una exportación de datos. Esto incluye notificaciones de error de credenciales para Google Cloud Services y Azure (Microsoft Cloud Services). | Correo electrónico, Webhook |
| Campaña detenida automáticamente | Notifica a los destinatarios cuando Braze ha detenido una campaña. | Correo electrónico |
| Expiración de la interacción de la campaña | Notifica a los destinatarios sobre cualquier campaña que esté a punto de caducar, junto con cualquier información sobre segmentos, campañas o Canvases que hagan referencia a ella en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| Campaña/Lienzo actualizados | Notifica a los destinatarios cuando se actualiza o desactiva una campaña o Canvas activo, así como cuando se reactiva una campaña o Canvas inactivo o se lanzan borradores. | Correo electrónico |
| Límite de volumen de campaña/lienzo alcanzado | Notifica a los destinatarios cuando una campaña o Canvas alcanza su límite de volumen. | Correo electrónico | 
| Caducidad de la Interacción Canvas | Notifica a los destinatarios sobre cualquier Canvas que esté a punto de caducar, junto con cualquier información sobre segmentos, campañas o Canvases que hagan referencia a él en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| Errores de credenciales push | Notifica a los destinatarios cuando las credenciales push de una aplicación no son válidas y cuando las credenciales push de una aplicación caducan pronto. | Correo electrónico, Webhook |
| Campaña programada Enviada/No enviada | Notifica a los destinatarios cuando las campañas programadas empiezan a enviar o cuando las campañas programadas intentan enviar pero no tienen usuarios elegibles a los que enviar. | Correo electrónico, Webhook |
| Límite de campaña programado Cumplido | Notifica a los destinatarios cuando se ha alcanzado el límite de una campaña programada recurrente. | Correo electrónico, Webhook |
| Campaña programada Envío finalizado | Notifica a los destinatarios cuándo ha finalizado el envío de una campaña programada. | Correo electrónico, Webhook |
| Informe semanal de análisis | Envía un resumen de la actividad del espacio de trabajo de la semana pasada a los destinatarios todos los lunes. Los destinatarios reciben un resumen por cada espacio de trabajo al que pertenecen. | Correo electrónico |
| Límites diarios de volumen de entrada en Canvas/Campaña | Envía notificaciones cada vez que se alcanza un límite de envío. | Correo electrónico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Informes semanales de análisis

Braze envía opcionalmente un informe semanal por correo electrónico a las personas que designes dentro de tu empresa todos los lunes a las 5 de la mañana EST. Puedes seleccionar los eventos personalizados que se incluirán en el informe semanal desde **Configuración de datos** > Eventos personalizados.

Puedes seleccionar hasta cinco eventos para incluirlos en tu informe semanal:

\![Seleccionar los eventos que se incluirán en el informe de análisis]({% image_buster /assets/img_archive/company_analytics_report_new.png %})

## Integración del webhook entrante de Slack

Slack tiene una [aplicación de webhook entrante](https://my.slack.com/services/new/incoming-webhook/) que permite enviar mensajes desde fuentes externas a Slack. Para empezar, abre la aplicación de webhook entrante.

1. Selecciona el canal de Slack al que quieres que lleguen las notificaciones y haz clic en **Añadir integración de webhooks entrantes**.<br><br>
    \![Añadir integración de webhooks entrantes en Slack]({% image_buster /assets/img_archive/slack_f.png %})<br><br>
  Slack generará una URL que tendrás que introducir en Braze para las notificaciones que desees recibir.<br><br>
2. Copia la **URL del webhook**.<br><br>
    \![Copia la URL del webhook]({% image_buster /assets/img_archive/copy_url.png %})<br><br>
3. Ve a la pestaña **Preferencias de notificación** en **Configuración de la empresa**.<br><br>
4. Selecciona la notificación que deseas habilitar para Slack. O, si tienes varias notificaciones que quieres enviar a este canal de Slack, utiliza **Añadir en bloque** para añadir el webhook a varias notificaciones.<br><br>
    \![Selecciona las notificaciones de Slack que quieres habilitar]({% image_buster /assets/img_archive/click_edit_f.png %}){: style="max-width:60%;"}<br><br>
5. Introduce la URL que Slack ha generado para ti.

Eso es. Deberías empezar a recibir notificaciones sobre tu empresa en este canal de Slack. También puedes consultar el artículo de ayuda de Slack sobre este tema: [Envío de mensajes mediante webhooks entrantes](https://api.slack.com/incoming-webhooks).

