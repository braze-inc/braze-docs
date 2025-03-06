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

- [iOS][2]
- [Android][3]
- [Web][4]

En general, las aplicaciones móviles utilizarán el chip GPS del dispositivo y otros sistemas (como el escaneado Wi-Fi) para rastrear la ubicación del usuario. Las aplicaciones Web utilizarán WPS (Sistema de Posicionamiento Wi-Fi) para seguir la ubicación de un usuario. Todas estas plataformas requerirán que los usuarios acepten voluntariamente el seguimiento de ubicación. La precisión de tus datos de seguimiento de ubicación puede verse afectada por el hecho de que tus usuarios tengan o no habilitada la conexión Wi-Fi en sus dispositivos. Los usuarios de Android también pueden elegir diferentes modos de localización: los usuarios que estén en modo "Ahorro de batería" o "Sólo dispositivo" pueden tener datos inexactos.

### Ubicación del usuario del SDK por dirección IP

A partir del 26 de noviembre de 2024, Braze detectará la ubicación de los usuarios desde el país geolocalizado utilizando la dirección IP desde el inicio de la primera sesión del SDK. 

Antes de esto, Braze utilizaba el código de país de la configuración regional del dispositivo durante la creación del usuario del SDK y durante la duración de la primera sesión. Sólo después de procesar el inicio de la primera sesión se utilizaría la dirección IP para configurar el país más fiable en el usuario. Esto significaba que el país del usuario sólo se configuraba con mayor precisión a partir de la segunda sesión, sólo después de procesar el inicio de la primera sesión.

Ahora, Braze utilizará la dirección IP para establecer el valor del país en los perfiles de usuario creados a través del SDK, y esa configuración del país basada en la IP estará disponible durante y después de la primera sesión.

## Segmentación de ubicación

Utilizando los datos de seguimiento de la ubicación y los segmentos, puede configurar campañas y estrategias basadas en la ubicación. Por ejemplo, puedes querer realizar una campaña promocional para usuarios que vivan en una región concreta o excluir a usuarios de una región que tenga normativas más estrictas.

Para más información sobre la creación de un segmento de ubicación, consulte la sección [Orientación por][1] ubicación.

## Configuración difícil del atributo de ubicación por defecto

También puedes utilizar el [punto final`users/track` ][8] de nuestra API para actualizar el atributo estándar [`current_location`][9]. Un ejemplo:

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

- [Radar][6]
- [Infillion][10]
- [Foursquare][7]

## Preguntas más frecuentes

Consulte nuestras [FAQ sobre][11] ubicaciones para obtener respuestas a las preguntas más frecuentes sobre ubicaciones.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
