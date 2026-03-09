---
nav_title: "Objeto de contexto Canvas"
article_title: Objeto de contexto API Canvas
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "Este artículo explica el objeto de contexto BRAZE CANVAS."

---

# Objeto de contexto Canvas

> Cuando utilices uno de los puntos finales para desencadenar o programar un Canvas a través de la API, puedes proporcionar un mapa de claves y valores para personalizar los mensajes enviados por los primeros pasos de tu Canvas, en el espacio de nombres `context`.

{% alert note %}
El objeto de contexto tiene un límite de tamaño máximo de 50 KB.
{% endalert %}

## Cuerpo del objeto

Este cuerpo de objeto contiene una petición de ejemplo.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Por ejemplo, puedes incluir`"context": {"product_name" : "shoes", "product_price" : 79.99}`  en tu solicitud de API y luego hacer referencia a la palabra «zapatos» en tu mensaje añadiendo```{{context.${product_name}}}```  a la plantilla del mensaje.
{% endraw %}
