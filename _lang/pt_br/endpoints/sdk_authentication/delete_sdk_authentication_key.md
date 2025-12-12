---
nav_title: "DELETE: Remover a chave de autenticação do SDK"
article_title: "DELETE: Remover a chave de autenticação do SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Delete SDK Authentication key Braze."
---

{% api %}
# Excluir a chave de autenticação do SDK
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Use esse endpoint para excluir uma chave de autenticação SDK do seu aplicativo.

{% alert important %}
A chave primária não pode ser excluída. Se você tentar excluir a chave primária, esse ponto de extremidade retornará um erro.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sdk_authentication.delete`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatória | String | O identificador da API do aplicativo. |
| `key_id` | Obrigatória | String | A ID da chave de autenticação do SDK a ser excluída. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## Parâmetros de resposta

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `keys` | Vetor | Matriz de objetos de chave de autenticação do SDK restantes. |
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
- A chave primária de autenticação do SDK não pode ser excluída.

{% endapi %}
