---
nav_title: Crea una plantilla Canvas
article_title: Crear una plantilla de Canvas
alias: "/canvas_templates/"
page_order: 0.5
description: "Este artículo de referencia explica cómo crear una plantilla para Canvas."
page_type: reference
---

# Crea una plantilla Canvas

> Este artículo de referencia explica cómo crear y administrar plantillas para Canvas. El uso de plantillas puede perfeccionar tu mensajería creando un marco coherente que puede personalizarse fácilmente para ajustarse a tus objetivos específicos en todos tus Lienzos.

{% alert tip %}
¡Ahorra tiempo y agiliza tu creación de Canvas utilizando [las plantillas de Braze](#available-braze-templates) Canvas! Navega por nuestra biblioteca de plantillas prediseñadas para encontrar una que se adapte a tu caso de uso y personalízala para satisfacer tus necesidades específicas.
{% endalert %}

## Método 1: Crear a partir de un Canvas existente

### Paso 1: Selecciona tu Canvas actual

En el panel de Braze, ve a **Mensajería** > **Canvas** y selecciona un Canvas existente que quieras utilizar como plantilla.

### Paso 2: Crea tu plantilla

En el editor de Canvas, selecciona **Editar Canvas** o **Editar borrador**, dependiendo de si tu Canvas está activo o en borrador. Despliega el desplegable **Guardar como borrador** en el pie de página y selecciona **Guardar como plantilla**.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Paso 3: Guarda tu plantilla

A continuación, da un nombre a tu plantilla y añade las etiquetas pertinentes. A continuación, selecciona **Guardar**. Tu plantilla ya está lista para utilizarla para crear un Canvas, lo que te da una ventaja con la configuración básica y los pasos ya establecidos.

## Método 2: Crear mediante el editor de plantillas Canvas

### Paso 1: Ve al editor de plantillas Canvas

En el panel de Braze, ve a **Plantillas** > **Plantillas Canvas**.

{% alert note %}
Si utilizas la navegación antigua, puedes encontrar esta página en **Interacción** > **Plantillas & Medios** > Plantillas Canvas.
{% endalert %}

### Paso 2: Crear una plantilla nueva

Selecciona **Crear plantilla** y comienza a configurar los detalles de tu Canvas. Puedes empezar dando un nombre a tu plantilla Canvas.

![Una plantilla Canvas de ejemplo llamada "Plantilla Canvas de venta anual" con la descripción "Utilizar para la promoción anual de primavera".]({% image_buster /assets/img/canvas_template_example.png %})

### Paso 3: Personaliza tu plantilla

A continuación, personaliza tu plantilla [configurando tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). Puedes decidir cuándo deben entrar los usuarios en el Canvas, determinar qué usuarios pueden entrar en este Canvas, ajustar tu configuración de envío y construir tu recorrido de usuario para la plantilla.

### Paso 4: Guarda tu plantilla

Cuando hayas terminado de personalizar tu plantilla, selecciona el botón **Guardar plantilla**. En la página de **la plantilla** Canvas, puedes ver los detalles de tu plantilla Canvas seleccionando <i class="fas fa-list"></i> **Detalles de la plantilla**. 

## Utilizar plantillas Canvas

Hay dos formas de utilizar tu plantilla al componer un Canvas:

- **De mensajería**: Ve a **Mensajería** > **Canvas**. Selecciona el botón **Crear Canvas** y **Utilizar una plantilla de Canvas**.
- **De plantillas**: Ve a **Plantillas** > **Plantillas Canvas** y busca la plantilla que desees. A continuación, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> seguido de **Aplicar plantilla**. Esto te llevará a un nuevo Canvas con la plantilla aplicada en el compositor de Canvas.

### Plantillas Braze disponibles

Para ver una lista de las plantillas de Canvas disponibles, consulta [Plantillas de Canvas]({{site.baseurl}}/canvas_templates/templates/). Para más detalles sobre el uso de las plantillas Canvas de eCommerce, consulta [Cómo utilizar los eventos recomendados por eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

## Administrador de plantillas Canvas

Las plantillas de Canvas pueden duplicarse y archivarse, de forma similar a un Canvas real. Para editar una plantilla de Canvas, selecciona la plantilla y luego **<i class="fas fa-pencil-alt"></i>Editar**.

A nivel de espacio de trabajo, puedes actualizar los permisos de usuario para permitir o limitar el acceso para crear, editar, ver o archivar plantillas de Canvas.

### Permisos para equipos y espacios de trabajo

Para permitir que sólo determinados usuarios accedan a determinadas plantillas de Canvas y las utilicen, [añade un equipo]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) a las plantillas y, a continuación, asigna permisos de "Acceso a campañas, lienzos, tarjetas de contenido, bloques de contenido, indicadores de características, segmentos, biblioteca multimedia y centro de preferencias" a nivel de equipo.

Si asignas alguno de los siguientes permisos a nivel de equipo, pero no a nivel de espacio de trabajo, sólo podrás hacer lo siguiente asignado a tu equipo:

- Crea y edita plantillas Canvas
- Ver plantillas Canvas
- Archivo Plantillas Canvas

Si se conceden permisos tanto a nivel de espacio de trabajo como de equipo, se dará prioridad a los permisos a nivel de espacio de trabajo.

## Preguntas más frecuentes

### ¿Puedo guardar un paso incompleto en una plantilla Canvas?

Sí, puedes guardar pasos incompletos como plantilla de Canvas. Sin embargo, cuando se utilice la plantilla, habrá un error en el botón **Guardar plantilla** que indica lo que se necesita para lanzar el Canvas.

### ¿Puedo guardar la configuración de mi constructor de Canvas como una plantilla o sólo puedo guardar los pasos? 

Sí, puedes guardar configuraciones en el constructor de Canvas dentro de una plantilla de Canvas. Por ejemplo, si piensas utilizar a menudo una combinación de segmentos y filtros, puedes guardar esta configuración de **audiencia objetivo** como parte de tu plantilla de Canvas.

