---
nav_title: Notificações de queda de preço
article_title: Notificações de Queda de Preço
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artigo de referência descreve como criar notificações de queda de preço nos catálogos da Braze."
---

# Notificações de queda de preço

> Esta página aborda como funcionam as notificações de queda de preço e como você pode configurá-las e usá-las. Com uma combinação de notificações de queda de preço por meio dos catálogos da Braze e um Canvas, você pode notificar os clientes quando o preço de um item diminuir.

## Como funciona

Quando um usuário aciona um evento personalizado para um item, nós automaticamente o inscrevemos para receber notificações de queda de preço para esse item. Quando o preço do item atender à sua regra de inventário (como uma queda maior que 50%), todos os inscritos serão elegíveis para notificações por meio de uma campanha ou Canvas. No entanto, apenas os usuários que optaram por receber notificações receberão as notificações. 

## Configurando um evento personalizado para notificações de queda de preço

Você configurará um evento personalizado para usar como evento de inscrição, como um evento `product_clicked`. Esse evento deve conter uma propriedade do ID do item (IDs dos itens do catálogo). Recomendamos incluir um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de preço, que deve ser um tipo de dado numérico. 

Você pode criar uma inscrição de queda de preço para um usuário e um item de catálogo quando o seguinte ocorrer:

- Um evento personalizado selecionado é realizado por um usuário
- O evento personalizado tem uma propriedade `type` que inclui `price_drop` (`type` deve ser um array)

Para definir notificações de queda de preço e de volta ao estoque no mesmo evento, você pode usar a propriedade `type`, que deve ser um array. Quando um item tem uma alteração de preço que atende à sua regra de preço, procuraremos todos os seus usuários inscritos nesse item (usuários que realizaram o evento de inscrição) e enviaremos um evento personalizado da Braze que você pode usar para disparar uma campanha ou Canvas. 

As propriedades do evento são enviadas junto com o usuário, para que você possa incluir os detalhes do item na campanha ou Canvas que faz o envio.

## Configurando notificações de queda de preço

Siga estas etapas para configurar notificações de queda de preço em um catálogo específico.

1. Acesse seu catálogo e selecione a guia **Configurações**.
2. Selecione a alternância de **Queda de Preço**.
3. Se as configurações globais do catálogo não tiverem sido definidas, você será solicitado a configurar os eventos personalizados e propriedades que serão usados para disparar notificações. <br><br> ![Gaveta de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Campo | Descrição |
| --- | --- |
| **Catálogo de fallback** | O catálogo usado para a inscrição se não houver uma propriedade `catalog_name` no evento personalizado. |
| **Evento personalizado para inscrição** | O evento personalizado usado para inscrever um usuário nas notificações de catálogo. Quando esse evento ocorrer, o usuário que o realizou será inscrito. |
| **Evento personalizado para cancelamento de inscrição** | O evento personalizado usado para cancelar a inscrição de um usuário nas notificações. Esse evento é opcional. Se o usuário não realizar esse evento, ele será desinscrito após 90 dias ou quando o evento de queda de preço for acionado, o que ocorrer primeiro. |
| **Propriedade de evento do ID do item** | A propriedade no evento personalizado acima usada para determinar o item para uma inscrição ou cancelamento de inscrição. Essa propriedade no evento personalizado deve conter um ID de item que existe em um catálogo. O evento personalizado deve conter uma propriedade `catalog_name` para especificar em qual catálogo esse item está. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Aqui está um exemplo de evento personalizado:

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
                "type": ["price_drop", "back_in_stock"]
            }
        }
    ]
}
```

{: start="4"}
4. Selecione **Salvar** e continue para a próxima seção para configurar as regras de notificação.

### Configurando regras de notificação

1. Acesse a página de **Configurações** do seu catálogo. 
2. Em **Regras de notificação**, selecione entre as seguintes opções:<br>

    - **Notificar todos os usuários inscritos:** Notifica todos os clientes que estão aguardando quando o preço do item cair.
    - **Definir limites de notificação:** Notifica um número especificado de clientes de acordo com o período de notificação configurado. A Braze notificará o número especificado de clientes em incrementos até que não haja mais clientes para notificar ou até que o preço do item volte a subir. Sua taxa de notificação não pode exceder 10.000 usuários por minuto.<br>

2. Defina o **Campo de preço no catálogo**. Este é o campo do catálogo que será usado para determinar o preço do item. Deve ser um tipo numérico.
3. Defina a **Regra de queda de preço**. Esta é a lógica usada para determinar se uma notificação deve ser enviada. Uma queda de preço pode ser configurada como uma mudança percentual de preço ou pela mudança no valor do campo de preço.
4. Selecione **Salvar configurações**.

![Configurações do catálogo que mostram o recurso de queda de preço ativado. A regra de queda de preço é uma mudança de três por cento em relação ao preço original.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
As regras de notificação nessas configurações não substituem as configurações de notificação do Canvas, como o horário de silêncio.
{% endalert %}

## Usando notificações de queda de preço em um Canvas

Após configurar as notificações de queda de preço em um catálogo, siga estas etapas para usar essas notificações em um Canvas.

1. Configure um Canvas baseado em ação.
2. Selecione **Executar Evento de Queda de Preço** como o gatilho.
3. Selecione o nome do catálogo com as notificações de queda de preço.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) seu Canvas como de costume.

Agora, seus clientes serão notificados quando o preço de um item cair.

### Usando Liquid

Para incluir detalhes sobre o item do catálogo que teve uma queda de preço, você pode usar a Liquid tag `context` para acessar o `item_id`. 

Usar {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que teve a queda de preço. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do preço do item antes da atualização, e {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do preço após a atualização. 

Use a Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} no topo da sua mensagem e depois use {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Considerações

- Os usuários ficam inscritos por 90 dias. Se um item não tiver queda de preço em 90 dias, o usuário é removido da inscrição.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, a Braze notificará 100.000 usuários em 10 minutos.
- A Braze suporta até 50.000 itens atualizados diariamente que são elegíveis para disparar notificações de queda de preço. Você pode ter até 100 milhões de inscrições ativas em um determinado momento, onde cada inscrição representa um perfil de usuário inscrito para acompanhar um item do catálogo.