---
nav_title: Biblioteca de bloques de contenido
article_title: Biblioteca de bloques de contenido
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo utilizar la biblioteca de bloques de contenido para gestionar su contenido reutilizable y multicanal en una única ubicación centralizada."
tool: 
  - Templates
  - Media

---

# Biblioteca de bloques de contenido

> La biblioteca de bloques de contenido le permite gestionar sus contenidos reutilizables y multicanal en una única ubicación centralizada.

Con los bloques de contenido, puede:

- Cree un aspecto coherente para sus campañas de correo electrónico utilizándolos como encabezados y pies de página.
- Distribuya los mismos códigos de oferta a través de distintos canales.
- Cree activos predefinidos que puedan utilizarse para construir mensajes con información y activos coherentes.
- Copiar cuerpos de mensaje completos en otros mensajes.

## Crear un bloque de contenido

Existen dos tipos de editores para crear un bloque de contenido: el clásico y el de arrastrar y soltar. Estos dos tipos de editores corresponden al tipo de Bloque de Contenido: HTML y arrastrar y soltar. También puedes crear y gestionar tus bloques de contenido [a través de la API][5].

{% tabs %}
{% tab Arrastrar y soltar %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Especificaciones del bloque de contenidos

| Atributo del bloque de contenido | Especificaciones |
|---|---|
| Apellidos | Campo obligatorio con un máximo de 100 caracteres. No se puede cambiar el nombre después de guardar el bloque de contenido. Además, no puede asignar a un nuevo Bloque de contenido el mismo nombre que a un Bloque de contenido anterior, aunque el anterior se haya archivado. |
| Descripción | (opcional) Máximo 250 caracteres. Describa el Bloque de contenido para que otros usuarios de Braze sepan para qué sirve y dónde se utiliza. |
| Tamaño del contenido | Máximo de 50kB (kilobyte). |
| Colocación | Los bloques de contenido no pueden utilizarse en el pie de página de un correo electrónico. |
| Creación | Editor HTML o editor de arrastrar y soltar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Al crear bloques de contenido, a veces resulta útil visualizar HTML y Liquid añadiendo saltos de línea. Si se dejan estos saltos de línea durante el envío, se corre el riesgo de tener espacios extraños que pueden afectar a la representación del bloque. Para evitarlo, utiliza la etiqueta **Capturar** en tu bloque junto con el filtro ** de banda |**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Uso de bloques de contenido

Después de crear tu Bloque de Contenido, puedes insertarlo en tus mensajes siguiendo estos pasos: 

1. Copie la **etiqueta Liquid del bloque de contenido** de la sección **Detalles del bloque de contenido**.
2. Inserta la etiqueta de Liquid del bloque de contenido en el mensaje. También puede empezar a escribir el Líquido y hacer que la etiqueta se rellene automáticamente.

{% alert note %}
Las propiedades de entrada del lienzo y las propiedades de eventos sólo se admiten en un lienzo, no en el bloque de contenido.
{% endalert %}

### Actualizar y copiar bloques de contenido

Si eliges actualizar un Bloque de contenido, se actualizará en todos los mensajes en los que se utilice el Bloque de contenido si se inserta a través de Liquid. Si el bloque de contenido se importa mediante el menú desplegable **Bloques de contenido** en **Filas** del editor de arrastrar y soltar, no se actualizará en todos los mensajes.

Si quieres actualizar un Content Block para un solo mensaje o hacer una copia para utilizarla en otros mensajes, puedes copiar el HTML del mensaje original al nuevo o editar el Content Block original (debe haberse utilizado ya en un mensaje) y guardarlo. Aparecerá un aviso que le permitirá guardarlo como un nuevo Bloque de Contenido.

Después de editar un bloque de contenido, puede guardarlo y ejecutarlo haciendo clic en **Ejecutar bloque de contenido**. También puede seleccionar **Más** > **Duplicar** para crear un duplicado de su Bloque de contenido.

![][2]

También puede [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) un Bloque de contenido. Esto crea una copia borrador del Bloque de Contenido.

### Previsualización de bloques de contenido

Después de añadir un Bloque de Contenido en una campaña o Lienzo activo, puedes previsualizar este Bloque de Contenido desde la Biblioteca de Bloques de Contenido pasando el ratón por encima del Bloque de Contenido y seleccionando el icono <i class="fa fa-eye preview-icon"></i> **Preview**. 

Esta vista previa incluye información sobre el bloque de contenido, como quién lo creó, etiquetas, fecha de creación, fecha de la última edición, descripción, tipo de editor, recuento de inclusiones con detalles y una vista previa real del bloque de contenido.

![][7]{: style="max-width:60%;"} 

### Anidamiento de bloques de contenido

Los bloques de contenido pueden anidarse, pero sólo una vez. Puede anidar el bloque de contenido A en el bloque de contenido B, pero no podrá anidar el bloque de contenido B en el bloque de contenido C.

{% alert warning %}
Nada le impedirá anidar un tercer nivel de Bloque de Contenido, pero no verá expandirse el contenido en los anidados más allá del segundo. El contenido y el fragmento de Liquid se eliminan del mensaje.
{% endalert %}

Además, los bloques de contenido no pueden utilizarse dentro de un pie de página de correo electrónico, aunque sí pueden utilizarse dentro de bloques de contenido.

### Archivar bloques de contenido

![Menú desplegable de Configuración ampliado que muestra tres opciones: Archivar, Duplicar y Copiar en espacio de trabajo.][3]{: style="max-width:20%;float:right;margin-left:15px;" }

Una vez que haya terminado de utilizar un Bloque de contenido, puede archivarlo desde la página [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/). Los bloques de contenido archivados son de sólo lectura, así que desarchívelos antes de editarlos. Los bloques de contenido no pueden archivarse si se utilizan en algún mensaje.

#### Buenas prácticas

- Si el bloque sólo se utiliza en unos pocos mensajes de correo electrónico, recomendamos archivar el bloque obsoleto y actualizar los mensajes en directo con un bloque más reciente que no se haya archivado.
- Cuando tu bloque solo tiene una errata o necesita un cambio menor, no recomendamos archivarlo. ¡Solo tienes que actualizar y enviar!
- Cuando su bloque se utiliza en más mensajes de los que puede gestionar razonablemente con la primera sugerencia de esta lista, le recomendamos que elimine todo el contenido del bloque y luego lo archive. Esto garantizará que no se incluya información obsoleta en los nuevos correos electrónicos enviados.
- Si accidentalmente archivas un bloque de contenido, puedes desarchivarlo.

![Panel de bloques de contenido guardados en el que el menú desplegable de configuración de "Test_32" se amplía para mostrar tres opciones: Desarchivar, duplicar y copiar en el espacio de trabajo][4]

[2]: {% image_buster /assets/img/copy-content-block.png %}
[3]: {% image_buster /assets/img/template_archive_cog.png %}
[4]: {% image_buster /assets/img/unarchive-content-block.png %}
[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[7]: {% image_buster /assets/img/preview_tab_content_block.png %}
