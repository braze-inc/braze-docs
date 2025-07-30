---
nav_title: "Objeto de atribuições do usuário"
article_title: Objeto de atribuições do usuário da API
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de atribuições do usuário."

---

# Objeto de atribuições do usuário

> Uma solicitação de API com qualquer campo no objeto de atribuições criará ou atualizará um atributo desse nome com o valor fornecido no perfil de usuário especificado. 

Use os nomes de campo do perfil de usuário do Braze (listados a seguir ou qualquer outro listado na seção de [campos de perfil de usuário do Braze](#braze-user-profile-fields)) para atualizar esses valores especiais no perfil de usuário no dashboard ou adicionar seus próprios dados de atributo personalizado ao usuário.

## Corpo do objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

- [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Para remover uma atribuição de perfil, defina-a como `null`. Alguns campos, como `external_id` e `user_alias`, não podem ser removidos depois de serem adicionados a um perfil de usuário.

#### Atualizar apenas os perfis existentes

Se desejar atualizar apenas os perfis de usuário existentes na Braze, passe a chave `_update_existing_only` com o valor `true` no corpo da solicitação. Se esse valor for omitido, a Braze criará um novo perfil de usuário se o `external_id` ainda não existir.

{% alert note %}
Se você estiver criando um perfil de usuário somente de alias por meio do endpoint `/users/track`, `_update_existing_only` deverá ser definido como `false`. Se esse valor for omitido, o perfil somente de alias não será criado.
{% endalert %}

#### Importação de token por push

Antes de importar tokens por push para o Braze, verifique novamente se é necessário. Quando os SDKs da Braze são implementados, eles lidam com tokens por push automaticamente, sem a necessidade de fazer upload deles por meio da API.

Se achar que precisa fazer upload deles por meio da API, eles podem ser carregados para usuários identificados ou usuários anônimos. Isso significa que um `external_id` precisa estar presente ou que os usuários anônimos devem ter o sinalizador `push_token_import` definido como `true`. 

{% alert note %}
Ao importar tokens por push de outros sistemas, um `external_id` nem sempre está disponível. Para manter a comunicação com esses usuários durante a transição para o Braze, é possível importar os tokens legados para usuários anônimos sem fornecer `external_id` especificando `push_token_import` como `true`.
{% endalert %}

Ao especificar `push_token_import` como `true`:

* `external_id` e `braze_id` **não** devem ser especificados
* O objeto de atribuição **deve** conter um token por push
* Se o token já existir no Braze, a solicitação será ignorada; caso contrário, o Braze criará um perfil de usuário temporário e anônimo para cada token, a fim de ativar a possibilidade de continuar enviando mensagens para essas pessoas

Após a importação, à medida que cada usuário iniciar a versão ativada pelo Braze do seu app, o Braze moverá automaticamente o token por push importado para o perfil de usuário do Braze e limpará o perfil temporário.

O Braze verificará uma vez por mês para encontrar qualquer perfil anônimo com o sinalizador `push_token_import` que não tenha um token por push. Se o perfil anônimo não tiver mais um token por push, nós o excluiremos. No entanto, se o perfil anônimo ainda tiver um token por push, o que sugere que o usuário real ainda não fez login no dispositivo com o referido token por push, não faremos nada.

Para saber mais, consulte [Migração de tokens por push]({{site.baseurl}}/help/help_articles/push/push_token_migration/).

#### Tipos de dados de atributos personalizados

Os seguintes tipos de dados podem ser armazenados como um atributo personalizado:

| Tipo de dados | Notas |
| --- | --- |
| Matrizes | Há suporte para matrizes de atributos personalizados. Adicionar um elemento a uma matriz de atributos personalizados anexa o elemento ao final da matriz, a menos que ele já esteja presente, caso em que ele é movido de sua posição atual para o final da matriz.<br><br>Por exemplo, se uma matriz `['hotdog','hotdog','hotdog','pizza']` for importada, ela será exibida na atribuição da matriz como `['hotdog', 'pizza']` porque somente valores exclusivos são suportados.<br><br>Além de definir os valores de uma matriz dizendo algo como `"my_array_custom_attribute":[ "Value1", "Value2" ]`, você pode adicionar a matrizes existentes fazendo algo como `"my_array_custom_attribute" : { "add" : ["Value3"] },` ou remover valores de uma matriz fazendo algo como `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>O número máximo de elementos em matrizes de atributos personalizados tem como padrão 25, mas pode ser aumentado até 100 para uma matriz individual. Para saber mais, consulte [Matrizes]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays). |
| Array de objetos | O vetor de objetos permite que você defina uma lista de objetos em que cada objeto contém um conjunto de atribuições. Isso pode ser útil se for necessário armazenar vários conjuntos de dados relacionados a um usuário, como estadias em hotéis, histórico de compras ou preferências. <br><br> Por exemplo, é possível definir um atributo personalizado em um perfil de usuário chamado `hotel_stays`. Esse atributo personalizado pode ser definido como um vetor de objeto em que cada objeto representa uma estadia separada, com atributos como `hotel_name`, `check_in_date`, `nights_stayed`. Para obter mais detalhes, consulte [este exemplo](#array-of-objects-example). |
| Booleanos | `true` ou `false` |
| Datas | Deve ser armazenado no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Note que "T" é um designador de tempo, não um espaço reservado, e não deve ser alterado ou removido. <br><br>As atribuições de horário sem um fuso horário terão como padrão a meia-noite UTC (e serão formatadas no dashboard como o equivalente à meia-noite UTC no fuso horário da empresa). <br><br> Os eventos com registros de data e hora no futuro terão como padrão a hora atual. <br><br> Para atributos personalizados regulares, se o ano for menor que 0 ou maior que 3000, a Braze armazenará esses valores como strings no usuário. |
| Floats | Os atributos personalizados Float são números positivos ou negativos com um ponto decimal. Por exemplo, você pode usar flutuadores para armazenar saldos de contas ou classificações de usuários para produtos ou serviços. |
| Inteiros | Os atributos personalizados inteiros podem ser incrementados por números inteiros positivos ou negativos, atribuindo a eles um objeto com o campo "inc" e o valor pelo qual você deseja incrementá-los. <br><br>Exemplo: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Atributos personalizados aninhados | Os atributos personalizados aninhados definem um conjunto de atributos como uma propriedade de outro atributo. Ao definir um objeto de atributo personalizado, você define um conjunto de atributos adicionais para esse objeto. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Strings | Os atributos personalizados de string são sequências de caracteres usadas para armazenar dados de texto. Por exemplo, é possível usar strings para armazenar nomes e sobrenomes, endereços de e-mail ou preferências. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obter informações sobre quando usar um evento personalizado em vez de um atributo personalizado, consulte nossa respectiva documentação sobre [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) e [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Exemplo de vetor de objetos 

Esse vetor de objetos permite que você crie segmentos com base em critérios específicos dentro das estadias e personalize suas mensagens usando os dados de cada estadia com modelos Liquid.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Campos de perfil de usuário do Braze {#braze-user-profile-fields}

{% alert important %}
Os seguintes campos de perfil de usuário diferenciam maiúsculas de minúsculas, portanto, certifique-se de referenciar esses campos em minúsculas.
{% endalert %}

| Campo de perfil do usuário | Especificação do tipo de dados |
| ---| --- |
| nome_alias | (string) |
| alias_label | (string) |
| braze_id | (string, opcional) Quando um perfil de usuário é reconhecido pelo SDK, um perfil de usuário anônimo é criado com um `braze_id` associado. O endereço `braze_id` é atribuído automaticamente pela Braze, não pode ser editado e é específico do dispositivo. | 
| country | (string) Exigimos que os códigos de país sejam transmitidos à Braze no [padrão ISO-3166-1 alfa-2](http://en.wikipedia.org/wiki/ISO_3166-1). Nossa API se esforçará ao máximo para mapear os países recebidos em diferentes formatos. Por exemplo, "Austrália" pode ser mapeado para "AU". No entanto, se a entrada não corresponder a um determinado [padrão ISO-3166-1 alfa-2](http://en.wikipedia.org/wiki/ISO_3166-1), o valor do país será definido como `NULL`. <br><br>A configuração de `country` em um usuário por importação de CSV ou API impedirá que a Braze capture automaticamente essas informações por meio do SDK. |
| current_location | (objeto) Da forma {"longitude": -73.991443, "latitude": 40.753824} |
| data_da_primeira_sessão | (data em que o usuário usou o app pela primeira vez) String no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| data_da_última_sessão | (data em que o usuário usou o app pela última vez) String no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (data de nascimento) String no formato "AAAA-MM-DD", por exemplo, 1980-12-21. |
| e-mail | (string) |
| email_subscribe | (string) Os valores disponíveis são "opted_in" (explicitamente registrado para receber mensagens de e-mail), "unsubscribed" (explicitamente cancelado inscrição para receber mensagens de e-mail) e "subscribed" (nem optado nem cancelado).  |
| email_open_tracking_disabled |(booleano) `true` ou `false` aceito. Defina como `true` para desativar a adição do pixel de rastreamento de abertura a todos os futuros e-mails enviados a esse usuário. Disponível apenas para SparkPost e SendGrid.|
| email_click_tracking_disabled |(booleano) `true` ou `false` aceito. Defina como `true` para desativar o rastreamento de cliques para todos os links em um e-mail futuro enviado a esse usuário. Disponível apenas para SparkPost e SendGrid.|
| external_id | (string) Um identificador exclusivo para um perfil de usuário. Depois de atribuído um `external_id`, o perfil do usuário é identificado nos dispositivos do usuário. Na primeira instância de atribuir um external_id a um perfil de usuário desconhecido, todos os dados do perfil de usuário existentes serão migrados para o novo perfil de usuário. |
| Facebook | hash contendo qualquer um dos seguintes itens: `id` (string), `likes` (vetor of strings), `num_friends` (inteiro). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). |
| home_city | (string) |
| language | (string), exigimos que a linguagem seja passada para a Braze no [padrão ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Para saber os idiomas compatíveis, consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>A configuração de `language` em um usuário por importação de CSV ou API impedirá que a Braze capture automaticamente essas informações por meio do SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (string) Data em que o e-mail do usuário foi marcado como spam. Aparece no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| telefone | (string) Recomendamos fornecer números de telefone no formato [E.164](https://en.wikipedia.org/wiki/E.164). Para obter detalhes, consulte [Números de telefone do usuário]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (string) Os valores disponíveis são "opted_in" (explicitamente registrado para receber mensagens push), "unsubscribed" (explicitamente optado por não receber mensagens push) e "subscribed" (nem nem optou por receber, nem por não receber).  |
| push_tokens | Vetor de objetos com `app_id` e `token` string. Como opção, você pode fornecer um `device_id` para o dispositivo ao qual esse token está associado, por exemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Se o endereço `device_id` não for fornecido, um será gerado aleatoriamente. |
| subscription_groups| Vetor de objetos com as strings `subscription_group_id` e `subscription_state`, por exemplo, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Os valores disponíveis para `subscription_state` são "subscribed" (inscrito) e "unsubscribed" (cancelado inscrição).|
| time_zone | (string) Nome do fuso horário do [banco de dados de fuso horário da IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). Somente os valores válidos de fuso horário serão definidos. |
| twitter | Hash contendo qualquer um dos seguintes itens: `id` (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Os valores de idioma definidos explicitamente por meio dessa API terão precedência sobre as informações de localização que o Braze recebe automaticamente do dispositivo.

####  Exemplo de solicitação de atribuição de usuário

Este exemplo contém quatro objetos de atribuição de usuário, de um total de 75 objetos de atribuição permitidos por chamada de API.

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

