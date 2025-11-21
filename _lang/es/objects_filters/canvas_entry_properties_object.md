---
nav_title: "Objeto de propiedades de entrada del lienzo"
article_title: Objeto de propiedades de entrada de API de Canvas
page_order: 2
page_type: reference
tool:
  - Canvas
description: "Este artículo explica el objeto de propiedades de entrada Braze Canvas."

---

# Objeto de propiedades de entrada al Canvas

> Cuando utilices uno de los puntos finales para desencadenar o programar un Canvas a través de la API, puedes proporcionar un mapa de claves y valores para personalizar los mensajes enviados por los primeros pasos de tu Canvas, en el espacio de nombres `canvas_entry_properties`.

{% alert note %}
El objeto Propiedades de entrada del lienzo tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Cuerpo del objeto

Este cuerpo de objeto contiene una petición de ejemplo.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Por ejemplo, una solicitud con `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` podría añadir la palabra "zapatos" a un mensaje añadiendo ```{{canvas_entry_properties.${product_name}}}``` a la solicitud.
{% endraw %}
