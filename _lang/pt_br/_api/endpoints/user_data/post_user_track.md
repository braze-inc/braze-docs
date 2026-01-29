---
nav_title: "POST: Criar e atualizar usuários"
article_title: "POST: Criar e atualizar usuários"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o ponto de extremidade do Braze para rastreamento de usuários."

---
{% api %}
# Criar e atualizar usuários
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Use esse endpoint para registrar eventos e compras personalizados e atualizar as atribuições do perfil do usuário.

{% alert note %}
O Braze processa os dados passados por meio da API pelo valor nominal, e os clientes devem passar apenas deltas (dados alterados) para minimizar o registro desnecessário de pontos de dados. Para saber mais, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.track`.

Os clientes que usam a API para chamadas de servidor para servidor podem precisar permitir a lista `rest.iad-01.braze.com` se estiverem protegidos por um firewall.

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
Para cada componente de solicitação listado na tabela a seguir, você deve incluir um dos seguintes itens: `external_id`, `user_alias`, `braze_id`, `email`, ou `phone`.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Vetor de objetos de atribuição | Consulte o [objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Vetor de objetos de eventos | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Vetor de objetos de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplos de solicitações

### Atualizar um perfil de usuário por endereço de e-mail

É possível atualizar um perfil de usuário por endereço de e-mail usando o ponto de extremidade `/users/track`.

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
Se você incluir uma solicitação com `email` e `phone`, o Braze usará o e-mail como identificador.
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

Este exemplo mostra como criar um usuário e definir seu grupo de inscrições no objeto de atribuições do usuário.

A atualização do status da inscrição com esse endpoint atualiza o usuário especificado pelo endereço `external_id` (como User1) e atualiza o status da inscrição de todos os usuários com o mesmo e-mail desse usuário (User1).

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
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### Exemplo de solicitação para criar um usuário somente de alias

Você pode usar o ponto de extremidade `/users/track` para criar um usuário somente de alias, definindo a chave `_update_existing_only` com um valor de `false` no corpo da solicitação. Se você omitir esse valor, o Braze não criará o perfil de usuário somente de alias. O uso de um usuário somente de alias garante que exista um perfil com esse alias. Isso é especialmente útil ao criar uma integração, pois evita que o Braze crie perfis de usuário duplicados.

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

### Envio de mensagens bem-sucedido

As mensagens bem-sucedidas são recebidas com a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### Mensagem bem-sucedida com erros não fatais

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

Para mensagens de sucesso, o Braze ainda processa todos os dados não afetados por um erro na matriz `errors`.

### Envio de mensagens com erros fatais

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

### Códigos de resposta a erros fatais

Para obter os códigos de status e as mensagens de erro associadas que o Braze retorna se sua solicitação encontrar um erro fatal, consulte [Erros fatais & respostas]({{site.baseurl}}/api/errors/#fatal-errors).

Se receber o erro "provided external_id is blacklisted and disallowed", sua solicitação pode ter incluído um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Perguntas frequentes

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### O que acontece quando são encontrados vários perfis com o mesmo endereço de e-mail?
Se o endereço `external_id` existir, o Braze priorizará o perfil atualizado mais recentemente com um ID externo para atualizações. Se o endereço `external_id` não existir, o Braze priorizará o perfil atualizado mais recentemente para atualizações.

### O que acontece se não houver nenhum perfil com o endereço de e-mail?
O Braze cria um perfil e um usuário somente de e-mail e define o campo de e-mail como test@braze.com, conforme notado na solicitação de exemplo para atualizar um perfil de usuário por endereço de e-mail. O Braze não cria um alias.

### Como usar o site `/users/track` para importar dados de usuários antigos?
Você pode enviar dados por meio da API do Braze para um usuário que ainda não tenha usado seu app móvel para gerar um perfil de usuário. Se o usuário usar o aplicativo posteriormente, todas as informações após a identificação usando o SDK serão mescladas com o perfil de usuário existente que você criou usando a chamada da API. Qualquer comportamento de usuário registrado anonimamente pelo SDK antes da identificação é perdido ao ser mesclado com o perfil de usuário existente gerado pela API.

A ferramenta de segmentação inclui esses usuários independentemente de seu engajamento com o app. Se você quiser excluir usuários enviados usando a API de Usuário que ainda não interagiram com o app, adicione o filtro `Session Count > 0`.

### Como o site `/users/track` lida com eventos duplicados?

Cada objeto de evento no vetor de eventos representa uma única ocorrência de um evento personalizado por um usuário em um momento designado. Isso significa que cada evento ingerido no Braze tem seu próprio ID de evento, de modo que os eventos "duplicados" são tratados como eventos separados e exclusivos.

### Como o site `/users/track` lida com atributos personalizados aninhados inválidos?

Quando um atributo personalizado aninhado contém quaisquer valores inválidos (como formatos de hora inválidos ou valores nulos), o Braze retira do processamento todas as atualizações de atributos personalizados aninhados na solicitação. Isso se aplica a todas as estruturas aninhadas dentro dessa atribuição específica. Para ajudar a garantir o processamento bem-sucedido, verifique se todos os valores dentro dos atributos personalizados aninhados são válidos antes do envio.

## Usuários ativos mensais no período de 24 a 25 de janeiro de 2015, MAU universal, MAU da Web e MAU móvel

Para clientes com novos preços, os limites de frequência são aplicados em nível de empresa. Os clientes podem definir limites de frequência do espaço de trabalho para limites por hora, mas os limites de explosão ainda são compartilhados entre todos os espaços de trabalho.

Para os clientes que adquiriram Monthly Active Users CY 24-25, Universal MAU, Web MAU ou Mobile MAU, o Braze gerencia diferentes limites de frequência em seu endpoint `/users/track`:
- Os limites de taxa horária são definidos de acordo com a atividade esperada de ingestão de dados em sua conta, que pode corresponder ao número de usuários ativos mensais que você adquiriu, setor, sazonalidade ou outros fatores.
- Além do limite por hora, o Braze impõe um limite de explosão no número de solicitações que podem ser enviadas a cada três segundos.
- Cada solicitação pode ter até 75 atualizações combinadas entre atributos, eventos ou objetos de compra.

Os limites atuais baseados na ingestão esperada podem ser encontrados no dashboard em **Settings** > **APIs and Identifiers** > **API Usage Dashboard**. Podemos modificar os limites de taxa para proteger a estabilidade do sistema ou permitir um aumento na taxa de transferência de dados em sua conta. Entre em contato com o suporte da Braze ou com o seu gerente de sucesso do cliente em caso de dúvidas ou preocupações relacionadas ao limite de solicitação por hora ou por segundo e às necessidades da sua empresa.

### Cabeçalhos de limite de frequência para Usuários ativos mensais CY 24-25, MAU universal, MAU da Web e MAU móvel

Todas as respostas sem limite de frequência (como não`429`) contêm os seguintes cabeçalhos de resposta HTTP que indicam o estado da janela de limite de frequência horária para o cliente. Use esses cabeçalhos para gerenciar sua taxa de solicitação:

| Nome do cabeçalho             | Descrição                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | O número de solicitações permitidas por período de tempo                                              |
| `X-RateLimit-Remaining` | O número aproximado de solicitações restantes em uma janela                                |
| `X-RateLimit-Reset`     | O número de segundos restantes antes da reinicialização da janela atual                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Observe que os cabeçalhos `RateLimit-Limit`, `RateLimit-Remaining` e `RateLimit-Reset` não são retornados quando você obtém um erro HTTP `429`. Quando o erro ocorre, esses cabeçalhos são substituídos por um cabeçalho `X-Ratelimit-Retry-After` que retorna um número inteiro indicando o número de segundos antes que você possa começar a fazer solicitações.

{% endapi %}
