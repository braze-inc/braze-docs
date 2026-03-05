{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Setting the last known location

To manually set the last known location for a user, use the `setLastKnownLocation` method. This is useful if you collect location data outside of the Braze SDK.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- On Android, `latitude` and `longitude` are required. `altitude`, `horizontalAccuracy`, and `verticalAccuracy` are optional.
- On iOS, `latitude`, `longitude`, and `horizontalAccuracy` are required. `altitude` and `verticalAccuracy` are optional.

For cross-platform compatibility, provide `latitude`, `longitude`, and `horizontalAccuracy` at a minimum.

## Setting a custom location attribute

To set a custom location attribute on a user profile, use the `setLocationCustomAttribute` method.

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## Requesting location initialization (Android only)

Call `requestLocationInitialization` after a user grants location permissions to initialize Braze location features on Android. This method is not supported on iOS and is not required for iOS geofence or location features.

```javascript
Braze.requestLocationInitialization();
```

## Geofences

Geofences are supported on both iOS and Android. By default, the Braze SDK can automatically request and monitor geofences when location is available. You can rely on this automatic configuration for most integrations.

### Manually requesting geofences

To manually request a geofence update for a specific GPS coordinate, use `requestGeofences`. This is available on both iOS and Android. If you use this method, disable automatic geofence requests in your native configuration so the SDK does not overwrite your manual requests.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
