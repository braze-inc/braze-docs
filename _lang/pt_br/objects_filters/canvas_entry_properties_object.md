---
nav_title: "Objeto de propriedades de entrada da tela"
article_title: Objeto de propriedades de entrada de canvas da API
page_order: 2
page_type: reference
tool:
  - Canvas
description: "Este artigo explica o objeto de propriedades de entrada do Braze Canvas."

---

# Objeto de propriedades de entrada da tela

> Ao usar um dos pontos de extremidade para disparar ou agendar um Canvas por meio da API, você pode fornecer um mapa de chaves e valores para personalizar as mensagens enviadas pelas primeiras etapas do seu Canva, no namespace `canvas_entry_properties`.

{% alert note %}
O objeto de propriedades de entrada do canva tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Corpo do objeto

Esse corpo de objeto contém um exemplo de solicitação.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Por exemplo, uma solicitação com `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` poderia acrescentar a palavra "sapatos" a uma mensagem adicionando ```{{canvas_entry_properties.${product_name}}}``` à solicitação.
{% endraw %}
