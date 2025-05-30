---
nav_title: "Sobre notificações por push"
article_title: Sobre notificações por push
page_order: 0
page_type: reference
description: "Este artigo de referência apresenta uma visão geral do push, fornece recursos para começar com mensagens push e observa algumas regulamentações."
channel:
  - Push

---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}Sobre notificações por push

> Notificações por push são maravilhosas para chamadas à ação sensíveis ao tempo, assim como para reengajar usuários que não acessam o app há algum tempo. Campanhas de push bem-sucedidas levam o usuário diretamente ao conteúdo e demonstram o valor do seu aplicativo.

Lembre-se de que os usuários precisam dar aceitação ao push para receber suas mensagens, o que significa que é uma boa ideia usar mensagens no app para explicar aos seus clientes por que você deseja enviar notificações por push e como habilitar o push os beneficiará. Este processo é chamado de [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

![Exemplo de mensagens push em produtos Apple.][1]{: height="400px"}  ![Exemplo de mensagens push do Stopwatch na tela inicial do iPhone que diz: Olá! Este é um push do iOS".][2]{: height="400px"}

Para ver mais exemplos de notificações por push, confira nossos [Estudos de Caso][8]].

## Casos de uso potenciais

Notificações por push são uma ótima ferramenta para atrair novos usuários e fazer campanhas de re-engajamento. Veja a seguir alguns exemplos de casos de uso comuns de mensagens push.

| Caso de Uso | Explicação |
| -------- | ----------- |
| Integração inicial | Até que os usuários deem os primeiros passos para usar seu app (como registrar uma conta), seu valor é severamente limitado. Use notificações por push para instar os usuários a completar essas etapas para que possam começar a usar seu app completamente. |
| Primeiras Compras | Depois que os usuários estiverem confortáveis usando seu app, você pode usar notificações por push para ajudá-los a se tornarem compradores dentro do app. |
| Novos Recursos | Notificações por push podem ser eficazes em notificar usuários desengajados sobre novos recursos que podem atraí-los de volta ao seu app. |
| Ofertas Sensíveis ao Tempo | Se você tem uma oferta com tempo limitado, às vezes o push é uma ótima maneira de informar seus usuários sobre isso antes que expire. Essas mensagens geralmente carregam um alto senso de urgência e são ideais para lembrar os usuários que recentemente deixaram de usar seu app.<br><br> Por exemplo, suponha que seu app seja um jogo e você ofereça aos seus usuários um bônus de moeda no jogo se eles mantiverem uma sequência de jogar o jogo diariamente. Alertar um usuário de que a sequência está em perigo de ser quebrada pode ser um push razoável se eles excederem um certo número de dias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais sobre como reengajar usuários inativos, consulte nossa [Vitórias rápidas][23] página sobre o assunto.

## Pré-requisitos para usar push

Antes de poder criar e enviar qualquer mensagem push usando Braze, você precisa trabalhar com seus desenvolvedores para integrar push ao seu site ou app. Consulte instruções detalhadas em nossos guias de integração para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Regulamentos de push de mensagens

Como as mensagens push são um tipo de envio de mensagens intrusivo que vai diretamente para o telefone ou navegador do seu cliente, existem diretrizes para o envio de mensagens push por meio de aplicativos e sites.

### Regulamentações de push móvel para aplicativos

{% alert important %}
Suas mensagens push devem estar dentro das diretrizes da Apple App Store e das políticas da Google Play Store, especificamente no que diz respeito ao uso de mensagens push como anúncios, spam, promoções e mais.
{% endalert %}

|Políticas da App Store da Apple|
|---|
|[3.2.2][9] Inaceitável: (i) Criar uma interface para exibir apps, extensões ou plug-ins de terceiros semelhante à App Store ou como uma coleção de interesse geral.| 
|[4.5.4][7] Notificações por push não devem ser necessárias para o app funcionar e não devem ser usadas para enviar informações pessoais ou confidenciais sensíveis. Notificações por push não devem ser usadas para promoções ou marketing direto, a menos que os clientes tenham optado explicitamente por recebê-las através da linguagem de consentimento exibida na interface do usuário do seu app, e você forneça um método no seu app para que um usuário possa optar por não receber essas mensagens.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Você não pode monetizar recursos integrados fornecidos pelo hardware ou sistema operacional, como notificações por push, câmera ou giroscópio; ou serviços e tecnologias da Apple, como acesso ao Apple Music, armazenamento no iCloud ou APIs do Tempo de Uso.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Política da Google Play Store|
|---|
|[Uso ou Imitação Não Autorizada da Funcionalidade do Sistema][10] Não permitimos aplicativos ou anúncios que imitem ou interfiram na funcionalidade do sistema, como notificações ou avisos. Notificações em nível de sistema podem ser usadas apenas para os recursos integrais de um app, como um app de companhia aérea que notifica os usuários sobre ofertas especiais, ou um jogo que notifica os usuários sobre promoções no jogo.|
{: .reset-td-br-1 role="presentation" }

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
Daqui a [8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
Daqui a [10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
