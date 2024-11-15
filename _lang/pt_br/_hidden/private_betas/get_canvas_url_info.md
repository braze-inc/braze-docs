---
nav_title: "OBTER: Listar Links de Apelidos para canva"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Este artigo descreve detalhes sobre o alias de link da Lista para o endpoint da canva."
---
{% api %}
# Lista de alias de link para canva
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> Use este endpoint para listar o conjunto de alias de link em uma etapa do canva de e-mail específica.

{% apiref postman %}  {% endapiref %}

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `canvas_step_id` | Obrigatória | String | Consulte [Identificador de API de etapa do canva]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier). |
| `message_variation_id ` | Obrigatória | String | Identificador de API da variante de mensagem (para a variante de mensagem de e-mail naquela etapa). Você pode encontrar isso clicando em **Analisar Variantes** na página de **Detalhes da Canva**. |
| `includes_link_id` | Opcional | String | Um identificador de link específico (conforme atribuído pela Braze) ou `null`. Isso é usado para filtrar os resultados por um(a) `link_id` específico(a). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

### Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Missing/Invalid Canvas ID` | O ID da API do Canva deve ser um identificador de API. Para encontrar essa informação, use o [endpoint para Exportar lista do canva]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) ou faça login no dashboard. |
| `Missing/Invalid Message Variant ID` | O ID da variante da mensagem API deve ser um identificador de API. Você pode encontrar isso usando o endpoint [Exportar detalhes da canva]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) ou fazendo login no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
