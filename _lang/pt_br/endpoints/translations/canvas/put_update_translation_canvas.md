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

> Use esse endpoint para alterar várias traduções para um canva.

Se você quiser atualizar as traduções após um Canvas ter sido lançado, precisará [salvar sua mensagem como um rascunho]({{site.baseurl}}/post-launch_edits/) primeiro.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
|`step_id`| Obrigatória | String | O ID de sua etapa do canva. |
|`message_variation_id`| Obrigatória | String | A ID de sua variação de mensagem. |
|`locale_name`| Obrigatória | String | O nome do local. |
|`workflow_id` | Obrigatória | String | A ID do Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação.
{% endalert %}

## Exemplo de solicitação

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad", // CANVAS ONLY
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac", // CANVAS ONLY
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
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Ocorre quando o tradutor de terceiros fornece traduções com exceções que geram erros de Liquid. Entre em contato com o Suporte da Braze para mais assistência. |
| `The provided translations are missing 'id_1', 'id_2'` | IDs de tradução não correspondem ou o texto traduzido excede os limites. Por exemplo, isso pode significar que a forma do payload está faltando campos no objeto de tradução. Cada mensagem (quando habilitada para múltiplas línguas) deve ter um número específico de "blocos de tradução" com um ID associado a ele. Se o payload fornecido estiver faltando algum dos IDs, isso seria considerado um objeto incompleto e resultaria em um erro. |
| `The provided locale code does not exist.` | O payload do tradutor de terceiros contém um código de local que não existe na Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | O payload fornecido excede o limite de tamanho. |
| `You have exceeded the maximum number of requests. Please try again later.` | Todas as APIs da Braze têm limitação de taxa embutida, e esse erro será retornado automaticamente quando a taxa exceder a quantidade permitida para este token de autenticação. |
| `This message does not support multi-language.` | Isso pode ocorrer quando um ID de mensagem ainda não suporta mensagens multilíngues. Apenas mensagens nos seguintes canais podem ser traduzidas: push, mensagens no aplicativo e e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
