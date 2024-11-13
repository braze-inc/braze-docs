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

> Use esse ponto de extremidade para identificar um usuário não identificado (somente alias). 

{% alert important %}
A partir de 7 de agosto de 2023, esse endpoint mesclará os dados de todas as chamadas. Isso significa que [`merge_behavior`](#merge) será definido como `merge` para todas as chamadas.
{% endalert %}

A chamada para `/users/identify` combina o perfil somente de alias com o perfil identificado e remove o perfil somente de alias.

A identificação de um usuário requer que um `external_id` seja incluído no objeto `aliases_to_identify`. Se não houver nenhum usuário com esse `external_id`, o `external_id` será adicionado ao registro do usuário com alias, e o usuário será considerado identificado. É possível adicionar até 50 aliases de usuário por solicitação.

Posteriormente, é possível associar vários aliases de usuário adicionais a um único `external_id`. 
- Quando essas associações subsequentes são feitas com o campo `merge_behavior` definido como `none`, somente os tokens por push e o histórico de mensagens associados ao alias do usuário são mantidos; quaisquer atributos, eventos ou compras ficarão "órfãos" e não estarão disponíveis para o usuário identificado. Uma solução alternativa é exportar os dados do usuário com aliasing de usuário antes da identificação usando o [ponto de extremidade`/users/export/ids` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) e, em seguida, associar novamente os atributos, eventos e compras ao usuário identificado.
- Quando as associações são feitas com o campo `merge_behavior` definido como `merge`, esse ponto de extremidade mesclará [campos específicos](#merge) encontrados no usuário anônimo com o usuário identificado.

{% alert tip %}
Para evitar a perda inesperada de dados ao identificar usuários, é altamente recomendável consultar primeiro [as práticas recomendadas de coleta de dados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) para saber como capturar dados de usuários quando as informações de usuários com alias já estiverem presentes.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.identify`.

## Limite de taxa 
Um limite de frequência é aplicado a solicitações feitas a esse endpoint para clientes que fizeram a integração com o Braze em 16 de setembro de 2021 ou após essa data. Para saber mais, consulte [Limites da API]({{site.baseurl}}/api/basics/#api-limits).

## Corpo da solicitação

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Parâmetros de solicitação

| Parâmetro             | Obrigatória | Tipo de dados                           | Descrição                                                                                                                                                                 |
| --------------------- | -------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases_to_identify` | Obrigatória | Vetor de aliases para identificar o objeto | Consulte [alias para identificar o objeto]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) e [o objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `merge_behavior`      | Opcional | String                              | Espera-se que seja um dos sites `none` ou `merge`.                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Campo Merge_behavior {#merge}

Definir o campo `merge_behavior` como `merge` define o ponto de extremidade para mesclar qualquer um dos seguintes campos encontrados **exclusivamente** no usuário anônimo para o usuário identificado. 
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

Qualquer um dos seguintes campos encontrados no usuário anônimo para o usuário identificado:
- Contagem de eventos personalizados e eventos de compra e registros de data e hora da primeira e da última data 
  - Esses campos mesclados atualizarão os filtros "para X eventos em Y dias". Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".

Os dados de sessão só serão mesclados se o app existir em ambos os perfis de usuário. Por exemplo, se o usuário-alvo não tiver um resumo do aplicativo "ABCApp", mas o usuário original tiver, o usuário-alvo terá o resumo do aplicativo "ABCApp" em seu perfil após a mesclagem. 

Definir o campo como `none` não mesclará nenhum dado de usuário ao perfil de usuário identificado.

### Identificação de usuários por e-mail
Se um `email` for especificado como um identificador, um valor `prioritization` adicional será necessário no identificador. O `prioritization` deve ser uma matriz que especifica qual usuário deve ser mesclado se houver vários usuários encontrados. `prioritization` é uma matriz ordenada, ou seja, se mais de um usuário corresponder a uma priorização, a mesclagem não ocorrerá.

Os valores permitidos para o vetor são: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` refere-se à priorização do usuário atualizado mais recentemente.

Somente uma das opções a seguir pode existir na matriz de priorização por vez:
- `identified` refere-se à priorização de um usuário com uma `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

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
  "merge_behavior": "merge"
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
