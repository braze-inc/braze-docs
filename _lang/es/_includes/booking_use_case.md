# Casos de uso: Sistema de recordatorio de reservas por correo electrónico

> Braze es una plataforma integral de interacción con los clientes diseñada para ser altamente controlable mediante programación. En este caso de uso, demostraremos sólo algunas formas en las que Braze proporciona funciones que puedes integrar en casos de uso que se encuentran en la intersección del producto y el marketing, como los sistemas de reservas.

Este caso de uso muestra cómo puedes utilizar las características de Braze para crear un servicio de mensajería por correo electrónico de recordatorio de reserva. El servicio permitirá a los usuarios reservar citas y enviará mensajes a los usuarios recordándoles sus próximas citas. Aunque este caso de uso utiliza mensajes de correo electrónico, puedes enviar mensajes en cualquier canal, o en varios, basándote en una única actualización de un perfil de usuario.

Otras ventajas de crear este servicio son:
- Los mensajes enviados tendrán seguimiento e informes completos.
- Los usuarios no técnicos de Braze pueden actualizar el contenido de los mensajes.
- Los mensajes obedecen a los estados de adhesión voluntaria y exclusión voluntaria en los perfiles de usuario por configuración de campaña.
- Tanto los datos de reservas como los de interacción con los mensajes pueden utilizarse para segmentar y dirigir a los usuarios mensajes adicionales. Por ejemplo, puedes reorientar a quienes no abran el mensaje recordatorio inicial con un recordatorio adicional antes de su cita.

Sigue estos pasos para conseguir este caso de uso:
1. [Escribir datos de próximas reservas en un perfil de usuario Braze](#step-1)
2. [Configurar y lanzar un mensaje recordatorio de reserva](#step-2)
3. [Gestionar las reservas y cancelaciones actualizadas](#step-3)

## Paso 1: Escribir datos de próximas reservas en un perfil de usuario Braze {#step-1}

Utiliza el punto final Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para escribir un [atributo personalizado anidado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) en un perfil de usuario cada vez que se realice una reserva. Asegúrate de que el atributo personalizado anidado contiene toda la información que se necesitará para enviar y personalizar el mensaje recordatorio. En este caso de uso, llamaremos "viajes" al atributo personalizado anidado.

### Añadir reserva

Cuando un usuario crea una reserva, utiliza la siguiente estructura para la matriz de objetos para enviar los datos a Braze a través del punto final `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

El atributo personalizado anidado "viajes" se mostrará así en el perfil de usuario.

![Dos atributos personalizados anidados para un viaje a Londres y otro a Sidney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Actualizar reserva
Cuando un usuario actualiza una reserva, utiliza la siguiente estructura para la matriz de objetos para enviar los datos a Braze a través del punto final `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Eliminar reserva

{% tabs %}
{% tab /usuarios/punto final de seguimiento %}
#### Envía datos a través del punto final `/users/track` 
Cuando un usuario elimina una reserva, utiliza la siguiente estructura para la matriz de objetos para enviar los datos a Braze a través del punto final `/users/track`.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### Escribir atributos anidados en perfiles de usuario a través del SDK

Si estás recopilando reservas de citas con tu aplicación, sitio web o ambos y quieres escribir esos datos directamente en un perfil de usuario, puedes utilizar el SDK de Braze para transmitir estos datos. Aquí tienes un ejemplo utilizando el SDK Web:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

La reserva especificada se eliminará del atributo personalizado anidado en el perfil de usuario y mostrará las reservas restantes.

![Un atributo personalizado anidado para un viaje a Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Paso 2: Configurar y lanzar un mensaje recordatorio de reserva {#step-2}

### Paso 2a: Crear una audiencia objetivo
Crea una audiencia objetivo para recibir recordatorios utilizando la segmentación multicriterio. Por ejemplo, si quieres enviar un recordatorio dos días antes de la fecha de reserva, selecciona lo siguiente:

- Una fecha de inicio **en más de 1 día** y
- Una fecha de inicio **en menos de 2 días** 

![Un atributo personalizado anidado "viajes" con criterios para una fecha de inicio superior a un día e inferior a dos.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Paso 2b: Crea tu mensaje

Crea el mensaje de correo electrónico recordatorio siguiendo los pasos de [Crear un correo electrónico con HTML personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/). Utiliza Liquid para personalizar el mensaje con los datos del atributo personalizado de cliente que hayas creado ("viajes"), como en este ejemplo.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Paso 2c: Lanza tu campaña

Lanza la campaña para el mensaje de correo electrónico recordatorio. Ahora, cada vez que Braze reciba el atributo personalizado "viajes", se programará un mensaje según los datos incluidos en el objeto de la reserva correspondiente.

## Paso 3: Gestionar las actualizaciones y cancelaciones de reservas {#step-3}

Ahora que envías mensajes recordatorios, puedes configurar mensajes de confirmación para enviarlos cuando se actualicen o cancelen reservas.

### Paso 3a: Enviar datos actualizados

{% tabs %}
{% tab /usuarios/seguimiento %}

#### Envía datos a través del punto final `/users/track` 
Utiliza el punto final Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para enviar un evento personalizado cuando un usuario actualice o cancele una reserva. En ese caso, introduce los datos necesarios en las propiedades del evento que confirmarán el cambio. 

Digamos que, en este caso de uso, un usuario ha actualizado la fecha de su viaje a Sydney. El evento tendría el siguiente aspecto:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### Escribir atributos anidados en perfiles de usuario a través del SDK

Envía eventos personalizados al perfil de usuario a través del SDK. Por ejemplo, si utilizas el SDK Web, podrías enviar:

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Paso 3b: Crea un mensaje para confirmar la actualización

Crea una [campaña basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para enviar al usuario una confirmación de su reserva actualizada. Puedes [utilizar Liquid para crear plantillas de propiedades del evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que reflejen el nombre, la hora antigua y la hora nueva de la reserva (o sólo el nombre si se trata de una cancelación) en el propio mensaje.

Por ejemplo, podrías redactar el siguiente mensaje:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Paso 3c: Modifica el perfil de usuario para reflejar la actualización

Por último, para enviar los recordatorios de reserva de los pasos 1 y 2 basándote en los datos más recientes, actualiza los atributos personalizados anidados para reflejar el cambio o la cancelación en la reserva.

#### Reserva actualizada

Si el usuario de este caso de uso actualizara su viaje a Sydney, utilizarías el punto final `/users/track` para cambiar la fecha con una llamada como ésta:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Reserva anulada

Si el usuario de este caso de uso cancelara su viaje en Syndey, enviarías la siguiente llamada al punto final `/users/track`:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Una vez enviadas estas llamadas y actualizado el perfil de usuario, los mensajes de recordatorio de reserva reflejarán los datos más recientes sobre las fechas de reserva del usuario.

