---
nav_title: Visão geral da plataforma
article_title: Visão geral da plataforma
page_order: 1
description: "Este artigo aborda as partes básicas e os recursos da plataforma Braze. Os links deste artigo se conectam a tópicos essenciais do Braze."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/path/developer) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Primeiros passos: Visão geral da plataforma

> Este artigo aborda as partes básicas e os recursos da plataforma Braze. Os links deste artigo se conectam a tópicos essenciais do Braze. 

{% alert tip %}
Confira nosso curso gratuito [Developer Learning Path](https://learning.braze.com/path/developer) junto com estes artigos.
{% endalert %}

## O que é a Braze?

A Braze é uma plataforma de engajamento com clientes. Isso significa simplesmente que o Braze o ajuda a ouvir seus usuários, entender as ações e os comportamentos deles e, em seguida, agir de acordo com eles. A plataforma Braze tem três componentes principais: o SDK, o dashboard e a API REST.

Se você for um profissional de marketing e estiver procurando uma visão geral do Braze, consulte a [seção Introdução para profissionais de marketing]({{site.baseurl}}/user_guide/getting_started/overview/).

![O Braze tem diferentes camadas. No total, ela é formada pelo SDK, a API, o dashboard e as integrações com parceiros. Cada uma delas contribui com partes de uma camada de ingestão de dados, uma camada de classificação, uma camada de orquestração, uma camada de personalização e uma camada de ação. A camada de ação tem vários canais, incluindo push, mensagens no app, Connected Catalog, webhook, SMS e e-mail.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

Os [SDKs Braze](#integrating-braze) podem ser integrados aos seus aplicativos móveis e da Web para fornecer ferramentas poderosas de marketing, gerenciamento de usuários e análise de dados.

Em resumo, quando está totalmente integrado, o SDK:

* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Coleta automaticamente dados da sessão, informações do dispositivo e tokens por push
* Captura dados de engajamento de marketing e dados personalizados específicos de sua empresa
* É arquitetado para segurança e testado quanto à penetração por terceiros
* É otimizado para dispositivos com pouca bateria ou de rede lenta
* Oferece suporte a assinaturas JWT no lado do servidor para aumentar a segurança
* Tem acesso somente para gravação aos seus sistemas (não pode recuperar dados de usuários)
* Potencializa as notificações por push, as mensagens no app e os canais de envio de mensagens do cartão de conteúdo

### Interface de usuário do dashboard

O dashboard é a interface do usuário que controla todos os dados e interações no coração da plataforma Braze. Os profissionais de marketing usarão o dashboard para fazer seu trabalho e criar conteúdo. Os desenvolvedores usam o dashboard para gerenciar as configurações de integração de apps, como chaves de API e credenciais de notificação por push.

Se estiver apenas começando, o administrador da sua equipe deve adicionar você (e todos os outros membros da equipe que precisam de acesso ao Braze) como [usuários no seu dashboard]({{site.baseurl}}/user_guide/administrative/access_braze).

### API REST

A API da Braze permite que você mova dados para dentro e para fora da Braze em escala. Use a API para trazer atualizações de seu back-end, data warehouses e outras fontes primárias e de terceiros. Além disso, use a API para adicionar eventos personalizados para fins de segmentação diretamente de um aplicativo baseado na Web. Você pode disparar e enviar mensagens por meio da API, permitindo que os recursos técnicos incluam metadados JSON complexos como parte de suas campanhas.

A API também fornece um serviço da Web em que é possível registrar as ações realizadas pelos usuários diretamente via HTTP, em vez de usar os SDKs móveis e da Web. Combinado com webhooks, isso significa que você pode rastrear ações e disparar atividades para usuários dentro e fora da experiência no app. O [guia da API]({{site.baseurl}}/api/home) lista os endpoints da Braze API disponíveis e seus usos.

Para saber mais sobre a Braze, confira: [Primeiros passos: Visão geral da arquitetura]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Análise de dados e ação

Os dados armazenados no Braze são retidos e podem ser usados para segmentação, personalização e direcionamento enquanto você for um cliente Braze. Isso permite que você aja com base nos dados de perfil de usuários (por exemplo, atividade de sessão ou compras) até que você decida descontinuar essas informações. Por exemplo, um serviço de fluxo de dados poderia rastrear o conteúdo visto por cada inscrito desde o primeiro dia no serviço (mesmo que isso tenha ocorrido há muitos anos) e usar esses dados para enviar mensagens relevantes.

![Um segmento no dashboard do Braze chamado "Compradores recentes" colocado ao lado de uma tela de telefone mostrando o e-mail "Principais recomendações para Linda".]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### Análise de dados do app

O dashboard do Braze exibe gráficos que são atualizados em tempo real com base em uma série de métricas de análise de dados, bem como em eventos personalizados que você instrumenta em seu aplicativo. A medição e a otimização consistentes de suas campanhas com Testes A/B, relatórios e análises de dados personalizados e inteligência automatizada ajudam a manter os clientes engajados e a se destacar dos concorrentes em seu espaço.

### Segmentação de usuários

A segmentação permite criar grupos de usuários com base em filtros poderosos de seu comportamento in-app, dados demográficos e similares. O Braze também permite que você defina qualquer ação do usuário no app como um "evento personalizado" se a ação desejada não for capturada por padrão. O mesmo se aplica às características do usuário por meio de "atributos personalizados". Depois que um segmento de usuário for criado no dashboard, seus usuários entrarão e sairão do segmento à medida que atenderem (ou não atenderem) aos critérios definidos. Por exemplo, você pode criar um segmento que inclua todos os usuários que gastaram dinheiro no app e que usaram o aplicativo pela última vez há mais de duas semanas.

Para saber mais sobre nossos modelos de dados, confira: [Primeiros passos: Visão geral da análise de dados]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## Mensagens em vários canais

Depois de definir um segmento, as ferramentas de mensagens privadas do Braze permitem o engajamento com seus usuários de forma dinâmica e personalizada. A Braze foi projetada com um modelo de dados independente de canal e centrado no usuário. O envio de mensagens é feito dentro do seu aplicativo ou site (como o envio de mensagens no app ou por meio de elementos gráficos como carrosséis e banners do cartão de conteúdo) ou fora da experiência no app (como o envio de notificações por push ou e-mails). Por exemplo, seus profissionais de marketing podem enviar uma notificação por push e um e-mail para o segmento de exemplo definido na seção anterior.

![Crie e dispare mensagens personalizadas em qualquer canal, seja fora ou dentro de seu app ou site.]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| Canal                                                                                              | Descrição                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Cartões de conteúdo*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) | Envie notificações in-app altamente direcionadas e dinâmicas sem interromper o cliente. |
| [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | Envie mensagens em HTML avançado criando seu e-mail usando o editor de rich-text, nosso editor de arrastar e soltar ou fazendo upload de um de seus modelos HTML existentes. |
| [Mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Envie notificações discretas no app usando a interface de usuário nativa personalizada da Braze. |
| [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | Dispare automaticamente notificações por push de campanhas de mensagens ou itens de notícias usando o serviço de Notificações por Push da Apple (APNs) para iOS ou o Firebase Cloud Messaging (FCM) para Android. |
| [SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs)* | Use SMS, MMS ou RCS para enviar notificações transacionais, compartilhar promoções, enviar lembretes e mais. |
| [Web push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | Envie notificações ao navegador da Web, mesmo que os usuários não estejam ativos no site no momento. |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Use webhooks para disparar ações que não sejam do aplicativo, fornecendo dados em tempo real a outros sistemas e aplicativos. |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | Conecte-se diretamente com seus usuários e clientes aproveitando a popular plataforma de envio de mensagens ponto a ponto: WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponível como um recurso complementar.</sup>

### Componentes personalizáveis

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> Todos os componentes da Braze são criados para serem acessíveis, adaptáveis e personalizáveis. Você pode começar a usar o Braze usando os componentes padrão do `BrazeUI` e personalizando-os para atender às necessidades de sua marca e ao seu caso de uso.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> Para ir além das opções padrão, você pode escrever um código personalizado para atualizar a aparência de um canal de envio de mensagens para que ele corresponda melhor à sua marca. Isso inclui a alteração do tipo de fonte, do tamanho da fonte e das cores de um componente. Os profissionais de marketing mantêm o controle do público, do conteúdo, do comportamento ao clicar e da expiração diretamente no dashboard do Braze.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> Também é possível criar componentes totalmente personalizados para controlar a aparência das mensagens, como elas se comportam e como interagem com outros canais de envio de mensagens (por exemplo, disparando um Content Card com base em uma notificação por push). A Braze fornece métodos SDK para permitir o registro de métricas como impressões, cliques e demissões no dashboard da Braze. Cada canal de envio de mensagens tem um artigo de análise de dados para ajudar a facilitar isso.
{% endgallery %}

<br>
<br>

## Integração do Braze

O Braze foi projetado para entrar em operação de forma rápida e fácil. Nosso tempo médio de obtenção de valor é de seis semanas em nossa base de clientes de centenas de marcas. Para saber mais sobre o processo de integração, confira: [Primeiros passos: Visão geral da integração]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## Recursos para adicionar aos favoritos

Como um recurso técnico, você estará envolvido em muitos dos detalhes básicos da Braze. Aqui estão alguns bons recursos que podem ser marcados como favoritos fora de nossa documentação. Enquanto estiver acessando, mantenha nosso glossário [Terms to Know]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) à mão caso tenha dúvidas sobre termos do Braze.

| Recursos | O que você aprenderá|
|---|---|
| [Depurando o SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | Ao solucionar problemas na sua integração, a ferramenta de debug do SDK será uma ferramenta útil. Certifique-se de tê-la à mão! |
| [GitHub público do Braze](https://github.com/braze-inc/) | Você encontrará informações detalhadas sobre integração e exemplos de código em nosso repositório do GitHub. |
| [Repositório GitHub do Android SDK](https://github.com/braze-inc/braze-android-sdk/) | O repositório GitHub do Android SDK. |
| [Referência do SDK do Android](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Documentação de classe para o Android SDK. |
| [Repositório do GitHub do SDK do iOS (Swift)](https://github.com/braze-inc/braze-swift-sdk) | O repositório GitHub do Swift SDK. |
| [Referência do SDK do iOS (Swift)](https://braze-inc.github.io/braze-swift-sdk/) | Documentação de classe para o SDK do iOS. |
| [Repositório do GitHub do Web SDK](https://github.com/braze-inc/braze-web-sdk) | O repositório GitHub do Web SDK. |
| [Referência do Web SDK](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | Documentação de classe para o SDK do iOS. |
| [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) | A Braze tem previsões de lançamentos mensais, além de lançamentos para quaisquer problemas críticos e atualizações importantes do sistema operacional. |
| [Coleção Braze API Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Baixe nossa coleção Postman aqui.  |
| [Monitor de status do sistema Braze](https://braze.statuspage.io/) | Nossa página de status é atualizada sempre que há incidentes ou interrupções. Acesse esta página para se inscrever para receber alertas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

