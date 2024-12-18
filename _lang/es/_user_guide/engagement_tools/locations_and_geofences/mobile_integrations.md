---
nav_title: Integraciones móviles
article_title: Integraciones móviles de Geofence
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre las integraciones móviles necesarias para utilizar geovallas."
tool: Location

---

# Integraciones móviles

> Este artículo de referencia cubre las integraciones móviles necesarias para utilizar geovallas.

## Requisitos multiplataforma

Las campañas desencadenadas por geovallas están disponibles en iOS y Android. Para admitir geovallas, debe existir lo siguiente:

1. Tu integración debe soportar notificaciones push en segundo plano.
2. Las geocercas Braze o la recopilación de ubicaciones deben estar activadas.
3. En los dispositivos con iOS versión 11 o superior, el usuario debe permitir siempre el acceso a la ubicación para que funcione la geolocalización.

{% alert important %}
A partir de la versión 3.6.0 del SDK de Braze, la recopilación de ubicaciones de Braze está desactivada predeterminadamente. Para comprobar que está habilitado en Android, confirma que `com_braze_enable_location_collection` está configurado como `true` en tu `braze.xml`.
{% endalert %}

## Configuración de geovallas

### Latitud y longitud

El centro geográfico de la geovalla.

### Radio

El radio de la geo-valla en metros, medido desde el centro geográfico. Recomendamos configurar un radio mínimo de 100-150 metros para todos los geovallados.

Consulta estas guías para obtener más orientación en función de tu plataforma:
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### Recuperación

Los usuarios reciben notificaciones desencadenadas por geovallas tras realizar transiciones de entrada o salida en geovallas individuales. Después de que se produzca una transición, hay un tiempo predefinido durante el cual ese usuario no puede volver a realizar la misma transición en esa geovalla individual. Este tiempo se denomina "enfriamiento" y está predefinido por Braze. Su objetivo principal es evitar solicitudes de red innecesarias.

### Socios tecnológicos

También puedes aprovechar las geovallas con algunos de nuestros socios, por ejemplo: 

- [Radar][12]
- [Foursquare][13]

## Preguntas más frecuentes

Visita [Preguntas frecuentes sobre geovallas][5] para obtener respuestas a las preguntas más frecuentes sobre geovallas.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

