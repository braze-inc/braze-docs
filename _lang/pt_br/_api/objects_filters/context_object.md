---
nav_title: "Objeto de contexto do Canvas"
article_title: Objeto de contexto da API Canvas
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "Este artigo explica o objeto de contexto do Braze Canvas."

---

# Objeto de contexto do Canvas

> Ao usar um dos pontos de extremidade para disparar ou agendar um Canvas por meio da API, você pode fornecer um mapa de chaves e valores para personalizar as mensagens enviadas pelas primeiras etapas do seu Canva, no namespace `context`.

{% alert note %}
O objeto de contexto tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Corpo do objeto

Esse corpo de objeto contém um exemplo de solicitação.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
Por exemplo, você pode incluir `"context": {"product_name" : "shoes", "product_price" : 79.99}` na sua solicitação de API e então referenciar a palavra "sapatos" na sua mensagem adicionando ```{{context.${product_name}}}``` ao modelo da mensagem.
{% endraw %}
