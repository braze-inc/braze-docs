---
nav_title: Exportar datos de campaña
article_title: Exportar datos de campaña
page_order: 0
page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de resultados de campaña de campañas únicas, multicanales o multivariantes. El artículo también explica cómo exportar los datos de usuario de los destinatarios."
tool: 
  - Campaigns
  - Reports
  
---

# Exportar datos de campaña

> En la página **Campañas** del panel, selecciona la campaña que quieras ver y desplázate hasta los gráficos históricos de rendimiento, que se pueden exportar.<br><br>En esta página se explica cómo exportar datos de resultados de campaña de campañas únicas, multicanales y multivariantes, y cómo exportar datos de usuario de los destinatarios.

## Campañas multicanal

Para las campañas multicanal, los datos que se pueden exportar dependen de los canales de mensajería que hayas utilizado. Aquí tienes una lista de todos los datos que se pueden exportar de una campaña que utilizó push de iOS, push de Android, correo electrónico y mensajes dentro de la aplicación:

- Mensajes enviados por fecha
    - Total de mensajes enviados
    - Mensajes enviados a través de los canales de la campaña (pueden incluir push, correo electrónico y mensajes dentro de la aplicación)
- Interacción de mensajes de correo electrónico por fecha
    - Número de correos electrónicos entregados
    - Número de envíos por correo electrónico
    - Número de correos electrónicos abiertos
    - Número de clics de correo electrónico
    - Número de rebotes de correo electrónico
    - Número de envíos electrónicos denunciados como spam
- Interacción de mensajes dentro de la aplicación por fecha
    - Número de mensajes dentro de la aplicación enviados
    - Impresiones de mensajes dentro de la aplicación
    - Número de clics en mensajes dentro de la aplicación
- Interacción push de iOS por fecha
    - Número de notificaciones push de iOS enviadas
    - Aperturas totales
    - Direct Opens
    - Rebotes
- Interacción push de Android por fecha
    - Número de notificaciones push Android enviadas
    - Aperturas totales
    - Direct Opens
    - Rebotes

## Campañas multivariantes

Para las campañas multivariantes, que utilizan un solo canal de mensajería, puedes exportar datos que muestren el rendimiento de cada variante en el análisis del canal de mensajería específico a lo largo del tiempo. Puedes ver estos datos agrupados por estadística o agrupados por variante de mensaje.

Los resultados de las campañas push contienen gráficos para los siguientes análisis:

- Mensajes enviados por fecha para cada variante
- Conversiones por fecha para cada variante
- Destinatarios únicos por fecha para cada variante
- Abre por fecha para cada variante
- Direct Opens por fecha para cada variante
- Rebotes por fecha para cada variante

Los resultados de la campaña de correo electrónico contienen gráficos para los siguientes análisis:

- Número entregado por fecha para cada variante
- Número de envíos por fecha para cada variante
- Abre por fecha para cada variante
- Clics por fecha para cada variante
- Rebotes por fecha para cada variante
- Informes de correos no deseados por fecha para cada variante

Los resultados de la campaña de mensajería dentro de la aplicación contienen gráficos para los siguientes análisis:

- Enviado por fecha para cada variante
- Impresiones por fecha para cada variante
- Clics por fecha para cada variante

## Destinatarios de la campaña

Puedes exportar los datos de usuario de todos los destinatarios de una campaña como un archivo CSV. Para ello, selecciona el botón **Datos de usuario** en la sección **Detalles de la campaña**.

{% alert note %}
¿No ves el botón **Datos de usuario**? Para exportar datos de usuario, necesitas los [permisos de]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Exportación de datos de usuario** para ese espacio de trabajo.
{% endalert %}

Desplegable de Datos de usuario en la página Detalles de la campaña]({% image_buster /assets/img/campaign_export_example.png %})

La salida CSV contiene datos de perfil de usuario de cada destinatario de la campaña. Braze generará el informe en segundo plano y lo enviará por correo electrónico al usuario que esté conectado en ese momento.

Si has vinculado tus [credenciales de Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) a Braze, el CSV también se cargará en tu contenedor de S3. De lo contrario, el enlace que se te ha enviado por correo electrónico caducará en unas horas.

El archivo exportado incluye los mismos campos de datos de usuario que se incluyen cuando [exportas datos de usuario para un segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). Además de esos campos de datos, si eliges "Exportar todos los datos del destinatario", el archivo exportado también contendrá los siguientes datos de cada usuario:

- Nombre de la campaña variación recibida
- API ID de la variación de campaña recibida
- Si el usuario está en el grupo de control

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

