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

Se quiser atualizar as traduções após o lançamento de uma campanha, será necessário [salvar a mensagem como rascunho]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) primeiro.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `campaigns.translations.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatória | String | O ID de sua campanha. |
| `message_variation_id` | Obrigatória | String | O ID de sua variação de mensagem. |
| `locale_name` | Obrigatória | String | O nome da localização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação GET.

## Exemplo de solicitação

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab", // CAMPAIGNS ONLY
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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


## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Mensagem de erro  | Solução de problemas |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Ocorre quando o tradutor terceirizado fornece traduções com exceções que geram erros Liquid. Entre em contato com o suporte da Braze para obter mais assistência. |
| `The provided translations are missing 'id_1', 'id_2'` | IDs de tradução não correspondem ou o texto traduzido excede os limites. Por exemplo, isso pode significar que a forma da carga útil está faltando campos no objeto de tradução. Cada mensagem (quando ativada para vários idiomas) deve ter um número específico de "blocos de tradução" com um ID associado a ela. Se a carga útil fornecida estiver faltando alguma das IDs, ela será considerada um objeto incompleto e resultará em um erro. |
| `The provided locale code does not exist.` | A carga útil do tradutor de terceiros contém um código de localidade que não existe no Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | A carga útil fornecida excede o limite de tamanho. |
| `You have exceeded the maximum number of requests. Please try again later.` | Todas as APIs do Braze têm limites de frequência integrados, e esse erro será automaticamente retornado quando a frequência exceder o valor alocado para esse token de autenticação. |
| `This message does not support multi-language.` | Isso pode ocorrer quando um ID de mensagem ainda não é compatível com mensagens em vários idiomas. Somente as mensagens nos seguintes canais podem ser traduzidas: push, mensagens no app e envio de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
