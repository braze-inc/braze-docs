---
nav_title: "Push para a web"
article_title: Notificações por push na Web
page_order: 8.5
page_type: reference
description: "Esta página de referência aborda brevemente as notificações por push da Web e apresenta os links para as etapas necessárias para criar uma."
platform: Web
channel:
  - push

---

# Web push

> Saiba mais sobre as notificações por push da Web no Braze e encontre recursos para criar suas próprias notificações.

O web push é outra ótima maneira de interagir com os usuários do seu aplicativo Web. Os clientes que visitam seu site em [navegadores compatíveis](#supported-browsers) podem aceitar receber web push de seu aplicativo da Web, independentemente de a página da Web estar ou não carregada.

## Visão geral

As notificações por push da Web fornecem atualizações urgentes e acionáveis que geram conversões rápidas. Com o web push, é possível:

- Envio de mensagens quando dados importantes são alterados, como uma redução de preço
- Leve as pessoas de volta ao seu site com botões simples de chamada para ação
- Personalize seu push com informações sobre produtos e clientes para tornar sua mensagem relevante

O web push funciona da mesma forma que as notificações por push de app funcionam em seu telefone. Para saber mais sobre como criar um web push, consulte [Criação de uma notificação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![web push exemplo com a mesma mensagem push exibida em um laptop e telefone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Casos de uso em potencial

Veja a seguir alguns exemplos de casos de uso comuns de mensagens pela internet.

| Caso de uso | Descrição |
| --- | --- | 
| Teste gratuito | Incentive os novos visitantes do seu site a inscreverem-se para testes gratuitos. Ao atrair os usuários com a chance de experimentar o que o torna especial, você pode aumentar a probabilidade de eles se tornarem clientes pagantes. |
| Download de app | Atraia os usuários da Web para o seu app móvel para ajudá-los a obter ainda mais valor dos seus produtos. Considere a possibilidade de aproveitar a personalização para destacar os benefícios do app com base em seus padrões de engajamento atuais. |
| Descontos e vendas | Aumentar a conscientização do cliente sobre eventos e promoções sensíveis ao tempo. Envie mensagens por vários canais, inclusive web push, para divulgar as promoções da sua marca. |
| Abandono de carrinho | Envie lembretes automáticos aos usuários que não concluíram suas transações para trazê-los de volta ao fluxo de checkout. <br><br>Uma pesquisa realizada pela Braze constatou que o web push é 53% mais eficaz do que o envio de e-mail e 23% mais impactante do que o mobile push para fazer com que os destinatários voltem e concluam uma compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-requisitos para usar o web push

Antes de criar e enviar mensagens push usando o Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu site. Consulte instruções detalhadas em nosso [guia de integração de web push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permissão de push

Qualquer marca pode integrar e usar notificações por push da Web em seu site. As notificações podem alcançar visitantes atuais e anteriores da Web, desde que tenham um navegador aberto. No entanto, os visitantes devem [aceitar receber notificações]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission), assim como no push tradicional de aplicativos móveis.

{% alert tip %}
Considere a possibilidade de usar uma mensagem no navegador para que os usuários aceitem o web push, também conhecido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatíveis

Os navegadores a seguir oferecem suporte a notificações por push da Web. No entanto, as janelas de navegação privada não aceitam web push.

- Chrome (e Chrome para celulares Android)
- Safari
- Firefox (e Firefox para celulares Android)
- Opera
- Edge

Para saber mais sobre os padrões do protocolo push e o suporte do navegador, consulte os recursos de acordo com o seu navegador:

- [Safari (desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (celular)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


