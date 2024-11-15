---
nav_title: "POST: Rastreamento de usuários (em massa)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "Este artigo descreve detalhes sobre o ponto de extremidade Rastrear usuários (em massa)."
---

{% api %}
# Rastreamento de usuários (em massa)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Use esse endpoint para registrar eventos e compras personalizados e atualizar atributos de perfil de usuário em massa.

{% alert important %}
Esse ponto de extremidade está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar da versão beta.
{% endalert %}

## Quando usar esse ponto de extremidade

Semelhante ao [POST: Ponto de extremidade de rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), você pode usar esse ponto de extremidade para atualizar os perfis de usuário. No entanto, esse endpoint é mais adequado para fazer atualizações em massa:

- **Solicitações maiores:** Esse endpoint permite 10.000 usuários por solicitação, o que significa que é necessário fazer menos solicitações para atender às suas necessidades de atualização em massa.
- **Priorização:** Durante as condições de pico de tráfego, as solicitações de `/users/track` serão priorizadas em relação às solicitações de `/users/track/bulk`. O uso de ambos os endpoints oferece mais controle sobre a ingestão de dados.

Observe que as atualizações do usuário nesse endpoint não dispararão nenhuma campanha baseada em ação ou Canvas baseado em ação, não dispararão nenhum evento de exceção nem rastrearão as métricas de conversão. As atualizações do usuário nesse endpoint estão disponíveis para segmentação e personalização.

Considere usar esse endpoint quando estiver preenchendo muitos perfis de usuário durante a integração ou sincronizando grandes quantidades de perfis de usuário como parte de uma sincronização diária.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma chave de API com a permissão `users.track.bulk`.

Se estiver usando a API para chamadas de servidor para servidor, talvez seja necessário listar o endpoint (por exemplo, `rest.iad-01.braze.com`) se estiver atrás de um firewall. Consulte os [pontos de extremidade por instância]({{site.baseurl}}/api/basics#endpoints) para saber mais.

## Limite de taxa

Aplicamos um limite de velocidade básico de 5 solicitações por segundo a esse endpoint para todos os clientes.

Cada solicitação `/users/sync/bulk` tem um limite de carga útil de 4 MB e pode conter até 10.000 objetos de evento, atribuição ou compra.

Cada objeto (evento, atribuição e vetor de compra) pode atualizar um usuário cada, o que significa que até 10.000 usuários diferentes podem ser atualizados em uma única solicitação. Um único perfil de usuário pode ser atualizado com até 100 objetos em uma única solicitação.

{% alert note %}
Se precisar aumentar seu limite de frequência, entre em contato com o gerente de sucesso do cliente.
{% endalert %}


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
Para cada componente de solicitação listado na tabela a seguir, um dos componentes `external_id`, `user_alias`, `braze_id`, `email` ou `phone` é necessário informar.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Vetor de objetos de atribuição | Consulte o [objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Vetor de objetos de eventos | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Vetor de objetos de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplos de solicitações

### Atualize em massa 10.000 perfis de usuário em uma única solicitação

É possível atualizar até 10.000 perfis de usuário. Aqui está um exemplo truncado em que a solicitação consiste em 10.000 objetos de atribuição:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Aqui está um exemplo em que a solicitação consiste em objetos de atribuição e de evento:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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
        }
    ]
}'
```

## Respostas

### Envios de mensagens bem-sucedidos

As mensagens bem-sucedidas receberão a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Mensagem bem-sucedida com erros não fatais

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

#### Códigos de resposta a erros fatais

Para obter os códigos de status e as mensagens de erro associadas que serão retornadas se sua solicitação encontrar um erro fatal, consulte [Erros e respostas fatais]({{site.baseurl}}/api/errors/#fatal-errors).

Se você receber o erro `provided external_id is blacklisted and disallowed`, sua solicitação pode ter incluído um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Perguntas frequentes

### Devo usar esse endpoint ou o `/users/track` normal?

Recomendamos o uso de ambos.

Para backfills e sincronizações de grandes perfis de usuários em que não são necessários disparos para campanhas e Canvas baseados em ação, rastreamento de conversões e eventos de exceção, use `/users/track/bulk`. 

Para casos de uso em tempo real, use o endpoint `/users/track`.

### Quais identificadores posso usar em /users/track/bulk?

É necessário um dos endereços `external_id`, `braze_id`, `user_alias`, `email`, ou `phone`. Para obter mais exemplos, consulte nossa documentação sobre o [objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [o objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) ou [o objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/). 

### Posso incluir atribuições, eventos e compras em uma única solicitação?

Sim. Você pode construir sua solicitação com qualquer quantidade de atribuições, eventos e objetos de compra, até 10.000 objetos por solicitação.


{% endapi %}
