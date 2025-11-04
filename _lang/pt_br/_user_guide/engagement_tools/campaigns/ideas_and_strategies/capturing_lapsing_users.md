---
nav_title: Captura de usuários inativos
article_title: Captura de usuários ausentes
page_order: 1
page_type: tutorial
description: "Este artigo de instruções aborda a questão dos usuários inativos e como usar efetivamente as campanhas do Braze para reengajar esses usuários."
tool:
  - Segments
  - Campaigns

---

# Captura de usuários inativos

> Se o seu público estiver diminuindo, é fundamental tentar atraí-lo de volta. Com o Braze, você pode configurar campanhas automatizadas e recorrentes de reengajamento para capturar usuários inativos. Você pode escolher o período de reengajamento e a recorrência mais adequados ao seu aplicativo, mas, para demonstrar, começaremos com um plano de reengajamento de 14 dias.

Para saber mais sobre a segmentação de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

## Etapa 1: Segmentar usuários

Primeiro, criaremos um segmento para segmentar usuários que não usaram seu aplicativo nas últimas duas semanas, usando os seguintes filtros:

- **Aplicativo usado pela última vez** há mais de 2 semanas
- **Aplicativo usado pela última vez** há menos de 3 semanas

\![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Nomeie o segmento com algo memorável, como "Lapsed Users - 2 Weeks" (Usuários perdidos - 2 semanas). Como estamos configurando a campanha para se repetir semanalmente, queremos garantir que haja pelo menos uma semana de usuários capturados no segmento. Por isso, selecionamos usuários que usaram o aplicativo pela última vez entre duas e três semanas atrás.

## Etapa 2: Criar uma campanha

Em seguida, clique em **Create Campaign (Criar campanha** ) e escolha o tipo de campanha que será enviada a esse segmento. Neste exemplo, criaremos uma nova [campanha push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).

\![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nomearemos a campanha como "Message to Lapsed Users - 2 Weeks" (Mensagem para usuários inativos - 2 semanas) e, em seguida, criaremos o conteúdo da nossa mensagem. Neste exemplo, vamos segmentar apenas os usuários de iOS, mas você pode usar o Braze para notificações por push para Android e iOS. 

Quanto mais próximo da última vez que um usuário esteve no aplicativo, mais importante é ser atual e relevante. Ao enviar uma mensagem a um usuário após duas semanas sem usar o aplicativo, é importante apresentar conteúdo relevante e destacar os benefícios de usar o aplicativo.

\![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Em seguida, criaremos um agendamento recorrente para enviar nossa mensagem semanal às quintas-feiras, às 17h45, usando [a entrega]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) no [fuso horário local]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) em **Time-Based Scheduling Options**. Recomendamos que você analise o gráfico de sessões para direcionar os usuários imediatamente antes dos períodos de alta utilização. Isso garante que você tente reengajar as pessoas quando elas estiverem mais propensas a usar o aplicativo. Você pode alterar isso mais tarde e testar sua hipótese inicial.

\![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Etapa 3: Lançar a campanha

Agora, você está pronto para enviar a campanha. Confirme as configurações na última página do compositor e clique em **Launch Campaign**!

