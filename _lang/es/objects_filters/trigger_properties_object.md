---
nav_title: "Objeto de propiedades de activación"
article_title: Objeto de propiedades de desencadenante de API
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto de propiedades de desencadenar."
tool: Campaigns

---

# Objeto desencadenar propiedades

> Cuando utilices uno de los puntos finales para enviar una campaña con entrega desencadenada por API, puedes proporcionar un mapeado de claves y valores para personalizar tu mensaje.

Si realizas una solicitud a la API que contenga un objeto en `trigger_properties`, los valores de ese objeto pueden referenciarse en tu plantilla de mensajes bajo el espacio de nombres `api_trigger_properties`. Por ejemplo, una solicitud con lo siguiente podría añadir la palabra `"shoes"` a un mensaje añadiendo {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}. 

Ten en cuenta que, aunque las propiedades desencadenantes pueden incluirse en plantillas de mensajes, no se almacenan automáticamente en el perfil de usuario de forma predeterminada.

{% alert note %}
El objeto `trigger_properties` y la sintaxis {% raw %}`api_trigger_properties.${product_name}`{% endraw %} solo se admiten en campañas. Para personalizar mensajes con claves y valores de una solicitud de desencadenamiento de API para Canvas, utiliza el [objeto de propiedades de entrada de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). El objeto `trigger_properties` tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Cuerpo del objeto

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


