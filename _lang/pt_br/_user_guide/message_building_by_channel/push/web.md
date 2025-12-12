---
nav_title: "Empurrar pela Web"
article_title: Notificações Web Push
page_order: 8.5
page_type: reference
description: "Esta página de referência aborda brevemente as notificações por push da Web e apresenta os links para as etapas necessárias para criar uma."
platform: Web
channel:
  - push

---

# Empurrar pela Web

> Saiba mais sobre as notificações push da Web no Braze e encontre recursos para criar suas próprias notificações.

O Web push é outra ótima maneira de interagir com os usuários do seu aplicativo Web. Os clientes que visitam seu site a partir de [navegadores compatíveis](#supported-browsers) podem optar por receber web push de seu aplicativo da Web, independentemente de a página da Web estar ou não carregada.

## Visão geral

As notificações push da Web fornecem atualizações urgentes e acionáveis que geram conversões rápidas. Com o Web Push, você pode:

- Acionar mensagens quando dados importantes forem alterados, como uma redução de preço
- Leve as pessoas de volta ao seu site com botões simples de chamada para ação
- Personalize seu push com informações sobre produtos e clientes para tornar sua mensagem relevante

O Web Push funciona da mesma forma que as notificações push de aplicativos funcionam em seu telefone. Para obter mais informações sobre a composição de um push da Web, consulte [Criação de uma notificação push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

Exemplo de push na Web com a mesma mensagem push exibida em um laptop e em um telefone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Casos de uso em potencial

Veja a seguir alguns exemplos de casos de uso comuns de mensagens Web Push.

| Caso de uso | Descrição |
| --- | --- | 
| Teste gratuito | Incentive os novos visitantes do seu site a se inscreverem em avaliações gratuitas. Ao atrair os usuários com a chance de experimentar o que o torna especial, você pode aumentar a probabilidade de eles se tornarem clientes pagantes. |
| Download do aplicativo | Atraia os usuários da Web para o seu aplicativo móvel para ajudá-los a obter ainda mais valor dos seus produtos. Considere aproveitar a personalização para destacar os benefícios do aplicativo com base em seus padrões de engajamento atuais. |
| Descontos e vendas | Aumentar a conscientização do cliente sobre eventos e promoções sensíveis ao tempo. Envie mensagens por vários canais, inclusive push na Web, para aumentar a conscientização sobre as promoções de sua marca. |
| Abandono de carrinho | Envie lembretes automáticos aos usuários que não concluíram suas transações para trazê-los de volta ao fluxo de checkout. <br><br>Uma pesquisa realizada pela Braze constatou que o web push é 53% mais eficaz do que o e-mail e 23% mais impactante do que o push móvel para fazer com que os destinatários voltem e concluam uma compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-requisitos para usar o web push

Antes de criar e enviar qualquer mensagem push usando o Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu site. Para obter etapas detalhadas, consulte nosso [guia de integração de Web Push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permissão de envio

Qualquer marca pode integrar e usar notificações push da Web em seu site. As notificações podem alcançar visitantes da Web atuais e anteriores, desde que tenham um navegador da Web aberto, mas os visitantes devem [optar por receber notificações - exatamente]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)como no push tradicional de aplicativos móveis.

{% alert tip %}
Considere a possibilidade de usar uma mensagem no navegador para que os usuários optem pelo web push, também conhecido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatíveis

Os navegadores a seguir são compatíveis com as notificações Web Push. No entanto, as janelas de navegação privada não suportam atualmente o web push.

- Chrome (e Chrome para celular Android)
- Safári
- Firefox (e Firefox para celulares Android)
- Ópera
- Borda

Para obter mais informações sobre os padrões do protocolo push e o suporte do navegador, você pode consultar os recursos com base no seu navegador:

- [Safari (desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (celular)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


