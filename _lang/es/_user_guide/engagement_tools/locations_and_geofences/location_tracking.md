---
nav_title: Seguimiento de la ubicación
article_title: Seguimiento de la ubicación
page_order: 0
page_type: reference
description: "Este artículo de referencia explica cómo utilizar el seguimiento de la ubicación y la orientación por ubicación en sus aplicaciones y qué socios admiten el seguimiento de la ubicación."
tool: Location
search_rank: 2
---

# Seguimiento de la ubicación

> La recopilación de ubicaciones captura la ubicación más reciente de un usuario cuando se abrió la aplicación utilizando datos de ubicación GPS. Puede utilizar esta información para segmentar los datos en función de los usuarios que se encontraban en una ubicación definida.

## Habilitar el seguimiento de ubicación

Para activar la recopilación de ubicaciones en tu aplicación, consulta la guía para desarrolladores de la plataforma que utilices:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

En general, las aplicaciones móviles utilizarán el chip GPS del dispositivo y otros sistemas (como el escaneado Wi-Fi) para rastrear la ubicación del usuario. Las aplicaciones Web utilizarán WPS (Sistema de Posicionamiento Wi-Fi) para seguir la ubicación de un usuario. Todas estas plataformas requerirán que los usuarios acepten voluntariamente el seguimiento de ubicación. La precisión de tus datos de seguimiento de ubicación puede verse afectada por el hecho de que tus usuarios tengan o no habilitada la conexión Wi-Fi en sus dispositivos. Los usuarios de Android también pueden elegir diferentes modos de localización: los usuarios que estén en modo "Ahorro de batería" o "Sólo dispositivo" pueden tener datos inexactos.

### Ubicación del usuario del SDK por dirección IP

A partir del 26 de noviembre de 2024, Braze detectará la ubicación de los usuarios desde el país geolocalizado utilizando la dirección IP desde el inicio de la primera sesión del SDK. 

Antes de esto, Braze utilizaba el código de país de la configuración regional del dispositivo durante la creación del usuario del SDK y durante la duración de la primera sesión. Sólo después de procesar el inicio de la primera sesión se utilizaría la dirección IP para configurar el país más fiable en el usuario. Esto significaba que el país del usuario sólo se configuraba con mayor precisión a partir de la segunda sesión, sólo después de procesar el inicio de la primera sesión.

Ahora, Braze utilizará la dirección IP para establecer el valor del país en los perfiles de usuario creados a través del SDK, y esa configuración del país basada en la IP estará disponible durante y después de la primera sesión.

## Segmentación de ubicación

Utilizando los datos de seguimiento de la ubicación y los segmentos, puede configurar campañas y estrategias basadas en la ubicación. Por ejemplo, puedes querer realizar una campaña promocional para usuarios que vivan en una región concreta o excluir a usuarios de una región que tenga normativas más estrictas.

Para más información sobre la creación de un segmento de ubicación, consulte la sección [Orientación por]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) ubicación.

## Configuración difícil del atributo de ubicación por defecto

También puedes utilizar el [punto final`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de nuestra API para actualizar el atributo estándar [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/). Un ejemplo:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Apoyo a la asociación para balizas y geovallas

La combinación de la beacon o geovalla existente con nuestras características de segmentación y mensajería te proporciona más información sobre las acciones físicas de tus usuarios para que puedas enviarles mensajes en consecuencia. Puedes aprovechar el seguimiento de ubicación con algunos de nuestros socios: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Preguntas más frecuentes

### ¿Cuándo recopila Braze datos de localización?

Braze sólo recoge la ubicación cuando la aplicación está abierta en primer plano. Como resultado, nuestro filtro `Most Recent Location` se dirige a los usuarios en función de dónde abrieron la aplicación por última vez (también denominado inicio de sesión).

También debe tener en cuenta los siguientes matices:

- Si la localización está desactivada, el filtro `Most Recent Location` mostrará la última localización registrada.
- Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, se le aplicará el filtro `Location Available`, aunque desde entonces haya optado por que no se rastree su ubicación.

### ¿Cuál es la diferencia entre los filtros Localización más reciente del dispositivo y Localización más reciente?

La dirección `Most Recent Device Locale` procede de la configuración del dispositivo del usuario. Por ejemplo, esto aparece para los usuarios de iPhone en su dispositivo en **Configuración** > **General** > **Idioma y región**. Este filtro se utiliza para capturar el idioma y el formato regional, como fechas y direcciones, y es independiente del filtro `Most Recent Location`.

La dirección `Most Recent Location` es la última ubicación GPS conocida del dispositivo. Se actualiza al iniciar la sesión y se almacena en el perfil del usuario.

### Si un usuario renuncia al seguimiento de su ubicación, ¿se eliminarán de Braze sus antiguos datos de localización?

No. Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, esos datos no se eliminarán automáticamente si posteriormente el usuario decide no participar en el seguimiento de ubicación.

