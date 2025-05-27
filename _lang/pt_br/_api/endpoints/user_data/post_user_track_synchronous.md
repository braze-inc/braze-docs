---
nav_title: "POST: Rastreamento de usuários (síncrono)"
article_title: "POST: Rastreamento de usuários (síncrono)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Este artigo detalha o endpoint da Braze de rastreamento de usuários síncronos."

---
{% api %}
# Rastreamento de usuários (síncrono)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Use esse endpoint para registrar eventos e compras personalizados e atualizar os atributos do perfil do usuário de forma síncrona. Esse endpoint funciona de forma semelhante ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que atualiza perfis de usuário de forma assíncrona.

{% alert important %}
Esse ponto de extremidade está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar dessa versão beta.
{% endalert %}

## Chamadas síncronas e assíncronas à API

Em uma chamada assíncrona, a API retornará o código de status `201`, indicando que sua solicitação foi recebida, compreendida e aceita com êxito. No entanto, isso não significa que sua solicitação tenha sido totalmente concluída.

Em uma chamada síncrona, a API retornará um código de status `201`, indicando que sua solicitação foi recebida, compreendida, aceita e concluída com êxito. A resposta da chamada mostrará os campos selecionados do perfil do usuário como resultado da operação.

Esse endpoint tem um limite de frequência menor do que o endpoint `/users/track` (consulte o [limite de frequência](#rate-limit) abaixo). Cada solicitação `/users/track/sync` pode incluir apenas um objeto de evento, um objeto de atributo **ou** um objeto de compra. Esse endpoint deve ser reservado para atualizações de perfil de usuário em que é necessária uma chamada síncrona. Para uma implementação adequada, recomendamos usar `/users/track/sync` e `/users/track` juntos.

Por exemplo, se estiver enviando solicitações consecutivas para o mesmo usuário em um curto período de tempo, as condições de corrida são possíveis com o endpoint assíncrono `/users/track`, mas com o endpoint `/users/track/sync` é possível enviar essas solicitações em sequência, cada uma após receber uma resposta `2XX`.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.track.sync`.

Os clientes que usam a API para chamadas de servidor para servidor podem precisar permitir a lista `rest.iad-01.braze.com` se estiverem protegidos por um firewall.

## Limite de taxa

Aplicamos um limite de velocidade básico de 500 solicitações por minuto para esse endpoint para todos os clientes. Cada solicitação `/users/track/sync` pode incluir até um objeto de evento, um objeto de atributo ou um objeto de compra. Cada objeto (evento, atributo e vetores de compra) pode atualizar um usuário cada.

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Parâmetros de solicitação

{% alert important %}
Para cada componente de solicitação listado na tabela a seguir, um dos componentes `external_id`, `user_alias`, `braze_id`, `email` ou `phone` é necessário informar.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Um objeto de atribuição | Consulte o [objeto de atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Um objeto de evento | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Um objeto de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Respostas

Ao usar os [parâmetros de solicitação](#request-parameters) desse endpoint, você deve receber uma das seguintes respostas: uma mensagem de sucesso ou uma mensagem com erros fatais.

### Envio de mensagens bem-sucedido

As mensagens bem-sucedidas retornarão a seguinte resposta, que inclui informações sobre os dados do perfil do usuário que foram atualizados.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
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

## Exemplos de solicitações e respostas

### Atualizar um atributo personalizado por ID externo

#### Solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Resposta

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
} 
```

### Atualizar um evento personalizado por e-mail

#### Solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### Resposta

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
} 
```

### Atualizar um evento de compra por alias de usuário

#### Solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : { 
          "alias_name" : "device123", 
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [ 
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            { 
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Resposta

```
{
    "users": [
        {
          "user_alias" : { 
            "alias_name" : "device123", 
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
} 
```

## Perguntas frequentes

### Devo usar o ponto de extremidade assíncrono ou síncrono?

Para a maioria das atualizações de perfil, o endpoint `/users/track` funcionará melhor devido ao seu limite de frequência mais alto e à flexibilidade para permitir solicitações em lote. No entanto, o endpoint `/users/track/sync` é útil se você estiver enfrentando condições de corrida devido a solicitações rápidas e consecutivas para o mesmo usuário.

### O tempo de resposta é diferente do ponto de extremidade `/users/track`?

Ao fazer uma chamada síncrona, a API espera até que a solicitação seja concluída para retornar uma resposta. Consequentemente, as solicitações síncronas levarão mais tempo, em média, do que as solicitações assíncronas para `/users/track`. Para a maioria das solicitações, você pode contar com uma resposta em segundos.

### Posso enviar várias solicitações ao mesmo tempo?

Sim, desde que as solicitações sejam para usuários diferentes, ou que cada solicitação atualize atribuições, eventos e compras diferentes para um usuário.

Se estiver enviando várias solicitações para um usuário, para o mesmo atributo, evento ou compra, o Braze recomenda aguardar uma resposta bem-sucedida entre cada solicitação para evitar a ocorrência de condições de corrida.

### Por que o valor da resposta não corresponde ao da minha solicitação original?

Embora sua solicitação tenha sido concluída, é possível que o valor do atributo personalizado não tenha sido atualizado. Isso pode acontecer quando a atualização do atributo personalizado exceder o número máximo de caracteres, exceder os limites da matriz ou se o usuário não existir no Braze e você tiver `_update_existing_only = true`.

Nessas situações, considere a resposta como um sinal de que sua requisição foi finalizada, mas a atualização que você desejava não foi efetuada. Solucione os problemas com os motivos pelos quais isso pode acontecer, conforme descrito acima.

{% endapi %}
