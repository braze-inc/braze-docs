---
nav_title: Locales en los mensajes
article_title: Locales en los mensajes
page_order: 6.3
description: "En este artículo se explican los pasos necesarios para utilizar las configuraciones regionales en la mensajería."
---

# Configuraciones regionales de mensajería

> Una vez añadidas las configuraciones regionales a su espacio de trabajo, podrá dirigirse a usuarios de distintos idiomas en un solo mensaje de correo electrónico.

## Requisitos previos

Para editar y administrar [el soporte multilingüe]({{site.baseurl}}/multi_language_support/), debes tener el permiso de usuario "Administrar configuración multilingüe". Para añadir la configuración regional a un mensaje, necesitarás permisos para editar campañas.

{% alert important %}
El soporte multilingüe y las localizaciones en los mensajes están actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Usar configuraciones regionales

Para utilizar las localizaciones en sus mensajes, redacte una campaña de correo electrónico o Canvas. Seleccione el editor HTML o el editor de arrastrar y soltar y, a continuación, siga los pasos en función de su editor.

{% tabs %}
{% tab Editor HTML %}

1. Resalta el texto que quieres traducir. Selecciona **Insertar etiqueta de traducción**. Esto envolverá tu texto con etiquetas de traducción. <br>![Editor HTML con una localización seleccionada.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Guarda el mensaje como borrador.
3. Seleccione **Multilenguaje** y añada sus idiomas para el mensaje utilizando el menú desplegable.
4. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. Después, rellena las traducciones en el archivo CSV. <br>![Un ejemplo de archivo CSV de traducción.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Seleccione **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endtab %}
{% tab Editor de arrastrar y soltar %}

1. Añada etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Editor de arrastrar y soltar con dos ID de traducción.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Después de añadir las etiquetas, guarda tu mensaje como borrador.
4. Seleccione **Multilenguaje** y añada sus idiomas para el mensaje utilizando el menú desplegable.
5. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. 
6. Rellena las traducciones en el archivo CSV. Si has copiado y pegado las etiquetas de traducción directamente desde el Paso 1, puede que tengas que eliminar `<code>` de la columna **Etiquetas de traducción** del archivo CSV.
7. Seleccione **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endtab %}
{% endtabs %}

Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.

## Vista previa de tus configuraciones regionales

En la sección **Vista previa y prueba**, selecciona **Usuario multilingüe** para comprobar si tu mensaje se traduce como esperabas.

## Administrador de traducciones

### Edición de traducciones para campañas lanzadas y Lonas

Después de lanzar una campaña o un Canvas, puedes seguir modificando las traducciones cuando estés en modo borrador. Esto se aplica tanto si estás editando traducciones directamente en el compositor, mediante carga CSV o a través de la API. 

Antes de realizar cualquier actualización de la traducción, la campaña o el Canvas deben guardarse primero como borrador.

1. Selecciona **Editar campaña/Canvas** y luego haz tus ediciones en el compositor.
2. Selecciona **Guardar como borrador** y, a continuación, selecciona **Sí** en el modal.
3. Ve al paso **Resumen de revisión** y selecciona **Actualizar campaña/Canvas**.
4. Selecciona **Actualizar campaña/Canvas** en el modal.

Para más detalles sobre la gestión de campañas y Canvas después del lanzamiento, consulta [Editar campañas lanzadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) y [borradores de Canvas y edición posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicar pasos en Canvas o campañas, y traducciones

Al duplicar un paso en Canvas o una campaña, ya sea en el modo borrador tras el lanzamiento o durante la creación inicial, las traducciones asociadas a ese paso no se transferirán. Hay que añadir las traducciones necesarias al nuevo paso o campaña. Asegúrate de revisar y actualizar las traducciones en consecuencia cuando realices modificaciones en tu Canvas o campaña.

### Utilizar la API multilingüe con Lienzos

Para utilizar [la API multilingüe con los Lienzos]({{site.baseurl}}/api/endpoints/translations/), debes incluir las direcciones `workflow_id`, `step_id`, y `message_variation_id` en la lista de parámetros.

#### Pasos en Canvas añadidos a los borradores posteriores al lanzamiento

Cuando utilices la API multilingüe con pasos en Canvas creados después de haber lanzado el Canvas, el `message_variation_id` que pases a la API estará vacío o en blanco.

{% multi_lang_include locales.md section="Preguntas frecuentes" %}