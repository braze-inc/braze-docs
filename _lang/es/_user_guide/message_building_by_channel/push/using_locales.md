---
nav_title: Locales en los mensajes
article_title: Locales en los mensajes
page_order: 9
description: "Este artículo explica cómo utilizar la localización en tus notificaciones push."
---

# Localizaciones en los mensajes

> Tras añadir localizaciones a tu espacio de trabajo, puedes dirigirte a usuarios en distintos idiomas con una sola notificación push.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
El soporte multilingüe y las localizaciones en los mensajes están actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Usar configuraciones regionales

Para utilizar localizaciones en tu mensajería, compón una campaña push o Canvas, y luego completa lo siguiente:

1. Añada etiquetas de traducción {% raw %}`{% translation %}` y `{% endtranslation %}`{% endraw %} para envolver todo el texto y las URL de imágenes o enlaces que se vayan a traducir.

![Creador de notificaciones push con etiquetas de traducción añadidas a los campos de título y mensaje.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Guarda tu mensaje como borrador.
3\. Selecciona **Gestionar idioma** y añade tus localizaciones para el mensaje utilizando el desplegable.
4\. Selecciona **Descargar plantilla** y, a continuación, rellena las traducciones dentro de la plantilla CSV.

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Para cargar la plantilla CSV completada, selecciona **Cargar traducciones**. 

![La ventana "Mensajes multilingües" con dos localizaciones seleccionadas y botones para descargar una plantilla o subir traducciones.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
