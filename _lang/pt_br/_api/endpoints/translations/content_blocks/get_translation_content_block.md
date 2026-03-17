---
nav_title: "OBTER: Veja todas as traduções para um bloco de conteúdo"
article_title: "OBTER: Veja todas as traduções para um bloco de conteúdo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Veja todas as traduções para um bloco de conteúdo."
---

{% api %}
# Veja todas as traduções para um bloco de conteúdo
{% apimethod get %}
/content_blocks/translations
{% endapimethod %}

> Use este endpoint para ver todas as traduções para um [bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/). Veja [Localizações em mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para saber mais sobre os recursos de tradução.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `content_blocks.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`content_block_id`| Obrigatória | String | O ID do seu bloco de conteúdo. |
|`locale_id`| Opcional | String | Um UUID de local para filtrar as respostas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404`, e `429`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### Exemplo de resposta de erro

O código de status `400` pode retornar o seguinte corpo de resposta.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```


{% endapi %}
