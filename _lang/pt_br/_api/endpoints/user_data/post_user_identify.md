---
nav_title: "POST: Identificar usuários"
article_title: "POST: Identificar usuários"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Este artigo traz informações sobre o endpoint da Braze \"Identificar usuários\"."

---
{% api %}
# Identificar usuários
{% apimethod post %}
/users/identify
{% endapimethod %}

> Use este endpoint para identificar um usuário não identificado (apenas por alias, apenas por e-mail ou apenas por número de telefone) usando o ID externo fornecido.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Como funciona

Chamar `/users/identify` combina um perfil de usuário identificado por um alias (perfil apenas por alias), endereço de e-mail (perfil apenas por e-mail) ou número de telefone (perfil apenas por número de telefone) com um perfil de usuário que tem um `external_id` (perfil identificado), e então remove o perfil apenas por alias.

Identificar um usuário requer que um `external_id` seja incluído nos seguintes objetos:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

Se não houver um usuário com esse `external_id`, o `external_id` é adicionado ao registro do usuário com alias, e o usuário é considerado identificado. Os usuários podem ter apenas um alias para um rótulo específico. Se um usuário já existir com o `external_id` e tiver um alias existente com o mesmo rótulo que o perfil apenas por alias, então os perfis de usuário não são combinados.

{% alert tip %}
Para evitar a perda inesperada de dados ao identificar usuários, é altamente recomendável consultar primeiro [as práticas recomendadas de coleta de dados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) para saber como capturar dados de usuários quando as informações de usuários com alias já estiverem presentes.
{% endalert %}

### Comportamento de mesclagem

Por padrão, este endpoint mescla a seguinte lista de campos encontrados **exclusivamente** no usuário anônimo para o usuário identificado.

{% details Lista de campos que são mesclados %}
- Nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- Número de telefone
- Fuso horário
- Cidade natal
- País
- Idioma
- Contagem de sessões (a soma das sessões de ambos os perfis)
- Data da primeira sessão (a Braze escolhe a data mais antiga entre as duas)
- Data da última sessão (a Braze escolhe a data mais recente entre as duas)
- Atributos personalizados
- Dados de eventos personalizados e de eventos de compra
- Propriedades de evento personalizado e evento de compra para segmentação "X vezes em Y dias" (onde X<=50 e Y<=30)
- Resumo dos eventos personalizados segmentáveis
  - Contagem de eventos (a soma de ambos os perfis)
  - O evento ocorreu pela primeira vez (a Braze escolhe a data mais antiga entre as duas)
  - O evento ocorreu pela última vez (a Braze escolhe a data mais recente entre as duas)
- Total de compras no app em centavos (a soma de ambos os perfis)
- Número total de compras (a soma de ambos os perfis)
- Data da primeira compra (a Braze escolhe a data mais antiga entre as duas)
- Data da última compra (a Braze escolhe a data mais recente entre as duas)
- Resumos do app
- Campos Last_X_at (a Braze atualiza os campos se os campos do perfil órfão forem mais recentes)
- Resumos de campanhas (a Braze escolhe os campos de data mais recentes)
- Resumos de fluxo de trabalho (a Braze escolhe os campos de data mais recentes)
- Histórico de mensagens e de engajamento com mensagens
- Contagem de eventos personalizados e eventos de compra e registros de data e hora da primeira e da última data
  - Esses campos mesclados atualizam filtros "para X eventos em Y dias". Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".
- Dados de sessão se o app existir em ambos os perfis de usuário
  - Por exemplo, se o usuário alvo não tiver um resumo de app para "ABCApp", mas o usuário original tiver, o usuário alvo terá o resumo do app "ABCApp" em seu perfil após a mesclagem.
{% enddetails %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.identify`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Parâmetros de solicitação

É possível adicionar até 50 aliases de usuário por solicitação. É possível associar vários aliases de usuário adicionais a um único `external_id`.

{% alert important %}
Um dos seguintes é obrigatório por solicitação: `aliases_to_identify`, `emails_to_identify` ou `phone_numbers_to_identify`. Por exemplo, você pode usar este endpoint para identificar usuários por e-mail usando `emails_to_identify` na sua solicitação.
{% endalert %}

| Parâmetro                   | Obrigatória | Tipo de dados                           | Descrição                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Obrigatória | Vetor de aliases para identificar o objeto | Consulte [alias para identificar o objeto]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) e [o objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Obrigatória | Vetor de aliases para identificar o objeto | Obrigatório se `email` for especificado como o identificador. Endereços de e-mail para identificar usuários. Consulte [Identificação de usuários por e-mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Obrigatória | Vetor de aliases para identificar o objeto | Números de telefone para identificar usuários.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identificando usuários por endereços de e-mail e números de telefone

Se um endereço de e-mail ou número de telefone for especificado como identificador, você também deve incluir `prioritization` no identificador.

O `prioritization` deve ser um array especificando qual usuário mesclar se houver vários usuários encontrados. `prioritization` é um array ordenado, o que significa que, se mais de um usuário corresponder a uma priorização, a mesclagem não ocorrerá.

Os valores permitidos para o array são:

- `identified`
- `unidentified`
- `most_recently_updated` (refere-se a priorizar o usuário atualizado mais recentemente)
- `least_recently_updated` (refere-se a priorizar o usuário atualizado menos recentemente)

Somente uma das opções a seguir pode existir no array de priorização por vez:

- `identified` refere-se à priorização de um usuário com um `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

{% alert note %}
A mesclagem não ocorre se o endereço de e-mail ou número de telefone corresponder a vários usuários. Isso inclui casos em que um desses usuários tem o mesmo `external_id` especificado na solicitação. Nesses casos, o endpoint retorna `"message": "success"`, mas os perfis de usuário não são combinados. Para evitar isso, verifique se o endereço de e-mail ou número de telefone está associado apenas a usuários não identificados antes de chamar este endpoint.
{% endalert %}

## Exemplo de solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

### Diferenciação de maiúsculas e minúsculas

O campo `alias_name` diferencia maiúsculas de minúsculas. Uma solicitação que retorna um código de status `201` confirma apenas que a sintaxe da solicitação era válida — não confirma que o alias foi correspondido. Se a capitalização de `alias_name` na sua solicitação não corresponder exatamente ao alias armazenado no perfil de usuário, a operação falhará silenciosamente e o `external_id` não será atribuído. Por exemplo, se o alias armazenado for `JimJones@example.com`, uma solicitação com `jimjones@example.com` retornará sucesso, mas não produzirá nenhum resultado.

{% alert tip %}
Para saber mais sobre `alias_name` e `alias_label`, consulte nossa documentação sobre [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

## Resposta

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}