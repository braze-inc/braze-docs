---
nav_title: "Anúncios que clicam no WhatsApp"
article_title: Anúncios que clicam no WhatsApp
page_order: 1
description: "Este artigo de referência fornece um guia passo a passo para configurar e usar o Ads That Click no WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Anúncios que clicam no WhatsApp

> Esta página fornece um guia passo a passo para configurar e usar o Ads That Click para WhatsApp, para que você e sua equipe possam elevar seu programa do WhatsApp.

Os anúncios que clicam no WhatsApp são uma maneira eficiente de atrair clientes novos e existentes a partir de anúncios do Meta no Facebook, Instagram ou outras plataformas. Use esses anúncios para promover seus produtos e serviços e, ao mesmo tempo, conscientizar os usuários sobre sua presença no WhatsApp.

\![Um anúncio do Facebook da Calorie Rocket que anuncia entrega gratuita e a respectiva conversa do WhatsApp que ocorre quando um usuário seleciona o botão do anúncio.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configuração de anúncios que clicam no WhatsApp

1. No Meta Ads Manager, crie um anúncio no Facebook, no Instagram ou em outras plataformas seguindo o guia passo a passo [Como criar anúncios que clicam no WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **Não** configure respostas automáticas; em vez disso, você configurará respostas no Braze.

Gerenciador de anúncios com um compositor para criar um anúncio de engajamento.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Ao configurar a mensagem pré-preenchida, que será enviada pelo usuário para sua conta do WhatsApp Business, inclua uma palavra ou frase específica que você usará para acionar uma resposta específica para o anúncio em questão. Neste exemplo, um aplicativo de entrega de comida está usando "entrega gratuita" porque isso é promovido em seu anúncio. 

\![Compositor de modelo do Gerenciador de Anúncios com uma mensagem pré-preenchida de "Quero entrega gratuita".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Deixe claro na descrição do anúncio que, ao clicar nele, você iniciará uma conversa com sua marca usando frases como "Converse agora no WhatsApp".
{% endalert %}

{: start="2"}
2\. No Braze, configure um Canvas baseado em ação em que a opção baseada em ação seja **Enviar uma mensagem de entrada do WhatsApp** e o corpo da mensagem seja “YOUR_TRIGGER_WORD”.. Neste exemplo, um aplicativo de entrega de comida está usando "entrega gratuita".

Programação de entrada para um Braze Canvas baseado em ação, com o evento de disparo "Enviar uma mensagem de entrada do WhatsApp" e um corpo de mensagem que corresponde ao regex de "entrega gratuita".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\. Configure uma mensagem de resposta no Canvas que seja enviada imediatamente após o cliente entrar no Canvas (por exemplo, sem atraso). Embora clicar no anúncio tecnicamente constitua uma aceitação, recomendamos configurar sua mensagem de resposta para perguntar ao usuário se ele gostaria de receber futuras mensagens de marketing suas no WhatsApp. 

{% alert tip %}
Configure sua mensagem de resposta com respostas rápidas (como "Sim" ou "Não, obrigado") para que os usuários possam indicar rapidamente se desejam participar.
{% endalert %}

Não se esqueça de fornecer também qualquer código de desconto, oferta ou outras informações prometidas no anúncio!

Compositor de mensagens do WhatsApp com botões de resposta "Sim" e "Não, obrigado".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

Etapa do Canvas com um grupo "Opting in" com um evento de acionamento "Enviou o WhatsApp de entrada para o grupo de assinatura" e uma palavra de acionamento "YES".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\. Faça opt-in de usuários atualizando o status de assinatura dos perfis de usuário com um dos seguintes métodos de atualização:
    \- Crie um webhook Braze-to-Braze que atualize o status da assinatura por meio da API REST.  
    \- Use o editor JSON avançado para atualizar o perfil do usuário com o modelo para [atualizar o status de assinatura de um usuário em um WhatsApp Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process).

Etapa do Canvas de atualização do usuário que usa o editor JSON avançado para atualizar o perfil do usuário.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

Canvas mostrando o fluxo de trabalho para enviar anúncios que clicam para o WhatsApp, incluindo três caminhos de ação: Optar por participar, optar por não participar e todos os outros.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Considerações

As conversas iniciadas a partir de um anúncio que clica no WhatsApp são gratuitas se as seguintes condições forem atendidas:

- Se um usuário enviar uma mensagem para você por meio de um [ponto de entrada gratuito](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), como um anúncio que clica no WhatsApp, uma [janela de atendimento ao cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) de 24 horas será aberta, na qual você poderá enviar qualquer tipo de mensagem a esse usuário.
- Se você responder dentro da janela de atendimento ao cliente (dentro de 24 horas), um ponto de entrada gratuito será aberto por 72 horas, e todas as mensagens dentro da janela de 72 horas serão gratuitas.
- As mensagens de resposta são gratuitas.