---
nav_title: Limites de frequência
article_title: Limites de frequência da API
page_order: 4.5
description: "Este artigo de referência aborda os limites de frequência da API para a infraestrutura da API da Braze."
page_type: reference

---

# Limites de frequência

> A infraestrutura da API da Braze foi projetada para lidar com grandes volumes de dados de nossa base de clientes. Para isso, aplicamos limites de frequência de API por espaço de trabalho.

Um limite de frequência é o número de solicitações que a API pode receber em um determinado período de tempo. Muitos incidentes de negação de serviço baseados em carga em grandes sistemas não são intencionais - causados por erros no software ou nas configurações - e não por ataques mal-intencionados. Os limites de frequência verificam se esses erros não privam nossos clientes dos recursos da API do Braze. Se muitas solicitações forem enviadas em um determinado período de tempo, você poderá ver respostas de erro com um código de status `429`, o que indica que o limite de frequência foi atingido.

{% alert warning %}
Os limites de frequência da API estão sujeitos a alterações, dependendo do uso adequado de nosso sistema. Incentivamos limites sensatos ao fazer uma chamada à API para evitar danos ou uso indevido.
{% endalert %}

## Limites de frequência por tipo de solicitação

A tabela a seguir lista os limites de frequência padrão da API para diferentes tipos de solicitação. Esses limites padrão podem ser aumentados mediante solicitação. Entre em contato com seu gerente de sucesso do cliente para saber mais.

{% alert note %}
As solicitações não listadas nesta tabela compartilham um limite de frequência padrão total de 250.000 solicitações por hora.
{% endalert %}

| Tipo de solicitação                                                                                                                                                                                                                                           | Limite de frequência padrão da API                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`/users/track`][10]                                                                                                                                                                                                                                   | **Solicitações:** 3.000 solicitações a cada três segundos.<br><br>**Lotes:** 75 eventos, 75 compras e 75 atribuições por solicitação de API. Para obter mais informações, consulte [Agrupamento de solicitações de rastreamento do usuário](#batch-user-track).<br><br>**Limites para Usuários Ativos Mensais CY 24-25:** consulte [Limites de Usuários Ativos Mensais CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **Se você embarcou em 22 de agosto de 2024 ou após essa data:** 250 solicitações por minuto. <br><br> **Se sua integração foi feita antes de 22 de agosto de 2024:** 2.500 solicitações por minuto.                                                                                                                                                                   |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 20.000 solicitações por minuto, compartilhadas entre os endpoints.                                                                                                                                  |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1.000 solicitações por minuto.                                                                                                                                                                 |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1.000 solicitações por minuto.                                                                                                                                                                 |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1.000 solicitações por hora, compartilhadas com o ponto de extremidade `/purchases/product_list`.                                                                                                               |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1.000 solicitações por hora, compartilhadas com o ponto de extremidade `/events/list`.                                                                                                                          |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 50.000 solicitações por minuto.                                                                                                                                                                |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | 250 solicitações por minuto para chamadas de transmissão (ao especificar apenas um segmento ou público conectado). Caso contrário, 250.000 solicitações por hora compartilhadas entre os endpoints.                     |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 100 solicitações por dia.                                                                                                                                                                      |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 5.000 solicitações por minuto.                                                                                                                                                                 |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | 1.000 solicitações por minuto, por espaço de trabalho.                                                                                                                                                  |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | 10 solicitações por minuto, por espaço de trabalho.                                                                                                                                                     |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 50 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                       |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 16.000 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                   |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 50 solicitações por minuto compartilhadas entre os endpoints.                                                                                                                                       |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 5.000 solicitações por dia, por empresa, compartilhadas entre os endpoints.                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## Agrupamento de solicitações de API

As APIs da Braze foram criadas para oferecer suporte a lotes. Com os lotes, a Braze pode receber o máximo de dados possível em uma única chamada de API para que você não precise fazer muitas chamadas de API. É mais eficiente para a Braze processar dados em lotes do que processar dados em uma chamada de cada vez. Por exemplo, lidar com 1.000 chamadas de API em lote requer menos recursos do que lidar com 75.000 chamadas individuais. O agrupamento é extremamente importante para qualquer aplicativo que possa necessitar de mais de 75.000 chamadas por hora.

{% alert note %}
Os aumentos do limite de frequência da API REST são considerados com base na necessidade dos clientes que estão usando os recursos em lote da API.
{% endalert %}

### Agrupamento de solicitações de rastreamento do usuário {#batch-user-track}

Cada solicitação `/users/track` pode conter até 75 objetos de evento, 75 objetos de atribuição e 75 objetos de compra. Cada objeto (evento, atributo e vetores de compra) pode atualizar um usuário. No total, isso significa que um máximo de 225 usuários pode ser atualizado em uma única chamada. Além disso, um único perfil de usuário pode ser atualizado por vários objetos.

As solicitações feitas a esse ponto de extremidade geralmente começarão a ser processadas nessa ordem:

1. Atributos
2. Eventos
3. Compras

### Envio de mensagens em lote para solicitações de endpoint

Uma única solicitação para os [pontos de extremidade de envio de mensagens][1] pode alcançar qualquer um dos seguintes:

- Até 50 sites específicos `external_ids`, cada um com parâmetros de mensagens individuais
- Um segmento de qualquer tamanho criado no dashboard do Braze, especificado por seu `segment_id`
- Usuários que correspondem a filtros de público adicionais de qualquer tamanho, definidos na solicitação como um objeto [de público conectado][2] 

### Exemplo de solicitação de lote

O exemplo a seguir usa `external_id` para fazer uma chamada de API para envio de e-mail e SMS.

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

## Monitoramento de seus limites de frequência

Toda solicitação de API enviada à Braze retorna as seguintes informações nos cabeçalhos de resposta:

| Nome do cabeçalho             | Descrição                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | O número máximo de solicitações que você pode fazer em um intervalo especificado (seu limite de frequência). |
| `X-RateLimit-Remaining` | O número de solicitações restantes na janela do limite de frequência atual.                          |
| `X-RateLimit-Reset`     | A hora em que a janela do limite de frequência atual é redefinida em segundos de epoch UTC.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Essas informações são incluídas intencionalmente no cabeçalho da resposta à solicitação da API, e não no dashboard da Braze. Isso permite que seu sistema reaja melhor em tempo real à medida que você interage com nossa API. Por exemplo, se o valor de `X-RateLimit-Remaining` cair abaixo de um determinado limite, talvez você queira diminuir a velocidade de envio para garantir que todos os e-mails de transação sejam enviados. Ou, se chegar a zero, talvez você queira pausar todos os envios até que passe o tempo especificado em `X-RateLimit-Reset`.

{% alert note %}
Os cabeçalhos HTTP serão retornados com todos os caracteres em minúsculas. Esse comportamento está alinhado com o protocolo HTTP/2, que exige que todos os nomes de campos de cabeçalho sejam minúsculos. Isso difere do HTTP/1.X, em que os nomes de cabeçalho não diferenciavam maiúsculas de minúsculas, mas eram comumente escritos em várias maiúsculas.
{% endalert %}

Se tiver dúvidas sobre os limites da API, entre em contato com o gerente de sucesso do cliente ou abra um [tíquete de suporte][support].

### Postergação ideal entre os pontos finais

{% alert note %}
Recomendamos que você permita uma postergação de 5 minutos entre chamadas consecutivas ao endpoint para minimizar erros.
{% endalert %}

Compreender a postergação ideal entre os pontos de extremidade é crucial ao fazer chamadas consecutivas para a API do Braze. Os problemas surgem quando os endpoints dependem do processamento bem-sucedido de outros endpoints e, se as chamadas forem feitas muito cedo, podem gerar erros. Por exemplo, se estiver atribuindo aos usuários um alias por meio do nosso endpoint `/user/alias/new` e, em seguida, usar esse alias para enviar um evento personalizado por meio do nosso endpoint `/users/track`, quanto tempo deve esperar?

Em condições normais, o tempo para que a consistência eventual de nossos dados ocorra é de 10 a 100 ms (1/10 de segundo). No entanto, em alguns casos, pode levar mais tempo para que essa consistência ocorra, portanto, recomendamos que você permita uma postergação de 5 minutos entre as chamadas subsequentes para minimizar a probabilidade de erro.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[17.3]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
[46]: {{site.baseurl}}/api/endpoints/cdi/get_integration_list/
[47]: {{site.baseurl}}/api/endpoints/cdi/job_sync/
[48]: {{site.baseurl}}/api/endpoints/cdi/job_sync_status/
