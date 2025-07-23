---
nav_title: Locales en los mensajes
article_title: Locales en los mensajes
page_order: 9
description: "Este artículo explica cómo utilizar la localización en tus notificaciones push."
---

# Localizaciones en los mensajes

> Tras añadir localizaciones a tu espacio de trabajo, puedes dirigirte a usuarios en distintos idiomas con una sola notificación push.

## Requisitos previos

Para editar y administrar [el soporte multilingüe]({{site.baseurl}}/multi_language_support/), debes tener el permiso de usuario "Administrar configuración multilingüe". Para añadir la configuración regional a un mensaje, necesitarás permisos para editar campañas.

## Usar configuraciones regionales

Para utilizar localizaciones en tu mensajería, compón una campaña push o Canvas, y luego completa lo siguiente:

1. Añada etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir.<br><br>![Creador de notificaciones push con etiquetas de traducción añadidas a los campos de título y mensaje.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. Guarda tu mensaje como borrador.
3. Selecciona **Gestionar idioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
4. Selecciona **Descargar plantilla** y, a continuación, rellena las traducciones dentro de la plantilla CSV. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. Para cargar la plantilla CSV completada, selecciona **Cargar traducciones**. <br><br>![La ventana "Mensajes multilingües" con dos localizaciones seleccionadas y botones para descargar una plantilla o subir traducciones.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Para actualizar las traducciones, actualiza el CSV y vuelve a subir el archivo. Esto significa que cualquier cambio en los ID o locales del CSV no se actualizará automáticamente en su mensaje.

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

## Vista previa de tus configuraciones regionales

En el desplegable **Vista previa del mensaje como usuario**, dentro de la pestaña **Prueba**, selecciona **Usuario personalizado** e introduce distintos idiomas para previsualizar el mensaje y comprobar si tu mensaje se traduce como esperabas.

{% multi_lang_include locales.md section="Preguntas frecuentes" %}
