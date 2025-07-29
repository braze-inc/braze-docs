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



Nomeie o segmento com algo memorável, como "Lapsed Users - 2 Weeks" (Usuários perdidos - 2 semanas). Como estamos configurando a campanha para se repetir semanalmente, queremos ter certeza de que há pelo menos uma semana de usuários capturados no segmento. Por isso, selecionamos usuários que usaram o app pela última vez entre duas e três semanas atrás.

## Etapa 2: Criar uma campanha





Nomearemos a campanha de "Message to Lapsed Users - 2 Weeks" (Mensagem para usuários inativos - 2 semanas) e criaremos o conteúdo da nossa mensagem. Neste exemplo, direcionaremos apenas os usuários do iOS, mas você pode usar a Braze para notificações por push para Android e iOS. 

Quanto mais próximo da última vez que um usuário esteve no app, mais importante é ser atual e relevante. Ao enviar mensagens no app para um usuário depois de duas semanas sem usar o aplicativo, é importante apresentar conteúdo relevante e destacar os benefícios de usar o aplicativo.



 Recomendamos que você observe o gráfico de sessões para direcionar os usuários imediatamente antes dos períodos de alta utilização. Isso garante que você tente reengajar as pessoas quando elas estiverem mais propensas a usar o app. Você pode alterar isso mais tarde e testar sua hipótese inicial.



## Etapa 3: Lançar a campanha

Agora, você está pronto para enviar a campanha. Confirme as configurações na última página do criador e clique em **Lançar campanha**!

