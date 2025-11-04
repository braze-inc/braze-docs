---
nav_title: "POST: Renomear IDs externos"
article_title: "POST: Renomear IDs externos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint \"Renomear IDs externos\"."

---
{% api %}
# Renomear ID externo
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Use esse ponto de extremidade para renomear as IDs externas dos seus usuários. 

Você pode enviar até 50 objetos de renomeação por solicitação. 

Esse ponto de extremidade define um novo `external_id` (primário) para o usuário e substitui o `external_id` existente. Isso significa que o usuário pode ser identificado por `external_id` até que o obsoleto seja removido. Ter vários IDs externos permite um período de migração para que as versões mais antigas de seus apps que usam o esquema de nomenclatura de ID externo anterior não sejam interrompidas. 

Depois que o esquema de nomenclatura antigo não estiver mais em uso, é altamente recomendável remover IDs externas obsoletas usando o [ponto de extremidade`/users/external_ids/remove` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Remova os IDs externos obsoletos com o endpoint `/users/external_ids/remove` em vez de `/users/delete`. O envio de uma solicitação para `/users/delete` com a ID externa obsoleta exclui totalmente o perfil do usuário e não pode ser desfeito.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.external_ids.rename`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obrigatória | Vetor de objetos de renomeação de identificador externo | Veja o exemplo de solicitação e as seguintes limitações para a estrutura do objeto de renomeação do identificador externo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Observe o seguinte:

- O `current_external_id` deve ser o ID principal do usuário e não pode ser um ID obsoleto.
- O endereço `new_external_id` não deve estar em uso como ID primária ou ID obsoleta.
- Os sites `current_external_id` e `new_external_id` não podem ser os mesmos.

## Exemplo de solicitação
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Resposta

A resposta confirmará todas as renomeações bem-sucedidas, bem como as renomeações malsucedidas com quaisquer erros associados. As mensagens de erro no campo `rename_errors` farão referência ao índice do objeto no vetor da solicitação original.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

O campo `message` retornará `success` para qualquer solicitação válida. Erros mais específicos são capturados no array `rename_errors`. O campo `message` retorna um erro no caso de:

- Chave de API inválida
- Matriz `external_id_renames` vazia
- `external_id_renames` vetor de objetos com mais de 50 objetos
- Limite de frequência atingido (mais de 1.000 solicitações por minuto)

## Perguntas frequentes

### Isso afeta o MAU?
Não, como o número de usuários permanecerá o mesmo, eles terão apenas um novo `external_id`.

### O comportamento do usuário muda historicamente?
Não, pois o usuário ainda é o mesmo, e todo o seu comportamento histórico ainda está conectado a ele.

### Ele pode ser executado em espaços de trabalho de desenvolvimento ou de preparação?
Sim. Na verdade, é altamente recomendável executar uma migração de teste em um espaço de trabalho de preparação ou desenvolvimento e garantir que tudo corra bem antes de executar nos dados de produção.

### Isso consome pontos de dados?
Esse recurso não custa pontos de dados.

### Qual é o período de depreciação recomendado?
Não temos um limite rígido de quanto tempo você pode manter IDs externas obsoletas, mas é altamente recomendável removê-las quando não houver mais necessidade de fazer referência aos usuários pela ID obsoleta.

{% endapi %}
