---
nav_title: Creación de tarjetas
article_title: Creación de tarjetas
alias: /card_creation/
description: "Este artículo describe las diferencias entre la creación de una tarjeta de contenido en el lanzamiento de una campaña o en la entrada al paso en Canvas frente a la primera impresión."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Creación de tarjetas

> Puedes elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para nuevas campañas de tarjeta de contenido y pasos en Canvas especificando cuándo se crea la tarjeta.

## Requisitos previos

Para aprovechar esta característica, debes actualizarte a las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Tras actualizar el SDK, tus usuarios móviles deben actualizar su aplicación. Puedes filtrar la audiencia de tu campaña o Canvas para [dirigirte]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) sólo [a los usuarios de estas versiones mínimas de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Resumen

{% tabs %}
{% tab Campaign %}

Puedes elegir cuándo Braze crea una tarjeta en el paso **Entrega** al crear una nueva [campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) con entrega programada.

\![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido programada.]({% image_buster /assets/img_archive/card_creation.png %})

Están disponibles las siguientes opciones:

- **En el lanzamiento de la campaña:** El comportamiento predeterminado anterior para las tarjetas de contenido. Braze calcula la audiencia elegible y la personalización cuando se lanza la campaña, luego crea la tarjeta y la almacena hasta que el usuario abre tu aplicación. 
- **En la primera impresión (recomendado):** La próxima vez que el usuario abra tu aplicación (es decir, cuando inicie una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze determinará para qué tarjetas de contenido es elegible el usuario, plantillas de personalización como Liquid o Contenido conectado y, a continuación, creará la tarjeta. Esta opción suele ofrecer un mejor rendimiento en las entregas de tarjetas.

Independientemente de la opción que elijas, la cuenta atrás de la fecha de caducidad de la tarjeta de contenido comenzará cuando se lance la campaña.

{% endtab %}
{% tab Canvas %}

Puedes elegir cuándo crea Braze una tarjeta en la pestaña **Canales de mensajería** del [paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) de una tarjeta de contenido.

\![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido programada.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Están disponibles las siguientes opciones:

- **A la entrada del escalón:** El comportamiento predeterminado anterior para las tarjetas de contenido. Braze calcula la audiencia elegible cuando el usuario entra en el paso en Canvas, luego crea la tarjeta y la almacena hasta que el usuario abre tu aplicación.
- **En la primera impresión (recomendado):** Braze calcula la audiencia elegible cuando el usuario entra en el paso en Canvas. La próxima vez que el usuario abra tu aplicación (es decir, cuando inicie una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze plantilla cualquier personalización como Liquid o Contenido conectado y, a continuación, crea la tarjeta. Con esta opción obtendrás un mejor rendimiento en la entrega de tarjetas y una personalización más actualizada.

Independientemente de la opción seleccionada, la cuenta atrás de la fecha de caducidad de la tarjeta de contenido comenzará cuando el usuario entre en el paso en Canvas.

{% alert tip %}
Si quieres que los usuarios anónimos vean una tarjeta de contenido en su primera sesión, utiliza una campaña en lugar de un Canvas. Esto se debe a que cuando un usuario anónimo entra en un Canvas, su sesión ya ha comenzado, por lo que no obtendrá la tarjeta de contenido hasta que inicie una nueva sesión.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Para ambas opciones, una vez creada la tarjeta, Braze no recalcula la audiencia elegible ni la personalización.
{% endalert %}

### Diferencias entre crear tarjetas en el lanzamiento o entrada frente a en la primera impresión

Esta sección describe las principales diferencias entre la creación de tarjetas en el lanzamiento de una campaña o en la entrada en una etapa, y en la primera impresión.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Cuando se lanza la campaña / En la entrada del paso en Canvas</th>
    <th class="tg-0pky">En la primera impresión</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Cuándo utilizarlo</td>
    <td class="tg-0pky">Si necesitas que el contenido sea instantáneo a una hora determinada (la hora de lanzamiento).</td>
    <td class="tg-0pky"><ul><li>Si necesitas mostrar tarjetas a usuarios nuevos o anónimos que puedan entrar en el segmento después del lanzamiento<a href="#campaign_note">(sólo campañas*</a>).</li><li>Si utilizas la personalización y quieres que el contenido más reciente esté disponible en la tarjeta.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audiencia</td>
    <td class="tg-0pky">Braze evalúa los miembros de la audiencia cuando se envía la campaña.<br><br>No se evaluará la elegibilidad de los usuarios nuevos o anónimos que intenten ver la tarjeta después del envío de la campaña. Para las campañas recurrentes, será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa la afiliación cuando el usuario vuelve a abrir tu aplicación (inicia una sesión, <a href="#campaign_note">sólo campañas*</a>).<br><br> Esta configuración tendrá un mayor alcance de audiencia porque siempre se evaluará la elegibilidad de cualquier usuario nuevo o anónimo cuando intente ver la tarjeta. <br><br>Además, el límite de tasa (limitar el número de personas que recibirán la tarjeta) no es aplicable cuando se establece en la primera impresión.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalización</td>
    <td class="tg-0pky">Braze evalúa Liquid, el contenido conectado y los bloques de contenido en el momento en que se lanza la campaña o cuando un usuario entra en el paso en Canvas. Para las campañas recurrentes, será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa el Líquido, el Contenido conectado y los Bloques de contenido en el momento de la primera impresión o después del siguiente intervalo de repetición.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análisis</td>
    <td class="tg-0pky"><em>Mensajes Enviados</em> se refiere al número de tarjetas creadas y disponibles para ser vistas. Esto no cuenta si los usuarios vieron la tarjeta.</td>
    <td class="tg-0pky"><em>Los mensajes enviados</em> se refieren al número de tarjetas enviadas a un usuario tras el inicio de una sesión. En Canvas, a los usuarios que entran en el paso sin iniciar una sesión no se les envía una tarjeta, por lo que esta métrica puede no coincidir con el número de usuarios que entran en un paso.<br><br>Aunque tus usuarios alcanzables e impresiones no cambiarán, puedes esperar ver una disminución en el volumen de envíos<em>(Mensajes enviados</em>) cuando se crea una tarjeta en la primera impresión, en comparación con si la misma tarjeta se creara en el lanzamiento de la campaña o en la entrada del paso en Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tiempo de procesamiento</td>
    <td class="tg-0pky">Se crean tarjetas para cada usuario elegible del segmento en el momento del lanzamiento. Para audiencias grandes, recomendamos seleccionar <b>A primera impresión</b>, ya que las tarjetas estarán disponibles más rápidamente tras el lanzamiento.</td>
    <td class="tg-0pky">Las tarjetas se crean la primera vez que un usuario intenta ver la tarjeta, por lo que puede tardar 1-2 segundos en mostrarse en la primera impresión.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Este escenario sólo se aplica a las campañas, ya que la audiencia de Canvas se evalúa a la entrada en Canvas, no a nivel de paso.</sup></p>

## Consideraciones

### Cambiar la creación de tarjetas tras el lanzamiento

Braze recomienda no cambiar cómo se crean las tarjetas tras el lanzamiento de una campaña. Debido a las diferencias en cómo se calculan los Mensajes Enviados entre los dos tipos de creación de tarjetas, cambiar cómo se crean las tarjetas una vez lanzada la campaña puede afectar a la precisión de tu volumen de envíos.

### Tiempo potencial de procesamiento

Recomendamos que las campañas con grandes audiencias seleccionen la opción de crear tarjetas en la primera impresión, ya que las tarjetas estarán disponibles mucho más rápidamente tras el lanzamiento de la campaña. Las campañas que se desencadenan al inicio de la sesión también pueden considerar la posibilidad de pasar a crear la tarjeta en la primera impresión (disponible mediante entrega programada) para obtener mejoras en el rendimiento.

Cuando las tarjetas se crean en la primera impresión, pueden tardar 1-2 segundos en procesarse. La duración de este tiempo de procesamiento depende de varios factores, como el tamaño de la tarjeta y la complejidad de las opciones de plantilla del mensaje. Por ejemplo, el tiempo de procesamiento de las tarjetas que utilizan Contenido conectado será al menos tan largo como el tiempo de respuesta del Contenido conectado.

### Versiones anteriores del SDK

Si la aplicación de un usuario está ejecutando una versión anterior del SDK, seguirá recibiendo tarjetas de contenido enviadas con una creación de tarjeta especificada. Sin embargo, las tarjetas tardarán más en aparecer para estos usuarios, y puede que no aparezcan hasta la próxima sincronización de Tarjetas de contenido.

