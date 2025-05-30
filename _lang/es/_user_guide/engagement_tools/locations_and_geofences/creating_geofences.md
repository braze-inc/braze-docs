---
nav_title: Crear geovallas
article_title: Crear geovallas
page_order: 1
page_type: reference
description: "En este artículo de referencia se explica qué son las geovallas y cómo crear y configurar eventos de geovalla."
tool: 
  - Location
search_rank: 9
---

# Geovallas

> El núcleo de la oferta de ubicación en tiempo real de Braze es el concepto de geovalla. Una geo-valla es un área geográfica virtual, representada como latitud y longitud combinadas con un radio, formando un círculo alrededor de una posición global específica. Las geocercas pueden tener desde el tamaño de un edificio hasta el de una ciudad entera.

Puede definir geocercas en el panel de control de Braze y utilizarlas para activar campañas en tiempo real a medida que los usuarios entran y salen de sus fronteras, o enviar campañas de seguimiento horas o días después. Los usuarios que entran o salen de sus geocercas añaden una nueva capa de datos de usuario que puede utilizar para la segmentación y la reorientación.

## Resumen

Gestiona los geovallados desde **Audiencia** > **Ubicaciones**.

Las geovallas se organizan en conjuntos de geovallas: un grupo de geovallas que pueden utilizarse para segmentar o interactuar con los usuarios en toda la plataforma. Cada conjunto de geovallas puede contener un máximo de 10 000 geovallas.

Puede crear o cargar una cantidad ilimitada de geovallas en el panel de control, lo que permite a su equipo de marketing configurar conjuntos de geovallas y campañas sin necesidad de calcular el número de geovallas. Braze resincronizará dinámicamente las geovallas que sigue para cada usuario individual, asegurándose de que las geovallas más relevantes para ellos estén siempre disponibles.

- Las aplicaciones de Android solo pueden almacenar localmente hasta 100 geovallas a la vez. Braze está configurado para almacenar solo hasta 20 geovallas localmente por aplicación.
- Los dispositivos iOS pueden controlar hasta 20 geovallas a la vez por aplicación. Braze supervisará hasta 20 ubicaciones si hay espacio disponible. 
- Si el usuario tiene derecho a recibir más de 20 geocercas, Braze descargará la cantidad máxima de ubicaciones en función de la proximidad al usuario en el punto de inicio de sesión/actualización push silenciosa.
- Para que las geovallas funcionen correctamente, debes asegurarte de que tu aplicación no está utilizando todos los puntos de geovalla disponibles.

## Crear conjuntos de geovallas

### Creación manual de conjuntos

En la página **Ubicaciones**, haga clic en **\+ Crear conjunto de geovallas**.

![Conjunto de geovallas de aeropuertos alemanes con un usuario que dibuja un radio de dos mil metros en el mapa para el aeropuerto de Hamburgo.][1]

Una vez que hayas creado un conjunto de geovallas, puedes añadir geovallas manualmente dibujándolas en el mapa. Recomendamos crear geovallas con un radio de al menos 200 metros para una funcionalidad óptima. Para más información sobre las opciones configurables, consulta [Configuración de geovallas]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### Creación de conjuntos mediante carga masiva {#creating-geofence-sets-via-bulk-upload}

Las geocercas pueden cargarse en bloque como un objeto GeoJSON de tipo `FeatureCollection`. Cada geo-valla individual es un tipo de geometría `Point` en la colección de características. Las propiedades de cada característica requieren una clave `"radius"`, y una clave opcional `"name"` para cada geovalla. Para cargar su GeoJSON, haga clic en **\+ Crear conjunto de geo-vallas** seguido de **Cargar GeoJSON**.

El siguiente ejemplo representa el GeoJSON correcto para especificar dos geocercas: una para la sede de Braze en Nueva York y otra para la Estatua de la Libertad al sur de Manhattan. Recomendamos crear geovallas con un radio de al menos 100 metros para una funcionalidad óptima.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

Cuando crees tus geovallas, ten en cuenta los siguientes puntos:

- El valor `coordinates` en el GeoJSON tiene el formato [Longitud, Latitud].
- El radio máximo de geovalla que se puede cargar es de 100 000 metros (unos 100 kilómetros o 62 millas).

## Actualizar los conjuntos de geovallas

Para los usuarios activos, el SDK de Braze solo solicitará geovallas una vez al día al iniciar la sesión. Esto significa que, si se realizan cambios en los conjuntos de geovallas después de iniciar la sesión, tendrás que esperar 24 horas desde el momento en que los conjuntos se desplieguen por primera vez para recibir el conjunto actualizado.

Para los usuarios inactivos, si el usuario tiene activado el push en segundo plano, Braze también enviará un push silencioso una vez cada 24 horas para descargar las ubicaciones más recientes en el dispositivo.

{% alert note %}
Si las geovallas no se cargan en el dispositivo localmente, el usuario no puede desencadenar el geovallado aunque entre en la zona.
{% endalert %}

### Actualización para usuarios individuales

Actualizar las geocercas para usuarios individuales puede ser útil a la hora de realizar pruebas. Para actualizar los conjuntos de geovallas, vaya a la parte inferior de la página **Ubicaciones** y haga clic en **Resincronizar geovallas**. A continuación, se le pedirá que introduzca `external_id` o `email` de los usuarios que desea actualizar.

## Usar eventos de geovallas

Una vez configuradas las geocercas, puede utilizarlas para mejorar y enriquecer la forma de comunicarse con sus usuarios.

### Desencadenantes

Para utilizar datos de geocercas como parte de los activadores de campañas y Canvas, seleccione **Entrega basada en acciones** para el método de entrega. A continuación, añade una acción desencadenante de `Trigger a Geofence`. Por último, elige el conjunto de geovallas y los tipos de eventos de transición de geovalla para tu mensaje. También puede hacer avanzar a los usuarios a través de un lienzo mediante eventos de geovalla.

![][2]

### Personalización

Para utilizar datos de geofence para personalizar un mensaje, puede utilizar la siguiente sintaxis de personalización de Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Preguntas más frecuentes

Visita [Preguntas frecuentes sobre geovallas][3] para obtener respuestas a las preguntas más frecuentes sobre geovallas.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
