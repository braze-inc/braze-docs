---
nav_title: "PUT: Atualizar traduções para um modelo de e-mail"
article_title: "PUT: Atualizar Traduções para um Modelo de E-mail"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de Atualizar traduções para um modelo de e-mail."
---

{% api %}
# Atualizar traduções para um modelo de e-mail
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Use este endpoint para atualizar traduções para um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates).

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `templates.translations.update`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros da jornada

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `template_id` | Obrigatória | String | O ID do seu modelo de e-mail. |
| `locale_id` | Obrigatória | String | O ID da localização. |
| `translations` | Obrigatória | String | O mapa das traduções para o seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação GET.

## Exemplo de solicitação

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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


## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Mensagem de erro  | Solução de problemas |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Ocorre quando o tradutor de terceiros fornece traduções com exceções que geram erros de Liquid. Entre em contato com o Suporte da Braze para mais assistência. |
| `The provided translations are missing 'id_1', 'id_2'` | IDs de tradução não correspondem ou o texto traduzido excede os limites. Por exemplo, isso pode significar que a forma do payload está faltando campos no objeto de tradução. Cada mensagem (quando habilitada para múltiplas línguas) deve ter um número específico de "blocos de tradução" com um ID associado a ele. Se o payload fornecido estiver faltando algum dos IDs, isso seria considerado um objeto incompleto e resultaria em um erro. |
| `The provided locale code does not exist.` | O payload do tradutor de terceiros contém um código de localidade que não existe na Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | O payload fornecido excede o limite de tamanho. |
| `You have exceeded the maximum number of requests. Please try again later.` | Todas as APIs da Braze têm limitação de taxa embutida, e esse erro será retornado automaticamente quando a taxa exceder a quantidade permitida para este token de autenticação. |
| `This message does not support multi-language.` | Isso pode ocorrer quando um ID de mensagem não suporta mensagens em múltiplas línguas ainda. Apenas mensagens nos seguintes canais podem ser traduzidas: push, mensagens no aplicativo e e-mail. |
| `Something went wrong. Translation IDs are mismatched or translated text exceeds limits.`| Este é um erro genérico. Entre em contato com [o Suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support) para mais assistência. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
