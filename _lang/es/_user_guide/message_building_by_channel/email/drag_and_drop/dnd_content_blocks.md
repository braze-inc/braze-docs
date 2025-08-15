---
nav_title: Bloques de contenido
article_title: Editor de arrastrar y soltar Bloques de contenido
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Este artículo de referencia explica cómo crear y utilizar bloques de contenido en el editor de arrastrar y soltar."
tool: Media

---

# Editor de arrastrar y soltar Bloques de contenido

> Los Bloques de contenido utilizados exclusivamente en el editor de arrastrar y soltar son similares en funcionalidad a los [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilizados en los distintos canales. Son una ubicación centralizada para guardar información a la que se puede hacer referencia en diversas campañas de correo electrónico. Esto puede incluir la agrupación de encabezados de correo electrónico, llamadas promocionales y más, todo en una fila reutilizable.

{% alert note %}
Los Bloques de contenido de arrastrar y soltar sólo están disponibles para su uso en campañas de correo electrónico y mensajes de correo electrónico en Canvas.
{% endalert %}

## Creación de un bloque de contenido

Para crear un Bloque de contenido, haz lo siguiente:

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Cada bloque de contenido de arrastrar y soltar está limitado a una fila. Sin embargo, puede utilizar los bloques del editor de arrastrar y soltar para construir y personalizar el Bloque de contenido y adaptarlo a su mensaje de correo electrónico.
{% endalert %}

## Uso de un bloque de contenido

Hay dos formas de añadir el Bloque de contenido a tu correo electrónico: utilizando el editor o utilizando Liquid.

### Uso del editor para añadir un bloque de contenido

Para añadir un Bloque de Contenido en el editor, haga lo siguiente:

1. Vaya a la pestaña **Filas** del editor y seleccione **Bloques de contenido**. 
2. Arrastre y suelte su Bloque de contenido en el editor de correo electrónico. 
3. (Opcional) Ajusta la anchura de tu Bloque de contenido seleccionando el botón en el menú de navegación. La anchura predeterminada es 100%. <br><br>![Una flecha de doble cara con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width.png %}){: style="max-width:30%;" }<br><br>

Después de añadir el Bloque de contenido al editor de correo electrónico, puedes realizar ediciones en el Bloque de contenido que no afectarán al Bloque de contenido original que creaste en **Plantillas y medios.** Esto se debe a que los Bloques de contenido añadidos mediante arrastrar y soltar no están vinculados al Bloque de contenido original. Para ver los cambios realizados en el Bloque de contenido original, arrástrelo de nuevo al editor de correo electrónico. 

Puede producirse una desalineación en el editor de arrastrar y soltar cuando se añaden varios bloques de contenido a un único bloque de fila. Pruebe a utilizar bloques de fila separados para mantener la alineación del contenido a nivel de fila.

### Uso de Liquid para añadir un bloque de contenido

Para añadir un bloque de contenido mediante Liquid, haga lo siguiente:

1. Vaya a su campaña de correo electrónico y seleccione **Editar cuerpo de correo electrónico**. 
2. Haga clic en <i class="fas fa-plus"></i> **Personalización**.
3. Localice la pestaña **Añadir personalización** y seleccione **Bloques de contenido** en el desplegable **Tipo de personalización**.
4. Seleccione el nombre de su Bloque de Contenido en el campo **Atributo**. El campo del fragmento de código de Liquid se rellenará con tu etiqueta de Liquid del bloque de contenido. 
5. Copie y pegue el fragmento de Liquid en un bloque del editor de texto. <br>![La pestaña Añadir personalización con opciones.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Cuando previsualice su mensaje de correo electrónico, el fragmento de Liquid se mostrará como Bloque de contenido del editor de arrastrar y soltar. 

{% alert important %}
Cuando se añade un Bloque de contenido en el editor de correo electrónico con Liquid, este Bloque de contenido se vincula al Bloque de contenido original creado en **Plantillas y medios.** Esto significa que el Bloque de Contenido se actualizará para reflejar cualquier cambio en la plantilla original del Bloque de Contenido.
{% endalert %}

## Actualización de bloques de contenido

Para actualizar un Bloque de Contenido existente, puedes editar el Bloque de Contenido original desde la página **de Bloques de Contenido**, o copiar el HTML del mensaje original al nuevo. Las actualizaciones de una plantilla de Content Block se actualizarán en todos los mensajes de correo electrónico en los que se añada el Content Block a través de Liquid.

Para archivar un bloque de contenido, vaya a **Plantillas** > **Bloques de contenido**, seleccione el icono de elipsis vertical <i class="fas fa-ellipsis-vertical"></i> del bloque de contenido y haga clic en **Archivar**. Cuando archivas un Bloque de Contenido, tus mensajes seguirán incluyendo el contenido del bloque archivado. Sin embargo, los bloques de contenido archivados son de sólo lectura, por lo que debe desarchivarlos antes de editarlos. 

