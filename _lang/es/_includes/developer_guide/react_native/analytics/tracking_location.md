{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configuración de la última ubicación conocida

Para establecer manualmente la última ubicación conocida de un usuario, utiliza el`setLastKnownLocation`método . Esto resulta útil si recopilas datos de ubicación fuera del SDK de Braze.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- En Android,`latitude`  y`longitude`  son obligatorios. `altitude`, `horizontalAccuracy`, y`verticalAccuracy`  son opcionales.
- En iOS, `latitude`,`longitude`  y`horizontalAccuracy`  son obligatorios.`altitude`  y`verticalAccuracy`  son opcionales.

Para garantizar la compatibilidad entre plataformas, proporciona como `horizontalAccuracy`mínimo`latitude` , `longitude`, y .

## Configuración de un atributo de ubicación personalizado

Para establecer un atributo de ubicación personalizado en un perfil de usuario, utiliza el`setLocationCustomAttribute`método .

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## Solicitud de inicialización de la ubicación (solo Android)

Llama`requestLocationInitialization`después de que el usuario conceda los permisos de ubicación para inicializar las características de ubicación de Braze en Android. Este método no es compatible con iOS y no es necesario para las características de geovalla o ubicación de iOS.

```javascript
Braze.requestLocationInitialization();
```

## Geovallas

Las geovallas son compatibles tanto con iOS como con Android. De forma predeterminada, el SDK de Braze puede solicitar y supervisar automáticamente las geovallas cuando la ubicación está disponible. Puedes confiar en esta configuración automática para la mayoría de las integraciones.

### Solicitar manual de geovallas

Para solicitar manualmente una actualización de la geovalla para una coordenada GPS específica, utiliza `requestGeofences`. Está disponible tanto para iOS como para Android. Si utilizas este método, desactiva las solicitudes automáticas de geovallas en tu configuración nativa para que el SDK no sobrescriba tus solicitudes manuales.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
