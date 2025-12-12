---
nav_title: "OBTER: Listar o status de sincronização do trabalho"
article_title: "OBTER: Listar status de sincronização do trabalho"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Listar status de sincronização do trabalho\"."

---
{% api %}
# Listar o status de sincronização do trabalho
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> Use esse ponto de extremidade para retornar uma lista de status de sincronização anteriores para uma determinada integração.

{% alert note %}
Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `cdi.integration_job_status`.
{% endalert %}

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `integration_id` | Obrigatória | String | ID de integração. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de consulta

Cada chamada a esse ponto de extremidade retornará 10 itens. Para uma integração com mais de 10 sincronizações, use o cabeçalho `Link` para recuperar os dados na próxima página, conforme mostrado no exemplo de resposta a seguir.

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `cursor` | Opcional | String | Determina a paginação do status de sincronização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

### Sem cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Com cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

### Exemplo de resposta bem-sucedida

O código de status `200` poderia retornar o seguinte corpo de resposta.

{% alert note %}
O cabeçalho `Link` não existirá se houver menos ou igual a 10 sincronizações no total. Nas chamadas sem cursor, o endereço `prev` não será exibido. Ao olhar a última página de itens, `next` não será exibido.
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors,
    },
  ],
  "message": "success"
}
```

| job_status | Explicação |
| --- | --- |
| `running` | O trabalho está em execução no momento. |
| `success` | Todas as linhas foram sincronizadas com sucesso. |
| `partial` | Algumas linhas não puderam ser sincronizadas devido a erros. |
| `error` | Nenhuma linha foi sincronizada. |
| `config_error` | Houve um erro na configuração da integração. Verifique sua configuração de integração. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `400 Invalid cursor` | Verifique se o site `cursor` é válido. |
| `400 Invalid integration ID` | Verifique se o site `integration_id` é válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter códigos de status adicionais e mensagens de erro associadas, consulte [Erros fatais & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
