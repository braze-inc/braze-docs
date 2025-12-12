---
nav_title: "POST: Exportar perfil de usuário por identificador"
article_title: "POST: Exportar perfil de usuário por identificador"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Exportar usuários por identificador Braze."

---
{% api %}
# Exportar perfil de usuário por identificador
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Use esse endpoint para exportar dados de qualquer perfil de usuário, especificando um identificador de usuário.

Até 50 `external_ids` ou `user_aliases` podem ser incluídos em uma única solicitação. Se você quiser especificar `device_id`, `email_address`, ou `phone`, somente um desses identificadores poderá ser incluído por solicitação.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `users.export.ids`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
Para clientes que fizeram a integração com o Braze em 22 de agosto de 2024 ou após essa data, é necessário o parâmetro de solicitação `fields_to_export`.
{% endalert %}

## Parâmetros de solicitação

| Parâmetro          | Obrigatória | Tipo de dados                                                     | Descrição                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | Opcional | Matriz de strings                                              | Identificadores externos para os usuários que deseja exportar.                                              |
| `user_aliases`     | Opcional | Vetor de objeto de alias de usuário                                    | [Aliases de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/) para usuários a serem exportados. |
| `device_id`        | Opcional | String                                                        | Identificador do dispositivo, conforme retornado por vários métodos do SDK, como `getDeviceId`.                 |
| `braze_id`         | Opcional | String                                                        | Identificador do Braze para um usuário específico.                                                      |
| `email_address`    | Opcional | String                                                        | Endereço de e-mail do usuário.                                                                       |
| `phone`            | Opcional | String em [E.164](https://en.wikipedia.org/wiki/E.164) formato | Número de telefone do usuário.                                                                        |
| `fields_to_export` | Opcional* | Array de strings                                              | Nome dos campos de dados de usuários a serem exportados.<br><br>\*Esse campo é obrigatório para usar o limite de taxa mais rápido de 40 solicitações por segundo. Se omitido, será usado o limite de taxa padrão de 250 solicitações por minuto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Requerido para clientes que tenham embarcado no Braze em ou após 22 de agosto de 2024.

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Campos a serem exportados

A seguir, uma lista de `fields_to_export` válidos. O uso do site `fields_to_export` para minimizar os dados retornados pode melhorar o tempo de resposta desse endpoint da API:

| Campo a ser exportado       | Tipo de dados       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | Vetor           | Apps nos quais esse usuário registrou sessões, que incluem os campos:<br><br>- `name`: nome do app<br>- `platform`: plataforma do app, como iOS, Android ou Web<br>- `version`: número ou nome da versão do app <br>- `sessions`: número total de sessões para este app<br>- `first_used`: data da primeira sessão<br>- `last_used`: data da última sessão<br><br>Todos os campos são strings.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | String          | Dados de [integrações de atribuição]({{site.baseurl}}/partners/message_orchestration/), se configurados. Identificador de uma determinada campanha publicitária.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | String          | Dados de [integrações de atribuição]({{site.baseurl}}/partners/message_orchestration/), se configurados. Identificador da plataforma em que o anúncio estava.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | String          | Dados de [integrações de atribuição]({{site.baseurl}}/partners/message_orchestration/), se configurados. Identificador de um subgrupo opcional abaixo da campanha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | String          | Dados de [integrações de atribuição]({{site.baseurl}}/partners/message_orchestration/), se configurados. Identificador de um subgrupo opcional abaixo da campanha e do grupo de anúncios.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | String          | Status da assinatura push do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | String          | Status da assinatura de e-mail do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | String          | Identificador de usuário exclusivo específico do dispositivo definido pelo Braze para esse usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | String          | País do usuário usando o padrão [ISO 3166-1 alfa-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | String          | Data e hora em que o perfil do usuário foi criado, no formato ISO 8601.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | Objeto          | Pares de valores-chave de atributos personalizados para esse usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | Vetor           | Eventos personalizados atribuídos a esse usuário nos últimos 90 dias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | Vetor           | Informações sobre o dispositivo do usuário, que podem incluir o seguinte, dependendo da plataforma:<br><br>- `model`: Nome do modelo do dispositivo<br>- `os`: Sistema operacional do dispositivo<br>- `carrier`: Operadora de serviço do dispositivo, se disponível<br>- `idfv`: (iOS) identificador do dispositivo Braze, o identificador da Apple para o fornecedor, se houver<br>- `idfa`: (iOS) Identificador para publicidade, se houver<br>- `device_id`: (Android) Identificador do dispositivo Braze<br>- `google_ad_id`: (Android) Identificador de publicidade do Google Play, se houver<br>- `roku_ad_id`: (Roku) Identificador de publicidade da Roku<br>- `ad_tracking_enabled`: Se o rastreamento de anúncios estiver ativado no dispositivo, pode ser verdadeiro ou falso. |
| `dob`                 | String          | Data de nascimento do usuário no formato `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | String          | Endereço de e-mail do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | String          | Identificador de usuário exclusivo para usuários identificados.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | String          | Nome do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | String          | Gênero do usuário. Os valores possíveis são:<br><br>- `M`: masculino<br>- `F`: feminino<br>- `O`: outros<br>- `N`: não aplicável<br>- `P`: prefere não se pronunciar<br>- `nil`: desconhecido                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | String          | Cidade natal do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | String          | Idioma do usuário no padrão ISO-639-1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | Matriz de valores flutuantes | O local mais recente do dispositivo do usuário, formatado como `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | String          | Sobrenome do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | String          | Número de telefone do usuário no formato E.164.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | Vetor           | Compras que esse usuário fez nos últimos 90 dias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | Vetor           | Identificador anônimo exclusivo que especifica para onde enviar as notificações de um app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | Inteiro         | [Número de bucket aleatório]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) do usuário, usado para criar segmentos uniformemente distribuídos de usuários aleatórios.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | Fuso horário do usuário no mesmo formato do banco de dados de fuso horário da IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Receita total atribuída a esse usuário. A receita total é calculada com base nas compras que o usuário fez durante as janelas de conversão para as campanhas e Canvas que recebeu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Data e hora       | Data e hora em que o usuário desinstala o app. Omitido se o app não tiver sido desinstalado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objeto          | [Objeto de aliases de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contendo `alias_name` e `alias_label`, se houver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Esteja ciente de que o ponto de extremidade `/users/export/ids` reunirá todo o perfil desse usuário, incluindo dados como todas as campanhas e Canvas recebidos, todos os eventos personalizados realizados, todas as compras feitas e todos os atributos personalizados. Como resultado, esse endpoint é mais lento do que outros endpoints da API REST.

Dependendo dos dados solicitados, esse endpoint da API pode não ser suficiente para atender às suas necessidades devido ao limite de frequência de 250 solicitações por minuto. Se você pretende usar esse endpoint regularmente para exportar usuários, considere exportar usuários por segmento, que é um processo assíncrono e mais otimizado para extrações de dados maiores.

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

Para obter um exemplo dos dados que podem ser acessados por meio desse endpoint, veja o exemplo a seguir.

### Exemplo de saída de arquivo de exportação do usuário

Objeto de exportação do usuário (incluiremos o mínimo de dados possível - se um campo estiver faltando no objeto, ele deverá ser considerado nulo ou vazio):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" :
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in",
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes":
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged":
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted":
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
