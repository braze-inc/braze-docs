## Logging the current location

To get a user's current location, use the geolocation API's [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) method. This will immediately prompt the user to allow or disallow tracking (unless they've already done so).

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

Now when data is sent to Braze, the SDK can automatically detect the user's country using their IP address. For more information, see [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Continuously tracking the location

To continuously track a user's location during a page load, use the geolocation API's [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) method. Calling this method will immediately prompt the user to allow or disallow tracking (unless they've already done so).

If they opt-in, a success callback will now be invoked every time their location is updated.

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

{% alert important %}
To learn how to disable continuous tracking, refer to the [Mozilla developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
{% endalert %}
