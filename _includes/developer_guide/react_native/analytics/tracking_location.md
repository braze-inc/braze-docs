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

## Requesting location initialization on Android

Call `requestLocationInitialization` after a user grants location permissions to initialize Braze location features. This is a no-op on iOS.

```javascript
Braze.requestLocationInitialization();
```

## Requesting geofences on Android

To manually request a geofence update for a specific GPS coordinate, use `requestGeofences`. Automatic geofence requests must be disabled for this to work. This is a no-op on iOS.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
