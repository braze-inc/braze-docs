---
nav_title: Localizaciones en los mensajes
article_title: Localizaciones en los mensajes
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artículo te explica cómo utilizar las localizaciones en tus mensajes."
---

# Localizaciones en los mensajes

> Después de añadir localizaciones a tu espacio de trabajo, puedes dirigirte a usuarios en diferentes idiomas con un solo push, correo electrónico o mensaje dentro de la aplicación.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
El soporte multilingüe y las localizaciones en los mensajes están actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Utilizar locales

{% tabs %}
{% tab In-app message %}

Para utilizar localizaciones en tus mensajes, compón una campaña de mensajería dentro de la aplicación o Canvas. Selecciona el editor de arrastrar y soltar o el editor tradicional, y luego sigue los pasos según tu editor.

{% subtabs %}
{% subtab traditional editor %}

1. Añade etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %}

\![Editor tradicional con ID de traducción.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Después de añadir las etiquetas, guarda tu mensaje como borrador.
4\. Selecciona **Gestionar idiomas** y añade tus localizaciones para el mensaje utilizando el desplegable.

\!["Gestionar idiomas" modal con una configuración regional seleccionada.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. Después, rellena las traducciones en el archivo CSV.

\![Un ejemplo de archivo CSV de traducción.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Selecciona **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Añade etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %} 

\![Editor de arrastrar y soltar con dos ID de traducción.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Después de añadir las etiquetas, guarda tu mensaje como borrador y vuelve a abrir el editor.
4\. En el panel **Construir**, selecciona **Multiidioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
5\. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. 

\!["Panel multilingüe" con botón para descargar la plantilla.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Rellena las traducciones en el archivo CSV. Si has copiado y pegado las etiquetas de traducción directamente desde el Paso 1, puede que tengas que eliminar `<code>` de la columna **Etiquetas de traducción** del archivo CSV.
7\. Selecciona **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

Panel "Multiidioma" con botones para descargar la plantilla y subir traducciones.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Email %}

Para utilizar las localizaciones en tus mensajes, redacta una campaña de correo electrónico o Canvas. Selecciona el editor HTML o el editor de arrastrar y soltar, y sigue los pasos según tu editor.

{% subtabs %}
{% subtab HTML editor %}

1. Resalta el texto que quieres traducir. Selecciona **Insertar etiqueta de traducción**. Esto envolverá tu texto con etiquetas de traducción. <br>\![Editor HTML con una localización seleccionada.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Guarda el mensaje como borrador.
3. Selecciona **Multiidioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
4. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. Después, rellena las traducciones en el archivo CSV. <br>\![Un ejemplo de archivo CSV de traducción.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Selecciona **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Añade etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %} <br>\![Editor de arrastrar y soltar con dos ID de traducción.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Después de añadir las etiquetas, guarda tu mensaje como borrador.
4. Selecciona **Multiidioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
5. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. 
6. Rellena las traducciones en el archivo CSV. Si has copiado y pegado las etiquetas de traducción directamente desde el Paso 1, puede que tengas que eliminar `<code>` de la columna **Etiquetas de traducción** del archivo CSV.
7. Selecciona **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Push %}

Para utilizar localizaciones en tu mensajería, compón una campaña push o Canvas, y luego completa lo siguiente:

1. Añade etiquetas de traducción {% raw %}`{% translation id1%}` y `{% endtranslation %}`{% endraw %} para envolver todas las URL de texto, imagen o enlace que se vayan a traducir. Cada ID de traducción (`id1`) debe ser único.

\![Creador de notificaciones push con etiquetas de traducción añadidas a los campos de título y mensaje.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Guarda tu mensaje como borrador.
3\. Selecciona **Gestionar idioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
4\. Selecciona **Descargar plantilla** y, a continuación, rellena las traducciones dentro de la plantilla CSV.

\![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Para cargar la plantilla CSV completada, selecciona **Cargar traducciones**. 

La ventana "Mensajes multilingües" con dos idiomas seleccionados y botones para descargar una plantilla o subir traducciones.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

{% endtab %}
{% endtabs %}

Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

## Vista previa de tus localizaciones

{% tabs %}
{% tab In-app message %}

En el desplegable **Vista previa del mensaje como usuario**, dentro de la pestaña **Prueba**, selecciona **Usuario personalizado** e introduce distintos idiomas para previsualizar el mensaje y comprobar si tu mensaje se traduce como esperabas.


{% endtab %}
{% tab Email %}

En la sección **Vista previa & Prueba**, selecciona **Usuario multilingüe** para comprobar si tu mensaje se traduce como esperabas.

{% endtab %}
{% tab Push %}

En el desplegable **Vista previa del mensaje como usuario**, dentro de la pestaña **Prueba**, selecciona **Usuario personalizado** e introduce distintos idiomas para previsualizar el mensaje y comprobar si tu mensaje se traduce como esperabas.

{% endtab %}
{% endtabs %}

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

## Preguntas más frecuentes

#### ¿Puedo modificar la copia traducida en una de mis localizaciones?
Sí. Primero, haz la edición en el CSV, y luego vuelve a subir el archivo para hacer un cambio en la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Puedo añadir estilos HTML en las etiquetas de traducción?
Sí, pero asegúrate de que el estilo HTML no se traduce con el contenido.

#### ¿Qué validaciones o comprobaciones adicionales hace Braze?

| Escenario                                                                                                                                                 | Validación en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Falta un archivo de traducción de las localizaciones asociadas al mensaje actual.                                                                               | Este archivo de traducción no se cargará.                                                                       |
| En un archivo de traducción faltan bloques de texto, como un texto dentro de las etiquetas de traducción de Liquid, del mensaje de correo electrónico actual.                                | Este archivo de traducción no se cargará.                                                                       |
| El archivo de traducción incluye el texto predeterminado que no coincide con los bloques de texto del mensaje de correo electrónico actual.                                          | Este archivo de traducción no se cargará. Corrige esto en tu CSV antes de intentar subirlo de nuevo.               |
| El archivo de traducción incluye localizaciones que no existen en la configuración **de Soporte multilingüe**.                                                           | Estas localizaciones no se guardarán en Braze.                                                                      |
| El archivo de traducción incluye bloques de texto que no existen en el mensaje actual (como el borrador actual en el momento de cargar las traducciones). | Los bloques de texto que no existan en tu mensaje actual no se guardarán del archivo de traducción a Braze. |
| Eliminar una localización del mensaje después de que esa localización ya se haya cargado en el mensaje como parte del archivo de traducción.                           | Al eliminar la configuración regional, se eliminarán todas las traducciones asociadas a dicha configuración en tu mensaje.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }