---
nav_title: "OBTER: Consulta à lista de endereços de e-mail que cancelaram inscrição"
article_title: "OBTER: Consulta à lista de endereços de e-mail cancelados"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint Retrieve list of or query email unsubscribes do Braze."

---
{% api %}
# Consulta à lista de endereços de e-mail que cancelaram inscrição
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Use esse endpoint para retornar os e-mails mais recentes que cancelaram inscrição durante o período de `start_date` a `end_date`. Para obter um histórico completo do estado da inscrição, use o [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) para rastrear esses dados.

Você pode usar esse endpoint para configurar uma sincronização bidirecional entre o Braze e outros sistemas de e-mail ou seu próprio banco de dados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.unsubscribe`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ---------|------ |
| `start_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD| Data de início do intervalo para recuperar os cancelamentos de inscrição, que deve ser anterior a end_date.. A API trata essa data como meia-noite no horário UTC. |
| `end_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD | Data final do intervalo para recuperar cancelamentos de inscrição. Isso é tratado como meia-noite no horário UTC pela API. |
| `limit` | Opcional | Inteiro | Campo opcional para limitar o número de resultados retornados. O padrão é 100, o máximo é 500. |
| `offset` | Opcional | Inteiro | Ponto inicial opcional na lista a ser recuperado. |
| `sort_direction` | Opcional | String | Passe o valor `asc` para classificar os cancelamentos de inscrição do mais antigo para o mais recente. Passe em `desc` para classificar do mais recente para o mais antigo. Se `sort_direction` não estiver incluído, a ordem padrão será da mais recente para a mais antiga. |
| `email` | Opcional <br>(ver nota) | String | Se fornecido, retornaremos se o usuário cancelou ou não a inscrição. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Você precisa fornecer um `end_date`, bem como um `email` ou um `start_date`.
{% endalert %}

Se o seu intervalo de datas tiver mais do que `limit` número de cancelamentos de inscrição, será necessário fazer várias chamadas à API, aumentando sempre o `offset` até que uma chamada retorne menos do que `limit` ou zero resultados.

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
