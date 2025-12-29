---
nav_title: Bloques de contenido
article_title: Bloques de contenido del editor de arrastrar y soltar
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Este artículo de referencia explica cómo crear y utilizar bloques de contenido en el editor de arrastrar y soltar."
tool: Media

---

# Editor de arrastrar y soltar Bloques de contenido

> Los bloques de contenido utilizados exclusivamente en el editor de arrastrar y soltar son similares en funcionalidad a los [bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilizados en los distintos canales. Son una ubicación centralizada para guardar información a la que se puede hacer referencia en varias campañas de correo electrónico. Esto puede incluir agrupar cabeceras de correo electrónico, llamadas promocionales y más, todo en una fila reutilizable.

{% alert note %}
Los bloques de contenido de arrastrar y soltar sólo están disponibles para su uso en campañas de correo electrónico y mensajes de correo electrónico en Canvas.
{% endalert %}

## Crear un bloque de contenido

Para crear un Bloque de contenido, haz lo siguiente:

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Cada bloque de contenido de arrastrar y soltar está limitado a una fila. Sin embargo, puedes utilizar bloques de editor de arrastrar y soltar para construir y personalizar el bloque de contenido y adaptarlo a tu mensajería electrónica.
{% endalert %}

## Utilizar un bloque de contenido

Hay dos formas de añadir el Bloque de contenido a tu correo electrónico: utilizando el editor o utilizando Liquid.

### Utilizar el editor para añadir un bloque de contenido

Para añadir un Bloque de contenido en el editor, haz lo siguiente:

1. Ve a la pestaña **Filas** del editor y selecciona **Bloques de contenido**. 
2. Arrastra y suelta tu bloque de contenido en el editor de correo electrónico. 
3. (Opcional) Ajusta la anchura de tu Bloque de contenido seleccionando el botón en el menú de navegación. La anchura predeterminada es 100% cuando no se especifica en la configuración global de estilo de tu correo electrónico; de lo contrario, se respetará la configuración global. <br><br>\![Una flecha de doble cara con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

Después de añadir el Bloque de contenido al editor de correo electrónico, puedes realizar ediciones en el Bloque de contenido que no afectarán al Bloque de contenido original que creaste en **Plantillas & Medios**. Esto se debe a que los Bloques de contenido añadidos mediante arrastrar y soltar no están vinculados al Bloque de contenido original. Para ver los cambios realizados en el bloque de contenido original, arrástralo de nuevo al editor de correo electrónico. 

Puede producirse una desalineación en el editor de arrastrar y soltar cuando se añaden varios bloques de contenido a un único bloque de fila. Prueba a utilizar bloques de fila separados para mantener la alineación de tu contenido a nivel de fila.

### Utilizar Liquid para añadir un bloque de contenido

Para añadir un bloque de contenido utilizando Liquid, haz lo siguiente:

1. Ve a tu campaña de correo electrónico y selecciona **Editar cuerpo del correo electrónico**. 
2. Haz clic en <i class="fas fa-plus"></i> **Personalización**.
3. Localiza la pestaña **Añadir personalización** y selecciona **Bloques de contenido** en el desplegable **Tipo de personalización**.
4. Selecciona el nombre de tu Bloque de Contenido en el campo **Atributo**. El campo del fragmento de Liquid se rellenará con tu etiqueta de Liquid del bloque de contenido. 
5. Copia y pega el fragmento de código de Liquid en un bloque de editor de texto. <br>\![La pestaña Añadir personalización con opciones.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Cuando previsualices tu mensajería electrónica, el fragmento de código Liquid se mostrará como el bloque de contenido del editor de arrastrar y soltar. 

{% alert important %}
Cuando se añade un Bloque de contenido en el editor de correo electrónico con Liquid, este Bloque de contenido se vincula al Bloque de contenido original creado en **Plantillas & Medios**. Esto significa que el Bloque de contenido se actualizará para reflejar cualquier cambio en la plantilla original del Bloque de contenido.
{% endalert %}

## Actualizar bloques de contenido

Para actualizar un bloque de contenido existente, puedes editar el bloque de contenido original desde la página **Bloques de contenido**, o copiar el HTML del mensaje original al nuevo. Las actualizaciones de una plantilla de Bloque de contenido se actualizarán en todos los mensajes de correo electrónico en los que se añada el Bloque de contenido a través de Liquid.

Para archivar un bloque de contenido, ve a **Plantillas** > **Bloques de contenido**, selecciona el icono de elipsis vertical <i class="fas fa-ellipsis-vertical"></i> para el bloque de contenido y haz clic en **Archivar**. Cuando archives un bloque de contenido, tus mensajes seguirán incluyendo el contenido del bloque archivado. Sin embargo, los Bloques de contenido archivados son de sólo lectura, así que desarchiva el Bloque de contenido antes de editarlo. 

