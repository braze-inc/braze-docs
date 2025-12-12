---
nav_title: "OBTER: Lista de blocos de conteúdo disponíveis"
article_title: "OBTER: Listar blocos de conteúdo disponíveis"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Listar blocos de conteúdo disponíveis\""

---
{% api %}
# Lista de blocos de conteúdo disponíveis
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Use esse ponto de extremidade para listar suas informações de [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Pré-requisitos
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `content_blocks.list`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `modified_after`  | Opcional | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera apenas blocos de conteúdo atualizados no momento ou após o momento determinado. |
| `modified_before`  |  Opcional | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera apenas blocos de conteúdo atualizados antes ou no momento determinado. |
| `limit` | Opcional | Número positivo | Número máximo de blocos de conteúdo a serem recuperados. O padrão é 100 se não for fornecido, com um valor máximo aceitável de 1000. |
| `offset`  |  Opcional | Número positivo | Número de blocos de conteúdo a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Modified after time is invalid` | A data fornecida não é uma data válida ou analisável. Reformate esse valor da string no formato ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | A data fornecida não é uma data válida ou analisável. Reformate esse valor da string no formato ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Altere o valor de `modified_after` para uma hora anterior à hora de `modified_before`. |
| `Content Block number limit is invalid` | O parâmetro `limit` precisa ser um número inteiro (número positivo) maior que 0. |
| `Content Block number limit must be greater than 0` | Altere o parâmetro `limit` para um número inteiro maior que 0. |
| `Content Block number limit exceeds maximum of 1000` | Altere o parâmetro `limit` para um número inteiro menor que 1000. |
| `Offset is invalid` | O parâmetro `offset` deve ser um número inteiro maior que 0. |
| O deslocamento precisa ser maior que 0 | Altere o parâmetro `offset` para um número inteiro maior que 0. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
