---
nav_title: Entendendo as instalações do usuário
article_title: Entendendo as instalações do usuário 
page_order: 7
page_type: reference
description: "Este artigo de referência descreve as instalações de usuários (rastreamento de atribuição de instalação) e as diferentes maneiras de aplicar essas informações em sua campanha."
tool:
  - Campaigns
  - Segments
---

# Entendendo as instalações do usuário

> O rastreamento de atribuição de instalação é uma ótima maneira de melhorar o relacionamento inicial com o usuário. Saber como, onde e, ainda mais importante, por que um usuário instala seu aplicativo permite que você entenda melhor quem é seu usuário e como deve apresentá-lo ao seu app. 

Embora a Braze não forneça rastreamento de atribuição de instalação, podemos nos integrar a [serviços]({{site.baseurl}}/partners/message_orchestration/) como Branch e AppsFlyer para fornecer dados de instalação sem problemas.

## Segmentar seus usuários

Depois que o usuário instala o app, você pode começar a segmentá-lo com base nos seguintes [filtros de atribuição de instalação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution). Em instância do app, os usuários que vieram de um anúncio relacionado a ofertas de férias na praia poderiam ser adicionados a um segmento "Amantes da praia". Da mesma forma, um app de música poderia segmentar os usuários com base no gênero de música exibido no anúncio que levou à instalação.

## Práticas recomendadas

### Integração personalizada

Agora que você tem mais informações sobre o usuário, pode personalizar o processo de integração dele. Isso pode ser tão simples quanto alterar as imagens em suas mensagens para que se ajustem às preferências do usuário ou tão complexo quanto criar uma integração de usuário exclusiva para cada anúncio que possa levar a uma instalação. Para dimensionar uma sequência de mensagens totalmente abrangente que possa levar em consideração o comportamento do usuário, consulte nossa documentação sobre o [Canva]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Dados de referência do anúncio

Os usuários podem ser atraídos para o seu app por uma oferta promocional ou brinde. O uso de dados de atribuição de instalação permite enviar campanhas contendo códigos de desconto ou ofertas apenas para os usuários que instalaram devido a essas promoções. De maneira semelhante, se o seu anúncio contiver informações sobre um determinado produto (como um filme específico em um aplicativo de vídeo ou uma venda em um aplicativo de comércio eletrônico), você poderá enviar campanhas direcionando os usuários para a página correta do seu app.

## Avaliar os esforços de publicidade

Os dados de atribuição de instalação podem ser valiosos para avaliar a eficácia de diferentes campanhas de marketing. Analisar para ver quais anúncios e campanhas estão levando ao maior número de instalações e quais estão ficando para trás pode ser usado para concentrar seus recursos nos anúncios mais atraentes.

