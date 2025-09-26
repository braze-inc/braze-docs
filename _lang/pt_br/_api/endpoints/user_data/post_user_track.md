---
nav_title: "POST: Rastreamento de usuários"
article_title: "POST: Rastreamento de usuários"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o ponto de extremidade do Braze para rastreamento de usuários."

---
{% api %}
# rastreia usuários
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Use esse endpoint para registrar eventos e compras personalizados e atualizar as atribuições do perfil do usuário.

{% alert note %}
O processo de Braze trata os dados passados pela API como estão, e os clientes devem passar apenas deltas (dados em mudança) para minimizar o consumo desnecessário de pontos de dados. Para saber mais, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.track`.

Os clientes que usam a API para chamadas de servidor para servidor talvez precisem permitir a lista `rest.iad-01.braze.com` se estiverem protegidos por um firewall.

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
Para cada componente de solicitação listado na tabela a seguir, é necessário um dos componentes `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
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
Se você incluir um pedido com `email` e `phone`, Braze usará o e-mail como identificador.
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

A atualização do status da inscrição com esse ponto de extremidade atualizará o usuário especificado pelo endereço `external_id` (como User1) e atualizará o status da inscrição de todos os usuários com o mesmo e-mail desse usuário (User1).

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

Você pode usar o ponto de extremidade `/users/track` para criar um novo usuário somente de alias, definindo a chave `_update_existing_only` com um valor de `false` no corpo da solicitação. Se esse valor for omitido, o perfil de usuário somente de alias não será criado. O uso de um usuário somente com alias garante que existirá um perfil com esse alias. Isso é especialmente útil ao criar uma nova integração, pois evita a criação de perfis de usuário duplicados.

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

As mensagens bem-sucedidas receberão a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
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

Para mensagens de sucesso, todos os dados não afetados por um erro na matriz `errors` ainda serão processados. 

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

Para obter os códigos de status e as mensagens de erro associadas que serão retornadas se sua solicitação encontrar um erro fatal, consulte [Erros e respostas fatais]({{site.baseurl}}/api/errors/#fatal-errors).

Se receber o erro "provided external_id is blacklisted and disallowed", sua solicitação pode ter incluído um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Perguntas frequentes

{% multi_lang_include email-via-sms-warning.md %}

### O que acontece quando são encontrados vários perfis com o mesmo endereço de e-mail?
Se o site `external_id` existir, o perfil atualizado mais recentemente com um ID externo terá prioridade para atualizações. Se o endereço `external_id` não existir, o perfil atualizado mais recentemente será priorizado para atualizações.

### O que acontece se não houver nenhum perfil com o endereço de e-mail no momento?
Um novo perfil será criado e um usuário somente de e-mail será criado. Não será criado um alias. O campo de e-mail será definido como test@braze.com, conforme notado na solicitação de exemplo para atualizar um perfil de usuário por endereço de e-mail.

### Como usar o site `/users/track` para importar dados de usuários antigos?
Você pode enviar dados por meio da API do Braze para um usuário que ainda não tenha usado seu app móvel para gerar um perfil de usuário. Se o usuário usar o aplicativo posteriormente, todas as informações após sua identificação usando o SDK serão mescladas com o perfil de usuário existente que você criou usando a chamada da API. Qualquer comportamento de usuário registrado anonimamente pelo SDK antes da identificação será perdido ao ser mesclado com o perfil de usuário existente gerado pela API.

A ferramenta de segmentação incluirá esses usuários independentemente de seu engajamento com o app. Se você quiser excluir usuários enviados usando a API de Usuário que ainda não interagiram com o app, adicione o filtro `Session Count > 0`.

### Como o site `/users/track` lida com eventos duplicados?

Cada objeto de evento no vetor de eventos representa uma única ocorrência de um evento personalizado por um usuário em um momento designado. Isso significa que cada evento ingerido no Braze tem seu próprio ID de evento, de modo que os eventos "duplicados" são tratados como eventos separados e exclusivos.

### Como `/users/track` lida com atributos personalizados aninhados inválidos?

Quando um atributo personalizado aninhado contém valores inválidos (como formatos de hora inválidos ou valores nulos), todas as atualizações de atributos personalizados aninhados na solicitação serão descartadas do processamento. Isso se aplica a todas as estruturas aninhadas dentro desse atributo específico. Para garantir um processamento bem-sucedido, verifique se todos os valores dentro dos atributos personalizados aninhados são válidos antes de enviar.

## Usuários Ativos Mensais CY 24-25
Para os clientes que adquiriram Usuários Ativos Mensais - CY 24-25, a Braze gerencia diferentes limites de taxa em seu endpoint `/users/track`:
- Os limites de taxa horária são definidos de acordo com a atividade esperada de ingestão de dados em sua conta, que pode corresponder ao número de usuários ativos mensais que você adquiriu, setor, sazonalidade ou outros fatores.
- Além do limite horário, a Braze impõe um limite de explosão no número de solicitações que podem ser enviadas a cada três segundos.
- Cada solicitação pode agrupar até 50 atualizações combinadas entre objetos de atributo, evento ou compra.

Os limites atuais com base na ingestão esperada podem ser encontrados no dashboard em **Configurações** > **APIs e Identificadores** > **Dashboard de Uso da API**. Podemos modificar os limites de taxa para proteger a estabilidade do sistema ou permitir um aumento na taxa de transferência de dados em sua conta. Por favor, entre em contato com o suporte da Braze ou com o gerente de sucesso do cliente para perguntas ou preocupações relacionadas ao limite de solicitações por hora ou por segundo e às necessidades do seu negócio.



{% endapi %}
