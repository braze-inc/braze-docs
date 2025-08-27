---
nav_title: Clonación de Canvas
article_title: Clonación de Canvas
page_order: 3
alias: "/cloning_canvases/"
description: "Este artículo de referencia describe cómo clonar un lienzo desde el editor de lienzos original al flujo de trabajo del flujo de lienzos."
tool: Canvas
---

# Clonar Canvas a Canvas Flow

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando la experiencia Canvas original. Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow.
{% endalert %}

> Si tienes un Lienzo existente del editor original, puedes clonar este Lienzo para crear una copia en el Canvas Flow. Al cambiar al flujo de trabajo del Canvas, obtienes acceso a [componentes ligeros del Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), [propiedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) y [edición posterior al lanzamiento]({{site.baseurl}}/post-launch_edits). Tu Canvas original no será alterado ni borrado.

Para clonar tu Canvas, haz lo siguiente:

1. Vaya al panel de control de Canvas. 
2. Identifique el lienzo del que desea crear una copia en el flujo de trabajo Flujo del lienzo. Puede clonar lienzos con estado **Borrador**, **Activo** o **Detenido**. 
3. Haga clic en <i class="fas fa-ellipsis-vertical"></i> **More actions** y seleccione **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Introduce el nombre de tu nuevo lienzo y haz clic en **Clonar en flujo de lienzo**. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Ahora, tienes dos versiones de tu Canvas: el Canvas original y la versión Canvas Flow. Tu Lienzo original sigue teniendo su estado original, y el Lienzo clonado tiene el estado **Borrador**. Puedes seguir accediendo al lienzo original, pero Braze recomienda utilizar el flujo de trabajo Canvas Flow para seguir construyendo tus lienzos.

Antes, algunos lienzos con ramificaciones no podían clonarse. Ahora, puedes clonar Lienzos con ramificación. Tenga en cuenta que la clonación de lienzos con ramificaciones puede dar lugar a pasos desconectados. Resuelva estos pasos desconectados (pasos que no tienen un paso precedente conectado a ellos) para asegurarse de que su Canvas journey está mapeado correctamente.

{% alert note %}
Si clona un Canvas activo, Braze seguirá enviando usuarios a través del Canvas original. Recomendamos detener un Canvas antes de clonarlo para evitar enviar mensajes duplicados a los usuarios de ambos Canvases.
{% endalert %}

![Tablero de lonas con dos lonas listadas: V2 Copia de Canvas V1 y Canvas V1. La copia V2 del Canvas V1 tiene un icono que indica que está utilizando el flujo de trabajo del Canvas.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Has completado la clonación de tu Canvas en el flujo de trabajo de Canvas Flow. Ahora, puedes seguir construyendo tus lienzos en esta experiencia actualizada.

## Recomendaciones

Para permitir que los usuarios existentes continúen su recorrido de usuario después de haber clonado tu Canvas original a Canvas Flow, puedes añadir filtros a tu Canvas existente que impidan a los nuevos usuarios entrar en el nuevo Canvas.

Si la reelegibilidad está desactivada, añada el filtro "Variación del lienzo introducido". Si está activada la reelección, estos son los posibles métodos a tener en cuenta para garantizar que los usuarios no introduzcan dos veces el mismo lienzo:
- Actualice el lienzo existente para incluir una etiqueta única. Para el nuevo lienzo, añada un filtro "Último mensaje recibido de campaña o lienzo con etiqueta". Esto impide que los usuarios entren dos veces en el lienzo después de una fecha de entrada específica (número total de días después del envío del último mensaje desde el lienzo original más la ventana de conversión). 
- **El siguiente método consumirá puntos de datos.** Actualiza el Canvas original para incluir un webhook Braze-to-Braze que active un atributo personalizado de fecha y hora al entrar. Este atributo puede utilizarse para impedir que los usuarios entren en el nuevo lienzo después de la fecha especificada (número total de días transcurridos desde el envío del último mensaje desde el lienzo original más la ventana de conversión).

En el caso de los lienzos activados por la API, coordine con su equipo de ingeniería para asegurarse de que estos lienzos utilizan el nuevo ID de lienzo cuando los nuevos lienzos estén listos para su lanzamiento.

Para más información sobre las diferencias entre el editor original de Canvas y la experiencia Canvas Flow, consulta [las preguntas frecuentes sobre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


