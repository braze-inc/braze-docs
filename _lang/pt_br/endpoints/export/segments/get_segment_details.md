---
nav_title: "OBTER: Detalhes do segmento de exportação"
article_title: "OBTER: Detalhes do segmento de exportação"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o ponto de extremidade do Braze dos detalhes do segmento de exportação."

---
{% api %}
# Detalhes do segmento de exportação
{% apimethod get %}
/segments/details
{% endapimethod %}

> Use esse endpoint para recuperar informações relevantes sobre um segmento, que pode ser identificado pelo endereço `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `segments.details`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação

| Parâmetro    | Obrigatória | Tipo de dados | Descrição            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Obrigatória | String | Consulte [Identificador da API de segmento]({{site.baseurl}}/api/identifier_types/).<br><br> O [endereço]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) `segment_id` para um determinado segmento pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) em sua conta Braze ou você pode usar o [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
