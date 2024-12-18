---
nav_title: "POST: Envio de e-mails para a lista de proibições"
article_title: "POST: Envio de e-mails para a lista de proibições"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "Este artigo descreve os detalhes sobre o endpoint da lista de proibições de e-mails do Braze."

---
{% api %}
# Envio de e-mails para a lista de proibições
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
A Braze lançou o [endpoint`/email/blocklist` ]({{site.baseurl}}/api/endpoints/email/post_blocklist/) com a mesma funcionalidade do endpoint `/email/blacklist`. Em vez disso, recomendamos que você use o ponto de extremidade `/email/blocklist`.
{% endalert %}

> Use esse endpoint para cancelar a inscrição de um usuário no e-mail e marcá-lo como hard bounce.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.blacklist`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| -----------|----------| --------|------- |
| `email` | Obrigatória | String ou matriz | Envio de e-mail em string para a lista de proibições ou uma matriz de até 50 endereços de e-mail para a lista de proibições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}
