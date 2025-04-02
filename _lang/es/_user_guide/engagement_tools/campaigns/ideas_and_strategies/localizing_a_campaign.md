---
nav_title: Localización
page_order: 3
page_type: reference
description: "El artículo destaca las ventajas de los distintos enfoques de orquestación en las campañas y los Canvases, y enumera las distintas formas en que los usuarios pueden gestionar la personalización de sus mensajes."
tool:
  - Campaigns
  - Canvas

---

# Localización

> Braze recopila automáticamente la información de localización de los dispositivos de los usuarios tras integrar el SDK. La configuración regional contiene el idioma y un identificador de región. Esta información está disponible en la herramienta de segmentación Braze en **País** e **Idioma**.

Visite los siguientes recursos de [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) y [Android/FireOS](http://developer.android.com/reference/java/util/Locale.html) para obtener detalles técnicos sobre cómo se recibe la configuración regional en función de su plataforma.

Para las empresas con clientes en muchos países, gestionar la localización al principio de su recorrido de Braze puede ahorrarles tiempo y recursos. En el siguiente artículo se enumeran las ventajas de los distintos enfoques de orquestación entre campañas y Canvases y también se enumeran las distintas formas en que los usuarios pueden gestionar la personalización en sus mensajes.

- **Opciones de orquestación**
  - [Campaña](#campaign) (una plantilla para todos frente a una plantilla por país)
  - [Canvas](#canvas) (un recorrido para todos frente a un recorrido por país)<br><br>
- **Opciones de personalización**
  - [Entrada manual](#option-1-manual-entry)
  - [Bloques de contenido](#option-2-content-blocks)
  - [Catálogos](#option-3-catalogs)
  - [Socios de localización](#option-4-localization-partners)
  - [Traducciones en una hoja pública de Google](#option-5-translations-in-a-public-google-sheet)
  - [Hoja de cálculo de Google en una API JSON a través de SheetDB](#option-6-google-spreadsheet-into-a-json-api-via-sheetdb)

## Orquestación

### Campaña

{% tabs local %}
{% tab Una plantilla para todos %}

En el enfoque "una plantilla para todos", la localización se aplica a una única plantilla en Braze utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Tras el envío, el panel proporciona análisis agregados de la campaña. El compromiso a nivel de usuario puede medirse utilizando embudos de segmentos personalizados, por ejemplo, combinando los filtros **País** y **Campaña recibida**.

| Ventajas | Consideraciones |
| --- | --- |
| \- Enfoque centralizado<br>\- Reducción del tiempo de creación del correo electrónico, sin necesidad de crear un correo electrónico varias veces | \- Elaboración manual de informes<br>\- El informe de campaña muestra métricas agregadas en lugar de métricas por país<br>\- Necesidad de probar a fondo Liquid para garantizar que se rellena como se espera<br>\- Dependiendo de cómo introduzcas el valor del país o de cuántos condados tengas configurados, podría ser complicado probar cada país<br>\- Es más difícil programar envíos a horas concretas en distintas zonas horarias<br>\- Es más difícil de usar si quieres enviar contenidos separados por país. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Una plantilla por país %}

El enfoque de "una plantilla por país" separa las plantillas en diferentes locales de envío. Tras el envío, el panel de control informa de los análisis de envío en función de cada país por separado, y cualquier evento [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) posterior a nivel de usuario también estará vinculado a una campaña específica.

- Las plantillas se benefician de la implantación de [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) con fines de mantenimiento y seguimiento.
- Las campañas pueden heredar las configuraciones de la misma [plantilla Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) y de [los Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (como las [plantillas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) que contienen Liquid).
- Las campañas y plantillas preexistentes pueden [duplicarse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/) para acelerar la obtención de valor.

| Ventajas | Consideraciones |
| --- | --- |
| \- Escalable a múltiples ubicaciones<br>\- Informes sobre ingresos por país en Braze (por ejemplo, por campaña)<br>\- Flexibilidad si hay contenidos drásticamente diferentes por país | \- Requiere una estructuración estratégica<br>\- Requiere más esfuerzo de construcción (como campañas separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Un recorrido para todos %}

En el enfoque "un recorrido para todos", la localización se gestiona dentro de [Recorridos de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) y Liquid para definir la mensajería para cada usuario. 

Tras el envío de un Canvas, el panel de control proporciona [análisis agregados de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), mientras que la participación a nivel de usuario puede medirse a través de [embudos de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_funnels/) personalizados, como la combinación de filtros de [**País**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) y [**Paso de Canvas recibido**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step).

| Ventajas | Consideraciones |
| --- | --- |
| \- Enfoque centralizado<br>\- Reducción del tiempo de creación del correo electrónico: no es necesario crear un correo electrónico varias veces. | \- Elaboración manual de informes<br>\- El informe Canvas muestra métricas agregadas en lugar de métricas por país<br>\- Necesidad de probar a fondo Liquid para garantizar que se rellena como se espera<br>\- Dependiendo de cómo introduzcas el valor del país o de cuántos condados tengas configurados, podría ser complicado probar cada país<br>\- Es más difícil programar envíos a horas concretas en distintas zonas horarias<br>\- Es más difícil de usar si quieres enviar contenidos separados por país. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Un recorrido por país %}

En el enfoque de "un recorrido por país", el constructor de recorridos de [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) proporciona la flexibilidad de crear recorridos de usuario mediante múltiples [componentes Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). Estos componentes pueden [duplicarse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-canvases) a nivel de componente y de trayecto global.

La localización puede lograrse mediante los siguientes métodos:
- Lienzos separados por país, lo que garantiza que los recorridos complejos de los usuarios se definan en la parte superior del embudo mediante filtros de audiencia.
- Viajes de usuario personalizados por país, la implementación de [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar intuitivamente a los usuarios a gran escala para cada viaje mediante la creación de hilos de mensajes separados para cada país en un único Canvas.

Una vez enviado, el panel proporciona análisis dinámicos por país y dentro de los eventos [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) a nivel de usuario en función de la ubicación actual del cliente.

| Ventajas | Consideraciones |
| --- | --- |
| \- Informes sobre ingresos por país dentro de Braze (como por Canvas, variante o paso)<br>\- Flexibilidad si hay contenidos drásticamente diferentes por país<br>\- Puedes añadir otros canales como parte del recorrido en el futuro | \- Requiere una estructuración estratégica<br>\- Requiere más esfuerzo de construcción (como pasos de mensaje separados para cada país)<br>\- El lienzo puede volverse grande y difícil de leer si tiene recorridos personalizados y complejos para cada país en un solo lienzo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Personalización

### Opción 1: Entrada manual

La entrada manual requiere que pegue manualmente el contenido en el cuerpo del mensaje y utilice [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para mostrar [condicionalmente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) el idioma correcto al destinatario.

{% raw %}
```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This will go to anyone who does not match the other specified languages!
{% endif %}
```
{% endraw %}

Esto puede hacerse utilizando el formato anterior o a través del panel de Braze: 
1. Al redactar su mensaje, seleccione el botón **Idioma** para generar la lógica condicional Líquido para cada idioma que seleccione.
2. Después de insertar el texto de la plantilla en tu mensaje, escribe diferentes variaciones para cada idioma. Para cada campo con plantillas, debe introducir las variaciones después del segmento de plantillas entre corchetes. La variación debe corresponder al código de idioma al que se hace referencia en los corchetes que la preceden.
3. Pruebe su mensaje antes de enviarlo introduciendo el ID o el correo electrónico de un usuario para comprobar cómo le aparecería un mensaje a una persona en función de su idioma. 

{% alert tip %}
Siempre recomendamos incluir una declaración {% raw %}`{% else %}`{% endraw %} en tu mensajería. Mientras que la mayoría de los usuarios verán los mensajes para su idioma específico, el texto será visible para aquellos que:
- No tienes ningún idioma seleccionado
- Tienes un idioma que Braze no admite
- Tener un dispositivo en el que el idioma sea indetectable
{% endalert %}

### Opción 2: Bloques de contenido

Los [bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) Braze son bloques de contenido reutilizables. Cuando se modifica un bloque, cambian todas las referencias a ese bloque. Por ejemplo, las actualizaciones del encabezado o pie de página de un correo electrónico se reflejarán en todos los correos electrónicos o en las traducciones de la casa. Estos bloques también pueden [crearse]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) y [actualizarse]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) mediante la API REST, y los usuarios pueden cargar traducciones mediante programación. 

Al crear una campaña en el panel de control, se puede hacer referencia a los bloques de contenido mediante la etiqueta {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Estos bloques pueden contener todas las traducciones dentro de una lógica condicional para cada idioma, como se muestra en la opción 1, o se puede utilizar un bloque independiente para cada idioma.

Los bloques de contenido también pueden utilizarse como un proceso de gestión de la traducción en el que el contenido que requiere traducción se aloja dentro de un bloque de contenido, se busca, se traduce y luego se actualiza:
1. Crea manualmente un bloque de contenido en el panel con la etiqueta "Necesita traducción".
2. Su servicio realiza una obtención nocturna de todos los bloques de contenido utilizando el [punto final`/content_blocks/list` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Su servicio obtiene detalles sobre cada bloque de contenido a través del [endpoint`/content_blocks/info` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) para ver qué bloques están etiquetados para su traducción.
4. Tu servicio de traducción traduce el cuerpo de todos los bloques de contenido "Necesita traducción".
5. Tu servicio accede al [punto final`/content_block/update` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) para actualizar el contenido traducido y actualizar la etiqueta a "Traducción completa".

### Opción 3: Catálogos

[Los catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) le permiten acceder a datos de objetos JSON importados a través de la API y archivos CSV para enriquecer sus mensajes, de forma similar a los atributos personalizados o propiedades de eventos personalizados a través de Liquid. Por ejemplo:

{% tabs local %}
{% tab API %}

Cree un catálogo mediante la siguiente llamada a la API:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```
Añada elementos mediante la siguiente llamada a la API:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endtab%}
{% tab CSV %}
Cree un CSV con el siguiente formato:

| ID | contexto | language | cuerpo |
| --- | --- | --- |
| 1 | 1 | en | Hola |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hola |
| 5 | 2 | en | Hola |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hola |
| 9 | 3 | en | Hola |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hola |

{% endtab %}
{% endtabs %}

Estos elementos del catálogo pueden ser referenciados utilizando [la personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-catalogs-in-a-message), que se muestra a continuación, o [selecciones]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections) que le permiten crear grupos de datos. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 

//returns “Hey”
```
{% endraw %}

### Opción 4: Añadir una configuración regional

Añada y utilice [configuraciones regionales en sus mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales) para dirigirse a usuarios de distintos idiomas en una misma campaña de correo electrónico o Canvas. 

{% alert important %}
Esta función se encuentra actualmente en acceso anticipado. Póngase en contacto con su gestor de cuenta Braze si está interesado en participar en el acceso anticipado.
{% endalert %}


### Opción 5: Socios de localización

Muchos socios de Braze ofrecen soluciones de localización, como [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) y [Crowdin](https://crowdin.com/). Normalmente, los usuarios utilizan la plataforma junto con un equipo interno y una agencia de traducción. Estas traducciones se cargan allí y se puede acceder a ellas a través de la API REST. Estos servicios también suelen aprovechar [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), lo que permite a los usuarios obtener las traducciones a través de la API.

Por ejemplo, las siguientes llamadas a Connected Content llaman a Transifex y Crowdin para obtener una traducción, aprovechando {% raw %}`{{${language}}}`{% endraw %} para identificar la traducción correcta para un usuario determinado. A continuación, esta traducción se guarda en el bloque JSON "cadenas" y se hace referencia a ella.

{% tabs local %}
{% tab Ejemplo de Transifex %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endtab %}
{% tab Ejemplo de Crowdin %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Opción 6: Traducciones en una hoja pública de Google 

Otra opción de traducción incluye alojar las traducciones en Hojas de Google; a menudo, esto puede gestionarse en colaboración con una agencia de traducción. Las traducciones alojadas aquí pueden consultarse mediante Contenido conectado. La traducción pertinente para un usuario en función de su idioma se incluirá en el cuerpo de la campaña en el momento del envío. 

{% alert note %}
La API de Google Sheets tiene un límite de 500 solicitudes cada 100 segundos por proyecto. Las llamadas a Contenidos Conectados pueden almacenarse en caché, pero esta solución no es escalable para una campaña de alto tráfico.
{% endalert %}

### Opción 7: Hoja de cálculo de Google en una API JSON a través de SheetDB  

Esta opción proporciona un método alternativo para transformar Google Sheets en objetos JSON consultados a través de Connected Content. Al convertir una hoja de cálculo en una API JSON a través de SheetDB, puede elegir entre [varios niveles de suscripción](https://sheetdb.io/pricing) en función de la cadencia de las llamadas a la API.

La estructura de la hoja de cálculo sigue los pasos de la opción 4, pero SheetDB también proporciona [filtros adicionales](https://docs.sheetdb.io/#sheetdb-api) para consultar los objetos.

Algunos usuarios pueden preferir implementar SheetDB con menos dependencias de Liquid y Connected Block implementando el [método de búsqueda](https://docs.sheetdb.io/#get-search-in-document) de SheetDB en las llamadas de solicitud GET para filtrar los objetos JSON basados en la etiqueta {% raw %}`{{${language}}}`{% endraw %} Liquid para devolver automáticamente los resultados de un solo idioma en lugar de construir grandes bloques condicionales.

#### Paso 1: Formatear la hoja de Google

Primero, construye la hoja de Google de modo que los idiomas sean objetos diferentes:

| idioma | título1 | cuerpo1 | título2 | cuerpo2 |
| es | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |

#### Paso 2: Utiliza la etiqueta de idioma Liquid en una llamada de contenido conectado

A continuación, implementa la etiqueta de Liquid {% raw %}`{{${language}}}`{% endraw %} dentro de una llamada a Contenido conectado. Tenga en cuenta que SheetDB generará automáticamente `sheet_id` al crear la hoja de cálculo.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Paso 3: Plantilla de tus mensajes

Por último, utilice Liquid para crear plantillas para sus mensajes:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Consideraciones

- El campo {% raw %}`{{${language}}}`{% endraw %} debe definirse para todos los usuarios; de lo contrario, debe aparecer un bloque condicional Liquid como gestor alternativo para los usuarios sin idioma.
- El modelado de datos dentro de Google Sheets tiene que seguir una vertical diferente basada en el lenguaje en lugar de tener objetos de mensaje.
- SheetDB ofrece una cuenta gratuita limitada y múltiples opciones de pago que deberían considerarse en función de su estrategia de campaña. 
- Las llamadas a Contenidos Conectados pueden almacenarse en caché. Recomendamos medir la cadencia prevista de las llamadas a la API e investigar un enfoque alternativo de llamar al punto final principal de SheetDB en lugar de utilizar el método de búsqueda.