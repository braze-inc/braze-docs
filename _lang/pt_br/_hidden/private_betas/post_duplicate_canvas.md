---
nav_title: "POST: Canvas duplicadas"
layout: api_page
page_type: reference
hidden: true
permalink: /api/endpoints/messaging/duplicate_canvases/
description: "Este artigo descreve detalhes sobre o endpoint de duplicação de canvas."
---

{% api %}
# Duplicação de telas via API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canva/duplicate
{% endapimethod %}

> Use esse ponto de extremidade para duplicar Canvas. Esse endpoint da API é semelhante à [duplicação de Canvas no dashboard do Braze][1].

{% alert important %}
A duplicação de um canva via API está em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.duplicate`.

## Limite de taxa

Esse endpoint está limitado a 100 chamadas de API por minuto.

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obrigatória | String | Consulte [Identificador do Canva]({{site.baseurl}}/api/identifier_types/). |
|`name`| Obrigatória | String | O nome da tela resultante. |
|`description`| Opcional | String | O campo de descrição do Canva resultante. |
|`tag_names` | Opcional | String | As tags para a tela resultante. Essas devem ser tags existentes. Se você adicionar novas tags na solicitação, elas substituirão todas as tags que estavam no Canva original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Resposta

Esse ponto de extremidade retornará um código de status `202` e a criação do Canva ocorrerá de forma assíncrona. É possível usar o [download do evento de segurança][2] para ver os registros de quando os canvas foram duplicados e por qual chave de API.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
