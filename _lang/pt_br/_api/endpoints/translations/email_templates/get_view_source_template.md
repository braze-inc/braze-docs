---
nav_title: "OBTER: Ver traduções de origem para o modelo de e-mail"
article_title: "OBTER: Ver traduções de origem para o modelo de e-mail"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o ponto final de ver traduções de origem para um modelo de e-mail."
---

{% api %}
# Veja as traduções de origem para um modelo de e-mail
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Use este ponto final para ver as traduções de origem para um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates).

{% alert important %}
Esse ponto de extremidade está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `templates.email.info`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta

| Parâmetro     | Obrigatória | Tipo de dados | Descrição                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obrigatória | String    | O ID para o seu modelo de e-mail. |
| `locale_id`   | Obrigatória | String    | O ID da localização.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Note que todas as IDs de tradução são consideradas identificadores únicos universais (UUIDs), que podem ser encontrados nas configurações do **Suporte multilíngue** ou na resposta da solicitação.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source' \
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
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
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
            "message": "The provided locale code does not exist."
        }
    ]
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Mensagem de erro                           | Solução de problemas                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_LOCALE_ID`                     | Confirme se o ID da localização existe na tradução da mensagem.                         |
| `LOCALE_NOT_FOUND`                      | Confirme se a localização existe em suas configurações de vários idiomas.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | As configurações de vários idiomas não estão ativadas em seu espaço de trabalho.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Apenas modelos de e-mail e campanhas de e-mail, push e mensagens in-app ou mensagens Canvas com e-mails podem ser traduzidos.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
