---
nav_title: "OBTER: Integrações de listas"
article_title: "OBTER: Integrações de listas"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Integrações de listas\"."

---
{% api %}
# Integrações de listas
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> Use esse ponto de extremidade para retornar uma lista de integrações existentes.


{% alert note %}
Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `cdi.integration_list`.
{% endalert %}

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Parâmetros de consulta

Cada chamada a esse ponto de extremidade retornará 10 itens. Para uma lista com mais de 10 integrações, use o cabeçalho `Link` para recuperar os dados na próxima página, conforme mostrado no exemplo de resposta.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `cursor` | Opcional | String | Determina a paginação da lista de integração. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

### Sem cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Com cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte corpo de resposta.

{% alert note %}
O cabeçalho `Link` não existirá se houver 10 integrações ou menos no total. Nas chamadas sem cursor, o endereço `prev` não será exibido. Ao olhar a última página de itens, `next` não será exibido.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `400 Invalid cursor` | Verifique se o site `cursor` é válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter códigos de status adicionais e mensagens de erro associadas, consulte [Erros fatais & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
