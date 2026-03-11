---
nav_title: Propiedades del contexto y del evento
article_title: Propiedades del contexto y del evento
page_order: 4.2
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las propiedades de contexto y las propiedades del evento, y cuándo utilizar cada una de ellas."
tool: Canvas
---

# Propiedades del contexto y del evento

> Este artículo de referencia cubre información sobre `context` y `event_properties`, incluyendo cuándo utilizar cada propiedad y las diferencias de comportamiento. <br><br> Para obtener información sobre las propiedades de eventos personalizados en general, consulte [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Las propiedades de contexto y las propiedades del evento funcionan de manera diferente dentro de los flujos de trabajo de Canvas. Las propiedades de los eventos o llamadas a la API que desencadenan la entrada de un usuario en un Canvas se conocen como `context`. Las propiedades del evento que se producen cuando un usuario se desplaza dentro de un recorrido de Canvas se conocen como `event_properties`. La diferencia clave es que`context`se centra en algo más que en los eventos, ya que también accede a las propiedades de las cargas útiles de entrada en los lienzos desencadenados por API.

Consulta la siguiente tabla para obtener un resumen de las diferencias entre las propiedades de contexto y las propiedades del evento.

| | Propiedades del contexto | Propiedades del evento |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistencia** | Puede ser referenciado por todos los pasos [de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante la duración de un lienzo creado con Canvas. | \- Solo puede referenciarse una vez. <br> \- No puede ser referenciado por ningún paso de Mensaje posterior. |
| **Comportamiento del Canvas** | Puede hacer referencia a `context` en cualquier paso de un Canvas. Para el comportamiento posterior al lanzamiento, consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Puede hacer referencia a `event_properties` en el primer paso de Mensaje **después de** un paso de [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) en el que la acción realizada es un evento personalizado o un evento de compra. <br> \- No puede estar después de la ruta Todos los demás del paso Vías de acción. <br> \- Puede haber otros componentes que no sean mensajes entre las rutas de acción y los pasos de mensaje. Si uno de estos componentes que no son Mensajes es un paso de Ruta de Acción, el usuario puede ir a través de la ruta Todos los demás de esa ruta de acción. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Ten en cuenta que Canvas Context no es compatible con el editor Canvas original, por lo que esta sección está disponible como referencia cuando se utilizan las propiedades de entrada y las propiedades del evento de Canvas para el flujo de trabajo anterior de Canvas.

**Propiedades de entrada del Canvas:**
- Debes tener activadas las propiedades de entrada persistente. 
- Solo se puede hacer referencia`canvas_entry_properties`  en el primer paso completo de un Canvas. El Canvas debe estar basado en acciones o activado por la API.

**Propiedades de entrada:**
- Puede hacer referencia`event_properties`  en cualquier paso completo que utilice la entrega basada en acciones en un Canvas.
- No se puede utilizar en pasos completos programados que no sean el primer paso completo de un Canvas basado en acciones. Sin embargo, si un usuario está utilizando un [componente Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), el comportamiento sigue las reglas actuales del flujo de trabajo de Canvas para `event_properties`.

**Propiedades del evento:**
- No puedes utilizar`event_properties`  en el paso Mensaje inicial. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.

{% enddetails %}

### Lo que hay que saber

- El contexto solo está disponible como referencia en Liquid. Para filtrar las propiedades dentro del lienzo, utilice [la segmentación de propiedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para los canales de mensajes dentro de la aplicación, puedes hacer referencia a`context`  y`event_properties`  en un Canvas.`event_properties`Se puede acceder a  cuando se incluye en el primer paso en Canvas, ya que se basa en un activador.
- No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, puedes utilizar`context`  o añadir un paso de rutas de acción con el evento correspondiente **antes** del paso de mensaje que incluye `event_properties`.
- Cuando un paso de Ruta de acción contiene un activador "Envió de un mensaje SMS entrante" o "Envió de un mensaje WhatsApp entrante", los pasos posteriores de Canvas pueden incluir una propiedad SMS o WhatsApp Liquid. Esto refleja cómo funcionan las propiedades del evento en Canvases. De este modo, puede aprovechar sus mensajes para guardar y consultar datos de origen sobre perfiles de usuario y mensajería conversacional.

{% alert note %}
La elegibilidad de la audiencia se evalúa una vez al entrar en Canvas. Si un usuario se fusiona durante la entrada, el usuario identificado continúa a través del Canvas y no se vuelve a evaluar según los criterios de segmentación del Canvas.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Marcas de tiempo para los desencadenantes

Si utilizas marcas de tiempo con un [tipo de fecha y hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de eventos que desencadenan lienzos basados en acciones, a los que se hace referencia mediante [el contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), las marcas de tiempo se normalizan a UTC.

Dado este comportamiento, Braze recomienda encarecidamente utilizar un filtro de zona horaria Liquid como el del siguiente ejemplo para garantizar que tus mensajes se envíen con tu [zona horaria preferida]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### Excepciones

- Las marcas de tiempo no se normalizan a UTC en el primer paso de Canvas si ese paso es un paso de mensaje.
- Las marcas de tiempo no se normalizan a UTC en ningún paso de mensaje que utilice el canal de mensajes dentro de la aplicación, independientemente de su orden en Canvas.

## Casos de uso

![Un paso de ruta de acción seguido de un paso de retraso y un paso de mensaje para los usuarios que han añadido un artículo a su lista de deseos, y una ruta para todos los demás.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para comprender mejor las diferencias entre`context`  y `event_properties`, consideremos este escenario en el que los usuarios entran en un Canvas basado en acciones si realizan el evento personalizado «añadir artículo a la lista de deseos». 

El contexto se configura en el paso [Programación de entradas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de la creación de un Canvas y se corresponde con el momento en que un usuario entra en un Canvas. También se puede hacer referencia al contexto en cualquier paso de mensaje.

En este Canvas, tenemos un recorrido de usuario que comienza con un paso de Action Paths para determinar si un usuario ha añadido un artículo a su wishlist. A partir de aquí, si el usuario ha añadido un artículo, experimentará un retraso antes de recibir el mensaje «¡Nuevo artículo en tu lista de deseos!» del paso Mensaje. 

El primer paso Mensaje del recorrido del usuario tiene acceso a la personalización`event_properties`  desde tu paso Rutas de acción. En este caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` en este paso de Mensaje como parte del contenido de nuestro mensaje. Si un usuario no añade un artículo a tu lista de deseos, sigue la ruta «Todos los demás», lo que significa que`event_properties`no se puede hacer referencia a él y se muestra un error de configuración no válida.

Tenga en cuenta que sólo tendrá acceso a `event_properties` si su paso Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso Rutas de acción. Si el paso Mensaje está conectado a una ruta Todos los demás, pero se puede rastrear hasta un paso Rutas de acción en el recorrido del usuario, entonces también seguirás teniendo acceso a `event_properties`. Para obtener más información sobre estos comportamientos, consulta [Paso de mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

