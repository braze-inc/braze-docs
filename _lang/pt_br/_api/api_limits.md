---
nav_title: Limites de taxa
article_title: Limites de taxa da API
page_order: 4.5
description: "Este artigo de referência aborda os limites de taxa da API para a infraestrutura da API da Braze."
page_type: reference

---

# Limites de taxa

> A infraestrutura da API da Braze foi projetada para lidar com grandes volumes de dados de nossa base de clientes. Para isso, aplicamos limites de taxa de API por espaço de trabalho.

Um limite de taxa é o número de solicitações que a API pode receber em um determinado período de tempo. Muitos incidentes de negação de serviço baseados em carga em grandes sistemas não são intencionais — causados por erros no software ou nas configurações — e não por ataques mal-intencionados. Os limites de taxa verificam se esses erros não privam nossos clientes dos recursos da API da Braze. Se muitas solicitações forem enviadas em um determinado período de tempo, você poderá ver respostas de erro com um código de status `429`, o que indica que o limite de taxa foi atingido.

{% alert warning %}
Os limites de taxa da API estão sujeitos a alterações, dependendo do uso adequado de nosso sistema. Incentivamos limites sensatos ao fazer uma chamada à API para evitar danos ou uso indevido.
{% endalert %}

## Limites de taxa por tipo de solicitação

Consulte a seguir os limites de taxa padrão da API para diferentes tipos de solicitações. Esses limites padrão podem ser aumentados mediante solicitação. Entre em contato com seu gerente de sucesso do cliente para saber mais.

### Solicitações com diferentes limites de taxa

| Tipo de solicitação                                                                                                                                                                                                                                           | Limite de taxa padrão da API                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **Solicitações:** 3.000 solicitações a cada três segundos.<br><br>**Lotes:** Até 75 objetos no total combinados entre `attributes`, `events` e `purchases` por solicitação de API. Clientes com limites de taxa legados podem incluir até 75 objetos por array de forma independente. Para saber mais, consulte [Agrupamento de solicitações de rastreamento de usuários](#batch-user-track).<br><br>**Limites para Usuários Ativos Mensais CY 24-25, MAU Universal, MAU Web e MAU Celular:** veja [orientações sobre limites aqui]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **Se você fez a integração em 22 de agosto de 2024 ou após essa data:** 250 solicitações por minuto. <br><br> **Se você fez a integração antes de 22 de agosto de 2024:** 2.500 solicitações por minuto.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 20.000 solicitações por minuto, compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1.000 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1.000 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1.000 solicitações por hora, compartilhadas com o endpoint `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1.000 solicitações por hora, compartilhadas com o endpoint `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 50.000 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | Para chamadas de transmissão (quando direcionando amplamente segmentos ou filtros ou um público conectado), 250 solicitações por minuto em todos os públicos, **e** 10 solicitações por minuto por [público único]({{site.baseurl}}/api/api_limits/#what-counts-as-the-same-unique-audience) (o limite que for atingido primeiro).<br><br>Caso contrário, ao direcionar destinatários individuais, a solicitação está incluída nas 250.000 solicitações por hora do [limite de taxa compartilhado]({{site.baseurl}}/api/api_limits/#requests-with-shared-rate-limits).                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 100 solicitações por dia.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 5.000 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1.000 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 10 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 50 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 16.000 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 50 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 solicitações por minuto compartilhadas entre os endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 5.000 solicitações por dia, por empresa, compartilhadas entre os endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 50 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 20 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 100 solicitações por minuto.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Solicitações com limites de taxa compartilhados

As seguintes solicitações têm um limite de taxa de 250.000 solicitações por hora, compartilhado entre elas.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) (apenas para chamadas não de transmissão — aquelas que especificam `external_user_ids` ou `aliases`)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) (apenas para chamadas não de transmissão)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) (apenas para chamadas não de transmissão)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

### O que conta como o mesmo público único? {#what-counts-as-the-same-unique-audience}

Isso se aplica aos seguintes três endpoints: [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) e [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/).

Para esses endpoints, as solicitações de transmissão são consideradas direcionadas ao mesmo público único quando todos os seguintes critérios correspondem:

- A campanha ou Canvas sendo acionado (o `campaign_id` ou `canvas_id` na sua solicitação de API, se especificado)
- O público sendo direcionado (os segmentos ou filtros, ou para campanhas de API, o `segment_id` na sua solicitação de API)
- Os filtros de público conectado (o objeto `audience` na sua solicitação de API, se especificado)

Cada combinação única desses atributos conta como um público distinto, portanto, o limite de taxa adicional para cada público único se aplica a cada combinação de forma independente.

## Agrupamento de solicitações de API

As APIs da Braze foram criadas para oferecer suporte a lotes. Com os lotes, a Braze pode receber o máximo de dados possível em uma única chamada de API para que você não precise fazer muitas chamadas de API. É mais eficiente para a Braze processar dados em lotes do que processar dados em uma chamada de cada vez. Por exemplo, lidar com 1.000 chamadas de API em lote requer menos recursos do que lidar com 75.000 chamadas individuais. O agrupamento é extremamente importante para qualquer aplicativo que possa necessitar de mais de 75.000 chamadas por hora.

{% alert note %}
Os aumentos do limite de taxa da API REST são considerados com base na necessidade dos clientes que estão usando os recursos de lote da API.
{% endalert %}

### Agrupando solicitações para o endpoint de rastreamento de usuários {#batch-user-track}

Cada solicitação `/users/track` pode conter até 75 objetos no total combinados entre `attributes`, `events` e `purchases`. Cada objeto pode atualizar um usuário. Um único perfil de usuário pode ser atualizado por vários objetos.

{% details Limites de taxa legados %}
Para clientes com limites de taxa legados, cada array (`attributes`, `events` e `purchases`) pode conter até 75 objetos de forma independente, para um máximo combinado de até 225 objetos por solicitação.
{% enddetails %}

Para saber mais sobre os limites de taxa do `/users/track`, consulte [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

As solicitações feitas a esse endpoint geralmente começarão a ser processadas nesta ordem:

1. Atributos
2. Eventos
3. Compras

### Agrupando solicitações de endpoints de envio de mensagens

Uma única solicitação para os [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) pode alcançar qualquer um dos seguintes:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagens individuais
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Usuários que correspondem a filtros de público adicionais de qualquer tamanho, definidos na solicitação como um objeto de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/)

### Exemplo de solicitação em lote

O exemplo a seguir usa `external_id` para fazer uma chamada de API para e-mail e SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Monitoramento dos seus limites de taxa

Toda solicitação de API enviada à Braze retorna as seguintes informações nos cabeçalhos de resposta:

| Nome do cabeçalho             | Descrição                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | O número máximo de solicitações que você pode fazer em um intervalo especificado (seu limite de taxa). |
| `X-RateLimit-Remaining` | O número de solicitações restantes na janela do limite de taxa atual.                          |
| `X-RateLimit-Reset`     | A hora em que a janela do limite de taxa atual é redefinida em segundos de epoch UTC.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Essas informações são incluídas intencionalmente no cabeçalho da resposta à solicitação da API, e não no dashboard da Braze. Isso permite que seu sistema reaja melhor em tempo real à medida que você interage com nossa API. Por exemplo, se o valor de `X-RateLimit-Remaining` cair abaixo de um determinado limite, talvez você queira diminuir a velocidade de envio para garantir que todos os e-mails de transação sejam enviados. Ou, se chegar a zero, talvez você queira pausar todos os envios até que passe o tempo especificado em `X-RateLimit-Reset`.

{% alert note %}
Os cabeçalhos HTTP serão retornados com todos os caracteres em minúsculas. Esse comportamento está alinhado com o protocolo HTTP/2, que exige que todos os nomes de campos de cabeçalho sejam minúsculos. Isso difere do HTTP/1.X, em que os nomes de cabeçalho não diferenciavam maiúsculas de minúsculas, mas eram comumente escritos em várias capitalizações.
{% endalert %}

Se tiver dúvidas sobre os limites da API, entre em contato com o gerente de sucesso do cliente ou abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

{% alert tip %}
Você pode usar o [dashboard de uso da API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) para visualizar e comparar o tráfego de entrada em relação aos seus limites de taxa.
{% endalert %}

### Postergação ideal entre endpoints

{% alert note %}
Recomendamos que você permita uma postergação de 5 minutos entre chamadas consecutivas ao endpoint para minimizar erros.
{% endalert %}

Compreender a postergação ideal entre endpoints é crucial ao fazer chamadas consecutivas para a API da Braze. Os problemas surgem quando os endpoints dependem do processamento bem-sucedido de outros endpoints e, se as chamadas forem feitas muito cedo, podem gerar erros. Por exemplo, se você estiver atribuindo aos usuários um alias por meio do nosso endpoint `/user/alias/new` e, em seguida, usando esse alias para enviar um evento personalizado por meio do nosso endpoint `/users/track`, quanto tempo deve esperar?

Em condições normais, o tempo para a eventual consistência dos nossos dados ocorrer é de 10-100ms (1/10 de segundo). No entanto, em alguns casos, pode levar mais tempo para que essa consistência ocorra, portanto, recomendamos que você permita uma postergação de 5 minutos entre as chamadas subsequentes para minimizar a probabilidade de erro.

### Redefinição do limite de taxa

Os limites de taxa são redefinidos na hora cheia, e não em uma janela contínua. Por exemplo, se o limite for de 250.000 solicitações por hora, você pode fazer 50.000 solicitações entre 22h00 e 22h59 e outras 250.000 solicitações entre 23h00 e 23h59, porque o contador é redefinido no início de cada hora.