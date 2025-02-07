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

## Preguntas más frecuentes

#### Quiero hacer un cambio en la copia traducida en una de mis configuraciones regionales. ¿Cómo puedo hacerlo?
Realiza la edición en el CSV y, a continuación, vuelve a subir el archivo para realizar un cambio en la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Puedo utilizar localizaciones en mis plantillas de correo electrónico?
No. Las localizaciones sólo se admiten en el editor de correo electrónico para campañas y pasos de mensajería en Canvas.

#### ¿Puedo añadir estilos HTML en las etiquetas de traducción?
Sí. Sin embargo, asegúrate de que el estilo HTML no se traduce con el contenido.

#### ¿Qué validaciones o comprobaciones adicionales hace Braze para las traducciones?

| Escenario                                                                                                                                                 | Validación en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Falta un archivo de traducción de las configuraciones regionales asociadas al mensaje actual.                                                                               | Este archivo de traducción no se cargará.                                                                       |
| A un archivo de traducción le faltan bloques de texto, como un texto dentro de etiquetas de traducción líquida, del mensaje de correo electrónico actual.                                | Este archivo de traducción no se cargará.                                                                       |
| El archivo de traducción incluye el texto predeterminado que no coincide con los bloques de texto del mensaje de correo electrónico actual.                                          | Este archivo de traducción no se cargará. Corrige esto en tu CSV antes de intentar cargarlo de nuevo.               |
| El archivo de traducción incluye locales que no existen en la configuración **de soporte multilingüe**.                                                           | Estas localizaciones no se guardarán en Braze.                                                                      |
| El archivo de traducción incluye bloques de texto que no existen en el mensaje actual (como el borrador actual en el momento de cargar las traducciones). | Los bloques de texto que no existan en el mensaje actual no se guardarán del archivo de traducción a Braze. |
| Eliminar una configuración regional del mensaje después de que esa configuración ya se haya cargado en el mensaje como parte del archivo de traducción.                           | Al eliminar la configuración regional, se eliminarán todas las traducciones asociadas a dicha configuración en tu mensaje.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }