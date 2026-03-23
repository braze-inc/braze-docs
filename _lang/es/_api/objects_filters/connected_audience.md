---
nav_title: "Filtro y objeto de audiencia conectada"
article_title: Objeto de audiencia conectada de API
page_order: 3
page_type: reference
description: "Este artículo explica el objeto de audiencia conectada, incluyendo cómo funciona, casos de uso y los diferentes filtros que lo crean."

---

# Objeto de audiencia conectada

> Una audiencia conectada es un filtro de audiencia dinámico que defines en línea dentro de tu solicitud de API, para que puedas dirigirte a los usuarios correctos en el momento del envío sin crear ni gestionar segmentos en el dashboard de Braze.

En lugar de crear previamente un segmento para cada posible combinación de audiencia, pasas los criterios de filtro directamente en el parámetro `audience` de tu llamada a la API. Braze evalúa a cada usuario contra esos criterios en tiempo real y entrega el mensaje solo a los usuarios que coincidan. Esto significa que una sola campaña, Canvas o definición de mensaje solo de API puede servir a un número ilimitado de variaciones de audiencia, impulsadas completamente por tu lógica de negocio.

## Cómo funciona

1. Define tu mensaje creando una campaña activada por API o un Canvas en el dashboard de Braze, o define el contenido del mensaje completamente en línea usando los [objetos de mensajería]({{site.baseurl}}/api/objects_filters/#messaging-objects) en tu solicitud de API. Usa [propiedades de desencadenamiento]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) o [contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object/) para personalización dinámica.
2. Llama a un punto de conexión compatible e incluye el parámetro `audience` con tus criterios de filtro. Puedes filtrar por atributos personalizados, estado de suscripción push, estado de suscripción de correo electrónico y hora de último uso de la aplicación.
3. Braze evalúa los filtros en el momento del envío, entregando el mensaje solo a los usuarios que coincidan con tus criterios.

{% alert tip %}
No se requiere un `campaign_id` cuando usas el parámetro `audience`. Los puntos de conexión [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) y [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) te permiten definir el contenido del mensaje en línea sin una campaña creada previamente. Sin embargo, si deseas rastrear métricas a nivel de campaña (como envíos, clics o rebotes) en el dashboard, incluye un `campaign_id`.
{% endalert %}

Dado que la audiencia se define por solicitud, tus sistemas de backend pueden desencadenar mensajes contextualmente relevantes en respuesta a cualquier evento de negocio (un cambio de precio, una alerta meteorológica, una actualización de puntuación en vivo) sin intervención del dashboard.

### Puntos de conexión compatibles

Puedes usar el objeto de audiencia conectada con el parámetro `audience` en estos puntos de conexión:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)

## Casos de uso

Usa audiencias conectadas para escenarios en los que tus sistemas de backend detectan un evento y necesitan notificar a un conjunto de usuarios determinado dinámicamente:

| Categoría | Ejemplo |
| --- | --- |
| Alertas meteorológicas | Un proveedor de datos meteorológicos detecta un evento climático severo y envía notificaciones push a los usuarios cuyo atributo `preferred_city` coincide con el área afectada. |
| Deportes y eventos en vivo | Una aplicación deportiva envía actualizaciones de puntuación en tiempo real o alertas de partidos a los usuarios cuyo atributo `favorite_team` coincide con uno de los equipos que juegan. |
| Contenido y entretenimiento | Un servicio de streaming notifica a los usuarios cuya matriz `favorite_shows` incluye el título de una serie cada vez que se estrena un nuevo episodio. |
| Comercio electrónico | Un comercio minorista en línea envía alertas de bajada de precio o de reposición de stock a los usuarios cuya matriz `wishlisted_products` incluye el ID del producto relevante. |
| Viajes | Una aplicación de viajes envía notificaciones de retraso de vuelo a los usuarios cuyo atributo `booked_flight` coincide con el número de vuelo afectado. |
| Servicios financieros | Una plataforma de trading alerta a los usuarios cuya matriz `watchlist` incluye un símbolo bursátil que ha cruzado un umbral de precio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En cada caso, una sola campaña o definición de mensaje solo de API maneja todas las variaciones. Tu backend determina los valores de filtro y los pasa en la solicitud de API, por lo que no necesitas crear un segmento o campaña separada para cada producto, programa, equipo o ubicación.

## Ejemplo de solicitud

El siguiente ejemplo usa el punto de conexión [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) para dirigirse a los usuarios que han marcado como favorito un programa específico y han optado por recibir notificaciones push:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Cuerpo del objeto

El objeto de audiencia conectada se compone de un único filtro de audiencia conectada o de varios filtros de audiencia conectada combinados con los operadores `AND` y `OR`.

**Ejemplo con múltiples filtros:**

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

## Filtros de audiencia conectada

Combina varios filtros con los operadores `AND` y `OR` para crear un filtro de audiencia conectada.

### Filtro de atributo personalizado

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
### Filtro de suscripción push

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

### Filtro de suscripción de correo electrónico

Este filtro te permite segmentar en función del estado de suscripción de correo electrónico de un usuario.

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

### Filtro de última aplicación utilizada

Este filtro te permite segmentar en función de cuándo el usuario utilizó la aplicación por última vez. Estos filtros contienen dos campos:

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

Las audiencias conectadas no pueden filtrar a los usuarios por atributos predeterminados, eventos personalizados, segmentos o eventos de interacción con mensajes. Para utilizar estos filtros, recomendamos incorporarlos a un segmento de audiencia y, a continuación, especificar ese segmento en el parámetro `segment_id` del [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Si utilizas otros puntos de conexión, primero deberás añadir el segmento a la campaña activada por API o al Canvas en el dashboard de Braze.