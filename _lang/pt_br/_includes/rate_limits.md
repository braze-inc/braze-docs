<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Aplicamos o limite de taxa padrão da Braze de 250.000 solicitações por hora a esse endpoint, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por dia, por empresa. Esse limite de taxa é compartilhado com os endpoints `/scim/v2/Users/` GET, DELETE e POST, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por dia, por empresa. Esse limite de taxa é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por dia, por empresa. Esse limite de taxa é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e POST, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por dia, por empresa. Esse limite de taxa é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e DELETE, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por dia, por empresa. Esse limite de taxa é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Aplicamos um limite de taxa de 1.000 solicitações por minuto a esse endpoint, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
A Braze aplica um limite de velocidade base de 3.000 solicitações a cada três segundos para esse endpoint. Cada solicitação `/users/track` pode conter até 75 objetos no total, combinados entre `attributes`, `events` e `purchases`. Cada objeto pode atualizar um usuário. Um único perfil de usuário pode ser atualizado por múltiplos objetos.

Para clientes que adquiriram Monthly Active Users CY 24-25, Universal MAU, Web MAU ou Mobile MAU, limites de taxa adicionais se aplicam. Para saber mais, consulte [Limites do Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau).

{% details Limites de taxa legados %}
Para clientes com limites de taxa legados, cada solicitação `/users/track` pode conter até 75 objetos de atributo, 75 objetos de evento e 75 objetos de compra. Cada objeto pode atualizar um usuário, para um máximo combinado de até 225 objetos por solicitação. Um único perfil de usuário pode ser atualizado por múltiplos objetos.
{% enddetails %}

Para saber mais, consulte [Limites de taxa da API]({{site.baseurl}}/api/api_limits/). Entre em contato com seu gerente de sucesso do cliente para solicitar um aumento.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Se sua integração com a Braze ocorreu em 22 de agosto de 2024 ou após essa data, esse endpoint tem um limite de taxa de 250 solicitações por minuto, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

Você também pode aumentar o limite de taxa desse endpoint para 40 solicitações por segundo atendendo aos seguintes requisitos:

- Seu espaço de trabalho tem o limite de taxa padrão (250 solicitações por minuto) ativado. Entre em contato com seu gerente de conta da Braze para mais assistência na remoção de qualquer limite de taxa pré-existente que você possa ter.
- Sua solicitação inclui o parâmetro `fields_to_export` para listar todos os campos que você deseja receber.

{% alert important %}
Se você incluir `canvases_received` ou `campaigns_received` no parâmetro `fields_to_export`, sua solicitação não será elegível para o limite de taxa mais rápido. Recomendamos incluir esses campos apenas em sua solicitação se você tiver um caso de uso específico para eles.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Aplicamos um limite de taxa compartilhado de 20.000 solicitações por minuto para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/users/alias/new`, `/users/identify`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Aplicamos um limite de taxa compartilhado de 20.000 solicitações por minuto para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/users/delete`, `/users/identify`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Aplicamos um limite de taxa compartilhado de 20.000 solicitações por minuto para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/identify` e `/users/merge`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Aplicamos um limite de taxa compartilhado de 20.000 solicitações por minuto para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Aplicamos um limite de taxa compartilhado de 20.000 solicitações por minuto para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/identify` e `/users/alias/update`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Aplicamos um limite de taxa compartilhado de 1.000 solicitações por hora para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/events`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "events" %}
Aplicamos um limite de taxa compartilhado de 1.000 solicitações por hora para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/custom_attributes`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Aplicamos um limite de taxa compartilhado de 1.000 solicitações por hora para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/custom_attributes`, `/events` e `/purchases/product_list`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Aplicamos um limite de taxa compartilhado de 1.000 solicitações por hora para esse endpoint. Esse limite de taxa é compartilhado com os endpoints `/custom_attributes`, `/events` e `/events/list`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Ao usar filtros de público conectado em sua solicitação, aplicamos um limite de taxa de 250 solicitações por minuto para esse endpoint. Caso contrário, se estiver especificando um `external_id`, esse endpoint terá um limite de taxa padrão de 250.000 solicitações por hora compartilhado entre `/messages/send`, `/campaigns/trigger/send` e `/canvas/trigger/send`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

Os endpoints da Braze suportam agrupamento de solicitações da API. Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de público conectado

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
O endpoint `/transactional/v1/campaigns/{campaign_id}/send` é um endpoint pago em unidades por hora (por exemplo, 50.000 por hora, dependendo do seu pacote). Não há limite de taxa separado por endpoint: você pode enviar além do seu volume alocado, mas apenas o volume alocado é coberto pelo SLA. As solicitações para esse endpoint contam para o seu [limite geral de taxa da API externa]({{site.baseurl}}/api/api_limits/). Se você exceder esse limite (por exemplo, 250.000 solicitações por hora em todos os endpoints), a Braze retorna 429 e as solicitações são limitadas. A contagem do volume transacional é redefinida a cada hora, então após uma hora, outra alocação fica disponível. Dentro do volume coberto pelo SLA, 99,9% dos e-mails serão enviados em menos de um minuto.

<!---POST /preference_center/v1 and PUT /preference_center/v1/{preferenceCenterExternalID}-->
{% elsif include.endpoint == "post or put preference center" %}
Esse endpoint tem um limite de taxa de 10 solicitações por minuto, por espaço de trabalho, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---GET /preference_center/v1-->
{% elsif include.endpoint == "get preference center" %}
Esse endpoint tem um limite de taxa de 1.000 solicitações por minuto, por espaço de trabalho, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Você pode criar até 100 identificadores de envio personalizados por dia usando esse endpoint para um determinado espaço de trabalho. Cada combinação de `send_id` e `campaign_id` que você criar contará para o seu limite diário. Os cabeçalhos de resposta para qualquer solicitação válida incluem o status atual do limite de taxa. Consulte [Limites de taxa da API]({{site.baseurl}}/api/api_limits/) para mais detalhes.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Esse endpoint tem um limite de taxa de 5.000 solicitações por minuto compartilhado entre os endpoints `/subscription/status/set` e `/v2/subscription/status/set`, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Esse endpoint tem um limite de taxa de 50 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Esse endpoint tem um limite de taxa de 20 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Esse endpoint tem um limite de taxa de 100 solicitações por minuto.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits/#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

{% if include.category == "send messages endpoints" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits/#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos, cada um com parâmetros de mensagem individuais
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Esse endpoint tem um limite de taxa de 250.000 solicitações por minuto.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits/#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto de [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Esse endpoint tem um limite de taxa compartilhado de 16.000 solicitações por minuto entre todos os endpoints assíncronos de itens de catálogo, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Esse endpoint tem um limite de taxa compartilhado de 50 solicitações por minuto entre todos os endpoints síncronos de itens de catálogo, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Esse endpoint tem um limite de taxa compartilhado de 50 solicitações por minuto entre todos os endpoints de catálogo síncronos, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Esse endpoint tem um limite de taxa compartilhado de 50 solicitações por minuto entre todos os endpoints assíncronos de campos de catálogo e seleções, conforme documentado em [Limites de taxa da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Esse endpoint tem um limite de taxa de 50.000 solicitações por minuto.

{% endif %}