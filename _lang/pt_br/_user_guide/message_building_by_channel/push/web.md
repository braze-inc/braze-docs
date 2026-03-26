---
nav_title: "Web push"
article_title: Notificações por push na Web
page_order: 8.5
page_type: reference
description: "Esta página de referência aborda brevemente as notificações por push da Web e apresenta os links para as etapas necessárias para criar uma."
platform: Web
channel:
  - push

---

# Push para a web

> Saiba mais sobre as notificações por push da Web na Braze e encontre recursos para criar suas próprias notificações.

O push para a web é outra ótima maneira de interagir com os usuários do seu aplicativo Web. Os clientes que visitam seu site em [navegadores compatíveis](#supported-browsers) podem aceitar receber push para a web do seu aplicativo da Web, independentemente de a página da Web estar ou não carregada.

## Visão geral

As notificações por push da Web fornecem atualizações urgentes e acionáveis que geram conversões rápidas. Com o push para a web, é possível:

- Disparar mensagens quando dados importantes são alterados, como uma redução de preço
- Levar as pessoas de volta ao seu site com botões de chamada para ação claros
- Personalizar seu push com informações sobre produtos e clientes para tornar sua mensagem relevante

O push para a web funciona da mesma forma que as notificações por push de app funcionam em seu telefone. Para saber mais sobre como compor um push para a web, confira [Criar uma notificação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Exemplo de push para a web com a mesma mensagem push exibida em um laptop e em um telefone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Casos de uso em potencial

Veja a seguir alguns exemplos de casos de uso comuns de mensagens por push para a web.

| Caso de uso | Descrição |
| --- | --- | 
| Teste gratuito | Incentive os novos visitantes do seu site a se inscreverem para testes gratuitos. Ao atrair os usuários com a chance de experimentar o que torna você especial, você pode aumentar a probabilidade de eles se tornarem clientes pagantes. |
| Download de app | Atraia os usuários da Web para o seu app móvel para ajudá-los a obter ainda mais valor dos seus produtos. Considere a possibilidade de aproveitar a personalização para destacar os benefícios do app com base em seus padrões de engajamento atuais. |
| Descontos e vendas | Aumente a conscientização do cliente sobre eventos e promoções sensíveis ao tempo. Envie mensagens por vários canais, inclusive push para a web, para divulgar as promoções da sua marca. |
| Abandono de carrinho | Envie lembretes automáticos aos usuários que não concluíram suas transações para trazê-los de volta ao fluxo de checkout. <br><br>Uma pesquisa realizada pela Braze constatou que o push para a web é 53% mais eficaz do que o e-mail e 23% mais impactante do que o push móvel para fazer com que os destinatários voltem e concluam uma compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-requisitos para usar o push para a web

Antes de criar e enviar mensagens push usando a Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu site. Para instruções detalhadas, consulte nosso [guia de integração de push para a web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permissão de push

Qualquer marca pode integrar e usar notificações por push da Web em seu site. As notificações podem alcançar visitantes atuais e anteriores da Web, desde que tenham um navegador aberto. No entanto, os visitantes devem [aceitar receber notificações]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission), assim como no push tradicional de aplicativos móveis.

{% alert tip %}
Considere usar uma mensagem no navegador para preparar os usuários para aceitar o push para a web, também conhecido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatíveis

Os navegadores a seguir oferecem suporte a notificações por push da Web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (e Chrome para celulares Android)
- Safari (versão 16 ou mais recente)
- Firefox (e Firefox para celulares Android)
- Opera
- Edge

Para saber mais sobre os padrões do protocolo push e o suporte do navegador, consulte os recursos de acordo com o seu navegador:

- [Safari (desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (celular)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)