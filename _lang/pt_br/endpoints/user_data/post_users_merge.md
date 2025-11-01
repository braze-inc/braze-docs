---
nav_title: "POST: Mesclar usuários"
article_title: "POST: Mesclar usuários"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o o endpoint da Braze \"Mesclar usuários\"."

---
{% api %}
# Mesclar usuários
{% apimethod post %}
/users/merge
{% endapimethod %}

> Use esse ponto de extremidade para mesclar um usuário em outro usuário. 

Até 50 mesclagens podem ser especificadas por solicitação. Esse ponto de extremidade é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.merge`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `merge_updates` | Obrigatória | Vetor | Um vetor de objetos. Cada objeto deve conter um objeto `identifier_to_merge` e um objeto `identifier_to_keep`, cada um dos quais deve fazer referência a um usuário por `external_id`, `user_alias`, `phone` ou `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Comportamento de mesclagem

O comportamento documentado abaixo é verdadeiro para todos os recursos da Braze que **não são** alimentados pelo Snowflake. As fusões de usuários não serão refletidas na guia **Histórico de mensagens**, Extensões de segmento, Criador de consultas e Currents.

{% alert important %}
O endpoint não garante que a sequência de objetos `merge_updates` seja atualizada.
{% endalert %}

Esse ponto de extremidade mesclará os seguintes campos se eles não forem encontrados no usuário de direcionamento.

- Nome
- Sobrenome
- Endereços de e-mail (a menos que estejam [encrypted]({{site.baseurl}}/user_guide/data/field_level_encryption/))
- Gênero
- Data de nascimento
- Número de telefone
- Fuso horário
- Cidade natal
- País
- Idioma
- Informações sobre o dispositivo
- Contagem de sessões (a soma das sessões de ambos os perfis)
- Data da primeira sessão (o Braze escolherá a data mais cedo entre as duas datas)
- Data da última sessão (o Braze escolherá a data mais recente entre as duas datas)
- Atributos personalizados (os atributos personalizados existentes no perfil de destino são mantidos e incluirão atributos personalizados que não existiam no perfil de destino)
- Dados de eventos personalizados e de eventos de compra
- Propriedades de evento personalizado e evento de compra para segmentação "X vezes em Y dias" (onde X<=50 e Y<=30)
- Resumo dos eventos personalizados segmentáveis
  - Contagem de eventos (a soma de ambos os perfis)
  - O evento ocorreu pela primeira vez (o Braze escolherá a data mais antiga entre as duas datas)
  - Evento ocorrido pela última vez (o Braze escolherá a data mais recente entre as duas datas)
- Total de compras no app em centavos (a soma de ambos os perfis)
- Número total de compras (a soma de ambos os perfis)
- Data da primeira compra (o Braze escolherá a data mais antiga entre as duas datas)
- Data da última compra (o Braze escolherá a data mais recente entre as duas datas)
- Resumos do app
- Campos Last_X_at (o Braze atualizará os campos se os campos do perfil órfão forem mais recentes)
- Dados de interação da campanha (o Braze escolherá os campos de data mais recentes)
- Resumos do fluxo de trabalho (o Braze escolherá os campos de data mais recentes)
- Histórico de mensagens e de engajamento com mensagens
- Os dados de sessão só serão mesclados se o app existir em ambos os perfis de usuário.

{% alert note %}
Ao mesclar usuários, o uso do endpoint `/users/merge` funciona da mesma forma que o [método`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Comportamento da data do evento personalizado e da data do evento de compra

Esses campos mesclados atualizarão os filtros "para X eventos em Y dias". Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".

### Envio de usuários por e-mail ou número de telefone

Se um `email` ou `phone` for especificado como um identificador, um valor adicional `prioritization` será necessário no identificador. O `prioritization` deve ser um array ordenado especificando qual usuário mesclar se vários usuários forem encontrados. Isso significa que, se mais de um usuário corresponder a uma priorização, a mesclagem não ocorrerá.

Os valores permitidos para o array são:

- `identified`
- `unidentified`
- `most_recently_updated` (refere-se a priorizar o usuário atualizado mais recentemente)
- `least_recently_updated` (refere-se a priorizar o usuário atualizado menos recentemente)

Somente uma das opções a seguir pode existir na matriz de priorização por vez:

- `identified` refere-se à priorização de um usuário com uma `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

## Exemplos de solicitações

### Solicitação básica

Esse é um corpo de solicitação básico para mostrar o padrão da solicitação.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Mesclando usuário não identificado

A solicitação a seguir mesclaria o usuário não identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com` no usuário com um ID externo `john`. Neste exemplo, usar `most_recently_updated` filtrará a consulta para apenas um usuário não identificado. Portanto, se houvesse dois usuários não identificados com esse endereço de e-mail, apenas um seria mesclado no usuário que tem um ID externo `john`.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Mesclando usuário não identificado com usuário identificado

O próximo exemplo mescla o usuário não identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com` com o usuário identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com`. 

Usar `most_recently_updated` filtrará as consultas para apenas um usuário (um usuário não identificado para `identifier_to_merge` e um usuário identificado para `identifier_to_keep`).

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Mesclando um usuário não identificado sem incluir a priorização most_recently_updated

Se houver dois usuários não identificados com o endereço de e-mail `john.smith@braze.com`, esse exemplo de solicitação não mescla nenhum usuário, pois há dois usuários não identificados com esse endereço de e-mail. Essa solicitação só funcionará se houver apenas um usuário não identificado com o endereço de e-mail `john.smith@braze.com`.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Resposta

Existem dois códigos de status para este endpoint: `202` e `400`.

### Exemplo de resposta bem-sucedida

O código de status `202` poderia retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Solução de problemas

A tabela a seguir lista as possíveis mensagens de erro que podem ocorrer.

| Erro | Solução de problemas |
| --- |
| `'merge_updates' must be an array of objects` | Verifique se `merge_updates` é um vetor de objetos. |
| `a single request may not contain more than 50 merge updates` | Você só pode especificar até 50 atualizações de mesclagem em uma única solicitação. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Verifique os identificadores em sua solicitação. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Verifique se o site `merge_updates` contém apenas os dois objetos `identifier_to_merge` e `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
