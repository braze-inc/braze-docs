---
nav_title: Mayo
page_order: 8
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de mayo de 2020."
---
# Mayo de 2020

## Google Tag Manager

Se ha añadido documentación y ejemplos sobre cómo desplegar y gestionar el SDK de Android de Braze mediante [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).

## Nuevo punto final API de correo electrónico de lista negra

Ahora puedes [hacer listas negras de]({{site.baseurl}}/api/endpoints/email/post_blacklist/) direcciones de correo electrónico a través de la API de Braze. Poner una dirección de correo electrónico en la lista negra cancelará la suscripción del usuario al correo electrónico y lo marcará como rebotado duro.

## Cambio de clave de API para los puntos finales de la API Braze

A partir de mayo de 2020, Braze ha cambiado la forma de leer las claves de API para que sean más seguras. Ahora las claves de API deben pasarse como encabezado de solicitud. Puedes encontrar ejemplos en las páginas de cada punto final, en **Solicitud de ejemplo**, así como en la **Explicación de la clave de API**.

Braze seguirá admitiendo que `api_key` se pase a través del cuerpo de la solicitud y los parámetros de la URL, pero con el tiempo dejará de serlo (TBD). **Actualiza tus llamadas a la API en consecuencia.** Estos cambios se han actualizado en [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details Explicación de la clave de API %}
{% tabs %}
{% tab Solicitud GET %}
Este ejemplo utiliza el punto final `/email/hard_bounces`.

**Antes: Clave de API en el cuerpo de la solicitud**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**Ahora: Clave de API en la cabecera**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab Solicitud POST %}
Este ejemplo utiliza el punto final `/user/track`.

**Antes: Clave de API en el cuerpo de la solicitud**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Ahora: Clave de API en la cabecera**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


