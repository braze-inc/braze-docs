---
nav_title: Notificações de estoque em espera
article_title: Notificações de estoque em espera
page_order: 2
description: "Este artigo de referência descreve como criar notificações de falta de estoque nos catálogos da Braze."
---

# Notificações de estoque em espera

> Use uma combinação de notificações de volta ao estoque por meio de catálogos do Braze e uma tela para notificar os clientes quando um item estiver de volta ao estoque. Sempre que um cliente realiza um evento personalizado selecionado, ele pode se inscrever automaticamente para ser notificado quando o item for reabastecido.<br><br>Esta página aborda como funcionam as notificações de falta de estoque e como você pode configurá-las e usá-las.

Quando um usuário dispara um evento personalizado para um item, nós o inscrevemos automaticamente para receber notificações de falta de estoque desse item. Quando a quantidade de estoque do item atender à sua regra de estoque (por exemplo, um estoque maior que 100), todos os assinantes serão elegíveis para notificações por meio de uma campanha ou do canva. No entanto, apenas os usuários que optaram por receber notificações receberão notificações. 

## Como funcionam as notificações de estoque em espera

Você configurará um evento personalizado para usar como um evento de inscrição, como um evento `product_clicked`. Este evento deve conter uma propriedade do ID do item (IDs dos itens do catálogo). Sugerimos que você inclua um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de quantidade de estoque, que deve ser um tipo de dado numérico.

Quando um item tiver uma quantidade de estoque que atenda à sua regra de estoque, procuraremos todos os seus usuários que estão inscritos nesse item (usuários que fizeram o evento de gatilho) e enviaremos um evento personalizado da Braze que poderá ser usado para disparar uma campanha ou canva.

As propriedades do evento são enviadas junto com seu usuário, para que você possa fazer um modelo com os detalhes do item na campanha ou canva que envia!

## Configurando notificações de estoque em espera

Siga estas etapas para configurar notificações de falta de estoque em um catálogo específico.

1. Acessar seu catálogo e selecionar a guia **Configurações**.
2. Selecione a opção **Voltar ao estoque**.
3. Se as configurações globais de estoque em espera não tiverem sido configuradas, será solicitado que você configure os eventos e propriedades personalizados que serão usados para disparar notificações de estoque em espera:
    <br> ![Gaveta de configurações do catálogo.][2]{: style="max-width:70%;"}
    - **Catálogo de fallback** Esse é o catálogo que será usado para a inscrição de back-in-stock, se não houver nenhuma propriedade `catalog_name` presente no evento personalizado.
    - O **evento personalizado para inscrições** é o evento personalizado do Braze que será usado para inscrever um usuário para receber notificações de falta de estoque. Quando esse evento ocorrer, o usuário que o realizou será inscrito.
    - O **evento personalizado para cancelamento de inscrição** é o evento personalizado do Braze que será usado para cancelar a inscrição de um usuário nas notificações de estoque em espera. Esse evento é opcional. Se o usuário não realizar esse evento, sua inscrição será cancelada depois de 90 dias ou quando o evento de estoque esgotado for disparado, o que ocorrer primeiro.
    - **A propriedade do evento Item ID** é a propriedade do evento personalizado acima que será usada para determinar o item para uma inscrição ou cancelamento de inscrição em estoque. Essa propriedade no evento personalizado deve conter um ID de item, que está presente em um catálogo. O evento personalizado também deve conter uma propriedade `catalog_name`, para especificar em qual catálogo esse item está.
    
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
Os disparadores de queda de preço e de volta ao estoque usam o mesmo evento para inscrever o usuário na notificação, portanto, é possível usar a matriz `type` para definir notificações de queda de preço e de volta ao estoque no mesmo evento.
{% endalert %}

{: start="4"}
4\. Selecione **Salvar** e continue para a página de **Configurações** do catálogo.
5\. Defina sua regra de notificação. Existem duas opções:
    - **Notify all subscribed users (Notificar todos os usuários inscritos)** notifica todos os clientes que estão aguardando quando o item estiver novamente em estoque.
    - **Definir limites de notificação** notifica um número específico de clientes por período de notificação configurado. O Braze notificará o número especificado de clientes em incrementos até que não haja mais clientes a serem notificados ou até que o item fique fora de estoque. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.
6\. Defina o **campo Inventário no catálogo**. Esse campo do catálogo será usado para determinar se o item está fora de estoque. O campo deve ser do tipo numérico.
7\. Selecione **Salvar configurações**.

![Configurações do catálogo que mostram o recurso de estoque em espera ativado. As regras de notificação são para notificar mil usuários a cada dez minutos.][1]

{% alert important %}
As regras de notificação nestas configurações não substituem as configurações de notificação do canva, como horário de silêncio.
{% endalert %}

## Uso de notificações de falta de estoque em um canva

Depois de configurar o recurso de reserva em um catálogo, siga estas etapas para usá-lo com o canva.

1. Configure uma canva baseada em ação.
2. Selecione **Voltar ao estoque** como o disparador.
3. Selecione o nome do catálogo com as notificações de falta de estoque.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) sua canva como de costume.

Agora, seus clientes podem ser notificados quando um item estiver novamente em estoque.

### Usando Liquid

Para obter detalhes sobre o item do catálogo que está de volta ao estoque, use o modelo `canvas_entry_properties` Liquid tag para acessar `item_id`. 

O uso de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que voltou ao estoque. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do estoque do item antes da atualização e {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do estoque após a atualização.

Use esta Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} no topo da sua mensagem, depois use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

## Considerações

- Os usuários só se inscrevem por 90 dias. Se o item não estiver novamente em estoque em 90 dias, o usuário terá sua inscrição cancelada.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, o Braze notificará 100.000 em 10 minutos.
- A Braze processará, no máximo, 10 atualizações de itens em um minuto. Se você atualizar 11 itens em um minuto, apenas os 10 primeiros poderão disparar uma notificação de falta de estoque.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
