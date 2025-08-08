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

> Use esse ponto de extremidade para identificar um usuário não identificado (somente alias, somente e-mail ou somente número de telefone) usando a ID externa fornecida.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Como funciona?

A chamada para `/users/identify` combina um perfil de usuário que é identificado por um alias (perfil somente de alias), endereço de e-mail (perfil somente de e-mail) ou número de telefone (perfil somente de número de telefone) com um perfil de usuário que tem um `external_id` (perfil identificado) e, em seguida, remove o perfil somente de alias. 

A identificação de um usuário requer que um `external_id` seja incluído nos seguintes objetos:

- `aliases_to_identify`
- `emails_to_identify` 
- `phone_numbers_to_identify`

Se não houver um usuário com esse `external_id`, o `external_id` será adicionado ao registro do usuário aliasing, e o usuário será considerado identificado. Os usuários só podem ter um alias para um rótulo específico. Se um usuário já existir com o `external_id` e tiver um alias existente com o mesmo rótulo do perfil somente de alias, os perfis de usuário não serão combinados.

{% alert tip %}
Para evitar a perda inesperada de dados ao identificar usuários, é altamente recomendável consultar primeiro [as práticas recomendadas de coleta de dados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) para saber como capturar dados de usuários quando as informações de usuários com alias já estiverem presentes.
{% endalert %}

### Comportamento de mesclagem

Por padrão, esse ponto de extremidade mesclará a seguinte lista de campos encontrados **exclusivamente** no usuário anônimo para o usuário identificado.

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
- Data da primeira sessão (o Braze escolherá a data mais cedo entre as duas datas)
- Data da última sessão (o Braze escolherá a data mais recente entre as duas datas)
- Atributos personalizados
- Dados de eventos personalizados e de eventos de compra
- Propriedades de eventos personalizados e de eventos de compra para a segmentação "X vezes em Y dias" (onde X<=50 e Y<=30)
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
- Resumos de campanha (o Braze escolherá os campos de data mais recentes)
- Resumos do fluxo de trabalho (o Braze escolherá os campos de data mais recentes)
- Histórico de mensagens e de engajamento com mensagens
- Contagem de eventos personalizados e eventos de compra e registros de data e hora da primeira e da última data 
  - Esses campos mesclados atualizarão os filtros "para X eventos em Y dias". Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".
- Dados de sessão se o app existir em ambos os perfis de usuário
  - Por exemplo, se o usuário-alvo não tiver um resumo do aplicativo "ABCApp", mas o usuário original tiver, o usuário-alvo terá o resumo do aplicativo "ABCApp" em seu perfil após a mesclagem.
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
É necessário um dos seguintes dados: `aliases_to_identify`, `emails_to_identify`, ou `phone_numbers_to_identify` por solicitação. Por exemplo, você pode usar esse endpoint para identificar usuários por e-mail usando `emails_to_identify` em sua solicitação.
{% endalert %}

| Parâmetro                   | Obrigatória | Tipo de dados                           | Descrição                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Obrigatória | Vetor de aliases para identificar o objeto | Consulte [alias para identificar o objeto]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) e [o objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Obrigatória | Vetor de aliases para identificar o objeto | Obrigatório se `email` for especificado como o identificador. Endereços de e-mail para identificar usuários. Consulte [Identificação de usuários por e-mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Obrigatória | Vetor de aliases para identificar o objeto | Números de telefone para identificar os usuários.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identificação de usuários por endereços de e-mail e números de telefone

Se um endereço de e-mail ou número de telefone for especificado como um identificador, você também deverá incluir `prioritization` no identificador.

O `prioritization` deve ser uma matriz que especifica qual usuário deve ser mesclado se houver vários usuários encontrados. `prioritization` é uma matriz ordenada, ou seja, se mais de um usuário corresponder a uma priorização, a mesclagem não ocorrerá.

Os valores permitidos para a matriz são:

- `identified`
- `unidentified`
- `most_recently_updated` (refere-se à priorização do usuário atualizado mais recentemente)
- `least_recently_updated` (refere-se à priorização do usuário atualizado menos recentemente)

Somente uma das opções a seguir pode existir na matriz de priorização por vez:

- `identified` refere-se à priorização de um usuário com uma `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

Se você especificar `identified` na matriz, isso significaria que o usuário **deve** ter um `external_id` para ser inserido no Canva. Se quiser que os usuários com endereços de e-mail digitem a mensagem, independentemente de estarem identificados ou não, use apenas o parâmetro `most_recently_updated` ou `least_recently_updated`.

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

{% alert tip %}
Para saber mais sobre `alias_name` e `alias_label`, consulte nossa documentação sobre [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

## Resposta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
