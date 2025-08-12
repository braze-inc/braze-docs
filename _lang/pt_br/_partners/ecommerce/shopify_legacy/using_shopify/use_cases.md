---
nav_title: Casos de uso
article_title: "Casos de Uso do Shopify no Braze"
description: "Este artigo de referência descreve casos de uso comuns básicos e avançados do Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# Casos de uso

> Interessado em ver como você pode aproveitar sua integração com o Shopify para criar envio de mensagens oportuno e eficaz para seus usuários? Consulte as seguintes seções sobre casos de uso comuns [iniciante](#beginner) e [avançado](#advanced) para saber mais!

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Iniciante

Estes são alguns casos de uso simples, mas eficazes, que você pode criar logo após configurar o Shopify. Nenhum trabalho adicional é necessário. 

### Campanhas

Esses casos de uso transacionais permitem que você alerte seus usuários quando houver uma atualização no pedido deles no Shopify.

{% tabs local %}
{% tab Reembolso %}
**Evento de reembolso do Shopify** - `shopify_created_refund`

Os usuários receberam um reembolso, parcial ou completo. Esta campanha informa ao usuário que seu pedido foi reembolsado com sucesso.

![Campanha baseada em ações que inscreve usuários que realizam o evento personalizado "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Exemplo de envio de mensagens**

![E-mail com o texto "Seu pedido foi reembolsado. Lamentamos que você não tenha gostado do produto. Enviamos seu reembolso com sucesso. Aguarde de 3 a 5 dias úteis para os fundos aparecerem no seu extrato" e o botão "Ver conta".]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancelamento %}
**Evento de cancelamento do Shopify** - `shopify_cancelled_order`

Os usuários podiam cancelar seus pedidos antes do processamento. Esta campanha informa ao usuário que sua compra foi cancelada com sucesso. 

![Campanha baseada em ação que insere usuários que realizam o evento personalizado "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Exemplo de envio de mensagens**

![E-mail com o texto "Seu pedido foi cancelado. Sentiremos sua falta! Cancelamos com sucesso o seu pedido. Aguarde de 3 a 5 dias úteis para os fundos aparecerem no seu extrato" e o botão "Ver conta".]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Pedido processado %}
**Shopify cumpriu o evento** - `shopify_fulfilled_order`

Todos os itens de linha no pedido de um usuário foram processados. Esta campanha informa ao usuário que todo o seu pedido foi atendido.

![Campanha baseada em ação que inscreve usuários que realizam o evento personalizado "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Exemplo de envio de mensagens**

![Mensagem de texto com o texto "Seu pedido foi atendido!" Todos os itens no seu carrinho foram entregues! Por favor, acesse sua conta e confirme o recebimento. Pontos extras por deixar feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Pedido parcialmente atendido %}
**Evento parcialmente atendido do Shopify** - `shopify_partially_fulfilled_order`

Alguns itens de linha no pedido de um usuário foram processados. Esta campanha informa aos usuários que parte de seu pedido foi atendida.

![Campanha baseada em ação que inscreve usuários que realizam o evento personalizado "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Exemplo de envio de mensagens**

![SMS com o texto "Seu pedido foi parcialmente processado!" Entregamos alguns dos itens do seu pedido e o restante está a caminho! Enviaremos outro alerta quando a entrega estiver totalmente concluída."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Pedido pago %}
**Evento de pedido pago da Shopify** – `shopify_paid_order`

O usuário paga pelo pedido, e o status do pedido muda para pago. Esta campanha informa ao usuário que o pagamento com cartão de crédito foi capturado ou que o pedido foi marcado como pago se houve um pagamento manual.

![Campanha baseada em ações que inscreve usuários que realizam o evento personalizado "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Exemplo de envio de mensagens**

![e-mail com o texto "Recebemos seu pagamento!" Woohoo seu pedido foi pago! Por favor, aguarde 1-2 dias úteis para que possamos processar o pagamento e preparar seus itens. O envio será feito logo depois!" e o botão "Ver conta".]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvas

{% tabs local %}
{% tab Canva de checkout abandonado %}

**Canva de checkout abandonado**

Os usuários estão abandonando o fluxo de checkout e não conseguem concluir as transações antes de sair. Esta canva permite que você envie lembretes automáticos para usuários que não finalizaram suas transações, trazendo-os de volta ao fluxo de checkout.

Evento de entrada baseado em ação: `shopify_abandoned_checkout`<br>
Evento de exceção: `shopify_created_order` ou Compra

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Canva pós-compra %}

**Canva pós-compra**

Os usuários fizeram uma compra bem-sucedida e agora você quer saber como eles gostaram da compra. Este canva permite enviar mensagens de acompanhamento para seu usuário para coletar feedback. 

Evento de entrada baseado em ação: `shopify_created_order` ou Compra

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Avançado

Depois de se familiarizar mais com a plataforma, você pode configurar casos de uso mais complexos.

### Campanhas

{% tabs local %}
{% tab Recomendações do usuário %}
**Recomendações do usuário**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

O usuário clicou ou visualizou um item, mas não o comprou. Esta campanha envia uma mensagem de acompanhamento ao usuário com os mesmos itens ou itens semelhantes (recomendados pelo Conteúdo Conectado) para incentivar o usuário a comprar um deles.

Evento de entrada baseado em ação: `shopify_product_clicked` ou `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Evento de exceção: `shopify_created_order` ou Compra<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canva

{% tabs local %}
{% tab Canva de recuperação por reembolso %}

**Canva de recuperação por reembolso**

Os usuários receberam um reembolso, parcial ou completo. Esta canva envia mensagens de acompanhamento para fazer com que o usuário faça sua compra novamente.

Evento de entrada baseado em ação: `shopify_created_refund`<br>
Evento de exceção: `shopify_created_order` ou Compra

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Canva de cancelamento para recuperação %}

**Canva de cancelamento para recuperação**

Os usuários podiam cancelar seus pedidos antes do processamento. Esta canva envia mensagens de acompanhamento para fazer com que o usuário faça sua compra novamente.

Evento de entrada baseado em ação: `shopify_cancelled_order`<br>
Evento de exceção: `shopify_created_order` ou Compra

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}