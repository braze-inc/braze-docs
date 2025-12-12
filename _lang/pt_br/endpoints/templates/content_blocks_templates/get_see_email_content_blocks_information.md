---
nav_title: "OBTER: Consulte as informações sobre blocos de conteúdo"
article_title: "OBTER: Consulte Informações sobre blocos de conteúdo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Consulte informações sobre blocos de conteúdo\""
---

{% api %}
# Consulte as informações do bloco de conteúdo
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Use esse ponto de extremidade para chamar informações de seus [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Pré-requisitos
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `content_blocks.info`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `content_block_id`  | Obrigatória | String | O identificador do bloco de conteúdo. <br><br>Você pode encontrar isso listando as informações do bloco de conteúdo por meio de uma chamada de API ou acessando a página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/), rolando até a parte inferior e pesquisando o identificador de API do bloco de conteúdo.|
| `include_inclusion_data`  | Opcional | Booleano | Quando definido como `true`, a API retorna o identificador da API de variação de mensagens de campanhas e Canvas em que esse bloco de conteúdo está incluído, para ser usado em chamadas subsequentes.  Os resultados excluem campanhas ou telas arquivadas ou excluídas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Content Block ID cannot be blank` | Confira se um bloco de conteúdo está listado em sua solicitação e entre aspas (`""`). |
| `Content Block ID is invalid for this workspace` | Esse bloco de conteúdo não existe ou está em uma conta ou espaço de trabalho diferente da empresa. |
| `Content Block has been deleted—content not available` | Esse bloco de conteúdo, embora possa ter existido anteriormente, foi excluído. |
| `Include Inclusion Data—error` | Esse parâmetro aceita apenas valores booleanos (verdadeiro ou falso). Certifique-se de que o valor de `include_inclusion_data` não esteja encapsulado entre aspas (`""`), o que faz com que o valor seja enviado como uma string. Consulte [os parâmetros da solicitação](#request-parameters) para obter detalhes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
