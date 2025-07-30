---
nav_title: Exportar análisis de uso
article_title: Exportar análisis de uso
page_order: 3

page_type: reference
description: "Este artículo de referencia explica cómo exportar datos de uso de aplicaciones de alto nivel."
tool: 
  - Reports

---

# Exportación de análisis de uso

> Esta página cubre la página de **inicio** del panel, que contiene datos de alto nivel del uso de la aplicación, así como estadísticas detalladas de diferentes KPI por fecha.

Para exportar CSV de los datos de esta página:

1. Establece el periodo de tiempo y las aplicaciones de las que quieres ver los datos. Por defecto, el panel muestra los datos de los últimos 30 días de todas las aplicaciones.

![Periodo de tiempo y campos de aplicación en el panel de Inicio.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Desplácese hasta el gráfico **Rendimiento a lo largo del tiempo**.
3\. Seleccione los datos que desea exportar en el campo **Estadísticas para**. Ver los [datos disponibles](#available-data) para exportar.

![Gráfico de rendimiento a lo largo del tiempo en el panel de inicio.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Selecciona <i class="fas fa-bars" title="Menú contextual del gráfico"></i> y selecciona la opción de exportación.

## Datos disponibles

Puede exportar CSV con los siguientes datos:

- Recuento de sesiones por fecha
    - (Opcional) Recuento de sesiones para diferentes segmentos
    - (Opcional) Recuento de sesiones para diferentes versiones de la aplicación
- DAUs por fecha
    - (Opcional) DAUs para diferentes segmentos
- Estadísticas de correo electrónico por fecha
    - Número de correos electrónicos enviados
    - Número de correos electrónicos enviados
    - Número de correos electrónicos abiertos
    - Número de clics por correo electrónico
    - Número de mensajes rebotados
    - Número de correos electrónicos denunciados como correo no deseado
- Mensajes en la aplicación por fecha
    - Número de mensajes In-App enviados
    - Impresiones de mensajes dentro de la aplicación
    - Número de mensajes abiertos en la aplicación
- MAUs por fecha
- Número de nuevos usuarios por fecha
- Notificaciones push por fecha
    - (Opcional) Notificaciones push para diferentes plataformas de aplicaciones
    - Número de notificaciones push enviadas
    - Total de aperturas
    - Direct Opens
    - Rebotes
- Recuento de sesiones por hora
- Recuento de sesiones por MAU por fecha
- Adherencia por fecha

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visite nuestro artículo [sobre resolución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

