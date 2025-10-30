---
nav_title: Estados
article_title: Estados de campaña y Canvas
page_order: 1
description: "Conoce los estados de las campañas y los Lienzos y cómo utilizarlos en el panel."
tool:
    - Campaigns
    - Canvas
---

# Estados de campaña y Canvas

> Conoce los estados de las campañas y los Lienzos y cómo puedes utilizarlos en el panel.

## Filtrar por estado

Para filtrar tus campañas o Lienzos por estado, selecciona **Todos los estados** y, a continuación, elige un estado.

Desplegable "Todos los estados" en el panel de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Cambiar el estado

Para cambiar el estado de una campaña o Canvas, selecciona el menú <i class="fas fa-ellipsis-vertical"></i>, y luego elige un estado.

\![Una lista de Lienzos en el panel de Braze, con el menú abierto para uno de los Lienzos.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Estados disponibles

Estos son los estados disponibles para campañas y Lienzos:

| Estado | Descripción |
| --- | --- |
| Activo | Las campañas activas y los Lienzos están en proceso de envío. Por defecto, verás las campañas activas y los Lienzos en las páginas respectivas. |
| Borrador | Los borradores de campañas y Lienzos se guardan, pero no se lanzan. Para continuar editando y empezar a enviar, puedes seleccionar el borrador yendo a **Mensajería** en el panel de Braze y seleccionando **Canvas** o **Campañas**. |
| Archivado | Las campañas y lienzos archivados son mensajes que ya no se envían. Estas campañas y Lienzos también se eliminan de los gráficos estadísticos de la página [**Inicio**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) y [**Ingresos**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) páginas.|
| Detenido | Las campañas y los lienzos detenidos están en pausa, pero aún puedes editarlos. Para reanudar, selecciona el menú <i class="fas fa-ellipsis-vertical"></i>, y luego **Reanudar**. Para más información, consulta [Comportamiento de Canvas detenido](#stopped-canvas-behavior). |
| Ralentí | Cuando una campaña o Canvas deje de enviar mensajes, Braze le asignará un estado de inactividad para ayudarte a ordenar y gestionar tu lista de campañas y Canvas. Puedes ver qué campañas o Lienzos se detendrán automáticamente y la fecha de detención asociada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Detenido el comportamiento de Canvas {#stopped-canvas-behavior}

Cuando se detiene un Canvas, ocurre lo siguiente:

- **Mensajes programados:** Tus mensajes programados no se enviarán, independientemente del lugar que ocupe un usuario en el Canvas. Esto también incluye a los usuarios que estaban en cola debido al límite de velocidad.
- **Envíos por correo electrónico:** Los envíos por correo electrónico pueden no detenerse inmediatamente, ya que tu proveedor de servicios de correo electrónico (ESP) puede seguir procesando tus solicitudes existentes.
- **Pasos de retardo:** Los usuarios que se encuentren en un [paso en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) permanecerán allí normalmente, pero saldrán del Canvas cuando finalice el periodo establecido.

Para reanudar el Canvas, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> y, a continuación, **Reanudar**. Cuando se reactive, los mensajes que se hayan detenido previamente se enviarán según lo programado, siempre que no haya pasado la hora programada.

## Buenas prácticas

### Controla tus mensajes por estado

Puedes controlar tus mensajes por estado para revisar los detalles de rendimiento. Por ejemplo, si tienes una serie de campañas activas, puedes evaluar el rendimiento de cada campaña con sus métricas de interacción y hacer los ajustes necesarios. Si, en cambio, tienes algunos Lienzos parados, puedes considerar si deben reanudarse para la mensajería o archivarse por completo.

{% alert tip %}
¿Buscas más formas de organizarte? Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags) para proporcionar más contexto de un vistazo.
{% endalert %}

### Audita tus mensajes activos

Realizando auditorías de tus campañas y Canvases activos, puedes evaluar la relevancia y el rendimiento, y eliminar o actualizar las campañas y Canvases obsoletos para mantener tu mensajería fresca.
