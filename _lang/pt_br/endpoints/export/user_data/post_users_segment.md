---
nav_title: "POST: Exportar perfil de usuário por segmento"
article_title: "POST: Exportar perfil de usuário por segmento"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Exportar perfil de usuário por segmento da Braze."

---
{% api %}
# Exportar perfil de usuário por segmento
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> Use esse ponto de extremidade para exportar todos os usuários de um segmento. 

{% alert important %}
Ao usar esse endpoint, observe o seguinte:<br><br>1\. O campo `fields_to_export` nessa solicitação da API é **obrigatório**.<br>2\. Os campos para `custom_events`, `purchases`, `campaigns_received` e `canvases_received` contêm apenas dados dos últimos 90 dias.
{% endalert %}

Os dados de usuários são exportados como vários arquivos de objetos JSON de usuários separados por novas linhas (como um objeto JSON por linha). Os dados são exportados para um URL gerado automaticamente ou para um bucket S3 se essa integração já estiver configurada.

Note que uma empresa pode executar no máximo uma exportação por segmento usando esse endpoint em um determinado momento. Aguarde a conclusão da exportação antes de tentar novamente. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `users.export.segment`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Detalhes de resposta baseados em credenciais

Se você tiver adicionado suas credenciais do [S3][1], [Azure][2] ou [Google Cloud Storage][3] ao Braze, cada arquivo será feito upload em seu bucket como um arquivo ZIP com o formato de chave semelhante a `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Se estiver usando o Azure, certifique-se de que a caixa **Tornar este o destino padrão de exportação de dados** esteja marcada na página de visão geral do parceiro do Azure no Braze. Em geral, criamos um arquivo para cada 5.000 usuários para otimizar o processamento. A exportação de segmentos menores em um espaço de trabalho grande pode resultar em vários arquivos. Em seguida, você pode extrair os arquivos e concatenar todos os arquivos `json` em um único arquivo, se necessário. Se você especificar um `output_format` de `gzip`, a extensão do arquivo será `.gz` em vez de `.zip`.

{% details Export pathing breakdown for ZIP %}
**Formato ZIP:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Exemplo de ZIP:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Propriedade                        | Informações                                                                              | Mostrado no exemplo como                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | Corrigido com base no nome de seu bucket.                                                     | `braze.docs.bucket`                    |
| `segment-export`                | Corrigido.                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | Incluído na solicitação de exportação.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | A data em que o retorno de chamada bem-sucedido foi recebido.                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | Um UUID aleatório gerado pelo Braze no momento da solicitação.                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Hora Unix (segundos desde 2017-01-01:00:00:00Z) em que a exportação foi solicitada em UTC. | `1556044807`                           |
| `filename`                      | Aleatório por arquivo.                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

É altamente recomendável configurar suas próprias credenciais do S3 ou do Azure ao usar esse endpoint para aplicar suas próprias políticas de bucket na exportação. Se não tiver suas credenciais de armazenamento em nuvem, a resposta à solicitação fornecerá o URL onde um arquivo ZIP contendo todos os arquivos do usuário pode ser baixado. O URL só se tornará um local válido depois que a exportação estiver pronta. 

Esteja ciente de que, se você não fornecer suas credenciais de armazenamento em nuvem, há uma limitação na quantidade de dados que você pode exportar desse endpoint. Dependendo dos campos que você está exportando e do número de usuários, a transferência do arquivo pode falhar se ele for muito grande. Uma prática recomendada é especificar quais campos você deseja exportar usando `fields_to_export` e especificar apenas os campos necessários para manter o tamanho da transferência menor. Se você estiver recebendo erros ao gerar o arquivo, considere dividir sua base de usuários em mais segmentos com base em um número de balde aleatório (por exemplo, crie um segmento em que um número de balde aleatório seja menor que 1.000 ou entre 1.000 e 2.000).

Em qualquer um dos cenários, você tem a opção de fornecer um `callback_endpoint` para receber uma notificação quando a exportação estiver pronta. Se o endereço `callback_endpoint` for fornecido, faremos uma solicitação de postagem para o endereço fornecido quando o download estiver pronto. O corpo da postagem será "success":true. Se você não tiver adicionado credenciais S3 ao Braze, o corpo da postagem também terá a atribuição `url` com o URL de download como valor.

Bases de usuários maiores resultarão em tempos de exportação mais longos. Por exemplo, um app com 20 milhões de usuários pode levar uma hora ou mais.

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## Parâmetros de solicitação

| Parâmetro                     | Obrigatória  | Tipo de dados        | Descrição                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id`                  | Obrigatória  | String           | Identificador do segmento a ser exportado. Consulte [identificador de segmento]({{site.baseurl}}/api/identifier_types/).<br><br>O [endereço]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) `segment_id` para um determinado segmento pode ser encontrado na página de [chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) em sua conta Braze ou você pode usar o [ponto de extremidade da lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). |
| `callback_endpoint`           | Opcional  | String           | Ponto de extremidade para postar uma URL de download quando a exportação estiver disponível.                                                                                                                                                                                                                                                                                                                                             |
| `fields_to_export`            | Obrigatório* | Matriz de strings | Nome dos campos de dados de usuários a serem exportados. Você também pode exportar todos os atributos personalizados incluindo `custom_attributes` nesse parâmetro. <br><br>\*A partir de abril de 2021, as novas contas devem especificar campos específicos para exportação.                                                                                                                                                                                        |
| `custom_attributes_to_export` | Opcional  | Matriz de strings | Nome do atributo personalizado específico a ser exportado. Até 500 atributos personalizados podem ser exportados. Para criar e gerenciar atributos personalizados no dashboard, acesse **Configurações de dados** > Atributos personalizados.                                                                                                                                                                                                          |
| `output_format`               | Opcional  | String           | O formato de saída de seu arquivo. O padrão é o formato de arquivo `zip`. Se estiver usando seu próprio bucket S3, você poderá especificar `zip` ou `gzip`.                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Se `custom_attributes` estiver incluído no parâmetro `fields_to_export`, todos os atributos personalizados serão exportados, independentemente do que estiver em `custom_attributes_to_export`. Se seu objetivo for exportar atribuições específicas, `custom_attributes` não deve ser incluído no parâmetro `fields_to_export`. Em vez disso, use o parâmetro `custom_attributes_to_export`.
{% endalert %}

## Exemplo de solicitação para exportar todos os atributos personalizados
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## Exemplo de solicitação para exportar atributos personalizados específicos
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
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
| `push_subscribe`      | String          | Status da inscrição push do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | String          | Status da inscrição de e-mail do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
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
| `push_tokens`         | Vetor           | Informações sobre os tokens por push do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `random_bucket`       | Inteiro         | [Número de bucket aleatório]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) do usuário, usado para criar segmentos uniformemente distribuídos de usuários aleatórios.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | Fuso horário do usuário no mesmo formato do banco de dados de fuso horário da IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Receita total atribuída a esse usuário. A receita total é calculada com base nas compras que o usuário fez durante as janelas de conversão para as campanhas e Canvas que recebeu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Data e hora       | Data e hora em que o usuário desinstala o app. Omitido se o app não tiver sido desinstalado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objeto          | [Objeto de aliases de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contendo `alias_name` e `alias_label`, se houver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Lembretes importantes

- Os campos para `custom_events`, `purchases`, `campaigns_received` e `canvases_received` conterão apenas dados dos últimos 90 dias.
- Tanto `custom_events` quanto `purchases` contêm campos para `first` e `count`. Esses dois campos refletirão informações de todo o período e não se limitarão apenas aos dados dos últimos 90 dias. Por exemplo, se um determinado usuário realizou o evento pela primeira vez há 90 dias, isso será refletido com precisão no campo `first`, e o campo `count` também levará em conta os eventos que ocorreram antes dos últimos 90 dias.
- O número de exportações de segmentos simultâneas que uma empresa pode executar no nível do endpoint é limitado a 100. As tentativas que ultrapassarem esse limite resultarão em um erro.
- A tentativa de exportar um segmento uma segunda vez enquanto o primeiro trabalho de exportação ainda estiver em execução resultará em um erro 429.

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Depois que a URL for disponibilizada, ela só será válida por algumas horas. Portanto, é altamente recomendável que você adicione suas próprias credenciais S3 à Braze.

Se você ver `object_prefix` na sua resposta da API e não houver URL para baixar os dados, isso significa que você já tem um bucket Amazon S3 configurado para este endpoint. Qualquer dado exportado usando este endpoint irá diretamente para o seu bucket S3.

## Exemplo de saída de arquivo de exportação do usuário

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

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}
