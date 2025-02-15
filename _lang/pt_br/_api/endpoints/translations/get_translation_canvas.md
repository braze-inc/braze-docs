---
nav_title: "OBTER: Ver Tradução para uma Canva"
article_title: "OBTER: Ver Tradução para uma Canva"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Ver tradução para um canva\""
---

{% api %}
# Ver tradução para uma canva
{% apimethod get %}
/canvas/translations/?locale_id={locale_id}
{% endapimethod %}

> Use este endpoint para visualizar uma mensagem traduzida e ver como essa mensagem aparece para um usuário.

{% alert important %}
A visualização de uma mensagem traduzida para uma canva via API está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.get`.

## Limite de taxa

Esse endpoint tem um limite de frequência de 250.000 solicitações por hora.

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`step_id`| Obrigatória | String | O ID de sua etapa do canva. |
|`message_variation_id`| Obrigatória | String | A ID de sua variação de mensagem. |
|`locale_id`| Obrigatória | String | O ID da localização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?locale_id={locale_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404`, e `429`.

## Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
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
			"message": "Invalid locale ID"
		}
	]
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Mensagem de erro                           | Solução de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirme se o ID da campanha corresponde à campanha que você está traduzindo.                   |
| `INVALID_LOCALE_ID`                     | Confirme se o ID da localização existe na tradução da mensagem.                         |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirme se o ID da mensagem está correto.                                                |
| `MESSAGE_NOT_FOUND`                     | Verifique se a mensagem a ser traduzida está correta.                                           |
| `LOCALE_NOT_FOUND`                      | Confirme se a localização existe em suas configurações de vários idiomas.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | As configurações de vários idiomas não estão ativadas em seu espaço de trabalho.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Somente as campanhas de e-mail ou as mensagens de canva com e-mails podem ser traduzidas.             |
| `UNSUPPORTED_CHANNEL`                   | Somente mensagens em campanhas de mensagens ou mensagens de canvas com e-mails podem ser traduzidas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
