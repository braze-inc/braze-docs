---
nav_title: "PUT: Definir a chave de autenticação primária do SDK"
article_title: "PUT: Definir a chave de autenticação do SDK primário"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Set primary SDK Authentication key Braze."
---

{% api %}
# Definir a chave primária de autenticação do SDK
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Use esse endpoint para definir uma chave de autenticação SDK como a chave primária do seu aplicativo.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sdk_authentication.primary`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "key_id": "key id"
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatória | String | O identificador da API do aplicativo. |
| `key_id` | Obrigatória | String | A ID da chave de autenticação do SDK a ser marcada como primária. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
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
| `keys` | Vetor | Matriz de todos os objetos de chave de autenticação do SDK. |
| `keys[].id` | String | A ID da chave de autenticação do SDK. |
| `keys[].rsa_public_key` | String | A cadeia de chaves públicas RSA. |
| `keys[].description` | String | Descrição da chave de autenticação do SDK. |
| `keys[].is_primary` | Booleano | Se essa chave é a chave principal de autenticação do SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Regras de validação

Esse endpoint tem as seguintes regras de validação:

- O endereço `key_id` deve ser uma ID de chave de autenticação SDK válida.
- O endereço `app_id` deve ser um identificador de API de aplicativo válido.
- A chave de autenticação do SDK deve existir para o aplicativo especificado.

{% endapi %}
