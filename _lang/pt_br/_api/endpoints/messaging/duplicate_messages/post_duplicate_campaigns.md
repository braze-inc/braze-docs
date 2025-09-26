---
nav_title: "POST: Campanhas duplicadas"
article_title: "POST: Campanhas duplicadas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre sobre o endpoint \"Duplicar campanhas\"."

---
{% api %}
# Campanhas duplicadas usando a API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Use esse ponto de extremidade para duplicar campanhas. Esse endpoint da API é semelhante à [duplicação de campanhas no dashboard do Braze][1].

{% alert important %}
A duplicação de uma campanha usando a API está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `campaigns.duplicate`.

## Limite de taxa

Esse endpoint está limitado a 100 chamadas de API por minuto.

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obrigatória | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types/). |
|`name`| Obrigatória | String | O nome da campanha resultante. |
|`description`| Opcional | String | O campo de descrição da campanha resultante. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Resposta

Esse endpoint retornará um código de status `202` e a criação da campanha ocorrerá de forma assíncrona. É possível usar o [download do evento de segurança][2] para ver os registros de quando as campanhas foram duplicadas e por qual chave de API.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}
