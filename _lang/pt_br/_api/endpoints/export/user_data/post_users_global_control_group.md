---
nav_title: "POST: Exportar perfil de usuário por grupo de controle global"
article_title: "POST: Exportar perfil de usuário por grupo de controle global"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar perfil de usuário por grupo\"."

---
{% api %}
# Exportar perfil de usuário por grupo de controle global
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> Use esse endpoint para exportar todos os usuários de um Grupo de Controle Global.

Os dados de usuários são exportados como vários arquivos de objetos JSON de usuários separados por novas linhas (como um objeto JSON por linha). Todos os usuários de um Grupo de Controle Global são incluídos sempre que os arquivos são gerados. O Braze não armazena um histórico de quando os usuários são adicionados e removidos de um Grupo de Controle Global.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `users.export.global_control_group`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Detalhes de resposta baseados em credenciais

Se você adicionou suas credenciais [do S3][1] ou [do Azure][2] à Braze, cada arquivo terá o upload no seu bucket como um arquivo ZIP com o formato de chave semelhante a `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Se estiver usando o Azure, certifique-se de que a caixa **Tornar este o destino padrão de exportação de dados** esteja marcada na página de visão geral do parceiro do Azure no Braze. Em geral, criamos um arquivo para cada 5.000 usuários para otimizar o processamento. A exportação de segmentos menores em um espaço de trabalho grande pode resultar em vários arquivos. Em seguida, você pode extrair os arquivos e concatenar todos os arquivos `json` em um único arquivo, se necessário. Se você especificar um `output_format` de `gzip`, a extensão do arquivo será `.gz` em vez de `.zip`.

{% details Detalhamento da jornada de exportação para ZIP %}
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

É altamente recomendável configurar suas próprias credenciais do S3 ou do Azure ao usar esse endpoint para aplicar suas próprias políticas de bucket na exportação. Se não tiver fornecido suas credenciais de armazenamento em nuvem, a resposta à solicitação fornecerá o URL onde um ZIP contendo todos os arquivos do usuário pode ser baixado. O URL só se tornará um local válido depois que a exportação estiver pronta.

Esteja ciente de que, se você não fornecer suas credenciais de armazenamento em nuvem, haverá uma limitação na quantidade de dados que você pode exportar desse endpoint. Dependendo dos campos que você está exportando e do número de usuários, a transferência do arquivo pode falhar se ele for muito grande. Uma prática recomendada é especificar quais campos você deseja exportar usando `fields_to_export` e especificando apenas os campos necessários para manter o tamanho da transferência menor. Se você estiver recebendo erros ao gerar o arquivo, considere dividir sua base de usuários em mais segmentos com base em um número de intervalo aleatório (por exemplo, crie um segmento em que o número de intervalo aleatório seja menor que 1.000 ou entre 1.000 e 2.000).

Em qualquer um dos cenários, você tem a opção de fornecer um `callback_endpoint` para receber uma notificação quando a exportação estiver pronta. Se o endereço `callback_endpoint` for fornecido, faremos uma solicitação de postagem para o endereço fornecido quando o download estiver pronto. O corpo da postagem será "success":true. Se você não tiver adicionado suas credenciais de armazenamento em nuvem ao Braze, o corpo da postagem também terá a atribuição `url` com o URL de download como valor.

Bases de usuários maiores resultarão em tempos de exportação mais longos. Por exemplo, um app com 20 milhões de usuários pode levar uma hora ou mais.

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
Atributos personalizados individuais não podem ser exportados. No entanto, todos os atributos personalizados podem ser exportados com a inclusão de custom_attributes na matriz fields_to_export (por exemplo, `['first_name', 'email', 'custom_attributes']`).
{% endalert %}

## Parâmetros de solicitação

| Parâmetro           | Obrigatória  | Tipo de dados        | Descrição                                                                                                                                                    |
| ------------------- | --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | Opcional  | String           | Ponto de extremidade para postar uma URL de download quando a exportação estiver disponível.                                                                                               |
| `fields_to_export`  | Necessário* | Matriz de strings | Nome dos campos de dados de usuários a serem exportados. Também é possível exportar atributos personalizados. <br><br>\*A partir de abril de 2021, as novas contas devem especificar campos específicos para exportação. |
| `output_format`     | Opcional  | String           | Ao usar seu próprio bucket S3, é possível especificar o formato do arquivo como `zip` ou `gzip`. O padrão é o formato de arquivo ZIP.                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
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
| `purchase`s           | Vetor           | Compras que esse usuário fez nos últimos 90 dias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `random_bucket`       | Inteiro         | [Número de bucket aleatório]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) do usuário, usado para criar segmentos uniformemente distribuídos de usuários aleatórios.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | Fuso horário do usuário no mesmo formato do banco de dados de fuso horário da IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Receita total atribuída a esse usuário. A receita total é calculada com base nas compras que o usuário fez durante as janelas de conversão para as campanhas e Canvas que recebeu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Data e hora       | Data e hora em que o usuário desinstala o app. Omitido se o app não tiver sido desinstalado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objeto          | [Objeto de aliases de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contendo `alias_name` e `alias_label`, se houver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Depois que a URL for disponibilizada, ela só será válida por algumas horas. Portanto, é altamente recomendável que você adicione suas próprias credenciais S3 à Braze.

### Exemplo de saída de arquivo de exportação do usuário

Objeto de exportação do usuário (incluiremos o mínimo de dados possível - se um campo estiver faltando no objeto, ele deverá ser considerado nulo ou vazio):

{% tabs %}
{% tab Todos os campos %}

```json
{
    "created_at" : (string),
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
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (string),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
}
```

{% endtab %}
{% tab Saída de amostra %}

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
}
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/

{% endapi %}
