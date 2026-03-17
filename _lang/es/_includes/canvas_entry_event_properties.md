Puedes utilizar las propiedades de entrada y las propiedades del evento de Canvas en tus recorridos de usuario de Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Las propiedades de entrada del lienzo]({{site.baseurl}}/api/objects_filters/context_object/) son las propiedades que se asignan a los lienzos basados en acciones o activados por la API. El objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB.

{% alert note %}
En el caso concreto de los canales de mensajes dentro de la aplicación, solo`context` se puede hacer referencia a ellos en Canvas.
{% endalert %}

Puedes hacer referencia a`context`  en cualquier paso de mensaje con este formato Liquid: ``{% raw %} context.${property_name} {% endraw %}``. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

#### Caso de uso

{% raw %}
Supongamos que una tienda minorista, RetailApp, tiene la siguiente petición: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp puede incluir el nombre del producto (zapatos) en un mensaje con este Liquid: `{{context.${product_name}}}`.
{% endraw %}

RetailApp también puede activar el envío de mensajes específicos para diferentes propiedades de `product_name` en un Canvas dirigido a los usuarios después de que hayan activado un evento de compra. Por ejemplo, pueden enviar mensajes diferentes a los usuarios que compraron zapatos y a los usuarios que compraron otra cosa añadiendo el siguiente Líquido en un paso de Mensaje.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible sólo como referencia. Para los lienzos creados con el editor original, las propiedades de entrada del lienzo solo se pueden consultar en el primer paso completo de un lienzo.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Las propiedades de eventos se refieren a las propiedades que usted establece para los eventos y compras personalizados. Estos `event_properties` se pueden utilizar en campañas con entrega basada en acciones y Lienzos.

{% alert important %}
No puedes utilizar`event_properties`  en el primer paso Mensaje de tu Canvas. En su lugar, debe utilizar `context` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.
{% endalert %}

En Canvas, las propiedades del evento personalizado y las propiedades de la compra se pueden utilizar en Liquid en cualquier paso de mensaje que siga a un paso de rutas de acción. Asegúrate de utilizar  {% raw %}``{{event_properties.${property_name}}}``{% endraw %} si haces referencia a estas propiedades del evento. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el primer paso Mensaje que sigue a una ruta de acción, puedes utilizar las propiedades del evento relacionadas con el evento al que se hace referencia en esa ruta de acción. Sin embargo, estas propiedades del evento solo se pueden utilizar si el usuario realmente ha realizado la acción (y no ha sido clasificado en el grupo «Todos los demás»). Puede tener otros pasos (que no sean otra Ruta de Acción o paso de Mensaje) entre esta Ruta de Acción y el paso de Mensaje.

{% details Expand for original Canvas editor %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible sólo como referencia. En el editor Canvas original, las propiedades del evento no se pueden utilizar en pasos completos programados. Sin embargo, puedes utilizar las propiedades del evento en el primer paso completo de un lienzo basado en acciones, incluso si el paso completo está programado.

{% enddetails %}

{% endtab %}
{% endtabs %}

Consulta las [propiedades de la entrada y las propiedades del evento en]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) Canvas para obtener más información y ejemplos.