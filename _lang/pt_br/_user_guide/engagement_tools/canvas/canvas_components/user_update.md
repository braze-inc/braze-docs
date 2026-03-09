---
nav_title: Atualização do usuário
article_title: Atualização de usuário 
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Este artigo de referência aborda o componente atualização do usuário e como usá-lo em seus canvas."
tool: Canvas
---

# Atualização de usuário 

> O componente de Atualização do Usuário permite que você atualize os atributos, eventos e compras de um usuário em um editor JSON, portanto, não há necessidade de incluir informações sensíveis, como chaves de API.

## Como este componente funciona

![Uma etapa de Atualização do Usuário chamada "Atualizar fidelidade" que atualiza um atributo "É Membro Premium" para "verdadeiro".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Ao usar este componente em seu Canva, as atualizações não contam para o seu `/users/track` limite de frequência de solicitações por minuto. Em vez disso, essas atualizações são agrupadas para que o Braze possa processá-las com mais eficiência do que um webhook de Braze para Braze. Observe que este componente não registra [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) quando usado para atualizar pontos de dados não faturáveis (como grupos de inscrição).

Depois que os usuários entram na etapa de Atualização do Usuário e ela conclui o processamento, eles avançam para a próxima etapa. Isso significa que qualquer envio de mensagens subsequente que dependa dessas atualizações de usuário está atualizado quando a próxima etapa é executada.

## Criação de uma atualização de usuário

Arraste e solte o componente da barra lateral, ou selecione o botão <i class="fas fa-plus-circle"></i> de mais na parte inferior da variante ou etapa e selecione **Atualização do Usuário**. 

Existem três opções que permitem que você atualize informações de perfil de usuário existentes, adicione novas informações ou remova informações do perfil do usuário. Combinadas, as etapas de atualização de usuários em um espaço de trabalho podem atualizar até 200.000 perfis de usuários por minuto.

{% alert tip %}
Também é possível testar as alterações feitas com esse componente pesquisando um usuário e aplicando a alteração a ele. Isso atualizará o usuário.
{% endalert %}

## Atualização de atributos personalizados

Para atualizar ou remover um atributo personalizado, selecione um nome de atributo da sua lista de atributos e insira o valor.

![Etapa de Atualização do Usuário que atualiza os dois atributos "Membro de Fidelidade" e "Programa de Fidelidade" para "verdadeiro".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Remoção de atributos personalizados

Para remover um atributo personalizado, selecione o nome do atributo usando o menu suspenso. Você pode mudar para o [editor JSON avançado](#advanced-json-editor) para editar ainda mais. 

![Etapa de Atualização do Usuário que remove um atributo "Membro de Fidelidade".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valores crescentes e decrescentes

A etapa de Atualização do Usuário pode aumentar ou diminuir o valor de um atributo. Selecione a atribuição, selecione **Increment By (Aumentar por** ) ou **Decrement By (Diminuir por)** e digite um número. 

#### Rastreamento do progresso semanal

Ao incrementar um atributo personalizado que rastreia um evento, é possível rastrear o número de aulas que um usuário teve em uma semana. Usando esse componente, a contagem de classes pode ser redefinida no início da semana e começar o rastreamento novamente. 

![Etapa de Atualização do Usuário que incrementa o atributo "class_count" em um.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Atualização de um vetor de objetos

Um [array de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) é um atributo personalizado rico em dados armazenado no perfil de um usuário. Você pode usá-lo para criar um histórico das interações do usuário com sua marca e para criar segmentos com base em um campo calculado, como histórico de compras ou valor total do tempo de vida.

Usando a opção **Editor JSON Avançado**, você pode inserir JSON para adicionar itens a ou remover itens deste array de objetos.

#### Caso de uso: Atualização da lista de desejos de um usuário

Acompanhe a lista de desejos de um usuário para que você possa segmentar ou personalizar com base em seus itens salvos.

1. Crie um atributo personalizado que seja um array de objetos, por exemplo `wishlist`. Cada objeto pode incluir campos como `product_id`, `product_name` e `added_at`.
2. Na etapa de Atualização do Usuário, selecione **Editor JSON Avançado**. Em seguida, na seção **Compor**, use a operação `$add` para adicionar um item ou a operação `$remove` para remover um item por valor.

O seguinte é um exemplo de adicionar um item à lista de desejos:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Para remover um item, use `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` com a mesma estrutura de objeto para que o Braze possa corresponder e removê-lo.

#### Caso de uso: Cálculo do total do carrinho de compras

Rastreie quando um usuário tem itens em seu carrinho de compras, quando adiciona novos itens ou remove itens e qual é o valor total do carrinho de compras. 

1. Crie um array personalizado de objetos chamado `shopping_cart`. O exemplo a seguir mostra a aparência desse atributo. Cada item tem um `product_id` único que possui dados adicionais em seu próprio array aninhado de objetos, incluindo `price`.

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
3\. Crie um Canva que tenha como alvo usuários que realizam este evento personalizado. Agora, quando um usuário adiciona um item ao carrinho, esse Canva é disparado. Em seguida, é possível direcionar o envio de mensagens diretamente para esse usuário, oferecendo códigos de cupom quando ele atingir um determinado gasto, abandonar o carrinho por um determinado período de tempo ou qualquer outra coisa que se alinhe ao seu caso de uso. 

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
         "product_id": ["1001", "1002"],
         "gift": true,
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

![Etapa de Atualização do Usuário que atualiza o atributo "most_recent_cart_item" com um ID de item.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

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

## Editor JSON Avançado

Adicione um atributo, evento ou objeto JSON de compra de até 65.536 caracteres ao editor JSON. A [inscrição global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) de um usuário e o estado [do grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) também podem ser definidos.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Usando o editor JSON, você também pode prévia e testar se o perfil do usuário é atualizado com suas alterações na guia **Prévia e teste**. Você pode selecionar um usuário aleatório ou procurar um usuário específico. Em seguida, depois de enviar um teste a um usuário, visualize o perfil do usuário usando o link gerado.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considerações

Você não precisa incluir dados sensíveis como sua chave de API ao usar o editor JSON, pois isso é fornecido automaticamente pela plataforma. Os seguintes campos não devem ser incluídos no editor JSON:
* ID de usuário externo
* Chave de API
* URL do cluster do Braze
* Campos relacionados a importações de token por push

{% alert important %}
Propriedades do Canva (como as tags Liquid `canvas_id`, `canvas_name` e `canvas_variant_name`) não são suportadas nas etapas de Atualização do Usuário.
{% endalert %}

{% raw %}
### Registre eventos personalizados

Usando o editor JSON, você também pode registrar eventos personalizados. Observe que isso requer um timestamp em formato ISO, portanto, é necessário atribuir um horário e data com Liquid no início. Considere este exemplo que registra um evento com uma hora.

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

Dentro do editor JSON, você também pode editar o estado de assinatura de um usuário. Por exemplo, veja a seguir o estado da inscrição de um usuário atualizado para `opted_in`. 

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

Você também pode atualizar os grupos de inscrições usando essa etapa do canva. O seguinte exemplo mostra como atualizar um ou mais grupos de assinatura.

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

