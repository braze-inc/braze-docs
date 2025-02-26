
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Aplicamos o limite de frequência padrão da Braze de 250.000 solicitações por hora a esse endpoint, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "alterar usuário no dashboard" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "procurar usuário do dashboard" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "excluir usuário do dashboard" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "criar usuário do dashboard" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET e DELETE, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "procurar o e-mail do usuário do dashboard" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por dia, por empresa. Esse limite de frequência é compartilhado com os endpoints `/scim/v2/Users/` PUT, GET, DELETE e POST, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "migração de id externa" %}
Aplicamos um limite de frequência de 1.000 solicitações por minuto a esse endpoint, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "rastreamento de usuários" %}
A partir de 28 de outubro de 2024, aplicaremos um limite de velocidade básico de 3.000 solicitações por três segundos a esse endpoint para todos os clientes. Cada solicitação `/users/track` pode conter até 75 objetos de evento, 75 objetos de atribuição e 75 objetos de compra. Cada objeto (evento, atributo e vetores de compra) pode atualizar um usuário. No total, isso significa que um máximo de 225 usuários pode ser atualizado em uma única chamada. Além disso, um único perfil de usuário pode ser atualizado por vários objetos.

Limites diferentes se aplicam aos clientes que adquiriram **Usuários ativos mensais - CY 24-25**. Para obter detalhes sobre esses limites, consulte [Usuários ativos mensais - limites do CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25).

Consulte nossa página sobre [limites de frequência da API]({{site.baseurl}}/api/api_limits/) para obter detalhes e entre em contato com o gerente de sucesso do cliente se precisar aumentar seu limite.

<!---/users/export/ids-->

{% elsif include.endpoint == "IDs de exportação dos usuários" %}
Se sua integração com a Braze ocorreu em 22 de agosto de 2024 ou após essa data, esse endpoint tem um limite de frequência de 250 solicitações por minuto, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/delete-->

{% elsif include.endpoint == "exclusão de usuários" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/alias/new`, `/users/identify` e `/users/merge`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "usuários alias new" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/identify`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "atualização de alias de usuários" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/identify`, `/users/merge` e `/users/alias/new`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "atualização de alias de usuários" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/identify` e `/users/merge`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/merge` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "fusão de usuários" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 20.000 solicitações por minuto a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/users/delete`, `/users/alias/new`, `/users/identify` e `/users/alias/update`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/events`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "eventos" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events/list` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "lista de eventos" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events` e `/purchases/product_list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "lista de produtos comprados" %}
Para clientes que integraram a Braze a partir de 16 de setembro de 2021, aplicamos um limite de frequência compartilhada de 1.000 solicitações por hora a esse endpoint. Esse limite de frequência é compartilhado com os endpoints `/custom_attributes`, `/events` e `/events/list`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "enviar endpoints" %}
Ao especificar um segmento ou público conectado em sua solicitação, aplicamos um limite de frequência de 250 solicitações por minuto a esse endpoint. Caso contrário, se estiver especificando um `external_id`, esse endpoint terá um limite de frequência padrão de 250.000 solicitações por hora compartilhadas entre `/messages/send`, `/campaigns/trigger/send` e `/canvas/trigger/send`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "e-mail de transação" %}
Os e-mails de transação da Braze não estão sujeitos a um limite de frequência. Dependendo do pacote escolhido, um número definido de e-mails de transação é coberto por hora pelo SLA. As solicitações que excederem essa taxa ainda serão enviadas, mas não serão cobertas pelo SLA. 99,9% dos e-mails serão enviados em menos de um minuto.

<!---/sends/id/create-->

{% elsif include.endpoint == "envia id create" %}
O número máximo diário de identificadores de envio personalizados que podem ser criados por meio desse endpoint é 100 para um determinado espaço de trabalho. Cada combinação de `send_id` e `campaign_id` que você criar contará para o seu limite diário. Os cabeçalhos de resposta de qualquer solicitação válida incluem o status do limite de frequência atual; consulte [Limites de frequência da API]({{site.baseurl}}/api/api_limits/) para obter detalhes.

<!---/subscription/status/set-->
{% elsif include.endpoint == "conjunto de status da inscrição" %}
Esse endpoint tem um limite de frequência de 5.000 solicitações por minuto compartilhado entre os endpoints `/subscription/status/set` e `/v2/subscription/status/set`, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "integrações de listas cdi" %}
Esse endpoint tem um limite de frequência de 50 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "sincronização de tarefas cdi" %}
Esse endpoint tem um limite de frequência de 20 solicitações por minuto.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "Status de sincronização de trabalho do cdi" %}
Esse endpoint tem um limite de frequência de 100 solicitações por minuto.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "endpoints de mensagens" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits/#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 sites específicos `external_ids`, cada um com parâmetros de mensagens individuais
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto [de público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "endpoint de envio de mensagens" %}

Os endpoints da Braze aceitam [solicitações de API em lote]({{site.baseurl}}/api/api_limits/#batching-api-requests). Uma única solicitação para os endpoints de envio de mensagens pode alcançar qualquer um dos seguintes itens:

- Até 50 `external_ids` específicos
- Um segmento de qualquer tamanho criado no dashboard da Braze, especificado por seu `segment_id`
- Um segmento de público de qualquer tamanho, definido na solicitação como um objeto [de público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

{% endif %}

{% if include.endpoint == "item de catálogo assíncrono" %}

Esse endpoint tem um limite de frequência compartilhado de 16.000 solicitações por minuto entre todos os endpoints assíncronos de itens de catálogo, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "item de catálogo síncrono" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os endpoints de itens de catálogo síncronos, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "catálogo síncrono" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os endpoints de catálogo síncrono, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "campos de catálogo assíncrono" ou include.endpoint == "seleções de catálogo assíncronos" %}

Esse endpoint tem um limite de frequência compartilhado de 50 solicitações por minuto entre todos os campos de catálogo assíncronos e endpoints de seleções, conforme documentado em [Limites de frequência da API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "análise de dados de campanhas de exportação" %}

Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto.

{% endif %}
