---
nav_title: Localización
article_title: Localización
page_order: 7
description: "Este artículo de referencia cubre los aspectos básicos de la localización, enumera las ventajas de los distintos enfoques de orquestación entre campañas y Canvases, y enumera las distintas formas en que los usuarios pueden gestionar la personalización en sus mensajes."
tool:
    - Campaigns
    - Canvas
---

# Localización

> Para las empresas con clientes en muchos países, gestionar la localización al principio de su viaje Braze puede ahorrarles tiempo y recursos.

## Cómo funciona

Después de [integrar el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/), la información de localización de los dispositivos de los usuarios se recopila automáticamente. La configuración regional contiene el idioma y un identificador de región. Esta información está disponible en la herramienta de segmentación Braze, en **País** e **Idioma**.

{% alert tip %}
Para más detalles técnicos sobre cómo se recibe la localización, consulta la documentación oficial [de iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) y [Android](http://developer.android.com/reference/java/util/Locale.html).
{% endalert %}

## Gestión de traducciones

Considera los siguientes enfoques para gestionar tus traducciones.

{% tabs local %}
{% tab campaign %}
### Una plantilla para todos

En este enfoque, la localización se aplica a una sola plantilla en Braze utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Tras el envío, el panel proporciona análisis agregados de la campaña. La interacción a nivel de usuario puede medirse utilizando embudos de segmentos personalizados, por ejemplo, combinando los filtros **País** y **Campaña recibida**.

| Ventajas | Consideraciones |
| --- | --- |
| \- Enfoque centralizado<br>\- Reducción del tiempo de creación del correo electrónico, sin necesidad de crear un correo electrónico varias veces. | \- Elaboración manual de informes<br>\- El informe de campaña muestra métricas agregadas en lugar de métricas por país<br>\- Necesidad de probar a fondo Liquid para garantizar que se rellena como se espera<br>\- Dependiendo de cómo introduzcas el valor del país o de cuántos condados tengas configurados, podría ser complicado probar cada país<br>\- Es más difícil programar envíos a horas concretas en distintas zonas horarias<br>\- Es más difícil de usar si quieres enviar contenidos separados por país. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Una plantilla por país 

Este enfoque separa la plantilla en distintas localizaciones de envío. Tras el envío, el panel informa de los análisis de envío basados en cada país por separado, y cualquier evento [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) posterior a nivel de usuario también estará vinculado a una campaña específica.

- Las plantillas se benefician de la implementación de [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) con fines de mantenimiento y seguimiento.
- Las campañas pueden heredar las configuraciones de la misma [plantilla Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) y de [los bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (como [las plantillas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) que contienen Liquid).
- Las campañas y plantillas preexistentes pueden [duplicarse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/) para acelerar la obtención de valor.

| Ventajas | Consideraciones |
| --- | --- |
| \- Escalable a múltiples ubicaciones<br>\- Informes de ingresos por país dentro de Braze (como por campaña)<br>\- Flexibilidad si hay contenidos drásticamente diferentes por país | \- Requiere una estructuración estratégica<br>\- Requiere más esfuerzo de construcción (como campañas separadas para cada país) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### Un viaje para todos

En este enfoque, la localización se gestiona dentro de [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) y Liquid para definir la mensajería para cada usuario. 

Después de enviar un Canvas, el panel proporciona [análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) agregados, mientras que la interacción a nivel de usuario puede medirse mediante [embudos de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) personalizados, como la combinación de [**País**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) y [**Paso en Canvas recibido**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) filtros.

| Ventajas | Consideraciones |
| --- | --- |
| \- Enfoque centralizado<br>\- Reducción del tiempo de creación del correo electrónico: no es necesario crear un correo electrónico varias veces. | \- Elaboración manual de informes<br>\- El informe Canvas muestra métricas agregadas en lugar de métricas por país<br>\- Necesidad de probar a fondo Liquid para garantizar que se rellena como se espera<br>\- Dependiendo de cómo introduzcas el valor del país o de cuántos condados tengas configurados, podría ser complicado probar cada país<br>\- Es más difícil programar envíos a horas concretas en distintas zonas horarias<br>\- Es más difícil de usar si quieres enviar contenidos separados por país. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Un viaje por país

En este enfoque, el constructor de recorridos [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) proporciona la flexibilidad de crear recorridos de usuario a través de múltiples [componentes Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). Estos componentes pueden [duplicarse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating) a nivel de componente y de recorrido global.

La localización se puede conseguir con los siguientes métodos:

- Lienzos separados por país, lo que garantiza que los recorridos complejos de los usuarios se definan en la parte superior del embudo utilizando filtros de audiencia.
- Viajes de usuario a medida por país, la implementación de [rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar intuitivamente a los usuarios a gran escala para cada viaje mediante la creación de hilos de mensajes separados para cada país en un único Canvas.

Una vez enviado, el panel proporciona análisis dinámicos por país y dentro de los eventos [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) a nivel de usuario basados en la ubicación actual del cliente.

| Ventajas | Consideraciones |
| --- | --- |
| \- Informes sobre ingresos por país dentro de Braze (como por Canvas, variante o paso)<br>\- Flexibilidad si hay contenidos drásticamente diferentes por país<br>\- Puedes añadir otros canales como parte del viaje en el futuro | \- Requiere una estructuración estratégica<br>\- Requiere más esfuerzo de construcción (como pasos de mensaje separados para cada país)<br>\- El Canvas puede volverse grande y difícil de leer si tienes recorridos personalizados y complejos para cada país en un único Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Envío de mensajes traducidos

Para enviar mensajes personalizados basados en el idioma o la localización de un usuario, utiliza uno de los siguientes métodos:

{% tabs local %}
{% tab Manually %}
Puedes pegar manualmente tu contenido en el cuerpo del mensaje y utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para mostrar [condicionalmente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) el idioma correcto al destinatario. Para ello:

1. Redacta tu mensaje y, a continuación, selecciona **Idioma** para generar la lógica condicional Liquid para cada uno de los idiomas que hayas seleccionado.
2. Puedes utilizar la siguiente plantilla Liquid para elaborar tu mensaje. Para cada campo con plantilla, debes introducir las variaciones después del segmento de plantilla entre corchetes. La variación debe corresponder al código de lengua al que se hace referencia en los corchetes que la preceden.
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
3. Prueba tu mensaje antes de enviarlo introduciendo la ID o el correo electrónico de un usuario para comprobar cómo le aparecería un mensaje a una persona en función de su idioma. 

{% alert tip %}
Siempre recomendamos incluir una declaración {% raw %}`{% else %}`{% endraw %} en tu mensajería. Aunque la mayoría de los usuarios verán la mensajería para su idioma específico, el texto será visible para aquellos que:
- No tienes ninguna lengua seleccionada
- Tienes un idioma que Braze no admite
- Tener un dispositivo en el que la lengua sea indetectable
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
[Los bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) Braze son bloques de contenido reutilizables. Cuando se modifica un bloque, cambian todas las referencias a ese bloque. Por ejemplo, las actualizaciones de un encabezado o pie de página de correo electrónico se reflejarán en todos los correos electrónicos o en las traducciones de la casa. Estos bloques también pueden [crearse]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) y [actualizarse]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) mediante la API REST, y los usuarios pueden cargar traducciones mediante programación. 

Al crear una campaña en el panel, se puede hacer referencia a los bloques de contenido mediante la etiqueta {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Estos bloques podrían contener todas las traducciones alojadas dentro de una lógica condicional para cada lengua, como se muestra en la opción 1, o se puede utilizar un bloque independiente para cada lengua.

Los bloques de contenido también pueden utilizarse como un proceso de gestión de la traducción en el que el contenido que requiere traducción se aloja en un bloque de contenido, se obtiene, se traduce y luego se actualiza:
1. Crea manualmente un bloque de contenido en el panel con la etiqueta "Necesita traducción".
2. Tu servicio realiza una obtención nocturna de todos los bloques de contenido utilizando el [punto final`/content_blocks/list` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Tu servicio obtiene detalles sobre cada bloque de contenido a través del [punto final`/content_blocks/info` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) para ver qué bloques están etiquetados para su traducción.
4. Tu servicio de traducción traduce el cuerpo de todos los bloques de contenido "Necesita traducción".
5. Tu servicio accede al [punto final`/content_block/update` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) para actualizar el contenido traducido y actualizar la etiqueta a "Traducción completa".
{% endtab %}

{% tab Catalogs %}
[Los catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) te permiten acceder a datos de objetos JSON importados a través de API y archivos CSV para enriquecer tus mensajes, de forma similar a los atributos personalizados o propiedades del evento personalizadas a través de Liquid. Por ejemplo:

{% subtabs local %}
{% subtab API %}

Crea un catálogo mediante la siguiente llamada a la API:
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

Añade elementos mediante la siguiente llamada a la API:

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
{% endsubtab%}
{% subtab CSV %}
Crea un CSV con el siguiente formato:

| ID | contexto | idioma | cuerpo |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

A estos elementos del catálogo se les puede hacer referencia utilizando la [personalización]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#using-catalogs-in-a-message), que se muestra a continuación, o [las selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) que te permiten crear grupos de datos. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Locale messages %}
Añade y utiliza localizaciones en tu mensaje para dirigirte a usuarios en diferentes idiomas, todo dentro de una misma campaña o Canvas para los canales de correo electrónico o push. Para una guía completa, consulta [Locales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/) [en los]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/) [mensajes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/) o [Locales en los mensajes push]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/).

{% alert important %}
Esta característica está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}
{% endtab %}

{% tab Braze partners %}
Muchos socios de Braze ofrecen soluciones de localización, como [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) y [Crowdin](https://crowdin.com/). Normalmente, los usuarios utilizan la plataforma junto con un equipo interno y una agencia de traducción. Estas traducciones se cargan allí y se puede acceder a ellas a través de la API REST. Estos servicios también suelen aprovechar [el Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), lo que permite a los usuarios obtener las traducciones a través de la API.

Por ejemplo, las siguientes llamadas a Contenido conectado llaman a Transifex y Crowdin para obtener una traducción, aprovechando {% raw %}`{{${language}}}`{% endraw %} para identificar la traducción correcta para un usuario determinado. A continuación, esta traducción se guarda en el bloque JSON "cadenas" y se hace referencia a ella.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
Aloja las traducciones en una hoja de cálculo y, a continuación, utiliza uno de los siguientes métodos para enviar tu mensaje en el idioma correspondiente.

{% subtabs local %}
{% subtab Connected Content %}
Puedes contratar a una agencia de traducción para que almacene las traducciones en una hoja de cálculo de Google y, a continuación, consultar este contenido mediante [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Cuando envíes un mensaje, la traducción correspondiente a cada usuario se incluirá en el cuerpo de tu campaña en función del idioma que haya seleccionado. 

{% alert note %}
La API de Google Sheets tiene un límite de 500 peticiones cada 100 segundos por proyecto. Las llamadas de contenido conectado pueden almacenarse en caché, pero esta solución no es escalable para una campaña de mucho tráfico.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Esta opción proporciona un método alternativo para transformar las Hojas de Google en objetos JSON consultados a través de Contenido conectado. Al convertir una hoja de cálculo en una API JSON mediante SheetDB, puedes elegir entre [varios niveles de suscripción](https://sheetdb.io/pricing) en función de la cadencia de las llamadas a la API.

La estructura de la hoja de cálculo sigue los pasos de la opción 4, pero SheetDB también proporciona [filtros adicionales](https://docs.sheetdb.io/#sheetdb-api) para consultar los objetos.

Algunos usuarios pueden preferir implementar SheetDB con menos dependencias de Liquid y Bloques Conectados implementando el [método de búsqueda](https://docs.sheetdb.io/#get-search-in-document) de SheetDB en llamadas de solicitud GET para filtrar los objetos JSON basándose en la etiqueta de Liquid {% raw %}`{{${language}}}`{% endraw %} para devolver automáticamente los resultados de un solo idioma en lugar de construir grandes bloques condicionales.

#### Paso 1: Formatear la hoja de Google

Primero, construye la hoja de Google de modo que las lenguas sean objetos diferentes:

| idioma | título1 | cuerpo1 | título2 | cuerpo2 |
| es | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### Paso 2: Utiliza la etiqueta de idioma Liquid en una llamada de contenido conectado

A continuación, implementa la etiqueta de Liquid {% raw %}`{{${language}}}`{% endraw %} dentro de una llamada a Contenido conectado. Ten en cuenta que SheetDB generará automáticamente la dirección `sheet_id` al crear la hoja de cálculo.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Paso 3: Plantilla de tus mensajes

Por último, utiliza Liquid para la plantilla de tus mensajes:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Consideraciones

- El campo {% raw %}`{{${language}}}`{% endraw %} debe definirse para todos los usuarios; de lo contrario, debe aparecer un bloque condicional Liquid como controlador alternativo para los usuarios sin idioma.
- El modelado de datos dentro de Google Sheets tiene que seguir una vertical diferente basada en el lenguaje, a diferencia de tener objetos de mensaje.
- SheetDB ofrece una cuenta gratuita limitada y múltiples opciones de pago que deberías considerar en función de tu estrategia de campaña. 
- Las llamadas a Contenido conectado pueden almacenarse en caché. Recomendamos medir la cadencia prevista de las llamadas a la API e investigar un enfoque alternativo de llamar al punto final principal de SheetDB en lugar de utilizar el método de búsqueda.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
