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

En general, las aplicaciones móviles utilizan el chip GPS del dispositivo y otros sistemas (como el escaneado Wi-Fi) para seguir la ubicación del usuario. Las aplicaciones Web utilizan WPS (Sistema de Posicionamiento Wi-Fi) para seguir la ubicación de un usuario. Todas estas plataformas requieren que los usuarios acepten voluntariamente el seguimiento de ubicación. La precisión de tus datos de seguimiento de ubicación puede verse afectada por el hecho de que tus usuarios tengan o no habilitada la conexión Wi-Fi en sus dispositivos. Los usuarios de Android también pueden elegir diferentes modos de localización: los usuarios que estén en modo "Ahorro de batería" o "Sólo dispositivo" pueden tener datos inexactos.

### Ubicación del usuario del SDK por dirección IP

Braze detecta la ubicación del usuario a partir del país geolocalizado utilizando la dirección IP del inicio de la primera sesión del SDK. 

Anteriormente, Braze utilizaba el código de país de la configuración regional del dispositivo durante la creación del usuario del SDK y mientras duraba la primera sesión. Sólo después de procesar el inicio de la primera sesión se utilizaría la dirección IP para configurar el país más fiable en el usuario. Esto significaba que el país del usuario sólo se configuraba con mayor precisión a partir de la segunda sesión, sólo después de procesar el inicio de la primera sesión.

Ahora, Braze utiliza la dirección IP para establecer el valor del país en los perfiles de usuario creados a través del SDK, y esa configuración del país basada en la IP está disponible durante y después de la primera sesión.

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

- Si la ubicación está desactivada, el filtro `Most Recent Location` muestra la última ubicación registrada.
- Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, se le puede aplicar el filtro `Location Available`, aunque haya renunciado al seguimiento de ubicación desde entonces.

### ¿Cuál es la diferencia entre los filtros Localización más reciente del dispositivo y Localización más reciente?

La dirección `Most Recent Device Locale` procede de la configuración del dispositivo del usuario. Por ejemplo, esto aparece para los usuarios de iPhone en su dispositivo en **Configuración** > **General** > **Idioma & Región**. Este filtro se utiliza para capturar el idioma y el formato regional, como fechas y direcciones, y es independiente del filtro `Most Recent Location`.

La dirección `Most Recent Location` es la última ubicación GPS conocida del dispositivo. Se actualiza al iniciar la sesión y se almacena en el perfil del usuario.

### Si un usuario renuncia al seguimiento de ubicación, ¿se eliminan de Braze sus datos de ubicación anteriores?

No. Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, esos datos no se eliminan automáticamente si posteriormente el usuario opta por no participar en el seguimiento de ubicación.

## Solución de problemas

### Ningún usuario tiene ubicaciones disponibles

Braze captura la ubicación más reciente de un usuario de forma predeterminada a través del SDK. Esto suele significar que la "ubicación reciente" es la ubicación desde la que tu usuario utilizó tu aplicación más recientemente. Si envías a Braze datos de ubicación en segundo plano, es posible que dispongas de datos más granulares.

Si no hay usuarios con ubicaciones disponibles, dos comprobaciones rápidas pueden ayudarte a confirmar la recopilación de datos y la transferencia de fechas.

#### Recopilación de datos

Confirma que tu aplicación está recopilando datos de ubicación:

- Para iOS, esto significa que los usuarios optan por compartir sus datos de ubicación a través de un aviso en algún punto del recorrido del usuario. 
- Para Android, confirma que tu aplicación pide permisos de ubicación fina o gruesa en la instalación.

Para ver si los datos de ubicación del usuario se envían a Braze, utiliza el filtro **Ubicación disponible**. Este filtro te permite ver el porcentaje de usuarios con una "ubicación más reciente".

![Un segmento de "Ubicación de prueba" que utiliza el filtro "Ubicación disponible".]({% image_buster /assets/img_archive/trouble7.png %})

#### Transferencia de datos

Confirma que tus desarrolladores pasan datos de ubicación a Braze. Normalmente, el SDK gestiona automáticamente la transmisión de datos de ubicación después de que el usuario dé sus permisos, pero es posible que tus desarrolladores hayan desactivado el seguimiento de ubicación en Braze. Puedes encontrar más información sobre el seguimiento de ubicación en:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)