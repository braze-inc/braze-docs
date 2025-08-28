---
nav_title: Atualização de usuário 
article_title: Atualização de usuário 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Este artigo de referência aborda o componente atualização do usuário e como usá-lo em seus canvas."
tool: Canvas
---

# Atualização de usuário 

> O componente atualização de usuários permite atualizar as atribuições, os eventos e as compras de um usuário em um criador de JSON, portanto, não há necessidade de incluir informações confidenciais, como chaves de API.

## Como esse componente funciona

![Uma etapa de atualização de usuário chamada "Atualizar fidelidade" que atualiza uma atribuição "Is Premium Member" para "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Ao usar esse componente em seu Canva, as atualizações não contam para o limite de frequência de `/users/track` solicitações por minuto. Em vez disso, essas atualizações são agrupadas para que o Braze possa processá-las com mais eficiência do que um webhook de Braze para Braze. Note que esse componente não consome [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) quando está sendo usado para atualizar pontos de dados não faturáveis (como grupos de inscrições).

Os usuários só avançarão para as próximas etapas do Canva depois que as atualizações relevantes do usuário tiverem sido concluídas. Isso significa que qualquer envio de mensagens subsequente que dependa dessas atualizações do usuário estará atualizado quando a próxima etapa for executada.

## Criação de uma atualização de usuário

Arraste e solte o componente da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior da variante ou etapa e selecione **Atualização do usuário**. 

Há três opções que permitem atualizar as informações existentes, adicionar novas ou remover informações do perfil do usuário. Combinadas, as etapas de atualização de usuários em um espaço de trabalho podem atualizar até 200.000 perfis de usuários por minuto.

{% alert tip %}
Também é possível testar as alterações feitas com esse componente pesquisando um usuário e aplicando a alteração a ele. Isso atualizará o usuário.
{% endalert %}

### Atualização de atributos personalizados

Para adicionar ou atualizar um atributo personalizado, selecione um nome de atributo em sua lista de atributos e digite o valor da chave.

![Etapa de atualização do usuário que atualiza as duas atribuições "Loyalty Member" e "Loyalty Program" para "true".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Remoção de atributos personalizados

Para remover um atributo personalizado, selecione o nome do atributo usando o menu suspenso. Você pode mudar para o [criador JSON avançado](#advanced-json-composer) para fazer edições mais complexas. 

![Etapa de atualização do usuário que remove uma atribuição "Membro de fidelidade".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valores crescentes e decrescentes

A etapa de atualização do usuário pode aumentar ou diminuir um valor de atribuição. Selecione a atribuição, selecione **Increment By (Aumentar por** ) ou **Decrement By (Diminuir por)** e digite um número. 

#### Rastreamento do progresso semanal

Ao incrementar um atributo personalizado que rastreia um evento, é possível rastrear o número de aulas que um usuário teve em uma semana. Usando esse componente, a contagem de classes pode ser redefinida no início da semana e começar o rastreamento novamente. 

![Etapa de atualização do usuário que incrementa a atribuição "class_count" em um.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Atualização de um vetor de objetos

Um [vetor de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) é um atributo personalizado armazenado no perfil de um usuário que é rico em dados. Isso permite que você crie um histórico das interações do usuário com a sua marca. Isso permite que você crie segmentos com base em um atributo personalizado que é um campo calculado, como histórico de compras ou valor total do tempo de vida.

A etapa de atualização do usuário pode adicionar ou remover atribuições a esse vetor de objetos. Para atualizar uma matriz, selecione o nome do atributo da matriz em sua lista de atribuições e digite o valor da chave.

#### Caso de uso: Atualização da lista de desejos de um usuário

Adicionar ou remover um item a uma matriz atualiza a lista de desejos do usuário.

![Etapa de atualização do usuário que adiciona um item "sunblock" ao atributo "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Caso de uso: Cálculo do total do carrinho de compras

Rastreie quando um usuário tem itens em seu carrinho de compras, quando adiciona novos itens ou remove itens e qual é o valor total do carrinho de compras. 

1. Crie um vetor personalizado de objetos chamado `shopping_cart`. O exemplo a seguir mostra a aparência desse atributo. Cada item tem um `product_id` exclusivo que tem dados mais complexos em seu próprio vetor aninhado de objetos, incluindo `price`.

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
3\. Crie uma tela com um público-alvo de usuários com esse evento personalizado. Agora, quando um usuário adiciona um item ao carrinho, esse Canva é disparado. Em seguida, é possível direcionar o envio de mensagens diretamente para esse usuário, oferecendo códigos de cupom quando ele atingir um determinado gasto, abandonar o carrinho por um determinado período de tempo ou qualquer outra coisa que se alinhe ao seu caso de uso. 

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

## Definição da propriedade de entrada do Canva como uma atribuição

É possível usar a etapa de atualização do usuário para manter um `canvas_entry_property`. Digamos que você tenha um evento que dispara quando um item é adicionado a um carrinho. Você pode armazenar o ID do item mais recente adicionado ao carrinho e usá-lo em uma campanha de remarketing. Use o recurso de personalização para recuperar uma propriedade de entrada do Canva e armazená-la em uma atribuição.

![Etapa de atualização do usuário que atualiza a atribuição "most_recent_cart_item" com um ID de item.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalização

Para armazenar a propriedade do evento de gatilho de um Canvas como uma atribuição, use o modal de personalização para extrair e armazenar a propriedade de entrada do Canvas. O User Update também oferece suporte aos seguintes recursos de personalização: 
* [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriedades de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Lógica Liquid (incluindo [mensagens de aborto]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Várias atualizações de atribuições ou eventos por objeto

{% alert warning %}
Recomendamos o uso cuidadoso da personalização do conteúdo conectado Liquid nas etapas de atualização do usuário, pois esse tipo de etapa tem um limite de frequência de 200.000 solicitações por minuto. Esse limite de frequência substitui o limite de frequência do Canva.
{% endalert %}

## Criador JSON avançado

Adicione um objeto JSON de atribuição, evento ou compra com até 65.536 caracteres ao criador do JSON. A [inscrição global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) de um usuário e o estado [do grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) também podem ser definidos.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando o criador avançado, também é possível fazer uma prévia e testar se o perfil do usuário está atualizado com as alterações na guia **Preview and test (Prévia e teste** ). Você pode selecionar um usuário aleatório ou procurar um usuário específico. Em seguida, depois de enviar um teste a um usuário, visualize o perfil do usuário usando o link gerado.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerações

Não é necessário incluir dados confidenciais, como sua chave de API, ao usar o criador de JSON, pois isso é fornecido automaticamente pela plataforma. Dessa forma, os campos a seguir são desnecessários e não devem ser usados no criador do JSON:
* ID de usuário externo
* Chave de API
* URL do cluster do Braze
* Campos relacionados a importações de token por push

{% raw %}
### Registre eventos personalizados

Usando o criador JSON, também é possível registrar eventos personalizados. Note que isso requer um registro de data e hora no formato ISO, portanto, é necessário atribuir uma hora e uma data com Liquid no início. Considere este exemplo que registra um evento com uma hora.

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

O próximo exemplo vincula um evento a um app específico usando um evento personalizado com propriedades opcionais e o `app_id`.

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

### Editar o estado da inscrição

No criador do JSON, você também pode editar o estado da inscrição do usuário. Por exemplo, veja a seguir o estado da inscrição de um usuário atualizado para `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Atualizar grupos de inscrições 

Você também pode atualizar os grupos de inscrições usando essa etapa do canva. O exemplo a seguir mostra uma atualização dos grupos de inscrições. Você pode realizar uma ou várias atualizações de grupos de inscrições.

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

