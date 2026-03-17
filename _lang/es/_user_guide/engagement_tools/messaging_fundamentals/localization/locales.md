---
nav_title: Locales en los mensajes
article_title: Localización de configuraciones regionales
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artículo proporciona los pasos para utilizar las configuraciones regionales en tus mensajes."
---

# Localización de configuraciones regionales

> Después de añadir configuraciones regionales a tu espacio de trabajo, puedes dirigirte a usuarios en diferentes idiomas con un solo push, correo electrónico, banner, mensaje dentro de la aplicación o bloque de contenido.

{% multi_lang_include locales.md section="Prerequisites" %}

## Usar configuraciones regionales

### Paso 1: Configura las configuraciones regionales en tu espacio de trabajo. {#workspace-setup}

Antes de poder utilizar las etiquetas de configuración regional y traducción, debes [añadir configuraciones regionales a tu espacio de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Paso 2: Añade etiquetas de Liquid a tu mensaje. {#add-translation-tags}

Añade las etiquetas de traducción{% raw %}`{% translation your_id_here %}`  y`{% endtranslation %}`{% endraw %}  para envolver todo el texto, las imágenes o las URL de los enlaces que vas a traducir.

Cada traducción debe tener un . único`id`. Por ejemplo, al traducir un saludo sencillo, puedes nombrar el ID «saludo»:

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localización de bloques HTML

Un párrafo más complicado puede tener varias etiquetas de traducción("offer_text"  y "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Envolver bloques HTML grandes en etiquetas de traducción puede causar problemas con las hojas de estilo o el diseño. Envuelve las secciones de texto más pequeñas que sea posible.
{% endalert %}

#### Localización de enlaces

Para la localización de los enlaces de etiquetas de anclaje, asegúrate de envolver **solo las partes específicas del idioma** y no todo el `href`atributo URL. Si envuelves toda la URL, es posible que las plantillas de enlaces no funcionen correctamente.

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

### Paso 3: Selecciona las configuraciones regionales de los mensajes {#choose-locales}

Una vez que las etiquetas de traducción estén en el mensaje, ve a la configuración multilingüe del mensaje y selecciona una o varias configuraciones regionales para traducir este mensaje.

![Configuración multilingüe con un campo desplegable para seleccionar las configuraciones regionales.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Selecciona **Multilingüe** en el menú Contenido cuando edites tu mensaje.

![Configuración multilingüe para el correo electrónico.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Selecciona **Administrar idiomas** al editar tu mensaje.

![Configuración multilingüe para push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Selecciona **Administrar idiomas** en la parte inferior de la sección **Compilar**.

![Configuración multilingüe para mensajes de arrastrar y soltar dentro de la aplicación.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Selecciona **Administrar idiomas** al editar tu mensaje.

![Configuración multilingüe para mensajes HTML dentro de la aplicación.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Selecciona **Administrar idiomas** al editar tu mensaje.

![Configuración multilingüe para banners.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
Selecciona **Administrar idiomas** al editar tu bloque de contenido.

{% alert important %}
Los bloques de contenido que tienen traducciones asociadas cargadas no pueden ser sobrescritos por una campaña individual o un mensaje de Canvas.
{% endalert %}

![Configuración multilingüe para bloques de contenido.]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Descargar plantilla CSV {#download-csv}

Después de seleccionar las configuraciones regionales, selecciona **Descargar plantilla** para descargar una plantilla CSV que contiene una matriz con los ID de traducción y las configuraciones regionales seleccionadas.

![Ejemplo de CSV para la localización regional en, fr y es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Paso 5: Sube un archivo CSV completado. {#upload-csv}

{% alert important %}
Cualquier cambio en las ID o localizaciones del archivo CSV no se actualizará automáticamente en tu mensaje. Para actualizar las traducciones, actualiza el archivo CSV y vuelve a subir el archivo.
{% endalert %}

A continuación se muestra el formato de un CSV completado a modo de ejemplo:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Paso 6: Vista previa de las configuraciones de localización {#preview-locales}

Al realizar la vista previa de tu mensaje, selecciona la opción **Usuario multilingüe** en el menú desplegable **Vista previa como usuario**. Esto te permite cambiar entre diferentes definiciones de configuración regional para obtener una vista previa de todas las traducciones de tu mensaje.

![Vistas previas locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Echa un vistazo a nuestra [API de traducción]({{site.baseurl}}/api/endpoints/translations) para gestionar y actualizar las traducciones en tus campañas y Canvases.
{% endalert %}

## Mensajes de derecha a izquierda

Al rellenar el archivo de traducción para idiomas que se escriben de derecha a izquierda (como el árabe), envuelve la traducción con`span`  para que se formatee correctamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Administración de traducciones

### Edición de traducciones para campañas lanzadas y lienzos.

Una vez lanzada una campaña o Canvas, puedes seguir modificando las traducciones mientras estés en modo borrador. Esto se aplica tanto si editas las traducciones directamente en el compositor, mediante la carga de CSV o a través de la API. 

Para obtener más información sobre cómo administrar campañas y Canvas después del lanzamiento, consulta [Edición]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) de [campañas lanzadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) y [borradores de Canvas y edición posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicar pasos o campañas en Canvas, y traducciones

Las traducciones se copian junto con un paso en Canvas, una campaña o una variación de campaña. Esto también es válido cuando se copian entre espacios de trabajo, siempre y cuando las configuraciones de localización estén definidas en el espacio de trabajo de destino. Asegúrate de revisar y actualizar las traducciones según corresponda cuando realices modificaciones en tu Canvas o campaña.

### Uso de la API multilingüe con lienzos

Para utilizar la [API multilingüe con lienzos]({{site.baseurl}}/api/endpoints/translations/), debes incluir `workflow_id`,`step_id`  y`message_variation_id`  en la lista de parámetros.

#### Se han añadido pasos en Canvas a los borradores posteriores al lanzamiento.

Cuando utilices la API multilingüe con pasos en Canvas creados después del lanzamiento de Canvas, el`message_variation_id`  que pases a la API estará vacío o en blanco.

## Preguntas más frecuentes

#### ¿Puedes realizar cambios en la copia traducida de una de tus configuraciones de localización?
Sí. Primero, realiza la edición en el archivo CSV y, a continuación, vuelve a cargar el archivo para aplicar los cambios a la copia traducida.

#### ¿Puedo anidar etiquetas de traducción?
No.

#### ¿Las traducciones admiten HTML para el estilo?
Sí, pero asegúrate de que el estilo HTML no se traduce junto con el contenido.

#### ¿Puedes envolver mensajes HTML completos en una etiqueta de traducción?
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
