---
nav_title: "POST: Criar chave de autenticação do SDK"
article_title: "POST: Criar chave de autenticação do SDK"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint do Braze Create SDK Authentication key."
---

{% api %}
# Criar chave de autenticação do SDK
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Use esse endpoint para criar uma nova chave de autenticação do SDK para seu app.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `sdk_authentication.create`.

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
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatória | String | O identificador da API do app. |
| `rsa_public_key_str` | Obrigatória | String | A string da chave pública RSA. Deve ser uma chave pública RSA válida ou retornará um erro. |
| `description` | Obrigatória | String | Descrição da chave de autenticação do SDK. |
| `make_primary` | Opcional | Booleano | Se definida como `true`, essa chave se tornará a chave primária de autenticação do SDK quando for criada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## Resposta
```json
{
  "id": "key id"
}
```

## Parâmetros de resposta

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `id` | String | A ID da chave de autenticação do SDK recém-criada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Regras de validação

Esse endpoint tem as seguintes regras de validação:

- Você pode ter até 3 chaves de autenticação do SDK por app.
- A string da chave pública RSA deve ser uma chave pública RSA válida no formato adequado.
- O endereço `app_id` deve ser um identificador válido da API do app.
- A descrição não pode estar vazia.

{% endapi %}
