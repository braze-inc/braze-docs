---
nav_title: "POST: Remover e-mails com hard bounce"
article_title: "POST: Remover e-mails com hard bounce"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint \"Remover endereços de e-mail com hard bounce da Braze\"."

---
{% api %}
# Remover e-mails com hard bounce
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Use esse endpoint para remover endereços de e-mail de sua lista de bounce da Braze e da lista de bounce mantida por seu provedor de e-mail.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.bounce.remove`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| ----------|-----------| ---------|------ |
| `email` | Obrigatória | String ou matriz | Envio de e-mail em string para modificar ou uma matriz de até 50 endereços de e-mail para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
