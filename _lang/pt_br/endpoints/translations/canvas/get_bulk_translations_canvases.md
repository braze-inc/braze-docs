---
nav_title: "OBTER: Exibir todas as traduções de um canva"
article_title: "OBTER: Exibir todas as traduções de um canva"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Exibir todas as traduções de um canva."
---

{% api %}
# Exibir todas as traduções de um canva
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> Use esse ponto de extremidade para visualizar todas as traduções de um Canva.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Obrigatória | String | A ID do Canva. |
|`step_id`| Obrigatória | String | O ID de sua etapa do canva. |
|`message_variation_id`| Obrigatória | String | A ID de sua variação de mensagem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404`, e `429`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Mensagem de erro                           | Solução de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirme se o ID da campanha corresponde à campanha que você está traduzindo.                   |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirme se o ID da mensagem está correto.                                                |
| `MESSAGE_NOT_FOUND`                     | Verifique se a mensagem a ser traduzida está correta.                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | As configurações de vários idiomas não estão ativadas em seu espaço de trabalho.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Apenas campanhas de e-mail, push e mensagens no aplicativo ou mensagens do Canva com e-mails podem ser traduzidas.             |
| `UNSUPPORTED_CHANNEL`                   | Apenas campanhas de e-mail, push ou mensagens no aplicativo ou mensagens do Canva podem ser traduzidas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
