---
nav_title: "GET: Lista de grupos de suscripción de usuarios"
article_title: "GET: Lista Grupos de suscripción de usuarios"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Braze Lista de grupos de suscripción de usuarios."

---
{% api %}
# Lista los grupos de suscripción del usuario
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Utiliza este punto final para listar y obtener los grupos de suscripción con el historial de un determinado usuario.

Si desea ver ejemplos o probar este punto final para **Grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de Suscripción SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.groups.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `external_id`  | Obligatoria | Cadena | La dirección `external_id` del usuario (debe incluir al menos uno y como máximo 50 `external_ids`). |
| `email`  |  Requerido* | Cadena | La dirección de correo electrónico del usuario, puede pasarse como una matriz de cadenas. Debes incluir al menos una dirección de correo electrónico (con un máximo de 50). |
| `phone` | Requerido* | Cadena en [E.164](https://en.wikipedia.org/wiki/E.164) formato | El número de teléfono del usuario. Debe incluir al menos un número de teléfono (con un máximo de 50). |
| `limit` | Opcional | Entero | El límite del número máximo de resultados devueltos. `limit` predeterminado (y como máximo) es 100. |
| `offset`  |  Opcional | Entero | Número de plantillas que saltar antes de devolver el resto de plantillas que se ajustan a los criterios de búsqueda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Si hay varios usuarios (varios `external_ids`) que comparten la misma dirección de correo electrónico, todos los usuarios serán devueltos como usuarios separados (aunque tengan la misma dirección de correo electrónico o grupo de suscripción).
{% endalert %}

## Ejemplo de solicitud 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Ejemplo de respuesta

Sólo se incluirán en una respuesta correcta los grupos de suscripción que hayan tenido una actualización del estado de suscripción en el historial de un usuario. Esto significa que los grupos de suscripción recién creados no aparecerán en la lista.

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}
