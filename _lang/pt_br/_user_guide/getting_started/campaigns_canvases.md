---
nav_title: Campanhas e telas
article_title: "Primeiros passos: Campanhas e telas"
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral das diferentes maneiras de enviar mensagens com o Braze."

---

# Primeiros passos: Campanhas e telas

No Braze, você pode enviar mensagens por meio de uma [campanha](#campaigns) ou de um [Canvas](#canvas).

- Para enviar uma única mensagem direcionada a um grupo de usuários, escolha uma campanha. Uma campanha é uma etapa de mensagem única para se conectar com seus usuários em vários canais de mensagens.
- Para enviar uma série de mensagens contínuas em uma jornada abrangente do cliente, escolha o Canvas, nossa ferramenta de orquestração de jornada. Embora as campanhas sejam boas para o envio de mensagens simples e direcionadas, é nas Canvases que você leva o relacionamento com os clientes para o próximo nível.

## Campanhas

Embora as campanhas possam ser criadas de forma exclusiva, dependendo do canal, há quatro tipos principais de campanhas no Braze que você deve conhecer:

| Tipo de campanha        | Descrição                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular              | Esse é o tipo mais comum de campanha. Você pode segmentar um ou mais canais, dependendo de suas metas de mensagens, e projetar, personalizar e testar seu conteúdo diretamente no Braze com nossos editores visuais. Saiba como [criar uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign). |
| Teste A/B          | No caso de campanhas direcionadas a um único canal, você pode enviar mais de uma versão da mesma campanha e ver qual delas se sai melhor. Você pode testar o texto, a personalização e muito mais em até oito versões diferentes com uma [campanha multivariada]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/). |
| API                  | [As campanhas de API]({{site.baseurl}}/api/api_campaigns/) permitem que você envie mensagens oportunas o mais rápido possível. Diferentemente de outros tipos de campanha, você não especifica a mensagem, os destinatários ou a programação no painel do Braze. Em vez disso, você passa esses identificadores em suas chamadas de API. Normalmente, eles são usados para mensagens transacionais em tempo real ou notícias de última hora.  |
| E-mails transacionais | [Os]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) Braze [Transactional Emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) são criados especificamente para o envio de mensagens de e-mail automatizadas e não promocionais para facilitar uma transação acordada entre você e seus clientes. Eles enviam notificações críticas de negócios para um único usuário, onde a velocidade é de extrema importância. *Disponível para pacotes selecionados.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
As campanhas regulares e de teste A/B podem ser programadas (por exemplo, informar uma lista de usuários sobre um evento futuro) ou automatizadas para envio em resposta a uma ação do usuário (por exemplo, enviar um e-mail quando alguém se inscreve em seu boletim informativo). Saiba mais sobre o [agendamento de campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types).
{% endalert %}

Independentemente do tipo de campanha que você criar, suas campanhas podem ouvir as necessidades do usuário e fornecer uma resposta atenciosa e personalizada. Depois de enviar sua campanha, use nossas [ferramentas de análise integradas]({{site.baseurl}}/user_guide/analytics/reporting/) para ver o desempenho e quantos usuários converteram com base em seus [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Confira estes recursos adicionais para saber mais sobre as campanhas no Braze:

- Braze Learning: [Configuração de campanha](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Criar uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [Ideias e estratégias]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## Tela

Em vez de enviar mensagens esporádicas em várias campanhas, o Canvases cria uma conversa fluida e contínua com os usuários. Isso ocorre porque a jornada de um usuário por meio de um Canvas pode se dividir em diferentes caminhos, dependendo das ações (ou da falta de ação) dele com a sua marca, permitindo que você avance automaticamente os usuários por um fluxo específico em tempo real.

\![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Dessa forma, os Canvases são ótimos para lançar uma rede para capturar usuários que estão fora do caminho da conversão e colocá-los nas iniciativas de alcance mais eficazes.

Ao criar um Canvas, você segue muitas das mesmas etapas da configuração de uma campanha: especificação de um público geral, condições de entrada e configurações de envio. Seu Canvas começa quando alguém corresponde à sua condição de acionador. Em seguida, eles se movem por um caminho no Canvas até atenderem às suas condições de saída.

Seu Canvas pode ter qualquer combinação de [mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [atrasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) e muito mais. Você pode enviar em qualquer canal de mensagens compatível e até mesmo [integrar-se a plataformas sociais e de anúncios]({{site.baseurl}}/partners/canvas_audience_sync/overview/), como Facebook, Google ou TikTok.

Confira estes recursos adicionais para saber mais sobre o Canvas:

- Braze Learning: [Orquestração de jornadas com o Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Criar uma tela]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [Contornos de tela]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## Canais de mensagens

Os canais de mensagens são os vários canais de comunicação por meio dos quais você pode interagir com seus clientes e enviar mensagens direcionadas. 

\![]({% image_buster /assets/img/getting_started/channels.png %})

A tabela a seguir descreve nossos canais compatíveis.

| Canal                                                                                              | Descrição                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | Envie e-mails personalizados para as caixas de entrada de seus usuários.                                                                                                       |
| [Push móvel]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | Envie mensagens diretamente para os dispositivos móveis dos usuários como notificações.                                                                                   |
| [Empurrar pela Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Envie notificações para os navegadores da Web dos usuários, mesmo quando eles não estiverem ativamente no seu site.                                                         |
| [Mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | Exiba mensagens no seu aplicativo móvel enquanto os usuários o utilizam ativamente.                                                                             |
| [SMS, MMS e RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)                   | Envie mensagens de texto para os telefones celulares dos usuários.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | Envie mensagens por meio da popular plataforma de mensagens, o WhatsApp, para alcançar e interagir com seus usuários.                                                   |
| [Banners*]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | Incorpore mensagens diretamente em seu aplicativo ou site. |
| [Cartões de conteúdo*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | Forneça uma caixa de entrada em seu aplicativo ou site onde os usuários possam receber e interagir com as mensagens ou exibi-las em um carrossel, como um banner e muito mais. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interaja com os usuários em plataformas de televisão conectadas.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Permita a comunicação e a integração em tempo real com sistemas externos por meio de retornos de chamada HTTP personalizados.                                                    |
| [LINHA]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Interaja com os usuários no LINE, o aplicativo de mensagens mais popular do Japão.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponível como um recurso complementar.</sup>

{% alert tip %}
Para mensagens curtas e urgentes que podem ser comunicadas pela maioria dos canais (e-mail, SMS, push), aproveite o filtro [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) para enviar automaticamente a mensagem pelo melhor canal para cada usuário.
{% endalert %}

