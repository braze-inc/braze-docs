---
nav_title: "OBTER: Exibir valores de origem padrão para as tags de tradução do Canva"
article_title: "OBTER: Exibir valores de origem padrão para as tags de tradução do Canva"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o ponto de extremidade de origem da tradução do Canva."
---

{% api %}
# Exibir valores de origem padrão para as tags de tradução de uma tela
{% apimethod get %}
/canva/translations/source
{% endapimethod %}

> Use esse ponto de extremidade para visualizar todas as fontes de tradução padrão para as tags de tradução de uma tela. Esses são os valores com o endereço {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulte [Localidades nas mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) para obter mais informações sobre os recursos de tradução.

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.get`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro              | Obrigatória | Tipo de dados | Descrição                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Obrigatória | String    | A ID da tela.              |
| `step_id`              | Obrigatória | String    | O ID de sua etapa do canva.        |
|`message_variation_id`| Obrigatória | String | O ID de sua variação de mensagem. |
| `locale_id`            | Opcional | String    | A ID (UUID) da localização.              |
| `post_launch_draft_version`| Opcional | Booleano | Quando `true` retorna a última versão de rascunho em vez da última versão publicada ao vivo. O padrão é `false`, que retorna a versão mais recente em tempo real.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do ponto de extremidade GET.
{% endalert %}

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
