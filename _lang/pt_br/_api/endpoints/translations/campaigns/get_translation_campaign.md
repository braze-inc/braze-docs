---
nav_title: "OBTER: Ver todas as traduções de uma campanha"
article_title: "OBTER: Ver todas as traduções de uma campanha"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre a opção Exibir todas as traduções para um ponto de extremidade de campanha."
---

{% api %}
# Ver todas as traduções de uma campanha
{% apimethod get %}
/campaigns/translations
{% endapimethod %}

> Use esse ponto de extremidade para visualizar todas as traduções de cada variante de mensagens em uma campanha. Consulte [Localidades nas mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obter mais informações sobre os recursos de tradução.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obrigatória | String | O ID de sua campanha. |
|`message_variation_id`| Obrigatória | String | O ID de sua variação de mensagem. |
|`locale_id`| Opcional | String | Um UUID de localização para filtrar as respostas. |
| `post_launch_draft_version`| Opcional | Booleano | Quando `true` retorna a última versão de rascunho em vez da última versão publicada ao vivo. O padrão é `false`, que retorna a versão mais recente em tempo real.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do ponto de extremidade GET.
{% endalert %}

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
