---
nav_title: Atualização do usuário
article_title: Atualização do usuário 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Este artigo de referência aborda o componente User Update e como usá-lo em seus Canvases."
tool: Canvas
---

# Atualização do usuário 

> O componente User Update permite atualizar os atributos, eventos e compras de um usuário em um compositor JSON, de modo que não há necessidade de incluir informações confidenciais, como chaves de API.

## Como esse componente funciona

Uma etapa de atualização do usuário chamada "Atualizar fidelidade" que atualiza um atributo "É membro Premium" para "verdadeiro".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Ao usar esse componente em seu Canvas, as atualizações não contam para o limite de taxa de `/users/track` solicitações por minuto. Em vez disso, essas atualizações são agrupadas para que o Braze possa processá-las com mais eficiência do que um webhook Braze-to-Braze. Observe que esse componente não registra [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) quando é usado para atualizar pontos de dados não faturáveis (como grupos de assinatura).

Os usuários só avançarão para as próximas etapas do Canvas depois que as atualizações relevantes do usuário forem concluídas. Isso significa que qualquer mensagem subsequente que dependa dessas atualizações do usuário estará atualizada quando a próxima etapa for executada.

## Criação de uma atualização de usuário

Arraste e solte o componente da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior da variante ou etapa e selecione **User Update (Atualização do usuário**). 

Há três opções que permitem atualizar as informações existentes, adicionar novas ou remover informações do perfil do usuário. Combinadas, as etapas do User Update em um espaço de trabalho podem atualizar até 200.000 perfis de usuário por minuto.

{% alert tip %}
Você também pode testar as alterações feitas com esse componente pesquisando um usuário e aplicando a alteração a ele. Isso atualizará o usuário.
{% endalert %}

### Atualização de atributos personalizados

Para adicionar ou atualizar um atributo personalizado, selecione um nome de atributo em sua lista de atributos e digite o valor da chave.

Etapa de atualização do usuário que atualiza os dois atributos "Loyalty Member" e "Loyalty Program" para "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Remoção de atributos personalizados

Para remover um atributo personalizado, selecione o nome do atributo usando o menu suspenso. Você pode alternar para o [compositor JSON avançado](#advanced-json-composer) para editar mais. 

Etapa de atualização do usuário que remove um atributo "Loyalty Member".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valores crescentes e decrescentes

A etapa de atualização do usuário pode aumentar ou diminuir um valor de atributo. Selecione o atributo, selecione **Increment By (Aumentar por** ) ou **Decrement By (Diminuir por)** e digite um número. 

#### Acompanhe o progresso semanal

Ao incrementar um atributo personalizado que rastreia um evento, você pode rastrear o número de aulas que um usuário fez em uma semana. Usando esse componente, a contagem de turmas pode ser redefinida no início da semana e começar a ser rastreada novamente. 

Etapa de atualização do usuário que incrementa o atributo "class_count" em um.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Atualização de uma matriz de objetos

Uma [matriz de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) é um atributo personalizado armazenado no perfil de um usuário que é rico em dados. Isso permite que você crie um histórico das interações do usuário com a sua marca. Isso permite que você crie segmentos com base em um atributo personalizado que é um campo calculado, como o histórico de compras ou o valor total do tempo de vida.

A etapa de atualização do usuário pode adicionar ou remover atributos a essa matriz de objetos. Para atualizar uma matriz, selecione o nome do atributo da matriz em sua lista de atributos e digite o valor da chave.

#### Caso de uso: Atualização da lista de desejos de um usuário

Adicionar ou remover um item a uma matriz atualiza a lista de desejos do usuário.

\![Etapa de atualização do usuário que adiciona um item "sunblock" ao atributo "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Caso de uso: Cálculo do total do carrinho de compras

Acompanhe quando um usuário tem itens em seu carrinho de compras, quando ele adiciona novos itens ou remove itens e qual é o valor total do carrinho de compras. 

1. Crie uma matriz personalizada de objetos chamada `shopping_cart`. O exemplo a seguir mostra a aparência desse atributo. Cada item tem um `product_id` exclusivo que possui dados mais complexos em sua própria matriz aninhada de objetos, incluindo `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\. Crie um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) chamado `add_item_to_cart` que é registrado quando um usuário adiciona um item à cesta.
3\. Crie um Canvas com um público-alvo de usuários com esse evento personalizado. Agora, quando um usuário adiciona um item ao carrinho, esse Canvas é acionado. Em seguida, você pode direcionar mensagens diretamente para esse usuário, oferecendo códigos de cupom quando ele atingir um determinado gasto, abandonar o carrinho por um determinado período de tempo ou qualquer outra coisa que se alinhe ao seu caso de uso. 

O atributo `shopping_cart` contém o total de muitos eventos personalizados: o custo total de todos os itens, o número total de itens no carrinho, se o carrinho de compras contém um presente e assim por diante. Isso pode ser parecido com o seguinte:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"]
         "gift": yes,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Definição da propriedade de entrada do Canvas como um atributo

Você pode usar a etapa de atualização do usuário para manter um `canvas_entry_property`. Digamos que você tenha um evento que é acionado quando um item é adicionado a um carrinho. Você pode armazenar o ID do item mais recente adicionado ao carrinho e usá-lo em uma campanha de remarketing. Use o recurso de personalização para recuperar uma propriedade de entrada do Canvas e armazená-la em um atributo.

Etapa de atualização do usuário que atualiza o atributo "most_recent_cart_item" com um ID de item.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalização

Para armazenar a propriedade do evento de acionamento de um Canvas como um atributo, use o modal de personalização para extrair e armazenar a propriedade de entrada do Canvas. O User Update também oferece suporte aos seguintes recursos de personalização: 
* [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriedades de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Lógica líquida (incluindo [mensagens de interrupção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Várias atualizações de atributos ou eventos por objeto

{% alert warning %}
Recomendamos o uso cuidadoso da personalização do Connected Content Liquid nas etapas de atualização do usuário, pois esse tipo de etapa tem um limite de taxa de 200.000 solicitações por minuto. Esse limite de taxa substitui o limite de taxa do Canvas.
{% endalert %}

## Compositor JSON avançado

Adicione um atributo, evento ou objeto JSON de compra com até 65.536 caracteres ao compositor JSON. A [assinatura global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) de um usuário e o estado [do grupo de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) também podem ser definidos.

\![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando o compositor avançado, você também pode visualizar e testar se o perfil do usuário está atualizado com as alterações na guia **Visualizar e testar**. Você pode selecionar um usuário aleatório ou procurar um usuário específico. Em seguida, depois de enviar um teste para um usuário, visualize o perfil do usuário usando o link gerado.

\![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerações

Você não precisa incluir dados confidenciais, como sua chave de API, ao usar o compositor JSON, pois isso é fornecido automaticamente pela plataforma. Dessa forma, os campos a seguir são desnecessários e não devem ser usados no compositor JSON:
* ID de usuário externo
* Chave da API
* URL do cluster do Braze
* Campos relacionados a importações de tokens push

{% raw %}
### Registrar eventos personalizados

Usando o compositor JSON, você também pode registrar eventos personalizados. Observe que isso requer um registro de data e hora no formato ISO, portanto, é necessário atribuir uma hora e uma data com Liquid no início. Considere este exemplo que registra um evento com uma hora.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

O próximo exemplo vincula um evento a um aplicativo específico usando um evento personalizado com propriedades opcionais e o `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Editar o estado da assinatura

No compositor JSON, você também pode editar o estado da assinatura do usuário. Por exemplo, o seguinte mostra o estado da assinatura de um usuário atualizado para `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Atualizar grupos de assinaturas 

Você também pode atualizar os grupos de assinatura usando essa etapa do Canvas. O exemplo a seguir mostra uma atualização dos grupos de assinatura. Você pode realizar uma ou várias atualizações de grupos de assinatura.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

