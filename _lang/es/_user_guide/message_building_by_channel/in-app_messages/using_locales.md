---
nav_title: Locales en los mensajes
article_title: Locales en los mensajes
page_order: 4
alias: /iam_locales/
description: "Este artículo explica cómo utilizar localizaciones en tus mensajes dentro de la aplicación."
---

# Localizaciones en los mensajes

> Tras añadir localizaciones a tu espacio de trabajo, puedes dirigirte a usuarios en distintos idiomas con un solo mensaje dentro de la aplicación.

{% multi_lang_include locales.md section="Prerequisites" %}

## Usar configuraciones regionales

Para utilizar localizaciones en tus mensajes, compón una campaña de mensajería dentro de la aplicación o Canvas. Selecciona el editor de arrastrar y soltar o el editor tradicional, y luego sigue los pasos según tu editor.

{% tabs %}
{% tab editor tradicional %}

1. Añada etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %}

![Editor tradicional con ID de traducción.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Después de añadir las etiquetas, guarda tu mensaje como borrador.
4\. Selecciona **Gestionar idiomas** y añade tus localizaciones para el mensaje utilizando el desplegable.

![Modalidad "Gestionar idiomas" con una localización seleccionada.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. Después, rellena las traducciones en el archivo CSV.

![Un ejemplo de archivo CSV de traducción.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Seleccione **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

{% endtab %}
{% tab Editor de arrastrar y soltar %}

1. Añada etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir. 
2. Añade una etiqueta ID a cada etiqueta de traducción. Un ejemplo es: {% raw %}`{% translation id_1 %}`{% endraw %} 

![Editor de arrastrar y soltar con dos ID de traducción.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Después de añadir las etiquetas, guarda tu mensaje como borrador y vuelve a abrir el editor.
4\. En el panel **Construir**, selecciona **Multiidioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
5\. Selecciona **Descargar plantilla** para descargar la plantilla de traducción como archivo CSV. 

![Panel "Multi-idioma" con botón para descargar la plantilla.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Rellena las traducciones en el archivo CSV. Si has copiado y pegado las etiquetas de traducción directamente desde el Paso 1, puede que tengas que eliminar `<code>` de la columna **Etiquetas de traducción** del archivo CSV.
7\. Seleccione **Cargar traducciones** para cargar el archivo CSV con las traducciones realizadas.

![Panel "multi-idioma" con botones para descargar la plantilla y subir traducciones.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
