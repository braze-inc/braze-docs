---
nav_title: "POST: Criar IDs de envio"
article_title: "POST: Criar IDs de envio"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint \"Criar IDs de envio\" da Braze"

---
{% api %}
# Criar IDs de envio
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Use esse ponto de extremidade para criar IDs de envio que possam ser usados para enviar mensagens e rastrear o desempenho das mensagens programaticamente, sem a criação de campanhas para cada envio.

Usar o identificador de envio para rastrear e enviar mensagens é útil se estiver planejando gerar e enviar conteúdo programaticamente.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `sends.id.create`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatória | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Opcional | String | Consulte [enviar identificador]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Resposta

### Exemplo de resposta bem-sucedida

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
