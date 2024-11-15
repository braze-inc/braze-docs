---
nav_title: "OBTER: Listar aplicativos do espaço de trabalho"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Este artigo descreve detalhes sobre o endpoint da Braze que lista apps dentro de espaços de trabalho."
---
{% api %}
# Listar aplicativos do espaço de trabalho
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Use esse endpoint para listar o nome e o identificador único (`api_key`) dos apps em um espaço de trabalho. 

O acesso a esse endpoint retorna um vetor de objeto chamado `apps`. Cada objeto em `apps` contém o nome e o identificador único do app. 

{% apiref postman %}  {% endapiref %}

## Limite de taxa

Esse endpoint tem um limite de frequência de 100 solicitações por dia (24 horas).

## Parâmetros de solicitação

Essa solicitação não aceita parâmetros.

## Exemplo de solicitação

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `401: Unauthorized` | A chave de API não tem as permissões necessárias. Certifique-se de que sua chave de API tenha permissões `apps.get`. |
| `403: Forbidden` | O flipper de recursos não está ativo para essa empresa. Entre em contato com o gerente de sucesso do cliente para obter assistência. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
