---
nav_title: "OBTER: Exibir a tradução de uma campanha"
article_title: "OBTER: Exibir tradução para uma campanha"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exibir tradução para uma campanha\"."
---

{% api %}
# Exibir a tradução de uma campanha
{% apimethod get %}
/campaigns/translations/?locale_id={locale_id}
{% endapimethod %}

> Use esse ponto de extremidade para visualizar uma mensagem traduzida para uma campanha.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro              | Obrigatória | Tipo de dados | Descrição                        |
|------------------------|----------|-----------|------------------------------------|
| `campaign_id`          | Obrigatória | String    | O ID de sua campanha.           |
| `message_variation_id` | Obrigatória | String    | A ID de sua variação de mensagem. |
| `locale_id`            | Obrigatória | String    | O ID da localização.              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/?locale_id={locale_uuid}' \
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
			"message": "The provided locale code does not exist."
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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Somente campanhas de e-mail, push e mensagens no aplicativo ou mensagens do Canvas com e-mails podem ser traduzidas.             |
| `UNSUPPORTED_CHANNEL`                   | Somente campanhas de e-mail, push, mensagens no aplicativo ou mensagens do Canvas podem ser traduzidas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
