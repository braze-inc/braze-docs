---
nav_title: Biblioteca de bloques de contenido
article_title: Biblioteca de bloques de contenido
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo utilizar la biblioteca de bloques de contenido para gestionar tus contenidos reutilizables y de canales cruzados en una ubicación única y centralizada."
tool: 
  - Templates
  - Media

---

# Biblioteca de bloques de contenido

> La biblioteca de bloques de contenido te permite gestionar tus contenidos reutilizables y de canales cruzados en una ubicación única y centralizada.

Con los bloques de contenido, puedes:

- Crea un aspecto coherente para tus campañas de correo electrónico utilizándolos como encabezados y pies de página.
- Distribuye los mismos códigos de oferta a través de distintos canales.
- Crea activos predefinidos que puedan utilizarse para construir mensajes con información y activos coherentes.
- Copia el cuerpo completo de los mensajes en otros mensajes.

## Crear un bloque de contenido

Hay dos tipos de editores para crear un Bloque de contenido: el clásico y el de arrastrar y soltar. Estos dos tipos de editores se corresponden con el tipo de Bloque de contenido: HTML y arrastrar y soltar. También puedes crear y gestionar tus bloques de contenido [utilizando la API]({{site.baseurl}}/api/endpoints/templates/).

{% tabs %}
{% tab Drag-and-drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Especificaciones del bloque de contenido

| Atributo del bloque de contenido | Especificaciones |
|---|---|
| Nombre | Campo obligatorio con un máximo de 100 caracteres. No se puede renombrar una vez guardado el Bloque de contenido. Además, no puedes nombrar un nuevo Bloque de contenido con el mismo nombre que un Bloque de contenido anterior, aunque el anterior se haya archivado. |
| Descripción | (opcional) Máximo de 250 caracteres. Describe el Bloque de contenido para que otros usuarios de Braze sepan para qué sirve y dónde se utiliza. |
| Tamaño del contenido | Máximo de 50 KB. |
| Colocación | Los bloques de contenido no pueden utilizarse dentro de un pie de página de correo electrónico. |
| Creación | Editor HTML o editor de arrastrar y soltar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Al crear bloques de contenido, puede ser beneficioso visualizar HTML y Liquid añadiendo saltos de línea. Si se dejan estos saltos de línea durante el envío, corres el riesgo de tener espacios extraños que pueden afectar a la representación del bloque. Para evitarlo, utiliza la etiqueta **Capturar** en tu bloque junto con el filtro ** de banda** |.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utilizar bloques de contenido

Después de crear tu bloque de contenido, puedes insertarlo en tus mensajes siguiendo estos pasos: 

1. Copia la **etiqueta de Liquid del bloque de contenido** de la sección **Detalles del bloque de contenido**.
2. Inserta la etiqueta de Liquid del bloque de contenido en el mensaje. También puedes empezar a escribir el Liquid y hacer que la etiqueta se rellene automáticamente.

### Lo que debes saber

- El uso de bloques de contenido HTML en correos electrónicos de arrastrar y soltar **o de** bloques de contenido de arrastrar y soltar en correos electrónicos HTML puede provocar problemas de representación inesperados. Esto se debe a que el editor de arrastrar y soltar genera HTML y CSS que representan dinámicamente el contenido, mientras que el editor HTML es más estático.
- Las propiedades del evento Canvas sólo se admiten en un Canvas. Si haces referencia a un bloque de contenido con propiedades de entrada de Canvas en una campaña, no se rellenará.

### Actualizar y copiar bloques de contenido

Si eliges actualizar un Bloque de contenido, se actualizará en todos los mensajes en los que se utilice el Bloque de contenido si se inserta a través de Liquid. Si el bloque de contenido se importa utilizando el desplegable **Bloques de contenido** en **Filas** del editor de arrastrar y soltar, no se actualizará en todos los mensajes.

Si quieres actualizar un Bloque de Contenido para un solo mensaje o hacer una copia para utilizarla en otros mensajes, puedes copiar el HTML del mensaje original al nuevo o editar el Bloque de Contenido original (debe haberse utilizado ya en un mensaje) y guardarlo. Aparecerá un aviso que te permitirá guardarlo como un nuevo Bloque de contenido.

Después de editar un bloque de contenido, puedes guardar e iniciar el bloque de contenido actualizado seleccionando **Iniciar bloque de contenido**. También puedes seleccionar **Más** > **Duplicar** para crear un duplicado de tu bloque de contenido.

Un bloque de contenido que dice "Bienvenido a nuestro boletín".]({% image_buster /assets/img/copy-content-block.png %})

También puedes [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) un Bloque de contenido. Esto crea una copia borrador del Bloque de contenido.

### Vista previa de los bloques de contenido

Después de añadir un Bloque de contenido en una campaña o Canvas activos, puedes obtener una vista previa de este Bloque de contenido desde la Biblioteca de Bloques de contenido pasando el ratón por encima del Bloque de contenido y seleccionando el icono <i class="fa fa-eye preview-icon"></i> **Vista previa**. 

Esta vista previa incluye información sobre el Bloque de contenido, como quién lo creó, etiquetas, fecha de creación, fecha de última edición, descripción, tipo de editor, recuento de inclusiones con detalles y una vista previa real del Bloque de contenido.

\![Vista previa de un bloque de contenido "Workout_Promo" para ciclismo y baile que tiene seis inclusiones.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### Anidamiento de bloques de contenido

Los bloques de contenido pueden anidarse, pero sólo una vez. Puedes anidar el bloque de contenido A en el bloque de contenido B, pero no podrás anidar el bloque de contenido B en el bloque de contenido C.

{% alert warning %}
Nada te impedirá anidar un tercer nivel de Bloque de contenido, pero no verás que el contenido se expande en los anidados más allá del segundo. El contenido y el fragmento de código Liquid se eliminan del mensaje.
{% endalert %}

Además, los Bloques de contenido no pueden utilizarse dentro de un pie de página de correo electrónico, aunque los pies de página de correo electrónico pueden utilizarse dentro de Bloques de contenido.

### Archivar bloques de contenido

Menú desplegable de configuración ampliado que muestra tres opciones: Archivar, Duplicar y Copiar en el espacio de trabajo.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Cuando hayas terminado de utilizar un bloque de contenido, puedes archivarlo desde la página [Plantillas & Medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/). Los bloques de contenido archivados son de sólo lectura, así que desarchiva el bloque de contenido antes de editarlo. Los bloques de contenido no pueden archivarse si se utilizan en algún mensaje.

#### Buenas prácticas

- Cuando tu bloque sólo se utilice en unos pocos correos electrónicos, te recomendamos archivar el bloque obsoleto y actualizar tus mensajes en vivo con un bloque más nuevo que no se haya archivado.
- Cuando tu bloque sólo tiene una errata o necesita un cambio menor, no recomendamos archivarlo. En lugar de eso, ¡actualiza el bloque y empieza a enviar!
- Cuando tu bloque se utiliza en más mensajes de los que puedes gestionar razonablemente con la primera sugerencia de esta lista, te recomendamos eliminar todo el contenido del bloque y archivarlo. Esto garantizará que no se incluya información obsoleta en los nuevos correos electrónicos enviados.
- Si accidentalmente archivas un bloque de contenido, puedes desarchivarlo.

\![Panel de bloques de contenido guardados donde el menú desplegable de configuración de "Test_32" se amplía para mostrar tres opciones: Desarchivar, Duplicar y Copiar en el espacio de trabajo]({% image_buster /assets/img/unarchive-content-block.png %})

