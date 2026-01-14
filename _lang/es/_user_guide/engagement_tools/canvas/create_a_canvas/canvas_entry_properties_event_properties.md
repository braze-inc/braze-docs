---
nav_title: Propiedades de la entrada en Canvas y propiedades del evento
article_title: Propiedades de entrada y propiedades del evento en Canvas
page_order: 4.2
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las propiedades de entrada del Canvas y las propiedades del evento, y cuándo utilizar cada propiedad."
tool: Canvas
---

# Propiedades de la entrada en Canvas y propiedades del evento

> Este artículo de referencia cubre información sobre `canvas_entry_properties` y `event_properties`, incluyendo cuándo utilizar cada propiedad y las diferencias de comportamiento. <br><br> Para obtener información sobre las propiedades del evento personalizado en general, consulta [Propiedades del evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Las propiedades de entrada al Canvas y las propiedades del evento funcionan de forma diferente dentro de tus flujos de trabajo en el Canvas. Las propiedades de los eventos o de las llamadas a la API que desencadenan la entrada de un usuario en un Canvas se conocen como `canvas_entry_properties`. Las propiedades de los eventos que se producen cuando un usuario se desplaza por un recorrido de Canvas se conocen como `event_properties`. La diferencia clave es que `canvas_entry_properties` no sólo se centra en los eventos, sino que también accede a las propiedades de las cargas útiles de entrada en los Lienzos desencadenados por la API.

Consulta la tabla siguiente para ver un resumen de las diferencias entre las propiedades de entrada del Canvas y las propiedades del evento.

| | Propiedades de entrada en Canvas | Propiedades del evento
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistencia** | Puede ser referenciado por todos los pasos de [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante la duración de un Canvas construido utilizando Canvas. | \- Sólo se puede consultar una vez. <br> \- No puede ser referenciado por ningún paso posterior de Mensaje. |
| **Comportamiento en Canvas** | Puedes hacer referencia a `canvas_entry_properties` en cualquier paso de un Canvas. Para el comportamiento posterior [al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties), consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Puede hacer referencia a `event_properties` en el primer paso de Mensaje **tras** un paso de [Ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) en el que la acción realizada sea un evento personalizado o un evento de compra. <br> \- No puede estar después de la ruta Todos los demás del paso Rutas de acción. <br> \- Puede tener otros componentes que no sean de Mensaje entre las rutas de acción y los pasos de Mensaje. Si uno de estos componentes que no son mensajes es un paso de Ruta de acción, el usuario puede pasar por la ruta de acción Todos los demás de esa ruta. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Este artículo está disponible como referencia cuando utilices las propiedades de entrada y las propiedades del evento de Canvas para el flujo de trabajo anterior de Canvas.

**Propiedades de entrada al Canvas:**
- Debe tener activadas las propiedades de entrada persistente. 
- Sólo puede hacer referencia a `canvas_entry_properties` en el primer paso completo de un Canvas. El Canvas debe estar basado en acciones o desencadenado por la API.

**Propiedades de entrada:**
- Puede hacer referencia a `event_properties` en cualquier paso completo que utilice la entrega basada en acciones en un Canvas.
- No puede utilizarse en pasos completos programados que no sean el primer paso completo de un Canvas basado en acciones. Sin embargo, si un usuario está utilizando un [componente Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), el comportamiento sigue las reglas actuales del flujo de trabajo Canvas para `event_properties`.

**Propiedades del evento:**
- No se puede utilizar `event_properties` en el paso Mensaje principal. En su lugar, debes utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.

{% enddetails %}

### Lo que debes saber

- Las propiedades de entrada del Canvas sólo están disponibles como referencia en Liquid. Para filtrar por las propiedades dentro del Canvas, utiliza en su lugar [la segmentación de propiedades del evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para los canales de mensajería dentro de la aplicación, sólo se puede hacer referencia a `canvas_entry_properties` en un Canvas. `event_properties` no puede utilizarse para canales de mensajería dentro de la aplicación.
- No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debes utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`. 
- Cuando un paso en Ruta de acción contiene un desencadenante "Enviado un mensaje entrante SMS" o "Enviado un mensaje entrante WhatsApp", los pasos en Canvas posteriores pueden incluir una propiedad SMS o WhatsApp Liquid. Esto refleja cómo funcionan las propiedades del evento en los Lienzos. De este modo, puedes aprovechar tus mensajes para guardar y consultar datos propios sobre perfiles de usuario y mensajería conversacional.

### Marcas de tiempo para propiedades del evento

Si utilizas marcas de tiempo con un [tipo de fecha/hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de las [propiedades del evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) en los Lienzos basados en acciones, las marcas de tiempo se normalizan a UTC. A continuación se detallan algunas excepciones.

Dado este comportamiento, Braze te recomienda encarecidamente que utilices un filtro de zona horaria Liquid como el del ejemplo siguiente para garantizar que tus mensajes se envían con tu [zona horaria preferida]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Excepciones

- Las marcas de tiempo no se normalizan a UTC en el primer paso de un Canvas si ese paso es un paso de Mensaje.
- Las marcas de tiempo no se normalizan a UTC en ningún paso de Mensaje que utilice el canal de mensajería dentro de la aplicación, independientemente de su orden en el Canvas.

## Casos de uso

Un paso de Ruta de acción seguido de un paso de Retraso y un paso de Mensaje para los usuarios que han añadido un artículo a su lista de deseos, y una ruta para todos los demás.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para comprender mejor las diferencias de `canvas_entry_properties` y `event_properties`, consideremos este escenario en el que los usuarios entrarán en un Canvas basado en acciones si realizan el evento personalizado "añadir artículo a la lista de deseos". 

Los `canvas_entry_properties` se configuran en el paso [Horario de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de la creación de un Canvas y corresponderán a cuando un usuario entre en un Canvas. También se puede hacer referencia a estos `canvas_entry_properties` en cualquier paso de Mensajes.

En este Canvas, tenemos un recorrido del usuario que comienza con un paso en Rutas de acción para determinar si un usuario ha añadido un artículo a su lista de deseos. A partir de aquí, si el usuario ha añadido un artículo, experimentará un retraso antes de recibir el mensaje "¡Nuevo artículo en tu lista de deseos!" del paso Mensaje. 

El primer paso de Mensaje en un recorrido del usuario tendrá acceso al `event_properties` personalizado de tu paso Rutas de acción. En este caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` en este paso Mensaje como parte del contenido de nuestro mensaje. Si un usuario no añade un artículo a su lista de deseos, pasa por la ruta Todos los demás, lo que significa que no se puede hacer referencia a `event_properties` y reflejará un error de configuración no válida.

Ten en cuenta que sólo tendrás acceso a `event_properties` si tu paso Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso Rutas de acción. Si el paso Mensaje está conectado a una ruta Todos los demás, pero puede remontarse a un paso Rutas de acción en el recorrido del usuario, entonces también seguirás teniendo acceso a `event_properties`. Para más información sobre estos comportamientos, consulta el [paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

