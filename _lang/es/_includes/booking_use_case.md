# Casos de uso: Sistema de recordatorios de reservas por correo electrónico

> Braze es una plataforma integral de interacción con los clientes diseñada para ser altamente controlable de forma programática. En este caso de uso, mostraremos algunas de las formas en que Braze ofrece funcionalidades que pueden integrarse en casos de uso que se encuentran en la intersección entre el producto y el marketing, como los sistemas de reservas.

Este caso de uso muestra cómo puedes utilizar las características de Braze para crear un servicio de mensajería por correo electrónico con recordatorios de reservas. El servicio permitirá a los usuarios reservar citas y les enviará mensajes con recordatorios de sus próximas citas. Aunque este caso de uso utiliza mensajes de correo electrónico, puedes enviar mensajes en cualquier canal o en varios canales basándote en una única actualización del perfil de usuario.

Otros beneficios de crear este servicio incluyen:
- Los mensajes enviados tendrán seguimiento y notificación completos.
- Los usuarios no técnicos de la empresa pueden actualizar el contenido de los mensajes.
- Los mensajes obedecen los estados de adhesión voluntaria y baja en los perfiles de usuario según la configuración de la campaña.
- Puedes utilizar tanto los datos de reserva como los datos de interacción de mensajes para segmentar y dirigirte a los usuarios con mensajes de mensajería adicionales. Por ejemplo, puedes reorientar a aquellos que no abren el mensaje recordatorio inicial con un recordatorio adicional antes de su cita.

Sigue estos pasos para lograr este caso de uso:
1. [Escribe los datos de la próxima reserva en un perfil de usuario de Braze.](#step-1)
2. [Configurar y enviar un mensaje recordatorio de reserva](#step-2)
3. [Gestionar las reservas y cancelaciones actualizadas.](#step-3)

## Paso 1: Escribe los datos de la próxima reserva en un perfil de usuario de Braze. {#step-1}

Utiliza el punto final [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)Braze para escribir un [atributo personalizado anidado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) en el perfil de usuario cada vez que se realice una reserva. Asegúrate de que el atributo personalizado anidado contenga toda la información que necesitas para enviar y personalizar el mensaje recordatorio. En este caso de uso, llamaremos al atributo personalizado anidado «trips».

### Añadir reserva

Cuando un usuario crea una reserva, utiliza la siguiente estructura para la matriz de objetos con el fin de enviar los datos a Braze a través del`/users/track`punto final.

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

El atributo personalizado anidado «trips» se mostrará en el perfil de usuario de la siguiente manera.

![Dos atributos personalizados anidados para un viaje a Londres y un viaje a Sídney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Actualizar reserva
Cuando un usuario actualice una reserva, utiliza la siguiente estructura para la matriz de objetos con el fin de enviar los datos a Braze a través del`/users/track`punto final.

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
{% tab /users/track endpoint %}
#### Enviar datos a través del`/users/track`  punto final
Cuando un usuario elimina una reserva, utiliza la siguiente estructura para la matriz de objetos con el fin de enviar los datos a Braze a través del`/users/track`punto final.

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
#### Escribir atributos anidados en los perfiles de usuario a través del SDK.

Si estás recopilando reservas de citas con tu aplicación, sitio web o ambos y deseas escribir esos datos directamente en un perfil de usuario, puedes utilizar el SDK de Braze para transmitir estos datos. A continuación se muestra un ejemplo en el que se utiliza el SDK Web:

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

Braze elimina la reserva especificada del atributo personalizado anidado en el perfil de usuario y muestra las reservas restantes.

![Un atributo personalizado anidado para un viaje a Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Paso 2: Configurar y enviar un mensaje recordatorio de reserva {#step-2}

### Paso 2a: Crea una audiencia objetivo
Crea una audiencia objetivo para recibir recordatorios utilizando la segmentación multicriterio. Por ejemplo, si deseas enviar un recordatorio dos días antes de la fecha de la reserva, selecciona lo siguiente:

- Una fecha de inicio **en más de 1 día** y
- Una fecha de inicio **en menos de 2 días** 

![Un atributo personalizado anidado «trips» con criterios para una fecha de inicio superior a un día e inferior a dos días.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Paso 2b: Crea tu mensaje

Crea el mensaje de correo electrónico de recordatorio siguiendo los pasos descritos en [Crear un correo electrónico con HTML personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/). Utiliza Liquid para personalizar el mensaje con datos del atributo de cliente personalizado que has creado («viajes»), como en este ejemplo.

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

Inicia la campaña para el mensaje de correo electrónico recordatorio. Ahora, cada vez que Braze recibe el atributo personalizado «viajes», programa un mensaje según los datos incluidos en el objeto de la reserva correspondiente.

## Paso 3: Gestionar las actualizaciones y cancelaciones de reservas. {#step-3}

Ahora que estás enviando mensajes recordatorios, puedes configurar mensajes de confirmación para enviar cuando se actualicen o cancelen las reservas.

### Paso 3a: Enviar datos actualizados

{% tabs %}
{% tab /users/track %}

#### Enviar datos a través del`/users/track`  punto final
Utiliza el punto final [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)Braze para enviar un evento personalizado cuando un usuario actualice o cancele una reserva. En ese caso, introduce los datos necesarios en las propiedades del evento que confirmarán el cambio. 

Supongamos que, en este caso de uso, un usuario ha actualizado la fecha de su viaje a Sídney. El evento sería así:

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

#### Escribir atributos anidados en los perfiles de usuario a través del SDK.

Envía eventos personalizados al perfil de usuario a través del SDK. Por ejemplo, si utilizas el SDK web, podrías enviar:

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

### Paso 3b: Crea un mensaje para confirmar la actualización.

Crea una [campaña basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para enviar al usuario una confirmación de su reserva actualizada. Puedes [utilizar Liquid para crear plantillas con las propiedades del evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que reflejen el nombre, la hora anterior y la nueva hora de la reserva (o solo el nombre si se trata de una cancelación) en el propio mensaje.

Por ejemplo, podrías redactar el siguiente mensaje:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Paso 3c: Modifica el perfil de usuario para reflejar la actualización.

Por último, para enviar los recordatorios de reserva de los pasos 1 y 2 basados en los datos más recientes, actualiza los atributos personalizados anidados para reflejar el cambio o la cancelación en la reserva.

#### Reserva actualizada

Si el usuario de este caso de uso actualizara su viaje a Sídney, utilizarías el`/users/track`  punto final para cambiar la fecha con una llamada como esta:

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

#### Reserva cancelada

Si el usuario de este caso de uso cancelara su viaje a Sídney, enviarías la siguiente llamada al`/users/track`  punto final:

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

Una vez enviadas estas llamadas y actualizado el perfil de usuario, los mensajes de recordatorio de la reserva reflejarán los datos más recientes sobre las fechas de reserva del usuario.

