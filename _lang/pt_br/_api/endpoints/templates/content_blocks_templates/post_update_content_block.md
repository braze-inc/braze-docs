---
nav_title: "POST: Atualizar bloco de conteúdo"
article_title: "POST: Atualizar bloco de conteúdo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve o endpoint da Braze \"Atualizar blocos de conteúdo\"."

---
{% api %}
# Atualizar bloco de conteúdo
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> Use esse endpoint para atualizar um [bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Pré-requisitos
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `content_blocks.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `content_block_id`|	Obrigatória |	String | O identificador de API de seu bloco de conteúdo.|
| `name` | Opcional | String | Nome do bloco de conteúdo. Deve ter menos de 100 caracteres. |
| `description` | Opcional | String | Descrição do bloco de conteúdo. Deve ter menos de 250 caracteres. |
| `content` | Opcional | String | Conteúdo HTML ou de texto em blocos de conteúdo.
| `state` | Opcional | String | Escolha `active` ou `draft`. O padrão é `active` se não for especificado. |
| `tags` | Opcional | Matriz de strings | [As tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) já devem existir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | Certifique-se de que seu conteúdo esteja encapsulado entre aspas (`""`). |
| `Content must be smaller than 50kb` | O conteúdo no seu bloco de conteúdo deve ser inferior a 50 KB no total. |
| `Content contains malformed liquid` | O Liquid fornecido não é válido ou não pode ser analisado. Tente novamente com um Liquid válido ou entre em contato com o suporte. |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | Certifique-se de que a descrição do bloco de conteúdo esteja encapsulada entre aspas (`""`). |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | Os nomes dos blocos de conteúdo podem incluir qualquer um dos seguintes caracteres: as letras (maiúsculas ou minúsculas) `A` a `Z`, os números `0` a `9`, os traços `-` e os sublinhados `_`. Não pode conter caracteres não alfanuméricos, como emojis, `!`, `@`, `~`, `&`, e outros caracteres "especiais". |
| `Content Block with this name already exists` | Tente um nome diferente. |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | As tags devem ser formatadas como uma matriz de strings, por exemplo, `["marketing", "promotional", "transactional"]`. |
| `All tags must be strings` | Confira se as tags estão entre aspas (`""`). |
| `Some tags could not be found` | Para adicionar uma tag ao criar um bloco de conteúdo, a tag já deve existir na Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
