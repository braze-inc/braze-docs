---
nav_title: "OBTER: Listar chaves de autenticação do SDK"
article_title: "OBTER: Listar chaves de autenticação do SDK"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de chaves de autenticação do SDK Listar Braze."
---

{% api %}
# Listar chaves de autenticação do SDK
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Use este endpoint para recuperar todas as chaves de autenticação do SDK para seu aplicativo.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sdk_authentication.keys`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatória | String | O identificador da API do aplicativo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## Parâmetros de resposta

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `keys` | Vetor | Array de objetos de chaves de autenticação do SDK. |
| `keys[].id` | String | O ID da chave de autenticação do SDK. |
| `keys[].rsa_public_key` | String | A string da chave pública RSA. |
| `keys[].description` | String | Descrição da chave de autenticação do SDK. |
| `keys[].is_primary` | Booleano | Se esta chave é a chave de autenticação do SDK primária. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Regras de validação

Este endpoint possui as seguintes regras de validação:

- O parâmetro `app_id` deve ser um identificador de API de aplicativo válido.
- O aplicativo deve existir em seu espaço de trabalho.

{% endapi %}
