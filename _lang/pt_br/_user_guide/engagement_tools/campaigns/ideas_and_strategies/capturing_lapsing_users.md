---
nav_title: Captura de usuários ausentes
article_title: Captura de usuários ausentes
page_order: 1
page_type: tutorial
description: "Este artigo de instruções aborda a questão dos usuários inativos e como usar efetivamente as campanhas da Braze para reengajar esses usuários."
tool:
  - Segments
  - Campaigns

---

# Captura de usuários ausentes

> Se o seu público estiver diminuindo, é crucial tentar atraí-lo de volta. Com o Braze, você pode configurar campanhas de reengajamento recorrentes e automatizadas para capturar usuários inativos. Você pode escolher o período de reengajamento e a recorrência mais adequados ao seu app, mas, para demonstrar, começaremos com um plano de reengajamento de 14 dias.

Para saber mais sobre o direcionamento de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

## Etapa 1: Segmentar usuários

Primeiro, criaremos um segmento para direcionar os usuários que não usaram seu app nas últimas duas semanas, usando os seguintes filtros:

- **Último aplicativo usado** há mais de 2 semanas
- **Último app usado** há menos de 3 semanas

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Nomeie o segmento com algo memorável, como "Lapsed Users - 2 Weeks" (Usuários perdidos - 2 semanas). Como estamos configurando a campanha para se repetir semanalmente, queremos ter certeza de que há pelo menos uma semana de usuários capturados no segmento. Por isso, selecionamos usuários que usaram o app pela última vez entre duas e três semanas atrás.

## Etapa 2: Criar uma campanha

Em seguida, clique em **Create Campaign (Criar campanha** ) e escolha o tipo de campanha que será enviada a esse segmento. Neste exemplo, criaremos uma nova [campanha push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nomearemos a campanha de "Message to Lapsed Users - 2 Weeks" (Mensagem para usuários inativos - 2 semanas) e criaremos o conteúdo da nossa mensagem. Neste exemplo, direcionaremos apenas os usuários do iOS, mas você pode usar a Braze para notificações por push para Android e iOS. 

Quanto mais próximo da última vez que um usuário esteve no app, mais importante é ser atual e relevante. Ao enviar mensagens no app para um usuário depois de duas semanas sem usar o aplicativo, é importante apresentar conteúdo relevante e destacar os benefícios de usar o aplicativo.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Em seguida, criaremos uma programação recorrente para enviar nossa mensagem semanal às quintas-feiras, às 17h45, usando [a entrega]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) no [horário local]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) em **Time-Based Scheduling Options**. Recomendamos que você observe o gráfico de sessões para direcionar os usuários imediatamente antes dos períodos de alta utilização. Isso garante que você tente reengajar as pessoas quando elas estiverem mais propensas a usar o app. Você pode alterar isso mais tarde e testar sua hipótese inicial.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Etapa 3: Lançar a campanha

Agora, você está pronto para enviar a campanha. Confirme as configurações na última página do criador e clique em **Lançar campanha**!

