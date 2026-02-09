---
nav_title: Localizaciones en los mensajes
article_title: Traducir locales
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artículo te explica cómo utilizar las localizaciones en tus mensajes."
---

# Traducir locales

> Después de añadir localizaciones a tu espacio de trabajo, puedes dirigirte a usuarios en diferentes idiomas con un solo push, correo electrónico, banner o mensaje dentro de la aplicación.

{% multi_lang_include locales.md section="Prerequisites" %}

## Usar configuraciones regionales

### Paso 1: Configura las localizaciones en tu espacio de trabajo {#workspace-setup}

Antes de poder utilizar locales y etiquetas de traducción, debes [añadir locales a tu espacio de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Paso 2: Añadir etiquetas de Liquid de traducción a tu mensaje {#add-translation-tags}

Añade las etiquetas de traducción {% raw %}`{% translation your_id_here %}` y `{% endtranslation %}`{% endraw %} para envolver todas las URL de texto, imágenes o enlaces que vayas a traducir.

Cada traducción debe tener un `id` único. Por ejemplo, al traducir un simple saludo, puedes llamar al ID "saludo":

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localización de bloques HTML

Un párrafo más complicado puede tener varias etiquetas de traducción ("offer_text" y "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Envolver grandes bloques HTML en etiquetas de traducción puede causar problemas de hoja de estilos o de estilización. Envuelve las secciones de texto lo más pequeñas posible.
{% endalert %}

#### Localización de enlaces

Para localizar enlaces de etiquetas de anclaje, asegúrate de envolver **sólo las partes específicas del idioma** y no todo el atributo `href` URL. Si envuelves toda la URL, puede que la plantilla de enlaces no funcione correctamente.

##### Uso correcto

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### Uso incorrecto

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### Paso 3: Elegir la localización de los mensajes {#choose-locales}

Una vez que tus etiquetas de traducción estén en el mensaje, ve a la configuración multilingüe del mensaje y selecciona una o más localizaciones para traducir este mensaje.

![Configuración multilingüe con un campo desplegable para seleccionar las localizaciones.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Selecciona **Multiidioma** en el menú Contenido al editar tu mensaje.

![Configuración multilingüe para el correo electrónico.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Selecciona **Gestionar idiomas** al editar tu mensaje.

![Configuración multilingüe para push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Selecciona **Gestionar idiomas** en la parte inferior de la sección **Construir**.

![Configuración multilingüe para arrastrar y soltar mensajes dentro de la aplicación.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Selecciona **Gestionar idiomas** al editar tu mensaje.

![Configuración multilingüe para mensajes HTML dentro de la aplicación.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Selecciona **Gestionar idiomas** al editar tu mensaje.

![Configuración multilingüe para los banners.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Descargar plantilla CSV {#download-csv}

Tras seleccionar tus localizaciones, selecciona **Descargar plantilla** para descargar una plantilla CSV que contiene una matriz de tus ID de traducción y localizaciones seleccionadas.

![Ejemplo de CSV para las localizaciones en, fr y es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Paso 5: Sube un CSV completo {#upload-csv}

{% alert important %}
Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.
{% endalert %}

Aquí tienes el formato de un CSV completado de ejemplo:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Paso 6: Vista previa locales {#preview-locales}

Cuando previsualices tu mensaje, selecciona la opción **Usuario multilingüe** en el menú desplegable **Vista previa como usuario**. Esto te permite cambiar entre diferentes definiciones de localización para obtener una vista previa de todas las traducciones de tu mensaje.

![Vistas previas de la localización]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

## Mensajes de derecha a izquierda

Cuando rellenes el archivo de traducción para lenguas que se escriben de derecha a izquierda (como el árabe), envuelve la traducción con `span` para que tenga el formato adecuado:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Administrador de traducciones

### Edición de traducciones para campañas lanzadas y Lonas

Después de lanzar una campaña o un Canvas, puedes seguir modificando las traducciones cuando estés en modo borrador. Esto se aplica tanto si estás editando traducciones directamente en el compositor, mediante carga CSV o a través de la API. 

Para más detalles sobre la gestión de campañas y Canvas después del lanzamiento, consulta [Editar campañas lanzadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) y [borradores de Canvas y edición posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicar pasos en Canvas o campañas, y traducciones

Las traducciones se copian junto con un paso en Canvas, campaña o variación de campaña. Lo mismo ocurre al copiar entre espacios de trabajo, siempre que las localizaciones estén definidas en el espacio de trabajo de destino. Asegúrate de revisar y actualizar las traducciones en consecuencia cuando realices modificaciones en tu Canvas o campaña.

### Utilizar la API multilingüe con los lienzos

Para utilizar [la API multilingüe con los lienzos]({{site.baseurl}}/api/endpoints/translations/), debes incluir las direcciones `workflow_id`, `step_id`, y `message_variation_id` en la lista de parámetros.

#### Pasos en Canvas añadidos a los borradores posteriores al lanzamiento

Cuando utilices la API Multilingüe con pasos en Canvas creados después de que se haya lanzado el Canvas, el `message_variation_id` que pases a la API estará vacío o en blanco.

## Preguntas más frecuentes

#### ¿Puedo modificar la copia traducida en una de mis localizaciones?
Sí. Primero, haz la edición en el CSV, y luego vuelve a subir el archivo para hacer un cambio en la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Las traducciones admiten HTML para el estilo?
Sí, pero asegúrate de que el estilo HTML no se traduce con el contenido.

#### ¿Puedo envolver mensajes HTML enteros en una etiqueta de traducción?
No, tus etiquetas de traducción deben ser lo más pequeñas posible para evitar limitaciones de rendimiento o tamaño.

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
