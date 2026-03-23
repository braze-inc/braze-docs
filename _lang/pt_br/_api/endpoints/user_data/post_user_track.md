---
nav_title: "POST: Criar e atualizar usuários"
article_title: "POST: Criar e atualizar usuários"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para rastreamento de usuários."
toc_headers: h2
---
{% api %}
# Criar e atualizar usuários
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Use esse endpoint para registrar eventos personalizados e compras, além de atualizar atributos do perfil de usuário.

{% alert note %}
A Braze processa os dados passados por meio da API pelo valor nominal, e os clientes devem passar apenas deltas (dados alterados) para minimizar o registro desnecessário de pontos de dados. Para saber mais, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.track`.

Os clientes que usam a API para chamadas de servidor para servidor podem precisar incluir `rest.iad-01.braze.com` na lista de permissões se estiverem protegidos por um firewall.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Parâmetros de solicitação

{% alert important %}
Para cada componente de solicitação listado na tabela a seguir, você deve incluir um dos seguintes: `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Vetor de objetos de atributos | Consulte o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Vetor de objetos de eventos | Consulte o [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Vetor de objetos de compra | Consulte o [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Resolução de identificadores

Cada objeto de solicitação deve incluir pelo menos um identificador. A tabela a seguir descreve como a Braze determina qual identificador usar para a busca do perfil de usuário.

| Tipo de identificador | Identificadores | Comportamento |
| --------------- | ----------- | -------- |
| Primário | `external_id`, `user_alias`, `braze_id` | Usado para busca do perfil de usuário. Apenas um identificador primário é permitido por objeto de solicitação — incluir mais de um faz com que o objeto seja rejeitado. |
| Secundário | `email`, `phone` | Usado para busca do perfil de usuário **somente** quando nenhum identificador primário está presente. Se tanto `email` quanto `phone` forem incluídos sem um identificador primário, `email` tem precedência. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um identificador primário está presente, quaisquer valores de `email` ou `phone` no mesmo objeto de solicitação são tratados como atributos do perfil — não como identificadores para busca de usuário. Por exemplo, se uma solicitação inclui tanto um `external_id` quanto um `email`:

- A Braze busca o perfil de usuário pelo `external_id`.
- O valor de `email` é definido (ou atualizado) como um atributo no perfil encontrado.

{% alert important %}
Incluir um identificador primário que não corresponde a nenhum perfil existente pode criar um perfil duplicado, mesmo quando `email` ou `phone` na mesma solicitação correspondem a um perfil existente. Para saber mais, consulte [Como evitar a criação de perfis de usuário duplicados?](#how-do-i-avoid-creating-duplicate-user-profiles).
{% endalert %}

## Exemplos de solicitações

### Atualizar um perfil de usuário por endereço de e-mail

É possível atualizar um perfil de usuário por endereço de e-mail usando o endpoint `/users/track`.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Atualizar um perfil de usuário por número de telefone

Você pode atualizar um perfil de usuário por número de telefone usando o endpoint `/users/track`. Esse endpoint só funciona se você incluir um número de telefone válido.

{% alert important %}
Se você incluir uma solicitação com `email` e `phone`, a Braze usará o e-mail como identificador.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Definir grupos de inscrições

Este exemplo mostra como criar um usuário e definir seu grupo de inscrições no objeto de atributos do usuário.

A atualização do status da inscrição com esse endpoint atualiza o usuário especificado pelo `external_id` (como User1) e atualiza o status da inscrição de todos os usuários com o mesmo e-mail desse usuário (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert note %}
Para grupos de inscrições de SMS, quando você define o `subscription_state` de um grupo como `subscribed`, é possível incluir o parâmetro opcional `use_double_opt_in_logic` definido como `true` dentro desse objeto de grupo de inscrições para inserir o usuário no fluxo de trabalho de [dupla aceitação de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Se esse parâmetro for omitido ou definido como `false` quando `subscription_state` for `subscribed`, o usuário será inscrito sem entrar no fluxo de trabalho de dupla aceitação. Esse parâmetro não é aplicado quando `subscription_state` é definido com outros valores, como `unsubscribed`.
{% endalert %}

### Exemplo de solicitação para criar um usuário somente de alias

Você pode usar o endpoint `/users/track` para criar um usuário somente de alias, definindo a chave `_update_existing_only` com o valor `false` no corpo da solicitação. Se você omitir esse valor, a Braze não criará o perfil de usuário somente de alias. O uso de um usuário somente de alias garante que exista um perfil com esse alias. Isso é especialmente útil ao criar uma integração, pois evita que a Braze crie perfis de usuário duplicados.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Respostas

Ao usar qualquer uma das solicitações de API mencionadas acima, você deve receber uma das três respostas gerais a seguir: uma [mensagem de sucesso](#successful-message), uma [mensagem de sucesso com erros não fatais](#successful-message-with-non-fatal-errors) ou uma [mensagem com erros fatais](#message-with-fatal-errors).

### Mensagem de sucesso

As mensagens de sucesso retornam a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### Mensagem de sucesso com erros não fatais

Se sua mensagem for bem-sucedida, mas tiver erros não fatais, como um objeto de evento inválido em uma longa lista de eventos, você receberá a seguinte resposta:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

Para mensagens de sucesso, a Braze ainda processa todos os dados não afetados por um erro no vetor `errors`.

### Mensagem com erros fatais

Se sua mensagem tiver um erro fatal, você receberá a seguinte resposta:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Códigos de resposta de erros fatais

Para obter os códigos de status e as mensagens de erro associadas que a Braze retorna se sua solicitação encontrar um erro fatal, consulte [Erros fatais e respostas]({{site.baseurl}}/api/errors/#fatal-errors).

Se receber o erro "provided external_id is blacklisted and disallowed", sua solicitação pode ter incluído um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

### Erros específicos do endpoint

Os erros a seguir são específicos do endpoint `/users/track` e são retornados no vetor `errors` da resposta. Use-os para solucionar problemas com objetos individuais em uma solicitação.

| Erro | Descrição |
|---|---|
| `BAD_DEVICE_ID` | O `device_id` para uma importação de token deve ter entre 8 e 255 bytes. |
| `BAD_EMAIL_SUBSCRIPTION_STATE` | `email_subscribe` deve ser `subscribed`, `unsubscribed` ou `opted_in`. |
| `BAD_LOCATION_UPDATE` | `current_location` deve ser um objeto contendo `longitude` e `latitude`. |
| `BAD_PUSH_SUBSCRIPTION_STATE` | `push_subscribe` deve ser `subscribed`, `unsubscribed` ou `opted_in`. |
| `BAD_PUSH_TOKEN_APP_ID` | O `app_id` em uma importação de token deve ser um identificador de app válido do espaço de trabalho atual. |
| `BAD_PUSH_TOKEN_IMPORT` | As importações de token devem incluir tokens e excluir `external_id` e `braze_id`. |
| `BAD_PUSH_TOKEN_STRING` | O valor de `token` em uma importação de token deve ser uma string. |
| `BAD_PUSH_TOKEN_VALUE` | `push_tokens` deve ser um vetor de objetos. |
| `BAD_SUBSCRIPTION_GROUP_ARRAY` | `subscription_groups` deve ser um vetor. |
| `BAD_SUBSCRIPTION_GROUP_HASH` | Cada item no vetor `subscription_groups` deve ser um objeto JSON com as chaves `subscription_group_id` e `subscription_state`. |
| `BAD_SUBSCRIPTION_GROUP_ID` | `subscription_group_id` deve ser um UUID válido de grupo de inscrições. |
| `BAD_SUBSCRIPTION_GROUP_STATE` | `subscription_state` para um grupo de inscrições deve ser `subscribed` ou `unsubscribed`. |
| `BLACKLISTED_EXTERNAL_USER_ID` | O `external_id` fornecido está na lista de proibições e não é permitido. |
| `EMAIL_BAD_FORMAT` | O valor fornecido para `email` não é um endereço de e-mail válido. |
| `EXTERNAL_USER_ID_TOO_LARGE` | O `external_id` excede o comprimento máximo permitido de 987 bytes. |
| `INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO` | `email_subscription_info` não é um atributo válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### O que acontece quando são encontrados vários perfis com o mesmo endereço de e-mail?
Se o `external_id` existir, a Braze priorizará o perfil atualizado mais recentemente com um ID externo para atualizações. Se o `external_id` não existir, a Braze priorizará o perfil atualizado mais recentemente para atualizações.

### O que acontece se não houver nenhum perfil com o endereço de e-mail?
A Braze cria um perfil e um usuário somente de e-mail e define o campo de e-mail como test@braze.com, conforme indicado no exemplo de solicitação para atualizar um perfil de usuário por endereço de e-mail. A Braze não cria um alias.

### Como usar o `/users/track` para importar dados de usuários antigos?
Você pode enviar dados por meio da API da Braze para um usuário que ainda não tenha usado seu app móvel para gerar um perfil de usuário. Se o usuário usar o aplicativo posteriormente, todas as informações após a identificação usando o SDK serão mescladas com o perfil de usuário existente que você criou usando a chamada da API. Qualquer comportamento de usuário registrado anonimamente pelo SDK antes da identificação é perdido ao ser mesclado com o perfil de usuário existente gerado pela API.

A ferramenta de segmentação inclui esses usuários independentemente de terem interagido com o app. Se você quiser excluir usuários enviados usando a API de Usuário que ainda não interagiram com o app, adicione o filtro `Session Count > 0`.

### Como evitar a criação de perfis de usuário duplicados?

Perfis duplicados podem ocorrer quando uma solicitação inclui um identificador primário (como `external_id`) que não corresponde a nenhum perfil existente, junto com um valor de `email` ou `phone` que corresponde a um perfil existente. Como os identificadores primários são usados para busca de usuário, a Braze cria um novo perfil para o `external_id` não reconhecido em vez de atualizar o perfil existente somente de e-mail ou somente de telefone.

Para evitar duplicatas:

- Ao fazer a transição de usuários de perfis somente de e-mail ou somente de telefone para perfis identificados, use o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) para atribuir um `external_id` ao perfil existente, em vez de enviar ambos para `/users/track`.
- Se já existirem duplicatas, mescle-as usando o [endpoint `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

### Como o `/users/track` lida com eventos duplicados?

Cada objeto de evento no vetor de eventos representa uma única ocorrência de um evento personalizado por um usuário em um momento designado. Isso significa que cada evento ingerido pela Braze tem seu próprio ID de evento, de modo que os eventos "duplicados" são tratados como eventos separados e exclusivos.

### Como o `/users/track` lida com atributos personalizados aninhados inválidos?

Quando um atributo personalizado aninhado contém valores inválidos (como formatos de hora inválidos ou valores nulos), a Braze descarta do processamento todas as atualizações de atributos personalizados aninhados na solicitação. Isso se aplica a todas as estruturas aninhadas dentro desse atributo específico. Para garantir o processamento bem-sucedido, verifique se todos os valores dentro dos atributos personalizados aninhados são válidos antes do envio.

## Monthly Active Users CY 24-25, Universal MAU, Web MAU e Mobile MAU

Para clientes com novos preços, os limites de taxa são aplicados no nível da empresa. Os clientes podem definir limites de taxa do espaço de trabalho para limites por hora, mas os limites de burst ainda são compartilhados entre todos os espaços de trabalho.

Para os clientes que adquiriram Monthly Active Users CY 24-25, Universal MAU, Web MAU ou Mobile MAU, a Braze gerencia diferentes limites de taxa em seu endpoint `/users/track`:
- Os limites de taxa por hora são definidos de acordo com a atividade esperada de ingestão de dados na sua conta, que pode corresponder ao número de usuários ativos mensais que você adquiriu, setor, sazonalidade ou outros fatores.
- Além do limite por hora, a Braze impõe um limite de burst no número de solicitações que podem ser enviadas a cada três segundos.
- Cada solicitação pode conter até 75 atualizações combinadas entre objetos de atributo, evento ou compra.

Os limites atuais baseados na ingestão esperada podem ser encontrados no dashboard em **Settings** > **APIs and Identifiers** > **API Usage Dashboard**. Podemos modificar os limites de taxa para proteger a estabilidade do sistema ou permitir um aumento na taxa de transferência de dados na sua conta. Entre em contato com o suporte da Braze ou com o seu gerente de sucesso do cliente em caso de dúvidas ou preocupações relacionadas ao limite de solicitações por hora ou por segundo e às necessidades da sua empresa.

### Cabeçalhos de limite de taxa para Monthly Active Users CY 24-25, Universal MAU, Web MAU e Mobile MAU

Todas as respostas sem limite de taxa (ou seja, que não retornam `429`) contêm os seguintes cabeçalhos de resposta HTTP que indicam o estado da janela de limite de taxa por hora para o cliente. Use esses cabeçalhos para gerenciar sua taxa de solicitações:

| Nome do cabeçalho             | Descrição                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | O número de solicitações permitidas por período de tempo                                              |
| `X-RateLimit-Remaining` | O número aproximado de solicitações restantes na janela atual                                |
| `X-RateLimit-Reset`     | O número de segundos restantes antes da reinicialização da janela atual                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Observe que os cabeçalhos `RateLimit-Limit`, `RateLimit-Remaining` e `RateLimit-Reset` não são retornados quando você recebe um erro HTTP `429`. Quando o erro ocorre, esses cabeçalhos são substituídos por um cabeçalho `X-Ratelimit-Retry-After` que retorna um número inteiro indicando o número de segundos antes que você possa voltar a fazer solicitações.

{% endapi %}