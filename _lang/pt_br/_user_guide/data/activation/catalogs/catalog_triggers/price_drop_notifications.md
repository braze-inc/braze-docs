---
nav_title: Notificações de queda de preço
article_title: Notificações de queda de preço
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artigo de referência descreve como criar notificações de queda de preço em catálogos Braze."
---

# Notificações de queda de preço

> Esta página aborda como funcionam as notificações de queda de preço e como você pode configurá-las e usá-las. Com uma combinação de notificações de queda de preço por meio dos catálogos Braze e de um Canvas, você pode notificar os clientes quando o preço de um item diminuir.

## Como funciona

Quando um usuário aciona um evento personalizado para um item, nós o inscreveremos automaticamente para receber notificações de queda de preço desse item. Quando o preço do item atender à sua regra de inventário (como uma queda maior que 50%), todos os assinantes estarão qualificados para receber notificações por meio de uma campanha ou do Canvas. No entanto, somente os usuários que optaram pelas notificações receberão notificações. 

## Definição de um evento personalizado para notificações de queda de preço

Você configurará um evento personalizado para usar como um evento de assinatura, como um evento `product_clicked`. Esse evento deve conter uma propriedade do ID do item (IDs de itens do catálogo). Recomendamos incluir um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de preço, que deve ser um tipo de dados numérico. 

Você pode criar uma assinatura de queda de preço para um usuário e um item de catálogo quando ocorrer o seguinte:

- Um evento personalizado selecionado é realizado por um usuário
- O evento personalizado tem uma propriedade `type` que inclui `price_drop` (`type` deve ser uma matriz)

Para definir notificações de queda de preço e de volta ao estoque no mesmo evento, você pode usar a propriedade `type`, que deve ser uma matriz. Quando um item tiver uma alteração de preço que atenda à sua regra de preço, procuraremos todos os seus usuários que estão inscritos nesse item (usuários que fizeram o evento de inscrição) e enviaremos um evento personalizado do Braze que você poderá usar para acionar uma campanha ou um Canvas. 

As propriedades do evento são enviadas junto com o usuário, de modo que você pode modelar os detalhes do item na campanha ou no Canvas que envia.

## Configuração de notificações de queda de preço

Siga estas etapas para configurar notificações de queda de preço em um catálogo específico.

1. Acesse seu catálogo e selecione a guia **Settings (Configurações** ).
2. Selecione a opção **Queda de preço**.
3. Se as configurações do catálogo global não tiverem sido definidas, você será solicitado a configurar os eventos e as propriedades personalizados que serão usados para acionar as notificações. <br><br> Gaveta de configurações do catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Campo | Descrição |
| --- | --- |
| **Catálogo de fallback** | O catálogo usado para a assinatura se não houver uma propriedade `catalog_name` no evento personalizado. |
| **Evento personalizado para assinatura** | O evento personalizado usado para inscrever um usuário em notificações de catálogo. Quando esse evento ocorrer, o usuário que o realizou será inscrito. |
| **Evento personalizado para cancelar a assinatura** | O evento personalizado usado para cancelar a inscrição de um usuário nas notificações. Esse evento é opcional. Se o usuário não realizar esse evento, sua inscrição será cancelada após 90 dias ou quando o evento de queda de preço for acionado, o que ocorrer primeiro. |
| **Propriedade do evento ID do item** | A propriedade no evento personalizado acima usado para determinar o item para uma assinatura ou cancelamento de assinatura. Essa propriedade no evento personalizado deve conter um ID de item que exista em um catálogo. O evento personalizado deve conter uma propriedade `catalog_name` para especificar em qual catálogo esse item está. |
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
4\. Selecione **Salvar** e continue na próxima seção para configurar as regras de notificação.

### Configuração de regras de notificação

1. Acesse a página de **Configurações** do seu catálogo. 
2. Para **regras de notificação**, selecione uma das seguintes opções:<br>

    - **Notificar todos os usuários inscritos:** Notifique todos os clientes que estão esperando quando o preço do item cair.
    - **Definir limites de notificação:** Notifique um número específico de clientes por período de notificação configurado. O Braze notificará o número especificado de clientes em incrementos até que não haja mais clientes para notificar ou até que o preço do item volte a subir. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.<br>

2. Defina o **campo Preço no catálogo**. Esse é o campo do catálogo que será usado para determinar o preço do item. Deve ser um tipo de número.
3. Defina a **regra de queda de preço**. Essa é a lógica usada para determinar se uma notificação deve ser enviada. Uma queda de preço pode ser configurada como uma alteração de preço percentual ou pela alteração no valor do campo de preço.
4. Selecione **Salvar configurações**.

Configurações do catálogo que mostram o recurso de queda de preço ativado. A regra de queda de preço é uma alteração de três por cento do preço original.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
As regras de notificação nessas configurações não substituem as configurações de notificação do Canvas, como Quiet Hours.
{% endalert %}

## Uso de notificações de queda de preço em um Canvas

Depois de configurar as notificações de queda de preço em um catálogo, siga estas etapas para usar essas notificações em um Canvas.

1. Configure um Canvas baseado em ações.
2. Selecione **Perform Price Drop Event** como o acionador.
3. Selecione o nome do catálogo com as notificações de queda de preço.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) o Canvas como de costume.

Agora, seus clientes serão notificados quando o preço de um item cair.

### Usando líquido

Para obter detalhes sobre o item do catálogo que caiu de preço, você pode usar a tag `canvas_entry_properties` Liquid para acessar o site `item_id`. 

O uso de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item cujo preço caiu. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do preço do item antes da atualização e {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do preço após a atualização. 

Use essa tag do Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} na parte superior da mensagem e, em seguida, use {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acessar dados sobre esse item em toda a mensagem.

## Considerações

- Os usuários são inscritos por 90 dias. Se o preço de um item não cair em 90 dias, o usuário será removido da assinatura.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, o Braze notificará 100.000 usuários em 10 minutos.
- O Braze processará 10 solicitações de atualização de itens do catálogo por minuto. Os endpoints de atualização permitem 50 atualizações de itens por solicitação, suportando até 500 atualizações de itens por minuto que podem acionar notificações de falta de estoque

