---
nav_title: "GET: [Nome do endpoint]"
article_title: "Exemplo de layout: GET: [Nome do endpoint]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "Este artigo descreve o uso e os parâmetros para usar o endpoint Get [nome do endpoint] Braze."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Consulta ou lista [Endpoint do item "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Use esse ponto de extremidade para obter uma lista de números de telefone que foram considerados "inválidos" em um determinado período de tempo.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limite de taxa

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

<!--This is where you can give more information about your endpoint parameters. -->

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD| A data de início do intervalo para recuperar números de telefone inválidos deve ser anterior a `end_date`. Isso é tratado como meia-noite no horário UTC pela API. |
| `end_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD | Data final do intervalo para recuperar números telefônicos inválidos. Isso é tratado como meia-noite no horário UTC pela API. |
| `limit` | Opcional | Inteiro | Campo opcional para limitar o número de resultados retornados. O padrão é 100, o máximo é 500. |
| `offset` | Opcional | Inteiro | Ponto inicial opcional na lista a ser recuperado. |
| `phone_numbers` | Opcional <br>(ver nota) | Matriz de strings no formato e.164  | Se fornecido, devolveremos o número de telefone se ele for considerado inválido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Você deve fornecer um `start_date` e um `end_date` OU `phone_numbers`. Se você fornecer todos os três, `start_date`, `end_date` e `phone_numbers`, priorizaremos os números de telefone fornecidos e desconsideraremos o intervalo de datas.
{% endalert %}

## Exemplo de solicitação

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta

<!-- An example response that defines the different variables returned-->
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
