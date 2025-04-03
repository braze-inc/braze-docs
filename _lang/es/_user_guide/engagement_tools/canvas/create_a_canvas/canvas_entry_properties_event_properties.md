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
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Este artículo está disponible como referencia cuando se utiliza `canvas_entry_properties` y `event_properties`para el flujo de trabajo original de Canvas.
{% endalert %}

Las propiedades de entrada del lienzo y las propiedades de evento funcionan de forma diferente en los flujos de trabajo del lienzo. Las propiedades de los eventos o llamadas a la API que desencadenan la entrada de un usuario en un Canvas se conocen como `canvas_entry_properties`. Las propiedades de los eventos que se producen a medida que un usuario se desplaza por un recorrido de Canvas se conocen como `event_properties`. La diferencia clave aquí es que `canvas_entry_properties` no sólo se centra en los eventos, sino que también accede a las propiedades de las cargas útiles de entrada en los lienzos activados por la API.

Para el editor de lienzo original y el flujo de lienzo, no se puede utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.

El comportamiento también varía entre los flujos de trabajo creados con Canvas Flow y el editor original. Por ejemplo, en el editor Canvas original, puede utilizar `event_properties` en el primer paso completo si se trata de un paso basado en acciones. En Canvas Flow, no se admiten pasos completos, por lo que esto no se aplica.

En la siguiente tabla se resumen las diferencias entre `canvas_entry_properties` y `event_properties`.

| | Propiedades de entrada de Canvas | Propiedades del evento
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistencia** | Puede ser referenciado por todos los pasos [del Mensaje][1] durante la duración de un Canvas construido usando el Flujo del Canvas. | \- Solo puede referenciarse una vez. <br> \- No puede ser referenciado por ningún paso de Mensaje posterior. |
| **Comportamiento original en lienzo** | \- Debe tener activadas las propiedades de entrada persistente. <br> \- Sólo puede hacer referencia a `canvas_entry_properties` en el primer paso completo de un Canvas. El Canvas debe estar basado en acciones o activado por la API. | \- Puede hacer referencia a `event_properties` en cualquier paso completo que utilice la entrega basada en acciones en un lienzo. <br> \- No puede utilizarse en pasos completos programados que no sean el primer paso completo de un Canvas basado en acciones. Sin embargo, si un usuario está utilizando un [componente Canvas][2], el comportamiento sigue las reglas de Canvas Flow para `event_properties`. |
| **Comportamiento de Canvas Flow** | Puede hacer referencia a `canvas_entry_properties` en cualquier paso de un Canvas. Para el comportamiento posterior al lanzamiento, consulta [Editar lienzos después del lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Puede hacer referencia a `event_properties` en el primer paso de Mensaje **después de** un paso de [Rutas de acción][3] en el que la acción realizada es un evento personalizado o un evento de compra. <br> \- No puede estar después de la ruta Todos los demás del paso Vías de acción. <br> \- Puede tener otros componentes que no sean del Lienzo de Mensajes entre las Rutas de Acción y los pasos de Mensajes. Si uno de estos componentes que no son Mensajes es un paso de Ruta de Acción, el usuario puede ir a través de la ruta Todos los demás de esa ruta de acción. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Tenga en cuenta que las propiedades de entrada de Canvas sólo están disponibles como referencia en Liquid. Para filtrar las propiedades dentro del lienzo, utilice [la segmentación de propiedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
Para los canales de mensajes in-app, `canvas_entry_properties` sólo puede referenciarse en Canvas Flow y en el editor Canvas original si tienes activadas [las propiedades de entrada persistente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) en el editor original como parte del acceso anticipado anterior. Sin embargo, `event_properties` no puede utilizarse para canales de mensajería dentro de la aplicación.
{% endalert %}

Cuando un paso de Ruta de acción contiene un activador "Envió de un mensaje SMS entrante" o "Envió de un mensaje WhatsApp entrante", los pasos posteriores de Canvas pueden incluir una propiedad SMS o WhatsApp Liquid. Esto refleja cómo funcionan las propiedades de eventos en el Canvas Flow. De este modo, puede aprovechar sus mensajes para guardar y consultar datos de origen sobre perfiles de usuario y mensajería conversacional.

## Caso de uso

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Para entender mejor las diferencias entre `canvas_entry_properties` y `event_properties`, consideremos este escenario en el que los usuarios entrarán en un Canvas basado en acciones si realizan el evento personalizado "añadir artículo a la lista de deseos". 

Los `canvas_entry_properties` se configuran en el paso [Horario de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de la creación de un lienzo y se corresponderán con el momento en que un usuario entra en un lienzo. Estos `canvas_entry_properties` también pueden ser referenciados en cualquier paso de Mensaje en el Flujo del Lienzo ya que el Flujo del Lienzo soporta propiedades de entrada persistentes. 

En este Canvas, tenemos un recorrido de usuario que comienza con un paso de Action Paths para determinar si un usuario ha añadido un artículo a su wishlist. A partir de aquí, si el usuario ha añadido un artículo, experimentará un retraso antes de recibir el mensaje "¡Nuevo artículo en su lista de deseos!" del paso Mensaje. 

El primer paso de Mensaje en un recorrido de usuario tendrá acceso al `event_properties` personalizado de su paso Rutas de acción. En este caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` en este paso de Mensaje como parte del contenido de nuestro mensaje. Si un usuario no añade un artículo a su lista de deseos, pasa por la ruta Todos los demás, lo que significa que no se puede hacer referencia a `event_properties` y reflejará un error de configuración no válida.

Tenga en cuenta que sólo tendrá acceso a `event_properties` si su paso Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso Rutas de acción. Si el paso Mensaje está conectado a una ruta Todos los demás, pero puede remontarse a un paso Rutas de acción en el recorrido del usuario, entonces también seguirás teniendo acceso a `event_properties`. Para más información sobre estos comportamientos, consulta [Paso de mensajes][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
