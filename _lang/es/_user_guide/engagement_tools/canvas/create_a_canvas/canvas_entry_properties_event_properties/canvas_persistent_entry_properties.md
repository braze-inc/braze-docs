---
nav_title: Propiedades de entrada persistente
article_title: Propiedades de entrada persistente
alias: "/persistent_entry/"
page_type: reference
description: "Este artículo de referencia describe cómo utilizar propiedades de entrada persistentes en tu Canvas para enviar más mensajes de selección y crear una experiencia de usuario final muy refinada."
tool: Canvas
page_order: 5
---

# Propiedades de entrada persistente

> Cuando un Canvas se desencadena por un evento personalizado, una compra o una llamada a la API, puedes utilizar los metadatos de la llamada a la API, el evento personalizado o el evento de compra para la personalización en cada paso de tu flujo de trabajo en Canvas. Puedes utilizar estas propiedades para enviar mensajes más seleccionados.

{% alert important %}
Las propiedades de entrada persistentes son un artefacto del editor original de Canvas, por lo que hay referencias obsoletas a términos que permanecen como referencia histórica. Para el editor de Canvas actualizado, consulta [Propiedades de la entrada y Propiedades del evento en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).
{% endalert %}

## Uso de las propiedades de la entrada

Las propiedades de entrada pueden utilizarse en Lienzos basados en acciones y desencadenados por API. Estas propiedades de entrada se definen cuando un Canvas se desencadena por un evento personalizado, una compra o una llamada a la API. Consulta los siguientes artículos para obtener más información:

- [Objeto de propiedades de entrada al Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Objeto de propiedades del evento]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Se puede hacer referencia a las propiedades pasadas desde estos objetos utilizando la etiqueta de Liquid `canvas_entry_properties`. Por ejemplo, una solicitud con `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` podría añadir la palabra "zapatos" a un mensaje añadiendo el Líquido {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Cuando un Canvas incluya un mensaje con la etiqueta de Liquid `canvas_entry_properties`, los valores asociados a esas propiedades se guardarán mientras dure el recorrido del usuario en el Canvas y se borrarán cuando el usuario salga de él. Ten en cuenta que las propiedades de entrada en Canvas sólo están disponibles como referencia en Liquid. Para filtrar por las propiedades dentro del Canvas, utiliza en su lugar [la segmentación de propiedades del evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
El objeto Propiedades de entrada del Canvas tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Actualizar Canvas para utilizar propiedades de entrada

Si un Canvas activo que anteriormente no incluía ningún mensaje que utilizara `canvas_entry_properties` se edita para incluir `canvas_entry_properties`, el valor correspondiente a esa propiedad no estará disponible para los usuarios que entraron en el Canvas antes de que se añadiera `canvas_entry_properties` al Canvas. Los valores sólo se guardarán para los usuarios que entren en el Canvas después de realizar el cambio.

Por ejemplo, si inicialmente lanzas un Canvas que no utiliza ninguna propiedad de entrada el 3 de noviembre, y luego añades una nueva propiedad `product_name` al Canvas el 11 de noviembre, los valores de `product_name` sólo se guardarán para los usuarios que hayan entrado en el Canvas a partir del 11 de noviembre.

En el caso de que una propiedad de entrada del Canvas sea nula o esté en blanco, puedes abortar mensajes utilizando condicionales. El siguiente fragmento de código es un ejemplo de cómo podrías utilizar Liquid para abortar un mensaje.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Para saber más sobre cómo abortar mensajes con Liquid, consulta nuestra [documentación sobre Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propiedades globales de entrada al Canvas

Con `canvas_entry_properties`, puedes establecer propiedades globales que se apliquen a todos los usuarios o propiedades específicas de usuario que sólo se apliquen al usuario especificado. La propiedad específica del usuario sustituirá a la propiedad global para ese usuario.

### Ejemplo de solicitud

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
En esta solicitud, el valor global de "alergias alimentarias" es "ninguna". Para Customer_123, el valor es "lácteos". Los mensajes de este Canvas que contengan el fragmento de código Liquid {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} tendrán una plantilla con "lácteos" para Customer_123 y "ninguno" para todos los demás. 

## Casos de uso

Si tienes un Canvas que se desencadena cuando un usuario navega por un artículo en tu sitio de comercio electrónico pero no lo añade a su cesta, el primer paso del Canvas podría ser una notificación push preguntándole si está interesado en comprar el artículo. Puedes hacer referencia al nombre del producto utilizando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

\![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

El segundo paso puede enviar otra notificación push para pedir al usuario que realice la compra si ha añadido el artículo a su cesta pero aún no lo ha comprado. Puedes seguir haciendo referencia a la propiedad de entrada `product_name` utilizando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

\![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

