---
nav_title: "POST: Sincronização do acionador"
article_title: "POST: Disparar Sync"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Disparar sincronização\""

---
{% api %}
# Disparar uma sincronização
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Use este endpoint para disparar uma sincronização para uma determinada integração.

{% alert note %}
Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `cdi.integration_sync`.
{% endalert %}

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Parâmetros da jornada

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `integration_id` | Obrigatória | String | ID de integração. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta

### Exemplo de resposta bem-sucedida

O código de status `202` pode retornar o seguinte corpo de resposta:

```json
{
  "message": "success"
}
```

## Solução de problemas

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `400 Invalid integration ID` | Verifique se o site `integration_id` é válido. |
| `404 Integration not found` | Não existe integração para o ID de integração fornecido. Certifique-se de que seu ID de integração é válido. |
| `429 Another job is in progress` | Há uma sincronização em execução para esta integração. Tente novamente após a sincronização ser concluída. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter códigos de status adicionais e mensagens de erro associadas, consulte [Erros fatais & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
