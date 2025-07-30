---
nav_title: Propriedades de entrada persistente
article_title: Propriedades de entrada persistente
alias: "/persistent_entry/"
page_type: reference
description: "Este artigo de referência descreve como usar propriedades de entrada persistente em seu Canvas para enviar mensagens com mais curadoria e criar uma experiência de usuário final altamente refinada."
tool: Canvas
page_order: 5
---

# Propriedades de entrada persistente

> Quando um Canvas é disparado por um evento personalizado, uma compra ou uma chamada de API, você pode usar metadados da chamada de API, do evento personalizado ou do evento de compra para personalização em cada etapa do fluxo de trabalho do Canvas. 

Antes desse recurso, as propriedades de entrada só podiam ser usadas na primeira etapa do canva. A capacidade de usar propriedades de entrada em toda a jornada do Canva permite que os clientes enviem mensagens com mais curadoria e criem uma experiência de usuário final altamente refinada.

## Uso de propriedades de entrada

As propriedades de entrada podem ser usadas em Canvas baseadas em ação e disparadas por API. Essas propriedades de entrada são definidas quando um Canvas é disparado por um evento personalizado, uma compra ou uma chamada de API. Consulte os artigos a seguir para saber mais:

- [Objeto de propriedades de entrada da tela]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [Objeto de propriedades do evento]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

As propriedades transmitidas por esses objetos podem ser referenciadas usando a tag `canvas_entry_properties` Liquid. Por exemplo, uma solicitação com `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` poderia acrescentar a palavra "shoes" (sapatos) a uma mensagem, adicionando o Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Quando um Canvas inclui uma mensagem com a tag `canvas_entry_properties` Liquid, os valores associados a essas propriedades serão salvos durante a jornada do usuário no Canvas e excluídos quando o usuário sair do Canvas. Note que as propriedades de entrada do canva só estão disponíveis para referência no Liquid. Para filtrar as propriedades dentro do canva, use [a segmentação de propriedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
O objeto de propriedades de entrada do canva tem um limite máximo de tamanho de 50 KB.
{% endalert %}

## Atualização do Canva para usar as propriedades de entrada

Se um Canvas ativo que anteriormente não incluía nenhuma mensagem que usasse `canvas_entry_properties` for editado para incluir `canvas_entry_properties`, o valor correspondente a essa propriedade não estará disponível para os usuários que entraram no Canvas antes de `canvas_entry_properties` ter sido adicionado ao Canvas. Os valores só serão salvos para os usuários que entrarem no Canva depois que a alteração for feita.

Por exemplo, se você lançou inicialmente um Canvas que não usava nenhuma propriedade de entrada em 3 de novembro e, em seguida, adicionou uma nova propriedade `product_name` ao Canvas em 11 de novembro, os valores de `product_name` só seriam salvos para os usuários que entraram no Canvas a partir de 11 de novembro.

No caso de uma propriedade de entrada do canva ser nula ou estar em branco, você pode abortar as mensagens usando condicionais. O trecho de código a seguir é um exemplo de como você poderia usar o Liquid para cancelar uma mensagem.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Para saber mais sobre o cancelamento de mensagens com o Liquid, consulte [a documentação do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages).

## Propriedades globais da entrada do Canva

Com `canvas_entry_properties`, é possível definir propriedades globais que se aplicam a todos os usuários ou propriedades específicas do usuário que se aplicam apenas ao usuário especificado. A propriedade específica do usuário substituirá a propriedade global para esse usuário.

### Exemplo de solicitação

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
 
Nessa solicitação, o valor global de "food allergies" (alergias alimentares) é "none" (nenhuma). Para Customer_123, o valor é "dairy". As mensagens nesse Canva que contêm o snippet do Liquid {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} terão como modelo "dairy" para Customer_123 e "none" para todos os outros. 

## Caso de uso

Se você tiver um Canvas que é disparado quando um usuário navega por um item em seu site de comércio eletrônico, mas não o adiciona ao carrinho, a primeira etapa do Canvas pode ser uma notificação por push perguntando se ele está interessado em comprar o item. Você pode fazer referência ao nome do produto usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

A segunda etapa pode enviar outra notificação por push solicitando que o usuário finalize a compra, caso tenha adicionado o item ao carrinho, mas ainda não o tenha comprado. Você pode continuar a fazer referência à propriedade de entrada `product_name` usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

