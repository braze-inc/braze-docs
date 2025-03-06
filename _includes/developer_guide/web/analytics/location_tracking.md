## Enabling location tracking

To set a user's current location, use the [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) method of the geolocation API and log the location data to Braze:

```javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

Calling `navigator.geolocation.getCurrentPosition()` will immediately request permission from the user unless they have already granted or denied permission. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) for information on setting the user's last known location.

## Logging a single location

When the Web SDK sends data to Braze servers, the user's country will automatically be detected from their IP Address if it has not been manually set by your application.

### Continuous tracking

If you'd like to continuously track a user's location during a page load, use the [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) method of the Geolocation API. This method will invoke the success callback each time the user's location is updated:

```javascript
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

Calling `navigator.geolocation.watchPosition()` will immediately request permission from the user unless they have already granted or denied permission. See the [Mozilla developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) for information on configuring and stopping the location tracking.
