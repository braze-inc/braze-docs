---
nav_title: Notificações de Queda de Preço
article_title: Notificações de Queda de Preço
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artigo de referência descreve como criar notificações de queda de preço nos catálogos da Braze."
---

# Notificações de queda de preço

> Usando uma combinação de notificações de queda de preço através de catálogos Braze e uma canva, você pode notificar os clientes quando o preço de um item diminuiu. Sempre que um cliente realiza um evento personalizado selecionado, ele pode ser automaticamente inscrito para ser notificado quando o preço do item for reduzido.

{% alert important %}
Notificações de queda de preço para catálogos estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar deste acesso antecipado.
{% endalert %}

Quando um usuário aciona um evento personalizado para um item, nós automaticamente os inscreveremos para receber notificações de queda de preço para esse item. Quando o preço do item atender à sua regra de inventário (como uma queda maior que 50%), todos os assinantes serão elegíveis para notificações por meio de uma campanha ou Canva. No entanto, apenas os usuários que optaram por receber notificações receberão notificações. 

## Como funcionam as notificações de queda de preço

Você configurará um evento personalizado para usar como um evento de inscrição, como um evento `product_clicked`. Este evento deve conter uma propriedade do ID do item (IDs dos itens do catálogo). Sugerimos que você inclua um nome de catálogo, mas isso não é obrigatório. Você também fornecerá o nome de um campo de preço, que deve ser do tipo de dado numérico. Quando um evento personalizado selecionado é realizado por um usuário e tem uma propriedade `type` que inclui `price_drop`, ele pode ser usado para criar uma inscrição de queda de preço para um usuário e um item de catálogo para o qual ocorreu.

Quando um item tem uma alteração de preço que atende à sua regra de preço, procuraremos todos os seus usuários que estão inscritos nesse item (usuários que fizeram o evento de inscrição) e enviaremos um evento personalizado do Braze que você pode usar para disparar uma campanha ou canva.

As propriedades do evento são enviadas junto com seu usuário, para que você possa fazer um modelo com os detalhes do item na campanha ou canva que envia!

## Configurando notificações de queda de preço

Siga estas etapas para configurar notificações de queda de preço em um catálogo específico.

1. Acessar seu catálogo e selecionar a guia **Configurações**.<br>
2. Selecione a alternância de **Queda de Preço**.<br>
3. Se as configurações do catálogo global não tiverem sido configuradas, você será solicitado a configurar os eventos e propriedades personalizados que serão usados para disparar notificações:
    <br> ![Gaveta de configurações do catálogo.][2]{: style="max-width:70%;"}
    - **Evento personalizado para inscrição:** O evento personalizado do Braze usado para inscrever um usuário para notificações de catálogo. Quando este evento ocorrer, o usuário que realizou o evento será inscrito.
    - **Evento personalizado para cancelamento de inscrição:** O evento personalizado do Braze usado para cancelar a inscrição de um usuário das notificações.
    - **ID do item propriedade do evento:** A propriedade no evento personalizado acima usada para determinar o item para uma inscrição ou cancelamento de inscrição. Esta propriedade no evento personalizado deve conter um ID de item que existe em um catálogo. O evento personalizado deve conter uma propriedade `catalog_name` para especificar em qual catálogo este item está.
    - **Catálogo de fallback:** O catálogo usado para a inscrição se não houver uma propriedade `catalog_name` no evento personalizado.
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
                    "type": ["price_drop"]
                }
            }
        ]
    }
    ```
{% alert note %}
Os disparos de reposição de estoque e de queda de preço usam o mesmo evento para inscrever o usuário na notificação. Crie uma notificação de queda de preço definindo `type` como `price_drop`. Não é possível definir uma notificação de queda de preço e de volta ao estoque.
{% endalert %}

{: start="4"}
4\. Selecione **Salvar** e continue para a página de **Configurações** do catálogo.
5\. Defina sua regra de notificação. Existem duas opções:
    - **Notify all subscribed users (Notificar todos os usuários inscritos** ) notifica todos os clientes que estão esperando quando o preço do item cai.
    - **Notificar um determinado número de usuários por um determinado número de minutos** notifica um número específico de clientes por período de notificação configurado. Braze notificará os números especificados de clientes em incrementos até que não haja mais clientes para notificar ou até que o preço do item volte a subir. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.
6\. Defina o campo **Preço no catálogo**. Este é o campo do catálogo que será usado para determinar o preço do item. Deve ser um tipo numérico.<br>
7\. Defina a **regra de queda de preço**. Esta é a lógica usada para determinar se uma notificação deve ser enviada. Uma queda de preço pode ser configurada como uma mudança percentual de preço ou quanto o valor do campo de preço mudou.<br>
8\. Selecione **Salvar configurações**.

![Configurações do catálogo que mostram o recurso de queda de preço ativado. A regra de queda de preço é uma mudança de três por cento do preço original.][1]{:style="max-width:60%;"}

{% alert important %}
As regras de notificação nestas configurações não substituem as configurações de notificação do canva, como horário de silêncio.
{% endalert %}

## Usando notificações de queda de preço na canva

Depois de configurar as notificações de queda de preço em um catálogo, siga estas etapas para usar essas notificações em uma canva.

1. Configure uma canva baseada em ação.
2. Selecione **Executar Evento de Queda de Preço** como o disparar.
3. Selecione o nome do catálogo com as notificações de queda de preço.
4. Continue [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) sua canva como de costume.

Agora, seus clientes serão notificados quando o preço de um item cair.

### Usando Liquid

Para modelo em detalhes sobre o item do catálogo que teve uma queda de preço, você pode usar a `canvas_entry_properties` Liquid tag para acessar o `item_id`. 

Usar {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} retornará o ID do item que teve uma queda de preço. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} retornará o valor do item antes da atualização, e {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} retornará o novo valor do item após a atualização. 

Use esta Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} no topo da sua mensagem, depois use {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acessar dados sobre esse item ao longo da mensagem.

## Considerações

- Os usuários estão inscritos por 90 dias. Se um item não baixar de preço em 90 dias, o usuário é removido da inscrição.
- Ao usar a regra de notificação **Notificar todos os usuários inscritos**, a Braze notificará 100.000 usuários em 10 minutos.
- Braze processará até 10 atualizações de itens por minuto. Isso significa que se você atualizar 11 itens em um minuto, apenas os primeiros 10 itens podem disparar uma notificação de queda de preço.

[1]: {% image_buster /assets/img/price_drop_notifications.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
