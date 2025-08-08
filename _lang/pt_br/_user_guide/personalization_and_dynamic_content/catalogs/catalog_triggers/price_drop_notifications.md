---
nav_title: Notificações de Queda de Preço
article_title: Notificações de Queda de Preço
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artigo de referência descreve como criar notificações de queda de preço nos catálogos da Braze."
---

# Notificações de queda de preço

> Esta página cobre como funcionam as notificações de queda de preço e como você pode configurá-las e usá-las. Com uma combinação de notificações de queda de preço através de catálogos Braze e um canva, você pode notificar os clientes quando o preço de um item diminuir.

## Como funciona?

Quando um usuário aciona um evento personalizado para um item, nós automaticamente os inscreveremos para receber notificações de queda de preço para esse item. Quando o preço do item atender à sua regra de inventário (como uma queda maior que 50%), todos os assinantes serão elegíveis para notificações por meio de uma campanha ou Canva. No entanto, apenas os usuários que optaram por receber notificações receberão notificações. 

## Definindo um evento personalizado para notificações de queda de preço

Você configurará um evento personalizado para usar como um evento de inscrição, como um evento `product_clicked`. Este evento deve conter uma propriedade do ID do item (IDs dos itens do catálogo). Recomendamos incluir um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de preço, que deve ser um tipo de dado numérico. 

Você pode criar uma inscrição de queda de preço para um usuário e um item de catálogo quando o seguinte ocorrer:

- Um evento personalizado selecionado é realizado por um usuário
- O evento personalizado tem uma `type` propriedade que inclui `price_drop` (`type` deve ser um array)

Para definir notificações de queda de preço e de volta ao estoque no mesmo evento, você pode usar a propriedade `type`, que deve ser um array. Quando um item tem uma alteração de preço que atende à sua regra de preço, procuraremos todos os seus usuários que estão inscritos nesse item (usuários que fizeram o evento de inscrição) e enviaremos um evento personalizado do Braze que você pode usar para disparar uma campanha ou canva. 

As propriedades do evento são enviadas junto com seu usuário, para que você possa incluir os detalhes do item na campanha ou no canva que envia.

## Configurando notificações de queda de preço

Siga estas etapas para configurar notificações de queda de preço em um catálogo específico.

1. Acessar seu catálogo e selecionar a guia **Configurações**.
2. Selecione a alternância de **Queda de Preço**.
3. Se as configurações do catálogo global não foram configuradas, você será solicitado a configurar os eventos personalizados e propriedades que serão usados para disparar notificações. <br><br> ![Painel de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Campo | Descrição |
| --- | --- |
| **Catálogo de fallback** | O catálogo usado para a inscrição se não houver uma propriedade `catalog_name` no evento personalizado. |
| **Evento personalizado para inscrição** | O evento personalizado usado para inscrever um usuário para notificações de catálogo. Quando este evento ocorrer, o usuário que realizou o evento será inscrito. |
| **Evento personalizado para cancelamento de inscrição** | O evento personalizado usado para cancelar a inscrição de um usuário das notificações. Este evento é opcional. Se o usuário não realizar este evento, ele será desinscrito após 90 dias ou quando o evento de queda de preço for acionado, o que ocorrer primeiro. |
| **Propriedade de evento do ID do item** | A propriedade no evento personalizado acima usada para determinar o item para uma inscrição ou cancelamento de inscrição. Esta propriedade no evento personalizado deve conter um ID de item que existe em um catálogo. O evento personalizado deve conter uma propriedade `catalog_name` para especificar em qual catálogo este item está. |
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
4\. Selecione **Salvar** e continue para a próxima seção para configurar as regras de notificação.

### Configurando regras de notificação

1. Acessar a página de **Configurações** do seu catálogo. 
2. Para **Regras de notificação**, selecione entre as seguintes opções:<br>

    - **Notificar todos os usuários inscritos:** Notificar todos os clientes que estão esperando quando o preço do item cair.
    - **Definir limites de notificação:** Notifique um número especificado de clientes por seu período de notificação configurado. Braze notificará os números especificados de clientes em incrementos até que não haja mais clientes para notificar ou até que o preço do item volte a subir. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.<br>

2. Defina o campo **Preço no catálogo**. Este é o campo do catálogo que será usado para determinar o preço do item. Deve ser um tipo numérico.
3. Defina a **Regra de queda de preço**. Esta é a lógica usada para determinar se uma notificação deve ser enviada. Uma queda de preço pode ser configurada como uma mudança percentual de preço ou pela mudança no valor do campo de preço.
4. Selecione **Salvar configurações**.

![Configurações do catálogo que mostram o recurso de queda de preço ativado. A regra de queda de preço é uma mudança de três por cento em relação ao preço original.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
As regras de notificação nestas configurações não substituem as configurações de notificação do canva, como horário de silêncio.
{% endalert %}

## Usando notificações de queda de preço em um canva

Após configurar as notificações de queda de preço em um catálogo, siga estas etapas para usar essas notificações para um canva.

1. Configure uma canva baseada em ação.
2. Selecione **Executar Evento de Queda de Preço** como o disparar.
3. Selecione o nome do catálogo com as notificações de queda de preço.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) sua canva como de costume.

Agora, seus clientes serão notificados quando o preço de um item cair.

### Usando Liquid

Para modelo em detalhes sobre o item do catálogo que teve uma queda de preço, você pode usar a `canvas_entry_properties` Liquid tag para acessar o `item_id`. 

Usar {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que teve a queda de preço. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do preço do item antes da atualização, e {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do preço após a atualização. 

Use esta Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} no topo da sua mensagem, depois use {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

## Considerações

- Os usuários estão inscritos por 90 dias. Se um item não baixar de preço em 90 dias, o usuário é removido da inscrição.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, a Braze notificará 100.000 usuários em 10 minutos.
- Braze processará 10 solicitações para atualizar itens do catálogo por minuto. Os pontos finais de atualização permitem 50 atualizações de itens por solicitação, suportando até 500 atualizações de itens por minuto que podem disparar notificações de volta em estoque.

