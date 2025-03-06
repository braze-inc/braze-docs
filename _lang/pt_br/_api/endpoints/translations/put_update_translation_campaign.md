---
nav_title: "PUT: Atualizar Tradução em uma Campanha"
article_title: "PUT: Atualizar Tradução em uma Campanha"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Atualizar tradução em uma campanha\""
---

{% api %}
# Atualizar tradução em uma campanha
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Use este endpoint para atualizar várias traduções para uma campanha.

{% alert important %}
O recurso de atualizar uma tradução em uma campanha via API está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.translations.update`.

## Limite de taxa

Esse endpoint tem um limite de frequência de 250.000 solicitações por hora.

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatória | String | O ID de sua campanha. |
| `message_variation_id` | Obrigatória | String | O ID de sua mensagem. |
|`locale_id`| Obrigatória | String | O ID da localização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação GET.

## Exemplo de solicitação

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## Exemplo de resposta bem-sucedida

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
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
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
| `INVALID_TRANSLATION_OBJECT`            | IDs de tradução não correspondem ou o texto traduzido excede os limites.                  |
| `MESSAGE_NOT_FOUND`                     | Verifique se a mensagem a ser traduzida está correta.                                           |
| `LOCALE_NOT_FOUND`                      | Confirme se a localização existe em suas configurações de vários idiomas.                         |
| `MISSING_TRANSLATIONS`                  | Os IDs de tradução devem corresponder à mensagem.                                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | As configurações de vários idiomas não estão ativadas em seu espaço de trabalho.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Somente as campanhas de e-mail ou as mensagens de canva com e-mails podem ser traduzidas.             |
| `UNSUPPORTED_CHANNEL`                   | Somente mensagens em campanhas de mensagens ou mensagens de canvas com e-mails podem ser traduzidas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
