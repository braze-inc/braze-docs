---
nav_title: Agosto
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão para agosto de 2021."
---

# Agosto de 2021

## Sincronização do público do Google

A integração da Braze [Audience Sync com o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) ativa as marcas para estender o alcance de suas jornadas de clientes entre canais para a Pesquisa do Google, o Google Shopping, o Gmail, o YouTube e o Google Display. Usando seus dados primários de clientes, é possível fornecer anúncios com segurança com base em disparadores comportamentais dinâmicos, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (por exemplo, push, e-mail, SMS etc.) como parte de um Braze Canvas pode ser usado para disparar um anúncio para esse usuário por meio do Customer Match do Google.

## Guia de práticas recomendadas para integração de SDK do iOS

Este guia opcional de [integração do SDK com o iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk) leva você a uma jornada passo a passo sobre as práticas recomendadas de configuração ao integrar pela primeira vez o SDK do iOS e seus componentes principais em seu aplicativo. Este guia o ajudará a criar um arquivo auxiliar `BrazeManager.swift` que desacoplará todas as dependências do SDK da Braze para iOS do restante do seu código de produção, resultando em um `import AppboyUI` em todo o seu aplicativo. Essa abordagem limita os problemas decorrentes do excesso de importações de SDK, facilitando o rastreamento, a depuração e a alteração do código. 

## Compras preditivas

As compras preditivas oferecem aos profissionais de marketing uma ferramenta poderosa para a identificação e o envio de mensagens privadas aos usuários com base na probabilidade de que eles façam uma compra. Quando você cria uma previsão de compra, o Braze treina um modelo de machine learning usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender com a atividade de compra anterior e prever a atividade de compra futura. Visite nossos documentos sobre [compras preditivas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) para saber mais. 

## Editor de arrastar e soltar

Com o Braze Email, você pode criar mensagens de e-mail totalmente personalizadas em campanhas ou canvas usando nossa nova [experiência de edição de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/). Os usuários agora podem arrastar blocos do editor para seus e-mails, permitindo uma personalização mais intuitiva. 

## Importação de alias de usuário

Para direcionar os usuários que não têm um `external_id`, é possível [importar uma lista de usuários com aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). Um alias serve como um identificador de usuário exclusivo alternativo. Pode ser útil se você estiver tentando fazer marketing para usuários anônimos que não se inscreveram ou fizeram uma conta no seu app. 

## Guia para fazer upgrade do iOS 15

Este [guia de atualização do iOS 15]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) descreve as alterações introduzidas no iOS 15 (WWDC21) e as etapas de atualização necessárias para a integração de seu SDK da Braze para iOS.

## Guia de atualização do Android 12

Este [guia de atualização do Android 12]({{site.baseurl}}/developer_guide/platforms/android/android_13/) descreve as alterações relevantes introduzidas no Android 12 (2021) e as etapas de atualização necessárias para a integração de seu Braze Android SDK.

## A2P 10DLC

A2P 10DLC refere-se a um sistema nos Estados Unidos que permite que as empresas enviem mensagens do tipo aplicativo para pessoa (A2P) por meio de um número de telefone padrão de código longo de 10 dígitos (10DLC). Os códigos longos de 10 dígitos foram tradicionalmente projetados para o tráfego de pessoa para pessoa (P2P), fazendo com que as empresas sejam restringidas por uma taxa de transferência limitada e por uma filtragem maior. Esse serviço ajuda a aliviar esses problemas, melhorando a entregabilidade geral das mensagens, permitindo que as marcas enviem mensagens em escala, incluindo links e chamadas para ação, e ajudando a proteger ainda mais os consumidores contra mensagens indesejadas. 

Todos os clientes que atualmente têm e/ou usam códigos longos dos EUA para enviar a clientes dos EUA devem registrar seus códigos longos para o 10DLC. Para saber mais sobre os detalhes do 10DLC e por que ele é necessário, acesse nosso [artigo dedicado ao 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Redefinição da autenticação de dois fatores

Os usuários que tiverem problemas para registrar-se por meio da autenticação de dois fatores podem entrar em contato com os administradores da empresa para [redefinir a autenticação de dois fatores]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## Novas parcerias Braze

### Hightouch - Automação do fluxo de trabalho

A integração entre a Braze e o [Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) permite que você crie campanhas melhores na Braze com dados atualizados de clientes de seu data warehouse. Você deseja fornecer interações relevantes e oportunas aos seus clientes e, para isso, depende muito de que os dados da sua conta Braze sejam precisos e atualizados. Ao sincronizar automaticamente os dados de clientes do seu data warehouse para o Braze, você não precisa mais se preocupar com a consistência dos dados e pode se concentrar na criação de experiências de clientes de classe mundial.

### Transcend - Privacidade e conformidade de dados

A parceria entre a Braze e a [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/) ajuda os usuários a automatizar as solicitações de privacidade orquestrando dados em dezenas de sistemas de dados. Em última análise, isso ajuda as equipes a cumprir regulamentos como GDPR e CCPA e coloca os indivíduos no comando quando se trata de seus dados.

### Tinyclues - Importação de coorte

O [Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/) é um recurso de criação de público que oferece a capacidade de aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, além de análise de dados para rastrear a performance das campanhas de CRM on-line e off-line. Juntas, a integração entre Braze e Tinyclues oferece aos usuários uma jornada para um melhor planejamento e estratégia de CRM, permitindo que os usuários enviem mais campanhas de direcionamento, encontrem novas oportunidades de produtos e aumentem a receita usando uma interface de usuário incrivelmente fácil de usar.

### Optilyz - Mala direta

A [optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/) é uma plataforma de automação de mala direta que ativa campanhas de mala direta mais centradas no cliente, sustentáveis e lucrativas. A optilyz é usada por centenas de empresas em toda a Europa e capacita você a integrar cartas, cartões postais e self-mailers em seu marketing de canais cruzados e a automatizar e personalizar melhor as campanhas. Use a integração entre o Optilyz e a Braze para enviar mala direta aos seus clientes.