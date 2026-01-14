---
nav_title: Solicitação de classificação no aplicativo para iOS
article_title: Solicitação de classificação no aplicativo para iOS
page_order: 6
description: "Este artigo descreve as abordagens e as implicações do uso do Braze para solicitar que os usuários avaliem seu aplicativo."
channel:
  - in-app messages

---

# Solicitação de classificação no aplicativo para iOS

> Este artigo descreve as abordagens e as implicações do uso do Braze para solicitar que os usuários avaliem seu aplicativo. Para obter dicas sobre como fazer uma campanha eficaz de classificação de aplicativos, confira [O que fazer e o que não fazer nas classificações de aplicativos de clientes](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

A Apple oferece um prompt nativo, introduzido no iOS 10.3, que permite que os usuários classifiquem os aplicativos dentro do próprio aplicativo. Se você quiser solicitar classificações de aplicativos de usuários usando uma mensagem in-app no iOS, deverá usar o prompt nativo, pois a Apple não permite prompts de avaliação personalizados (consulte [Diretrizes de avaliação da App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), seção 5.6.1).

De acordo com as diretrizes da Apple, os prompts de avaliação de aplicativos podem ser exibidos a um usuário até três vezes por ano, portanto, qualquer campanha de avaliação de aplicativos deve aproveitar a [limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Os usuários também podem optar por não ver os avisos de avaliação do aplicativo completamente nas configurações do aplicativo. Para saber mais sobre as classificações da App Store, consulte o artigo da Apple sobre [classificações, resenhas e respostas](https://developer.apple.com/app-store/ratings-and-reviews/).

## Usar o Braze para solicitar aos usuários avaliações de aplicativos

Embora a Apple exija que você use o prompt nativo, você ainda pode aproveitar as campanhas do Braze para pedir aos usuários que avaliem seu aplicativo no momento certo. Há duas abordagens principais que você pode adotar.

### Abordagem 1: Links diretos para a App Store

Com essa abordagem, você deseja incentivar os usuários a visitar a App Store para adicionar uma avaliação. Para isso, crie uma campanha de mensagem in-app com [links diretos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) para a App Store.

\![Duas telas de celular lado a lado. A primeira é uma mensagem no aplicativo que solicita ao usuário que avalie o aplicativo na App Store. A segunda é a página da iOS App Store para esse aplicativo.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Abordagem 2: Escorvamento suave

Se não quiser que os usuários saiam do seu aplicativo, você pode primeiramente dar aos usuários uma mensagem separada no aplicativo. Priming é uma forma de pedir permissão aos usuários antes de enviar a eles o prompt de avaliação nativo da App Store. Para fazer isso, crie uma campanha de mensagem in-app e adicione um deep link personalizado que chame o método `requestReview` quando clicado. 

Para obter etapas detalhadas, consulte o [prompt de revisão da Custom App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

\![Duas mensagens no aplicativo lado a lado. A primeira prepara o usuário para avaliar o aplicativo, perguntando se ele tem um momento para avaliar o aplicativo. A segunda é a mensagem de avaliação nativa da App Store do iOS, que exibe uma escala de cinco estrelas que o usuário pode selecionar para avaliar o aplicativo.]({% image_buster /assets/img_archive/prime_app_review.png %})

Os usuários enviarão uma avaliação por meio do prompt de avaliação nativo da App Store e poderão escrever e enviar uma avaliação sem sair do aplicativo.

### Considerações

Como alternativa ao soft primer, você também pode exibir o prompt de classificação do aplicativo iOS diretamente, sem nenhuma mensagem do Braze soft primer exibida antes. A vantagem disso é que, se o usuário optar por não receber os avisos de avaliação do aplicativo, não haverá a experiência de usuário abaixo do ideal de tentar avaliar o aplicativo, mas não aparecer nenhum aviso para fazê-lo.

{% alert important %}
Não crie mensagens HTML personalizadas no aplicativo que imitem um prompt de classificação de aplicativo iOS nativo, pois isso viola as diretrizes da Apple.
{% endalert %}

