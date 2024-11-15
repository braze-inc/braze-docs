---
nav_title: "OBTER: Alias de link de lista para campanhas"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Este artigo descreve detalhes sobre o endpoint da Braze de Listar alias de link."
---
{% api %}
# Listar o alias do link para a campanha
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Use esse ponto de extremidade para listar o alias de link definido em uma variante de mensagem de campanha específica.

{% apiref postman %}  {% endapiref %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `campaign_id`  | Obrigatória | String | Consulte o [identificador da API da campanha]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier).|
| `message_variation_id `  |  Obrigatória | String | Identificador da API da variante de mensagens. Isso pode ser encontrado na página de detalhes de uma campanha, na seção **API Identifier**. |
| `includes_link_id` | Opcional | String | Um identificador de link específico (conforme atribuído pela Braze) ou `null`. Isso é usado para filtrar os resultados por um(a) `link_id` específico(a). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Resolução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Missing/Invalid Campaign ID` | O ID da API da campanha deve ser um identificador de API. Para encontrar essa informação, use o [endpoint para Exportar lista da campanha]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) ou faça login no dashboard. |
| `Missing/Invalid Message Variant ID` | O ID da variante da mensagem API deve ser um identificador de API. Para encontrar essa informação, use o [endpoint para Exportar lista da campanha]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou faça login no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
