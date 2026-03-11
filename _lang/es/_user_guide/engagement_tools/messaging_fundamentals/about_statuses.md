---
nav_title: Estados
article_title: Estado de la campaña y del Canvas
page_order: 11
description: "Obtén información sobre los estados de las campañas y los lienzos, y sobre cómo utilizarlos en el panel."
tool:
    - Campaigns
    - Canvas
---

# Estado de la campaña y del Canvas

> Obtén información sobre los estados de las campañas y los lienzos, y cómo puedes utilizarlos en el panel.

## Filtrar por estado

Para filtrar tus campañas o lienzos por estado, selecciona **Todos los estados** y, a continuación, elige un estado.

![El menú desplegable «Todos los estados» en el panel de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Cambiar el estado

Para cambiar el estado de una campaña o Canvas, selecciona el<i class="fas fa-ellipsis-vertical"></i>menú y, a continuación, elige un estado.

![Una lista de lienzos en el panel de Braze, con el menú abierto para uno de los lienzos.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Estados disponibles

Estos son los estados disponibles para las campañas y los lienzos:

| Estado | Descripción |
| --- | --- |
| Activos | Las campañas activas y los lienzos están en proceso de envío. De forma predeterminada, verás las campañas activas y los lienzos en las páginas respectivas. |
| En borrador | Los borradores de las campañas y los lienzos se guardan, pero no se lanzan. Para continuar editando y comenzar a enviar, puedes seleccionar el borrador yendo a **Mensajería** en el panel de Braze y seleccionando **Canvas** o **Campañas**. |
| Archivadas | Las campañas y los lienzos archivados son mensajes que ya no se envían. Estas campañas y lienzos también se eliminan de los gráficos estadísticos de las páginas [**Inicio**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) e [**Ingresos**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report).|
| Detenida | Las campañas y los lienzos detenidos se pausan, pero tú puedes seguir editándolos. Para reanudar un Canvas, ve al paso **Resumen** del generador de Canvas y selecciona **Reanudar Canvas**. Para las campañas, selecciona el<i class="fas fa-ellipsis-vertical"></i>menú y, a continuación, **Reanudar**. Para obtener más información, consulta [Comportamiento](#stopped-canvas-behavior) de [Stopped Canvas](#stopped-canvas-behavior). |
| Inactivo | Cuando una campaña o Canvas deja de enviar mensajes, Braze le asignará un estado inactivo para ayudarte a ordenar y gestionar tu lista de campañas y Canvases. Puedes ver qué campañas o lienzos se detendrán automáticamente y la fecha de detención asociada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamiento de Canvas detenido {#stopped-canvas-behavior}

Cuando se detiene un Canvas, ocurre lo siguiente:

- **Mensajes programados:** Tus mensajes programados no se enviarán, independientemente de la ubicación del usuario en Canvas. Esto también incluye a los usuarios que quedaron en cola debido al límite de velocidad.
- **Envíos por correo electrónico:** Es posible que el envío de correos electrónicos no se detenga inmediatamente, ya que tu proveedor de servicios de correo electrónico (ESP) puede seguir procesando tus solicitudes existentes.
- **Pasos de retardo:** Los usuarios que se encuentren en una [etapa de retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) permanecerán allí como de costumbre, pero saldrán del Canvas cuando finalice el período establecido.
- **Borrador de cambios:** Cualquier borrador de cambios en el Canvas se descartará cuando se detenga el Canvas.

Para reanudar el Canvas, ve al paso **Resumen** del generador de Canvas y selecciona **Reanudar Canvas**. Cuando se reactiva, cualquier mensaje que se haya detenido previamente se enviará según lo programado, siempre y cuando la hora programada no haya pasado ya.

## Buenas prácticas

### Supervisa tus mensajes por estado

Puedes supervisar tus mensajes por estado para revisar los detalles del rendimiento. Por ejemplo, si tienes una serie de campañas activas, puedes evaluar el rendimiento de cada una de ellas con sus métricas de interacción y realizar los ajustes necesarios. Si, por el contrario, tienes algunos lienzos detenidos, puedes considerar si deben reanudarse para la mensajería o archivarse por completo.

{% alert tip %}
¿Buscas más formas de mantenerte organizado? Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags) para proporcionar más contexto de un vistazo.
{% endalert %}

### Audita tus mensajes activos

Al realizar auditorías de tus campañas y lienzos activos, puedes evaluar la relevancia y el rendimiento, y eliminar o actualizar cualquier campaña y lienzo obsoleto para mantener tus mensajes actualizados.
