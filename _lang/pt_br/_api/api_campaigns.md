---
nav_title: Campanhas de API
article_title: Campanhas de API
page_order: 5
description: "Este artigo de referência aborda como gerar um campaign_id para incluir em suas chamadas de API e como configurar essa campanha."
page_type: reference
tool: Campaigns

---
# Campanhas da API

> Este artigo de referência aborda como gerar um `campaign_id` para incluir em suas chamadas de API e como configurar essa campanha.

As campanhas de API são normalmente usadas para envio de mensagens de transações. Ao criar campanhas de API (não [campanhas disparadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)), o dashboard do Braze é usado apenas para gerar um `campaign_id`, que permite rastrear a análise de dados para relatórios de campanha. Também é possível gerar um ID de variação de mensagem, que é diferente para cada variante de sua campanha. 

Em seguida, você enviará essas informações à sua equipe de desenvolvimento para serem usadas na solicitação da API, juntamente com:
- Cópia da campanha
- Participação do público
- Ativos

Após o início da campanha, você pode visualizar os resultados no dashboard. As campanhas de API usam as [APIs de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) do Braze, que têm as mesmas opções detalhadas de relatórios e redirecionamento que as campanhas criadas completamente por meio do dashboard.

{% alert warning %}
Como as campanhas de API são normalmente transacionais, todos os usuários são elegíveis, mesmo os do seu grupo de controle global. Um cabeçalho [de cancelamento de inscrição na lista de um clique]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) não é adicionado a esses envios. Se quiser adicionar um cabeçalho de cancelamento de inscrição com um clique a todas as campanhas da API, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Criar uma nova campanha

Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha** e, em seguida, selecione **Campanhas de API**. Agora, você pode prosseguir com a configuração de sua campanha de API.

Uma [campanha disparada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) é diferente de uma campanha por API.

## Configure sua campanha

Para configurar sua campanha, execute as seguintes etapas:

1. Adicione um título descritivo para que possa encontrar os resultados em nossa página de campanhas após o envio das mensagens.
2. Clique em **Add Message (Adicionar mensagem** ) e adicione os tipos de mensagens que serão incluídos em sua campanha de mensagens API. Isso permitirá que você gere um `campaign_id` e um ID de variação de mensagem, que é diferente para cada canal que você incluir. 
3. Opcionalmente, é possível adicionar um evento de conversão para rastrear as conversões do usuário em uma ação ou meta de campanha específica.
4. Clique em **Salvar campanha** e você poderá iniciar sua campanha da API!

## Chamadas de API

Depois de salvar sua campanha de API, inclua o seguinte em sua solicitação de API: 
- Os campos `campaign_id` gerados com sua solicitação de API foram notados nos [Endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints).
- Um [objeto de mensagem]({{site.baseurl}}/api/objects_filters/#messaging-objects) para cada plataforma incluída na campanha. No objeto de mensagem, forneça o ID de variação da mensagem. Isso especificará que as estatísticas devem ser coletadas e exibidas nessa variante. Os seguintes objetos de mensagem são suportados: Android, cartões de conteúdo, e-mail, iOS, Kindle, SMS/MMS, web push e webhook.


