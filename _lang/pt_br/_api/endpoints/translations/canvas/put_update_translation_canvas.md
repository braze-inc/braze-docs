---
nav_title: "PUT: Atualizar a tradução em uma tela"
article_title: "PUT: Atualizar a conversão em uma tela"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Alterar tradução em um canva\"."
---

{% api %}
# Atualizar a tradução em uma tela
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Use esse endpoint para alterar várias traduções para um canva. Veja [Locais em mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para saber mais sobre os recursos de tradução.

Se você quiser atualizar as traduções depois que um canva for lançado, precisará [salvar sua mensagem como um rascunho]({{site.baseurl}}/post-launch_edits/) primeiro.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Obrigatória | String | O ID do canva. |
|`step_id`| Obrigatória | String | O ID de sua etapa do canva. |
|`message_variation_id`| Obrigatória | String | O ID da sua variação de mensagem. |
|`locale_id`| Obrigatória | String | O ID (UUID) do local. |
|`translation_map` | Obrigatória | Objeto | Objeto contendo as novas traduções. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Resposta

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404`, e `429`.

### Exemplo de resposta bem-sucedida

```json
{
	"message": "success"
}
```

### Exemplo de resposta de erro

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
	"errors": [
		{
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}
