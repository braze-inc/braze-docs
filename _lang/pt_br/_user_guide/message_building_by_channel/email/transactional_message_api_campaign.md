---
nav_title: Campanhas de e-mail transacionais
article_title: Campanhas de e-mail transacionais
page_order: 10

description: "Este artigo de referência aborda como criar e configurar uma nova campanha de Braze Transactional Email."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campanhas de e-mail transacionais

> Os Braze Transactional Emails são enviados para facilitar uma transação acordada entre o remetente e o destinatário. Este artigo de referência aborda como criar uma campanha de e-mail transacional no painel do Braze e gerar um `campaign_id` para incluir em suas chamadas de API para nosso [endpoint`/transactional/v1/campaigns/{campaign_id}/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
O Braze Transactional Email está disponível apenas como parte de pacotes Braze selecionados. Entre em contato com o gerente de sucesso do cliente Braze ou abra um [tíquete de suporte]({{site.baseurl}}/braze_support/) para obter mais detalhes.
{% endalert %}

O tipo de campanha de e-mail transacional foi criado especificamente para enviar mensagens de e-mail automatizadas e não promocionais para facilitar uma transação acordada entre você e seus clientes. Isso inclui informações como:

- Confirmações de pedidos
- Redefinição de senha
- Alertas de faturamento
- Alertas de remessa

Em resumo, você pode usar e-mails transacionais para enviar notificações críticas de negócios originadas do seu serviço para um único usuário, em que a velocidade é de extrema importância. 

{% alert important %}
Os e-mails transacionais diferem das campanhas transacionais, que podem ser usadas para direcionar seus usuários sem custos adicionais. As campanhas transacionais, por exemplo, podem incluir mensagens enviadas depois que um usuário adiciona um item ao carrinho. Confira [as opções de segmentação de público-alvo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) para obter mais informações.
{% endalert %}

## Etapa 1: Criar uma nova campanha

Para criar uma nova campanha de e-mail transacional, crie uma campanha e selecione **E-mail transacional** como seu canal de mensagens.

Crie o menu suspenso Campanha com a opção destacada para e-mail transacional.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Agora, você pode prosseguir com a configuração de sua campanha de e-mail transacional.

## Etapa 2: Configure sua campanha

O fluxo de criação de campanhas para campanhas de e-mail de transação é simplificado em comparação com o de uma [campanha de e-mail padrão]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) para garantir que o e-mail de transação crítico para os negócios possa alcançar todos os usuários.

Como resultado, você notará que várias configurações com as quais você pode estar familiarizado em outros tipos de campanha do Braze não são necessárias ao configurar esse tipo de campanha:

- A etapa **de entrega** foi simplificada para remover as opções de agendamento. Os e-mails transacionais sempre serão acionados por meio da Braze REST API usando o ID da campanha mostrado na página de **entrega**. Configurações adicionais, como controles de reelegibilidade e configurações de limite de frequência, também foram removidas para confirmar que todos os usuários estão acessíveis para esses alertas transacionais essenciais quando seu serviço aciona uma solicitação de envio.
- A etapa **Target Audiences** foi removida. Como os e-mails transacionais inscrevem toda a sua base de usuários como elegível (incluindo usuários que não se inscreveram), não há necessidade de especificar filtros ou segmentos. Como resultado, se você tiver alguma lógica a ser aplicada a quem deve receber essa mensagem, recomendamos aplicar essa lógica antes de determinar se deve fazer a solicitação de API ao Braze para disparar a mensagem para um usuário específico.
- A etapa **Conversões** foi removida. Os e-mails transacionais não são compatíveis com o rastreamento de eventos de conversão no momento.

Fluxo de trabalho de composição, entrega e confirmação para criar uma campanha de e-mail transacional.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Para configurar sua campanha de e-mail transacional, siga estas etapas:

1. Adicione um nome descritivo para que você possa encontrar os resultados na página **Campaigns** depois de enviar as mensagens.
2. Escreva seu e-mail ou selecione um modelo.
3. Anote seu `campaign_id`. Depois de salvar sua campanha de API, você deve incluir os campos `campaign_id` gerados com sua solicitação de API, conforme indicado no artigo sobre o [endpoint de e-mail transacional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Clique em **Save Campaign (Salvar campanha)** e você estará pronto para iniciar sua campanha de API!

{% alert note %}
A configuração de cancelamento de inscrição na lista de um clique para campanhas de e-mail transacionais tem como padrão **Usar padrão do espaço de trabalho**, semelhante a outras campanhas de e-mail. Como isso se destina a mensagens transacionais, o Braze não adiciona o cancelamento de inscrição com um clique. Para adicionar um cancelamento de assinatura com um clique a esse tipo de campanha, [edite essa configuração]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) em **Informações de envio**.
{% endalert %}

### Tags não permitidas em e-mails transacionais

As tags `Connected Content` e `Promotion Code` Liquid não estão disponíveis em campanhas de e-mail transacionais.

O uso da tag `Connected Content` exige que o Braze faça uma solicitação de API de saída durante o nosso processo de envio, o que pode tornar o processo de envio de mensagens mais lento se o serviço externo que solicitamos estiver sofrendo latência. Da mesma forma, a tag `Promotion Code` exige que o Braze realize um processamento adicional para avaliar a disponibilidade de uma promoção antes do envio, o que pode retardar o processo de envio caso não haja uma disponível.

Como resultado, não aceitamos a inclusão de tags `Connected Content` ou `Promotion Code` em nenhum campo de sua campanha de e-mail transacional.


