---
nav_title: Notificações de volta ao estoque
article_title: Configurando notificações de volta ao estoque
page_order: 2
description: "Aprenda como configurar notificações de volta ao estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque."
---

# Notificações de volta ao estoque

> Aprenda como configurar notificações de volta ao estoque usando seu catálogo e eventos personalizados, para que você possa inscrever automaticamente os clientes para receber notificações quando um item estiver de volta ao estoque. Tenha em mente que isso se aplica apenas a usuários que já optaram por receber notificações.

## Como funciona

Você pode configurar um evento personalizado para usar como um evento de inscrição, como um evento `product_clicked`. Este evento deve conter uma propriedade do ID do item (IDs de itens do catálogo). Sugerimos que você inclua um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de quantidade de inventário, que deve ser um tipo de dado numérico. 

Observe que o estoque de um item do catálogo deve estar em zero para que um usuário possa se inscrever com sucesso. Quando um item tem uma quantidade de inventário maior que zero, a Braze procurará todos os usuários inscritos naquele item e enviará um evento personalizado que você pode usar para acionar uma campanha ou Canvas.

As propriedades do evento são enviadas junto com seu usuário, para que você possa incluir os detalhes do item na campanha ou Canvas que envia.

## Configurando notificações de volta ao estoque

Siga estas etapas para configurar notificações de volta ao estoque em um catálogo específico.

1. Vá para seu catálogo e selecione a aba **Configurações**.
2. Selecione o botão **Voltar ao estoque**.
3. Se as configurações globais de volta ao estoque não foram configuradas, você será solicitado a configurar os eventos personalizados e propriedades que serão usados para acionar notificações de volta ao estoque:
    <br> \![Painel de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Catálogo de fallback** Este é o catálogo que será usado para a inscrição de volta ao estoque, se não houver a propriedade `catalog_name` presente no evento personalizado.
    - **Evento personalizado para inscrições** é o evento personalizado da Braze que será usado para inscrever um usuário para notificações de volta ao estoque. Quando este evento ocorrer, o usuário que realizou o evento será inscrito.
    - **Evento personalizado para cancelar a inscrição** é o evento personalizado do Braze que será usado para cancelar a inscrição de um usuário nas notificações de volta ao estoque. Este evento é opcional. Se o usuário não realizar este evento, ele será cancelado após 90 dias ou quando o evento de volta ao estoque for acionado, o que ocorrer primeiro.
    - **Propriedade do evento ID do item** é a propriedade do evento personalizado acima que será usada para determinar o item para uma assinatura ou cancelamento de volta ao estoque. Esta propriedade no evento personalizado deve conter um ID de item (`id`) que está presente em um catálogo. O ID do item deve ser enviado como uma string para que corresponda ao tipo de dado `id` armazenado no catálogo de destino. O evento personalizado também deve conter uma propriedade `catalog_name` para especificar em qual catálogo este item está.
    
    - Um exemplo de evento personalizado seria
    ```json
    {
        "events": [
            {
                "external_id": "<external_id>",
                "name": "subscription",
                "time": "2024-04-15T19:22:28Z",
                "properties": {
                    "id": "shirt-xl",
                    "catalog_name": "on_sale_products",
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
Os gatilhos de volta ao estoque e de queda de preço usam o mesmo evento para inscrever o usuário na notificação, então você pode usar a propriedade `type` para definir tanto as notificações de queda de preço quanto as de volta ao estoque no mesmo evento. Observe que a propriedade `type` deve ser um array.
{% endalert %}

{: start="4"}
4\. Selecione **Salvar** e continue para a página **Configurações** do catálogo.
5\. Defina sua regra de notificação. Existem duas opções:
    - **Notificar todos os usuários inscritos** notifica todos os clientes que estão esperando quando o item estiver de volta em estoque.
    - **Definir limites de notificação** notifica um número especificado de clientes de acordo com seu período de notificação configurado. O Braze notificará os números especificados de clientes em incrementos até que não haja mais clientes para notificar ou até que o item fique fora de estoque. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.
6\. Defina o **campo de inventário no catálogo**. Este campo de catálogo será usado para determinar se o item está fora de estoque. O campo deve ser do tipo numérico.
7\. Selecione **Salvar configurações**.

\![Configurações do catálogo que mostram o recurso de volta ao estoque ativado. As regras de notificação são para notificar mil usuários a cada dez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
As regras de notificação nessas configurações não substituem as configurações de notificação do Canvas, como Horas Silenciosas.
{% endalert %}

## Usando notificações de volta ao estoque em um Canvas

Após configurar o recurso de volta ao estoque em um catálogo, siga estas etapas para usar com o Canvas.

1. Configure um Canvas baseado em ações.
2. Selecione **Voltar ao estoque** como o gatilho.
3. Selecione o nome do catálogo com as notificações de volta ao estoque.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) seu Canvas como faria.

Agora, seus clientes podem ser notificados quando um item estiver de volta em estoque.

### Usando Liquid

Para modelar detalhes sobre o item do catálogo que está de volta em estoque, você pode usar a tag `canvas_entry_properties` Liquid para acessar o `item_id`. 

Usar {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que voltou ao estoque. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do inventário do item antes da atualização, e {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do inventário após a atualização.

Use esta tag Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} no topo da sua mensagem, depois use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

## Considerações

- Os usuários estão inscritos por apenas 90 dias. Se o item não voltar ao estoque em 90 dias, o usuário será desinscrito.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, a Braze notificará 100.000 em 10 minutos.
- A Braze processará no máximo 10 atualizações de itens em um minuto. Se você atualizar 11 itens em um minuto, apenas os primeiros 10 podem acionar uma notificação de volta ao estoque.

