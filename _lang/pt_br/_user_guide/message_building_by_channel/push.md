---
nav_title: Empurrar
article_title: Empurrar
page_order: 4
layout: dev_guide
guide_top_header: "Empurrar"
guide_top_text: "As notificações push são uma maneira comprovada de enviar chamadas à ação sensíveis ao tempo por meio de dispositivos móveis ou da Web, além de reengajar usuários que não acessam o aplicativo há algum tempo. Eles levam o usuário diretamente ao conteúdo e demonstram o valor do seu aplicativo. As notificações push são úteis para direcionar os usuários a um local específico, mas você deve usá-las com sabedoria. <br><br> Leia qualquer um dos artigos a seguir ou confira nosso [Push Braze Learning course] (https://learning.braze.com/messaging-channels-push) para saber para quem você pode enviar um push, como enviá-lo e quais recursos avançados de push o Braze oferece. Para ver exemplos de notificações por push, confira nossas [histórias de clientes] (https://www.braze.com/customers)."
description: "Essa página de destino abriga mensagens push. Aqui, você pode encontrar artigos sobre tipos de push, registro de push, ativação de push, primers de push, relatórios de push e muito mais."
channel:
  - push

guide_featured_title: "Artigos populares"
guide_featured_list:
- name: Tipos de empurradores
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Registro por push
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Ativação e assinatura de push
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Criação de uma mensagem push
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Opções avançadas
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Primers de empurrar
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Relatórios
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Opções do Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Opções do iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web Push
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Práticas recomendadas
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locais em mensagens
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: Mensagens de erro comuns do Push
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Solução de problemas
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Perguntas frequentes
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso

Exemplo de mensagem push em produtos Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"} Exemplo de mensagem push do Stopwatch em uma tela inicial do iPhone que diz: "Olá! Este é um iOS Push".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

As notificações push são uma ótima ferramenta para atrair novos usuários e fazer campanhas de reengajamento. Veja a seguir alguns exemplos de casos de uso comuns de mensagens push.

| Caso de uso | Explicação |
| -------- | ----------- |
| Integração inicial | Até que os usuários tomem as medidas iniciais para usar seu aplicativo (como registrar uma conta), o valor deles é severamente limitado. Use notificações push para incentivar os usuários a concluírem essas etapas para que possam começar a usar seu aplicativo por completo. |
| Primeiras compras | Depois que os usuários se sentirem à vontade para usar o aplicativo, você poderá usar as notificações por push para ajudar a convertê-los em compradores no aplicativo. |
| Novos recursos | As notificações por push podem ser eficazes para notificar os usuários não engajados sobre novos recursos que podem atraí-los de volta ao seu aplicativo. |
| Ofertas sensíveis ao tempo | Se você tiver uma oferta em andamento, às vezes o push é uma ótima maneira de informar os usuários sobre ela antes que expire. Essas mensagens geralmente têm um alto senso de urgência e são ideais para lembrar os usuários que perderam o aplicativo recentemente.<br><br> Por exemplo, suponha que seu aplicativo seja um jogo e que você ofereça aos usuários um bônus em moeda do jogo se eles mantiverem uma sequência de jogos diários. Alertar um usuário de que essa sequência corre o risco de ser quebrada pode ser um incentivo razoável se ele tiver ultrapassado um determinado número de dias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter mais informações sobre o reengajamento de usuários inativos, consulte nossa página [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sobre o assunto.

## Pré-requisitos para usar o push

Antes de criar e enviar qualquer mensagem push usando o Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu site ou aplicativo. Para obter etapas detalhadas, consulte nossos guias de integração para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Escorvamento por pressão

Lembre-se de que os usuários precisam optar pelo push para receber suas mensagens, o que significa que é uma boa ideia usar mensagens no aplicativo para explicar aos seus clientes por que você deseja enviar notificações push e como a ativação do push os beneficiará. Esse processo é chamado de [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Regulamentos de mensagens push

Como as mensagens push são um tipo de mensagem intrusiva que vai diretamente para o telefone ou navegador do cliente, há diretrizes para o envio de mensagens push por meio de aplicativos e sites.

### Regulamentos de push móvel para aplicativos

{% alert important %}
Suas mensagens push devem estar dentro das diretrizes das políticas da Apple App Store e da Play Store do Google, especificamente em relação ao uso de mensagens push como anúncios, spam, promoções e muito mais.
{% endalert %}

|Políticas da Apple App Store|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceitável: (i) Criar uma interface para exibir aplicativos, extensões ou plug-ins de terceiros semelhantes aos da App Store ou como uma coleção de interesse geral.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) As notificações push não devem ser necessárias para o funcionamento do aplicativo e não devem ser usadas para enviar informações pessoais sensíveis ou confidenciais. As notificações por push não devem ser usadas para fins de promoções ou marketing direto, a menos que os clientes tenham optado explicitamente por recebê-las por meio de uma linguagem de consentimento exibida na interface do usuário do seu aplicativo e que você forneça um método no seu aplicativo para que o usuário opte por não receber essas mensagens.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Você não poderá monetizar recursos incorporados fornecidos pelo hardware ou sistema operacional, tais como Notificações Push, a câmera ou o giroscópio; ou serviços e tecnologias da Apple, tais como acesso ao Apple Music, armazenamento do iCloud ou APIs de tempo de tela.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Política da Google Play Store|
|---|
|[Uso não autorizado ou imitação da funcionalidade do sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Não permitimos aplicativos ou anúncios que imitem ou interfiram na funcionalidade do sistema, como notificações ou avisos. As notificações no nível do sistema só podem ser usadas para os recursos integrais de um aplicativo, como um aplicativo de companhia aérea que notifica os usuários sobre ofertas especiais ou um jogo que notifica os usuários sobre promoções no jogo.|
{: .reset-td-br-1 role="presentation" }
