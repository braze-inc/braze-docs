---
nav_title: Exportar datos de campaña
article_title: Exportar datos de campaña
page_order: 0
page_type: reference
description: "En este artículo de referencia se explica cómo exportar datos de resultados de campañas individuales, multicanal o multivariantes. El artículo también explica cómo exportar los datos de usuario de los destinatarios."
tool: 
  - Campaigns
  - Reports
  
---

# Exportar datos de campaña

> En la página **Campañas** del panel, selecciona la campaña que quieras ver y desplázate hasta los gráficos históricos de rendimiento, que se pueden exportar.<br><br>En esta página se explica cómo exportar datos de resultados de campaña de campañas únicas, multicanales y multivariantes, y cómo exportar datos de usuario de los destinatarios.

## Campañas multicanal

Para las campañas multicanal, los datos que se pueden exportar dependen de los canales de mensajería que hayas utilizado. Aquí tienes una lista de todos los datos que se pueden exportar de una campaña que haya utilizado mensajes push de iOS, push de Android, correo electrónico y mensajes in-app:

- Mensajes enviados por fecha
    - Total de mensajes enviados
    - Mensajes enviados a través de los canales de la campaña (pueden incluir push, correo electrónico y mensajes dentro de la aplicación)
- Participación en mensajes de correo electrónico por fecha
    - Número de correos electrónicos enviados
    - Número de correos electrónicos enviados
    - Número de correos electrónicos abiertos
    - Número de clics por correo electrónico
    - Número de mensajes rebotados
    - Número de correos electrónicos denunciados como correo no deseado
- Participación en los mensajes de la aplicación por fecha
    - Número de mensajes In-App enviados
    - Impresiones de mensajes dentro de la aplicación
    - Número de clics en mensajes dentro de la aplicación
- Interacción push de iOS por fecha
    - Número de notificaciones push de iOS enviadas
    - Total de aperturas
    - Direct Opens
    - Rebotes
- Interacción push de Android por fecha
    - Número de notificaciones push Android enviadas
    - Total de aperturas
    - Direct Opens
    - Rebotes

## Campañas multivariantes

Para las campañas multivariantes, que utilizan un solo canal de mensajería, puedes exportar datos que muestren el rendimiento de cada variante en el análisis del canal de mensajería específico a lo largo del tiempo. Puede ver estos datos agrupados por estadística o agrupados por variante de mensaje.

Los resultados de las campañas push contienen gráficos para los siguientes análisis:

- Mensajes enviados por fecha para cada variante
- Conversiones por fecha para cada variante
- Destinatarios únicos por fecha para cada variante
- Aperturas por fecha para cada variante
- Aperturas directas por fecha para cada variante
- Rebotes por fecha para cada variante

Los resultados de las campañas de correo electrónico contienen gráficos para los siguientes análisis:

- Número de entregas por fecha para cada variante
- Número de envíos por fecha para cada variante
- Aperturas por fecha para cada variante
- Clics por fecha para cada variante
- Rebotes por fecha para cada variante
- Informes de spam por fecha para cada variante

Los resultados de las campañas de mensajes in-app contienen gráficos para los siguientes análisis:

- Enviados por fecha para cada variante
- Impresiones por fecha para cada variante
- Clics por fecha para cada variante

## Destinatarios de la campaña

Puede exportar los datos de usuario de todos los destinatarios de una campaña como archivo CSV. Para ello, seleccione el botón **Datos del usuario** en la sección **Detalles de la campaña**.

{% alert note %}
¿No ve el botón **Datos de usuario**? Para exportar datos de usuario, necesita los [permisos de]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Exportación de Datos de Usuario** para ese espacio de trabajo.
{% endalert %}

![Desplegable de datos de usuario en la página de detalles de la campaña]({% image_buster /assets/img/campaign_export_example.png %})

La salida CSV contiene datos de perfil de usuario para cada destinatario de la campaña. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) a Braze, el CSV también se cargará en tu contenedor de S3. De lo contrario, el enlace que reciba por correo electrónico caducará en unas horas.

El archivo exportado incluye los mismos campos de datos de usuario que se incluyen cuando [exportas datos de usuario para un segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). Además de estos campos de datos, si selecciona "Exportar todos los datos del destinatario", el archivo exportado también contendrá los siguientes datos para cada usuario:

- Nombre de la variación de campaña recibida
- API ID de la variación de campaña recibida
- Si el usuario está en el grupo de control

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

