---
title: Glossário de API ou código
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Esta é a descrição da Pesquisa Google. Caracteres com mais de 160 caracteres são truncados, portanto, seja breve."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 Criar modelo de e-mail
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Envio de e-mail,Criar,Modelo,REST,API
{% endapitags %}

Use as APIs REST de e-mail para gerenciar programaticamente os modelos de e-mail que você armazenou nos dashboards do Braze, na página Modelos e mídias. A Braze oferece dois endpoints para criar e atualizar seus modelos de e-mail.

A resposta desse endpoint inclui um campo para `email_template_id`, que pode ser usado para atualizar o modelo em chamadas subsequentes à API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### EXEMPLO DE RESPOSTA
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### DETALHES DOS PARÂMETROS

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `modified_after`  | Não | String em ISO 8601 | Recupera apenas modelos atualizados no momento ou após o momento determinado. |
| `modified_before`  |  Não | String em ISO 8601 | Recupera apenas modelos atualizados no momento ou antes do momento determinado. |
| `limit` | Não | Número positivo | Número máximo de modelos a serem recuperados; o padrão é 100 se não for fornecido; o valor máximo aceitável é 1000. |
| `offset`  |  Não | Número positivo | Número de modelos a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 Modelo de e-mail disponível na lista
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Obter,E-mail,Modelo,Lista,REST
{% endapitags %}

Use os seguintes endpoints para obter uma lista de modelos disponíveis.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### EXEMPLO DE RESPOSTA
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### DETALHES DOS PARÂMETROS

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id`  | Sim | String | O identificador de API de seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 Campanhas disparam o envio
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Postar, campanhas, disparar, enviar{% endapitags %}

O envio disparado por API permite que você abrigue o conteúdo da mensagem dentro do dashboard da Braze e, ao mesmo tempo, determine quando a mensagem será enviada e para quem por meio de sua API. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### EXEMPLO DE RESPOSTA
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### DETALHES DOS PARÂMETROS

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id`  | Sim | String | O identificador de API de seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 Campanhas disparam o envio
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, campanhas, disparar, enviar{% endapitags %}

Esse ponto de extremidade pode ser usado para registrar eventos personalizados, atributos de usuário e compras para usuários. Você pode incluir até 75 atributos, eventos e objetos de compra por solicitação. Ou seja, só é possível publicar atribuições para até 75 usuários por vez, mas na mesma chamada de API também é possível fornecer até 75 eventos e até 75 compras.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### EXEMPLO DE RESPOSTA
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
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

#### DETALHES DOS PARÂMETROS

| Campo de perfil do usuário | Especificação do tipo de dados |
| ---| --- |
| country | (string) Exigimos que os códigos de país sejam transmitidos à Braze no [padrão ISO-3166-1 alfa-2][17]. |
| current_location | (objeto) Da forma {"longitude": -73.991443, "latitude": 40.753824} |
| data_da_primeira_sessão | (data em que o usuário usou o app pela primeira vez) String no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| data_da_última_sessão | (data em que o usuário usou o app pela última vez) String no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| dob | (data de nascimento) String no formato "AAAA-MM-DD", por exemplo, 1980-12-21. |
| e-mail | (string) |
| email_subscribe | (string) Os valores disponíveis são "opted_in" (explicitamente registrado para receber mensagens de e-mail), "unsubscribed" (explicitamente cancelado inscrição para receber mensagens de e-mail) e "subscribed" (nem optado nem cancelado).  |
| id_externo | (string) Do identificador exclusivo do usuário. |
| Facebook | hash contendo qualquer um dos seguintes itens: `id` (string), `likes` (vetor de strings), `num_friends` (inteiro). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). |
| home_city | (string) |
| image_url | (string) URL da imagem a ser associada ao perfil do usuário. |
| language | (string), exigimos que o idioma seja passado para a Braze no [padrão ISO-639-1][24]. <br>[Lista de idiomas aceitos][1]|
| last_name | (string) |
|marked_email_as_spam_at| (string) Data em que o e-mail do usuário foi marcado como spam. Aparece no formato ISO 8601 ou no formato aaaa-MM-dd'T'HH:mm:ss:SSSZ.|
| telefone | (string) |
| push_subscribe | (string) Os valores disponíveis são "opted_in" (explicitamente registrado para receber mensagens push), "unsubscribed" (explicitamente optado por não receber mensagens push) e "subscribed" (nem nem optou por receber, nem por não receber).  |
| push_tokens | Vetor de objetos com `app_id` e `token` string. Como opção, você pode fornecer um `device_id` para o dispositivo ao qual esse token está associado, por exemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Se o endereço `device_id` não for fornecido, um será gerado aleatoriamente. |
| time_zone | (string) Nome do fuso horário do [banco de dados de fuso horário da IANA][26] (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). Somente os valores válidos de fuso horário serão definidos. |
| twitter | Hash contendo qualquer um dos seguintes itens: `id` (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
