---
nav_title: "PUT: Atualizar traduções para um e-mail modelo"
article_title: "PUT: Atualizar traduções para um E-mail Modelo"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de Atualizar traduções para um e-mail modelo."
---

{% api %}
# Atualizar traduções para um e-mail modelo
{% apimethod put %}
/templates/e-mail/traducoes/
{% endapimethod %}

> Use este endpoint para atualizar traduções para um [e-mail modelo]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates). Veja [Localizações em mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para saber mais sobre os recursos de tradução.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `templates.translations.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `template_id` | Obrigatória | String | O ID do seu e-mail modelo. |
| `locale_id` | Obrigatória | String | O ID da localização. |
| `translations_map` | Obrigatória | String | O mapa das traduções para o seu e-mail modelo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
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
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}
