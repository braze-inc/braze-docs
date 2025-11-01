---
nav_title: "Filtro e objeto do público conectado"
article_title: Objeto do público conectado à API
page_order: 3
page_type: reference
description: "Este artigo explica os diferentes componentes do objeto de público conectado e os filtros que o criam."

---

# Objeto do público conectado

> Um objeto de público conectado é um seletor que identifica o público para o qual enviar a mensagem. 

Esse objeto é composto de um único filtro de público conectado ou de vários filtros de público conectados em uma expressão lógica usando os operadores `AND` ou `OR`.

**Exemplo de filtro múltiplo:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Filtros de público conectados

A combinação de vários filtros de atributos personalizados criará um filtro de público conectado, que criará um filtro de público conectado quando combinado com os operadores `AND` e `OR`.

### Filtro de atributo personalizado

Esse filtro permite segmentar com base em um atributo personalizado do usuário. Esses filtros contêm até três campos:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Comparações permitidas por tipo de dados

O tipo de dados do atributo personalizado determina as comparações que são válidas para um determinado filtro.

| Tipo de atributo personalizado | Comparações permitidas |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Vetor | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numérico | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Booleano | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Horário | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Advertências sobre a comparação de atribuições

| Comparação | Considerações adicionais |
| --- | --- |
| `value` | O `value` não é necessário ao usar as comparações `exists` ou `does_not_exist`. `value` deve ser uma string de data e hora ISO 8601 ao usar as comparações `before` e `after`. |
|`matches_regex` | Ao usar a comparação `matches_regex`, o valor passado deve ser uma string. Para saber mais sobre o uso de expressões regulares com o Braze, consulte [Expressões regulares]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) e [Tipos de dados de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Exemplo de atributo personalizado

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Filtro de inscrição push

Esse filtro permite segmentar com base no status da inscrição push de um usuário.

#### Corpo do filtro

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparações permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de inscrição de e-mail

Esse filtro permite segmentar com base no status de inscrição de e-mail de um usuário.

#### Corpo do filtro

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparações permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Último filtro de app usado

Esse filtro permite segmentar com base em quando foi a última vez que o usuário usou o app. Esses filtros contêm dois campos:

#### Corpo do filtro
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparações permitidas:** `after`, `before`
- **Valores permitidos:** datetime (string ISO 8601)

### Considerações

Os públicos conectados não podem filtrar usuários por atributos padrão, eventos personalizados, segmentos ou eventos de engajamento de mensagens. Para usar esses filtros, recomendamos incorporá-los em um segmento de público-alvo e, em seguida, especificar esse segmento no parâmetro `segment_id` para o [ponto de extremidade`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Ao usar outros endpoints, você precisará adicionar primeiro o segmento à campanha acionada pela API ou ao Canvas no painel do Braze.
