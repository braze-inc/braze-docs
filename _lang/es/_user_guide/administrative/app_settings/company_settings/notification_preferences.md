---
nav_title: Preferencias de notificación
article_title: Preferencias de notificación
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre las opciones disponibles para supervisar la mensajería y la actividad en la cuenta de su empresa."

---

# Preferencias de notificación

> Si desea supervisar la mensajería y la actividad en la cuenta de su empresa, puede optar por configurar notificaciones específicas y seleccionar a dónde van.

La página **Preferencias de notificación** es donde puede configurar quién (si alguien) recibe notificaciones sobre su empresa. Puede configurar quién debe recibir notificaciones sobre la entrega de campañas o errores técnicos. También puede especificar destinatarios para el informe analítico semanal. Para la mayoría de las notificaciones, Braze admite canales de correo electrónico y webhook.

![Página de preferencias de notificación en el panel de control de Braze][61]

Para acceder a esta página, vaya a **Configuración** > **Configuración del administrador** > **Preferencias de notificación**.

{% alert note %}
Si utilizas la [navegación anterior]({{site.baseurl}}/navigation), selecciona el menú desplegable de tu cuenta y ve a **Configuración de la empresa** > **Preferencias de notificación**.
{% endalert %}

## Notificaciones disponibles

La siguiente tabla enumera las notificaciones disponibles:

| Notificación | Descripción | Canales de notificación disponibles |
|--------------|-------------|-----------------|
| Errores de credenciales de AWS | Notifica a los destinatarios cuando Braze recibe un error mientras intenta usar tus credenciales de Amazon Web Services para una exportación de datos. | Correo electrónico, Webhook |
| La campaña se ha detenido automáticamente | Notifica a los destinatarios cuando Braze ha detenido una campaña. | Correo electrónico |
| Caducidad de interacciones de la campaña | Notifica a los destinatarios sobre cualquier campaña que esté a punto de caducar, junto con cualquier información sobre segmentos, campañas o lienzos que hagan referencia a ella en un filtro de retargeting y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| La campaña/El Canvas se ha actualizado | Notifica a los destinatarios cuando se actualiza o desactiva una campaña/lienzo activo, así como cuando se reactiva una campaña/lienzo inactivo o cuando se lanzan borradores. | Correo electrónico |
| Caducidad de interacciones del Canvas | Notifica a los destinatarios la caducidad de los datos de interacción de cualquier lienzo, junto con cualquier información sobre segmentos, campañas o lienzos a los que se haga referencia en un filtro de retargeting y que se hayan utilizado para enviar un mensaje en los 30 días anteriores. | Correo electrónico |
| Tarjeta de canal de noticias publicado/en vivo | Notifica a los destinatarios cuando se programan o publican tarjetas de noticias. | Correo electrónico, Webhook |
| Errores de credenciales de notificaciones push | Notifica a los destinatarios el momento en que las credenciales de inserción de una aplicación dejan de ser válidas y cuando se acerca su caducidad. | Correo electrónico, Webhook |
| Campaña planificada enviada/no enviada | Notifica a los destinatarios cuando las campañas programadas comienzan a enviarse o cuando las campañas programadas intentaron enviarse pero no había usuarios elegibles a los que enviar. | Correo electrónico, Webhook |
| Se ha alcanzado el límite de campañas planificadas | Notifica a los destinatarios el momento en que se ha alcanzado el límite de una campaña planificada recurrente. | Correo electrónico, Webhook |
| La campaña planificada ha finalizado el envío | Notifica a los destinatarios el momento en que una campaña planificada ha completado los envíos. | Correo electrónico, Webhook |
| Informe de análisis semanal | Envía a los destinatarios, cada lunes, un resumen de la actividad del espacio de trabajo de la semana pasada. Los destinatarios reciben un resumen de cada espacio de trabajo al que pertenecen. | Correo electrónico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Informes analíticos semanales

Braze envía opcionalmente un informe semanal por correo electrónico a las personas que usted designe dentro de su empresa todos los lunes a las 5 am EST. Puede seleccionar los eventos personalizados que se incluirán en el informe semanal desde **Configuración de datos** > **Eventos personalizados**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), esta página se encuentra en **Gestionar configuración** > **Eventos personalizados**.
{% endalert %}

Puede seleccionar hasta cinco eventos para incluirlos en su informe semanal:

![Seleccionar los eventos que se incluirán en el Informe Analítico][22]

## Integración del webhook entrante de Slack

Slack tiene una [aplicación de webhook entrante][67] que permite enviar mensajes desde fuentes externas a Slack. Para empezar, abre la aplicación de webhooks entrantes.

1. Seleccione el canal de Slack al que desea que lleguen las notificaciones y haga clic en **Añadir integración de Webhooks entrantes**.<br><br>
    ![Añadir integración de webhooks entrantes en Slack][63]<br><br>
  Slack generará una URL que tendrás que introducir en Braze para las notificaciones que desees recibir.<br><br>
2. Copie la **URL del Webhook**.<br><br>
    ![Copiar URL del webhook][64]<br><br>
3. Vaya a la pestaña **Preferencias de notificación** en **Configuración de la empresa**.<br><br>
4. Seleccione la notificación que desea activar para Slack. O, si tienes varias notificaciones que quieres enviar a este canal de Slack, utiliza **Añadir en bloque** para añadir el webhook a varias notificaciones.<br><br>
    ![Seleccione las notificaciones de Slack que desea activar][65]{: style="max-width:60%;"}<br><br>
5. Introduce la URL que Slack ha generado para ti.

Eso es todo. Debería empezar a recibir notificaciones sobre su empresa en este canal de Slack. También puedes consultar el artículo de ayuda de Slack sobre este tema: [Envío de mensajes mediante Webhooks entrantes][62].


[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks