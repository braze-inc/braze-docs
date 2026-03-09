---
nav_title: "OBTER: Veja os valores de origem padrão para as tags de tradução da campanha"
article_title: "OBTER: Veja os valores de origem padrão para as tags de tradução da campanha"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de origem da tradução da campanha."
---

{% api %}
# Veja os valores de origem padrão para as tags de tradução de uma campanha
{% apimethod get %}
/campanhas/traducoes/origem
{% endapimethod %}

> Use este endpoint para ver todas as fontes de tradução padrão para as tags de tradução de uma campanha. Estes são os valores dentro do {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Veja [Locais em mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para saber mais sobre os recursos de tradução.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obrigatória | String | O ID de sua campanha. |
|`message_variation_id`| Obrigatória | String | O ID da sua variação de mensagem. |
|`locale_id`| Opcional | String | Um UUID de local para filtrar as respostas. |
|`post_launch_draft_version`| Opcional | Booleano | Quando `true` retorna a versão mais recente do rascunho em vez da versão publicada mais recente. Padrão para `false` retornando a versão publicada mais recente.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404`, e `429`.

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
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

{% endapi %}
