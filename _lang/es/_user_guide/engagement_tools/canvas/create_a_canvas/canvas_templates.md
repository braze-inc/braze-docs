---
nav_title: Crear una plantilla de Canvas
article_title: Crear una plantilla de Canvas
alias: "/canvas_templates/"
page_order: 0.5
description: "Este artículo de referencia explica cómo crear una plantilla para Canvas."
page_type: reference
---

# Crear una plantilla Canvas

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
Si utilizas la navegación antigua, puedes encontrar esta página en **Interacción** > **plantillas y medios** > **plantillas Canvas**.
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

Braze dispone de una selección de plantillas de Canvas que puedes consultar y utilizar como mejores prácticas para casos de uso comunes. Aunque estas plantillas no se pueden editar, puedes verlas en **Plantillas** > **Plantillas Braze** o utilizarlas en tus Lienzos.

![Plantillas Braze en la sección de plantillas Canvas con seis plantillas disponibles.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecciona una de las siguientes plantillas disponibles para utilizarla como referencia o como Canvas.

{% tabs %}
{% tab Intención abandonada %}

Interactúa con los usuarios en tiempo real para animarles a completar sus compras.

Ten en cuenta lo siguiente cuando utilices esta plantilla:

- Añade una audiencia específica. Actualmente, las rutas de audiencia se desencadenan basándose en "Realizada cualquier compra", pero puedes adaptar esto a productos específicos a los que quieras dirigirte.
- Esta plantilla asume que tienes un recorrido post-compra separado, por lo que realizar una compra hará que los usuarios salgan del Canvas.
- Rellena los datos en el paso Sincronizar audiencia.

{% endtab %}
{% tab De nuevo en stock %}

Impulsa las compras notificando a tus usuarios cuando un artículo vuelve a estar disponible con mensajes personalizados. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En **Programa de entradas**, selecciona un catálogo para utilizarlo. Esto te permite acceder a datos, como productos, descuentos y promociones, para dirigirte más a tus usuarios.
- En **Audiencia objetivo**, añade un segmento para dirigirte a los usuarios que indicaron interés por un determinado artículo.
- En los pasos de Mensaje en todo el Canvas, actualiza el Liquid para hacer referencia a tu catálogo.

{% endtab %}
{% tab Adopción de características %}

Entrega oportunamente mensajes personalizados para destacar las ventajas y consejos de uso. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- Excluye a los usuarios que ya hayan utilizado el producto. Por ejemplo, en **Audiencia objetivo**, añade un filtro en 
-  Para utilizar el paso de ruta de experimentos, define un evento de conversión. Este acontecimiento debe ser el que señale la adopción de la característica.
- Configura el paso Ruta de acción en la plantilla con eventos personalizados para "Característica activada" y "Recorrido realizado".
- Configura los atributos personalizados en el paso Mensaje llamado "Encuesta de opinión" para captar el sentimiento de la opinión.

{% endtab %}
{% tab Usuario caducado %}

Haz que los usuarios vuelvan a tu aplicación con incentivos basados en sus interacciones anteriores. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En **Conceptos básicos**, selecciona una aplicación específica para realizar el seguimiento de las conversiones.
- En el editor Canvas, añade aplicaciones específicas para los pasos de las Rutas de acción.
- Configura el paso Sincronización de audiencias con los socios y audiencias para tu caso de uso.

{% endtab %}
{% tab Incorporación %}

Crea trayectos de incorporación que promuevan una fuerte adopción inicial y fomenten relaciones duraderas con tus usuarios. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En el paso Rutas de audiencia denominado "División de la audiencia", considera la posibilidad de personalizar las acciones clave para los usuarios comprometidos. En la plantilla, el filtro de segmento es "Ha hecho clic en el correo electrónico para el paso Correo electrónico de bienvenida".

{% endtab %}
{% tab Comentarios posteriores a la compra %}

Orquesta experiencias personalizadas que te permitan responder a los comentarios y establecer relaciones con tus usuarios. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En el primer paso del editor Canvas:
    - Especifica los atributos personalizados en el mensaje dentro de la aplicación para indicar el sentimiento de la respuesta en función de la opción de cuestionario seleccionada. 
    - Especifica atributos en los enlaces de cada llamada a la acción para captar qué opción se selecciona. Se hace referencia a estos atributos en la ruta de audiencia posterior.
- Personaliza la ruta de audiencia con los atributos del primer paso de esta plantilla.
- Configura el paso de Sincronización de audiencias denominado "Reorientación de anuncios".

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener una guía paso a paso para crear un Canvas de ejemplo utilizando estas plantillas Braze, consulta [Utilizar plantillas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

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

