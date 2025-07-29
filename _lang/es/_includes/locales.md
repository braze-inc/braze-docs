{% if include.section == "Prerequisites" %}
## Requisitos previos

Para editar y administrar [el soporte multilingüe]({{site.baseurl}}/multi_language_support/), debes tener el permiso de usuario "Administrar configuración multilingüe". Para añadir la configuración regional a un mensaje, necesitarás permisos para editar campañas.

{% endif %}

{% if include.section == "Preview" %}

## Vista previa de tus configuraciones regionales

En el desplegable **Vista previa del mensaje como usuario**, dentro de la pestaña **Prueba**, selecciona **Usuario personalizado** e introduce distintos idiomas para previsualizar el mensaje y comprobar si tu mensaje se traduce como esperabas.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Preguntas más frecuentes

#### ¿Puedo modificar la copia traducida en una de mis localizaciones?
Sí. Primero, haz la edición en el CSV, y luego vuelve a subir el archivo para hacer un cambio en la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Puedo añadir estilos HTML en las etiquetas de traducción?
Sí, pero asegúrate de que el estilo HTML no se traduce con el contenido.

#### ¿Qué validaciones o comprobaciones adicionales realiza Braze?

| Escenario                                                                                                                                                 | Validación en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Falta un archivo de traducción de las configuraciones regionales asociadas al mensaje actual.                                                                               | Este archivo de traducción no se cargará.                                                                       |
| A un archivo de traducción le faltan bloques de texto, como un texto dentro de etiquetas de traducción líquida, del mensaje de correo electrónico actual.                                | Este archivo de traducción no se cargará.                                                                       |
| El archivo de traducción incluye el texto predeterminado que no coincide con los bloques de texto del mensaje de correo electrónico actual.                                          | Este archivo de traducción no se cargará. Corrige esto en tu CSV antes de intentar cargarlo de nuevo.               |
| El archivo de traducción incluye locales que no existen en la configuración **de soporte multilingüe**.                                                           | Estas localizaciones no se guardarán en Braze.                                                                      |
| El archivo de traducción incluye bloques de texto que no existen en el mensaje actual (como el borrador actual en el momento de cargar las traducciones). | Los bloques de texto que no existan en el mensaje actual no se guardarán del archivo de traducción a Braze. |
| Eliminar una configuración regional del mensaje después de que esa configuración ya se haya cargado en el mensaje como parte del archivo de traducción.                           | Al eliminar la configuración regional, se eliminarán todas las traducciones asociadas a dicha configuración en tu mensaje.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}