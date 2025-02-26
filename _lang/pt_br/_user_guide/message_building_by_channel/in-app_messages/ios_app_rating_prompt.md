---
nav_title: Solicitação de classificação no app para iOS
article_title: Solicitação de classificação no app para iOS
page_order: 6
description: "Este artigo descreve as abordagens e as implicações do uso da Braze para pedir aos usuários que avaliem seu app."
channel:
  - in-app messages

---

# Solicitação de classificação no app para iOS

> Este artigo descreve as abordagens e as implicações do uso da Braze para pedir aos usuários que avaliem seu app. Para obter dicas sobre como fazer uma campanha eficaz de classificação de aplicativos, consulte [O que fazer e o que não fazer nas classificações de aplicativos para clientes](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

A Apple oferece um prompt nativo, introduzido com o iOS 10.3, que permite que os usuários avaliem os apps dentro do próprio aplicativo. Se quiser solicitar classificações de app de usuários usando uma mensagem no app no iOS, você deve usar o prompt nativo, pois a Apple não permite prompts de avaliação personalizados (consulte [Diretrizes de avaliação da App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), seção 5.6.1).

De acordo com as diretrizes da Apple, os avisos de revisão de aplicativos podem ser exibidos a um usuário até três vezes por ano, portanto, qualquer campanha de revisão de aplicativos deve aproveitar o [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Os usuários também podem optar por não ver os pedidos de aceitação de aplicativos totalmente nas configurações do aplicativo. Para obter mais informações sobre as classificações da App Store, consulte o artigo da Apple sobre [classificações, resenhas e respostas](https://developer.apple.com/app-store/ratings-and-reviews/).

## Usar o Braze para pedir avaliações de app aos usuários

Embora a Apple exija o uso do prompt nativo, você ainda pode aproveitar as campanhas do Braze para pedir aos usuários que avaliem seu app no momento certo. Há duas abordagens principais que você pode adotar.

### Abordagem 1: Deep linking para a App Store

Com essa abordagem, você deseja incentivar os usuários a visitar a App Store para adicionar uma avaliação. Para fazer isso, crie uma campanha de mensagens no app que [faça deep linking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) para a App Store.

![Duas telas de celular lado a lado. A primeira é uma mensagem no app que pede ao usuário para avaliar o aplicativo na App Store. A segunda é a página da App Store do iOS para esse app.][1]

### Abordagem 2: Escorvamento suave

Se não quiser que os usuários saiam do seu app, você pode primeiramente dar aos usuários uma mensagem no app separada. Priming é uma forma de pedir permissão aos usuários antes de enviar a eles o prompt de revisão nativo da App Store. Para fazer isso, crie uma campanha de mensagens no app e adicione um deep link personalizado que chame o método `requestReview` quando clicado. 

Para obter informações detalhadas, consulte o [prompt de revisão da Custom App Store]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_app_store_review_prompt/).

![Duas mensagens no app lado a lado. A primeira prepara o usuário para avaliar o app, perguntando se ele tem um momento para avaliar o aplicativo. A segunda é a mensagem nativa de avaliação da App Store do iOS, que exibe uma escala de cinco estrelas que o usuário pode selecionar para avaliar o app.][2]

Os usuários enviarão uma classificação por meio do prompt de avaliação nativo da App Store e poderão escrever e enviar uma avaliação sem sair do app.

### Considerações

Como alternativa ao soft priming, você também pode exibir o prompt de classificação do app iOS diretamente, sem nenhuma mensagem no app Braze soft primer exibida antes. A vantagem disso é que, se o usuário tiver optado por não receber prompts de avaliação no app, não haverá a experiência de usuário abaixo do ideal de tentar avaliar o aplicativo, mas não aparecer nenhum pedido para fazê-lo.

{% alert important %}
Não crie mensagens no app em HTML personalizado que imitem um prompt de classificação de aplicativo iOS nativo, pois isso viola as diretrizes da Apple.
{% endalert %}

[1]: {% image_buster /assets/img_archive/app_store_app_review.png %}
[2]: {% image_buster /assets/img_archive/prime_app_review.png %}