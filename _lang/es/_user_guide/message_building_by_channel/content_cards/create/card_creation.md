---
nav_title: Creación de tarjetas
article_title: Creación de tarjetas
alias: /card_creation/
description: "En este artículo se describen las diferencias entre la creación de tarjetas de contenido en el momento del lanzamiento de la campaña o de la entrada en el paso Canvas y en la primera impresión."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Creación de tarjetas

> Puede elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para nuevas campañas de tarjeta de contenido y pasos de Canvas especificando cuándo se crea la tarjeta.

## Requisitos previos

Para aprovechar esta característica, debes actualizarte a las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Tras actualizar el SDK, tus usuarios móviles deben actualizar su aplicación. Puede filtrar su campaña o su público de Canvas para [dirigirse únicamente a los usuarios de estas versiones mínimas de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Resumen

{% tabs %}
{% tab Campaña %}

Puede elegir cuándo Braze crea una tarjeta en el paso **Entrega** al crear una nueva [campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) con entrega programada.

![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido programada.]({% image_buster /assets/img_archive/card_creation.png %})

Existen las siguientes opciones:

- **En el lanzamiento de la campaña:** El comportamiento anterior por defecto para las Tarjetas de Contenido. Braze calcula la elegibilidad de la audiencia y la personalización cuando se lanza la campaña, luego crea la tarjeta y la almacena hasta que el usuario abre su aplicación. 
- **En la primera impresión (recomendado):** La próxima vez que el usuario abra la aplicación (es decir, cuando inicie una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze determinará para qué tarjetas de contenido es elegible, plantillas de personalización como Liquid o Connected Content y, a continuación, creará la tarjeta. Esta opción suele ofrecer un mejor rendimiento en las entregas de tarjetas.

Independientemente de la opción seleccionada, la cuenta atrás de la fecha de caducidad de la tarjeta de contenido comenzará cuando se lance la campaña.

{% endtab %}
{% tab Canvas %}

Puede elegir cuándo Braze crea una tarjeta en la pestaña **Canales de mensajería** de un [paso de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) de tarjeta de contenido.

![Sección Controles de la tarjeta de contenido al editar la entrega de una tarjeta de contenido programada.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Existen las siguientes opciones:

- **En la entrada del paso:** El comportamiento anterior por defecto para las Tarjetas de Contenido. Braze calcula la elegibilidad de la audiencia cuando el usuario entra en el paso Canvas, luego crea la tarjeta y la almacena hasta que el usuario abre su aplicación.
- **En la primera impresión (recomendado):** Braze calcula la audiencia elegible cuando el usuario entra en el paso en Canvas. La próxima vez que el usuario abra la aplicación (es decir, cuando inicie una nueva [sesión](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze aplicará las plantillas de personalización, como Liquid o Connected Content, y creará la tarjeta. Con esta opción obtendrá un mejor rendimiento en la entrega de tarjetas y una personalización más actualizada.

Independientemente de la opción seleccionada, la cuenta atrás de la fecha de caducidad de la tarjeta de contenido comenzará cuando el usuario entre en el paso Lienzo.

{% alert tip %}
Si quieres que los usuarios anónimos vean una tarjeta de contenido en su primera sesión, utiliza una campaña en lugar de un Canvas. Esto se debe a que cuando un usuario anónimo entra en un Canvas, su sesión ya ha comenzado, por lo que no obtendrá la tarjeta de contenido hasta que inicie una nueva sesión.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Para ambas opciones, una vez creada una tarjeta, Braze no recalcula la elegibilidad del público ni la personalización.
{% endalert %}

### Diferencias entre crear tarjetas en el momento del lanzamiento o la entrada y en la primera impresión

En esta sección se describen las principales diferencias entre la creación de tarjetas en el momento del lanzamiento de la campaña o de la entrada en el paso y en la primera impresión.

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
    <th class="tg-0pky">Cuando se lanza la campaña / En la entrada del paso Canvas</th>
    <th class="tg-0pky">En la primera impresión</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Cuándo utilizarlo</td>
    <td class="tg-0pky">Si necesitas que el contenido sea instantáneo a una hora determinada (la hora de lanzamiento).</td>
    <td class="tg-0pky"><ul><li>Si necesita mostrar tarjetas a usuarios nuevos o anónimos que puedan entrar en el segmento después del lanzamiento<a href="#campaign_note">(sólo campañas*</a>).</li><li>Si utilizas la personalización y quieres que el contenido más reciente esté disponible en la tarjeta.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audiencia</td>
    <td class="tg-0pky">Braze evalúa los miembros de la audiencia cuando se envía la campaña.<br><br>No se evaluará la elegibilidad de los usuarios nuevos o anónimos si intentan ver la tarjeta después del envío de la campaña. Para las campañas recurrentes, será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa la afiliación la próxima vez que el usuario abre su aplicación (inicia una sesión, <a href="#campaign_note">sólo campañas*</a>).<br><br> Esta configuración tendrá un alcance de público más amplio porque siempre se evaluará la elegibilidad de cualquier usuario nuevo o anónimo cuando intente ver la tarjeta. <br><br>Además, el límite de velocidad (limitar el número de personas que recibirán la campaña) no es aplicable cuando se establece en la primera impresión (<a href="#campaign_note">solo campañas*</a>).</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalización</td>
    <td class="tg-0pky">Braze evalúa Liquid, el contenido conectado y los bloques de contenido en el momento en que se lanza la campaña o cuando un usuario entra en el paso en Canvas. Para las campañas recurrentes, será en el siguiente intervalo de recurrencia.</td>
    <td class="tg-0pky">Braze evalúa Liquid, Connected Content y Content Blocks en el momento de la primera impresión o tras el siguiente intervalo de recurrencia.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análisis</td>
    <td class="tg-0pky"><em>Mensajes Enviados</em> se refiere al número de tarjetas creadas y disponibles para ser vistas. Esto no cuenta si los usuarios vieron la tarjeta.</td>
    <td class="tg-0pky"><em>Los mensajes enviados</em> se refieren al número de tarjetas enviadas a un usuario tras el inicio de una sesión. En Canvas, a los usuarios que entran en el paso sin iniciar una sesión no se les envía una tarjeta, por lo que esta métrica puede no coincidir con el número de usuarios que entran en un paso.<br><br>Aunque sus usuarios alcanzables e impresiones no cambiarán, puede esperar ver una disminución en el volumen de envíos<em>(Mensajes Enviados</em>) cuando una tarjeta se crea en la primera impresión en comparación con si la misma tarjeta se creara en el lanzamiento de la campaña o en la entrada del paso Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tiempo de procesamiento</td>
    <td class="tg-0pky">En el momento del lanzamiento, se crean tarjetas para todos los usuarios del segmento que cumplen los requisitos. Para grandes audiencias, recomendamos seleccionar <b>A primera impresión</b>, ya que las tarjetas estarán disponibles más rápidamente tras el lanzamiento.</td>
    <td class="tg-0pky">Las tarjetas se crean la primera vez que un usuario intenta verlas, por lo que pueden tardar entre 1 y 2 segundos en mostrarse en la primera impresión.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Este escenario solo se aplica a las campañas, ya que la audiencia de Canvas se evalúa a la entrada de Canvas, no a nivel de paso.</sup></p>

## Consideraciones

### Modificación de la creación de tarjetas tras el lanzamiento

Braze recomienda no cambiar la forma de crear las tarjetas una vez lanzada la campaña. Debido a las diferencias en cómo se calculan los Mensajes Enviados entre los dos tipos de creación de tarjetas, cambiar cómo se crean las tarjetas después de que la campaña se haya lanzado puede afectar a la precisión de su volumen de envíos.

### Tiempo potencial de procesamiento

Recomendamos que las campañas con grandes audiencias seleccionen la opción de crear tarjetas en la primera impresión, ya que las tarjetas estarán disponibles mucho más rápidamente tras el lanzamiento de la campaña. Las campañas que se activan al inicio de la sesión también pueden considerar la posibilidad de pasar a crear la tarjeta en la primera impresión (disponible a través de la entrega programada) para obtener mejoras en el rendimiento.

Cuando las tarjetas se crean en la primera impresión, pueden tardar entre 1 y 2 segundos en procesarse. La duración de este tiempo de procesamiento depende de varios factores, como el tamaño de la tarjeta y la complejidad de las opciones de plantillas de mensajes. Por ejemplo, el tiempo de procesamiento de las tarjetas que utilizan Contenidos Conectados será al menos tan largo como el tiempo de respuesta de Contenidos Conectados.

### Versiones anteriores del SDK

Si la aplicación de un usuario ejecuta una versión anterior del SDK, seguirá recibiendo las tarjetas de contenido enviadas con una creación de tarjeta especificada. Sin embargo, las tarjetas tardarán más en aparecer para estos usuarios, y puede que no aparezcan hasta la próxima sincronización de tarjetas de contenido.

