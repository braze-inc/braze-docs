---
nav_title: Propiedades de entrada y propiedades de evento del lienzo
article_title: Propiedades de entrada y propiedades de evento del lienzo
page_order: 4.2
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las propiedades de entrada del lienzo y las propiedades de evento, y cuándo utilizar cada propiedad."
tool: Canvas
---

# Propiedades de entrada en el lienzo y propiedades de eventos

> Este artículo de referencia cubre información sobre `canvas_entry_properties` y `event_properties`, incluyendo cuándo utilizar cada propiedad y las diferencias de comportamiento. <br><br> Para obtener información sobre las propiedades de eventos personalizados en general, consulte [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% alert important %}
Si participas en el [acceso anticipado al componente Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), las propiedades de entrada de Canvas forman parte de las variables de contexto de Canvas. Esto significa que `canvas_entry_properties` se denomina ahora `context`. Cada variable de `context` incluye un nombre, un tipo de datos y un valor que puede incluir Liquid.
{% endalert %}

Las propiedades de entrada del lienzo y las propiedades de evento funcionan de forma diferente en los flujos de trabajo del lienzo. Las propiedades de los eventos o llamadas a la API que desencadenan la entrada de un usuario en un Canvas se conocen como `canvas_entry_properties`. Las propiedades de los eventos que se producen a medida que un usuario se desplaza por un recorrido de Canvas se conocen como `event_properties`. La diferencia clave es que `canvas_entry_properties` no sólo se centra en los eventos, sino que también accede a las propiedades de las cargas útiles de entrada en los Lienzos desencadenados por la API.

Consulta la tabla siguiente para ver un resumen de las diferencias entre las propiedades de entrada del Canvas y las propiedades del evento.

| | Propiedades de entrada de Canvas | Propiedades del evento
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistencia** | Puede ser referenciado por todos los pasos [del Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante la duración de un Canvas construido usando el Flujo del Canvas. | \- Solo puede referenciarse una vez. <br> \- No puede ser referenciado por ningún paso de Mensaje posterior. |
| **Comportamiento en Canvas** | Puede hacer referencia a `canvas_entry_properties` en cualquier paso de un Canvas. Para el comportamiento posterior al lanzamiento, consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Puede hacer referencia a `event_properties` en el primer paso de Mensaje **después de** un paso de [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) en el que la acción realizada es un evento personalizado o un evento de compra. <br> \- No puede estar después de la ruta Todos los demás del paso Vías de acción. <br> \- Puede tener otros componentes que no sean de Mensaje entre las rutas de acción y los pasos de Mensaje. Si uno de estos componentes que no son Mensajes es un paso de Ruta de Acción, el usuario puede ir a través de la ruta Todos los demás de esa ruta de acción. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Detalles del editor Original Canvas %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Este artículo está disponible como referencia cuando utilices las propiedades de entrada y las propiedades del evento de Canvas para el flujo de trabajo anterior de Canvas.

**Propiedades de entrada al Canvas:**
- Debe tener activadas las propiedades de entrada persistente. 
- Sólo puede hacer referencia a `canvas_entry_properties` en el primer paso completo de un Canvas. El Canvas debe estar basado en acciones o activado por la API.

**Propiedades de entrada:**
- Puede hacer referencia a `event_properties` en cualquier paso completo que utilice la entrega basada en acciones en un Canvas.
- No puede utilizarse en pasos completos programados que no sean el primer paso completo de un Canvas basado en acciones. Sin embargo, si un usuario está utilizando un [componente Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), el comportamiento sigue las reglas de Canvas Flow para `event_properties`.

**Propiedades del evento:**
- No se puede utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.

{% enddetails %}

### Lo que hay que saber

- Las propiedades de entrada del Canvas sólo están disponibles como referencia en Liquid. Para filtrar las propiedades dentro del lienzo, utilice [la segmentación de propiedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para los canales de mensajería dentro de la aplicación, sólo se puede hacer referencia a `canvas_entry_properties` en un Canvas. `event_properties` no puede utilizarse para canales de mensajería dentro de la aplicación.
- No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`. 
- Cuando un paso de Ruta de acción contiene un activador "Envió de un mensaje SMS entrante" o "Envió de un mensaje WhatsApp entrante", los pasos posteriores de Canvas pueden incluir una propiedad SMS o WhatsApp Liquid. Esto refleja cómo funcionan las propiedades del evento en los Lienzos. De este modo, puede aprovechar sus mensajes para guardar y consultar datos de origen sobre perfiles de usuario y mensajería conversacional.

### Marcas de tiempo para propiedades del evento

Si utilizas `event_properties` en un Canvas, las marcas de tiempo se normalizan a UTC, con algunas excepciones que se detallan a continuación. Dado este comportamiento, Braze te recomienda encarecidamente que utilices un filtro de zona horaria Liquid como el del ejemplo siguiente para garantizar que tus mensajes se envían con tu [zona horaria preferida]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Excepciones

- Las marcas de tiempo no se normalizan a UTC en el primer paso de un Canvas si ese paso es un paso de Mensaje.
- Las marcas de tiempo no están normalizadas a UTC en ningún paso de Mensaje que utilice el canal de mensajería dentro de la aplicación, independientemente de su orden en el Canvas.

## Caso de uso

![Un paso de Ruta de acción seguido de un paso de Retraso y un paso de Mensaje para los usuarios que han añadido un artículo a su lista de deseos, y una ruta para todos los demás.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para entender mejor las diferencias entre `canvas_entry_properties` y `event_properties`, consideremos este escenario en el que los usuarios entrarán en un Canvas basado en acciones si realizan el evento personalizado "añadir artículo a la lista de deseos". 

Los `canvas_entry_properties` se configuran en el paso [Horario de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de la creación de un lienzo y se corresponderán con el momento en que un usuario entra en un lienzo. Estos `canvas_entry_properties` también pueden ser referenciados en cualquier paso de Mensaje en el Flujo del Lienzo ya que el Flujo del Lienzo soporta propiedades de entrada persistentes. 

En este Canvas, tenemos un recorrido de usuario que comienza con un paso de Action Paths para determinar si un usuario ha añadido un artículo a su wishlist. A partir de aquí, si el usuario ha añadido un artículo, experimentará un retraso antes de recibir el mensaje "¡Nuevo artículo en su lista de deseos!" del paso Mensaje. 

El primer paso de Mensaje en un recorrido de usuario tendrá acceso al `event_properties` personalizado de su paso Rutas de acción. En este caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` en este paso de Mensaje como parte del contenido de nuestro mensaje. Si un usuario no añade un artículo a su lista de deseos, pasa por la ruta Todos los demás, lo que significa que no se puede hacer referencia a `event_properties` y reflejará un error de configuración no válida.

Tenga en cuenta que sólo tendrá acceso a `event_properties` si su paso Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso Rutas de acción. Si el paso Mensaje está conectado a una ruta Todos los demás, pero puede remontarse a un paso Rutas de acción en el recorrido del usuario, entonces también seguirás teniendo acceso a `event_properties`. Para más información sobre estos comportamientos, consulta el [paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

