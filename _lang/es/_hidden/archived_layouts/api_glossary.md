---
title: Glosario API o Código
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Esta es la descripción de la Búsqueda de Google. Los caracteres que pasan de 160 se truncan, sé breve."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 Crear plantilla de correo electrónico
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Publicar,Correo electrónico,Crear,Plantilla,REST,API
{% endapitags %}

Utiliza las API REST de plantillas de correo electrónico para administrar mediante programación las plantillas de correo electrónico que almacenaste en los paneles Braze, en la página Plantillas y medios. Braze proporciona dos puntos finales para crear y actualizar tus plantillas de correo electrónico.

La respuesta de este punto final incluye un campo para `email_template_id`, que puede utilizarse para actualizar la plantilla en posteriores llamadas a la API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### EJEMPLO DE RESPUESTA
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### DETALLES DE LOS PARÁMETROS

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `modified_after`  | No | Cadena en ISO 8601 | Recupera solo las plantillas actualizadas a partir de la hora indicada o después. |
| `modified_before`  |  No | Cadena en ISO 8601 | Recupera sólo las plantillas actualizadas a la hora indicada o antes. |
| `limit` | No | Número positivo | Número máximo de plantillas a recuperar, predeterminado a 100 si no se proporciona, el valor máximo aceptable es 1000. |
| `offset`  |  No | Número positivo | Número de plantillas que saltar antes de devolver el resto de plantillas que se ajustan a los criterios de búsqueda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 Plantilla de correo electrónico de lista disponible
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Obtener,Correo electrónico,Plantilla,Lista,REST
{% endapitags %}

Utiliza los siguientes puntos finales para obtener una lista de las plantillas disponibles.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### EJEMPLO DE RESPUESTA
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### DETALLES DE LOS PARÁMETROS

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `email_template_id`  | Sí | Cadena | El identificador API de tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 Campañas Desencadenar envío
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Publicar, Campañas, Desencadenar,Enviar{% endapitags %}

La entrega desencadenada por API te permite alojar el contenido de los mensajes dentro del panel de Braze, a la vez que dictas cuándo se envía un mensaje y a quién a través de tu API. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### EJEMPLO DE RESPUESTA
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### DETALLES DE LOS PARÁMETROS

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `email_template_id`  | Sí | Cadena | El identificador API de tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 Campañas Desencadenar envío
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campañas, Desencadenar, Enviar{% endapitags %}

Este punto final puede utilizarse para registrar eventos personalizados, atributos de usuario y compras de usuarios. Puedes incluir hasta 75 atributos, eventos y objetos de compra por solicitud. Es decir, sólo puedes publicar atributos para un máximo de 75 usuarios a la vez, pero en la misma llamada a la API también puedes proporcionar hasta 75 eventos y hasta 75 compras.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### REQUEST BODY
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### EJEMPLO DE RESPUESTA
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### DETALLES DE LOS PARÁMETROS

| Campo Perfil de usuario | Especificación del tipo de datos |
| ---| --- |
| country | (cadena) Requerimos que los códigos de país se pasen a Braze en la [norma ISO-3166-1 alfa-2][17]. |
| current_location | (objeto) De la forma {"longitude": -73.991443, "latitude": 40.753824} |
| fecha_de_primera_sesión | (fecha en la que el usuario utilizó la aplicación por primera vez) Cadena en formato ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| fecha_de_última_sesión | (fecha en la que el usuario utilizó la aplicación por última vez) Cadena en formato ISO 8601 o en formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| dob | (fecha de nacimiento) Cadena en formato "AAAA-MM-DD", por ejemplo, 1980-12-21. |
| correo electrónico | (cadena) |
| email_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes de correo electrónico), "unsubscribed" (excluido explícitamente de los mensajes de correo electrónico) y "subscribed" (ni opted in ni out).  |
| external_id | (cadena) Del identificador único del usuario. |
| Facebook | hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| first_name | (cadena) |
| gender | (cadena) "M", "F", "O" (otro), "N" (no procede), "P" (prefiere no decirlo) o nil (desconocido). |
| home_city | (cadena) |
| URL_imagen | (cadena) URL de la imagen que se asociará al perfil de usuario. |
| language | (cadena) requerimos que el idioma se pase a Braze en la [norma ISO-639-1][24]. <br>[Lista de lenguas aceptadas][1]|
| last_name | (cadena) |
|marked_email_as_spam_at| (cadena) Fecha en la que el correo electrónico del usuario fue marcado como correo no deseado. Aparece en formato ISO 8601 o en formato aaaa-MM-dd'T'HH:mm:ss:SSSZ.|
| teléfono | (cadena) |
| push_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes push), "unsubscribed" (excluido explícitamente de los mensajes push) y "subscribed" (ni opted in ni opted out).  |
| push_tokens | Matriz de objetos con `app_id` y cadena `token`. Opcionalmente, puedes proporcionar un `device_id` para el dispositivo al que está asociado este token, por ejemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si no se proporciona un `device_id`, se generará uno aleatoriamente. |
| zona_horaria | (cadena) Del nombre de la zona horaria de la [Base de datos de zonas horarias de la IANA][26] (por ejemplo, "America/New_York" o "Eastern Time (US & Canada)"). Sólo se establecerán los valores de zona horaria válidos. |
| twitter | Hash que contiene `id` (entero), `screen_name` (cadena, X (antes Twitter) handle), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
