---
nav_title: Crear geovallas
article_title: Crear geovallas
page_order: 1
page_type: reference
toc_headers: h2
description: "En este artículo de referencia se explica qué son las geovallas y cómo crear y configurar eventos de geovalla."
tool: 
  - Location
search_rank: 9
---

# Geovallas

> El núcleo de la oferta de ubicación en tiempo real de Braze es el concepto de geovalla. Una geo-valla es un área geográfica virtual, representada como latitud y longitud combinadas con un radio, formando un círculo alrededor de una posición global específica. Las geocercas pueden tener desde el tamaño de un edificio hasta el de una ciudad entera.

## Cómo funciona

Las geovallas pueden utilizarse para desencadenar campañas en tiempo real cuando los usuarios entran y salen de sus fronteras, o para enviar campañas de seguimiento horas o días después. Los usuarios que entran o salen de sus geocercas añaden una nueva capa de datos de usuario que puede utilizar para la segmentación y la reorientación.

Las geovallas se organizan en conjuntos de geovallas: un grupo de geovallas que pueden utilizarse para segmentar o interactuar con los usuarios en toda la plataforma. Cada conjunto de geovallas puede contener un máximo de 10 000 geovallas.

Puedes crear o subir un número ilimitado de geovallas.

- Las aplicaciones de Android solo pueden almacenar localmente hasta 100 geovallas a la vez. Braze está configurado para almacenar solo hasta 20 geovallas localmente por aplicación.
- Los dispositivos iOS pueden controlar hasta 20 geovallas a la vez por aplicación. Braze supervisará hasta 20 ubicaciones si hay espacio disponible. 
- Si el usuario es elegible para recibir más de 20 geovallas, Braze descargará la cantidad máxima de ubicaciones en función de la proximidad al usuario en el punto de inicio de la sesión.
- Para que las geovallas funcionen correctamente, debes asegurarte de que tu aplicación no está utilizando todos los puntos de geovalla disponibles.

Consulta la tabla siguiente para conocer los términos comunes de geovalla y sus descripciones.

| Plazo | Descripción |
|---|---|
| Latitud y longitud | El centro geográfico de la geovalla. |
| Radio | El radio de la geo-valla en metros, medido desde el centro geográfico. Recomendamos configurar un radio mínimo de 100-150 metros para todos los geovallados. |
| Recuperación | Los usuarios reciben notificaciones desencadenadas por geovallas tras realizar transiciones de entrada o salida en geovallas individuales. Después de que se produzca una transición, hay un tiempo predefinido durante el cual ese usuario no puede volver a realizar la misma transición en esa geovalla individual. Este tiempo se denomina "enfriamiento" y está predefinido por Braze, y su finalidad principal es evitar peticiones de red innecesarias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Crea geovallas manualmente

### Paso 1: Crear un conjunto de geovallas

Para crear una geovalla, primero tendrás que crear un conjunto de geovallas.

1. Ve a **Audiencia** > **Ubicaciones** en el panel de Braze.
2. Selecciona **Crear conjunto de geovallas**.
3. En **Nombre del conjunto**, introduce un nombre para tu conjunto de geovallas.
4. (Opcional) Añade etiquetas para filtrar tu conjunto.

### Paso 2: Añade las geovallas

A continuación, puedes añadir geovallas a tu conjunto de geovallas.

1. Selecciona **Dibujar geovalla** para hacer clic y arrastrar el círculo sobre el mapa. Repítelo para añadir más geovallas a tu conjunto según sea necesario.
2. (Opcional) Puedes seleccionar **Editar** y sustituir la descripción de la geovalla por un nombre.
3. Selecciona **Guardar configuración de geovalla** para guardarla.

{% alert tip %}
Recomendamos crear geovallas con un radio de al menos 200 metros para una funcionalidad óptima. Para más información sobre las opciones configurables, consulta [Integraciones móviles](#mobile-integrations).
{% endalert %}

![Un conjunto de geovallas con dos geovallas "EastCoastGreaterNY" y "WesternRegion" con dos círculos en el mapa.]({% image_buster /assets/img/geofence_example.png %})

## Carga masiva de geovallas {#creating-geofence-sets-via-bulk-upload}

Las geocercas pueden cargarse en bloque como un objeto GeoJSON de tipo `FeatureCollection`. Cada geovalla es un tipo de geometría `Point` de la colección de características. Las propiedades de cada característica requieren una clave `radius`, y una clave opcional `name` para cada geovalla. 

Para subir tu GeoJSON, selecciona **Más** > **Subir GeoJSON**.

Cuando crees tus geovallas, ten en cuenta los siguientes detalles:

- El valor `coordinates` en el GeoJSON tiene el formato `[Longitude, Latitude]`.
- El radio máximo de geovalla que se puede cargar es de 10.000 metros (unos 100 kilómetros o 62 millas).

### Ejemplo

El siguiente ejemplo representa el GeoJSON correcto para especificar dos geovallas: una para la sede de Braze en Nueva York, y otra para la Estatua de la Libertad, al sur de Manhattan.

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

## Usar eventos de geovallas

Una vez configuradas las geovallas, puedes utilizarlas para mejorar y enriquecer la forma en que te comunicas con tus usuarios.

### Desencadenar campañas y lonas

Para utilizar datos de geocercas como parte de los activadores de campañas y Canvas, seleccione **Entrega basada en acciones** para el método de entrega. A continuación, añade una acción desencadenante de `Trigger a Geofence`. Por último, elige el conjunto de geovallas y los tipos de eventos de transición de geovalla para tu mensaje. También puede hacer avanzar a los usuarios a través de un lienzo mediante eventos de geovalla.

![Una campaña basada en acciones con un geovallado que se desencadenará cuando un usuario entre en los aeropuertos alemanes.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalización de mensajes

Para utilizar datos de geofence para personalizar un mensaje, puede utilizar la siguiente sintaxis de personalización de Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Actualizar los conjuntos de geovallas

Para los usuarios activos, el SDK de Braze solo solicitará geovallas una vez al día al iniciar la sesión. Esto significa que, si se realizan cambios en los conjuntos de geovallas después de iniciar la sesión, tendrás que esperar 24 horas desde el momento en que los conjuntos se desplieguen por primera vez para recibir el conjunto actualizado.

{% alert note %}
Si las geovallas no se cargan en el dispositivo localmente, el usuario no puede desencadenar el geovallado aunque entre en la zona.
{% endalert %}

## Integraciones móviles {#mobile-integrations}

### Requisitos multiplataforma

Las campañas desencadenadas por geovallas están disponibles en iOS y Android. Para admitir geovallas, debe existir lo siguiente:

1. Tu integración debe soportar notificaciones push en segundo plano.
2. Las geocercas Braze o la recopilación de ubicaciones deben estar activadas.
3. En los dispositivos con iOS versión 11 o superior, el usuario debe permitir siempre el acceso a la ubicación para que funcione la geolocalización.

{% alert important %}
A partir de la versión 3.6.0 del SDK de Braze, la recopilación de ubicaciones de Braze está desactivada predeterminadamente. Para comprobar que está habilitado en Android, confirma que `com_braze_enable_location_collection` está configurado como `true` en tu `braze.xml`.
{% endalert %}

Consulta la documentación de [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) o [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) para obtener más orientación en función de tu plataforma.

{% alert tip %}
También puedes aprovechar las geovallas con nuestros socios tecnológicos, como [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) y [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Preguntas más frecuentes

### ¿Cuál es la diferencia entre geovallas y seguimiento de ubicación?

En Braze, una geovalla es un concepto diferente del seguimiento de ubicación. Las geovallas se utilizan como desencadenantes de determinadas acciones. Una geovalla es un límite virtual establecido alrededor de una ubicación geográfica. Cuando un usuario entra o sale de este límite, puede desencadenar una acción específica, como el envío de un mensaje.

El seguimiento de la ubicación se utiliza para recopilar y almacenar los datos de ubicación más recientes de un usuario. Estos datos pueden utilizarse para segmentar a los usuarios en función del filtro `Most Recent Location`. Por ejemplo, puede utilizar el filtro `Most Recent Location` para dirigirse a una región específica de su audiencia, como enviar un mensaje a usuarios situados en Nueva York.

### ¿Qué grado de precisión tienen las geovallas Braze?

Las geocercas Braze utilizan una combinación de todos los proveedores de localización disponibles en un dispositivo para triangular la ubicación del usuario. Entre ellos se encuentran las torres Wi-Fi, GPS y de telefonía móvil.

La precisión típica se sitúa en el intervalo de 20-50 m y la precisión en el mejor de los casos estará en el intervalo de 5-10 m. En las zonas rurales, la precisión puede degradarse significativamente, pudiendo llegar a varios kilómetros. Braze recomienda crear geocercas con radios mayores en las zonas rurales.

Para más información sobre la precisión de las geocercas, consulte la documentación de [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) e [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### ¿Cómo afectan las geocercas a la duración de la batería?

Nuestra solución de geovallado utiliza el servicio nativo del sistema de geovallas en iOS y Android y está ajustada para compensar de forma inteligente precisión y potencia, ahorrando batería y mejorando el rendimiento a medida que mejora el servicio subyacente.

### ¿Cuándo están activas las geovallas?

Las geocercas Braze funcionan a cualquier hora del día, incluso cuando la aplicación está cerrada. Se activan en cuanto se definen y se cargan en el panel Braze. Sin embargo, las geovallas no pueden funcionar si el usuario ha desactivado el seguimiento de la ubicación.

Para que las geocercas funcionen, los usuarios deben tener activados los servicios de localización en su dispositivo y deben haber concedido permiso a tu aplicación para acceder a su ubicación. Si un usuario ha desactivado el seguimiento de su ubicación, tu aplicación no podrá detectar cuándo entra o sale de una geo-valla.

### ¿Se almacenan los datos de la geovalla en los perfiles de usuario?

No, Braze no almacena datos de geovallas en los perfiles de usuario. Las geovallas son controladas por los servicios de ubicación de Apple y Google, y Braze solo recibe una notificación cuando un usuario desencadena una geovalla. En ese momento, procesamos cualquier campaña desencadenante asociada.

### ¿Puedo configurar una geovalla dentro de una geovalla?

Como práctica recomendada, evite configurar geocercas una dentro de otra, ya que esto puede causar problemas con la activación de las notificaciones.

