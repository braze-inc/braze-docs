---
nav_title: Propiedades de entrada persistente
article_title: Propiedades de entrada persistente
alias: "/persistent_entry/"
page_type: reference
description: "Este artículo de referencia describe cómo utilizar propiedades de entrada persistentes en su Canvas para enviar mensajes más curados y crear una experiencia de usuario final altamente refinada."
tool: Canvas
page_order: 5
---

# Propiedades de entrada persistentes

> Cuando un lienzo se activa mediante un evento personalizado, una compra o una llamada a la API, puede utilizar los metadatos de la llamada a la API, el evento personalizado o el evento de compra para la personalización en cada paso del flujo de trabajo del lienzo. 

Antes de esta función, las propiedades de entrada sólo podían utilizarse en el primer paso de Canvas. La posibilidad de utilizar propiedades de entrada a lo largo de un recorrido de Canvas permite a los clientes enviar mensajes más curados y crear una experiencia de usuario final muy refinada.

## Uso de las propiedades de entrada

Las propiedades de entrada pueden utilizarse en lienzos basados en acciones y activados por API. Estas propiedades de entrada se definen cuando un Canvas es activado por un evento personalizado, una compra o una llamada a la API. Consulte los siguientes artículos para obtener más información:

- [Objeto de propiedades de entrada del lienzo]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Objeto de propiedades de eventos]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Las propiedades pasadas desde estos objetos pueden ser referenciadas utilizando la etiqueta `canvas_entry_properties` Liquid. Por ejemplo, una solicitud con `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` podría añadir la palabra "zapatos" a un mensaje añadiendo {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} de Liquid.

Cuando un lienzo incluye un mensaje con la etiqueta `canvas_entry_properties` Liquid, los valores asociados a esas propiedades se guardarán mientras dure el recorrido del usuario en el lienzo y se borrarán cuando el usuario salga del lienzo. Tenga en cuenta que las propiedades de entrada de Canvas sólo están disponibles como referencia en Liquid. Para filtrar las propiedades dentro del lienzo, utilice [la segmentación de propiedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
El objeto Propiedades de entrada del lienzo tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Actualización de Canvas para utilizar propiedades de entrada

Si un lienzo activo que anteriormente no incluía ningún mensaje que utilizara `canvas_entry_properties` se edita para incluir `canvas_entry_properties`, el valor correspondiente a esa propiedad no estará disponible para los usuarios que entraron en el lienzo antes de que se añadiera `canvas_entry_properties` al lienzo. Los valores sólo se guardarán para los usuarios que entren en el Lienzo después de realizar el cambio.

Por ejemplo, si inicialmente lanzó un lienzo que no utilizaba ninguna propiedad de entrada el 3 de noviembre, y luego añadió una nueva propiedad `product_name` al lienzo el 11 de noviembre, los valores de `product_name` sólo se guardarían para los usuarios que entraran en el lienzo a partir del 11 de noviembre.

En el caso de que una propiedad de entrada del Lienzo sea nula o esté en blanco, puede abortar los mensajes utilizando condicionales. El siguiente fragmento de código es un ejemplo de cómo utilizar Liquid para abortar un mensaje.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Para saber más sobre cómo anular mensajes con Liquid, consulta nuestra [documentación sobre Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propiedades globales de la entrada Canvas

Con `canvas_entry_properties`, puede establecer propiedades globales que se apliquen a todos los usuarios o propiedades específicas de usuario que sólo se apliquen al usuario especificado. La propiedad específica del usuario sustituirá a la propiedad global para ese usuario.

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
 
En esta solicitud, el valor global de "alergias alimentarias" es "ninguna". Para Cliente_123, el valor es "lácteos". Los mensajes de este Canvas que contengan el fragmento de Liquid {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} tendrán como plantilla "dairy" para Customer_123 y "none" para todos los demás. 

## Caso de uso

Si tienes un Canvas que se desencadena cuando un usuario navega por un artículo en tu sitio de comercio electrónico pero no lo añade a su cesta, el primer paso del Canvas podría ser una notificación push preguntándole si está interesado en comprar el artículo. Puede hacer referencia al nombre del producto utilizando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

El segundo paso puede enviar otra notificación push para pedir al usuario que realice el pago si ha añadido el artículo a su cesta pero aún no lo ha comprado. Puede seguir haciendo referencia a la propiedad de entrada `product_name` utilizando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

