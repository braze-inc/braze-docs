---
nav_title: "OBTER: Consulta de e-mails hard bounce"
article_title: "OBTER: Consulta de e-mails hard bounce"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint da Braze \"Consulta de e-mails hard bounce\"."

---
{% api %}
# Consulta de e-mails hard bounce
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Use esse ponto de extremidade para obter uma lista de endereços de e-mail que sofreram "hard bounce" em suas mensagens de e-mail em um determinado período de tempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.hard_bounces`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional* | String no formato YYYY-MM-DD| \*É necessário um dos sites `start_date` ou `email`. Essa é a data de início do intervalo para recuperar hard bounces e deve ser anterior a `end_date`. Isso é tratado como meia-noite no horário UTC pela API. |
| `end_date` | Obrigatória | String no formato YYYY-MM-DD | Data final do intervalo para recuperar hard bounces. Isso é tratado como meia-noite no horário UTC pela API. |
| `limit` | Opcional | Inteiro | Campo opcional para limitar o número de resultados retornados. O padrão é 100, o máximo é 500. |
| `offset` | Opcional | Inteiro | Ponto inicial opcional na lista a ser recuperado. |
| `email` | Opcional* | String | \*É necessário um dos sites `start_date` ou `email`. Se fornecido, retornaremos se o usuário sofreu hard bounce ou não. Verifique se as strings de e-mail estão formatadas corretamente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Você deve fornecer um `end_date`, e um `email` ou um `start_date`. Se você fornecer todos os três, `start_date`, `end_date`, e um `email`, priorizaremos os e-mails fornecidos e desconsideraremos o intervalo de datas.
{% endalert %}

Se o seu intervalo de datas tiver mais do que o número `limit` de hard bounces, será necessário fazer várias chamadas à API, aumentando a cada vez o `offset` até que uma chamada retorne menos do que `limit` ou zero resultados. A inclusão dos parâmetros `offset` e `limit` com `email` pode retornar uma resposta vazia.

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta
As entradas são listadas em ordem decrescente.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
