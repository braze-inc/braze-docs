---
nav_title: "GET: Estado del grupo de suscripción de los usuarios de la lista"
article_title: "GET: Listar el estado del grupo de suscripción del usuario"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar el estado del grupo de suscripción del usuario de Braze."

---
{% api %}
# Listar el estado del grupo de suscripción del usuario
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Utilice este punto final para obtener el estado de suscripción de un usuario en un grupo de suscripción.

Estos grupos estarán disponibles en la página **Grupo de suscripción**. La respuesta de este punto final incluirá el ID externo y la categoría de suscrito, dado de baja o desconocido para el grupo de suscripción específico solicitado en la llamada a la API. Esto se puede utilizar para actualizar el estado del grupo de suscripción en posteriores llamadas a la API o para mostrarlo en una página web alojada.

Si desea ver ejemplos o probar este punto final para **Grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de Suscripción SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.status.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Obligatoria | Cadena | La dirección `id` de su grupo de suscripción. |
| `external_id`  |  Requerido* | Cadena | La dirección `external_id` del usuario (debe incluir como mínimo uno y como máximo 50 `external_ids`). <br><br>Cuando se envían tanto un `external_id` como un `email`/`phone`, solo se aplicarán a la consulta de resultados los `external_id` proporcionados. |
| `email` | Requerido* | Cadena | La dirección de correo electrónico del usuario. Se puede pasar como una matriz de cadenas con un máximo de 50.<br><br> Si envías una dirección de correo electrónico y un número de teléfono (sin `external_id`), se producirá un error. |
| `phone` | Requerido* | Cadena en [E.164](https://en.wikipedia.org/wiki/E.164) formato | El número de teléfono del usuario. Si no se incluye el correo electrónico, deberá incluir al menos un número de teléfono (con un máximo de 50).<br><br> Si envías una dirección de correo electrónico y un número de teléfono (sin `external_id`), se producirá un error. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Se requiere uno de `external_id` o `email` o `phone` para cada usuario.

- Para los grupos de suscripción de SMS y WhatsApp, se requiere `external_id` o `phone`.  Cuando se envían ambos, sólo se utiliza el `external_id` para la consulta y el número de teléfono se aplica a ese usuario.
- Para los grupos de suscripción por correo electrónico, se requiere `external_id` o `email`.  Cuando se envían ambos, sólo se utiliza el `external_id` para la consulta y la dirección de correo electrónico se aplica a ese usuario.

## Ejemplo de solicitud 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Respuesta

Todas las respuestas correctas devolverán `Subscribed`, `Unsubscribed`, o `Unknown` dependiendo del estado y del historial del usuario con el grupo de suscripción.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
