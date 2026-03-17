{% if include.section == "Prerequisites" %}
## Requisitos previos

Para editar y administrar [la compatibilidad con varios idiomas]({{site.baseurl}}/multi_language_support/), necesitas los siguientes [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) para tu espacio de trabajo:

- Ver configuración multilingüe
- Crear configuración regional multilingüe de localización
- Eliminar configuración regional multilingüe

Para añadir la configuración regional a un mensaje, necesitas el permiso «Editar campañas».

{% alert important %}
La compatibilidad con varios idiomas se encuentra actualmente en fase de acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Vista previa de tus configuraciones regionales

En el menú desplegable **Mensaje de vista previa como usuario** de la pestaña **Prueba**, selecciona **Usuario personalizado** e introduce diferentes idiomas para obtener una vista previa del mensaje y comprobar si se traduce según lo esperado.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Preguntas más frecuentes

#### ¿Puedes realizar cambios en la copia traducida de una de tus configuraciones de localización?
Sí. Primero, realiza la edición en el archivo CSV y, a continuación, vuelve a cargar el archivo para aplicar los cambios a la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Puedo añadir estilos HTML en las etiquetas de traducción?
Sí, pero asegúrate de que el estilo HTML no se traduce junto con el contenido.

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
