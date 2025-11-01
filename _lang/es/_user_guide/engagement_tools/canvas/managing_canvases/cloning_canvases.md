---
nav_title: Clonación de lienzos
article_title: Clonación de lienzos
page_order: 3
alias: "/cloning_canvases/"
description: "Este artículo de referencia describe cómo clonar un Canvas desde el editor de Canvas original al flujo de trabajo del Flujo de Canvas."
tool: Canvas
---

# Clonar lienzos en Canvas Flow

{% alert important %}
Ya no puedes crear o duplicar Lienzos utilizando la experiencia original de Canvas. Braze recomienda a los clientes que utilizan la experiencia Canvas original que pasen a Canvas Flow, la experiencia Canvas actual.
{% endalert %}

> Si tienes un Canvas existente del editor original, puedes clonar este Canvas para crear una copia en el Flujo de Canvas. Al cambiar al flujo de trabajo Canvas actual, obtienes acceso a [componentes Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) ligeros, [propiedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) y [edición posterior al lanzamiento]({{site.baseurl}}/post-launch_edits). Tu Canvas original no se alterará ni se borrará.

Para clonar tu Canvas, haz lo siguiente:

1. Ve al panel Canvas. 
2. Identifica el Canvas del que quieres crear una copia en el flujo de trabajo del Flujo del Canvas. Puedes clonar Lienzos con estado **Borrador**, **Activo** o **Detenido**. 
3. Haz clic en <i class="fas fa-ellipsis-vertical"></i> **Más acciones** y selecciona **Clonar en flujo Canvas**.

\![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Introduce el nombre de tu nuevo Canvas y haz clic en **Clonar en flujo de Canvas**. 

\![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Ahora tienes dos versiones de tu Canvas: el Canvas original y la versión Canvas Flow. Tu Canvas original sigue teniendo su estado original, y el Canvas clonado tiene el estado **Borrador**. Puedes seguir accediendo al Canvas original, pero Braze recomienda utilizar el flujo de trabajo Flujo de Canvas para seguir construyendo tus Canvas.

Antes, algunos Lienzos con ramificaciones no se podían clonar. Ahora puedes clonar Lienzos con ramificación. Ten en cuenta que la clonación de Lienzos con ramificaciones puede dar lugar a pasos desconectados. Resuelve estos pasos desconectados (pasos que no tienen un paso precedente conectado a ellos) para asegurarte de que tu recorrido en Canvas está mapeado correctamente.

{% alert note %}
Si clonas un Canvas activo, Braze seguirá enviando usuarios a través del Canvas original. Recomendamos detener un Canvas antes de clonarlo para evitar enviar mensajes duplicados a los usuarios de ambos Canvases.
{% endalert %}

\![Panel Canvas con dos lienzos listados: V2 Copia de Canvas V1 y Canvas V1. La Copia V2 del Canvas V1 tiene un icono que indica que está utilizando el flujo de trabajo del Flujo del Canvas.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Has completado la clonación de tu Canvas en el flujo de trabajo del Flujo del Canvas. Ahora, ¡puedes seguir construyendo tus Lienzos en esta experiencia actualizada!

## Recomendaciones

Para permitir que los usuarios existentes continúen su viaje de usuario después de haber clonado tu Canvas original a Canvas Flow, puedes añadir filtros a tu Canvas existente que impidan a los nuevos usuarios entrar en el nuevo Canvas.

Si la reelegibilidad está desactivada, añade el filtro "Variación introducida en Canvas". Si la reelegibilidad está activada, estos son los posibles métodos a tener en cuenta para garantizar que los usuarios no entren dos veces en el mismo Canvas:
- Actualiza el Canvas existente para incluir una etiqueta única. Para el nuevo Canvas, añade un filtro "Último mensaje recibido de la campaña o Canvas con etiqueta". Esto impide que los usuarios entren dos veces en el Canvas después de una fecha de entrada específica (número total de días después del envío del último mensaje desde el Canvas original más la ventana de conversión). 
- **El siguiente método registrará puntos de datos.** Actualiza el Canvas original para incluir un webhook Braze to Braze que desencadene un sello de fecha y hora de atributo personalizado al entrar. Este atributo puede utilizarse para impedir que los usuarios entren en el nuevo Canvas después de la fecha especificada (número total de días transcurridos desde el envío del último mensaje desde el Canvas original más la ventana de conversión).

Para los Canvas desencadenados por la API, coordínate con tu equipo de ingeniería para asegurarte de que estos Canvas están utilizando el nuevo ID de Canvas cuando los nuevos Canvas estén listos para lanzarse.

Para más información sobre las diferencias entre el editor original de Canvas y la experiencia Canvas Flow, consulta [las preguntas frecuentes sobre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


