---
nav_title: "Objeto de propriedades do disparador"
article_title: Objeto de propriedades do disparador da API
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de propriedades do disparo."
tool: Campaigns

---

# Objeto de propriedades do disparador

> Ao usar um dos pontos de extremidade para enviar uma campanha com entrega disparada por API, você pode fornecer um mapa de chaves e valores para personalizar sua mensagem.

Se você fizer uma solicitação de API que contenha um objeto em `trigger_properties`, os valores desse objeto poderão ser referenciados em seu modelo de mensagem no namespace `api_trigger_properties`. Por exemplo, uma solicitação como esta poderia adicionar a palavra `"shoes"` a uma mensagem, acrescentando {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}. 

Observe que, embora as propriedades de gatilho possam ser modeladas em mensagens, elas não são armazenadas automaticamente no perfil do usuário por padrão.

{% alert note %}
O objeto `trigger_properties` e a sintaxe {% raw %}`api_trigger_properties.${product_name}`{% endraw %} são compatíveis apenas com campanhas. Para personalizar o envio de mensagens com chaves e valores de uma solicitação de disparo de API para o Canvas, use o [objeto de propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). O objeto `trigger_properties` tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Corpo do objeto

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


