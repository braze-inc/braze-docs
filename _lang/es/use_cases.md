---
nav_title: Casos de uso de la API
article_title: Casos de uso de la API
description: "Tanto si eres un desarrollador experto como un especialista en marketing con recursos mínimos de desarrollo, este artículo de referencia está diseñado para ayudarte a comprender cómo aprovechar la potencia de la API REST de Braze para realizar diversas tareas y mejorar tu estrategia de interacción con los clientes."
page_type: reference
page_order: 4.8
---

# Casos de uso de la API

> [La API REST de Braze]({{site.baseurl}}/api/basics/) proporciona una amplia gama de puntos finales diseñados para ayudar a gestionar y optimizar tu estrategia de interacción con los clientes. En este artículo, exploraremos varios casos de uso para cada punto final de recopilación: catálogos, listas de correo electrónico y direcciones, exportación, mensajes, centro de preferencias, SMS, grupos de suscripción, plantillas y datos de usuario.<br><br>Cada sección presenta un escenario con una guía paso a paso, un ejemplo de código y el resultado esperado. Al final de este artículo, comprenderás mejor cómo utilizar la API REST de Braze para mejorar tus esfuerzos de interacción con los clientes.

## Eliminar varios elementos de un catálogo

Un nuevo año da la bienvenida a nuevos lanzamientos de productos en Kitchenerie, una marca minorista especializada en utensilios de cocina. En el panel de Braze, Kitchenerie tiene configurado un catálogo para su colección de vajilla llamado "Vajilla". Este nuevo año también supone la retirada de los siguientes productos de su colección de vajillas.

* Bizcocho liso
* Porcelana perlada
* Brillo rosa

Para eliminar estos productos de su catálogo, Kitchener puede utilizar el [punto final`/catalogs/{catalog_name}/items` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) para introducir los ID de los elementos.

Este es el ejemplo de solicitud:

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

Tras enviar esta carga útil, la siguiente respuesta confirma que las tres colecciones se han eliminado correctamente del catálogo de vajillas de Kitchenerie.

```json
{
  "message": "success"
}
```

## Eliminar correos electrónicos de la lista de correo no deseado Braze

En MovieCanon, una empresa de servicios de streaming, el equipo de desarrolladores es responsable de auditar periódicamente sus listas de correo electrónico para identificar y mantener a los usuarios suscritos a sus campañas de correo electrónico. Como parte de esta auditoría, MovieCanon quiere eliminar esta lista de correos electrónicos de su lista de correo no deseado:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

Para llevar a cabo esta tarea, el equipo de desarrolladores necesitará una clave de API con el permiso `email.spam.remove` para utilizar el punto final `/email/spam/remove`. Este punto final elimina direcciones de correo electrónico de la lista de correo no deseado de Braze y de la lista de correo no deseado mantenida por el proveedor de correo electrónico de MovieCanon.

Para enviar esta solicitud, incluye una dirección de correo electrónico de cadena o una matriz de hasta 50 direcciones de correo electrónico para modificar. Como la lista de correos electrónicos a eliminar es inferior a 50, MovieCanon puede realizar esta tarea con el siguiente cuerpo de solicitud:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

Tras enviar esta carga útil con éxito, esta respuesta confirma que los correos han sido eliminados de la lista de correo no deseado de MovieCanon.

```json
{
  "message": "success"
}
```

## Auditar todos los lienzos

Siege Valley Health es un sistema hospitalario que incluye 10 hospitales en funcionamiento y centros de investigación con miles de pacientes. Su equipo de marketing quiere comparar los Lienzos enviados a los pacientes para recordarles que concierten una cita para vacunarse contra la gripe de los últimos 3 años de uso de Braze. El equipo de marketing de Siege Valley Health también quiere una forma rápida y eficaz de ver tanto la lista de Lienzos como el resumen de análisis.

Veamos cómo Siege Valley Health puede llevar a cabo estas dos tareas utilizando una combinación de puntos finales en lugar de filtrar a través del panel Braze.

Para la primera tarea de auditoría de Lienzos, utiliza el [punto final`/canvas/list` ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) para exportar una lista de Lienzos que incluya el nombre y las etiquetas. He aquí un ejemplo de solicitud:

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

Pasemos a la siguiente tarea de ver el resumen de análisis del primer Canvas de la lista de Canvas de Siege Valley Health. Para ello, utilizaríamos el [punto final`/canvas/data_summary` ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) con los siguientes parámetros de solicitud:

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

Aquí tienes un ejemplo de solicitud:

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Comprobación de las próximas campañas y lonas programadas

La época más ajetreada del año se acerca rápidamente para Flash & Thread, una marca de comercio minorista que vende ropa y productos de belleza en línea y en tiendas. Su equipo de marketing quiere comprobar las próximas campañas y Lienzos desde el panel de Braze antes del 31 de marzo de 2024, a las 12 h. Para ello, se puede utilizar el [punto final`/messages/scheduled_broadcasts` ]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/). 

Este es el ejemplo de solicitud:

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

Este punto final devolverá la lista de próximas campañas y Lienzos. A partir de aquí, el equipo de marketing puede confirmar su lista de mensajes consultando el campo `name` para las campañas y Lienzos en la respuesta.

## Ver un centro de preferencias antiguo

PoliterWeekly es una revista digital a la que se puede llegar a los suscriptores a través del correo electrónico. En un esfuerzo por comprender mejor el recorrido del usuario de sus suscriptores, el equipo de marketing quiere revisar los detalles del centro de preferencias de PoliterWeekly para comprobar cuándo se creó y actualizó por última vez.

Utilizando el [punto final`/preference_center/v1/{preferenceCenterExternalID}` ]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), el equipo de marketing sólo tiene que insertar el ID externo del centro de preferencias como parámetro de ruta, que quedaría así:

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

A partir de esta respuesta, el equipo de marketing puede ver que el centro de preferencias se creó 3 años antes de su actualización más reciente. Con esta información en mente, el equipo de marketing podría crear y lanzar un nuevo centro de preferencias.

{% enddetails %}

## Eliminar números de teléfono no válidos

En CashBlastr, el objetivo principal es agilizar la forma en que la gente puede enviar y recibir pagos rápidos. Como empresa de servicios financieros, CashBlastr quiere mantener actualizada y precisa su lista de números de teléfono para sus clientes. Se ha encargado al equipo de desarrolladores que elimine la siguiente lista de números de teléfono marcados como "no válidos" para que los mensajes SMS del equipo de marketing puedan llegar a los clientes CashBlastr adecuados.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

Para enviar una solicitud con el [punto final`/sms/invalid_phone_numbers/remove` ]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/), los números de teléfono deben estar en una matriz de cadenas en [formatoe.164 ](https://en.wikipedia.org/wiki/E.164), con un máximo de 50 números de teléfono por solicitud. Como la lista no supera los 50 números de teléfono, aquí tienes un ejemplo del cuerpo de la solicitud que enviaría el equipo de desarrolladores de CashBlastr:

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

Tras enviar esta carga útil, la siguiente respuesta confirma que los números de teléfono no válidos de CashBlastr se han eliminado de la lista de inválidos de Braze.

```json
{
  "message": "success"
}
```

## Ver el estado del grupo de suscripción de un usuario

SandwichEmperor es una cadena de restaurantes de comida rápida de Estados Unidos, y su equipo de marketing quiere comprobar los estados del grupo de suscripción de una lista aleatoria de sus usuarios por SMS. Usando el [punto final`/subscription/status/get` ]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), SandwichEmperor puede realizar esta tarea para un usuario individual con la siguiente petición de ejemplo:

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

Este punto final también enumera los estados del grupo de suscripción de un usuario por correo electrónico y puede utilizarse para ver el estado del grupo de suscripción de varios usuarios.

## Comprobación de una plantilla HTML para mensajería por correo electrónico

En WorkFriends, una red social que ayuda a crear conexiones entre trabajadores de distintos sectores, su equipo de marketing se encarga de enviar campañas por correo electrónico a sus usuarios. Estas campañas suelen incluir recordatorios de eventos locales, boletines semanales y actividades destacadas del perfil.

En este escenario, WorkFriends ha utilizado históricamente una plantilla HTML singular con su marca heredada. En un esfuerzo por alinear su identidad de marca, WorkFriends quiere verificar si hay alguna información útil en esta plantilla HTML para aprovecharla antes de hacer la transición a una nueva plantilla.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

Después de revisar esta información de la plantilla, WorkFriends también puede utilizar el [punto final`/templates/email/update` ]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) para actualizar la plantilla de correo electrónico a través de la API. La plantilla de correo electrónico del panel de Braze reflejará estas modificaciones.
