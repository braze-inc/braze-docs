{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Desactivación del seguimiento de datos

Para desactivar la recopilación de datos, utiliza el`disableSDK`método . Después de llamar a este método, el SDK de Braze deja de enviar datos a los servidores de Braze.

```javascript
Braze.disableSDK();
```

## Reanudación del seguimiento de datos

Para reanudar la recopilación de datos después de desactivarla, utiliza el`enableSDK`método .

```javascript
Braze.enableSDK();
```

## Borrar datos

Para eliminar todos los datos del SDK de Braze almacenados localmente en el dispositivo, utiliza el`wipeData`método . Después de llamar a este método, el SDK se desactiva y debe volver a habilitarse con `enableSDK`.

```javascript
Braze.wipeData();
```

## Borrar datos

Para solicitar un envío inmediato de cualquier dato pendiente a los servidores de Braze, utiliza `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Configuración del seguimiento de anuncios habilitado

Para informar a Braze si el seguimiento de anuncios está habilitado para este dispositivo, utiliza el`setAdTrackingEnabled`método . El SDK no recopila automáticamente estos datos.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

El segundo parámetro es el ID de publicidad de Google y solo se utiliza en Android.

## Actualización de la lista de propiedades de seguimiento (solo iOS)

Para actualizar la lista de tipos de datos declarados para el seguimiento, utiliza `updateTrackingPropertyAllowList`. Esto no funciona en Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Para obtener más información, consulta el [Manifiesto de privacidad]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
