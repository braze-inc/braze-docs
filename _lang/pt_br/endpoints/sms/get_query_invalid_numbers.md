---
nav_title: "OBTER: Consulta de números telefônicos inválidos"
article_title: "OBTER: Consulta de números de telefone inválidos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Consulta de números de telefone inválidos\"."
---
{% api %}
# Consulta de números telefônicos inválidos
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> Use esse ponto de extremidade para obter uma lista de números de telefone que foram marcados como "inválidos" em um determinado período de tempo. Para saber mais, consulte a documentação [sobre o tratamento de números telefônicos inválidos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sms.invalid_phone_numbers`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD| A data de início do intervalo para recuperar números de telefone inválidos deve ser anterior a `end_date`. Isso é tratado como meia-noite no horário UTC pela API. |
| `end_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD | Data final do intervalo para recuperar números telefônicos inválidos. Isso é tratado como meia-noite no horário UTC pela API. |
| `limit` | Opcional | Inteiro | Campo opcional para limitar o número de resultados retornados. O padrão é 100, o máximo é 500. |
| `offset` | Opcional | Inteiro | Ponto inicial opcional na lista a ser recuperado. |
| `phone_numbers` | Opcional <br>(ver nota) | Matriz de strings no formato e.164  | Se fornecido, devolveremos o número de telefone se ele for considerado inválido. |
| `reason` | Opcional <br>(ver nota) | String | Os valores disponíveis são "provider_error" (o erro do provedor indica que o telefone não pode receber SMS) ou "desativado" (o número de telefone foi desativado). Se omitido, todos os motivos são retornados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Você deve fornecer um `start_date` e um `end_date` OU `phone_numbers`. Se você fornecer todos os três, `start_date`, `end_date` e `phone_numbers`, priorizaremos os números de telefone fornecidos e desconsideraremos o intervalo de datas.
{% endalert %}

Se o seu intervalo de datas tiver mais do que o número `limit` de números de telefone inválidos, será necessário fazer várias chamadas à API, aumentando o `offset` a cada vez até que uma chamada retorne menos do que `limit` ou zero resultados.

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta
As entradas são listadas em ordem decrescente.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}
