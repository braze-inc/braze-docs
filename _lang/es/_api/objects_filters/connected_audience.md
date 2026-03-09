---
nav_title: "Filtro y objeto de Audiencia conectada"
article_title: Objeto de Audiencia conectada de API
page_order: 3
page_type: reference
description: "Este artículo explica los diferentes componentes del objeto audiencia conectada y los filtros que lo crean."

---

# Objeto de audiencia conectado

> Un objeto de audiencia conectado tiene un identificador que identifica la audiencia de tu mensaje. Por ejemplo, si utilizas matrices de atributos personalizados para realizar el seguimiento de todas las categorías y programas de televisión que un usuario ha marcado como favoritos, puedes utilizar las audiencias conectadas para enviar automáticamente una notificación push o un correo electrónico a cualquier persona que haya marcado un programa como favorito cada vez que se estrene un nuevo episodio, sin necesidad de configurar un segmento para cada programa.

Este objeto se compone de un único filtro de audiencia conectado o de varios filtros de audiencia conectados en una expresión lógica que utiliza los operadores `AND` o `OR`.

**Ejemplo de filtro múltiple:**

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

## Filtros de audiencia conectados

La combinación de varios filtros de atributos personalizados con los operadores`AND``OR`  y  crea un filtro de audiencia conectado.

### Filtro de atributos personalizado

Este filtro te permite segmentar en función del atributo personalizado de un usuario. Estos filtros contienen hasta tres campos:

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

#### Comparaciones permitidas por tipo de datos

El tipo de datos del atributo personalizado determina las comparaciones válidas para un filtro determinado.

| Tipo de atributo personalizado | Comparaciones permitidas |
| ---------------------| --------------- |
| Cadena | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Matriz | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numérico | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Booleano | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Tiempo | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Advertencias sobre la comparación de atributos

| Comparación | Consideraciones adicionales |
| --- | --- |
| `value` | El `value` no es necesario cuando se utilizan las comparaciones `exists` o `does_not_exist`. `value` debe ser una cadena de fecha y hora ISO 8601 cuando se utilizan las comparaciones `before` y `after`. |
|`matches_regex` | Cuando utilices la comparación `matches_regex`, el valor pasado debe ser una cadena. Para obtener más información sobre el uso de expresiones regulares con Braze, consulta [Expresiones regulares]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) y [Tipos de datos de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Ejemplo de atributo personalizado

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Filtro push de suscripción

Este filtro te permite segmentar en función del estado de suscripción push de un usuario.

#### Cuerpo del filtro

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaciones permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de suscripción por correo electrónico

Este filtro te permite segmentar en función del estado de suscripción al correo electrónico de un usuario.

#### Cuerpo del filtro

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaciones permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de la última aplicación utilizada

Este filtro te permite segmentar en función de cuándo utilizaste por última vez la aplicación. Estos filtros contienen dos campos:

#### Cuerpo del filtro
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparaciones permitidas:** `after`, `before`
- **Valores permitidos:** datetime (cadena ISO 8601)

### Consideraciones

Las audiencias conectadas no pueden filtrar a los usuarios por atributos predeterminados, eventos personalizados, segmentos o eventos de interacción con mensajes. Para utilizar estos filtros, recomendamos incorporarlos a un segmento de audiencia y, a continuación, especificar ese segmento en el`segment_id`parámetro para el[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)[punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Si utilizas otros puntos finales, primero deberás añadir el segmento a la campaña activada por API o al Canvas en el panel de Braze.
