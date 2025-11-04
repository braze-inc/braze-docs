---
nav_title: "POST: Remover ID Externo"
article_title: "POST: Remover ID Externo"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Remover IDs externos."

---
{% api %}
# Remover ID externo
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> Use este endpoint para remover os antigos IDs externos obsoletos de seus usuários. 

Você pode enviar até 50 IDs externos por solicitação. 

{% alert warning %}
Este endpoint remove completamente o ID obsoleto e não pode ser desfeito. Usar este endpoint para remover `external_ids` obsoletos que ainda estão associados a usuários em seu sistema pode impedir permanentemente que você encontre os dados desses usuários.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.external_ids.remove`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Obrigatória | Array de strings | Identificadores externos para os usuários removerem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
Somente IDs obsoletos podem ser removidos; tentar remover um ID externo primário resultará em um erro.
{% endalert %}

## Resposta

A resposta confirmará todas as remoções bem-sucedidas, bem como as remoções malsucedidas com os erros associados. Mensagens de erro no campo `removal_errors` farão referência ao índice no vetor da solicitação original.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

O campo `message` retornará `success` para qualquer solicitação válida. Erros mais específicos são capturados no array `removal_errors`. O campo `message` retorna um erro no caso de:
- Chave de API inválida
- Array `external_ids` vazio
- `external_ids` array com mais de 50 itens
- Limite de frequência atingido (mais de 1.000 solicitações/minuto)

{% endapi %}
