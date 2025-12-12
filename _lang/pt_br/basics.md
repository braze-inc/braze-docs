---
nav_title: "Visão geral da API"
article_title: Visão geral da API
page_order: 2.1
description: "Este artigo de referência aborda os fundamentos da API, incluindo o que é uma API REST, a terminologia e uma visão geral das chaves de API."
page_type: reference
alias: /api/api_key/
---

# Visão geral da API

> Este artigo de referência aborda os conceitos básicos da API, incluindo a terminologia comum e uma visão geral das chaves da API REST, permissões e como mantê-las seguras.

## Coleção da API do Braze REST

| Coleção                                                                 | Finalidade                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catálogos]({{site.baseurl}}/api/endpoints/catalogs/)                       | Crie e gerencie catálogos e itens de catálogo para fazer referência em suas campanhas no Braze.    |
| [Ingestão de dados na nuvem]({{site.baseurl}}/api/endpoints/cdi/)                | Gerencie as integrações e sincronizações de seu data warehouse.                                    |
| [Listas e endereços de e-mail]({{site.baseurl}}/api/endpoints/email/)         | Configure e gerencie a sincronização bidirecional entre o Braze e seus sistemas de e-mail.           |
| [Exportar]({{site.baseurl}}/api/endpoints/export/)                           | Acesse e exporte várias informações de suas campanhas, canvas, KPIs e muito mais.        |
| [Mensagens]({{site.baseurl}}/api/endpoints/messaging/)                      | Programe, envie e gerencie suas campanhas e Canvas.                               |
| [Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/)     | Crie sua Central de Preferências e atualize o estilo dela.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Gerencie identidades de usuários em aplicativos e serviços baseados em nuvem.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Gerencie os números de telefone de seus usuários em seus grupos de inscrições.                         |
| [Grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) | Liste e atualize os grupos de inscrições para e-mail e SMS armazenados no dashboard do Braze. |
| [Modelos]({{site.baseurl}}/api/endpoints/templates/)                     | Crie e atualize modelos para envio de mensagens de e-mail e blocos de conteúdo.                   |
| [Dados de usuários]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifique, rastreie e gerencie seus usuários.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Definições da API

A seguir, uma visão geral dos termos que você poderá ver na documentação da Braze REST API.

### Endpoints

A Braze gerencia várias instâncias diferentes para nosso dashboard e endpoints REST. Quando sua conta for provisionada, você fará o registro em um dos seguintes URLs. Use o endpoint REST correto com base na instância para a qual você está provisionado. Se não tiver certeza, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/) ou use a tabela a seguir para fazer a correspondência entre o URL do painel que você usa e o endpoint REST correto.

{% alert important %}
Ao usar endpoints para chamadas de API, use o endpoint REST.

Para integração de SDK, use o [endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), não o endpoint de REST.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### Limites da API

Para a maioria das APIs, a Braze tem um limite de frequência padrão de 250.000 solicitações por hora. No entanto, determinados tipos de solicitação têm seu próprio limite de frequência aplicado para lidar melhor com grandes volumes de dados de nossa base de clientes. Para obter informações, consulte [os limites de frequência da API]({{site.baseurl}}/api/api_limits/)

### IDs de usuário

- **ID de usuário externo**: O endereço `external_id` serve como um identificador exclusivo do usuário para o qual você está enviando dados. Esse identificador deve ser o mesmo que você definiu no SDK do Braze para evitar a criação de vários perfis para o mesmo usuário.
- **Braze user ID**: `braze_id` serve como um identificador de usuário exclusivo que é definido pela Braze. Esse identificador pode ser usado para excluir usuários por meio da API REST, além de external_ids.

Para saber mais, consulte os seguintes artigos com base em sua plataforma: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

## Sobre as chaves da API REST

Uma chave de interface de programação de aplicativo REST (chave de API REST) é um código exclusivo que é passado para uma API para autenticar a chamada de API e identificar o aplicativo ou o usuário que está fazendo a chamada. O acesso à API é feito usando solicitações da Web HTTPS para o endpoint da API REST de sua empresa. Usamos as chaves da API REST no Braze em conjunto com as chaves do App Identifier para rastrear, acessar, enviar, exportar e analisar dados para ajudar a garantir que tudo esteja funcionando sem problemas, tanto do seu lado quanto do nosso.

Os espaços de trabalho e as chaves de API andam de mãos dadas no Braze. Os espaços de trabalho são projetados para abrigar versões do mesmo aplicativo em várias plataformas. Muitos clientes também usam espaços de trabalho para conter versões gratuitas e premium de seus aplicativos na mesma plataforma. Como você pode notar, esses espaços de trabalho também estão usando a API REST e têm suas próprias chaves de API REST. Estas chaves podem ter escopo individual para incluir acesso a endpoints específicos na API. Cada chamada para a API precisa incluir uma chave com acesso ao endpoint atingido.

Referimo-nos tanto à chave da API REST quanto à chave da API do espaço de trabalho como `api_key`. O `api_key` é incluído em cada solicitação como um cabeçalho de solicitação e atua como uma chave de autenticação que lhe permite usar nossas APIs REST. Essas APIs REST são usadas para rastrear usuários, enviar mensagens, exportar dados de usuários e muito mais. Ao criar uma nova chave da API REST, você precisará dar a ela acesso a endpoints específicos. Ao atribuir permissões específicas a uma chave de API, você pode limitar exatamente quais chamadas uma chave de API pode autenticar.

![Painel de chaves da API REST na guia Chaves da API.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Além das chaves da API REST, também existe um tipo de chave chamado Chaves de identificador que pode ser usado para fazer referência a itens específicos, como aplicativos, modelos, Canvas, campanhas, cartões de conteúdo e segmentos da API. Para saber mais, consulte [Tipos de identificadores da API]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Criação de chaves da API REST

Para criar uma nova chave da API REST:

1. Acesse **Configurações** > **APIs e identificadores**.
2. Selecione **Create API Key (Criar chave de API**).
3. Dê um nome à sua nova chave para identificá-la rapidamente.
4. Especifique [endereços de IP na lista de permissões](#api-ip-allowlisting) e subredes para a nova chave.
5. Selecione as [permissões](#rest-api-key-permissions) que deseja associar à sua nova chave.

{% alert important %}
Lembre-se: depois de criar uma nova chave de API, você não poderá editar o escopo das permissões ou os IPs permitidos. Essa limitação está em vigor por motivos de segurança. Se você precisar alterar o escopo de uma chave, crie uma nova chave com as permissões atualizadas e implemente essa chave no lugar da antiga. Depois de concluir a implementação, você pode excluir a chave antiga.
{% endalert %}

### Permissões de chave de API REST

As permissões de chave de API são permissões que podem ser atribuídas a um usuário ou grupo para limitar seu acesso a determinadas chamadas de API. Para visualizar sua lista de permissões de chave de API, acesse **Settings (Configurações)** > **APIs and Identifiers (APIs e identificadores)** e selecione sua chave de API.

{% tabs %}
{% tab User Data %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Registre atributos do usuário, eventos personalizados e compras. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Exclua qualquer usuário. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Crie um novo alias para um usuário existente. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifique um usuário somente de alias com um ID externo. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Faça uma consulta para obter informações do perfil do usuário por ID do usuário. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Consulta de informações de perfil de usuário por segmento. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Mescla dois usuários existentes um no outro. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Altere o ID externo de um usuário existente. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Remova o ID externo de um usuário existente. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Atualize um alias de um usuário existente. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Faça uma consulta para obter informações do perfil do usuário no grupo de controle global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab Email %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Faça uma consulta para obter endereços de e-mail com cancelamento de inscrição.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Altere o status do endereço de e-mail. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Faça uma consulta para obter endereços de e-mail com hard bounce. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Remova endereços de e-mail da sua lista de hard bounce. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Remova endereços de e-mail da sua lista de spam. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Endereços de e-mail da lista de bloqueio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Envie uma mensagem imediata para usuários específicos. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Agende uma mensagem para ser enviada em um horário específico. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Atualize uma mensagem agendada. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Exclua uma mensagem agendada. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Faça uma consulta para obter todas as mensagens de divulgação agendadas. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Atualizar uma atividade do iOS Live. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campaigns %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Disparar o envio de uma campanha existente. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Programe um envio futuro de uma campanha com entrega disparada por API. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Atualize uma campanha programada com entrega disparada por API. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Exclua uma campanha programada com entrega disparada por API. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Consulta de uma lista de campanhas. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Consulta para análise de dados de campanha em um intervalo de tempo. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Consulta de detalhes de uma campanha específica. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Faça uma consulta para obter análise de dados de envios de mensagens ao longo de um período. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Criar ID de envio para rastreamento de mensagens. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Faça uma consulta para obter informações do URL de uma variação de mensagem específica dentro de uma campanha. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Permite a capacidade de enviar mensagens transacionais usando o endpoint de mensagens transacionais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Dispare o envio de um canva existente. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Agende um envio futuro de um canva com entrega disparada pela API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Atualize um canva agendado com entrega disparada pela API. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Exclua um canva agendado com entrega disparada pela API. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Faça uma consulta para obter uma lista de canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Faça uma consulta para obter análise de dados do canva em um período. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Faça uma consulta para obter informações de um canva específico. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Faça uma consulta para obter resultados consolidados sobre a análise de dados do canva em um período. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Consulta de detalhes de URL de uma variação de mensagem específica em uma etapa do Canva. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segments %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Consulta de uma lista de segmentos. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Consulta para análise de dados de segmento em um intervalo de tempo. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Consulta de detalhes de um segmento específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Purchases %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Faça uma consulta para obter uma lista de produtos comprados em seu app. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Faça uma consulta para obter o valor total gasto por dia em seu app em um período. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Consulte o número total de compras por dia em seu app em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Events %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Consulta de uma lista de eventos personalizados. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Consulte as ocorrências de um evento personalizado em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Faça uma consulta para obter a quantidade de sessões por dia em um período. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Faça uma consulta para obter a quantidade de usuários ativos únicos por dia em um período. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Faça uma consulta para obter o total de usuários ativos únicos em um intervalo de 30 dias ao longo de um período. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Faça uma consulta para obter a quantidade de usuários novos por dia em um período. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Faça uma consulta para obter a quantidade de desinstalações de app por dia em um período. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Crie um novo modelo de e-mail no dashboard. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Faça uma consulta para obter informações de um modelo específico. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Consulte uma lista de modelos de e-mail. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Atualizar um modelo de e-mail armazenado no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Permissão | Descrição |
|---|---|---|
| `sso.saml.login` | Configure o login iniciado pelo provedor de identidade. Para saber mais, consulte o [login iniciado pelo prestador de serviço (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content Blocks %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Faça uma consulta para obter informações de um modelo específico. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Faça uma consulta para obter uma lista de blocos de conteúdo. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Crie um novo bloco de conteúdo no dashboard. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Atualize um bloco de conteúdo existente no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Preference Center %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Obtenha uma Central de Preferências. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Liste as Centrais de Preferências. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Crie ou atualize uma Central de Preferências. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Obtenha o link de uma Central de Preferências para um usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Subscription %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Definir o status do grupo de inscrições. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Obtenha o status do grupo de inscrições. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Obtenha o status dos grupos de inscrições nos quais usuários específicos estão explicitamente inscritos e cancelaram a inscrição. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Faça uma consulta para obter números de telefones inválidos. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Remova a sinalização de número de telefone inválido de usuários. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogs %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Adicione vários itens a um catálogo existente. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Atualize vários itens de um catálogo existente. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Exclua vários itens de um catálogo existente. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Obtenha um único item de um catálogo existente. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Atualize um único item de um catálogo existente. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Crie um item único em um catálogo existente. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Exclua um item único de um catálogo existente. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Substitua um item de um catálogo existente. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Criar um catálogo. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Obter uma lista de catálogos |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Excluir um catálogo. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Obtenha uma prévia de itens de um catálogo existente. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Substituir itens em um catálogo existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK Authentication %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Crie uma nova chave de autenticação do SDK para seu aplicativo. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | Marque uma chave de autenticação do SDK como a chave primária do seu aplicativo. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Exclua uma chave de autenticação do SDK para seu aplicativo. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obtenha todas as chaves de autenticação do SDK para seu aplicativo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Gerenciamento de chaves da API REST

Você pode visualizar detalhes ou excluir chaves de API REST existentes na guia **Configurações** > **APIs e identificadores** > **Chaves de API**. Observe que as chaves da API REST não podem ser editadas depois de criadas.

A guia **Chaves de API** inclui as seguintes informações para cada chave:

| Campo        | Descrição                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nome da chave de API | O nome dado à chave na criação.                                                                            |
| Identificador   | A chave de API.                                                                                                        |
| Criado por   | O endereço de e-mail do usuário que criou a chave. Esse campo será exibido como "N/A" para chaves criadas antes de junho de 2023. |
| Data de criação | A data em que essa chave foi criada.                                                                                      |
| Último envio    | A data em que essa chave foi usada pela última vez. Esse campo será exibido como "N/A" para chaves que nunca foram usadas.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para visualizar os detalhes de uma chave de API, passe o mouse sobre a chave e selecione <i class="fa-solid fa-eye" alt="View"></i> **View**. Isso inclui todas as permissões que essa chave tem, IPs na lista de permissões (se houver) e se essa chave foi aceita na lista de permissões de IP do Braze.

![A lista de permissões da chave de API no dashboard do Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Note que, ao [excluir um usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/), as chaves de API associadas que o usuário criou não serão excluídas. Para excluir uma chave, passe o mouse sobre a chave e selecione <i class="fa-solid fa-trash-can" alt="Delete"></i> **Delete**.

![Uma chave de API chamada "Last Seen" com o ícone de lixeira destacado, mostrando "Delete".]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Segurança da chave da API REST

As chaves de API são usadas para autenticar uma chamada de API. Ao criar uma nova chave da API REST, você precisa dar a ela acesso a endpoints específicos. Ao atribuir permissões específicas a uma chave de API, você pode limitar exatamente quais chamadas uma chave de API pode autenticar.

Como as chaves da API REST permitem o acesso a endpoints da API REST potencialmente confidenciais, proteja essas chaves e compartilhe-as apenas com parceiros confiáveis. Elas nunca devem ser expostas publicamente. Por exemplo, não use essa chave para fazer chamadas AJAX em seu site nem a exponha de qualquer outra forma pública.

Uma boa prática de segurança é atribuir a um usuário apenas o acesso necessário para concluir seu trabalho: esse princípio também pode ser aplicado às chaves de API atribuindo permissões a cada chave. Essas permissões proporcionam mais segurança e controle sobre as diferentes áreas da sua conta.

{% alert warning %}
Como as chaves da API REST permitem o acesso a endpoints da API REST potencialmente confidenciais, certifique-se de que elas sejam armazenadas e usadas com segurança. Por exemplo, não use essa chave para fazer chamadas AJAX em seu site nem a exponha de qualquer outra forma pública.
{% endalert %}

Se ocorrer a exposição acidental de uma chave, ela poderá ser excluída do console de desenvolvedor. Para obter ajuda com esse processo, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

### Lista de permissões de IP da API

Para maior segurança, você pode especificar uma lista de endereços IP e sub-redes que têm permissão para fazer solicitações de API REST para uma determinada chave de API REST. Isso é chamado de lista de permissões. Para permitir endereços IP ou sub-redes específicos, adicione-os à seção **Lista de permissões de IPs** ao criar uma nova chave da API REST:

![Opção para permitir a lista de IPs ao criar uma chave de API.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Se você não especificar nenhum, as solicitações poderão ser enviadas de qualquer endereço IP.

{% alert tip %}
Como criar um webhook Braze-to-Braze e usar o allowlisting? Confira nossa lista de [IPs para lista de permissões]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Recursos adicionais

### Biblioteca de cliente Ruby

Se estiver implementando a Braze usando Ruby, poderá usar nossa [biblioteca de cliente Ruby](https://github.com/braze-inc/braze-api-client-ruby) para reduzir o tempo de importação de dados. Uma biblioteca de cliente é uma coleção de códigos específicos de uma linguagem de programação - neste caso, Ruby - que facilita o uso de uma API.

A biblioteca do cliente Ruby é compatível com os [endpoints do usuário]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Essa biblioteca de clientes está atualmente na versão beta. Quer nos ajudar a melhorar esta biblioteca? Envie-nos seu feedback em [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

