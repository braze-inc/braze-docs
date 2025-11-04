---
nav_title: Entendendo as instalações de usuários
article_title: Entendendo as Instalações de Usuários 
page_order: 7
page_type: reference
description: "Este artigo de referência descreve as instalações de usuários (rastreamento de atribuição de instalação) e diferentes maneiras de aplicar essas informações em sua campanha."
tool:
  - Campaigns
  - Segments
---

# Entendendo as instalações de usuários

> O rastreamento de atribuição de instalação é uma ótima maneira de melhorar seu relacionamento inicial com o usuário. Saber como, onde e, mais importante, por que um usuário instala seu aplicativo permite que você tenha uma melhor compreensão de quem é seu usuário e como você deve apresentá-lo ao seu aplicativo. 

Embora a Braze não forneça rastreamento de atribuição de instalação, podemos integrar com [serviços]({{site.baseurl}}/partners/message_orchestration/) como Branch e AppsFlyer para fornecer dados de instalação de forma integrada.

## Segmentar seus usuários

Uma vez que seu usuário instala seu aplicativo, você pode começar a segmentá-los com base nos seguintes [filtros de atribuição de instalação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution). Por exemplo, um aplicativo de viagens poderia adicionar usuários que vieram de um anúncio relacionado a ofertas de férias na praia a um segmento "Amantes da Praia". Da mesma forma, um aplicativo de música poderia segmentar usuários com base no gênero musical exibido no anúncio que levou à instalação.

## Melhores práticas

### Onboarding personalizado

Agora que você tem mais informações sobre seu usuário, pode personalizar o processo de onboarding dele. Isso pode ser tão simples quanto mudar as imagens em suas mensagens para se adequar às preferências deles, ou tão complexo quanto criar um onboarding único para cada anúncio que poderia levar a uma instalação. Para escalar uma sequência totalmente abrangente de mensagens que pode levar em consideração o comportamento do usuário, consulte nossa documentação sobre [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Dados de referência do anúncio

Os usuários podem ser atraídos para seu aplicativo por uma oferta promocional ou sorteio. Usar dados de atribuição de instalação permite que você envie campanhas contendo códigos de desconto ou ofertas apenas para os usuários que instalaram devido a essas promoções. De maneira semelhante, se seu anúncio contiver informações sobre um produto específico (como um filme específico em um aplicativo de vídeo ou uma venda em um aplicativo de eCommerce), você pode enviar campanhas direcionando os usuários para a página correta do seu aplicativo.

## Avaliar esforços publicitários

Instalar dados de atribuição pode ser valioso na avaliação da eficácia de diferentes campanhas de marketing. Analisar quais anúncios e campanhas estão levando ao maior número de instalações e quais estão ficando para trás pode ser usado para concentrar seus recursos nos anúncios mais atraentes.

