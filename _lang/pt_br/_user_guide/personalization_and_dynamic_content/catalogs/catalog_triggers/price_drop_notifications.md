---
nav_title: Notificações de Queda de Preço
article_title: Notificações de Queda de Preço
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artigo de referência descreve como criar notificações de queda de preço nos catálogos da Braze."
---

# Notificações de queda de preço

> Esta página cobre como funcionam as notificações de queda de preço e como você pode configurá-las e usá-las. 

## 

Quando um usuário aciona um evento personalizado para um item, nós automaticamente os inscreveremos para receber notificações de queda de preço para esse item. Quando o preço do item atender à sua regra de inventário (como uma queda maior que 50%), todos os assinantes serão elegíveis para notificações por meio de uma campanha ou Canva. No entanto, apenas os usuários que optaram por receber notificações receberão notificações. 

## 

Você configurará um evento personalizado para usar como um evento de inscrição, como um evento `product_clicked`. Este evento deve conter uma propriedade do ID do item (IDs dos itens do catálogo).   



- 
- 

 Quando um item tem uma alteração de preço que atende à sua regra de preço, procuraremos todos os seus usuários que estão inscritos nesse item (usuários que fizeram o evento de inscrição) e enviaremos um evento personalizado do Braze que você pode usar para disparar uma campanha ou canva. 



## Configurando notificações de queda de preço

Siga estas etapas para configurar notificações de queda de preço em um catálogo específico.

1. Acessar seu catálogo e selecionar a guia **Configurações**.
2. Selecione a alternância de **Queda de Preço**.
3.  <br><br> ![Gaveta de configurações do catálogo.][2]{: style="max-width:70%;"}

|  |  |
| --- | --- |
|  |  |
|  |  Quando este evento ocorrer, o usuário que realizou o evento será inscrito. |
|  |  Este evento é opcional. Se o usuário não realizar este evento, ele será desinscrito após 90 dias ou quando o evento de queda de preço for acionado, o que ocorrer primeiro. |
|  | A propriedade no evento personalizado acima usada para determinar o item para uma inscrição ou cancelamento de inscrição. Esta propriedade no evento personalizado deve conter um ID de item que existe em um catálogo.  |




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
4\. 

### 

1.  
2. <br>

    -  
    -   Braze notificará os números especificados de clientes em incrementos até que não haja mais clientes para notificar ou até que o preço do item volte a subir. Sua taxa de notificação não pode exceder a notificação de 10.000 usuários por minuto.<br>

2.  Este é o campo do catálogo que será usado para determinar o preço do item. Deve ser um tipo numérico.
3. Defina a **Regra de queda de preço**. Esta é a lógica usada para determinar se uma notificação deve ser enviada. Uma queda de preço pode ser configurada como uma mudança percentual de preço ou quanto o valor do campo de preço mudou.
4. Selecione **Salvar configurações**.

![Configurações do catálogo que mostram o recurso de queda de preço ativado. 

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
